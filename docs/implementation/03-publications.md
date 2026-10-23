# PR-3 — Publication browser and discovery

Implemented text/year/topic filters, descending publication years, abstract disclosures, canonical paper/OA/code/data links and optional featured summaries. Rendering accepts only reviewed public records.

OpenAlex discovery uses configured ORCID resolution or exact author IDs, follows cursors and deduplicates normalized DOI. Existing approvals/rejections are excluded. Provider publication type is retained separately; journal presence does not imply peer review. Preprint/version relationships require review through `version_of`. On failure no candidate cache is written. No name matching or automatic public promotion.

Following the owner’s request for selected publications on the landing page, three real papers were manually checked against Crossref plus publisher/PubMed records and entered as the initial review selection. Their full author lists and DOI metadata are retained. These are selected records, not a claim to a complete bibliography. Final owner approval of selection and summaries remains a production launch gate. Automatic discovery still requires a verified author identity and cannot promote records.

Checks: content/discovery unit tests; manual no-identity sync confirms safe skip. Network discovery is not claimed verified without a configured identity/API access.
