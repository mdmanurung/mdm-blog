"""Discover OpenAlex candidates by verified persistent identity; never publish."""
import os
import re
from urllib.parse import urlencode
from content import ROOT, read_yaml, norm_doi, records
from sync_common import json_fetch, write_cache, now

def discover(profile, fetcher=json_fetch):
    author_ids=list(profile.get('openalex_author_ids') or [])
    orcid=profile.get('orcid')
    if orcid:
        if not re.fullmatch(r'\d{4}-\d{4}-\d{4}-\d{3}[\dX]',orcid): raise ValueError('Invalid ORCID syntax')
        author=fetcher('https://api.openalex.org/authors/https://orcid.org/'+orcid)
        author_ids.append(author['id'].rsplit('/',1)[-1])
    if not author_ids: return None
    for author in author_ids:
        if not re.fullmatch(r'A\d+',author): raise ValueError('Invalid OpenAlex author ID')
    works={}
    for author in sorted(set(author_ids)):
        cursor='*'
        seen=set()
        while cursor:
            if cursor in seen: raise ValueError('Provider pagination loop')
            seen.add(cursor)
            params={'filter':'authorships.author.id:'+author,'per-page':200,'cursor':cursor}
            if os.getenv('OPENALEX_API_KEY'): params['api_key']=os.environ['OPENALEX_API_KEY']
            page=fetcher('https://api.openalex.org/works?'+urlencode(params))
            if not isinstance(page.get('results'),list): raise ValueError('Invalid OpenAlex results')
            for work in page['results']:
                doi=norm_doi(work['doi']) if work.get('doi') else None
                key='doi:'+doi if doi else work['id']
                if doi and not re.fullmatch(r'10\.\d{4,9}/\S+',doi): raise ValueError('Invalid candidate DOI')
                works[key]={'id':key,'doi':doi,'title':work.get('display_name'),'year':work.get('publication_year'),'authors':[a['author']['display_name'] for a in work.get('authorships',[])], 'venue':((work.get('primary_location') or {}).get('source') or {}).get('display_name'),'provider_type':work.get('type'),'related_work_ids':work.get('related_works',[]),'status':'other','visibility':'draft','provenance':{'discovered_from':work['id'],'checked_at':now()}}
            cursor=page.get('meta',{}).get('next_cursor') if page['results'] else None
    return sorted(works.values(),key=lambda x:x['id'])

def main():
    profile=read_yaml(ROOT/'content/profile.yml')
    result=discover(profile)
    if result is None:
        print('SKIP publications: verified ORCID/OpenAlex identity not configured; cache retained')
        return
    decisions=records(ROOT/'content/decisions.yml')
    rejected={x['id'] for x in decisions if x.get('decision')=='rejected'}
    approved={x['id'] for x in records(ROOT/'content/publications.yml')}
    result=[x for x in result if x['id'] not in rejected and x['id'] not in approved]
    write_cache('openalex_candidates.yml',result)
    print(f'Publications: {len(result)} unreviewed candidates; curated records unchanged')

if __name__=='__main__': main()
