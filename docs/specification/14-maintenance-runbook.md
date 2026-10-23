# 14 — Operations and authoring runbook

## Add a publication

1. Collect official DOI/paper metadata; check if preprint or published version already listed.
2. Add an entry to reviewed `content/publications.yml`, `visibility: public` only after factual checks.
3. Add 1–2 stable research `topics` and optional code/data links. `featured` only if deliberately curated.
4. Run validator and Quarto render; inspect bibliography order and links; publish through PR.

## Add a software project

1. Confirm exact public GitHub `owner/repo`; list it in `content/projects.yml`.
2. Owner writes purpose/audience/maturity/docs; set `visibility: public`.
3. Link relevant publication IDs and topic IDs, if real and verified.
4. Test project page/docs/repo URL; merge through review.

## Add a native post

1. Copy native Quarto post template; give unique slug, title, date, meaningful abstract, topics, and publish status.
2. Publish actual content from `writing/posts/`; Quarto listing indexes it.
3. Add original figure assets and rights/alt text; render and validate.

## Add a Substack post

1. Run manual/scheduled RSS fetch with approved feed URL.
2. Review proposed external card: title/date/canonical URL/excerpt and tags.
3. Merge to curated data; existing historical entries remain even if removed from active RSS feed.
4. Writing list links to Substack canonical location; no full-text mirroring.

## Review every 3 months

- Reconfirm bio, role and contact details; inspect featured work choices and software maturity.
- Test Substack feed and publication discovery job; check GitHub Actions schedule status.
- Scan broken links and redirects; review accessibility on desktop and a phone.
- Keep token/theme changes consolidated; update pinned dependencies deliberately.

## Incident handling

- Data error: mark record draft, regenerate site, redeploy; publish a correction if false scientific attribution was visible.
- External API down: use curated data; do not block static render.
- Broken deployment: redeploy last tagged known-good build, keep domain unchanged.
- Scheduled workflow disabled: run manual workflow_dispatch or re-enable; builds from pushes still work.
- DNS/HTTPS problem: restore prior provider routing; use documented owner account procedure.

## Scope protection rule

Any new feature request must state what reader problem it solves, its maintenance burden, and whether existing Quarto listing/template capabilities already solve it. If no clear measured problem, park the feature in `PR-7 Optional`.
