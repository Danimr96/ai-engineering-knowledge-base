---
id: "lesson:01/14"
type: lesson
ref: 01/14
phase: 1
num: 14
title: Norms and Distances
lesson_type: build
time_min: 90
on_route: false
quiz_count: 5
code_files: 1
concepts: 18
prereqs: 2
community: 18
aliases:
  - 01/14
  - 01-14
tags:
  - phase/01
  - type/build
  - community/18
  - stdlib-only
source: ai-engineering-from-scratch/phases/01-math-foundations/14-norms-and-distances/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/14-norms-and-distances"
---

# 01/14 Norms and Distances

> Your distance function defines what "similar" means. Choose wrong and everything downstream breaks.

**Phase:** [[Phases/01 Math Foundations|Phase 1: Math Foundations]] · **Type:** Build · **Time:** 90 min · **Status:** —  
**Open:** [[Upstream/01-math-foundations/14-norms-and-distances/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/14-norms-and-distances) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/01-math-foundations/14-norms-and-distances) · code: distances.py · quiz: 5 questions  
**Community:** [[Communities/18 Embedding · Cosine Similarity · HNSW|18 Embedding · Cosine Similarity · HNSW]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 1, Lessons 01 (Linear Algebra Intuition), 02 (Vectors, Matrices & Operations)`

- [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]] — Linear Algebra Intuition
- [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]] — Vectors, Matrices & Operations

## Builds on this

- [[Lessons/02-05 Support Vector Machines|02/05 Support Vector Machines]]
- [[Lessons/02-06 K-Nearest Neighbors and Distances|02/06 K-Nearest Neighbors and Distances]]
- [[Lessons/06-01 Audio Fundamentals — Waveforms, Sampling, Fourier Transform|06/01 Audio Fundamentals — Waveforms, Sampling, Fourier Transform]]

## Concepts taught

- Norm `lesson term` — A function that maps a vector to a non-negative scalar, satisfying triangle inequality, absolute homogeneity, and zero only for the zero vector
- L1 norm `lesson term` — Sum of absolute component values. Produces sparsity in optimization. Robust to outliers
- L2 norm `lesson term` — Square root of sum of squared components. The straight-line distance in Euclidean space
- Lp norm `lesson term` — The p-th root of the sum of p-th powers of absolute components. L1 and L2 are special cases
- L-infinity norm `lesson term` — The maximum absolute component value. The limit of Lp as p approaches infinity
- [[Concepts/Cosine Similarity|Cosine Similarity]] `glossary` — Dot product normalized by both magnitudes. Ranges from -1 to +1. Ignores vector length
- Cosine distance `lesson term` — Converts cosine similarity to a distance. Ranges from 0 to 2
- [[Concepts/Dot product|Dot product]] `lesson term` — Sum of component-wise products. Equals cosine similarity times both magnitudes
- Mahalanobis distance `lesson term` — L2 distance in a space that has been whitened (decorrelated and normalized) using the data covariance matrix
- Jaccard similarity `lesson term` — Size of intersection divided by size of union. For sets, not vectors
- Edit distance `lesson term` — Minimum insertions, deletions, and substitutions to transform one string into another
- [[Concepts/KL divergence|KL divergence]] `lesson term` — Not a true distance (not symmetric). Measures extra bits from using Q to encode P
- Wasserstein distance `lesson term` — Minimum work to transport mass from one distribution to another. A true metric
- [[Concepts/Approximate Nearest Neighbor (ANN)|Approximate Nearest Neighbor (ANN)]] (as *Approximate nearest neighbor*) `glossary` — Algorithms (HNSW, LSH, IVF) that find approximately closest points much faster than exact search
- [[Concepts/HNSW|HNSW]] `glossary` — Hierarchical Navigable Small World graph. Multi-layer graph for fast approximate nearest neighbor search
- L1 regularization `lesson term` — Adding the L1 norm of weights to the loss. Drives weights to zero (sparsity)
- [[Concepts/L2 regularization|L2 regularization]] `lesson term` — Adding the squared L2 norm of weights to the loss. Shrinks weights toward zero without sparsity
- Elastic Net `lesson term` — Combines L1 and L2 regularization. Handles correlated feature groups better than either alone

## Ships

- [[Artifacts/01-14 prompt-distance-chooser|prompt-distance-chooser]] `prompt` — Guides the user through choosing the right distance metric for their specific task

## Further reading

- Efficient Estimation of Word Representations (Mikolov et al., 2013) ([link](https://arxiv.org/abs/1301.3781)) — Word2Vec, where cosine similarity became the default for embeddings
- [[Resources/Wasserstein GAN (Arjovsky et al., 2017)|Wasserstein GAN (Arjovsky et al., 2017)]] ([link](https://arxiv.org/abs/1701.07875)) — the paper that introduced Earth Mover's distance to GANs ·  also cited by 1 other lesson
- Locality-Sensitive Hashing (Indyk & Motwani, 1998) ([link](https://dl.acm.org/doi/10.1145/276698.276876)) — foundational ANN algorithm
- [[Resources/FAISS- A Library for Efficient Similarity Search|FAISS: A Library for Efficient Similarity Search]] ([link](https://github.com/facebookresearch/faiss)) — Meta's library for billion-scale ANN search ·  also cited by 1 other lesson
- [[Resources/sklearn.neighbors documentation|sklearn.neighbors documentation]] ([link](https://scikit-learn.org/stable/modules/neighbors.html)) — practical guide to distance metrics and neighbor algorithms in scikit-learn ·  also cited by 1 other lesson


%% ── my notes ── %%
