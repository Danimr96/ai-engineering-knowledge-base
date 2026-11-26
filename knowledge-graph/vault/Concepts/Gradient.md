---
id: "concept:gradient"
type: concept
name: Gradient
canonical: true
category: "Math & training"
taught_in: 2
community: 8
tags:
  - concept/glossary
  - category/math-and-training
  - community/08
source: ai-engineering-from-scratch/glossary/terms.md
---

# Gradient

**Community:** [[Communities/08 Backpropagation · Gradient · Activation Function|08 Backpropagation · Gradient · Activation Function]]

> *What people say:* The slope of the loss.

**What it actually means:** A vector of partial derivatives pointing in the direction of steepest increase. In ML, you go opposite to the gradient (gradient descent) to minimize the loss.

**Common confusion:** Optimizers can transform, average, clip, or adapt gradients instead of taking a plain negative-gradient step.

**Category:** [[Categories/Math & training|Math & training]]

## Related concepts

- [[Concepts/Activation Function|Activation Function]]
- [[Concepts/Autograd|Autograd]]
- [[Concepts/Backpropagation|Backpropagation]]
- [[Concepts/Batch Size|Batch Size]]
- [[Concepts/Gradient Clipping|Gradient Clipping]]
- [[Concepts/Gradient Descent|Gradient Descent]]
- [[Concepts/Loss Function|Loss Function]]
- [[Concepts/NaN (Not a Number)|NaN (Not a Number)]]
- [[Concepts/Optimizer|Optimizer]]
- [[Concepts/ReLU|ReLU]]

## Taught in

- [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]] — A vector of all partial derivatives. Points in the direction that increases the function fastest.
- [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]] — The partial derivative of the loss with respect to a parameter -- tells you how to change that parameter to reduce the loss


%% ── my notes ── %%
