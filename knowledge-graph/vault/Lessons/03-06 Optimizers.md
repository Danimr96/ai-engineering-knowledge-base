---
id: "lesson:03/06"
type: lesson
ref: 03/06
phase: 3
num: 6
title: Optimizers
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 0
code_files: 1
concepts: 10
prereqs: 1
community: 11
aliases:
  - 03/06
  - 03-06
tags:
  - phase/03
  - type/build
  - community/11
  - stdlib-only
source: ai-engineering-from-scratch/phases/03-deep-learning-core/06-optimizers/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/06-optimizers"
---

# 03/06 Optimizers

> Gradient descent tells you which direction to move. It says nothing about how far or how fast. SGD is a compass. Adam is GPS with traffic data.

**Phase:** [[Phases/03 Deep Learning Core|Phase 3: Deep Learning Core]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/03-deep-learning-core/06-optimizers/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/06-optimizers) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/03-deep-learning-core/06-optimizers) · code: main.py  
**Community:** [[Communities/11 Learning Rate · Optimizer · Batch Size|11 Learning Rate · Optimizer · Batch Size]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Lesson 03.05 (Loss Functions)`

- [[Lessons/03-05 Loss Functions|03/05 Loss Functions]] — Loss Functions

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/03-04 Activation Functions|03/04 Activation Functions]]
- depth 3: [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]]

## Builds on this

- [[Lessons/03-07 Regularization|03/07 Regularization]]
- [[Lessons/03-09 Learning Rate Schedules and Warmup|03/09 Learning Rate Schedules and Warmup]]
- [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]]
- [[Lessons/03-12 Introduction to JAX|03/12 Introduction to JAX]]
- [[Lessons/03-13 Debugging Neural Networks|03/13 Debugging Neural Networks]]
- [[Lessons/04-09 Image Generation — GANs|04/09 Image Generation — GANs]]
- [[Lessons/04-10 Image Generation — Diffusion Models|04/10 Image Generation — Diffusion Models]]
- [[Lessons/06-03 Audio Classification — From k-NN on MFCCs to AST and BEATs|06/03 Audio Classification — From k-NN on MFCCs to AST and BEATs]]

## Concepts taught

- [[Concepts/Learning Rate|Learning Rate]] `glossary` — The scalar multiplier on the gradient update; the single most impactful hyperparameter in training
- [[Concepts/Stochastic Gradient Descent (SGD)|Stochastic Gradient Descent (SGD)]] (as *SGD*) `glossary` — Stochastic gradient descent: update weights by subtracting lr gradient, computed on a mini-batch
- [[Concepts/Momentum|Momentum]] `lesson term` — Exponential moving average of past gradients; dampens oscillation and accelerates consistent directions
- RMSProp `lesson term` — Divides each parameter's gradient by the running RMS of its recent gradients; equalizes learning rates
- [[Concepts/Adam (Optimizer)|Adam (Optimizer)]] (as *Adam*) `glossary` — Combines momentum (first moment) and RMSProp (second moment) with bias correction for the initial steps
- [[Concepts/AdamW|AdamW]] `glossary` — Adam with decoupled weight decay; applies regularization directly to weights rather than through the gradient
- [[Concepts/Bias correction|Bias correction]] `lesson term` — Dividing by (1 - beta^t) to compensate for the zero-initialization of Adam's moment estimates
- [[Concepts/Weight Decay|Weight Decay]] `glossary` — Subtracting a fraction of the weight value at each step; a regularizer that penalizes large weights
- [[Concepts/Learning Rate Schedule|Learning Rate Schedule]] `glossary` — A function that adjusts the learning rate during training; warmup + cosine decay is the modern default
- [[Concepts/Gradient Clipping|Gradient Clipping]] `glossary` — Scaling down the gradient vector when its norm exceeds a threshold; prevents exploding gradient updates

## Ships

- [[Artifacts/03-06 prompt-optimizer-selector|prompt-optimizer-selector]] `prompt` — A decision prompt for choosing the right optimizer and learning rate for any architecture


%% ── my notes ── %%
