"""Content contracts shared by validation, rendering and candidate ingestion."""
from __future__ import annotations
from datetime import date
from pathlib import Path
import re
from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode
import yaml

ROOT = Path(__file__).resolve().parents[1]
KINDS = ('research', 'publications', 'projects', 'substack', 'news')

def read_yaml(path, default=None):
    if not Path(path).exists() and default is not None:
        return default
    return yaml.safe_load(Path(path).read_text(encoding='utf-8'))

def records(path):
    data = read_yaml(path)
    if not isinstance(data, list) or any(not isinstance(x, dict) for x in data):
        raise ValueError(f'{path}: expected a list of mappings')
    return data

def load(root=ROOT):
    return {kind: records(root / 'content' / f'{kind}.yml') for kind in KINDS}

def url(value):
    if not isinstance(value, str):
        return False
    try:
        p = urlsplit(value)
        return p.scheme == 'https' and bool(p.hostname) and not p.username and not p.password and not any(c.isspace() for c in value)
    except ValueError:
        return False

def canonical(value):
    p = urlsplit(value)
    query = [(k,v) for k,v in parse_qsl(p.query) if not k.startswith('utm_') and k not in {'fbclid','gclid'}]
    return urlunsplit((p.scheme.lower(), p.netloc.lower(), p.path.rstrip('/'), urlencode(query), ''))

def norm_doi(value):
    return re.sub(r'^https?://(?:dx\.)?doi\.org/', '', str(value).strip(), flags=re.I).lower()

def iso_date(value):
    try:
        return date.fromisoformat(str(value)).isoformat()
    except (ValueError, TypeError):
        return None

def native_posts(root=ROOT):
    rows = []
    for path in sorted((root/'writing/posts').glob('*/index.qmd')):
        text = path.read_text()
        if not text.startswith('---\n') or '\n---\n' not in text[4:]:
            raise ValueError(f'{path}: missing YAML front matter')
        meta = yaml.safe_load(text.split('---',2)[1])
        meta['path'] = '/' + str(path.relative_to(root).with_suffix('.html'))
        meta['canonical_url'] = meta['path'].replace('/index.html','/')
        meta['source'] = 'native'
        rows.append(meta)
    return rows

def validate(data, posts=()):
    errors = []
    def fail(anchor, message): errors.append(f'{anchor}: {message}')
    ids = {}
    for kind, rows in data.items():
        seen = set()
        for i,row in enumerate(rows):
            a = f'{kind}[{i+1}]'
            rid = row.get('id')
            if not isinstance(rid,str) or not rid.strip(): fail(a,'missing id')
            elif rid in seen: fail(a,'duplicate id')
            else: seen.add(rid)
            if row.get('visibility') not in {'public','draft'}: fail(a,'visibility must be public/draft')
        ids[kind] = seen
    topics = ids.get('research',set())
    public_topics = {x['id'] for x in data['research'] if x.get('visibility') == 'public'}
    public_papers = {x['id'] for x in data['publications'] if x.get('visibility') == 'public'}
    dois, urls, repos = set(), set(), set()
    all_rows = [(k,x) for k,rows in data.items() for x in rows] + [('native',p) for p in posts]
    for kind,row in all_rows:
        a = f'{kind}:{row.get("id", "?")}'
        public = row.get('visibility') == 'public'
        if kind != 'research':
            ts = row.get('topics',[])
            if not isinstance(ts,list) or any(not isinstance(t,str) or t not in topics for t in ts): fail(a,'unknown topics')
            elif public and (not ts or any(t not in public_topics for t in ts)): fail(a,'public output requires public topics')
            if not isinstance(row.get('title'),str) or not row['title'].strip(): fail(a,'missing title')
        if public and (row.get('synthetic') or 'example' in str(row.get('doi','')).lower()): fail(a,'synthetic records cannot be public')
        if kind == 'research':
            if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',str(row.get('id',''))): fail(a,'invalid topic slug')
            if not row.get('name') or not row.get('question'): fail(a,'missing name/question')
        elif kind == 'publications':
            doi = row.get('doi')
            if doi:
                normalized = norm_doi(doi)
                if not re.fullmatch(r'10\.\d{4,9}/\S+',normalized): fail(a,'invalid DOI')
                if normalized != doi: fail(a,'DOI must be normalized')
                if normalized in dois: fail(a,'duplicate DOI')
                dois.add(normalized)
                if row.get('id') != 'doi:'+normalized: fail(a,'id must match DOI')
                if public and row.get('paper_url') != 'https://doi.org/'+normalized: fail(a,'paper URL must match DOI')
            elif public and not str(row.get('id','')).startswith('local:'): fail(a,'DOI-less id requires local: prefix')
            if type(row.get('year')) is not int or not 1900 <= row['year'] <= 2100: fail(a,'invalid year')
            if row.get('status') not in {'peer-reviewed','preprint','accepted','other'}: fail(a,'invalid publication status')
            if public:
                if not row.get('venue') or not isinstance(row.get('authors'),list) or not row['authors']: fail(a,'missing venue/authors')
                if not url(row.get('paper_url')): fail(a,'invalid paper URL')
                if not row.get('provenance',{}).get('confirmed_by'): fail(a,'approval provenance required')
            if row.get('version_of') and row['version_of'] not in ids['publications']: fail(a,'unknown version_of')
            for name in ['oa_url']:
                if row.get(name) and not url(row[name]): fail(a,'invalid '+name)
            for name in ['code_urls','data_urls']:
                if not isinstance(row.get(name,[]),list) or any(not url(u) for u in row.get(name,[])): fail(a,'invalid '+name)
        elif kind == 'projects':
            repo = row.get('repository','')
            if not isinstance(repo,str) or not re.fullmatch(r'[\w.-]+/[\w.-]+',repo): fail(a,'invalid repository')
            if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',str(row.get('id',''))): fail(a,'invalid project slug')
            repo = str(repo)
            if repo.lower() in repos: fail(a,'duplicate repository')
            repos.add(repo.lower())
            if row.get('maturity') not in {'stable','active','experimental','archived'}: fail(a,'invalid maturity')
            if public and (not row.get('summary') or not row.get('audience')): fail(a,'missing summary/audience')
            refs = row.get('paper_ids',[])
            if not isinstance(refs,list) or any(x not in ids['publications'] for x in refs): fail(a,'unknown paper_ids')
            elif public and any(x not in public_papers for x in refs): fail(a,'public project references draft paper')
            if row.get('docs_url') and not url(row['docs_url']): fail(a,'invalid docs URL')
        elif kind == 'news':
            if not iso_date(row.get('date')): fail(a,'invalid news date')
            address=row.get('url','')
            if address and not address.startswith('/') and not url(address): fail(a,'invalid news URL')
            for item in row.get('links',[]):
                if not isinstance(item,dict) or not item.get('label') or not url(item.get('url')): fail(a,'invalid news source link')
        elif kind in {'substack','native'}:
            if not iso_date(row.get('date')): fail(a,'invalid date')
            if kind == 'substack':
                u = row.get('canonical_url')
                if not url(u): fail(a,'invalid canonical URL')
                else:
                    key = canonical(u)
                    if u != key: fail(a,'canonical URL contains tracking/trailing slash')
                    if key in urls: fail(a,'duplicate canonical URL')
                    urls.add(key)
                if len(str(row.get('description',''))) > 280: fail(a,'description exceeds 280 characters')
            if kind == 'native' and row.get('visibility') != 'public': fail(a,'draft native posts must live outside render tree in drafts/')
    return errors
