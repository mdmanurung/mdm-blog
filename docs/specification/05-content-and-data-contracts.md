# 05 — Data model, ownership and integrity contracts

## The design principle

**External APIs discover, the owner approves, the static repository publishes.** No provider can overwrite hand-curated editorial text or silently remove previously approved content.

## Data locations

```text
content/
  research.yml                # topic taxonomy and research theme copy; human-managed
  publications.yml            # approved bibliography; human-managed
  projects.yml                # allowlisted GitHub projects; human-managed
  substack.yml                # approved external metadata cards, append/merge by canonical URL
  profile.yml                 # verified current/future roles and contact IDs
writing/posts/*.qmd           # native essays and tutorials, original content
cache/openalex_candidates.yml # proposals only
cache/github_snapshot.yml     # optional metadata enrichments
cache/substack_feed.yml       # proposal/feed metadata, no raw HTML
```

## `publications.yml` schema

```yaml
- id: doi:10.0000/example      # illustrative; NEVER publish as real paper
  doi: 10.0000/example
  title: Example publication
  year: 2026
  venue: Example journal
  authors: [A. Researcher, B. Scholar]
  status: peer-reviewed        # peer-reviewed | preprint | accepted | other
  topics: [immune-variation]
  featured: false
  paper_url: https://doi.org/10.0000/example
  oa_url: null                 # verified, legally hosted OA only
  data_urls: []
  code_urls: []
  significance: null          # optional owner's one-line summary
  visibility: draft           # public | draft
  provenance:
    discovered_from: openalex
    confirmed_by: owner
    checked_at: 2026-10-23
```

**Rules:** normalized DOI lowercase, strip `https://doi.org/`; DOI unique; `status` and `year` mandatory; names/venue verify against source; official paper and working canonical URL; stable local ID for DOI-less works; no public 'draft'. Preprint + published versions linked with `version_of` or reviewed grouping, not silently conflated.

## `projects.yml` schema

```yaml
- id: cellprograms
  repository: mdmanurung/cellprograms
  title: cellprograms
  summary: null               # owner must write scientific use case
  category: analysis-tool
  topics: [computational-immunology]
  maturity: experimental      # provisional; owner must approve
  docs_url: null
  paper_ids: []
  featured: true
  feature_order: 1
  visibility: draft
```

**Rules:** `owner/repo` exact; do not conflate GitHub accounts `mdmanurung` vs `MikhaelManurung` without owner verification; keep experimental or private work unpublished unless explicitly approved. GitHub availability may be checked, but stars/releases never rewrite `summary`/`maturity`/`featured`.

## `substack.yml` schema

```yaml
- id: substack:example-article
  title: Example essay (synthetic)
  canonical_url: https://example.substack.com/p/example-article
  date: 2026-10-01
  description: Synthetic example.
  topics: [computational-immunology]
  source: substack
  visibility: draft
  first_seen: 2026-10-23
  last_seen: 2026-10-23
```

**Rules:** unique canonical URL (strip UTM tracking and trailing slash carefully); description plain text, max ~280 chars; neither mirror content nor truncate embedded HTML into unsafe markup. Older feed entries remain when RSS stops including them. Manual hidden/removed wins over refresh.

## Research taxonomy

```yaml
- id: immune-variation
  name: Human immune variation
  question: How do environment, ancestry and infection history shape immunity?
  visibility: draft
```

Use one primary topic and optional secondary topics; do not create uncontrolled synonymous tags. Reject unknown topic IDs during validation. The topic ID drives reciprocal 'related outputs' blocks.

## Content provenance and precedence

| Field | Source of truth | Provider may update? |
|---|---|---|
| Publication DOI/title/venue/year | Verified record / owner-approved | Candidate only, then reviewed |
| Publication significance and topics | Owner | No |
| GitHub repo URL/name | Owner allowlist | Check existence only |
| GitHub stars/latest release | Provider snapshot | Optional, yes |
| Software scientific summary/maturity | Owner | No |
| Substack title/date/canonical URL | Substack feed/export, reviewed | Yes after safe merge |
| Substack topic tags/featured | Owner | No |
| Biography/appointments | Owner | No |

## Data validation gates

1. Parse YAML with fixed schemas; reject unexpected canonical URLs or invalid status.
2. Require unique IDs and normalized DOI/canonical external URL.
3. Validate topic references and cross-referenced publication IDs.
4. Verify public records contain title, valid URL, year/date and required metadata.
5. No synthetic/placeholder records may have `visibility: public`.
6. Keep a changelog of review decisions for accepted/rejected discovery candidates.
7. Feed fetch failures leave public cache unmodified, and render passes against last approved data.
8. For third-party scientific figures require source/license and meaningful alt text.
