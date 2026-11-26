---
id: "lesson:02/03"
type: lesson
ref: 02/03
phase: 2
num: 3
title: Logistic Regression
lesson_type: build
languages:
  - Python
time_min: 90
on_route: false
quiz_count: 0
code_files: 2
concepts: 12
prereqs: 2
community: 4
libraries:
  - numpy
  - scikit-learn
aliases:
  - 02/03
  - 02-03
tags:
  - phase/02
  - type/build
  - community/04
source: ai-engineering-from-scratch/phases/02-ml-fundamentals/03-logistic-regression/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/02-ml-fundamentals/03-logistic-regression"
---

# 02/03 Logistic Regression

> Logistic regression bends a straight line into an S-curve to answer yes-or-no questions with probabilities.

**Phase:** [[Phases/02 ML Fundamentals|Phase 2: ML Fundamentals]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/02-ml-fundamentals/03-logistic-regression/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/02-ml-fundamentals/03-logistic-regression) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/02-ml-fundamentals/03-logistic-regression) · code: logistic_regression.py, main.jl  
**Community:** [[Communities/04 Overfitting · Underfitting · Data Leakage|04 Overfitting · Underfitting · Data Leakage]] · **Libraries:** [[Libraries/numpy (python)|numpy]], [[Libraries/scikit-learn (python)|scikit-learn]]  

## Prerequisites

Stated upstream: `Phase 2 Lesson 1-2 (What Is ML, Linear Regression)`

- **02/01-02** — What Is ML, Linear Regression:
    - [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]]
    - [[Lessons/02-02 Linear Regression|02/02 Linear Regression]]

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

## Concepts taught

- Logistic regression `lesson term` — A linear model followed by a sigmoid function that outputs class probabilities
- Sigmoid function `lesson term` — The function 1/(1+e^(-z)) that maps any real number to the range (0, 1)
- [[Concepts/Binary cross-entropy|Binary cross-entropy]] `lesson term` — The loss function -[ylog(p) + (1-y)log(1-p)] that penalizes confident wrong predictions severely
- [[Concepts/Decision boundary|Decision boundary]] `lesson term` — The surface where the model's output probability equals 0.5, separating predicted classes
- [[Concepts/Softmax|Softmax]] `glossary` — A function that converts a vector of scores into probabilities that sum to 1
- [[Concepts/Precision|Precision]] `lesson term` — TP / (TP + FP), the fraction of positive predictions that are actually positive
- [[Concepts/Recall|Recall]] `lesson term` — TP / (TP + FN), the fraction of actual positives that the model correctly identifies
- F1 score `lesson term` — The harmonic mean of precision and recall: 2PR / (P+R)
- [[Concepts/Confusion matrix|Confusion matrix]] `lesson term` — A table showing TP, TN, FP, FN counts for each class pair
- Threshold `lesson term` — The probability value above which the model predicts class 1 (default 0.5, tunable)
- [[Concepts/One-hot encoding|One-hot encoding]] `lesson term` — Representing class k as a vector of zeros with a 1 at position k
- Categorical cross-entropy `lesson term` — The extension of binary cross-entropy to k classes using one-hot encoded labels

## Ships

- [[Artifacts/02-03 skill-classification-baseline|skill-classification-baseline]] `skill` — Establish a strong classification baseline before reaching for complex models


%% ── my notes ── %%
