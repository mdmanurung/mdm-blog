# 11 — Sourcebook: high-quality examples and official references

## Design and information architecture precedents

These websites are **design/function references, not code to clone**. Pages can change; check them before final implementation.

| Reference | URL | Distinctive practice to borrow | Limitations |
|---|---|---|---|
| Ava Amini | https://avaamini.com/ | Publications as substantive highlighted scientific contributions | Avoid graphics without rights |
| Andrew Heiss | https://www.andrewheiss.com/ | Links papers with code/data/replication/writing | Information-dense; simplify top-level nav |
| Robin Lovelace | https://robinlovelace.net/ | Quarto-based researcher identity, papers, open tools and notes | Adapt to immunology not transportation |
| Silvia Canelón | https://silviacanelon.com/ | Editorial warmth, readable prose, personal presence | Not a publication-specific UI blueprint |
| Simon Willison | https://simonwillison.net/ | Clear blog/notes/tool taxonomy and linkable evergreen writing | Too developer-heavy to copy directly |
| al-folio | https://github.com/alshedivat/al-folio | Rich scholarly metadata, BibTeX, project presentation | Jekyll stack vs Quarto; don't migrate just for styling |
| Mayank Mittal | https://mayankm96.github.io/ | Compact publication previews and links to code/project/paper | Robotics-focused visual style; contextual adaptation |
| Mike Mahoney | https://www.mm218.dev/ | Practical project/software/talks/write-up grouping | Some layouts depend on content volume |

## Official software & publishing documentation (consult before coding)

1. Quarto metadata listings: https://quarto.org/docs/websites/website-listings.html
2. Quarto custom listing templates: https://quarto.org/docs/websites/website-listings-custom.html
3. Quarto website search: https://quarto.org/docs/websites/website-search.html
4. Quarto navigation and aliases: https://quarto.org/docs/websites/website-navigation
5. Quarto site/publishing GitHub Pages: https://quarto.org/docs/publishing/github-pages.html
6. Quarto CI and cached execution: https://quarto.org/docs/publishing/ci.html
7. OpenAlex API / persistent IDs: https://help.openalex.org/api/
8. OpenAlex filters and ORCID: https://help.openalex.org/api/filtering/
9. Substack publication RSS: https://support.substack.com/hc/en-us/articles/360038239391-Is-there-an-RSS-feed-for-my-publication
10. Substack publication export: https://support.substack.com/hc/en-us/articles/360037466012-How-do-I-export-my-posts
11. GitHub Actions scheduled workflows: https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows
12. GitHub Pages custom domains: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site
13. W3C accessibility requirements: https://www.w3.org/TR/WCAG22/

## Original source facts verified in repository

- Repo https://github.com/mdmanurung/mdm-blog
- `_site.yml`, `index.Rmd`, `about.Rmd`, `projects.Rmd`, `posts.Rmd`, `_posts/welcome/welcome.Rmd`, `_subscribe.html`, `utterances.html`, `mdm_theme.scss`, `R/`, `templates/`.
- GitHub repo metadata as of 2026-10-23: last push 2024-08-26; main branch; site URL in description. Actual hosting provider not proven.

Do not paraphrase third-party pages wholesale in website content. This bibliography is an implementation reference, not a license to copy source code, illustrations or prose.
