---
id: "concept:residual-vq"
type: concept
name: Residual VQ
canonical: false
taught_in: 2
tags:
  - concept/lesson-term
source: ai-engineering-from-scratch/phases/08-generative-ai/19-visual-autoregressive-var/docs/en.md
---

# Residual VQ

> *What people say:* "Additive tokenization"

**What it actually means:** Each scale's tokens encode the residual left by lower scales; decoder sums all scale embeddings

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/08-19 Visual Autoregressive Modeling (VAR)- Next-Scale Prediction|08/19 Visual Autoregressive Modeling (VAR): Next-Scale Prediction]]
- [[Lessons/12-16 MIO and Any-to-Any Streaming Multimodal Models|12/16 MIO and Any-to-Any Streaming Multimodal Models]] — Multi-codebook tokenization where each layer adds information; base layer is content, later layers are prosody


%% ── my notes ── %%
