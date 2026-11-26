---
id: "concept:stochastic-gradient-descent-sgd"
type: concept
name: Stochastic Gradient Descent (SGD)
canonical: true
category: "Math & training"
aliases:
  - SGD
taught_in: 2
community: 11
tags:
  - concept/glossary
  - category/math-and-training
  - community/11
source: ai-engineering-from-scratch/glossary/terms.md
---

# Stochastic Gradient Descent (SGD)

**Community:** [[Communities/11 Learning Rate · Optimizer · Batch Size|11 Learning Rate · Optimizer · Batch Size]]

**What it actually means:** An optimizer family that updates parameters from a gradient estimated on a sampled example or minibatch rather than the complete training dataset.

**Why it matters:** It is the baseline for understanding gradient noise, momentum, batch scaling, and the adaptive optimizers used in modern training.

**In practice:** Record batch sampling, learning rate, momentum if used, and schedule, then compare validation behavior under equal update or token budgets.

**Common confusion:** In current practice, SGD usually means minibatch SGD, and its useful learning rate does not follow one universal batch-scaling rule.

**Category:** [[Categories/Math & training|Math & training]]

## Related concepts

- [[Concepts/Batch Size|Batch Size]]
- [[Concepts/Gradient Descent|Gradient Descent]]
- [[Concepts/Learning Rate|Learning Rate]]
- [[Concepts/Optimizer|Optimizer]]

## Taught in

- [[Lessons/01-08 Optimization|01/08 Optimization]] `alias` — Stochastic gradient descent. Compute gradient on a random subset instead of the full dataset. Almost always means mini-batch SGD in practice.
- [[Lessons/03-06 Optimizers|03/06 Optimizers]] `alias` — Stochastic gradient descent: update weights by subtracting lr gradient, computed on a mini-batch

## Sources

- Optimization Methods for Large-Scale Machine Learning ([link](https://arxiv.org/abs/1606.04838))
- Accurate, Large Minibatch SGD ([link](https://arxiv.org/abs/1706.02677))


%% ── my notes ── %%
