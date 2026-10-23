# 02 — Architecture decision records

## ADR-001: Quarto as site generator (accepted)

**Context:** Existing Distill/R Markdown site, technical writing in R/Python, output-centric academic site.

**Decision:** Quarto static website; local `.qmd` documents; YAML listing data; SCSS theme; site-wide built-in search. No framework-level client-side SPA.

**Alternatives rejected for now:**
- **al-folio/Jekyll**: mature academic templates and BibTeX support but Ruby/Jekyll/plugin runtime maintenance; latest al-folio v1 architecture is modular but still another ecosystem.
- **Astro**: better bespoke client-side UI and components, but raises JavaScript/frontend complexity for little MVP benefit.
- **Next.js**: server rendering/framework footprint is disproportionate to static academic outputs.

**Reconsider when:** verified user testing shows Quarto listings and custom templates cannot deliver core UX, or portfolio evolves into a genuine app with rich interactive data exploration.

## ADR-002: Reviewed structured metadata as publishing source of truth (accepted)

- `content/publications.yml`: manually approved publication records, keyed by normalized DOI or stable local ID.
- `content/projects.yml`: allowlisted featured and listed repositories with owner-authored narratives.
- `content/research.yml`: stable topic slugs, one curated paragraph each, links resolved through IDs.
- `content/substack.yml`: union of previously accepted articles plus feed updates, each external canonical URL.
- `writing/posts/*.qmd`: native articles with front matter.
- `cache/*`: fetched provider metadata/proposals, not authoritative. **Never use an unreviewed provider cache as the public collection.**

## ADR-003: No API calls at page-view time (accepted)

Run ingestion on controlled CI/manual schedule. Render deterministic static pages. GitHub stars/release dates are optional enrichments and never determine featured order. Avoid external dynamic embeds where possible.

## ADR-004: Publishing provenance and versioning (accepted)

Provider IDs and `checked_at` timestamps stored alongside cache records. Source-independent owner-authored description/tags remain in curated files. Stable IDs make cross-linking robust to title changes. Never overwrite editorial metadata through a sync.

## ADR-005: Deployment stage before cutover (accepted)

Use a separate preview destination and test every legacy permalink. Keep `https://mdmanurung.rbind.io` until host ownership, DNS, redirects, HTTPS and rollback are proven. Official Quarto supports GitHub Pages, but do not presume Pages is the existing live host.

## ADR-006: Accessibility / no heavy animation (accepted)

Semantically structured pages, AA contrast, keyboard-visible focus, captions and alt text, reduced-motion friendliness, no animations preventing content access. Use responsive CSS, not client-side layout scripts.

## ADR-007: Selective deep-dive pages (accepted)

Publication index records have canonical external DOI links by default; featured articles can have local `publications/slug.qmd` commentary pages. Projects can have a short local overview with external docs link if curated context adds value. Cross-links are always reviewed, not guessed.

## System diagram

```text
    ORCID / OpenAlex     GitHub API      Substack RSS/export
           |                 |                   |
           +--------- discovery/snapshot jobs ---+
                              |
                     unreviewed proposals/cache
                              |
                      manual approval / PR
                              |
          curated publications / projects / articles / topics
                              |
                  Quarto + custom listing templates
                              |
                     static preview / tests
                              |
                     approved production host
```

**Trade-off:** curation adds a small approval step but prevents stale/inaccurate academic claims. For a personal scholarly identity, this is a worthwhile cost.
