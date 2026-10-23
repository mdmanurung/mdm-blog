from pathlib import Path
from html import escape
root = Path(__file__).resolve().parents[1] / "_preview"
for source, target in {"about.html":"/about/", "posts.html":"/writing/", "projects.html":"/software/", "posts/welcome/index.html":"/writing/"}.items():
    path = root / source
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Page moved</title><meta http-equiv="refresh" content="0;url={escape(target)}"><meta name="robots" content="noindex"></head><body><h1>Page moved</h1><a href="{escape(target)}">Continue to the new page</a></body></html>')
(root / "robots.txt").write_text("User-agent: *\nDisallow: /\n")
