---
id: "lesson:02/18"
type: lesson
ref: 02/18
phase: 2
num: 18
title: Feature Selection
lesson_type: build
time_min: 75
on_route: false
quiz_count: 0
code_files: 1
concepts: 10
prereqs: 9
community: 4
libraries:
  - numpy
aliases:
  - 02/18
  - 02-18
tags:
  - phase/02
  - type/build
  - community/04
source: ai-engineering-from-scratch/phases/02-ml-fundamentals/18-feature-selection/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/02-ml-fundamentals/18-feature-selection"
---

# 02/18 Feature Selection

> More features is not better. The right features is better.

**Phase:** [[Phases/02 ML Fundamentals|Phase 2: ML Fundamentals]] · **Type:** Build · **Time:** 75 min · **Status:** —  
**Open:** [[Upstream/02-ml-fundamentals/18-feature-selection/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/02-ml-fundamentals/18-feature-selection) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/02-ml-fundamentals/18-feature-selection) · code: feature_selection.py  
**Community:** [[Communities/04 Overfitting · Underfitting · Data Leakage|04 Overfitting · Underfitting · Data Leakage]] · **Libraries:** [[Libraries/numpy (python)|numpy]]  

## Prerequisites

Stated upstream: `Phase 2, Lessons 01-09, 08 (feature engineering)`

- **02/01-09**:
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

## Concepts taught

- Filter method `lesson term` — A feature selection approach that ranks features using a statistical measure without training a model, evaluating each feature in isolation
- Wrapper method `lesson term` — A feature selection approach that evaluates feature subsets by training a model and using its performance as the selection criterion
- Embedded method `lesson term` — Feature selection that happens as part of model fitting, such as L1 regularization driving weights to zero
- [[Concepts/Mutual information|Mutual information]] `lesson term` — A measure of the reduction in uncertainty about Y given knowledge of X, capturing both linear and nonlinear dependencies
- Recursive Feature Elimination `lesson term` — An iterative wrapper method that trains a model, removes the least important feature(s), and repeats until a target count is reached
- L1 / Lasso regularization `lesson term` — Adding the sum of absolute weight values to the loss function, which drives unimportant feature weights to exactly zero
- Variance threshold `lesson term` — Dropping features whose variance across samples falls below a specified threshold, filtering out features that carry no information
- [[Concepts/Feature importance|Feature importance]] `lesson term` — A score indicating how much each feature contributes to model predictions, computed from split gains (trees) or coefficient magnitudes (linear)
- [[Concepts/Permutation importance|Permutation importance]] `lesson term` — Evaluating feature importance by randomly shuffling each feature's values and measuring the resulting drop in model performance
- [[Concepts/Curse of dimensionality|Curse of dimensionality]] `lesson term` — The phenomenon where adding features increases the volume of the feature space exponentially, making data sparse and distances meaningless

## Ships

- [[Artifacts/02-18 skill-feature-selector|skill-feature-selector]] `skill` — Quick reference decision tree for choosing the right feature selection method

## Further reading

- Stability Selection (Meinshausen & Buhlmann, 2010) ([link](https://arxiv.org/abs/0809.2932)) — combines subsampling with feature selection for robust, reproducible results
- Beware Default Random Forest Importances (Strobl et al., 2007) ([link](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-8-25)) — demonstrates the cardinality bias in tree-based importance and proposes conditional importance as an alternative
- An Introduction to Variable and Feature Selection (Guyon & Elisseeff, 2003) ([link](https://jmlr.org/papers/v3/guyon03a.html)) — the foundational survey on feature selection methods, still widely referenced
- scikit-learn Feature Selection Guide ([link](https://scikit-learn.org/stable/modules/feature_selection.html)) — practical reference for filter, wrapper, and embedded methods with code examples


%% ── my notes ── %%
