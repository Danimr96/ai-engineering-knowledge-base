---
id: "concept:ffn-expansion"
type: concept
name: FFN expansion
canonical: false
taught_in: 2
community: 5
tags:
  - concept/lesson-term
  - community/05
source: ai-engineering-from-scratch/phases/07-transformers-deep-dive/05-full-transformer/docs/en.md
---

# FFN expansion

**Community:** [[Communities/05 Temperature · Autoregressive · Logits|05 Temperature · Autoregressive · Logits]]

> *What people say:* "How wide the middle MLP is"

**What it actually means:** Ratio of hidden-size to d_model, usually 4 (LayerNorm) or 2.6 (SwiGLU).

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]]
- [[Lessons/19-59 Vision Transformer Encoder|19/59 Vision Transformer Encoder]] — The feed-forward layer widens to 4 hidden before contracting


%% ── my notes ── %%
