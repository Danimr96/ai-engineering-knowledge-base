---
id: "concept:swiglu"
type: concept
name: SwiGLU
canonical: false
taught_in: 2
community: 1
tags:
  - concept/lesson-term
  - community/01
source: ai-engineering-from-scratch/phases/07-transformers-deep-dive/05-full-transformer/docs/en.md
---

# SwiGLU

**Community:** [[Communities/01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism|01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism]]

> *What people say:* "The FFN everyone switched to"

**What it actually means:** Swish(W1 x) ⊙ W3 x → W2. Beats ReLU/GELU on LM ppl.

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]]
- [[Lessons/10-14 Open Models- Architecture Walkthroughs|10/14 Open Models: Architecture Walkthroughs]] — Gated linear unit with Swish: (xW1) sigmoid(xW1) xV — standard in every 2024+ open model


%% ── my notes ── %%
