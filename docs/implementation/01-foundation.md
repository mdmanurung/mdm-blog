# PR-1 — Quarto foundation

Added six top-level pages, editorial SCSS/CSS, built-in search and redirect generation. System font fallbacks avoid redistributing unverified fonts. Headshot and figures are omitted pending reuse confirmation. Output is `_preview/`; legacy `_site/` is unchanged.

Generate fragments before Quarto's initial include scan: `python3 scripts/render_content.py`, then `quarto render --profile staging`. The pre-render hook regenerates them on subsequent builds. The build wrapper introduced in PR-6 makes this ordering automatic for clean checkouts.

Biography copy is a review draft based on the owner-provided professional background; future appointments and a downloadable CV are omitted pending launch review. No production deployment occurs.
