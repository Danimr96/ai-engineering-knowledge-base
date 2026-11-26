---
id: "lesson:01/03"
type: lesson
ref: 01/03
phase: 1
num: 3
title: Matrix Transformations
lesson_type: build
languages:
  - Python
  - Julia
time_min: 75
on_route: false
quiz_count: 5
code_files: 2
concepts: 10
prereqs: 2
community: 8
libraries:
  - numpy
aliases:
  - 01/03
  - 01-03
tags:
  - phase/01
  - type/build
  - community/08
source: ai-engineering-from-scratch/phases/01-math-foundations/03-matrix-transformations/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/03-matrix-transformations"
---

# 01/03 Matrix Transformations

> A matrix is a machine that reshapes space. Learn what it does to every point, and you understand the whole transformation.

**Phase:** [[Phases/01 Math Foundations|Phase 1: Math Foundations]] · **Type:** Build · **Time:** 75 min · **Languages:** Python, Julia · **Status:** —  
**Open:** [[Upstream/01-math-foundations/03-matrix-transformations/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/03-matrix-transformations) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/01-math-foundations/03-matrix-transformations) · code: transformations.jl, transformations.py · quiz: 5 questions  
**Community:** [[Communities/08 Backpropagation · Gradient · Activation Function|08 Backpropagation · Gradient · Activation Function]] · **Libraries:** [[Libraries/numpy (python)|numpy]]  

## Prerequisites

Stated upstream: `Phase 1, Lessons 01-02 (Linear Algebra Intuition, Vectors & Matrices Operations)`

- **01/01-02** — Linear Algebra Intuition, Vectors & Matrices Operations:
    - [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]]
    - [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]]

## Builds on this

- [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]]
- [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]]
- [[Lessons/01-10 Dimensionality Reduction|01/10 Dimensionality Reduction]]
- [[Lessons/01-11 Singular Value Decomposition|01/11 Singular Value Decomposition]]
- [[Lessons/01-13 Numerical Stability|01/13 Numerical Stability]]
- [[Lessons/01-17 Linear Systems|01/17 Linear Systems]]
- [[Lessons/01-19 Complex Numbers for AI|01/19 Complex Numbers for AI]]
- [[Lessons/01-20 The Fourier Transform|01/20 The Fourier Transform]]
- [[Lessons/01-21 Graph Theory for Machine Learning|01/21 Graph Theory for Machine Learning]]

## Concepts taught

- Rotation matrix `lesson term` — An orthogonal matrix that moves points along circular arcs while preserving distances and angles. Determinant is always 1.
- Scaling matrix `lesson term` — A diagonal matrix that stretches or compresses independently along each axis. Determinant is the product of scale factors.
- Shearing matrix `lesson term` — A matrix that shifts one coordinate proportionally to another, turning rectangles into parallelograms. Determinant is 1.
- [[Concepts/Reflection|Reflection]] `lesson term` — A matrix that flips space across an axis or plane. Determinant is -1.
- [[Concepts/Composition|Composition]] `lesson term` — Multiplying transformation matrices to chain operations. Order matters: B @ A means apply A first, then B.
- Eigenvector `lesson term` — A direction that the matrix only scales, never rotates. The transformation's fingerprint.
- [[Concepts/Eigenvalue|Eigenvalue]] `glossary` — The scalar factor by which the matrix scales its eigenvector. Can be negative (flip) or complex (rotation).
- Eigendecomposition `lesson term` — Writing a matrix as V @ D @ V^(-1), separating it into its fundamental scaling directions and magnitudes.
- [[Concepts/Determinant|Determinant]] `lesson term` — The factor by which the transformation scales area (2D) or volume (3D). Zero means the transformation is irreversible.
- Characteristic equation `lesson term` — det(A - lambda I) = 0. The polynomial whose roots are the eigenvalues.

## Ships

- [[Artifacts/01-03 prompt-transformation-visualizer|prompt-transformation-visualizer]] `prompt` — Explain what a matrix transformation does geometrically given its entries

## Further reading

- 3Blue1Brown: Eigenvectors and Eigenvalues ([link](https://www.3blue1brown.com/lessons/eigenvalues)) — the best visual explanation of what eigenvectors mean geometrically
- 3Blue1Brown: Linear Transformations ([link](https://www.3blue1brown.com/lessons/linear-transformations)) — visual intuition for how matrices reshape space
- [[Resources/MIT 18.06 Lecture 21- Eigenvalues and Eigenvectors|MIT 18.06 Lecture 21: Eigenvalues and Eigenvectors]] ([link](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)) — Gilbert Strang's classic treatment ·  also cited by 1 other lesson


%% ── my notes ── %%
