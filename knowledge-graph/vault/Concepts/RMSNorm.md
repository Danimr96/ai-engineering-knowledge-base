---
id: "concept:rmsnorm"
type: concept
name: RMSNorm
canonical: false
taught_in: 3
community: 72
tags:
  - concept/lesson-term
  - community/72
source: ai-engineering-from-scratch/phases/03-deep-learning-core/07-regularization/docs/en.md
---

# RMSNorm

**Community:** [[Communities/72 Early stopping · Layer normalization · RMSNorm|72 Early stopping · Layer normalization · RMSNorm]]

> *What people say:* "LayerNorm without the mean"

**What it actually means:** Root mean square normalization; drops the mean subtraction from LayerNorm for 10% speedup with equal accuracy

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/03-07 Regularization|03/07 Regularization]]
- [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]] — Divide by RMS; one less op, same empirical stability.
- [[Lessons/10-14 Open Models- Architecture Walkthroughs|10/14 Open Models: Architecture Walkthroughs]] — Normalize by root mean square only, with a learned scale — cheaper and comparable to LayerNorm


%% ── my notes ── %%
