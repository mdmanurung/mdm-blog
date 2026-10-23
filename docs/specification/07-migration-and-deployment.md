# 07 — Distill → Quarto migration, URLs and safe release

## Preflight: inventory and ownership

1. Capture working clone and tagged baseline from `main` (e.g. `before-quarto-migration`); record current URL crawl.
2. Verify who controls `mdmanurung.rbind.io`, DNS/provider, redirect rules, HTTPS and current deployment path. **Do not assume GitHub Pages** because the repository `has_pages=true`.
3. Document exact URL list from live domain and `_site/` generated files; identify backlinks in prior papers and ORCID/CV.
4. Inspect source `images/` for headshot ownership/consent; assess `R/` helpers and talk templates for reuse.
5. Confirm actual profile contact handles; `_site.yml` points to `MikhaelManurung/mdm-distill`, while inspected repository is `mdmanurung/mdm-blog`.

## Proposed file move map

| Legacy file | New home / action |
|---|---|
| `_site.yml` | Replace with `_quarto.yml` |
| `index.Rmd` | Rewrite as `index.qmd`, preserve original URL `/` |
| `about.Rmd` | Rewrite into `about/index.qmd` or `about.qmd` |
| `projects.Rmd` | Replaced by `/software/`, redirect `/projects.html` |
| `posts.Rmd` | Replaced by `/writing/`, redirect `/posts.html` |
| `_posts/welcome` | Exclude starter/placeholder content; redirect legacy link intentionally if published |
| `_subscribe.html` | Remove misleading feed link; replace with verified Substack CTA |
| `utterances.html` | Retire or explicitly reinstall modern comments, off by default |
| `mdm_theme.*`, `mdm_styles.css` | Consolidate to one tokenized SCSS and optional small CSS |
| `templates/*.Rmd`, `R/*.R` | Archive or selectively port if genuinely valuable |
| `_site/` | Remove from tracked source *after* choosing new publication path and ensuring rollback |

## Redirect strategy

- Quarto supports per-page `aliases` (generated HTML redirects). Add `posts.html` alias to Writing and `projects.html` alias to Software; preserve `/about.html` if About path changes.
- Preserve existing published article URLs when possible; if a live legacy post has backlinks, implement a specific redirect to equivalent content, not a generic homepage.
- Check relative links to existing assets and external social shares.
- Preview and test redirects on the chosen host. Some hosts may require server-level 301 rules for ideal SEO; HTML redirect alone is not an HTTP 301.

## Staging and cutover

1. Work on `feat/quarto-portfolio` in the **existing** repository, with small reviewed PRs.
2. Render locally. Publish preview to a separate address (temporary Pages project URL or hosting preview, depending on verified provider) with appropriate base path.
3. Test desktop/mobile links, search, all record URLs, form-free navigation, redirect list, accessibility and metadata.
4. Freeze content for cutover. Verify HTTPS, canonical base URL, preview indexing controls and sitemap.
5. Deploy to original host if feasible; alternatively configure approved replacement host and domain ownership safely.
6. Monitor functionality, broken links, search results and API-independent loading; retain previous deployment for rollback.
7. Switch domain only when DNS and preview fully verified; **never change DNS during an exploratory build**.

## Rollback

- Keep a Git tag and archived live artifacts.
- Document provider-specific rollback (revert deployment/branch or redeploy previous artifact); DNS rollback if changed.
- Restore legacy pages and redirect definitions if preview fails quality gates.

## Release checklist

- [ ] Legacy `/`, `/about.html`, `/posts.html`, `/projects.html` work or redirect appropriately.
- [ ] All verified real data, no example biography or pseudo-DOIs.
- [ ] Site search finds key research/software/post terms.
- [ ] Actual Substack publication URL and subscription CTA verified.
- [ ] HTTPS/canonical URLs/social previews correct.
- [ ] Real mobile devices / keyboard / contrast tested.
- [ ] No JS console errors, broken images or dead navigation.
- [ ] Owner signs off before production deployment.
