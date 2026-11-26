---
id: "concept:loss-function"
type: concept
name: Loss Function
canonical: true
category: "Math & training"
taught_in: 2
community: 4
tags:
  - concept/glossary
  - category/math-and-training
  - community/04
source: ai-engineering-from-scratch/glossary/terms.md
---

# Loss Function

**Community:** [[Communities/04 Overfitting · Underfitting · Data Leakage|04 Overfitting · Underfitting · Data Leakage]]

> *What people say:* A number that measures training error.

**What it actually means:** An objective that maps predictions and targets, sometimes with regularization terms, to a value optimization tries to reduce. The loss determines which errors training directly rewards or penalizes.

**Common confusion:** A low training loss does not guarantee useful, safe, or generalizable behavior on production tasks.

**Category:** [[Categories/Math & training|Math & training]]

## Related concepts

- [[Concepts/Contrastive Learning|Contrastive Learning]]
- [[Concepts/Cross-Entropy|Cross-Entropy]]
- [[Concepts/Evaluation (Eval)|Evaluation (Eval)]]
- [[Concepts/GAN (Generative Adversarial Network)|GAN (Generative Adversarial Network)]]
- [[Concepts/Gradient|Gradient]]
- [[Concepts/Knowledge Distillation|Knowledge Distillation]]
- [[Concepts/Underfitting|Underfitting]]

## Taught in

- [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]] — A function that measures the gap between predicted and actual outputs, which training tries to minimize
- [[Lessons/03-05 Loss Functions|03/05 Loss Functions]] — A differentiable function mapping predictions and targets to a scalar that the optimizer minimizes


%% ── my notes ── %%
