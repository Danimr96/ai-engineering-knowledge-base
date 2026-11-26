---
id: "concept:data-augmentation"
type: concept
name: Data Augmentation
canonical: true
category: "Math & training"
taught_in: 1
community: 4
tags:
  - concept/glossary
  - category/math-and-training
  - community/04
source: ai-engineering-from-scratch/glossary/terms.md
---

# Data Augmentation

**Community:** [[Communities/04 Overfitting · Underfitting · Data Leakage|04 Overfitting · Underfitting · Data Leakage]]

> *What people say:* Making more training data.

**What it actually means:** Creating modified examples, such as transformed images, perturbed audio, or paraphrased text, to increase training diversity without collecting entirely new source data. It can reduce overfitting when the transformation preserves the task signal.

**Common confusion:** An augmentation must preserve the target label or behavior you want the model to learn.

**Category:** [[Categories/Math & training|Math & training]]

## Related concepts

- [[Concepts/Epoch|Epoch]]
- [[Concepts/Eval Set|Eval Set]]
- [[Concepts/Overfitting|Overfitting]]

## Taught in

- [[Lessons/03-07 Regularization|03/07 Regularization]] — Transforming training inputs (flip, crop, noise) to increase effective dataset size and force invariance learning


%% ── my notes ── %%
