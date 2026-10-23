"""Metadata-only RSS/CSV candidate import. Curated archives remain authoritative."""
import argparse
import csv
from datetime import timezone
from email.utils import parsedate_to_datetime
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import urlsplit
import xml.etree.ElementTree as ET
from content import ROOT, canonical, read_yaml, records, url, iso_date
from sync_common import fetch, now, write_cache

class PlainText(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True); self.parts=[]; self.blocked=0
    def handle_starttag(self,tag,attrs):
        if tag in {'script','style'}: self.blocked+=1
        if tag in {'p','br','div'}: self.parts.append(' ')
    def handle_endtag(self,tag):
        if tag in {'script','style'}: self.blocked=max(0,self.blocked-1)
        if tag in {'p','div'}: self.parts.append(' ')
    def handle_data(self,text):
        if not self.blocked: self.parts.append(text)

def plain(text):
    parser=PlainText(); parser.feed(text or '')
    return re.sub(r'\s+',' ',''.join(parser.parts)).strip()[:280]

def candidate(title,address,when,description,origins):
    if not url(address) or urlsplit(address).scheme+'://'+urlsplit(address).netloc not in origins:
        raise ValueError('Article URL is outside the configured publication origins')
    address=canonical(address)
    if not title or not when: raise ValueError('Missing article title/date')
    if not iso_date(when):
        when=parsedate_to_datetime(when).astimezone(timezone.utc).date().isoformat()
    return {'id':'substack:'+address.rsplit('/',1)[-1], 'title':plain(title),'canonical_url':address,'date':str(when),'description':plain(description),'source':'substack','topics':[],'visibility':'draft','first_seen':now(),'last_seen':now()}

def parse_feed(body,origins):
    if b'<!DOCTYPE' in body.upper() or b'<!ENTITY' in body.upper(): raise ValueError('DTD/entity declarations are not supported')
    root=ET.fromstring(body)
    if root.tag!='rss' or root.find('channel') is None: raise ValueError('Expected an RSS channel')
    rows=[]
    for item in root.findall('./channel/item'):
        rows.append(candidate(item.findtext('title'),item.findtext('link'),item.findtext('pubDate'),item.findtext('description'),origins))
    return rows

def merge_candidates(existing,incoming,curated):
    # Owner edits, hidden/draft flags and old entries always survive refreshes.
    accepted={canonical(x['canonical_url']) for x in curated}
    result={canonical(x['canonical_url']):dict(x) for x in existing}
    for row in incoming:
        key=canonical(row['canonical_url'])
        if key in accepted: continue
        if key in result:
            original=result[key]
            row=dict(row,first_seen=original.get('first_seen',row['first_seen']))
            for field in ['topics','visibility','featured','hidden']:
                if field in original: row[field]=original[field]
        result[key]=row
    return sorted(result.values(),key=lambda x:(str(x['date']),x['canonical_url']),reverse=True)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--csv',type=Path,help='Normalized metadata export: title, canonical_url, date, description; no body HTML')
    args=parser.parse_args()
    profile=read_yaml(ROOT/'content/profile.yml')
    feed=profile.get('substack_feed'); origins=profile.get('substack_origins') or []
    if not origins or (not feed and not args.csv):
        print('SKIP Substack: verified feed/origins not configured; archive retained'); return
    if args.csv:
        with args.csv.open(newline='') as stream:
            incoming=[candidate(x['title'],x['canonical_url'],x['date'],x.get('description',''),origins) for x in csv.DictReader(stream)]
    else:
        if not url(feed) or urlsplit(feed).scheme+'://'+urlsplit(feed).netloc not in origins: raise ValueError('Feed outside approved origins')
        incoming=parse_feed(fetch(feed),origins)
    rows=merge_candidates(read_yaml(ROOT/'cache/substack_feed.yml',[]),incoming,records(ROOT/'content/substack.yml'))
    write_cache('substack_feed.yml',rows)
    print(f'Substack: {len(incoming)} incoming, {len(rows)} retained candidates; curated archive unchanged')

if __name__=='__main__': main()
