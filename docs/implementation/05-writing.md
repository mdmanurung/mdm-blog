# PR-5 — Native and external writing

Unified writing renderer reads public native front matter and the reviewed Substack archive, sorts by date and labels the original platform. Substack links are canonical; imported body HTML is never published. Draft native posts stay outside the render tree, in `drafts/`; the validator rejects a draft placed under `writing/posts/` to prevent accidental direct-URL exposure.

RSS and normalized CSV metadata imports require configured publication origins. Plain-text excerpts strip markup/scripts and are capped at 280 characters. Canonical tracking parameters are removed. Candidate union retains historical items and manual flags; reviewed content is never overwritten. Failed parsing/network leaves the prior file intact. Add approved topic IDs before promoting a candidate. The CSV adapter expects title/canonical_url/date/description, not raw full-text export; map a Substack export to those metadata columns locally.

No real Substack feed or authored article was supplied, so no fabricated essay or subscription CTA is public. Two external cards and a native post are demonstrated in isolated automated fixtures only. Actual integration remains gated on the owner’s feed and content approval.
