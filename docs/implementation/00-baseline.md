# Migration baseline — 23 October 2026

Original commit: `1db8ecb` (full SHA in git history). Default branch: `main`.
Repository: https://github.com/mdmanurung/mdm-blog
Existing public URL: https://mdmanurung.rbind.io

The existing source is Distill/postcards. No repository workflow or provider configuration establishes the production hosting account. Domain/provider access and rollback controls require owner verification before cutover. No DNS, Pages settings, production host or main-branch changes are authorized by this implementation.

`legacy-urls.json` inventories tracked HTML outside vendor libraries. Preserve `/`, redirect `/about.html`, `/posts.html`, `/projects.html`. The only old post is a starter attributed to another author; redirect `/posts/welcome/` to Writing without republishing its text. Preserve `/posts.xml` as a redirect to the native feed. Assets stay in Git history; tracked `_site` remains untouched for rollback until a host is selected.

R helpers and old article/talk templates stay available but are excluded by an explicit Quarto render allowlist. New output uses ignored `_preview/`, independent of the tracked legacy `_site/`.

## Owner inputs needed before launch

- Approved bibliography, featured papers, official ORCID or OpenAlex author ID.
- Verified Substack feed/export and permission to publish selected entries.
- Confirm public biography/current role, software maturity and summaries.
- Current CV PDF, figure/headshot reuse permission if images are used.
- Existing hosting/DNS ownership, cutover and provider-specific rollback.

## Source isolation

Implementation is on `feat/quarto-portfolio`; builds never write `_site/`. No deploy-to-production workflow is added. Staging is a separate private preview. The original main commit is the rollback source; do not merge until content and host review are complete.
