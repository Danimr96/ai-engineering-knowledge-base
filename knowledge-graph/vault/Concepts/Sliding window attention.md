---
id: "concept:sliding-window-attention"
type: concept
name: Sliding window attention
canonical: false
aliases:
  - SWA
taught_in: 2
community: 70
tags:
  - concept/lesson-term
  - community/70
source: ai-engineering-from-scratch/phases/07-transformers-deep-dive/15-attention-variants/docs/en.md
---

# Sliding window attention

**Community:** [[Communities/70 Differential attention · Sliding window attention|70 Differential attention · Sliding window attention]]

> *What people say:* "Local attention"

**What it actually means:** Each query attends to its last W tokens; KV cache shrinks to O(W).

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/07-15 Attention Variants — Sliding Window, Sparse, Differential|07/15 Attention Variants — Sliding Window, Sparse, Differential]]
- [[Lessons/10-14 Open Models- Architecture Walkthroughs|10/14 Open Models: Architecture Walkthroughs]] — Each token attends only to the last W tokens — caps attention cost at O(W) per token, used in Gemma 2 and early Mistral


%% ── my notes ── %%
