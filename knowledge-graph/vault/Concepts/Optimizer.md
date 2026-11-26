---
id: "concept:optimizer"
type: concept
name: Optimizer
canonical: true
category: "Math & training"
taught_in: 1
community: 11
tags:
  - concept/glossary
  - category/math-and-training
  - community/11
source: ai-engineering-from-scratch/glossary/terms.md
---

# Optimizer

**Community:** [[Communities/11 Learning Rate · Optimizer · Batch Size|11 Learning Rate · Optimizer · Batch Size]]

> *What people say:* The algorithm that updates weights.

**What it actually means:** An algorithm that transforms gradients into parameter updates. Plain stochastic gradient descent is a simple baseline; momentum, Adam, and other optimizers change the update using history or adaptive scaling. Each choice has different memory, stability, and tuning behavior.

**Common confusion:** The optimizer consumes gradients; backpropagation computes them.

**Category:** [[Categories/Math & training|Math & training]]

## Related concepts

- [[Concepts/Adam (Optimizer)|Adam (Optimizer)]]
- [[Concepts/AdamW|AdamW]]
- [[Concepts/Backpropagation|Backpropagation]]
- [[Concepts/Batch Size|Batch Size]]
- [[Concepts/Checkpoint|Checkpoint]]
- [[Concepts/Gradient|Gradient]]
- [[Concepts/Gradient Accumulation|Gradient Accumulation]]
- [[Concepts/Gradient Descent|Gradient Descent]]
- [[Concepts/Learning Rate|Learning Rate]]
- [[Concepts/Learning Rate Schedule|Learning Rate Schedule]]
- [[Concepts/Stochastic Gradient Descent (SGD)|Stochastic Gradient Descent (SGD)]]
- [[Concepts/Weight|Weight]]
- [[Concepts/Weight Decay|Weight Decay]]

## Taught in

- [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]] — An algorithm that uses gradients to update parameters, implementing SGD, Adam, or other rules


%% ── my notes ── %%
