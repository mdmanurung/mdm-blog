# Website migration changes

## Review implementation — 23 October 2026

- PR-0: inventory baseline, legacy routes and production isolation.
- PR-1: responsive Quarto site, editorial theme, navigation and search.
- PR-2: reviewed YAML contracts, escaping, visibility/reference gates.
- PR-3: publication browser and identity-based review-only discovery.
- PR-4: three allowlisted software projects with overview/docs/repository links.
- PR-5: native/Substack writing renderer and metadata-only RSS/CSV import.
- PR-6: reciprocal topic links, CI build/discovery artifacts, redirects, native feed, noindex staging, quality checks and screenshots.
- Owner steering: bio/news/selected-paper/package homepage inspired by Mayank Mittal; illustrated research-theme explorer inspired by Cecilia Baldoni; research narratives structured around questions, approaches and findings following Ana Rebeka Kamšek’s example. No layouts, text, artwork or code were copied.

## Review decisions

- Full bibliography, author identity, Substack feed, CV and new scientific images remain owner inputs. Three manually verified papers form the initial selection, not an automatic bibliography import.
- Use deterministic Python HTML templates and a small JS filter rather than Quarto listing internals for combined facets and unified source types.
- Keep the old Distill sources and tracked `_site/` unchanged until production hosting and rollback are verified.
- Use one review branch with milestone-sized commits and a draft PR rather than seven dependent review branches. No merge or live-site deployment.
- Discovery workflow uploads proposals as artifacts with read-only permissions; it does not autonomously open PRs or publish candidates.

- Owner-requested Rubicon news entry added, dated July 2026, with links to the ZonMw announcement and LUCID feature. It describes the award/project without presenting the future Sanger position as current.

- Expanded the reviewed public software selection to five repositories. Mycelium Extra is the lead homepage/directory spotlight; cellprograms, stablr and RaJIVEplus are the other homepage selections. ViralScan remains in the full directory. Original method/upstream attribution is retained.

- Applied the owner’s authorship rule: homepage selected papers and Research related-work studies must list Mikhael first, second or last. The full bibliography retains verified co-authored papers. Author roles are checked against the full author order.

- Reused the owner-requested portrait from the existing website beside the short biography; original image bytes retained, with responsive sizing and descriptive alt text.
