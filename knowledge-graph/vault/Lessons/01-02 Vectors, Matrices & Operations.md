---
id: "lesson:01/02"
type: lesson
ref: 01/02
phase: 1
num: 2
title: "Vectors, Matrices & Operations"
lesson_type: build
languages:
  - Python
  - Julia
time_min: 60
on_route: false
quiz_count: 6
code_files: 2
concepts: 9
prereqs: 1
community: 8
aliases:
  - 01/02
  - 01-02
tags:
  - phase/01
  - type/build
  - community/08
  - stdlib-only
source: ai-engineering-from-scratch/phases/01-math-foundations/02-vectors-matrices-operations/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/02-vectors-matrices-operations"
---

# 01/02 Vectors, Matrices & Operations

> Every neural network is just matrix multiplication with extra steps.

**Phase:** [[Phases/01 Math Foundations|Phase 1: Math Foundations]] · **Type:** Build · **Time:** 60 min · **Languages:** Python, Julia · **Status:** —  
**Open:** [[Upstream/01-math-foundations/02-vectors-matrices-operations/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/02-vectors-matrices-operations) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/01-math-foundations/02-vectors-matrices-operations) · code: matrices.jl, matrices.py · quiz: 6 questions  
**Community:** [[Communities/08 Backpropagation · Gradient · Activation Function|08 Backpropagation · Gradient · Activation Function]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 1, Lesson 01 (Linear Algebra Intuition)`

- [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]] — Linear Algebra Intuition

## Builds on this

- [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]]
- [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]]
- [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]]
- [[Lessons/01-10 Dimensionality Reduction|01/10 Dimensionality Reduction]]
- [[Lessons/01-11 Singular Value Decomposition|01/11 Singular Value Decomposition]]
- [[Lessons/01-12 Tensor Operations|01/12 Tensor Operations]]
- [[Lessons/01-13 Numerical Stability|01/13 Numerical Stability]]
- [[Lessons/01-14 Norms and Distances|01/14 Norms and Distances]]
- [[Lessons/01-17 Linear Systems|01/17 Linear Systems]]
- [[Lessons/01-19 Complex Numbers for AI|01/19 Complex Numbers for AI]]
- [[Lessons/01-20 The Fourier Transform|01/20 The Fourier Transform]]
- [[Lessons/01-21 Graph Theory for Machine Learning|01/21 Graph Theory for Machine Learning]]

## Concepts taught

- [[Concepts/Vector|Vector]] `lesson term` — An ordered list of numbers. In AI: a point in high-dimensional space.
- [[Concepts/Matrix|Matrix]] `lesson term` — A linear transformation. It maps vectors from one space to another.
- Matrix multiply `lesson term` — Dot products between every row of the first matrix and every column of the second. Order matters.
- Transpose `lesson term` — Swap rows and columns. Turns an m x n matrix into n x m. Critical in backpropagation.
- [[Concepts/Determinant|Determinant]] `lesson term` — Measures how much the matrix scales area (2D) or volume (3D). Zero means the transformation crushes a dimension.
- Inverse `lesson term` — The matrix that reverses the transformation. Only exists when the determinant is not zero.
- Identity matrix `lesson term` — The matrix equivalent of multiplying by 1. Used in residual connections (ResNets).
- [[Concepts/Broadcasting|Broadcasting]] `lesson term` — Stretching a smaller array to match a larger one by repeating along missing dimensions.
- Element-wise `lesson term` — Multiply matching positions. Both arrays must have the same shape (or be broadcastable).

## Ships

- [[Artifacts/01-02 prompt-matrix-operations|prompt-matrix-operations]] `prompt` — Teaches matrix operations through geometric intuition, connecting abstract math to neural network mechanics

## Further reading

- 3Blue1Brown: Essence of Linear Algebra ([link](https://www.3blue1brown.com/topics/linear-algebra)) — visual intuition for every operation covered here
- Stanford CS229 Linear Algebra Review ([link](http://cs229.stanford.edu/section/cs229-linalg.pdf)) — concise reference for ML-specific linear algebra
- [[Resources/NumPy documentation on broadcasting|NumPy documentation on broadcasting]] ([link](https://numpy.org/doc/stable/user/basics.broadcasting.html)) — the exact rules NumPy follows ·  also cited by 1 other lesson


%% ── my notes ── %%
