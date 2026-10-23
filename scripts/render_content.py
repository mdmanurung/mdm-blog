from pathlib import Path
root = Path(__file__).resolve().parents[1]
out = root / "_generated"
out.mkdir(exist_ok=True)
for name in ["themes", "featured-publications", "featured-projects", "latest-writing", "research", "publications", "projects", "writing"]:
    (out / (name + ".html")).write_text("<p>Content is being prepared for review.</p>\n")
