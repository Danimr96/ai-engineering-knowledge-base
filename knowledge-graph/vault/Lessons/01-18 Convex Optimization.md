---
id: "lesson:01/18"
type: lesson
ref: 01/18
phase: 1
num: 18
title: Convex Optimization
lesson_type: build
time_min: 90
on_route: false
quiz_count: 5
code_files: 1
concepts: 16
prereqs: 2
aliases:
  - 01/18
  - 01-18
tags:
  - phase/01
  - type/build
  - stdlib-only
source: ai-engineering-from-scratch/phases/01-math-foundations/18-convex-optimization/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/18-convex-optimization"
---

# 01/18 Convex Optimization

> Convex problems have one valley. Neural networks have millions. Knowing the difference matters.

**Phase:** [[Phases/01 Math Foundations|Phase 1: Math Foundations]] · **Type:** Build · **Time:** 90 min · **Status:** —  
**Open:** [[Upstream/01-math-foundations/18-convex-optimization/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/18-convex-optimization) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/01-math-foundations/18-convex-optimization) · code: convex.py · quiz: 5 questions  
**Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 1, Lessons 04 (Calculus for ML), 08 (Optimization)`

- [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]] — Calculus for ML
- [[Lessons/01-08 Optimization|01/08 Optimization]] — Optimization

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]], [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]], [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]], [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]]

## Builds on this

- [[Lessons/02-05 Support Vector Machines|02/05 Support Vector Machines]]

## Concepts taught

- Convex set `lesson term` — A set where the line segment between any two points in the set stays inside the set
- [[Concepts/Convex function|Convex function]] `lesson term` — A function where the line between any two points on its graph lies above or on the graph. Equivalently, Hessian is positive semidefinite everywhere
- Local minimum `lesson term` — A point lower than all nearby points. For convex functions, every local minimum is the global minimum
- Global minimum `lesson term` — The lowest point of a function over its entire domain
- Hessian matrix `lesson term` — The matrix of all second partial derivatives. Encodes curvature information
- Positive semidefinite `lesson term` — A matrix whose eigenvalues are all non-negative. The multidimensional analogue of "second derivative >= 0"
- [[Concepts/Condition number|Condition number]] `lesson term` — Ratio of largest to smallest eigenvalue of the Hessian. High condition number means elongated valleys and slow gradient descent
- Newton's method `lesson term` — Second-order optimizer that uses the inverse Hessian to determine step direction and size. Quadratic convergence near the minimum
- Lagrange multiplier `lesson term` — A variable introduced to convert a constrained optimization problem into an unconstrained one
- KKT conditions `lesson term` — Necessary conditions for optimality with inequality constraints. Generalize Lagrange multipliers
- Complementary slackness `lesson term` — At the solution, either a constraint is active or its multiplier is zero. Never both nonzero
- Duality `lesson term` — Every constrained problem has a companion dual problem. For convex problems, both have the same optimal value
- Strong duality `lesson term` — Primal and dual optimal values are equal. Holds for convex problems satisfying Slater's condition
- L-BFGS `lesson term` — Approximate second-order method that stores the last m gradient differences instead of the full Hessian
- [[Concepts/Saddle point|Saddle point]] `lesson term` — A point where the gradient is zero but it is a minimum in some directions and a maximum in others
- Overparameterization `lesson term` — Using more parameters than training examples. Smooths the loss landscape and reduces bad local minima

## Ships

- [[Artifacts/01-18 skill-convexity-checker|skill-convexity-checker]] `skill` — Determine if an optimization problem is convex and choose the right solver

## Further reading

- Choromanska et al.: The Loss Surfaces of Multilayer Networks (2015) ([link](https://arxiv.org/abs/1412.0233)) — why non-convex neural network landscapes are not as bad as they seem
- Optimization Methods for Large-Scale Machine Learning ([link](https://arxiv.org/abs/1606.04838)) — bridges convex optimization theory and deep learning practice
- Nocedal & Wright: Numerical Optimization ([link](https://link.springer.com/book/10.1007/978-0-387-40065-5)) — comprehensive reference for Newton's method, L-BFGS, and constrained optimization
- Boyd & Vandenberghe: Convex Optimization ([link](https://web.stanford.edu/~boyd/cvxbook/)) — the standard textbook, freely available online


%% ── my notes ── %%
