# PR-2 — Reviewed content contracts

A single Python content module owns schemas, normalization, topic relationships and visibility gates. It rejects duplicate DOIs/URLs, unsafe schemes, public synthetic records, missing provenance and public-to-draft references. Rendered HTML escapes all imported text. Draft data and provider snapshots never enter rendered pages.

Deterministic Python templates generate HTML fragments; a small progressive-enhancement script provides combined query/topic/year filtering. This replaces custom Quarto listing templates: unified native/external records and consistent facets use the same markup contract without depending on Quarto listing internals. Without JavaScript, all reviewed records and links remain readable.

Validation: `python3 -m unittest discover -s tests -v`; `python3 scripts/validate_content.py`.
