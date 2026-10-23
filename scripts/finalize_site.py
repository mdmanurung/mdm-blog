from pathlib import Path
from html import escape
import os
import xml.etree.ElementTree as ET
from content import ROOT, native_posts
root = ROOT/'_preview'
for source,target in {'about.html':'/about/','posts.html':'/writing/','projects.html':'/software/','posts/welcome/index.html':'/writing/','posts/welcome.html':'/writing/'}.items():
    path=root/source; path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Page moved</title><meta http-equiv="refresh" content="0;url={escape(target)}"><meta name="robots" content="noindex"></head><body><h1>Page moved</h1><a href="{escape(target)}">Continue to the new page</a></body></html>')
staging=os.getenv('MDM_STAGING','1')=='1'
base=os.getenv('MDM_SITE_URL','https://mdmanurung.rbind.io').rstrip('/')
(root/'robots.txt').write_text('User-agent: *\n'+('Disallow: /\n' if staging else 'Allow: /\nSitemap: '+base+'/sitemap.xml\n'))
rss=ET.Element('rss',version='2.0'); channel=ET.SubElement(rss,'channel')
for key,value in [('title','Mikhael Manurung — Writing'),('link',base+'/writing/'),('description','Original research notes and technical writing.')]: ET.SubElement(channel,key).text=value
for post in native_posts():
    if post.get('visibility')!='public': continue
    item=ET.SubElement(channel,'item')
    for key,value in [('title',post['title']),('link',base+post['canonical_url']),('guid',base+post['canonical_url']),('description',post.get('description',''))]: ET.SubElement(item,key).text=value
    from datetime import date, datetime, time, timezone
    from email.utils import format_datetime
    ET.SubElement(item,'pubDate').text=format_datetime(datetime.combine(date.fromisoformat(str(post['date'])),time(),timezone.utc))
feed=ET.tostring(rss,encoding='utf-8',xml_declaration=True)
(root/'writing/index.xml').write_bytes(feed)
(root/'posts.xml').write_bytes(feed)

# Put the skip link before navigation, independent of Quarto's include placement.
import re
skip = (ROOT/'assets/skip.html').read_text().strip()
for page in root.rglob('*.html'):
    text=page.read_text()
    if 'quarto-document-content' in text:
        text=text.replace(skip,'')
        text=re.sub(r'(<body[^>]*>)',lambda match:match.group(1)+'\n'+skip,text,count=1)
        page.write_text(text)
