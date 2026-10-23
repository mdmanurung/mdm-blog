"""Refresh optional metadata for the explicit project allowlist, never narratives."""
import os
from content import ROOT, records
from sync_common import json_fetch, write_cache, now

def snapshot(rows, fetcher=json_fetch):
    result=[]
    for row in rows:
        repo=row['repository']
        response=fetcher('https://api.github.com/repos/'+repo,token=os.getenv('GITHUB_TOKEN'))
        if response.get('private') or response.get('full_name','').lower()!=repo.lower():
            raise ValueError('Private, inaccessible or renamed repository requires review: '+repo)
        result.append({'repository':repo,'language':response.get('language'),'archived':response.get('archived'), 'fork':response.get('fork'), 'homepage':response.get('homepage'), 'checked_at':now()})
    return result

if __name__=='__main__':
    rows=snapshot(records(ROOT/'content/projects.yml'))
    write_cache('github_snapshot.yml',rows)
    print(f'GitHub: {len(rows)} allowlisted snapshots; curated fields unchanged')
