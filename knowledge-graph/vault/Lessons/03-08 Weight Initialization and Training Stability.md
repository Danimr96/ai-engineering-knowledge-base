---
id: "lesson:03/08"
type: lesson
ref: 03/08
phase: 3
num: 8
title: Weight Initialization and Training Stability
lesson_type: build
languages:
  - Python
time_min: 90
on_route: false
quiz_count: 0
code_files: 1
concepts: 10
prereqs: 2
community: 22
aliases:
  - 03/08
  - 03-08
tags:
  - phase/03
  - type/build
  - community/22
  - stdlib-only
source: ai-engineering-from-scratch/phases/03-deep-learning-core/08-weight-initialization/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/08-weight-initialization"
---

# 03/08 Weight Initialization and Training Stability

> Initialize wrong and training never starts. Initialize right and 50 layers train as smoothly as 3.

**Phase:** [[Phases/03 Deep Learning Core|Phase 3: Deep Learning Core]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/03-deep-learning-core/08-weight-initialization/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/08-weight-initialization) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/03-deep-learning-core/08-weight-initialization) · code: main.py  
**Community:** [[Communities/22 Backward pass · Forward pass · Vanishing gradient|22 Backward pass · Forward pass · Vanishing gradient]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Lesson 03.04 (Activation Functions), Lesson 03.07 (Regularization)`

- [[Lessons/03-04 Activation Functions|03/04 Activation Functions]] — Activation Functions
- [[Lessons/03-07 Regularization|03/07 Regularization]] — Regularization

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-06 Optimizers|03/06 Optimizers]]
- depth 3: [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]], [[Lessons/03-05 Loss Functions|03/05 Loss Functions]]

## Builds on this

- [[Lessons/03-09 Learning Rate Schedules and Warmup|03/09 Learning Rate Schedules and Warmup]]
- [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]]
- [[Lessons/03-12 Introduction to JAX|03/12 Introduction to JAX]]
- [[Lessons/03-13 Debugging Neural Networks|03/13 Debugging Neural Networks]]
- [[Lessons/08-03 GANs — Generator vs Discriminator|08/03 GANs — Generator vs Discriminator]]

## Concepts taught

- Weight initialization `lesson term` — The strategy for choosing initial weight values that determines whether a network can train at all
- Symmetry breaking `lesson term` — Using random initialization to ensure neurons learn distinct features instead of computing identical functions
- Fan-in `lesson term` — The number of incoming connections, which determines how input variance accumulates in the weighted sum
- Fan-out `lesson term` — The number of outgoing connections, relevant for maintaining gradient variance during backpropagation
- Xavier/Glorot init `lesson term` — Var(w) = 2/(fan_in + fan_out), designed to preserve variance through sigmoid and tanh activations
- Kaiming/He init `lesson term` — Var(w) = 2/fan_in, accounts for ReLU zeroing half the activations
- Variance propagation `lesson term` — The mathematical analysis of how activation variance changes layer by layer based on weight scale
- Residual scaling `lesson term` — Scaling residual connection weights by 1/sqrt(2N) to prevent variance growth through N transformer layers
- Dead network `lesson term` — A network where poor initialization causes all gradients to be zero or all activations to saturate
- Exploding activations `lesson term` — When weight variance is too high, causing activation magnitudes to grow exponentially through layers

## Ships

- [[Artifacts/03-08 prompt-init-strategy|prompt-init-strategy]] `prompt` — Diagnose weight initialization problems and recommend the right strategy for any neural network architecture


%% ── my notes ── %%
