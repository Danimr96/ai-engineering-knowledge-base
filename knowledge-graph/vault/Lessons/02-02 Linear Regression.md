---
id: "lesson:02/02"
type: lesson
ref: 02/02
phase: 2
num: 2
title: Linear Regression
lesson_type: build
languages:
  - Python
time_min: 90
on_route: false
quiz_count: 0
code_files: 2
concepts: 12
prereqs: 1
community: 4
libraries:
  - numpy
  - scikit-learn
aliases:
  - 02/02
  - 02-02
tags:
  - phase/02
  - type/build
  - community/04
source: ai-engineering-from-scratch/phases/02-ml-fundamentals/02-linear-regression/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/02-ml-fundamentals/02-linear-regression"
---

# 02/02 Linear Regression

> Linear regression draws the best straight line through your data. It is the "hello world" of machine learning.

**Phase:** [[Phases/02 ML Fundamentals|Phase 2: ML Fundamentals]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/02-ml-fundamentals/02-linear-regression/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/02-ml-fundamentals/02-linear-regression) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/02-ml-fundamentals/02-linear-regression) · code: linear_regression.py, main.jl  
**Community:** [[Communities/04 Overfitting · Underfitting · Data Leakage|04 Overfitting · Underfitting · Data Leakage]] · **Libraries:** [[Libraries/numpy (python)|numpy]], [[Libraries/scikit-learn (python)|scikit-learn]]  

## Prerequisites

Stated upstream: `Phase 1 (Linear Algebra, Calculus, Optimization), Phase 2 Lesson 1`

- [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]]
- Whole phase: [[Phases/01 Math Foundations|Phase 1: Math Foundations]] — Linear Algebra, Calculus, Optimization ·  medium confidence

## Builds on this

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
- [[Lessons/05-02 Bag of Words, TF-IDF, and Text Representation|05/02 Bag of Words, TF-IDF, and Text Representation]]

## Concepts taught

- Linear regression `lesson term` — Find weight w and bias b that minimize the sum of squared differences between wx+b and actual y values
- Cost function `lesson term` — A function that maps model parameters to a single number measuring prediction error, which optimization minimizes
- Mean squared error `lesson term` — (1/n) sum of (predicted - actual)^2, penalizing large errors disproportionately
- [[Concepts/Gradient Descent|Gradient Descent]] `glossary` — Iteratively adjust parameters in the direction that reduces the cost function, using partial derivatives
- [[Concepts/Learning Rate|Learning Rate]] `glossary` — A scalar that controls how much parameters change per gradient descent step
- Normal equation `lesson term` — The closed-form solution w = (X^T X)^-1 X^T y that gives optimal weights without iteration
- [[Concepts/R-squared|R-squared]] `lesson term` — The fraction of variance in y explained by the model, ranging from negative infinity to 1.0
- [[Concepts/Feature scaling|Feature scaling]] `lesson term` — Transforming features to similar ranges (e.g., zero mean, unit variance) so gradient descent converges faster
- [[Concepts/Regularization|Regularization]] `lesson term` — Adding a term to the cost function that shrinks weights, preventing overfitting
- [[Concepts/Ridge regression|Ridge regression]] `lesson term` — Linear regression with a penalty of lambda sum(w_i^2) added to MSE
- Polynomial regression `lesson term` — Linear regression on polynomial features (x, x^2, x^3, ...), still linear in the weights
- [[Concepts/Overfitting|Overfitting]] `glossary` — Using a model so complex that it fits noise in training data and fails on new data

## Ships

- [[Artifacts/02-02 skill-regression|skill-regression]] `skill` — Choose the right regression approach based on data characteristics and problem constraints

## Further reading

- Stanford CS229 Lecture Notes on Linear Regression ([link](https://cs229.stanford.edu/main_notes.pdf)) — Andrew Ng's notes deriving the normal equation and gradient descent from first principles
- [[Resources/The Elements of Statistical Learning (ESL)|The Elements of Statistical Learning (ESL)]] ([link](https://hastie.su.domains/ElemStatLearn/)) — free PDF, the more mathematical companion to ISLR with deeper treatment of ridge and lasso ·  also cited by 1 other lesson
- scikit-learn LinearRegression documentation ([link](https://scikit-learn.org/stable/modules/linear_model.html)) — practical reference for LinearRegression, Ridge, Lasso, and ElasticNet with code examples
- [[Resources/An Introduction to Statistical Learning|An Introduction to Statistical Learning]] ([link](https://www.statlearning.com/)) — free PDF, chapters 3 and 6 cover linear regression and regularization with practical R examples ·  also cited by 1 other lesson


%% ── my notes ── %%
