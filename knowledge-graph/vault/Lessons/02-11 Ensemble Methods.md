---
id: "lesson:02/11"
type: lesson
ref: 02/11
phase: 2
num: 11
title: Ensemble Methods
lesson_type: build
time_min: 120
on_route: false
quiz_count: 0
code_files: 1
concepts: 9
prereqs: 1
community: 4
libraries:
  - numpy
  - scikit-learn
aliases:
  - 02/11
  - 02-11
tags:
  - phase/02
  - type/build
  - community/04
source: ai-engineering-from-scratch/phases/02-ml-fundamentals/11-ensemble-methods/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/02-ml-fundamentals/11-ensemble-methods"
---

# 02/11 Ensemble Methods

> A group of weak learners, combined correctly, becomes a strong learner. This is not a metaphor. It is a theorem.

**Phase:** [[Phases/02 ML Fundamentals|Phase 2: ML Fundamentals]] · **Type:** Build · **Time:** 120 min · **Status:** —  
**Open:** [[Upstream/02-ml-fundamentals/11-ensemble-methods/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/02-ml-fundamentals/11-ensemble-methods) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/02-ml-fundamentals/11-ensemble-methods) · code: ensembles.py  
**Community:** [[Communities/04 Overfitting · Underfitting · Data Leakage|04 Overfitting · Underfitting · Data Leakage]] · **Libraries:** [[Libraries/numpy (python)|numpy]], [[Libraries/scikit-learn (python)|scikit-learn]]  

## Prerequisites

Stated upstream: `Phase 2, Lesson 10 (Bias-Variance Tradeoff)`

- [[Lessons/02-10 Bias-Variance Tradeoff|02/10 Bias-Variance Tradeoff]] — Bias-Variance Tradeoff

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]], [[Lessons/02-02 Linear Regression|02/02 Linear Regression]], [[Lessons/02-03 Logistic Regression|02/03 Logistic Regression]], [[Lessons/02-04 Decision Trees and Random Forests|02/04 Decision Trees and Random Forests]], [[Lessons/02-05 Support Vector Machines|02/05 Support Vector Machines]], [[Lessons/02-06 K-Nearest Neighbors and Distances|02/06 K-Nearest Neighbors and Distances]], [[Lessons/02-07 Unsupervised Learning|02/07 Unsupervised Learning]], [[Lessons/02-08 Feature Engineering & Selection|02/08 Feature Engineering & Selection]], [[Lessons/02-09 Model Evaluation|02/09 Model Evaluation]]
- depth 3: [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/01-08 Optimization|01/08 Optimization]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/01-14 Norms and Distances|01/14 Norms and Distances]], [[Lessons/01-18 Convex Optimization|01/18 Convex Optimization]]

## Builds on this

- [[Lessons/02-12 Hyperparameter Tuning|02/12 Hyperparameter Tuning]]

## Concepts taught

- [[Concepts/Bagging|Bagging]] `lesson term` — Bootstrap aggregating: train models on bootstrap samples, average predictions to reduce variance
- Boosting `lesson term` — Train models sequentially, each correcting errors of the ensemble so far, to reduce bias
- AdaBoost `lesson term` — Boosting via sample weight updates; misclassified points get higher weight for the next learner
- Gradient boosting `lesson term` — Boosting via fitting each new model to the negative gradient of the loss function
- XGBoost `lesson term` — Gradient boosting with regularization, second-order optimization, and systems-level speed tricks
- Stacking `lesson term` — Use predictions of base models as input features for a meta-learner
- [[Concepts/Random forest|Random forest]] `lesson term` — Bagging with decision trees, adding random feature subsampling at each split for diversity
- Ensemble diversity `lesson term` — Models must be uncorrelated in their errors for the ensemble to improve over individuals
- Out-of-bag error `lesson term` — Samples not in a bootstrap draw (~36.8%) serve as a validation set without needing a holdout

## Ships

- [[Artifacts/02-11 prompt-ensemble-selector|prompt-ensemble-selector]] `prompt` — Pick the right ensemble method for a given dataset and problem
- [[Artifacts/02-11 skill-ensemble-builder|skill-ensemble-builder]] `skill` — Choose the right ensemble method and configure it for your problem

## Further reading

- [[Resources/XGBoost- A Scalable Tree Boosting System (Chen & Guestrin, 2016)|XGBoost: A Scalable Tree Boosting System (Chen & Guestrin, 2016)]] ([link](https://arxiv.org/abs/1603.02754)) — the XGBoost paper ·  also cited by 1 other lesson
- Schapire & Freund: Boosting: Foundations and Algorithms ([link](https://mitpress.mit.edu/9780262526036/)) — the book by AdaBoost's creators
- Wolpert: Stacked Generalization (1992) ([link](https://www.sciencedirect.com/science/article/abs/pii/S0893608005800231)) — the original stacking paper
- scikit-learn Ensemble Methods ([link](https://scikit-learn.org/stable/modules/ensemble.html)) — practical reference
- Friedman: Greedy Function Approximation: A Gradient Boosting Machine (2001) ([link](https://statweb.stanford.edu/~jhf/ftp/trebst.pdf)) — the original gradient boosting paper


%% ── my notes ── %%
