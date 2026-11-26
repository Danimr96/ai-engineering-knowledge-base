---
id: "lesson:03/01"
type: lesson
ref: 03/01
phase: 3
num: 1
title: The Perceptron
lesson_type: build
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 0
code_files: 2
concepts: 8
prereqs: 0
community: 27
aliases:
  - 03/01
  - 03-01
tags:
  - phase/03
  - type/build
  - community/27
  - stdlib-only
source: ai-engineering-from-scratch/phases/03-deep-learning-core/01-the-perceptron/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/01-the-perceptron"
---

# 03/01 The Perceptron

> The perceptron is the atom of neural networks. Split it open and you find weights, a bias, and a decision.

**Phase:** [[Phases/03 Deep Learning Core|Phase 3: Deep Learning Core]] · **Type:** Build · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/03-deep-learning-core/01-the-perceptron/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/01-the-perceptron) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/03-deep-learning-core/01-the-perceptron) · code: main.jl, perceptron.py  
**Community:** [[Communities/27 Decision boundary · Bias · ELBO|27 Decision boundary · Bias · ELBO]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 1 (Linear Algebra Intuition)`

- Whole phase: [[Phases/01 Math Foundations|Phase 1: Math Foundations]] — Linear Algebra Intuition ·  medium confidence

## Builds on this

- [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]]
- [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]]
- [[Lessons/03-12 Introduction to JAX|03/12 Introduction to JAX]]
- [[Lessons/03-13 Debugging Neural Networks|03/13 Debugging Neural Networks]]

## Concepts taught

- Perceptron `lesson term` — A linear classifier: dot product of inputs and weights, plus bias, through a step function
- [[Concepts/Weight|Weight]] `glossary` — A multiplier that scales each input's contribution to the decision
- [[Concepts/Bias|Bias]] `lesson term` — A constant that shifts the decision boundary, letting the perceptron fire even with zero inputs
- [[Concepts/Activation Function|Activation Function]] `glossary` — A function applied after the weighted sum - step function for perceptrons, sigmoid/ReLU for modern networks
- Linearly separable `lesson term` — A dataset where a single hyperplane can perfectly separate the classes
- XOR problem `lesson term` — Proof that single-layer networks cannot learn non-linearly-separable functions
- [[Concepts/Decision boundary|Decision boundary]] `lesson term` — The hyperplane wx + b = 0 that divides input space into two classes
- Multi-layer perceptron `lesson term` — Perceptrons stacked in layers, where each layer's output feeds the next layer's input

## Ships

- [[Artifacts/03-01 skill-perceptron|skill-perceptron]] `skill` — Understand the perceptron pattern and when to use single-layer vs multi-layer architectures


%% ── my notes ── %%
