---
id: "concept:adam-optimizer"
type: concept
name: Adam (Optimizer)
canonical: true
category: "Math & training"
taught_in: 2
community: 11
tags:
  - concept/glossary
  - category/math-and-training
  - community/11
source: ai-engineering-from-scratch/glossary/terms.md
---

# Adam (Optimizer)

**Community:** [[Communities/11 Learning Rate · Optimizer · Batch Size|11 Learning Rate · Optimizer · Batch Size]]

> *What people say:* The optimizer you use without thinking about it.

**What it actually means:** Adaptive Moment Estimation. It combines an exponential average of gradients with an exponential average of squared gradients, applies bias correction, and adapts the update scale per parameter. It is a useful baseline, but it still needs a suitable learning rate and schedule.

**Common confusion:** Adam is a strong baseline, not a universal best optimizer.

**Category:** [[Categories/Math & training|Math & training]]

## Related concepts

- [[Concepts/AdamW|AdamW]]
- [[Concepts/Learning Rate|Learning Rate]]
- [[Concepts/Optimizer|Optimizer]]

## Taught in

- [[Lessons/01-08 Optimization|01/08 Optimization]] `alias` — Adaptive Moment Estimation. Tracks per-weight running averages of gradients and squared gradients to give each weight its own learning rate.
- [[Lessons/03-06 Optimizers|03/06 Optimizers]] `alias` — Combines momentum (first moment) and RMSProp (second moment) with bias correction for the initial steps

## Sources

- Adam paper ([link](https://arxiv.org/abs/1412.6980))


%% ── my notes ── %%
