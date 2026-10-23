# PR-3 — Publication browser and discovery

Implemented text/year/topic filters, descending publication years, abstract disclosures, canonical paper/OA/code/data links and optional featured summaries. Rendering accepts only reviewed public records.

OpenAlex discovery uses configured ORCID resolution or exact author IDs, follows cursors and deduplicates normalized DOI. Existing approvals/rejections are excluded. Provider publication type is retained separately; journal presence does not imply peer review. Preprint/version relationships require review through `version_of`. On failure no candidate cache is written. No name matching or automatic public promotion.

The initial catalogue remains empty because no owner-approved DOI list or verified persistent identity is supplied. This blocks the content acceptance criterion and production launch, not implementation of the browser. Synthetic search cases exist only in tests. Add DOI/BibTeX-derived records following the runbook, then review all featured records.

Checks: content/discovery unit tests; manual no-identity sync confirms safe skip. Network discovery is not claimed verified without a configured identity/API access.
