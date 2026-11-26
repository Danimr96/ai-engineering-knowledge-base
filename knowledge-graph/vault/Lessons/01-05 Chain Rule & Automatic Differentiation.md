---
id: "lesson:01/05"
type: lesson
ref: 01/05
phase: 1
num: 5
title: "Chain Rule & Automatic Differentiation"
lesson_type: build
time_min: 90
on_route: false
quiz_count: 5
code_files: 2
concepts: 13
prereqs: 1
community: 82
libraries:
  - torch
aliases:
  - 01/05
  - 01-05
tags:
  - phase/01
  - type/build
  - community/82
source: ai-engineering-from-scratch/phases/01-math-foundations/05-chain-rule-and-autodiff/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/05-chain-rule-and-autodiff"
---

# 01/05 Chain Rule & Automatic Differentiation

> The chain rule is the engine behind every neural network that learns.

**Phase:** [[Phases/01 Math Foundations|Phase 1: Math Foundations]] · **Type:** Build · **Time:** 90 min · **Status:** —  
**Open:** [[Upstream/01-math-foundations/05-chain-rule-and-autodiff/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/05-chain-rule-and-autodiff) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/01-math-foundations/05-chain-rule-and-autodiff) · code: autodiff.py, main.jl · quiz: 5 questions  
**Community:** [[Communities/82 Computational graph · Gradient checking · Topological sort|82 Computational graph · Gradient checking · Topological sort]] · **Libraries:** [[Libraries/torch (python)|torch]]  

## Prerequisites

Stated upstream: `Phase 1, Lesson 04 (Derivatives & Gradients)`

- [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]] — Derivatives & Gradients

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]], [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]], [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]]

## Builds on this

- [[Lessons/01-08 Optimization|01/08 Optimization]]

## Concepts taught

- [[Concepts/Chain rule|Chain rule]] `lesson term` — The derivative of composed functions equals the product of each function's local derivative, evaluated at the right point
- [[Concepts/Computational graph|Computational graph]] `lesson term` — A directed acyclic graph where nodes are operations and edges carry values (forward) or gradients (backward)
- Forward mode `lesson term` — Autodiff that propagates derivatives from inputs to outputs. One pass per input variable.
- Reverse mode `lesson term` — Autodiff that propagates gradients from outputs to inputs. One pass per output variable.
- [[Concepts/Autograd|Autograd]] `glossary` — A system that records operations on values, builds a graph, and computes exact gradients via the chain rule
- Dual numbers `lesson term` — Numbers of the form a + bepsilon (epsilon^2 = 0) that carry derivative information through arithmetic
- [[Concepts/Topological sort|Topological sort]] `lesson term` — Ordering graph nodes so every node comes after all its dependencies. Required for correct gradient propagation.
- [[Concepts/Gradient Accumulation|Gradient Accumulation]] `glossary` — When a value feeds into multiple operations, its gradient is the sum of all incoming gradient contributions
- Dynamic graph `lesson term` — A computation graph rebuilt on every forward pass, allowing Python control flow inside models (PyTorch style)
- [[Concepts/Gradient checking|Gradient checking]] `lesson term` — Comparing autodiff gradients against numerical finite-difference gradients to verify correctness. Essential for debugging.
- MLP `lesson term` — A neural network with one or more hidden layers of neurons. Each neuron computes a weighted sum plus bias, then applies an activation function.
- Neuron `lesson term` — The basic unit: output = activation(w1x1 + w2x2 + ... + b). The weights and bias are learnable parameters.

## Ships

- [[Artifacts/01-05 skill-autodiff|skill-autodiff]] `skill` — Build, debug, and reason about automatic differentiation systems

## Further reading

- Baydin et al., Automatic Differentiation in Machine Learning: a Survey ([link](https://arxiv.org/abs/1502.05767)) — comprehensive reference
- PyTorch Autograd mechanics ([link](https://pytorch.org/docs/stable/notes/autograd.html)) — how the real system works
- 3Blue1Brown: Backpropagation calculus ([link](https://www.youtube.com/watch?v=tIeHLnjs5U8)) — visual explanation of the chain rule in neural networks


%% ── my notes ── %%
