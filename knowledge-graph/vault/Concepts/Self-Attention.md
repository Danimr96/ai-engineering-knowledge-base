---
id: "concept:self-attention"
type: concept
name: Self-Attention
canonical: true
category: "Models & inference"
taught_in: 2
community: 12
tags:
  - concept/glossary
  - category/models-and-inference
  - community/12
source: ai-engineering-from-scratch/glossary/terms.md
---

# Self-Attention

**Community:** [[Communities/12 Attention · Cross-Attention · Self-Attention|12 Attention · Cross-Attention · Self-Attention]]

> *What people say:* Tokens deciding which other tokens matter.

**What it actually means:** Attention in which queries, keys, and values are derived from the same sequence representation. Scaled similarity scores are normalized and used to combine values, subject to causal, padding, local, or other masks.

**Why it matters:** It builds context-sensitive token representations, but the permitted attention pattern depends on the architecture.

**Common confusion:** Not every token can always attend to every other token. Causal and sparse models intentionally restrict connections.

**Category:** [[Categories/Models & inference|Models & inference]]

## Related concepts

- [[Concepts/Attention|Attention]]
- [[Concepts/Context Window|Context Window]]
- [[Concepts/Cross-Attention|Cross-Attention]]
- [[Concepts/FlashAttention|FlashAttention]]
- [[Concepts/Transformer|Transformer]]
- [[Concepts/Vision Transformer (ViT)|Vision Transformer (ViT)]]

## Taught in

- [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]] — Attention where Q, K, V all come from the same sequence, letting every position attend to every other position
- [[Lessons/19-59 Vision Transformer Encoder|19/59 Vision Transformer Encoder]] — Each token attends to every other token in the same sequence


%% ── my notes ── %%
