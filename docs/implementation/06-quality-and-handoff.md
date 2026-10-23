# PR-6 — Quality checks and review handoff

## Result and scope

Quarto portfolio with a short bio, dated news, illustrated research explorer, three selected publications, three selected tools, research narratives and unified writing infrastructure. Existing main, `_site/`, Distill source, production host and domain remain unchanged. Rollback is the original main commit and unchanged legacy artifacts. One feature branch contains PR-0–PR-6 milestone commits; no production publishing workflow is added.

## Verification performed

- `python3 -m unittest discover -s tests -v`: **22 tests pass** (schemas, DOI normalization/duplicates, escaping, URL security, draft visibility, related references, pagination, provider failure, native/two-external rendering, malformed/empty feed and archive retention).
- `QUARTO_BIN=/tmp/quarto-1.8.27/bin/quarto python3 scripts/build.py`: **passes**, Quarto 1.8.27, 14 generated HTML pages. Local URLs/anchors, one H1 and description/title metadata per content page, redirects, search index, sitemap, robots and RSS checked.
- `python3 scripts/sync_github.py`: **three real allowlisted repository snapshots fetched**. Render does not consume them.
- Missing-identity publication discovery and missing-feed Substack refresh both skip safely. Real OpenAlex/Substack network integration remains untested until verified settings are supplied. Provider handling is covered with isolated fixtures.
- Browser: visually inspected all six main pages at the available desktop viewport (~1348–1363 CSS px) and in 390px mobile frames. Screenshots are in `docs/qa/`. Read-only DOM overflow checks at native desktop and 320/390/1440px frames: **24 checks, zero horizontal overflows**. Exact 1440px screenshot capture was unavailable; native desktop screenshots document the actual browser viewport.
- Browser interactions: actual publication searches `phage`, `hookworm`, `immuno-functionomics` each return one result; year 2024 returns one result; synthetic three-query fixture also tested. Software title search and no-results state verified. Quarto site search for ViralScan returns four indexed documents. Research explorer works with click and Enter; mobile menu opens with Enter at 320px.
- Contrast computations for main text/link/surface pairings are **5.29:1–13.17:1**, in `contrast-check.json`. Focus styling, labels, headings, reduced-motion CSS and skip link implemented. No full WCAG certification, real-device validation, Lighthouse scores, 200% zoom audit or screen-reader audit is claimed.
- Baseline screenshot is the **original tracked repository `_site` homepage**, served only as a local QA snapshot; not evidence of the currently deployed hosting provider.
- `git diff --check`: passes. `_site/` and legacy production source are unchanged relative to main.

## Bibliography and scientific copy

Three records manually checked on 23 October 2026 against Crossref plus publisher/PubMed sources:

| DOI | Source checks |
|---|---|
| 10.1016/j.isci.2026.117252 | Crossref title/authors/venue/year; PubMed PMID 42657060; publisher record |
| 10.1016/j.isci.2025.113839 | Crossref; PubMed PMID 41312379; publisher record |
| 10.1038/s41467-024-50313-0 | Crossref; Nature article metadata; institutional publication record |

These manually curated records form the **preview selection**, not a full bibliography or an assertion that owner editorial approval has occurred. Owner sign-off on selection, summaries, research explanations, news, biography and software maturity remains required before production launch. No unsupported code/data association is added. Figures and portraits are omitted; no third-party artwork is reused.

## Intentional deviations

1. One draft PR with ordered milestone commits, rather than seven dependent PRs.
2. Deterministic Python templates plus small JS for facets/unified content, rather than Quarto listing internals.
3. Read-only discovery uploads a review artifact; no autonomous PR creation or catalogue edits.
4. Legacy files and generated `_site` are retained for rollback but excluded from Quarto by an explicit allowlist.
5. No real Substack entries, CV download or full bibliography until owner supplies verified inputs. Synthetic fixtures are isolated in `_qa/` and **removed before staging packaging**.
6. The owner’s design steering adds an accessible illustrated explorer and bio/news landing page, superseding the original noninteractive homepage layout. It borrows principles, not source/artwork, from the linked examples.

## Still needed before production

Owner content/selection approval; verified ORCID/OpenAlex ID and complete bibliography; actual Substack feed/origins/export; optional current CV and image reuse; existing hosting/DNS ownership plus provider-specific rollback. Private staging is separate from the existing domain. Review first, then explicitly authorize any cutover.

## Reproduce browser fixtures

Build first, then `python3 scripts/prepare_browser_qa.py`. Restart the supervised preview after a clean build replaces the output directory. Only `http://terminal.local:4173/` is used for internal QA. Remove `_preview/_qa` before staging packaging. Browser screenshots and metric JSON document the performed checks; they are not automated proof of scientific correctness.
