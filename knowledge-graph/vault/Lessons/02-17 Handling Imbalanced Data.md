---
id: "lesson:02/17"
type: lesson
ref: 02/17
phase: 2
num: 17
title: Handling Imbalanced Data
lesson_type: build
time_min: 90
on_route: false
quiz_count: 0
code_files: 1
concepts: 9
prereqs: 9
community: 4
libraries:
  - numpy
aliases:
  - 02/17
  - 02-17
tags:
  - phase/02
  - type/build
  - community/04
source: ai-engineering-from-scratch/phases/02-ml-fundamentals/17-imbalanced-data/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/02-ml-fundamentals/17-imbalanced-data"
---

# 02/17 Handling Imbalanced Data

> When 99% of your data is "normal," accuracy is a lie.

**Phase:** [[Phases/02 ML Fundamentals|Phase 2: ML Fundamentals]] · **Type:** Build · **Time:** 90 min · **Status:** —  
**Open:** [[Upstream/02-ml-fundamentals/17-imbalanced-data/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/02-ml-fundamentals/17-imbalanced-data) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/02-ml-fundamentals/17-imbalanced-data) · code: imbalanced.py  
**Community:** [[Communities/04 Overfitting · Underfitting · Data Leakage|04 Overfitting · Underfitting · Data Leakage]] · **Libraries:** [[Libraries/numpy (python)|numpy]]  

## Prerequisites

Stated upstream: `Phase 2, Lessons 01-09 (especially evaluation metrics)`

- **02/01-09** — especially evaluation metrics:
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

- Class imbalance `lesson term` — The distribution of classes in the dataset is significantly skewed, causing models to favor the majority class
- SMOTE `lesson term` — Creates new minority samples by interpolating between existing minority samples and their k-nearest minority neighbors
- Class weights `lesson term` — Multiplying the loss function by class-specific weights so the model penalizes minority misclassification more heavily
- Threshold tuning `lesson term` — Changing the probability cutoff for classification from the default 0.5 to a value that optimizes the desired metric
- Precision-recall tradeoff `lesson term` — Lowering the threshold catches more positives (higher recall) but also flags more false positives (lower precision), and vice versa
- [[Concepts/AUPRC|AUPRC]] `lesson term` — Summarizes the precision-recall curve into a single number; more informative than AUC-ROC when classes are heavily imbalanced
- Matthews Correlation Coefficient `lesson term` — A correlation between predicted and actual labels that produces a high score only when the model performs well on both classes
- Cost-sensitive learning `lesson term` — Incorporating real-world misclassification costs into the training objective so the model optimizes for total cost, not error count
- Random oversampling `lesson term` — Repeating minority class samples to balance class counts; simple but risks overfitting to duplicated points

## Ships

- [[Artifacts/02-17 skill-imbalanced-data|skill-imbalanced-data]] `skill` — Decision checklist for handling imbalanced classification problems

## Further reading

- SMOTE: Synthetic Minority Over-sampling Technique (Chawla et al., 2002) ([link](https://arxiv.org/abs/1106.1813)) — the original SMOTE paper, still the most cited work on imbalanced learning
- Learning from Imbalanced Data (He & Garcia, 2009) ([link](https://ieeexplore.ieee.org/document/5128907)) — comprehensive survey covering sampling, cost-sensitive, and algorithmic approaches
- imbalanced-learn documentation ([link](https://imbalanced-learn.org/stable/)) — Python library with SMOTE variants, undersampling strategies, and pipeline integration
- The Precision-Recall Plot Is More Informative than the ROC Plot (Saito & Rehmsmeier, 2015) ([link](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0118432)) — when and why to prefer PR curves over ROC curves for imbalanced problems


%% ── my notes ── %%
