---
id: "concept:condition-number"
type: concept
name: Condition number
canonical: false
taught_in: 3
community: 8
tags:
  - concept/lesson-term
  - community/08
source: ai-engineering-from-scratch/phases/01-math-foundations/11-singular-value-decomposition/docs/en.md
---

# Condition number

**Community:** [[Communities/08 Backpropagation · Gradient · Activation Function|08 Backpropagation · Gradient · Activation Function]]

> *What people say:* "How sensitive to errors"

**What it actually means:** sigma_max / sigma_min. A large condition number means small input changes cause large output changes. SVD reveals this directly.

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/01-11 Singular Value Decomposition|01/11 Singular Value Decomposition]]
- [[Lessons/01-17 Linear Systems|01/17 Linear Systems]] — kappa = sigma_max / sigma_min. Measures sensitivity to input perturbations. Lose about log10(kappa) digits of precision.
- [[Lessons/01-18 Convex Optimization|01/18 Convex Optimization]] — Ratio of largest to smallest eigenvalue of the Hessian. High condition number means elongated valleys and slow gradient descent


%% ── my notes ── %%
