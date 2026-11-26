---
id: "lesson:01/17"
type: lesson
ref: 01/17
phase: 1
num: 17
title: Linear Systems
lesson_type: build
time_min: 120
on_route: false
quiz_count: 5
code_files: 1
concepts: 15
prereqs: 3
community: 8
libraries:
  - numpy
  - scikit-learn
aliases:
  - 01/17
  - 01-17
tags:
  - phase/01
  - type/build
  - community/08
source: ai-engineering-from-scratch/phases/01-math-foundations/17-linear-systems/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/17-linear-systems"
---

# 01/17 Linear Systems

> Solving Ax = b is the oldest problem in mathematics that still runs your neural network.

**Phase:** [[Phases/01 Math Foundations|Phase 1: Math Foundations]] · **Type:** Build · **Time:** 120 min · **Status:** —  
**Open:** [[Upstream/01-math-foundations/17-linear-systems/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/17-linear-systems) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/01-math-foundations/17-linear-systems) · code: linear_systems.py · quiz: 5 questions  
**Community:** [[Communities/08 Backpropagation · Gradient · Activation Function|08 Backpropagation · Gradient · Activation Function]] · **Libraries:** [[Libraries/numpy (python)|numpy]], [[Libraries/scikit-learn (python)|scikit-learn]]  

## Prerequisites

Stated upstream: `Phase 1, Lessons 01 (Linear Algebra Intuition), 02 (Vectors & Matrices), 03 (Matrix Transformations)`

- [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]] — Linear Algebra Intuition
- [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]] — Vectors & Matrices
- [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]] — Matrix Transformations

## Concepts taught

- Linear system `lesson term` — A set of linear equations Ax = b. Finding x means finding the input that produces output b under transformation A.
- Gaussian elimination `lesson term` — Systematically zero out entries below the diagonal using row operations, producing an upper triangular system solvable by back substitution. O(n^3).
- Partial pivoting `lesson term` — Before eliminating in column k, swap the row with the largest absolute value in that column to the pivot position. Prevents division by small numbers.
- LU decomposition `lesson term` — Write A = LU where L is lower triangular (stores multipliers) and U is upper triangular (the eliminated matrix). Amortizes the O(n^3) cost over multiple solves.
- QR decomposition `lesson term` — Write A = QR where Q has orthonormal columns and R is upper triangular. More stable than LU for least squares.
- Cholesky decomposition `lesson term` — For symmetric positive definite A, write A = LL^T. Half the cost of LU. Used for covariance matrices, kernel matrices, and ridge regression.
- Least squares `lesson term` — ^2 when the system is overdetermined (more equations than unknowns).
- Normal equations `lesson term` — ^2 to zero. This IS the closed-form solution to linear regression.
- [[Concepts/Pseudoinverse|Pseudoinverse]] `lesson term` — A+ = V Sigma+ U^T via SVD. Gives the minimum-norm least-squares solution for any matrix, square or rectangular, singular or not.
- [[Concepts/Condition number|Condition number]] `lesson term` — kappa = sigma_max / sigma_min. Measures sensitivity to input perturbations. Lose about log10(kappa) digits of precision.
- [[Concepts/Ridge regression|Ridge regression]] `lesson term` — Solve (X^T X + lambda I) w = X^T y. Adding lambda I improves conditioning and shrinks weights toward zero. Prevents overfitting.
- Conjugate gradient `lesson term` — An iterative solver for symmetric positive definite systems. Converges in at most n steps. Practical for large sparse systems where factorization is too expensive.
- Overdetermined system `lesson term` — m > n in an m-by-n system. No exact solution exists. Least squares finds the best approximation. This is every regression problem.
- Back substitution `lesson term` — Given an upper triangular system, solve the last equation first, then substitute backward. O(n^2).
- Forward substitution `lesson term` — Given a lower triangular system, solve the first equation first, then substitute forward. O(n^2). Used in the L step of LU solves.

## Ships

- [[Artifacts/01-17 prompt-linear-solver|prompt-linear-solver]] `prompt` — Recommend the right algorithm for solving a linear system Ax=b based on matrix properties

## Further reading

- 3Blue1Brown: Inverse Matrices ([link](https://www.3blue1brown.com/lessons/inverse-matrices)) — visual intuition for what solving Ax = b means geometrically
- Matrix Computations ([link](https://www.cs.cornell.edu/cv/GolubVanLoan4/golubandvanloan.htm)) — (Golub & Van Loan) -- the encyclopedic reference for every matrix algorithm
- [[Resources/MIT 18.06 Lecture 21- Eigenvalues and Eigenvectors|MIT 18.06 Lecture 21: Eigenvalues and Eigenvectors]] ([link](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)) — (Gilbert Strang) -- the definitive course on linear systems and matrix factorizations ·  also cited by 1 other lesson
- [[Resources/Numerical Linear Algebra by Trefethen and Bau|Numerical Linear Algebra by Trefethen and Bau]] ([link](https://people.maths.ox.ac.uk/trefethen/text.html)) — (Trefethen & Bau) -- the standard reference for understanding numerical stability, conditioning, and why algorithms fail ·  also cited by 1 other lesson


%% ── my notes ── %%
