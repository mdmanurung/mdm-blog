# MDM Website Revamp — Implementation Bundle (v2.1)

**Date:** 23 October 2026  
**Target repository:** https://github.com/mdmanurung/mdm-blog  
**Current published URL:** https://mdmanurung.rbind.io  
**Status:** Reviewed implementation plan + reference configuration/data validator. **No changes have been applied to the GitHub repository or published site.**

## Executive decision

Build a **content-first Quarto research portfolio** with a restrained scientific-editorial design. Navigation: **Research / Publications / Software / Writing / About**; homepage is a curated index, not a chronological feed. Research themes cross-link publication records, curated GitHub software, and native/Substack writing. Synchronizers **propose data changes; only reviewed/approved records go public.**

Retain the current site URL at launch **if its DNS/hosting ownership and deployment route can be verified**; stage beforehand. Implement a **working static site first**. No database, runtime API, bespoke frontend framework, or unreviewed content publishing in MVP.

## Bundle map (reading order)

| File | Purpose |
|---|---|
| `docs/01-audit-and-critique.md` | Repository-grounded audit and corrections to prior strategy |
| `docs/02-adr-architecture.md` | Architecture decisions, considered alternatives, trade-offs |
| `docs/03-information-architecture.md` | Sitemap, journeys, cross-links and page specs |
| `docs/04-design-system.md` | Layout, typography, components, mobile and accessibility |
| `docs/05-content-and-data-contracts.md` | Authoritative data, schemas, provenance, linking rules |
| `docs/06-ingestion-and-automation.md` | ORCID/OpenAlex, GitHub, Substack, sync and CI behaviors |
| `docs/07-migration-and-deployment.md` | Migration mapping, URLs, preview, cutover, rollback |
| `docs/08-implementation-backlog.md` | Sequenced pull requests, dependencies, DoD |
| `docs/09-validation-and-acceptance.md` | Functional/a11y/SEO/content tests and release gates |
| `docs/10-risk-register.md` | Scientific, publishing and operational risks |
| `docs/11-examples-and-sources.md` | Design references and verifiable documentation URLs |
| `docs/12-agent-execution-prompt.md` | Paste-ready instruction for Claude Code / Codex / OpenCode |
| `docs/13-content-writing-brief.md` | Homepage/about/research copy guardrails and open facts |
| `docs/14-maintenance-runbook.md` | Practical authoring, moderation and recovery |

## Reference assets (not deployed)

`reference/config/_quarto.yml` and `reference/config/styles.scss` are **proposed starting configuration** and need integration, host configuration, and an actual Quarto render. `reference/data/` contains **synthetic examples**, not a claimed bibliography. `reference/scripts/validate_content.py` is a runnable PyYAML-based validator for selected contracts, covered by `reference/tests/test_validate_content.py`.

## Execution in 3 commands

```bash
# First: open the target repository on an implementation branch.
git clone https://github.com/mdmanurung/mdm-blog.git
cd mdm-blog
git checkout -b feat/quarto-portfolio
# Second: give your code agent docs/12-agent-execution-prompt.md and this bundle.
# Third: review PRs in docs/08-implementation-backlog.md; never replace current hosting until release gates pass.
```

**Unknowns to resolve from the owner (do not fabricate):** actual Substack publication URL, verified ORCID, publication allowlist, authoritative GitHub handles, chosen public email, image reuse rights, current DNS/hosting setup, and approved CV/bio text. These are content/setup inputs, **not blockers** for building the scaffold and validating the pipeline.

## Scope control

**Must ship:** readable homepage, 5 pages, curated publication catalogue, curated projects, writing listing (native + Substack metadata), site search, responsive accessible layout, working RSS where applicable, provenance-safe ingestion and URL redirects.

**Not now:** live citation counts, automatically generated biographies, per-paper microsites, an interactive research network graph, newsletter migration, realtime GitHub widgets, CMS/backend, and complex client-side filtering until scale justifies it.
