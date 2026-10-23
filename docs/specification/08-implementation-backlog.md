# 08 — Milestone and PR-sized implementation backlog

Implement as small pull requests. **Do not change the production site without explicit final approval.** All PRs should contain screenshots of desktop/mobile pages, test results and brief decision notes.

## PR-0 — Inventory and baseline (P0, dependency: none)

- Document original publishing provider/domain, published paths, routes, repository links, `R/` and `templates/` usefulness.
- Capture screenshots/readme/current build. Preserve a release tag and rollback instructions.
- Identify real public profile and content-source identifiers (Substack/ORCID/GitHub); use TODO values pending confirmation.
- **Acceptance:** baseline URLs and fallback deployment captured; no production mutations.

## PR-1 — Quarto skeleton and design foundation (P0, requires PR-0)

- `_quarto.yml`, a single SCSS theme, five nav destinations, site search, README build commands.
- Implement homepage, Research, Publications, Software, Writing, About with **no invented public content**.
- Add 2 responsive layouts, headers/footers, first-pass SEO and accessibility landmarks.
- Add old `posts.html`, `projects.html` redirects; proper local URL handling.
- **Acceptance:** `quarto render` succeeds; pages/links render on staging; no default placeholder CV/articles exposed.

## PR-2 — Schema/validation (P0, requires PR-1)

- Introduce `content/research.yml`, `content/publications.yml`, `content/projects.yml`, `content/substack.yml` and normalizers.
- Add test scripts for IDs, duplicates, topics, visibility, canonical URLs, status, missing fields.
- Custom Quarto listing templates for publication rows and software cards; prefer native listings where sufficient.
- **Acceptance:** malformed test fixture fails with useful error; only visibility-public data appears.

## PR-3 — Publications experience (P0, requires PR-2)

- Owner supplies vetted initial list (ORCID/DOIs or BibTeX), ensure no synthetic outputs; import manually first.
- Add typeahead search, newest-first ordering, category/topic browse, DOI/oa/data/code links, 3 featured summaries.
- Add discovery job to create candidate metadata snapshot; explicit review step before public publication.
- **Acceptance:** every displayed record verifies against canonical DOI; duplicate preprint/paper recognized, no misattribution; 3 test search queries pass.

## PR-4 — Software experience (P0, requires PR-2)

- Curate allowlist for `cellprograms`, `ViralScan`, `RaJIVEplus` and any other owner-approved repos; crosscheck exact GitHub handle.
- Add purpose, scientific audience, maturity, docs, related work and 3–4 featured entries.
- Optional build-time GitHub metadata cache and flag inaccessible repos.
- **Acceptance:** every displayed repo exists, docs/source links work, content is written/reviewed rather than inferred from README snippets alone.

## PR-5 — Unified writing (P0, requires PR-2)

- Native `.qmd` article template, Writing listing merging local posts with `content/substack.yml`.
- Substack RSS feed ingest proposal job; plain text sanitization, canonical URLs and historical export import path.
- Preserve historical items when feed ages out; add owned verified Substack CTA.
- **Acceptance:** one original article and two reviewed Substack items display in test fixtures; external article opens correct canonical original; broken/empty feed retains existing items.

## PR-6 — Research cross-linking & quality gates (P1, requires PR-3/4/5)

- Topic-ID-based related outputs, research programme landing, owner-approved language, figure rights review.
- Validate all internal relations; performance/SEO/a11y smoke tests; publication links, mobile browser QA, redirect QA.
- Prepare staging preview, final sign-off, cutover/rollback.
- **Acceptance:** no orphan curated public outputs; every research theme has meaningful linked assets; accessibility high-priority failures resolved.

## PR-7 — Optional enhancements (P2, after successful launch)

- Deep-dive pages for flagship research/software; selectively add interactive figures from user-owned data; BibTeX export; advanced multi-facet filters; dark mode; additional languages or talks archive.
- **Trigger:** user demand or measurable catalog scale; don't include speculative work in MVP.

## Dependencies

```text
PR-0 -> PR-1 -> PR-2 -> PR-3 ---+
                    |-> PR-4 ---+-> PR-6 -> cutover -> PR-7 optional
                    |-> PR-5 ---+
```

## Definition of done per PR

- Scope limited to stated deliverables; snapshot tested; no broken links; accessible controls; metadata validated; documentation updated; owner review when scientific content appears.
- Agent must leave short change log, any outstanding uncertainties, and before/after screenshots, plus local verification commands.
