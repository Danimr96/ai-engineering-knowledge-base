---
id: "lesson:03/10"
type: lesson
ref: 03/10
phase: 3
num: 10
title: Build Your Own Mini Framework
lesson_type: build
languages:
  - Python
time_min: 120
on_route: false
quiz_count: 0
code_files: 1
concepts: 10
prereqs: 9
community: 22
aliases:
  - 03/10
  - 03-10
tags:
  - phase/03
  - type/build
  - community/22
  - stdlib-only
source: ai-engineering-from-scratch/phases/03-deep-learning-core/10-mini-framework/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/10-mini-framework"
---

# 03/10 Build Your Own Mini Framework

> You have built neurons, layers, networks, backprop, activations, loss functions, optimizers, regularization, initialization, and LR schedules. All as separate pieces. Now wire them together into a framework. Not PyTorch. Not TensorFlow. Yours.

**Phase:** [[Phases/03 Deep Learning Core|Phase 3: Deep Learning Core]] · **Type:** Build · **Time:** 120 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/03-deep-learning-core/10-mini-framework/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/10-mini-framework) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/03-deep-learning-core/10-mini-framework) · code: main.py  
**Community:** [[Communities/22 Backward pass · Forward pass · Vanishing gradient|22 Backward pass · Forward pass · Vanishing gradient]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `All of Phase 03 (Lessons 01-09)`

- **03/01-09**:
    - [[Lessons/03-01 The Perceptron|03/01 The Perceptron]]
    - [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]]
    - [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]]
    - [[Lessons/03-04 Activation Functions|03/04 Activation Functions]]
    - [[Lessons/03-05 Loss Functions|03/05 Loss Functions]]
    - [[Lessons/03-06 Optimizers|03/06 Optimizers]]
    - [[Lessons/03-07 Regularization|03/07 Regularization]]
    - [[Lessons/03-08 Weight Initialization and Training Stability|03/08 Weight Initialization and Training Stability]]
    - [[Lessons/03-09 Learning Rate Schedules and Warmup|03/09 Learning Rate Schedules and Warmup]]

## Builds on this

- [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]]
- [[Lessons/03-12 Introduction to JAX|03/12 Introduction to JAX]]
- [[Lessons/03-13 Debugging Neural Networks|03/13 Debugging Neural Networks]]
- [[Lessons/04-04 Image Classification|04/04 Image Classification]]

## Concepts taught

- Module `lesson term` — The base abstraction in a framework -- anything with forward(), backward(), and parameters()
- Sequential `lesson term` — A container that chains modules, applying them in sequence for forward and reverse for backward
- [[Concepts/Forward pass|Forward pass]] `lesson term` — Computing the output by passing input through each module in order
- [[Concepts/Backward pass|Backward pass]] `lesson term` — Propagating the loss gradient through each module in reverse to compute parameter gradients
- [[Concepts/Parameter|Parameter]] (as *Parameters*) `glossary` — All values in the network that the optimizer can update -- weights and biases
- [[Concepts/Optimizer|Optimizer]] `glossary` — An algorithm that uses gradients to update parameters, implementing SGD, Adam, or other rules
- [[Concepts/DataLoader|DataLoader]] `lesson term` — An iterator that splits a dataset into batches, optionally shuffling between epochs
- Training mode `lesson term` — A flag that enables stochastic behavior like dropout and batch normalization with batch stats
- Evaluation mode `lesson term` — A flag that disables dropout and uses running statistics for batch normalization
- [[Concepts/Zero grad|Zero grad]] `lesson term` — Resetting all parameter gradients to zero before computing the next batch's gradients

## Ships

- [[Artifacts/03-10 prompt-framework-architect|prompt-framework-architect]] `prompt` — Design neural network architectures using framework abstractions -- modules, containers, losses, and optimizers


%% ── my notes ── %%
