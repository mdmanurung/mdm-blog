"""Check generated pages, local links, SEO, visibility and unsafe legacy content."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json
from content import ROOT, load
class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]; self.h1=0; self.description=False; self.ids=set(); self.title=False
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='h1': self.h1+=1
        if tag=='title': self.title=True
        if tag=='meta' and a.get('name')=='description' and a.get('content'): self.description=True
        if a.get('id'): self.ids.add(a['id'])
        if tag in {'a','link','script','img'}:
            value=a.get('href') or a.get('src')
            if value: self.links.append(value)
root=ROOT/'_preview'; errors=[]; pages={}
for path in root.rglob('*.html'):
    page=Page(); text=path.read_text(); page.feed(text); pages[path]=page
    for forbidden in ['Nora Jones','Spacely Sprockets','themockup.blog/index.xml','MikhaelManurung/mdm-distill']:
        if forbidden in text: errors.append(f'{path}: forbidden legacy text: {forbidden}')
    if 'http-equiv="refresh"' not in text:
        if page.h1!=1: errors.append(f'{path}: expected one h1, got {page.h1}')
        if not page.description or not page.title: errors.append(f'{path}: missing SEO metadata')
for path,page in pages.items():
    for href in page.links:
        parts=urlsplit(href)
        if parts.scheme or parts.netloc: continue
        target=(root/parts.path.lstrip('/')) if parts.path.startswith('/') else (path.parent/unquote(parts.path))
        if not parts.path: target=path
        if target.is_dir(): target=target/'index.html'
        if not target.exists(): errors.append(f'{path.relative_to(root)}: broken local URL {href}')
        elif parts.fragment and target in pages and unquote(parts.fragment) not in pages[target].ids:
            errors.append(f'{path.relative_to(root)}: missing anchor {href}')
for route in ['index.html','research/index.html','publications/index.html','software/index.html','writing/index.html','about/index.html','posts.html','projects.html','about.html','posts/welcome/index.html','posts.xml','writing/index.xml','search.json','sitemap.xml','robots.txt']:
    if not (root/route).exists(): errors.append('Missing '+route)
all_text='\n'.join(x.read_text() for x in root.rglob('*.html'))
public_titles={x.get('title') for rows in load().values() for x in rows if x.get('visibility')=='public'}
for kind,rows in load().items():
    for row in rows:
        if row['visibility']=='draft' and row.get('title') and row['title'] not in public_titles and row['title'] in all_text: errors.append('Draft leaked: '+row['id'])
search=json.loads((root/'search.json').read_text())
if len(search)<6: errors.append('Search index missing top-level pages')
if errors: raise SystemExit('\n'.join(errors))
print(f'OK: {len(pages)} HTML pages, local links/anchors, redirects, SEO, search and visibility')
