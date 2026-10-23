# 04 — Design and interaction specification

## Style statement

**Scientific editorial / restrained modern**: typography-first, clear hierarchy, modest accent, academic substance rather than flashy bioinformatics artwork. Design precedents: Ava Amini (publication storytelling), Andrew Heiss (linked research artifacts), Silvia Canelón (editorial warmth), Robin Lovelace (Quarto content-first information flow).

## Tokens

| Token | Value | Use |
|---|---|---|
| Background | `#FAFAF7` | Main light canvas |
| Primary ink | `#1D3034` | Body/title |
| Accent | `#176A70` | Links/interactive |
| Surface | `#E5EDEB` | Soft areas |
| Border | `#CAD8D5` | Card outlines |
| Text secondary | `#526366` | Supporting metadata |

Use **Source Serif 4** (or Georgia fallback) for prominent editorial titles; **Source Sans 3** (or system sans fallback) for body; system monospace / IBM Plex Mono for code. Do not bundle or redistribute font binaries. Keep legible fallback fonts.

## Layout and type

- Container: `max-width: 1120px`; prose `max-width: 70ch`.
- Responsive: 1-column phones; 2-column cards on tablet; 3-column selective cards on desktop.
- Hierarchy: H1 ≤ 2.6rem desktop, H2 around 1.65rem; responsive `clamp`; body ~1.05rem with ≥1.55 line height.
- Header on desktop small, clearly differentiated active state; mobile hamburger with visible focus.
- Use a grid for featured work, list for complete scholarly bibliography (dense records), and readable editorial rows for essays.
- Avoid carousels, parallax, continuously moving animations, oversized hero imagery, generic particle networks.

## Component inventory / contracts

- `Hero`: name, verified one-sentence mission, role, optional portrait, two semantic links.
- `ResearchTheme`: tag/number, title, question, 1-2-line description, link.
- `PublicationRow`: verified title, contributors/venue/year, primary DOI URL, status, topic links, optional meaningful image.
- `SoftwareCard`: name, purpose, maturity label, stack, docs/repo; no star count by default.
- `WritingRow`: title, date, source, category, summary, canonical URL. External links distinguishable visually and accessibly.
- `RelatedOutputs`: grouped list populated by stable topic IDs.
- `Search`: Quarto built-in search (site pages) plus listing filter in publication index. Avoid duplicate search widgets visually close to each other.
- `Footer`: verified identifiers, contact and license/copyright.

## Interaction decisions

- Default no dynamic JS needed for home, about and research.
- Quarto custom metadata listings support sorting/filtering/pagination when template includes required classes/attributes (official docs).
- Category chips must have meaningful label and keyboard access; if multi-facet filtering is too fragile, ship single category filter + query first.
- Link buttons should show destinations: `Paper`, `Code`, `Documentation`, `Data`, `Article`. No 'Read more' without context.

## Accessibility (target WCAG 2.2 AA)

- Keyboard-only traversal, visible focus, skip-to-content and semantic headings; minimum touch target size per WCAG unless exceptions apply.
- Verify contrast with a tool; provided token palette is **candidate**, not an automatically certified AA pairing.
- Descriptive alt text for meaningful science figures; empty alt only when purely decorative.
- Captions and source/license for scientific figures; respect reduced-motion settings.
- Make link purpose understandable without color alone.
- Browser zoom 200% and narrow 320px width without horizontal content overflow.
- No auto-play content; avoid third-party trackers without an explicit decision.

## SEO and social

Title/description per page; Open Graph image from owned/allowed assets; sitemap/robots/canonical links; scholarly identifiers with DOI/ORCID link; structured schema.org markup only if tested and factual. Never invent citation counts, rank or affiliation.
