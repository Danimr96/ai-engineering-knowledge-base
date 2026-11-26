---
id: "concept:gradient-descent"
type: concept
name: Gradient Descent
canonical: true
category: "Math & training"
taught_in: 3
community: 11
tags:
  - concept/glossary
  - category/math-and-training
  - community/11
source: ai-engineering-from-scratch/glossary/terms.md
---

# Gradient Descent

**Community:** [[Communities/11 Learning Rate · Optimizer · Batch Size|11 Learning Rate · Optimizer · Batch Size]]

> *What people say:* Walking downhill on the loss surface.

**What it actually means:** A family of optimization updates that move parameters using the negative gradient of an objective, usually estimated from batches rather than the entire dataset.

**Category:** [[Categories/Math & training|Math & training]]

## Related concepts

- [[Concepts/Gradient|Gradient]]
- [[Concepts/Learning Rate|Learning Rate]]
- [[Concepts/Optimizer|Optimizer]]
- [[Concepts/Stochastic Gradient Descent (SGD)|Stochastic Gradient Descent (SGD)]]

## Taught in

- [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]] — Subtract the gradient (times a learning rate) from the parameters to reduce the loss. The core of neural network training.
- [[Lessons/01-08 Optimization|01/08 Optimization]] — Update weights by subtracting the gradient scaled by the learning rate. The most basic optimizer.
- [[Lessons/02-02 Linear Regression|02/02 Linear Regression]] — Iteratively adjust parameters in the direction that reduces the cost function, using partial derivatives


%% ── my notes ── %%
