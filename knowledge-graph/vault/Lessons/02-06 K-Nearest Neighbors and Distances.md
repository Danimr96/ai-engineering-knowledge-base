---
id: "lesson:02/06"
type: lesson
ref: 02/06
phase: 2
num: 6
title: K-Nearest Neighbors and Distances
lesson_type: build
time_min: 90
on_route: false
quiz_count: 0
code_files: 1
concepts: 12
prereqs: 1
community: 4
aliases:
  - 02/06
  - 02-06
tags:
  - phase/02
  - type/build
  - community/04
  - stdlib-only
source: ai-engineering-from-scratch/phases/02-ml-fundamentals/06-knn-and-distances/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/02-ml-fundamentals/06-knn-and-distances"
---

# 02/06 K-Nearest Neighbors and Distances

> Store everything. Predict by looking at your neighbors. The simplest algorithm that actually works.

**Phase:** [[Phases/02 ML Fundamentals|Phase 2: ML Fundamentals]] · **Type:** Build · **Time:** 90 min · **Status:** —  
**Open:** [[Upstream/02-ml-fundamentals/06-knn-and-distances/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/02-ml-fundamentals/06-knn-and-distances) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/02-ml-fundamentals/06-knn-and-distances) · code: knn.py  
**Community:** [[Communities/04 Overfitting · Underfitting · Data Leakage|04 Overfitting · Underfitting · Data Leakage]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 1 (Lesson 14 Norms and Distances)`

- [[Lessons/01-14 Norms and Distances|01/14 Norms and Distances]] — Norms and Distances

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]], [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]]

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

- K-nearest neighbors `lesson term` — Non-parametric algorithm that predicts by finding the K closest training points to a query
- Lazy learning `lesson term` — No computation at training time. All work happens at prediction time. KNN is the canonical example
- Eager learning `lesson term` — Heavy computation at training time to build a compact model. Most ML algorithms are eager
- [[Concepts/Curse of dimensionality|Curse of dimensionality]] `lesson term` — In high dimensions, distances converge and neighborhoods expand to cover most of the space, making KNN ineffective
- KD-tree `lesson term` — Binary tree that recursively partitions space along feature axes. O(log n) queries in low dimensions
- Ball tree `lesson term` — Tree of nested hyperspheres. Works better than KD-trees in moderate dimensions (up to ~50)
- Weighted KNN `lesson term` — Neighbors weighted inversely by distance. Closer neighbors have more influence on the prediction
- [[Concepts/Feature scaling|Feature scaling]] `lesson term` — Normalizing features to comparable ranges. Required for distance-based methods like KNN
- Majority vote `lesson term` — Classification by counting which class is most common among K neighbors
- Brute force search `lesson term` — Computing distance to every training point. O(nd) per query. Exact but slow for large n
- [[Concepts/Approximate Nearest Neighbor (ANN)|Approximate Nearest Neighbor (ANN)]] (as *Approximate nearest neighbor*) `glossary` — Algorithms (HNSW, LSH, IVF) that find approximately nearest points much faster than exact search
- Voronoi diagram `lesson term` — The partition of space where each region contains all points closer to one training point than any other. K=1 KNN produces Voronoi boundaries

## Ships

- [[Artifacts/02-06 prompt-distance-metric-advisor|prompt-distance-metric-advisor]] `prompt` — Recommend the right distance metric based on data type and problem characteristics

## Further reading

- Friedman, Bentley, Finkel: An Algorithm for Finding Best Matches in Logarithmic Expected Time (1977) ([link](https://dl.acm.org/doi/10.1145/355744.355745)) — the original KD-tree paper
- [[Resources/FAISS- A Library for Efficient Similarity Search|FAISS: A Library for Efficient Similarity Search]] ([link](https://github.com/facebookresearch/faiss)) — Meta's library for billion-scale approximate nearest neighbor search ·  also cited by 1 other lesson
- Cover & Hart: Nearest Neighbor Pattern Classification (1967) ([link](https://ieeexplore.ieee.org/document/1053964)) — the foundational KNN paper proving it has error rate at most twice the Bayes optimal
- Beyer et al.: When Is "Nearest Neighbor" Meaningful? (1999) ([link](https://link.springer.com/chapter/10.1007/3-540-49257-7_15)) — formal analysis of the curse of dimensionality for nearest neighbor
- [[Resources/sklearn.neighbors documentation|sklearn.neighbors documentation]] ([link](https://scikit-learn.org/stable/modules/neighbors.html)) — practical guide with algorithm selection ·  also cited by 1 other lesson


%% ── my notes ── %%
