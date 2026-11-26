---
id: "lesson:02/16"
type: lesson
ref: 02/16
phase: 2
num: 16
title: Anomaly Detection
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
  - 02/16
  - 02-16
tags:
  - phase/02
  - type/build
  - community/04
source: ai-engineering-from-scratch/phases/02-ml-fundamentals/16-anomaly-detection/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/02-ml-fundamentals/16-anomaly-detection"
---

# 02/16 Anomaly Detection

> Normal is easy to define. Abnormal is whatever doesn't fit.

**Phase:** [[Phases/02 ML Fundamentals|Phase 2: ML Fundamentals]] · **Type:** Build · **Time:** 75 min · **Status:** —  
**Open:** [[Upstream/02-ml-fundamentals/16-anomaly-detection/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/02-ml-fundamentals/16-anomaly-detection) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/02-ml-fundamentals/16-anomaly-detection) · code: anomaly_detection.py  
**Community:** [[Communities/04 Overfitting · Underfitting · Data Leakage|04 Overfitting · Underfitting · Data Leakage]] · **Libraries:** [[Libraries/numpy (python)|numpy]]  

## Prerequisites

Stated upstream: `Phase 2, Lessons 01-09`

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

- [[Concepts/Anomaly|Anomaly]] `lesson term` — A data point that deviates significantly from the expected pattern of normal data
- Point anomaly `lesson term` — An individual observation that is unusual regardless of context
- Contextual anomaly `lesson term` — An observation that is unusual given its context (time, location, etc.) but might be normal in another context
- Isolation Forest `lesson term` — An ensemble of random trees that isolates anomalies with fewer splits than normal points
- Local Outlier Factor `lesson term` — A method that flags points whose local density is much lower than their neighbors' density
- Z-score `lesson term` — (x - mean) / std, measuring how far a point is from the center in units of standard deviation
- [[Concepts/IQR|IQR]] `lesson term` — Q3 - Q1, measuring the spread of the middle 50% of data, used for robust outlier detection
- [[Concepts/Benchmark Contamination|Benchmark Contamination]] (as *Contamination*) `glossary` — A hyperparameter telling the detector what proportion of the data it should flag as anomalous
- [[Concepts/Precision@k|Precision@k]] `lesson term` — Precision computed on only the k most suspicious points, useful for imbalanced anomaly detection
- [[Concepts/AUPRC|AUPRC]] `lesson term` — A metric that summarizes precision-recall performance across all thresholds, better than AUROC for imbalanced data

## Ships

- [[Artifacts/02-16 skill-anomaly-detector|skill-anomaly-detector]] `skill` — Choose the right anomaly detection approach for your problem

## Further reading

- Liu et al., Isolation Forest (2008) ([link](https://cs.nju.edu.cn/zhouzh/zhouzh.files/publication/icdm08b.pdf)) — the original Isolation Forest paper
- Chandola et al., Anomaly Detection: A Survey (2009) ([link](https://dl.acm.org/doi/10.1145/1541880.1541882)) — comprehensive survey of anomaly detection methods
- Breunig et al., LOF: Identifying Density-Based Local Outliers (2000) ([link](https://dl.acm.org/doi/10.1145/342009.335388)) — the original LOF paper
- Goldstein and Uchida, A Comparative Evaluation of Unsupervised Anomaly Detection Algorithms (2016) ([link](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0152173)) — empirical comparison of 10 methods on real datasets
- scikit-learn Outlier Detection docs ([link](https://scikit-learn.org/stable/modules/outlier_detection.html)) — overview of all sklearn anomaly detectors


%% ── my notes ── %%
