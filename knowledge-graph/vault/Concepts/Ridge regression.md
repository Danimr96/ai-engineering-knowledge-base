---
id: "concept:ridge-regression"
type: concept
name: Ridge regression
canonical: false
taught_in: 2
community: 4
tags:
  - concept/lesson-term
  - community/04
source: ai-engineering-from-scratch/phases/01-math-foundations/17-linear-systems/docs/en.md
---

# Ridge regression

**Community:** [[Communities/04 Overfitting · Underfitting · Data Leakage|04 Overfitting · Underfitting · Data Leakage]]

> *What people say:* "Regularized least squares"

**What it actually means:** Solve (X^T X + lambda I) w = X^T y. Adding lambda I improves conditioning and shrinks weights toward zero. Prevents overfitting.

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/01-17 Linear Systems|01/17 Linear Systems]]
- [[Lessons/02-02 Linear Regression|02/02 Linear Regression]] — Linear regression with a penalty of lambda sum(w_i^2) added to MSE


%% ── my notes ── %%
