---
id: "concept:triplet-loss"
type: concept
name: Triplet loss
canonical: false
taught_in: 2
community: 22
tags:
  - concept/lesson-term
  - community/22
source: ai-engineering-from-scratch/phases/03-deep-learning-core/05-loss-functions/docs/en.md
---

# Triplet loss

**Community:** [[Communities/22 Backward pass · Forward pass · Vanishing gradient|22 Backward pass · Forward pass · Vanishing gradient]]

> *What people say:* "Anchor-positive-negative"

**What it actually means:** Pushes anchor closer to positive than negative by at least a margin in embedding space

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/03-05 Loss Functions|03/05 Loss Functions]]
- [[Lessons/04-20 Image Retrieval & Metric Learning|04/20 Image Retrieval & Metric Learning]] — L = max(0, d(a, p) - d(a, n) + margin); the canonical metric-learning loss


%% ── my notes ── %%
