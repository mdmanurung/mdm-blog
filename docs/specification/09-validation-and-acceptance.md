# 09 — Acceptance test plan and release gates

## Automated CI gates

1. **Data schema:** YAML/JSON valid; topic IDs exist; no duplicate DOI; no duplicate canonical Substack URLs; public records pass required fields and source URL check.
2. **Build:** clean `quarto render` passes without external network fetch; output includes root and each navigation section. No unreviewed source placeholders.
3. **Links:** internal paths resolve; external URLs have HTTP(S) scheme (network smoke check nonblocking for temporary external outage); no links to `themockup.blog/index.xml` or `MikhaelManurung/mdm-distill` unless specifically intentional and verified.
4. **Visibility:** no draft project/paper/essay leaks into public HTML or XML feed.
5. **Search & listings:** site search index generated; listing typeahead finds sample known real title; order is newest first and filter categories consistent; zero-results state understandable.
6. **Redirects:** `/posts.html` -> Writing; `/projects.html` -> Software; `/about.html` preserved or redirected; legacy real articles individually mapped.
7. **Smoke SEO:** one H1 per main page, unique title/description, canonical site root correct, sitemap/robots and RSS (native posts) as intended.
8. **Security:** no credentials or unescaped imported HTML in output; no raw third-party scripts from RSS; minimum workflow token permissions.

## Manual experience acceptance (desktop + mobile)

| Scenario | Expected result |
|---|---|
| First visit (30–60 seconds) | Audience understands scientific identity and can find research/publications/code |
| Collaborator searches for a paper | Finds verified bibliographic record and DOI within two actions from nav |
| Software user | Finds docs, repository, installation and related publication if available |
| Substack reader | Sees publication source label and original article link, not duplicate site content |
| Research topic exploration | Theme leads to relevant publications, projects, writing through stable IDs |
| Keyboard-only navigation | Nav, filters, search and links operable with visible focus |
| Mobile phone at 320px | No horizontal scrolling or clipped title/buttons |
| Provider outage | Last approved data remains available; site pages continue loading |

## Visual quality bar

- Two screenshots per top-level page: 1440px desktop, 390px mobile; visually inspect heading hierarchy, card density, body measures, image permissions/alt text.
- Real authored content, not lorem ipsum, stock images or fake publication titles.
- Baseline Lighthouse audits of accessibility/performance/SEO; budget goals: desktop/phone Core Web Vitals within current Google guidance if measurable. Do not claim pass from automated scores alone.

## Scientific correctness test

Owner explicitly checks 5 sampled records + all featured records against DOI/publisher pages; independent reviewer checks that software descriptors do not exaggerate validation maturity; check cited data/paper relationships.

## Release blocking conditions

- False or unverifiable publication; demo DOI accidentally made public; unconfirmed affiliation/status; inaccessible or wrong GitHub handle.
- Current site domain would be disrupted; redirect regressions; missing owner permissions for figures; critical accessibility keyboard failure; or non-reproducible build.

## Optional lightweight test infrastructure

- `python -m unittest discover -s reference/tests -v` for bundled schema sample (requires PyYAML).
- In implementation repo, use `pytest` if already part of stack; choose one validator and avoid duplicate independent sources of truth.
- For browser/regression tests, Playwright + axe-core if tooling is approved; keep tests scoped to 5 top-level pages and 3 important flows.

## Acceptance demonstration

Agent records exact command outputs/summary in the PR description and includes screenshots; it must not assert that `quarto render` passed unless it actually ran in an environment with Quarto installed.
