---
id: "lesson:03/03"
type: lesson
ref: 03/03
phase: 3
num: 3
title: Backpropagation from Scratch
lesson_type: build
languages:
  - Python
time_min: 120
on_route: false
quiz_count: 0
code_files: 2
concepts: 11
prereqs: 1
community: 22
aliases:
  - 03/03
  - 03-03
tags:
  - phase/03
  - type/build
  - community/22
  - stdlib-only
source: ai-engineering-from-scratch/phases/03-deep-learning-core/03-backpropagation/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/03-backpropagation"
---

# 03/03 Backpropagation from Scratch

> Backpropagation is the algorithm that makes learning possible. Without it, neural networks are just expensive random number generators.

**Phase:** [[Phases/03 Deep Learning Core|Phase 3: Deep Learning Core]] · **Type:** Build · **Time:** 120 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/03-deep-learning-core/03-backpropagation/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/03-backpropagation) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/03-deep-learning-core/03-backpropagation) · code: main.jl, main.py  
**Community:** [[Communities/22 Backward pass · Forward pass · Vanishing gradient|22 Backward pass · Forward pass · Vanishing gradient]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Lesson 03.02 (Multi-Layer Networks)`

- [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]] — Multi-Layer Networks

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/03-01 The Perceptron|03/01 The Perceptron]]

## Builds on this

- [[Lessons/03-04 Activation Functions|03/04 Activation Functions]]
- [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]]
- [[Lessons/03-12 Introduction to JAX|03/12 Introduction to JAX]]
- [[Lessons/03-13 Debugging Neural Networks|03/13 Debugging Neural Networks]]
- [[Lessons/05-03 Word Embeddings — Word2Vec from Scratch|05/03 Word Embeddings — Word2Vec from Scratch]]
- [[Lessons/09-05 Deep Q-Networks (DQN)|09/05 Deep Q-Networks (DQN)]]
- [[Lessons/09-06 Policy Gradient — REINFORCE from Scratch|09/06 Policy Gradient — REINFORCE from Scratch]]

## Concepts taught

- [[Concepts/Backpropagation|Backpropagation]] `glossary` — An algorithm that computes dL/dw for every weight by applying the chain rule backward through the computational graph
- [[Concepts/Computational graph|Computational graph]] `lesson term` — A directed acyclic graph where nodes are operations and edges carry values (forward) and gradients (backward)
- [[Concepts/Chain rule|Chain rule]] `lesson term` — If y = f(g(x)), then dy/dx = f'(g(x)) g'(x) -- the mathematical foundation of backpropagation
- [[Concepts/Gradient|Gradient]] `glossary` — The partial derivative of the loss with respect to a parameter -- tells you how to change that parameter to reduce the loss
- [[Concepts/Vanishing gradient|Vanishing gradient]] `lesson term` — Gradients shrink exponentially as they propagate through layers with saturating activations like sigmoid
- [[Concepts/Forward pass|Forward pass]] `lesson term` — Computing the output from inputs by sequentially applying each layer's operations and storing intermediate values
- [[Concepts/Backward pass|Backward pass]] `lesson term` — Traversing the computational graph in reverse, accumulating gradients at each node using the chain rule
- [[Concepts/Learning Rate|Learning Rate]] `glossary` — A scalar that controls the step size when updating weights: w_new = w_old - lr gradient
- [[Concepts/Topological sort|Topological sort]] `lesson term` — An ordering of graph nodes where each node appears after all nodes it depends on -- ensures gradients are fully accumulated before propagation
- [[Concepts/Autograd|Autograd]] `glossary` — A system that builds computational graphs during forward computation and automatically computes gradients -- what PyTorch's engine does

## Ships

- [[Artifacts/03-03 prompt-gradient-debugger|prompt-gradient-debugger]] `prompt` — Diagnose and fix gradient problems in neural networks -- vanishing gradients, exploding gradients, and NaN values


%% ── my notes ── %%
