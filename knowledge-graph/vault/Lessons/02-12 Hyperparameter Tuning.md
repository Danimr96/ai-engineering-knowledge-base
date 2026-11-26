---
id: "lesson:02/12"
type: lesson
ref: 02/12
phase: 2
num: 12
title: Hyperparameter Tuning
lesson_type: build
time_min: 90
on_route: false
quiz_count: 0
code_files: 1
concepts: 9
prereqs: 1
community: 11
libraries:
  - numpy
  - optuna
aliases:
  - 02/12
  - 02-12
tags:
  - phase/02
  - type/build
  - community/11
source: ai-engineering-from-scratch/phases/02-ml-fundamentals/12-hyperparameter-tuning/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/02-ml-fundamentals/12-hyperparameter-tuning"
---

# 02/12 Hyperparameter Tuning

> Hyperparameters are the knobs you turn before training starts. Turning them well is the difference between a mediocre model and a great one.

**Phase:** [[Phases/02 ML Fundamentals|Phase 2: ML Fundamentals]] · **Type:** Build · **Time:** 90 min · **Status:** —  
**Open:** [[Upstream/02-ml-fundamentals/12-hyperparameter-tuning/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/02-ml-fundamentals/12-hyperparameter-tuning) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/02-ml-fundamentals/12-hyperparameter-tuning) · code: tuning.py  
**Community:** [[Communities/11 Learning Rate · Optimizer · Batch Size|11 Learning Rate · Optimizer · Batch Size]] · **Libraries:** [[Libraries/numpy (python)|numpy]], [[Libraries/optuna (python)|optuna]]  

## Prerequisites

Stated upstream: `Phase 2, Lesson 11 (Ensemble Methods)`

- [[Lessons/02-11 Ensemble Methods|02/11 Ensemble Methods]] — Ensemble Methods

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/02-10 Bias-Variance Tradeoff|02/10 Bias-Variance Tradeoff]]
- depth 3: [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]], [[Lessons/02-02 Linear Regression|02/02 Linear Regression]], [[Lessons/02-03 Logistic Regression|02/03 Logistic Regression]], [[Lessons/02-04 Decision Trees and Random Forests|02/04 Decision Trees and Random Forests]], [[Lessons/02-05 Support Vector Machines|02/05 Support Vector Machines]], [[Lessons/02-06 K-Nearest Neighbors and Distances|02/06 K-Nearest Neighbors and Distances]], [[Lessons/02-07 Unsupervised Learning|02/07 Unsupervised Learning]], [[Lessons/02-08 Feature Engineering & Selection|02/08 Feature Engineering & Selection]], [[Lessons/02-09 Model Evaluation|02/09 Model Evaluation]]

## Builds on this

- [[Lessons/02-13 ML Pipelines|02/13 ML Pipelines]]

## Concepts taught

- [[Concepts/Hyperparameter|Hyperparameter]] `glossary` — A value set before training that controls the learning process, not learned from data
- Grid search `lesson term` — Exhaustive search over a specified parameter grid. Exponential cost.
- Random search `lesson term` — Sample hyperparameters from distributions. Covers important dimensions better than grid search.
- Bayesian optimization `lesson term` — Uses a surrogate model of the objective to decide where to evaluate next, balancing exploration and exploitation
- Surrogate model `lesson term` — A model (usually Gaussian process) that approximates the expensive objective function from observed evaluations
- Acquisition function `lesson term` — Scores candidate points by balancing expected improvement with uncertainty. EI and UCB are common choices.
- [[Concepts/Early stopping|Early stopping]] `lesson term` — Terminate training early when validation performance stops improving
- Hyperband `lesson term` — Adaptive resource allocation: start many configs with small budgets, keep the best and increase their budgets
- [[Concepts/Learning Rate Schedule|Learning Rate Schedule]] (as *Learning rate scheduler*) `glossary` — A function that adjusts the learning rate over the course of training for better convergence

## Ships

- [[Artifacts/02-12 prompt-tuning-strategy|prompt-tuning-strategy]] `prompt` — Recommend a hyperparameter tuning strategy based on model type, data size, and compute budget

## Further reading

- Snoek et al., Practical Bayesian Optimization of Machine Learning Algorithms (2012) ([link](https://arxiv.org/abs/1206.2944)) — Bayesian optimization for ML
- Optuna: A Next-generation Hyperparameter Optimization Framework ([link](https://arxiv.org/abs/1907.10902)) — the Optuna paper
- Bergstra & Bengio: Random Search for Hyper-Parameter Optimization (2012) ([link](https://jmlr.org/papers/v13/bergstra12a.html)) — the paper that showed random beats grid
- Li et al., Hyperband: A Novel Bandit-Based Approach (2018) ([link](https://jmlr.org/papers/v18/16-558.html)) — the Hyperband paper
- Probst et al., Tunability: Importance of Hyperparameters (2019) ([link](https://jmlr.org/papers/v20/18-444.html)) — which hyperparameters matter


%% ── my notes ── %%
