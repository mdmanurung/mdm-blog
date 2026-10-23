# 12 — Copy/paste prompt for an implementation agent

```text
You are a senior frontend engineer, academic web publisher, and data engineer.

TASK
Revamp https://github.com/mdmanurung/mdm-blog using the accompanying MDM Website Revamp Bundle v2.1. Implement in the EXISTING repository in reviewable PR-sized stages. The website must become a Quarto-powered scientific-editorial research portfolio, linking research programmes, peer-reviewed publications, curated open-source software, and native/Substack writing.

REQUIRED READING ORDER
1. README.md
2. docs/01-audit-and-critique.md
3. docs/02-adr-architecture.md
4. docs/03-information-architecture.md
5. docs/05-content-and-data-contracts.md
6. docs/07-migration-and-deployment.md
7. docs/08-implementation-backlog.md
8. docs/09-validation-and-acceptance.md
Then consult remaining documents; inspect the repository and public site yourself. Bundle files are the planning source, not proof that deployment has happened.

HARD CONSTRAINTS
- Work in a feature branch; do not mutate main, DNS, production hosting, publication catalogue, or external Substack without explicit authorization.
- Do not invent publications, biographies, affiliations, grants, DOI, ORCID, Substack URL, contact addresses, links, research outcomes or project maturities. Use TODOs only in configuration/dev data; hide unfinished public blocks.
- Do not leak scaffold author Nora Jones/Spacely Sprockets or an incorrect subscription URL; remove these from published outputs.
- Preserve/redirect current URLs (`/`, `/about.html`, `/posts.html`, `/projects.html`) after inventory; never delete public material without redirect evaluation.
- Keep a static site; no runtime API, new backend/database, paid CMS, heavy animation or React SPA. Prefer native Quarto features and small code.
- External metadata ingestion yields a reviewed candidate queue; only owner-approved records publish. Do not copy Substack full text.
- No scientific figures without permission/attribution. No fabricated stats or GitHub stars as quality metrics.
- Strict reproducibility: schema validate -> render -> smoke test -> stage -> review; report commands actually run vs not run. No silent changes to plans.
- Minimize dependencies. Use Python standard library + PyYAML where available, not a bespoke graph engine.
- Keep desktop/mobile clarity, keyboard usability, alt text, AA contrast as acceptance requirements.

DELIVERABLES
- Quarto `_quarto.yml`, editorial styles, homepage and 5 main section pages.
- Structured curated content models and tests.
- Publication directory with validated DOI data and search/filter.
- Allowlisted software directory and curated featured cards.
- Unified native/metadata-only Substack writing list and a manual RSS refresh procedure.
- Topic-ID cross-links Research <-> Publications <-> Software <-> Writing.
- CI workflows for independent deterministic site builds and optional scheduled discovery; staging deployment without production replacement.
- Redirects, site search, basic SEO, accessibility/performance checks, CHANGELOG of migration decisions.

IMPLEMENTATION APPROACH
A. Inventory repository and host; produce exact URL map and owner-input checklist. Present a concise implementation plan and risks; proceed with tasks that do not require unresolved facts.
B. Apply PR-0...PR-6 in docs/08 in sequence; aim small diff boundaries and a working site after PR-1.
C. For each phase write `What changed`, `Why`, `Files`, `Test evidence`, `Remaining risks` in PR notes. Pause and ask owner ONLY before irreversible production changes or when a missing verified identity directly blocks publishing personal content. For otherwise incomplete data, implement the structural feature with no fabricated records.
D. Before completing, run and report exact validation; test mobile layout and original URLs. Confirm no automatic public promotion of unreviewed metadata.

DECISION RULE
When design completeness conflicts with trustworthy academic information, prioritize correctness, maintainability and readable typography. Never fill a page with synthetic projects or made-up papers. Optional features remain out of scope unless explicitly approved.
```

## Suggested work product format per PR

```text
PR title:
Goal:
Files changed:
Source of truth changed? (yes/no):
Data/identity requiring owner approval:
Verification commands run and results:
Screenshots:
Rollout/rollback:
Deferred work:
```
