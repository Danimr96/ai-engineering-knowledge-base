---
id: "lesson:01/08"
type: lesson
ref: 01/08
phase: 1
num: 8
title: Optimization
lesson_type: build
time_min: 75
on_route: false
quiz_count: 5
code_files: 2
concepts: 12
prereqs: 2
community: 11
aliases:
  - 01/08
  - 01-08
tags:
  - phase/01
  - type/build
  - community/11
  - stdlib-only
source: ai-engineering-from-scratch/phases/01-math-foundations/08-optimization/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/08-optimization"
---

# 01/08 Optimization

> Training a neural network is nothing more than finding the bottom of a valley.

**Phase:** [[Phases/01 Math Foundations|Phase 1: Math Foundations]] · **Type:** Build · **Time:** 75 min · **Status:** —  
**Open:** [[Upstream/01-math-foundations/08-optimization/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/08-optimization) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/01-math-foundations/08-optimization) · code: main.jl, optimizers.py · quiz: 5 questions  
**Community:** [[Communities/11 Learning Rate · Optimizer · Batch Size|11 Learning Rate · Optimizer · Batch Size]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 1, Lessons 04-05 (Derivatives, Gradients)`

- **01/04-05** — Derivatives, Gradients:
    - [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]]
    - [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]]

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]], [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]], [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]]

## Builds on this

- [[Lessons/01-18 Convex Optimization|01/18 Convex Optimization]]
- [[Lessons/02-05 Support Vector Machines|02/05 Support Vector Machines]]

## Concepts taught

- [[Concepts/Gradient Descent|Gradient Descent]] `glossary` — Update weights by subtracting the gradient scaled by the learning rate. The most basic optimizer.
- [[Concepts/Learning Rate|Learning Rate]] `glossary` — A scalar that controls how far each update moves the weights. Too large causes divergence. Too small wastes compute.
- [[Concepts/Momentum|Momentum]] `lesson term` — Accumulate past gradients into a velocity vector. Dampens oscillations and accelerates movement through consistent directions.
- [[Concepts/Stochastic Gradient Descent (SGD)|Stochastic Gradient Descent (SGD)]] (as *SGD*) `glossary` — Stochastic gradient descent. Compute gradient on a random subset instead of the full dataset. Almost always means mini-batch SGD in practice.
- Mini-batch `lesson term` — A small subset of training data (32-256 samples) used to estimate the gradient. Balances speed and gradient accuracy.
- [[Concepts/Adam (Optimizer)|Adam (Optimizer)]] (as *Adam*) `glossary` — Adaptive Moment Estimation. Tracks per-weight running averages of gradients and squared gradients to give each weight its own learning rate.
- [[Concepts/Bias correction|Bias correction]] `lesson term` — Adam's first and second moments are initialized to zero. Bias correction divides by (1 - beta^t) to compensate during early steps.
- [[Concepts/Learning Rate Schedule|Learning Rate Schedule]] `glossary` — A function that adjusts the learning rate during training. Large steps early, small steps late.
- [[Concepts/Convex function|Convex function]] `lesson term` — A function where any local minimum is the global minimum. Gradient descent always finds it. Neural network losses are not convex.
- [[Concepts/Saddle point|Saddle point]] `lesson term` — A point where the gradient is zero but it is a minimum in some directions and a maximum in others. Common in high dimensions.
- Loss landscape `lesson term` — The loss function plotted over weight space. Visualized by slicing along two random directions.
- [[Concepts/Convergence|Convergence]] `lesson term` — The optimizer has reached a point where further steps do not meaningfully reduce the loss.

## Ships

- [[Artifacts/01-08 prompt-optimizer-guide|prompt-optimizer-guide]] `prompt` — Guides the user through choosing the right optimizer for their specific machine learning problem

## Further reading

- Adam paper ([link](https://arxiv.org/abs/1412.6980)) — the original Adam paper, readable and short
- Visualizing the Loss Landscape of Neural Nets (Li et al., 2018) ([link](https://arxiv.org/abs/1712.09913)) — the paper that showed sharp vs flat minima
- Why Momentum Really Works (Distill) ([link](https://distill.pub/2017/momentum/)) — interactive visualization of momentum dynamics
- Sebastian Ruder: An overview of gradient descent optimization algorithms ([link](https://ruder.io/optimizing-gradient-descent/)) — comprehensive survey of all major optimizers


%% ── my notes ── %%
