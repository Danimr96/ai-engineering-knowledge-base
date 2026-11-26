---
id: "lesson:01/11"
type: lesson
ref: 01/11
phase: 1
num: 11
title: Singular Value Decomposition
lesson_type: build
languages:
  - Python
  - Julia
time_min: 120
on_route: false
quiz_count: 5
code_files: 2
concepts: 12
prereqs: 3
community: 8
libraries:
  - numpy
  - scikit-learn
aliases:
  - 01/11
  - 01-11
tags:
  - phase/01
  - type/build
  - community/08
source: ai-engineering-from-scratch/phases/01-math-foundations/11-singular-value-decomposition/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/11-singular-value-decomposition"
---

# 01/11 Singular Value Decomposition

> SVD is the Swiss Army knife of linear algebra. Every matrix has one. Every data scientist needs one.

**Phase:** [[Phases/01 Math Foundations|Phase 1: Math Foundations]] · **Type:** Build · **Time:** 120 min · **Languages:** Python, Julia · **Status:** —  
**Open:** [[Upstream/01-math-foundations/11-singular-value-decomposition/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/11-singular-value-decomposition) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/01-math-foundations/11-singular-value-decomposition) · code: svd.jl, svd.py · quiz: 5 questions  
**Community:** [[Communities/08 Backpropagation · Gradient · Activation Function|08 Backpropagation · Gradient · Activation Function]] · **Libraries:** [[Libraries/numpy (python)|numpy]], [[Libraries/scikit-learn (python)|scikit-learn]]  

## Prerequisites

Stated upstream: `Phase 1, Lessons 01 (Linear Algebra Intuition), 02 (Vectors & Matrices Operations), 03 (Matrix Transformations)`

- [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]] — Linear Algebra Intuition
- [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]] — Vectors & Matrices Operations
- [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]] — Matrix Transformations

## Concepts taught

- SVD `lesson term` — Decompose A into U Sigma V^T where U and V are orthogonal and Sigma is diagonal with non-negative entries. Works for any matrix of any shape.
- Singular value `lesson term` — The i-th diagonal entry of Sigma. Measures how much the matrix stretches along the i-th principal direction. Always non-negative, sorted in decreasing order.
- Left singular vector `lesson term` — A column of U. The direction in output space that the i-th right singular vector maps to (after scaling by sigma_i).
- Right singular vector `lesson term` — A column of V. The direction in input space that the matrix maps to the i-th left singular vector (after scaling by sigma_i).
- Truncated SVD `lesson term` — Keep only the top k singular values and their vectors. Produces the provably best rank-k approximation to the original matrix (Eckart-Young theorem).
- [[Concepts/Rank|Rank]] `lesson term` — The number of non-zero singular values. Tells you how many independent directions the matrix actually uses.
- [[Concepts/Pseudoinverse|Pseudoinverse]] `lesson term` — V Sigma+ U^T. Inverts non-zero singular values, leaves zeros as zeros. Solves least-squares problems for non-square or singular matrices.
- [[Concepts/Condition number|Condition number]] `lesson term` — sigma_max / sigma_min. A large condition number means small input changes cause large output changes. SVD reveals this directly.
- Latent factor `lesson term` — A dimension in the low-rank space discovered by SVD. In recommendations, a latent factor might correspond to genre preference. In NLP, it might correspond to a topic.
- Frobenius norm `lesson term` — Square root of the sum of squared entries. Equals the square root of the sum of squared singular values. Used to measure approximation error.
- Eckart-Young theorem `lesson term` — For any target rank k, the truncated SVD minimizes the approximation error over all possible rank-k matrices.
- Power iteration `lesson term` — Repeatedly multiply a random vector by the matrix and normalize. Converges to the eigenvector with the largest eigenvalue. The building block of many SVD algorithms.

## Ships

- [[Artifacts/01-11 skill-svd|skill-svd]] `skill` — Apply SVD to real problems including compression, denoising, recommendations, and least-squares solving

## Further reading

- We Recommend a Singular Value Decomposition ([link](https://www.ams.org/publicoutreach/feature-column/fcarc-svd)) — accessible overview from the American Mathematical Society
- Latent Semantic Analysis ([link](https://en.wikipedia.org/wiki/Latent_semantic_analysis)) — the original NLP application of SVD
- [[Resources/Gilbert Strang- Linear Algebra and Its Applications, Chapter 7|Gilbert Strang: Linear Algebra and Its Applications, Chapter 7]] ([link](https://math.mit.edu/~gs/linearalgebra/)) — thorough treatment of SVD with applications ·  also cited by 1 other lesson
- [[Resources/Numerical Linear Algebra by Trefethen and Bau|Numerical Linear Algebra by Trefethen and Bau]] ([link](https://people.maths.ox.ac.uk/trefethen/text.html)) — the gold standard for understanding SVD algorithms and their numerical properties ·  also cited by 1 other lesson
- Netflix Prize and Matrix Factorization ([link](https://sifter.org/~simon/journal/20061211.html)) — Simon Funk's original blog post on SVD for recommendations
- 3Blue1Brown: But what is the SVD? ([link](https://www.youtube.com/watch?v=vSczTbgc8Rc)) — geometric intuition for SVD


%% ── my notes ── %%
