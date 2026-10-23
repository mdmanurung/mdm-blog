# 03 — Sitemap, reader journeys, and page contracts

## Top-level sitemap

```text
/                        Home: identity / featured work / latest writing
/research/                Three thematic research questions
/research/immune-variation/
/research/infection-vaccines/
/research/computational-immunology/
/publications/            Complete publication catalogue; optional local featured essays
/software/                Curated software collection
/software/<slug>/         Local overview only for selected tools
/writing/                 Native posts + external Substack article cards
/writing/posts/<slug>/    Original Quarto articles only
/about/                   Bio / trajectory / CV / contact
```

**Nav:** site-name link to Home; `Research · Publications · Software · Writing · About`; search icon and optional social links. On small screens collapse to accessible native navbar. No top-level `Projects`, `News`, `Resources`, or `CV` item; these are subitems or links.

## Reader journeys

- **Grant reviewer (60 sec):** homepage research identity → Research → selected peer-reviewed outputs → downloadable CV.
- **Scientist seeking a method:** Software → tool category → install/docs/paper → software-specific article.
- **Collaborator:** Publications → filter/topic → canonical DOI + data/software links → contact.
- **Substack reader:** Writing → essays + native research notes → research topic context without being forced to leave Substack.

## Home (components in order)

1. Hero with name, one scientifically specific positioning statement, current verified affiliation, one primary CTA (`Research`) and secondary CTA (`CV` or `Publications`). **Do not state future positions as current.**
2. Three research themes (compact, no oversized image cards).
3. Selected publications (3 max): title, venue/year, 1-line significance, DOI; no impact factor badge.
4. Selected software (up to 4): narrative purpose, status and docs/source link; avoid stars/rankings.
5. Writing (2–3 newest) with source badges; subscribe CTA should point to actual Substack publication.
6. Footer: ORCID, GitHub, email/contact and licensing/privacy as applicable.

## Research

Landing: 3 themes, each with a guiding question, methods, studies, selected evidence and linked outputs. Detail pages only when ≥2 worthwhile scientific outputs exist; otherwise anchor sections on landing page.

Suggested theme IDs (editable): `immune-variation`, `infection-vaccines`, `computational-immunology`.

## Publications

By default: compact list/table rather than visual cards for every record. Controls: text filter + year/topic labels + newest first. Record: title, full authorship/author-short display where verified, venue, year, status (preprint vs peer reviewed), DOI, open-access link if trustworthy, code/data links, 1-line owner-authored significance for featured only. Optional BibTeX/CSL export after validated metadata. DOI links to publisher; never host paywalled full text.

## Software

Feature first 4 projects; below show an alphabetical/faceted directory of **approved** repositories. Each item: scientific problem, tool type, language, maturity (`stable`, `active`, `experimental`, `archived`), docs, repository, publication, topic. Never infer development status from last commit automatically.

## Writing

Single page with source indicators `On this site` / `Substack`; topical categories `Research notes`, `Technical tutorials`, `Essays`, `News`. Native article pages carry canonical URL on this domain; external item links point directly to Substack original. Do not generate duplicate full-text copies from feed.

## About

Short 3-paragraph biography; positions as **time-stamped** timeline, research interests, selective invited talks, CV download, contact/social. Research claims and positions require manual approval.

## Discoverability and link logic

Each curated record uses `topics: [<stable slug>]`. A research page derives lists of related papers, software and writing by topic ID, not repeated hand-coded links. Detail pages have `Related work` and breadcrumbs. Avoid auto-generating 'related' claims from semantic similarity alone.

## Empty and failure states

- No publication items? Do not publish a misleading empty library; hold launch until real list approved.
- No Substack URL? Writing page ships with local posts and an honest 'External essays will appear when connected' note only if useful; avoid fake cards.
- Missing project logo? Use text-only card, not arbitrary stock imagery.
- Broken outbound link? Hide external button or fail validation; don't present a dead CTA.
