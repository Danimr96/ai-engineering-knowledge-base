---
id: "concept:layer-normalization"
type: concept
name: Layer normalization
canonical: false
taught_in: 2
community: 72
tags:
  - concept/lesson-term
  - community/72
source: ai-engineering-from-scratch/phases/03-deep-learning-core/07-regularization/docs/en.md
---

# Layer normalization

**Community:** [[Communities/72 Early stopping · Layer normalization · RMSNorm|72 Early stopping · Layer normalization · RMSNorm]]

> *What people say:* "Normalize per sample"

**What it actually means:** Normalizing across features within each sample; batch-independent, used in transformers where batch size varies

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/03-07 Regularization|03/07 Regularization]]
- [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]] — Normalizing across the feature dimension to mean 0 and variance 1, with learnable scale and bias parameters


%% ── my notes ── %%
