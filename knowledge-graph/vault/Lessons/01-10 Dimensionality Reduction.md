---
id: "lesson:01/10"
type: lesson
ref: 01/10
phase: 1
num: 10
title: Dimensionality Reduction
lesson_type: build
time_min: 90
on_route: false
quiz_count: 5
code_files: 1
concepts: 9
prereqs: 4
community: 8
libraries:
  - numpy
  - scikit-learn
  - umap
aliases:
  - 01/10
  - 01-10
tags:
  - phase/01
  - type/build
  - community/08
source: ai-engineering-from-scratch/phases/01-math-foundations/10-dimensionality-reduction/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/10-dimensionality-reduction"
---

# 01/10 Dimensionality Reduction

> High-dimensional data has structure. You find it by looking from the right angle.

**Phase:** [[Phases/01 Math Foundations|Phase 1: Math Foundations]] · **Type:** Build · **Time:** 90 min · **Status:** —  
**Open:** [[Upstream/01-math-foundations/10-dimensionality-reduction/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/10-dimensionality-reduction) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/01-math-foundations/10-dimensionality-reduction) · code: dim_reduction.py · quiz: 5 questions  
**Community:** [[Communities/08 Backpropagation · Gradient · Activation Function|08 Backpropagation · Gradient · Activation Function]] · **Libraries:** [[Libraries/numpy (python)|numpy]], [[Libraries/scikit-learn (python)|scikit-learn]], [[Libraries/umap (python)|umap]]  

## Prerequisites

Stated upstream: `Phase 1, Lessons 01 (Linear Algebra Intuition), 02 (Vectors, Matrices & Operations), 03 (Eigenvalues & Eigenvectors), 06 (Probability & Distributions)`

- [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]] — Linear Algebra Intuition
- [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]] — Vectors, Matrices & Operations
- [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]] — Eigenvalues & Eigenvectors
- [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]] — Probability & Distributions

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]]

## Concepts taught

- [[Concepts/Curse of dimensionality|Curse of dimensionality]] `lesson term` — Distances, volumes, and data density all behave counterintuitively as dimensions grow. Models need exponentially more data to compensate.
- PCA `lesson term` — Rotate your coordinate system so the axes align with the directions of maximum variance, then drop the low-variance axes.
- Principal component `lesson term` — An eigenvector of the covariance matrix. The direction in feature space along which the data varies most.
- Explained variance ratio `lesson term` — The fraction of total variance captured by one principal component. Sum the top k ratios to see how much k components preserve.
- [[Concepts/Covariance matrix|Covariance matrix]] `lesson term` — A symmetric matrix where entry (i,j) measures how feature i and feature j move together. Diagonal entries are individual variances.
- t-SNE `lesson term` — A nonlinear method that maps high-dimensional data to 2D by preserving pairwise neighborhood probabilities. Good for visualization, not for preprocessing.
- [[Concepts/UMAP|UMAP]] `lesson term` — A nonlinear method based on topological data analysis. Preserves both local and some global structure. Scales better than t-SNE.
- [[Concepts/Perplexity|Perplexity]] `glossary` — Controls the effective number of neighbors each point considers. Low perplexity focuses on very local structure. High perplexity captures broader patterns.
- Manifold `lesson term` — A lower-dimensional surface embedded in a higher-dimensional space. A sheet of paper crumpled in 3D is a 2D manifold.

## Ships

- [[Artifacts/01-10 skill-dimensionality-reduction|skill-dimensionality-reduction]] `skill` — Choose the right dimensionality reduction technique for a given task based on data size, goal, and downstream use

## Further reading

- A Tutorial on Principal Component Analysis ([link](https://arxiv.org/abs/1404.1100)) — (Shlens) - clear derivation of PCA from the ground up
- How to Use t-SNE Effectively ([link](https://distill.pub/2016/misread-tsne/)) — (Wattenberg et al.) - interactive guide to t-SNE pitfalls and parameter choices
- UMAP documentation ([link](https://umap-learn.readthedocs.io/)) — theory and practical guidance from the UMAP authors


%% ── my notes ── %%
