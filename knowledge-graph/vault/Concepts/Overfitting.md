---
id: "concept:overfitting"
type: concept
name: Overfitting
canonical: true
category: "Math & training"
taught_in: 5
community: 4
tags:
  - concept/glossary
  - category/math-and-training
  - community/04
source: ai-engineering-from-scratch/glossary/terms.md
---

# Overfitting

**Community:** [[Communities/04 Overfitting · Underfitting · Data Leakage|04 Overfitting · Underfitting · Data Leakage]]

> *What people say:* The model memorized the training data.

**What it actually means:** A generalization gap in which performance on training data is substantially better than performance on representative unseen data. Memorization can contribute, but the operational symptom is poor generalization.

**In practice:** Compare training and held-out metrics, inspect subgroup failures, and test changes such as data quality, regularization, early stopping, or model capacity.

**Category:** [[Categories/Math & training|Math & training]]

## Related concepts

- [[Concepts/Data Augmentation|Data Augmentation]]
- [[Concepts/Data Deduplication|Data Deduplication]]
- [[Concepts/Dataset Split|Dataset Split]]
- [[Concepts/Distribution Shift|Distribution Shift]]
- [[Concepts/Dropout|Dropout]]
- [[Concepts/Epoch|Epoch]]
- [[Concepts/Eval Set|Eval Set]]
- [[Concepts/Underfitting|Underfitting]]
- [[Concepts/Weight Decay|Weight Decay]]

## Taught in

- [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]] — The model learned training-specific noise instead of general patterns, so it fails on new data
- [[Lessons/02-02 Linear Regression|02/02 Linear Regression]] — Using a model so complex that it fits noise in training data and fails on new data
- [[Lessons/02-09 Model Evaluation|02/09 Model Evaluation]] — The model captures noise in the training data, performing well on training but poorly on unseen data
- [[Lessons/02-10 Bias-Variance Tradeoff|02/10 Bias-Variance Tradeoff]] — Model has high variance. It fits noise in training data that does not generalize.
- [[Lessons/03-07 Regularization|03/07 Regularization]] — When a model's training performance significantly exceeds its test performance, indicating it learned noise rather than signal


%% ── my notes ── %%
