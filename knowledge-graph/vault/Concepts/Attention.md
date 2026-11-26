---
id: "concept:attention"
type: concept
name: Attention
canonical: true
category: "Models & inference"
taught_in: 3
community: 12
tags:
  - concept/glossary
  - category/models-and-inference
  - community/12
source: ai-engineering-from-scratch/glossary/terms.md
---

# Attention

**Community:** [[Communities/12 Attention · Cross-Attention · Self-Attention|12 Attention · Cross-Attention · Self-Attention]]

> *What people say:* How a model focuses on important tokens.

**What it actually means:** A mechanism that forms contextual representations by comparing query vectors with key vectors, normalizing the resulting scores, and using them to combine value vectors. Masks, position rules, or sparse patterns can restrict which positions participate.

**Why it matters:** Attention lets a model route information between sequence positions, but it does not by itself explain or prove what the model understood.

**Common confusion:** Attention weights are computation coefficients, not a faithful explanation of model reasoning.

**Category:** [[Categories/Models & inference|Models & inference]]

## Related concepts

- [[Concepts/Cross-Attention|Cross-Attention]]
- [[Concepts/FlashAttention|FlashAttention]]
- [[Concepts/KV Cache|KV Cache]]
- [[Concepts/Self-Attention|Self-Attention]]
- [[Concepts/Softmax|Softmax]]
- [[Concepts/Transformer|Transformer]]
- [[Concepts/Visual Grounding|Visual Grounding]]

## Taught in

- [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]] — Weighted average of a value sequence, weights computed from a query-key similarity.
- [[Lessons/07-01 Why Transformers — The Problems with RNNs|07/01 Why Transformers — The Problems with RNNs]] — Weighted sum sum_j a_ij v_j where a_ij comes from a similarity score between positions i and j.
- [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]]

## Sources

- [[Resources/Attention Is All You Need|Attention Is All You Need]] ([link](https://arxiv.org/abs/1706.03762))


%% ── my notes ── %%
