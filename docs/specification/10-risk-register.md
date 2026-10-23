# 10 — Risk register and mitigations

| ID | Risk | L/I | Preventive control | Detect / recover |
|---|---|---|---|---|
| R01 | Wrong author's paper added | Med/High | ORCID + DOI + owner approval | Sample DOI cross-check; revert candidate |
| R02 | Preprint and journal version duplicate | High/Med | DOI normalization plus version-link review | Duplicate report by normalized title/author/year |
| R03 | Stale/misleading career biography | High/High | Time-stamped role fields; signed-off homepage copy | Owner reviews before cutover |
| R04 | GitHub project immature/undocumented | High/Med | Curated allowlist, maturity reviewed | Broken docs check; remove from featured |
| R05 | Substack back catalog incomplete | High/Low | Owner export historical import; RSS union merge | Compare article counts and source archive |
| R06 | Substack full-text duplication / copyright or paywall | Med/High | Metadata-only links and canonical original URL | Scan generated site; delete copied body |
| R07 | Broken legacy permalinks | Med/High | URL inventory, Quarto aliases, staging crawl | Redirect test; roll back deployment |
| R08 | Custom domain misconfigured | Med/High | Verify DNS/host before changes | Restore old routing and artifact |
| R09 | GitHub schedule disabled in dormant repo | High/Low | Manual dispatch and docs; schedule not required for builds | Periodic check; update/re-enable |
| R10 | Third-party API outage | High/Low | Last reviewed cached data, independent build | Report warning; retry later |
| R11 | Unsafe imported HTML/JS | Med/High | Plain-text sanitization + escaping; no runtime feed embed | Build scan and review |
| R12 | Figures reproduced without right to reuse | Med/High | Use owner-owned/appropriately licensed visuals with attribution | Remove figure / replace with title-only |
| R13 | Inaccessible small controls or low contrast | Med/Med | Accessible base components and tests | Audit/fix to WCAG 2.2 AA target |
| R14 | Too much manual site maintenance | High/Med | Curated metadata + automated candidate queue, no per-paper pages | Quarterly effort review |
| R15 | Distill-era CSS/name mismatch leaks into Quarto | High/Low | Single current design token file; URL/link audit | Search build output for stale patterns |
| R16 | Overengineering agents/JS/backend | High/Med | No SPA/CMS; PR scope enforcement; explicit P2 list | ADR review before new dependencies |

`L/I` means estimated likelihood/impact (qualitative engineering judgment, not measured frequencies).

## Decision checkpoints

**Stop publishing** if R01/R03/R06/R08 remain unresolved. **Allow staging** with absent Substack/ORCID when pages hide missing-source content appropriately. Do not present citations, roles or code availability that cannot be verified.
