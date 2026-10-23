# Generate escaped fragments from reviewed records only; no network.
from html import escape
from pathlib import Path
from content import ROOT, load, native_posts, validate

E = lambda value: escape(str(value), quote=True)

def link(href, label):
    return f'<a href="{E(href)}">{E(label)}</a>'

def related(row, topics):
    return '<div class="topic-links">' + ' · '.join(link('/research/#'+t,topics[t]['name']) for t in row.get('topics',[])) + '</div>'

def publication(row, topics):
    links = [link(row['paper_url'],'Paper')]
    if row.get('oa_url'): links.append(link(row['oa_url'],'Open access'))
    for field,label in [('code_urls','Code'),('data_urls','Data')]:
        links += [link(u,label) for u in row.get(field,[])]
    abstract = '<details><summary>Abstract</summary><p>'+E(row['abstract'])+'</p></details>' if row.get('abstract') else ''
    return f'''<article class="record" data-record data-year="{row['year']}" data-topic="{E('|'.join(row['topics']))}">
<h3>{link(row['paper_url'],row['title'])}</h3><p class="meta">{E(', '.join(row['authors']))}<br>{E(row['venue'])} · {row['year']} <span class="badge-label">{E(row['status'])}</span></p>
{('<p>'+E(row['significance'])+'</p>') if row.get('significance') else ''}{abstract}<div class="record-links">{' '.join(links)}</div>{related(row,topics)}</article>'''

def project(row, topics):
    links = [link('/software/'+row['id']+'/', 'Overview'),link('https://github.com/'+row['repository'],'Repository')]
    if row.get('docs_url'): links.append(link(row['docs_url'],'Documentation'))
    return f'''<article class="software-card" data-record data-topic="{E('|'.join(row['topics']))}" data-maturity="{E(row['maturity'])}">
<span class="badge-label">{E(row['maturity'])}</span><h3>{link('/software/'+row['id']+'/',row['title'])}</h3><p>{E(row['summary'])}</p><p class="meta">For {E(row['audience'])}</p><div class="record-links">{' '.join(links)}</div>{related(row,topics)}</article>'''

def writing(row,topics):
    source = 'Substack' if row['source'] == 'substack' else 'On this site'
    return f'''<article class="record" data-record data-source="{E(row['source'])}" data-topic="{E('|'.join(row['topics']))}"><p class="meta">{E(row['date'])} · <span class="badge-label">{source}</span></p><h3>{link(row['canonical_url'],row['title'])}</h3><p>{E(row.get('description',''))}</p>{related(row,topics)}</article>'''

def controls(kind,rows,topics):
    facets = [('topic','Research topic',[(t,topics[t]['name']) for t in topics])]
    if kind == 'publications': facets += [('year','Year',[(str(y),str(y)) for y in sorted({x['year'] for x in rows},reverse=True)])]
    if kind == 'projects': facets += [('maturity','Development status',[(v,v.title()) for v in sorted({x['maturity'] for x in rows})])]
    if kind == 'writing': facets += [('source','Source',[('native','On this site'),('substack','Substack')])]
    html = f'<div class="controls"><label>Search {kind}<input type="search" data-filter="query" aria-label="Search {kind}" placeholder="Search titles and descriptions"></label>'
    for field,label,options in facets:
        html += f'<label>{label}<select data-filter="{field}"><option value="">All</option>'+''.join(f'<option value="{E(v)}">{E(n)}</option>' for v,n in options)+'</select></label>'
    return html+'</div>'

def catalog(kind,rows,topics,render):
    if not rows:
        return '<p class="empty-state">The publication catalogue is being curated. Verified records will appear here after review.</p>' if kind == 'publications' else '<p class="empty-state">No writing has been published here yet. Research notes and links to external essays will appear as they are added.</p>'
    return '<section data-catalog aria-label="'+kind+' directory">'+controls(kind,rows,topics)+'<p class="meta" data-count aria-live="polite">'+str(len(rows))+' results</p><div class="'+('software-grid' if kind=='projects' else 'records')+'">'+''.join(render(x,topics) for x in rows)+'</div><p class="empty-state" data-empty hidden>No matching results. Try another search or clear the filters.</p></section>'

def generate(root=ROOT):
    data = load(root)
    posts = native_posts(root)
    errors = validate(data,posts)
    if errors: raise ValueError('\n'.join(errors))
    data = {k:[x for x in rows if x['visibility']=='public'] for k,rows in data.items()}
    topics = {x['id']:x for x in data['research']}
    papers = sorted(data['publications'],key=lambda x:(-x['year'],x['title']))
    projects = sorted(data['projects'],key=lambda x:(not x.get('featured',False),x.get('feature_order',100),x['title'].lower()))
    writings = sorted(data['substack']+posts,key=lambda x:str(x['date']),reverse=True)
    out = root/'_generated'; out.mkdir(exist_ok=True)
    # Remove stale fragments after a record is removed or made draft.
    for path in out.glob('*.html'): path.unlink()
    def put(name,text): (out/(name+'.html')).write_text(text+'\n')
    put('themes','<div class="theme-grid">'+''.join(f'<article class="theme-card"><span class="eyebrow">0{i+1}</span><h3>{link("/research/#"+x["id"],x["name"])}</h3><p>{E(x["question"])}</p></article>' for i,x in enumerate(topics.values()))+'</div>')
    put('publications',catalog('publications',papers,topics,publication))
    put('projects',catalog('projects',projects,topics,project))
    put('writing',catalog('writing',writings,topics,writing))
    featured = [p for p in papers if p.get('featured')][:3]
    put('featured-publications',('<h2>Selected research</h2>'+''.join(publication(x,topics) for x in featured)) if featured else '')
    put('featured-projects','<div class="software-grid">'+''.join(project(x,topics) for x in projects if x.get('featured'))+'</div>')
    put('latest-writing',('<h2>Writing & ideas</h2>'+''.join(writing(x,topics) for x in writings[:3])+link('/writing/','All writing →')) if writings else '')
    research = ''
    for t in topics.values():
        research += f'<section id="{t["id"]}"><h2>{E(t["name"])}</h2><p><strong>{E(t["question"])}</strong></p><p>{E(t.get("description",""))}</p>'
        for rows,render in [(papers,publication),(projects,project),(writings,writing)]:
            research += ''.join(render(x,topics) for x in rows if t['id'] in x['topics'])
        research += '</section>'
    put('research',research)
    for row in projects:
        text = f'<p>{E(row["summary"])}</p><h2>Who it is for</h2><p>{E(row["audience"])}</p><p><span class="badge-label">{E(row["maturity"])}</span> Status is a curated assessment; consult the repository before use.</p><h2>Installation and examples</h2><p>Use the repository README for current installation instructions, examples and limitations.</p><p>{link("https://github.com/"+row["repository"],"Open repository →")}</p>'
        if row.get('docs_url'): text += '<p>'+link(row['docs_url'],'Documentation →')+'</p>'
        text += related(row,topics)
        for p in papers:
            if p['id'] in row.get('paper_ids',[]): text += publication(p,topics)
        put('project-'+row['id'],text)

if __name__ == '__main__': generate()
