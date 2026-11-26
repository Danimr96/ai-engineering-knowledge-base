---
id: "lesson:02/04"
type: lesson
ref: 02/04
phase: 2
num: 4
title: Decision Trees and Random Forests
lesson_type: build
time_min: 90
on_route: false
quiz_count: 0
code_files: 1
concepts: 12
prereqs: 2
community: 4
aliases:
  - 02/04
  - 02-04
tags:
  - phase/02
  - type/build
  - community/04
  - stdlib-only
source: ai-engineering-from-scratch/phases/02-ml-fundamentals/04-decision-trees/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/02-ml-fundamentals/04-decision-trees"
---

# 02/04 Decision Trees and Random Forests

> A decision tree is just a flowchart. But a forest of them is one of the most powerful tools in ML.

**Phase:** [[Phases/02 ML Fundamentals|Phase 2: ML Fundamentals]] · **Type:** Build · **Time:** 90 min · **Status:** —  
**Open:** [[Upstream/02-ml-fundamentals/04-decision-trees/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/02-ml-fundamentals/04-decision-trees) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/02-ml-fundamentals/04-decision-trees) · code: trees.py  
**Community:** [[Communities/04 Overfitting · Underfitting · Data Leakage|04 Overfitting · Underfitting · Data Leakage]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 1 (Lessons 09 Information Theory, 06 Probability)`

- [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]] — Probability
- [[Lessons/01-09 Information Theory|01/09 Information Theory]] — Information Theory

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]], [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]], [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]], [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]]

## Builds on this

- [[Lessons/02-07 Unsupervised Learning|02/07 Unsupervised Learning]]
- [[Lessons/02-08 Feature Engineering & Selection|02/08 Feature Engineering & Selection]]
- [[Lessons/02-09 Model Evaluation|02/09 Model Evaluation]]
- [[Lessons/02-10 Bias-Variance Tradeoff|02/10 Bias-Variance Tradeoff]]
- [[Lessons/02-14 Naive Bayes|02/14 Naive Bayes]]
- [[Lessons/02-15 Time Series Fundamentals|02/15 Time Series Fundamentals]]
- [[Lessons/02-16 Anomaly Detection|02/16 Anomaly Detection]]
- [[Lessons/02-17 Handling Imbalanced Data|02/17 Handling Imbalanced Data]]
- [[Lessons/02-18 Feature Selection|02/18 Feature Selection]]
- [[Lessons/08-14 Evaluation — FID, CLIP Score, Human Preference|08/14 Evaluation — FID, CLIP Score, Human Preference]]

## Concepts taught

- Decision tree `lesson term` — A model that partitions feature space into rectangular regions by learning a sequence of if/else splits
- Gini impurity `lesson term` — Probability of misclassifying a random sample at a node. 0 = pure, 0.5 = maximum impurity for binary
- [[Concepts/Entropy|Entropy]] `lesson term` — Information content at a node. 0 = pure, 1.0 = maximum uncertainty for binary. From information theory
- Information gain `lesson term` — Reduction in impurity after a split. The greedy criterion for choosing splits
- Pre-pruning `lesson term` — Stopping tree growth early by setting max depth, min samples, or min gain thresholds
- Post-pruning `lesson term` — Growing the full tree, then removing subtrees that do not improve validation performance
- [[Concepts/Bagging|Bagging]] `lesson term` — Bootstrap aggregating. Train each model on a different random sample with replacement
- [[Concepts/Random forest|Random forest]] `lesson term` — Ensemble of decision trees, each trained on a bootstrap sample with random feature subsets at each split
- [[Concepts/Feature importance|Feature importance]] (as *Feature importance (MDI)*) `lesson term` — Total impurity decrease contributed by each feature, summed across all trees and nodes
- [[Concepts/Permutation importance|Permutation importance]] `lesson term` — Accuracy drop when a feature's values are randomly shuffled. More reliable than MDI for noisy features
- Variance reduction `lesson term` — The regression tree analogue of information gain. Picks the split that reduces target variance the most
- Bootstrap sample `lesson term` — A random sample drawn with replacement from the original dataset. Same size, but with duplicates

## Ships

- [[Artifacts/02-04 prompt-tree-interpreter|prompt-tree-interpreter]] `prompt` — Interpret decision tree results and diagnose potential issues

## Further reading

- [[Resources/XGBoost- A Scalable Tree Boosting System (Chen & Guestrin, 2016)|XGBoost: A Scalable Tree Boosting System (Chen & Guestrin, 2016)]] ([link](https://arxiv.org/abs/1603.02754)) — the gradient boosting paper that dominates Kaggle ·  also cited by 1 other lesson
- Grinsztajn et al.: Why do tree-based models still outperform deep learning on tabular data? (2022) ([link](https://arxiv.org/abs/2207.08815)) — rigorous comparison of trees vs neural networks on tabular tasks
- Breiman: Random Forests (2001) ([link](https://link.springer.com/article/10.1023/A:1010933404324)) — the original random forest paper
- scikit-learn Decision Trees documentation ([link](https://scikit-learn.org/stable/modules/tree.html)) — practical guide with visualization tools


%% ── my notes ── %%
