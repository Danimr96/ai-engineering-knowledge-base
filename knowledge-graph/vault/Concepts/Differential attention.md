---
id: "concept:differential-attention"
type: concept
name: Differential attention
canonical: false
taught_in: 2
community: 70
tags:
  - concept/lesson-term
  - community/70
source: ai-engineering-from-scratch/phases/07-transformers-deep-dive/15-attention-variants/docs/en.md
---

# Differential attention

**Community:** [[Communities/70 Differential attention · Sliding window attention|70 Differential attention · Sliding window attention]]

> *What people say:* "Two maps, one subtracts"

**What it actually means:** DIFF Transformer: subtract a learned λ times a second attention map from the first to cancel attention sinks.

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/07-15 Attention Variants — Sliding Window, Sparse, Differential|07/15 Attention Variants — Sliding Window, Sparse, Differential]]
- [[Lessons/10-16 Differential Attention (V2)|10/16 Differential Attention (V2)]] — Split Q, K into two halves, compute two softmax maps, subtract the second (scaled by lambda) from the first, then multiply by V


%% ── my notes ── %%
