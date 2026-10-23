# 01 — Repo audit and adversarial second-round critique

## Confirmed observations (GitHub connector, repository `mdmanurung/mdm-blog`, main, 23 Oct 2026)

- `README.md` explicitly names a Distill site at `https://mdmanurung.rbind.io`.
- `_site.yml`: `distill::distill_article`, navbar About / Posts / Projects, **search disabled**, old `repository_url` points to `MikhaelManurung/mdm-distill` (not the inspected repo), `output_dir: _site`.
- `index.Rmd`: `postcards::jolla`, image and links, bio based on older Leiden role; do not migrate it as current truth without editing.
- `about.Rmd` is placeholder; `projects.Rmd` is effectively title-only; `posts.Rmd` defines a Distill listing.
- `_posts/welcome/welcome.Rmd` is a scaffold post that names **Nora Jones / Spacely Sprockets** rather than the site owner. Exclude from public replacement.
- `_subscribe.html` points to `https://themockup.blog/index.xml` (someone else's feed): **remove immediately from replacement**.
- `utterances.html` attaches GitHub issue comments to Distill `d-article`; not portable unmodified.
- `mdm_theme.scss`, `mdm_theme.css`, and `mdm_styles.css` diverge; some styles use all-uppercase typography; a custom font file is referenced but not established as distributable. Do **not** copy font files.
- `_site/` contains tracked/generated HTML; do not retain duplicate generated output in source branch without a deliberate hosting mechanism.
- `templates/post-template.Rmd` and `templates/talk-template.Rmd` and `R/` helpers exist; assess individually before retiring them.
- GitHub metadata shows `main` as default and most recent pushed_at **2024-08-26** when inspected. Deployment and domain ownership are not established from repo metadata.

## Critique of prior recommendations

1. **Automated public bibliography risks attribution errors.** ORCID/OpenAlex discovery is a queue. Publish only reviewed DOI records or explicitly approved non-DOI identifiers. Guard against preprints and version-of-record duplicates.
2. **A page for every paper and every repository is wasteful.** Default to good searchable index cards pointing to canonical paper and repo; manually create deep-dive pages for 3–5 flagship items only when worthwhile.
3. **A 'unified writing' listing must respect canonical sources.** External Substack cards link to original articles; native Quarto articles live on your domain. Never silently mirror paywalled/full-text Substack content.
4. **Multiple 'research programmes' can overstate finished work.** Label themes as research interests/questions; avoid fabricated claims, paper counts, grants, affiliation timelines. Curate launch copy with owner.
5. **Theme frameworks are not architecture.** Built-in Litera/Cosmo are styling baselines, not project templates. al-folio is strong functionally but switching to Jekyll/Ruby adds maintenance outside the existing R/Quarto skillset.
6. **A live API on page load harms resilience/privacy.** Materialize snapshots at build time. Provenance + cache + review make the site deterministic and testable.
7. **'Nightly automation' is fragile in a dormant public repo.** GitHub can disable scheduled workflows after 60 days inactivity. Add workflow_dispatch, clear stale-data indication and manual reconciliation path.
8. **Domain migration is a release concern, not a design default.** `rbind.io` could be hosted through a provider not evident from GitHub; inspect current host, DNS and configuration before choosing target.
9. **An interactive publication catalogue does not require a JS app.** Quarto listings give search/sort/categories; add one extra facet only if research users demonstrably need it.
10. **No generic stock scientific imagery.** Prefer user-owned paper figures, graphs, headshot and screenshots of real tools, with permissions and captions.

## Final scope gates

- If GitHub/Quarto are enough for curated content, **reject** a new database/CMS.
- If a section has no real content, **hide it or publish a useful explanation**—never ship synthetic placeholders.
- If an external data source fails, **preserve the last reviewed catalogue**, not replace it with an empty result.
- If the current domain cannot be migrated safely, **retain the existing website** and ship the new site to staging only.
- Site writing is professional but human: no grand claims or generic AI-generated academic boilerplate.
