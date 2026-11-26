---
id: "concept:learning-rate-schedule"
type: concept
name: Learning Rate Schedule
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

# Learning Rate Schedule

**Community:** [[Communities/11 Learning Rate · Optimizer · Batch Size|11 Learning Rate · Optimizer · Batch Size]]

**What it actually means:** A policy that changes the optimizer's learning rate as training progresses according to steps, epochs, metrics, or a predefined curve.

**Why it matters:** Different training stages can benefit from different update scales, so one constant rate may be unstable early or wasteful late.

**In practice:** Version the schedule with the optimizer configuration, log the actual rate at every step, and compare schedules under the same token or update budget.

**Common confusion:** A scheduler controls the learning rate over time; it does not decide when an optimizer step occurs or guarantee convergence.

**Category:** [[Categories/Math & training|Math & training]]

## Related concepts

- [[Concepts/Epoch|Epoch]]
- [[Concepts/Learning Rate|Learning Rate]]
- [[Concepts/Optimizer|Optimizer]]
- [[Concepts/Warmup|Warmup]]

## Taught in

- [[Lessons/01-08 Optimization|01/08 Optimization]] — A function that adjusts the learning rate during training. Large steps early, small steps late.
- [[Lessons/02-12 Hyperparameter Tuning|02/12 Hyperparameter Tuning]] `alias` — A function that adjusts the learning rate over the course of training for better convergence
- [[Lessons/03-06 Optimizers|03/06 Optimizers]] — A function that adjusts the learning rate during training; warmup + cosine decay is the modern default

## Sources

- SGDR ([link](https://arxiv.org/abs/1608.03983))
- [[Resources/Attention Is All You Need|Attention Is All You Need]] ([link](https://arxiv.org/abs/1706.03762))


%% ── my notes ── %%
