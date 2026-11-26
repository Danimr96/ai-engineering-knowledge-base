---
id: "lesson:02/10"
type: lesson
ref: 02/10
phase: 2
num: 10
title: Bias-Variance Tradeoff
lesson_type: learn
time_min: 75
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 9
community: 4
libraries:
  - numpy
aliases:
  - 02/10
  - 02-10
tags:
  - phase/02
  - type/learn
  - community/04
source: ai-engineering-from-scratch/phases/02-ml-fundamentals/10-bias-variance/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/02-ml-fundamentals/10-bias-variance"
---

# 02/10 Bias-Variance Tradeoff

> Every model error comes from one of three sources: bias, variance, or noise. You can only control the first two.

**Phase:** [[Phases/02 ML Fundamentals|Phase 2: ML Fundamentals]] · **Type:** Learn · **Time:** 75 min · **Status:** —  
**Open:** [[Upstream/02-ml-fundamentals/10-bias-variance/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/02-ml-fundamentals/10-bias-variance) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/02-ml-fundamentals/10-bias-variance) · code: bias_variance.py  
**Community:** [[Communities/04 Overfitting · Underfitting · Data Leakage|04 Overfitting · Underfitting · Data Leakage]] · **Libraries:** [[Libraries/numpy (python)|numpy]]  

## Prerequisites

Stated upstream: `Phase 2, Lessons 01-09 (ML basics, regression, classification, evaluation)`

- **02/01-09** — ML basics, regression, classification, evaluation:
    - [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]]
    - [[Lessons/02-02 Linear Regression|02/02 Linear Regression]]
    - [[Lessons/02-03 Logistic Regression|02/03 Logistic Regression]]
    - [[Lessons/02-04 Decision Trees and Random Forests|02/04 Decision Trees and Random Forests]]
    - [[Lessons/02-05 Support Vector Machines|02/05 Support Vector Machines]]
    - [[Lessons/02-06 K-Nearest Neighbors and Distances|02/06 K-Nearest Neighbors and Distances]]
    - [[Lessons/02-07 Unsupervised Learning|02/07 Unsupervised Learning]]
    - [[Lessons/02-08 Feature Engineering & Selection|02/08 Feature Engineering & Selection]]
    - [[Lessons/02-09 Model Evaluation|02/09 Model Evaluation]]

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/01-08 Optimization|01/08 Optimization]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/01-14 Norms and Distances|01/14 Norms and Distances]], [[Lessons/01-18 Convex Optimization|01/18 Convex Optimization]]
- depth 3: [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]], [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]], [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]], [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]], [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]]

## Builds on this

- [[Lessons/02-11 Ensemble Methods|02/11 Ensemble Methods]]
- [[Lessons/09-11 Sim-to-Real Transfer|09/11 Sim-to-Real Transfer]]

## Concepts taught

- [[Concepts/Bias|Bias]] `lesson term` — Systematic error from wrong assumptions. The gap between the average model prediction and truth.
- [[Concepts/Variance|Variance]] `lesson term` — Error from sensitivity to training data. How much predictions change across different training sets.
- Irreducible error `lesson term` — Error from randomness in the true data-generating process. No model can eliminate it.
- [[Concepts/Underfitting|Underfitting]] `glossary` — Model has high bias. It misses the real pattern even on training data.
- [[Concepts/Overfitting|Overfitting]] `glossary` — Model has high variance. It fits noise in training data that does not generalize.
- [[Concepts/Regularization|Regularization]] `lesson term` — Adding a penalty to reduce model complexity, trading bias for lower variance.
- Double descent `lesson term` — Test error decreases again when model capacity far exceeds the interpolation threshold.
- Model complexity `lesson term` — The capacity of a model to fit arbitrary patterns. Controlled by architecture, features, or regularization.

## Ships

- [[Artifacts/02-10 prompt-model-diagnostics|prompt-model-diagnostics]] `prompt` — Diagnose model performance issues using train/test metrics and learning curves

## Further reading

- Belkin et al., Reconciling modern machine learning practice and the bias-variance trade-off (2019) ([link](https://arxiv.org/abs/1812.11118)) — the double descent paper
- Nakkiran et al., Deep Double Descent (2019) ([link](https://arxiv.org/abs/1912.02292)) — epoch-wise and sample-wise double descent
- [[Resources/The Elements of Statistical Learning (ESL)|The Elements of Statistical Learning (ESL)]] ([link](https://hastie.su.domains/ElemStatLearn/)) — the definitive treatment of bias-variance decomposition ·  also cited by 1 other lesson
- Scott Fortmann-Roe: Understanding the Bias-Variance Tradeoff ([link](http://scott.fortmann-roe.com/docs/BiasVariance.html)) — clear visual explanation


%% ── my notes ── %%
