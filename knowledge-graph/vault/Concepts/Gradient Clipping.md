---
id: "concept:gradient-clipping"
type: concept
name: Gradient Clipping
canonical: true
category: "Math & training"
taught_in: 4
community: 11
tags:
  - concept/glossary
  - category/math-and-training
  - community/11
source: ai-engineering-from-scratch/glossary/terms.md
---

# Gradient Clipping

**Community:** [[Communities/11 Learning Rate · Optimizer · Batch Size|11 Learning Rate · Optimizer · Batch Size]]

**What it actually means:** Limiting gradient values or their combined norm before an optimizer update when they exceed a chosen threshold.

**Why it matters:** It can prevent an unusually large gradient from destabilizing a training step and producing non-finite values.

**In practice:** Log unclipped norms, clip after unscaling mixed-precision gradients, and investigate repeated clipping instead of treating it as a substitute for diagnosing instability.

**Common confusion:** Clipping controls update magnitude; it does not repair invalid data, a broken loss, or a consistently unsuitable learning rate.

**Category:** [[Categories/Math & training|Math & training]]

## Related concepts

- [[Concepts/Gradient|Gradient]]
- [[Concepts/Learning Rate|Learning Rate]]
- [[Concepts/Mixed Precision|Mixed Precision]]
- [[Concepts/NaN (Not a Number)|NaN (Not a Number)]]

## Taught in

- [[Lessons/01-13 Numerical Stability|01/13 Numerical Stability]] — Scaling the gradient vector so its norm does not exceed a threshold. Prevents exploding gradients from ruining weights.
- [[Lessons/03-06 Optimizers|03/06 Optimizers]] — Scaling down the gradient vector when its norm exceeds a threshold; prevents exploding gradient updates
- [[Lessons/03-13 Debugging Neural Networks|03/13 Debugging Neural Networks]] — Scaling gradients down when their norm exceeds a threshold, preventing exploding gradient updates
- [[Lessons/07-14 Build a Transformer from Scratch — The Capstone|07/14 Build a Transformer from Scratch — The Capstone]] — Cap global grad norm at 1.0; prevents training blowups.

## Sources

- On the difficulty of training recurrent neural networks ([link](https://arxiv.org/abs/1211.5063))


%% ── my notes ── %%
