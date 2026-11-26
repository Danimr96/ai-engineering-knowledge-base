---
id: "lesson:02/07"
type: lesson
ref: 02/07
phase: 2
num: 7
title: Unsupervised Learning
lesson_type: build
languages:
  - Python
time_min: 90
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 6
community: 4
aliases:
  - 02/07
  - 02-07
tags:
  - phase/02
  - type/build
  - community/04
  - stdlib-only
source: ai-engineering-from-scratch/phases/02-ml-fundamentals/07-unsupervised-learning/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/02-ml-fundamentals/07-unsupervised-learning"
---

# 02/07 Unsupervised Learning

> No labels, no teacher. The algorithm finds structure on its own.

**Phase:** [[Phases/02 ML Fundamentals|Phase 2: ML Fundamentals]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/02-ml-fundamentals/07-unsupervised-learning/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/02-ml-fundamentals/07-unsupervised-learning) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/02-ml-fundamentals/07-unsupervised-learning) · code: clustering.py  
**Community:** [[Communities/04 Overfitting · Underfitting · Data Leakage|04 Overfitting · Underfitting · Data Leakage]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 1 (Norms & Distances, Probability & Distributions), Phase 2 Lessons 1-6`

- **02/01-06**:
    - [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]]
    - [[Lessons/02-02 Linear Regression|02/02 Linear Regression]]
    - [[Lessons/02-03 Logistic Regression|02/03 Logistic Regression]]
    - [[Lessons/02-04 Decision Trees and Random Forests|02/04 Decision Trees and Random Forests]]
    - [[Lessons/02-05 Support Vector Machines|02/05 Support Vector Machines]]
    - [[Lessons/02-06 K-Nearest Neighbors and Distances|02/06 K-Nearest Neighbors and Distances]]
- Whole phase: [[Phases/01 Math Foundations|Phase 1: Math Foundations]] — Norms & Distances, Probability & Distributions ·  medium confidence

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/01-08 Optimization|01/08 Optimization]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/01-14 Norms and Distances|01/14 Norms and Distances]], [[Lessons/01-18 Convex Optimization|01/18 Convex Optimization]]
- depth 3: [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]], [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]], [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]], [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]], [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]]

## Builds on this

- [[Lessons/02-08 Feature Engineering & Selection|02/08 Feature Engineering & Selection]]
- [[Lessons/02-09 Model Evaluation|02/09 Model Evaluation]]
- [[Lessons/02-10 Bias-Variance Tradeoff|02/10 Bias-Variance Tradeoff]]
- [[Lessons/02-14 Naive Bayes|02/14 Naive Bayes]]
- [[Lessons/02-15 Time Series Fundamentals|02/15 Time Series Fundamentals]]
- [[Lessons/02-16 Anomaly Detection|02/16 Anomaly Detection]]
- [[Lessons/02-17 Handling Imbalanced Data|02/17 Handling Imbalanced Data]]
- [[Lessons/02-18 Feature Selection|02/18 Feature Selection]]

## Concepts taught

- Clustering `lesson term` — Partitioning data into subsets where within-group similarity exceeds between-group similarity, measured by a specific distance metric
- Centroid `lesson term` — The mean of all points assigned to a cluster; used by K-Means as the cluster representative
- Inertia `lesson term` — Sum of squared distances from each point to its assigned centroid; lower is tighter
- Silhouette score `lesson term` — For each point, (b - a) / max(a, b) where a is mean intra-cluster distance and b is mean nearest-cluster distance
- Core point `lesson term` — A point with at least min_samples neighbors within eps distance, in DBSCAN
- EM algorithm `lesson term` — Expectation-Maximization: iteratively compute membership probabilities (E-step) and update distribution parameters (M-step)
- Dendrogram `lesson term` — A tree diagram showing the order and distance at which clusters were merged in hierarchical clustering
- [[Concepts/Anomaly|Anomaly]] `lesson term` — A data point that does not conform to the expected pattern, identified as noise by DBSCAN or low-probability by GMM

## Ships

- [[Artifacts/02-07 skill-clustering-guide|skill-clustering-guide]] `skill` — Choose the right clustering algorithm based on data shape, noise, and constraints

## Further reading

- DBSCAN original paper (Ester et al., 1996) ([link](https://www.aaai.org/Papers/KDD/1996/KDD96-037.pdf)) — the paper that introduced density-based clustering
- Stanford CS229 - Unsupervised Learning ([link](https://cs229.stanford.edu/notes2022fall/main_notes.pdf)) — Andrew Ng's lecture notes on clustering and EM
- scikit-learn Clustering Guide ([link](https://scikit-learn.org/stable/modules/clustering.html)) — practical comparison of all clustering algorithms with visual examples


%% ── my notes ── %%
