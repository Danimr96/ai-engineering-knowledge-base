---
id: "concept:weight-decay"
type: concept
name: Weight Decay
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

# Weight Decay

**Community:** [[Communities/11 Learning Rate · Optimizer · Batch Size|11 Learning Rate · Optimizer · Batch Size]]

> *What people say:* Regularization that shrinks weights during optimization.

**What it actually means:** An update rule that reduces selected parameter magnitudes over training, often by multiplying weights by a shrinkage factor separate from the gradient update.

**Why it matters:** It can improve generalization, but the useful coefficient and excluded parameter groups depend on model, optimizer, schedule, and data.

**Common confusion:** Decoupled weight decay is equivalent to an L2 loss penalty for some simple optimizers, but not generally for adaptive optimizers such as Adam.

**Category:** [[Categories/Math & training|Math & training]]

## Related concepts

- [[Concepts/AdamW|AdamW]]
- [[Concepts/Dropout|Dropout]]
- [[Concepts/Optimizer|Optimizer]]
- [[Concepts/Overfitting|Overfitting]]

## Taught in

- [[Lessons/03-06 Optimizers|03/06 Optimizers]] — Subtracting a fraction of the weight value at each step; a regularizer that penalizes large weights
- [[Lessons/03-07 Regularization|03/07 Regularization]] — Shrinking all weights toward zero by subtracting lambda w at each step; penalizes complexity through weight magnitude


%% ── my notes ── %%
