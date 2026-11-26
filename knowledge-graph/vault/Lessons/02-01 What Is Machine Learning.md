---
id: "lesson:02/01"
type: lesson
ref: 02/01
phase: 2
num: 1
title: What Is Machine Learning
lesson_type: learn
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 0
code_files: 1
concepts: 12
prereqs: 0
community: 4
libraries:
  - numpy
aliases:
  - 02/01
  - 02-01
tags:
  - phase/02
  - type/learn
  - community/04
source: ai-engineering-from-scratch/phases/02-ml-fundamentals/01-what-is-machine-learning/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/02-ml-fundamentals/01-what-is-machine-learning"
---

# 02/01 What Is Machine Learning

> Machine learning is teaching computers to find patterns in data instead of writing rules by hand.

**Phase:** [[Phases/02 ML Fundamentals|Phase 2: ML Fundamentals]] · **Type:** Learn · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/02-ml-fundamentals/01-what-is-machine-learning/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/02-ml-fundamentals/01-what-is-machine-learning) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/02-ml-fundamentals/01-what-is-machine-learning) · code: ml_intro.py  
**Community:** [[Communities/04 Overfitting · Underfitting · Data Leakage|04 Overfitting · Underfitting · Data Leakage]] · **Libraries:** [[Libraries/numpy (python)|numpy]]  

## Prerequisites

Stated upstream: `Phase 1 (Math Foundations)`

- Whole phase: [[Phases/01 Math Foundations|Phase 1: Math Foundations]] — Math Foundations ·  medium confidence

## Builds on this

- [[Lessons/02-02 Linear Regression|02/02 Linear Regression]]
- [[Lessons/02-03 Logistic Regression|02/03 Logistic Regression]]
- [[Lessons/02-07 Unsupervised Learning|02/07 Unsupervised Learning]]
- [[Lessons/02-08 Feature Engineering & Selection|02/08 Feature Engineering & Selection]]
- [[Lessons/02-09 Model Evaluation|02/09 Model Evaluation]]
- [[Lessons/02-10 Bias-Variance Tradeoff|02/10 Bias-Variance Tradeoff]]
- [[Lessons/02-14 Naive Bayes|02/14 Naive Bayes]]
- [[Lessons/02-15 Time Series Fundamentals|02/15 Time Series Fundamentals]]
- [[Lessons/02-16 Anomaly Detection|02/16 Anomaly Detection]]
- [[Lessons/02-17 Handling Imbalanced Data|02/17 Handling Imbalanced Data]]
- [[Lessons/02-18 Feature Selection|02/18 Feature Selection]]
- [[Lessons/09-01 MDPs, States, Actions & Rewards|09/01 MDPs, States, Actions & Rewards]]

## Concepts taught

- Model `lesson term` — A mathematical function with learnable parameters that maps inputs to outputs
- Training `lesson term` — Running an optimization algorithm to adjust model parameters so predictions match known outputs
- [[Concepts/Feature|Feature]] `glossary` — A measurable property of the data that the model uses to make predictions
- Label `lesson term` — The known output for a training example, used to compute the error signal
- [[Concepts/Hyperparameter|Hyperparameter]] `glossary` — A parameter set before training that controls the learning process (learning rate, number of layers)
- [[Concepts/Loss Function|Loss Function]] `glossary` — A function that measures the gap between predicted and actual outputs, which training tries to minimize
- [[Concepts/Overfitting|Overfitting]] `glossary` — The model learned training-specific noise instead of general patterns, so it fails on new data
- [[Concepts/Underfitting|Underfitting]] `glossary` — The model is too simple to capture the real patterns in the data
- Generalization `lesson term` — The model's ability to make accurate predictions on data it was not trained on
- [[Concepts/Cross-validation|Cross-validation]] `lesson term` — Repeatedly splitting data into train/test folds and averaging results, giving a more robust performance estimate
- [[Concepts/Regularization|Regularization]] `lesson term` — Adding a penalty term to the loss function that discourages overly complex models
- Data drift `lesson term` — The statistical distribution of incoming data shifts over time, degrading model performance

## Ships

- [[Artifacts/02-01 prompt-ml-problem-framer|prompt-ml-problem-framer]] `prompt` — Frame a real-world business problem as a machine learning task

## Further reading

- Google's Machine Learning Crash Course ([link](https://developers.google.com/machine-learning/crash-course)) — concise visual introduction to ML concepts
- Scikit-learn User Guide ([link](https://scikit-learn.org/stable/user_guide.html)) — the practical reference for implementing ML in Python
- [[Resources/An Introduction to Statistical Learning|An Introduction to Statistical Learning]] ([link](https://www.statlearning.com/)) — free textbook covering all classical ML methods with practical examples ·  also cited by 1 other lesson


%% ── my notes ── %%
