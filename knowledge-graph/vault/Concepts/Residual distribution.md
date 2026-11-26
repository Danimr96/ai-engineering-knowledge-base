---
id: "concept:residual-distribution"
type: concept
name: Residual distribution
canonical: false
taught_in: 3
community: 20
tags:
  - concept/lesson-term
  - community/20
source: ai-engineering-from-scratch/phases/07-transformers-deep-dive/16-speculative-decoding/docs/en.md
---

# Residual distribution

**Community:** [[Communities/20 Acceptance rate · Draft model · EAGLE-3|20 Acceptance rate · Draft model · EAGLE-3]]

> *What people say:* "The rejection fallback"

**What it actually means:** (q - p)+ normalized; sampling from this on rejection preserves the verifier's distribution.

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/07-16 Speculative Decoding — Draft, Verify, Repeat|07/16 Speculative Decoding — Draft, Verify, Repeat]]
- [[Lessons/10-15 Speculative Decoding and EAGLE-3|10/15 Speculative Decoding and EAGLE-3]] — (q - p)+ clamped at zero and renormalized — the correct distribution to sample from on rejection
- [[Lessons/10-25 Speculative Decoding and EAGLE|10/25 Speculative Decoding and EAGLE]] — 1, the distribution to sample from on rejection


%% ── my notes ── %%
