---
id: "lesson:02/05"
type: lesson
ref: 02/05
phase: 2
num: 5
title: Support Vector Machines
lesson_type: build
time_min: 90
on_route: false
quiz_count: 0
code_files: 2
concepts: 13
prereqs: 3
community: 4
aliases:
  - 02/05
  - 02-05
tags:
  - phase/02
  - type/build
  - community/04
  - stdlib-only
source: ai-engineering-from-scratch/phases/02-ml-fundamentals/05-support-vector-machines/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/02-ml-fundamentals/05-support-vector-machines"
---

# 02/05 Support Vector Machines

> Find the widest street between two classes. That is the entire idea.

**Phase:** [[Phases/02 ML Fundamentals|Phase 2: ML Fundamentals]] · **Type:** Build · **Time:** 90 min · **Status:** —  
**Open:** [[Upstream/02-ml-fundamentals/05-support-vector-machines/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/02-ml-fundamentals/05-support-vector-machines) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/02-ml-fundamentals/05-support-vector-machines) · code: main.jl, svm.py  
**Community:** [[Communities/04 Overfitting · Underfitting · Data Leakage|04 Overfitting · Underfitting · Data Leakage]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 1 (Lessons 08 Optimization, 14 Norms and Distances, 18 Convex Optimization)`

- [[Lessons/01-08 Optimization|01/08 Optimization]] — Optimization
- [[Lessons/01-14 Norms and Distances|01/14 Norms and Distances]] — Norms and Distances
- [[Lessons/01-18 Convex Optimization|01/18 Convex Optimization]] — Convex Optimization

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]], [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]], [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]], [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]]
- depth 3: [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]]

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

- Support vectors `lesson term` — The training points closest to the decision boundary. The only points that determine the hyperplane
- Margin `lesson term` — The distance between the decision boundary and the nearest support vectors. SVMs maximize this
- Hinge loss `lesson term` — max(0, 1 - yf(x)). Zero when correctly classified and outside the margin. Linear penalty otherwise
- C parameter `lesson term` — Trade-off between margin width and classification errors. Large C = narrow margin, small C = wide margin
- Soft margin `lesson term` — SVM formulation that allows margin violations via slack variables. Handles non-separable data
- Kernel trick `lesson term` — Computing dot products in a high-dimensional feature space without explicitly mapping to that space
- Linear kernel `lesson term` — K(x, z) = x . z. Equivalent to standard dot product. For linearly separable data
- RBF kernel `lesson term` — K(x, z) = exp(-gamma ||x-z||^2). Maps to infinite dimensions. Learns any smooth boundary
- Polynomial kernel `lesson term` — K(x, z) = (x . z + c)^d. Maps to a feature space of polynomial combinations
- Dual formulation `lesson term` — Reformulation of the SVM problem that depends only on dot products between data points. Enables kernels
- SVR `lesson term` — Support Vector Regression. Fits an epsilon-tube around the data. Points inside the tube have zero loss
- Slack variables `lesson term` — xi_i: measures how much a point violates the margin. Zero for correctly classified points outside margin
- Maximum margin `lesson term` — The principle of choosing the hyperplane that maximizes the distance to the nearest points of each class

## Ships

- [[Artifacts/02-05 skill-svm-kernel-chooser|skill-svm-kernel-chooser]] `skill` — Choose the right SVM kernel and tune C and gamma for your problem

## Further reading

- LIBSVM: A Library for Support Vector Machines ([link](https://www.csie.ntu.edu.tw/~cjlin/libsvm/)) — the C++ library behind most SVM implementations
- Cortes & Vapnik: Support-vector networks (1995) ([link](https://link.springer.com/article/10.1007/BF00994018)) — the original SVM paper
- Vapnik: The Nature of Statistical Learning Theory (1995) ([link](https://link.springer.com/book/10.1007/978-1-4757-3264-1)) — the foundational text on SVMs and statistical learning
- Platt: Sequential Minimal Optimization (1998) ([link](https://www.microsoft.com/en-us/research/publication/sequential-minimal-optimization-a-fast-algorithm-for-training-support-vector-machines/)) — the SMO algorithm that made SVM training practical
- scikit-learn SVM documentation ([link](https://scikit-learn.org/stable/modules/svm.html)) — practical guide with implementation details


%% ── my notes ── %%
