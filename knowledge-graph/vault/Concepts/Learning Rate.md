---
id: "concept:learning-rate"
type: concept
name: Learning Rate
canonical: true
category: "Math & training"
taught_in: 6
community: 11
tags:
  - concept/glossary
  - category/math-and-training
  - community/11
source: ai-engineering-from-scratch/glossary/terms.md
---

# Learning Rate

**Community:** [[Communities/11 Learning Rate · Optimizer · Batch Size|11 Learning Rate · Optimizer · Batch Size]]

> *What people say:* How large each optimization step is.

**What it actually means:** A scale factor used by an optimizer to control parameter-update magnitude. Values that are too large can destabilize training; values that are too small can make useful progress impractically slow.

**Common confusion:** The effective update also depends on the optimizer, schedule, gradient scale, batch, and parameter history.

**Category:** [[Categories/Math & training|Math & training]]

## Related concepts

- [[Concepts/Adam (Optimizer)|Adam (Optimizer)]]
- [[Concepts/Batch Size|Batch Size]]
- [[Concepts/Gradient Clipping|Gradient Clipping]]
- [[Concepts/Gradient Descent|Gradient Descent]]
- [[Concepts/Hyperparameter|Hyperparameter]]
- [[Concepts/Learning Rate Schedule|Learning Rate Schedule]]
- [[Concepts/NaN (Not a Number)|NaN (Not a Number)]]
- [[Concepts/Optimizer|Optimizer]]
- [[Concepts/Stochastic Gradient Descent (SGD)|Stochastic Gradient Descent (SGD)]]
- [[Concepts/Warmup|Warmup]]

## Taught in

- [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]] — A scalar that controls how big each gradient descent step is. Too large: diverge. Too small: converge slowly.
- [[Lessons/01-08 Optimization|01/08 Optimization]] — A scalar that controls how far each update moves the weights. Too large causes divergence. Too small wastes compute.
- [[Lessons/02-02 Linear Regression|02/02 Linear Regression]] — A scalar that controls how much parameters change per gradient descent step
- [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]] — A scalar that controls the step size when updating weights: w_new = w_old - lr gradient
- [[Lessons/03-06 Optimizers|03/06 Optimizers]] — The scalar multiplier on the gradient update; the single most impactful hyperparameter in training
- [[Lessons/03-09 Learning Rate Schedules and Warmup|03/09 Learning Rate Schedules and Warmup]] — The scalar that multiplies the gradient to determine the parameter update size


%% ── my notes ── %%
