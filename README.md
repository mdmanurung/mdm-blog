# Mikhael Manurung — Quarto research portfolio

Review branch for the Distill → Quarto migration. **The existing website is unchanged.**
The original source and `_site/` remain for rollback. New builds write only `_preview/`.

## Build and test

Requires Python 3.12 and Quarto **1.8.27**.

```sh
python3 -m pip install -r requirements.txt
python3 -m unittest discover -s tests -v
python3 scripts/build.py
```

`build.py` defaults to the noindex staging profile, validates content, cleans stale output, generates reviewed fragments, runs Quarto and checks the resulting pages. Set `QUARTO_BIN` if Quarto is not on PATH. All render steps work without external data requests. A production-target **build only** is available with `--production`; it does not publish anything.

## Edit content

- `content/profile.yml`: verified identifiers/feed settings; unresolved values stay null.
- `content/research.yml`: questions, importance, methods and evidence narratives.
- `content/news.yml`: dated, manually curated news, newest first (up to four on Home).
- `content/publications.yml`: 21 verified public scholarly records (19 journal articles and two preprints). `featured: true` selects up to three for Home. `version_of` records reviewed version relationships.
- `content/projects.yml`: allowlisted tools, owner-curated ordering and descriptions.
- `content/substack.yml`: reviewed metadata-only external articles, linked to originals.
- `writing/posts/<slug>/index.qmd`: original published articles. Keep drafts under `drafts/`, outside the render tree. Start from `templates/quarto/post.qmd`.

Only `visibility: public` records render. Every public output needs a public research topic. Do not change visibility until bibliographic/identity checks are complete. The current software maturity labels, selected-paper summaries, biography and news are review copy pending owner launch approval.

## Refresh metadata for review

```sh
python3 scripts/sync_publications.py
python3 scripts/sync_github.py
python3 scripts/sync_substack.py
python3 scripts/sync_substack.py --csv /absolute/path/to/metadata.csv
```

Publication discovery needs the owner’s ORCID or exact OpenAlex author ID; the API may also require `OPENALEX_API_KEY`. Substack needs a verified feed and explicit `substack_origins` in the profile. The CSV adapter expects `title,canonical_url,date,description`; normalize the owner export to those metadata fields first. It never imports body HTML.

All refreshes write only `cache/`, never `content/`. Failed fetches/parsing retain the last cache. RSS omissions never remove historical records. Review additions and version relationships, preserve manual tags and hidden/draft decisions, then add accepted records through a PR. `content/decisions.yml` records rejected publication IDs. The read-only weekly/manual discovery workflow uploads a review artifact instead of opening PRs automatically. GitHub can disable scheduled workflows in inactive repositories; manual dispatch/local commands remain available.

## Preview and review

The preview workflow builds downloadable artifacts without deploying to GitHub Pages or the existing domain. A separate private staging Site is used for review. No production deploy workflow is included.

For browser QA in the managed environment: run `python3 scripts/prepare_browser_qa.py` after building, then restart `sites-preview` if the clean build replaced its output directory. `_qa/` contains synthetic fixtures and must be removed before staging packaging. It is never part of a final clean build.

See [implementation notes](docs/implementation/06-quality-and-handoff.md), [original specification](docs/specification/README.md) and [maintenance runbook](docs/specification/14-maintenance-runbook.md).

## Launch gates

Owner approval of profile, news, selected papers and software descriptions; Scholar bibliography reconciliation and Substack feed if desired; CV/figure permission if used; production-host ownership and rollback verification. Do not merge or deploy to the existing website until reviewed.

Latest review includes the owner-supplied portrait, both Rubicon news sources, five software projects led by mycelium-extra, and first/second/last-author filtering for featured and related papers. ORCID/OpenAlex identities are verified. Google Scholar returned HTTP 429, so the bibliography is independently verified rather than claimed as a complete Scholar import; see [source review](docs/implementation/publication-source-review.md).
