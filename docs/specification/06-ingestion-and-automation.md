# 06 — Ingestion, CI and publishing workflow

## A. Publication discovery (ORCID + OpenAlex)

**Precondition:** owner supplies verified ORCID (not guessed). Fetch associated OpenAlex author IDs or `authorships.author.orcid`-filtered works. Account for pagination, provider rate limits, and multiple OpenAlex author IDs.

1. Read current curated publications and reviewed rejection list.
2. Query API using **persistent IDs** (ORCID, OpenAlex author ID or DOI), not fuzzy author-name search. Fetch bibliographic candidates and apply provider retries/timeouts and conditional caching if supported.
3. Normalize DOI and dates; classify work status when verified (do not infer peer review simply from presence of a venue).
4. Compare against curated records and preprint/version-of-record pairs. Record additions/changes in `cache/openalex_candidates.yml` with provenance.
5. Open/prepare a PR with candidate diff; **do not add unreviewed works to `content/publications.yml`.**
6. Owner accepts or rejects; maintain rejection decisions and aliases; test data validity; publish on merge.

Avoid relying on article counts, citations or author position without checks. Journal cover screenshots or article figures require rights review.

## B. GitHub catalogue

- `content/projects.yml` holds explicit `owner/repo` allowlist and site narrative.
- Fetch only those repositories using REST with timeouts and resource-aware caching; no automatic import of all personal repositories.
- API can enrich optional language, release link, archived flag, updated timestamp; **archived flag should trigger a review**, not automatic removal.
- Reject inaccessible/private repositories in public catalog unless owner explicitly approves a description and safe link.
- Do not publish GitHub stars as a scientific quality ranking; avoid per-visit requests.

## C. Substack

- Owner supplies actual feed URL `https://<publication>.substack.com/feed` or verified custom-domain feed. Use published RSS metadata.
- Normalize GUID and canonical URL, title/date and a sanitized *plain-text* description. Retain `first_seen` and `last_seen` timestamps.
- Merge as a union into reviewed article catalog; do not delete historical entries merely because absent from current feed.
- For **historical backfill**, use the publication-owner export (Substack Settings > Exports) if available; review canonical URLs before importing.
- External articles link directly to source and retain original publication metadata and canonical URL. No unauthorized full-text copy or paywall bypass.
- If feed unavailable/URL not supplied: skip and retain last data; show no broken subscription links.

## D. Scheduler + approvals

- `workflow_dispatch` (manual) plus `schedule` (e.g. **weekly**) for candidate/snapshot refresh.
- On scheduled run, fetch and validate then propose a reviewable branch/PR if metadata changed. Never commit unreviewed public publications.
- Build on ordinary `push`/PR independent of schedule; manual refresh fallback because public GitHub scheduled workflows can be disabled after 60 days inactivity.
- Use `GITHUB_TOKEN` minimal contents permissions; separate read-only sync from write/PR creation, scoped permissions; do not expose custom tokens in rendered output.
- Depend on SHA-pinned third-party GitHub Actions for production if security policy demands, with dependency updates maintained.
- No silent drift: include summary counts `candidate/new/modified/rejected`, fetch errors, and publication-build status.

## E. Recommended deployment CI sequence

```text
push / PR
   -> install pinned Quarto
   -> validate curated YAML and internal IDs
   -> render Quarto locally in CI (without external sync/network dependency)
   -> inspect generated HTML for broken links/landmarks
   -> accessibility smoke tests / optional browser screenshots
   -> upload preview artifact (PR)
merge / approved release
   -> deploy static output to verified provider
```

## F. Exception handling

| Failure | Behavior |
|---|---|
| OpenAlex 429 or downtime | Retry with backoff, preserve curated metadata, report warning |
| ORCID missing or ambiguous | Skip publication sync, require owner confirmation |
| GitHub repository renamed | Flag mapping for review, preserve owner-written metadata |
| RSS feed omits older article | Retain previously published item |
| RSS malformed | Reject untrusted markup, log error, keep last catalog |
| YAML validation failure | Stop build/deployment; show file and field error |
| External link 404 | Report; do not delete item automatically |
| Scheduled workflow disabled | Document manual dispatch/re-enable procedure |

## Official docs

- Quarto listings/custom YAML: https://quarto.org/docs/websites/website-listings-custom.html
- Quarto GitHub Pages: https://quarto.org/docs/publishing/github-pages.html
- OpenAlex IDs and filters: https://help.openalex.org/api/filtering/
- Substack RSS: https://support.substack.com/hc/en-us/articles/360038239391-Is-there-an-RSS-feed-for-my-publication
- Substack export: https://support.substack.com/hc/en-us/articles/360037466012-How-do-I-export-my-posts
- GitHub scheduled workflows: https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows
