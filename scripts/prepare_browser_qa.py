"""Create temporary browser QA frames and synthetic interactions; never deploy _qa/."""
from pathlib import Path
from content import ROOT
from render_content import catalog
q=ROOT/'_preview/_qa';q.mkdir(exist_ok=True)
for name,route in [('home','/'),('research','/research/'),('publications','/publications/'),('software','/software/'),('writing','/writing/'),('about','/about/')]:
    for width in [1440,390,320]:
        (q/f'{name}-{width}.html').write_text(f'<!doctype html><html><head><title>Internal QA</title><meta name="robots" content="noindex"><style>body{{margin:0;width:{width}px;background:#fff}}iframe{{display:block;border:0;width:{width}px;height:850px}}</style></head><body><iframe title="{name} at {width}px" src="{route}" width="{width}" height="850"></iframe></body></html>')
from render_content import publication
rows=[dict(id='fixture'+str(i),title=title,authors=['Fixture Author'],venue='TEST DATA ONLY',year=year,status='preprint',topics=['test-topic'],paper_url='https://example.org',doi=None) for i,(title,year) in enumerate([('Immune variation fixture',2026),('Vaccination fixture',2025),('Single cell fixture',2024)])]
html=catalog('publications',rows,{'test-topic':{'name':'Test topic'}},publication)
(q/'filters.html').write_text('<!doctype html><html lang="en"><head><title>Internal synthetic filter tests</title><meta name="robots" content="noindex"><link rel="stylesheet" href="/assets/site.css"></head><body><h1>Synthetic fixtures — never deployed</h1>'+html+'<script src="/assets/catalog.js"></script></body></html>')
print('QA frames ready; remove _preview/_qa before packaging')
