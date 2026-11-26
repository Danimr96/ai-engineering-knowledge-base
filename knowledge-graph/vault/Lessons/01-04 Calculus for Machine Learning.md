---
id: "lesson:01/04"
type: lesson
ref: 01/04
phase: 1
num: 4
title: Calculus for Machine Learning
lesson_type: learn
time_min: 60
on_route: false
quiz_count: 5
code_files: 2
concepts: 12
prereqs: 3
community: 8
aliases:
  - 01/04
  - 01-04
tags:
  - phase/01
  - type/learn
  - community/08
  - stdlib-only
source: ai-engineering-from-scratch/phases/01-math-foundations/04-calculus-for-ml/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/04-calculus-for-ml"
---

# 01/04 Calculus for Machine Learning

> Derivatives tell you which way is downhill. That is all a neural network needs to learn.

**Phase:** [[Phases/01 Math Foundations|Phase 1: Math Foundations]] · **Type:** Learn · **Time:** 60 min · **Status:** —  
**Open:** [[Upstream/01-math-foundations/04-calculus-for-ml/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/04-calculus-for-ml) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/01-math-foundations/04-calculus-for-ml) · code: derivatives.py, main.jl · quiz: 5 questions  
**Community:** [[Communities/08 Backpropagation · Gradient · Activation Function|08 Backpropagation · Gradient · Activation Function]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 1, Lessons 01-03`

- **01/01-03**:
    - [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]]
    - [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]]
    - [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]]

## Builds on this

- [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]]
- [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]]
- [[Lessons/01-08 Optimization|01/08 Optimization]]
- [[Lessons/01-13 Numerical Stability|01/13 Numerical Stability]]
- [[Lessons/01-18 Convex Optimization|01/18 Convex Optimization]]
- [[Lessons/01-19 Complex Numbers for AI|01/19 Complex Numbers for AI]]
- [[Lessons/01-20 The Fourier Transform|01/20 The Fourier Transform]]
- [[Lessons/08-13 Flow Matching & Rectified Flows|08/13 Flow Matching & Rectified Flows]]

## Concepts taught

- Derivative `lesson term` — The rate of change of a function at a point. Tells you how much the output changes per unit change in input.
- Partial derivative `lesson term` — The derivative with respect to one variable while all others are held constant.
- [[Concepts/Gradient|Gradient]] `glossary` — A vector of all partial derivatives. Points in the direction that increases the function fastest.
- [[Concepts/Gradient Descent|Gradient Descent]] `glossary` — Subtract the gradient (times a learning rate) from the parameters to reduce the loss. The core of neural network training.
- [[Concepts/Learning Rate|Learning Rate]] `glossary` — A scalar that controls how big each gradient descent step is. Too large: diverge. Too small: converge slowly.
- [[Concepts/Chain rule|Chain rule]] `lesson term` — The rule for differentiating composed functions: df/dx = df/dg dg/dx. The mathematical basis of backpropagation.
- Jacobian `lesson term` — When a function maps vectors to vectors, the Jacobian is the matrix of all partial derivatives of outputs with respect to inputs.
- Numerical derivative `lesson term` — Approximating a derivative by evaluating the function at two nearby points and computing the slope between them.
- [[Concepts/Backpropagation|Backpropagation]] `glossary` — Computing gradients layer by layer from output to input using the chain rule. How neural networks learn.
- Hessian `lesson term` — The matrix of all second-order partial derivatives. Describes the curvature of a function. Positive definite Hessian at a critical point means local minimum.
- Taylor series `lesson term` — Approximating a function near a point using its derivatives: f(x+h) ~ f(x) + f'(x)h + (1/2)f''(x)h^2 + ... The basis for understanding why gradient descent and Newton's method work.
- Integral `lesson term` — The accumulation of a quantity over a range. In ML, integrals define probabilities, expected values, and KL divergence.

## Ships

- [[Artifacts/01-04 skill-gradient-computation|skill-gradient-computation]] `skill` — Compute gradients of common ML loss functions and choose the right derivative approach

## Further reading

- 3Blue1Brown: Essence of Calculus ([link](https://www.3blue1brown.com/topics/calculus)) — visual intuition for derivatives, integrals, and the chain rule
- Stanford CS231n: Backpropagation ([link](https://cs231n.github.io/optimization-2/)) — how gradients flow through neural network layers


%% ── my notes ── %%
