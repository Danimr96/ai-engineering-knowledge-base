---
id: "lesson:03/13"
type: lesson
ref: 03/13
phase: 3
num: 13
title: Debugging Neural Networks
lesson_type: build
languages:
  - Python
  - PyTorch
time_min: 90
on_route: false
quiz_count: 0
code_files: 1
concepts: 10
prereqs: 10
community: 22
libraries:
  - torch
aliases:
  - 03/13
  - 03-13
tags:
  - phase/03
  - type/build
  - community/22
source: ai-engineering-from-scratch/phases/03-deep-learning-core/13-debugging-neural-networks/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/13-debugging-neural-networks"
---

# 03/13 Debugging Neural Networks

> Your network compiled. It ran. It produced a number. The number is wrong and nothing crashed. Welcome to the hardest kind of debugging -- the kind where there is no error message.

**Phase:** [[Phases/03 Deep Learning Core|Phase 3: Deep Learning Core]] · **Type:** Build · **Time:** 90 min · **Languages:** Python, PyTorch · **Status:** —  
**Open:** [[Upstream/03-deep-learning-core/13-debugging-neural-networks/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/13-debugging-neural-networks) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/03-deep-learning-core/13-debugging-neural-networks) · code: debug_neural_nets.py  
**Community:** [[Communities/22 Backward pass · Forward pass · Vanishing gradient|22 Backward pass · Forward pass · Vanishing gradient]] · **Libraries:** [[Libraries/torch (python)|torch]]  

## Prerequisites

Stated upstream: `Phase 03 Lessons 01-10 (especially backpropagation, loss functions, optimizers)`

- **03/01-10** — especially backpropagation, loss functions, optimizers:
    - [[Lessons/03-01 The Perceptron|03/01 The Perceptron]]
    - [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]]
    - [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]]
    - [[Lessons/03-04 Activation Functions|03/04 Activation Functions]]
    - [[Lessons/03-05 Loss Functions|03/05 Loss Functions]]
    - [[Lessons/03-06 Optimizers|03/06 Optimizers]]
    - [[Lessons/03-07 Regularization|03/07 Regularization]]
    - [[Lessons/03-08 Weight Initialization and Training Stability|03/08 Weight Initialization and Training Stability]]
    - [[Lessons/03-09 Learning Rate Schedules and Warmup|03/09 Learning Rate Schedules and Warmup]]
    - [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]]

## Concepts taught

- Silent bug `lesson term` — A bug that produces no error but degrades model quality -- the dominant failure mode in ML
- Dead ReLU `lesson term` — A ReLU neuron whose input is always negative, so it outputs 0 and receives 0 gradient permanently
- Vanishing gradients `lesson term` — Gradients shrink exponentially through layers, making weights in early layers effectively frozen
- Exploding gradients `lesson term` — Gradients grow exponentially through layers, causing weight updates so large they overflow
- [[Concepts/Gradient checking|Gradient checking]] `lesson term` — Comparing analytical gradients from backprop to numerical gradients from finite differences
- Overfit-one-batch `lesson term` — Training on a single small batch to verify the model CAN learn -- if it cannot, something is fundamentally broken
- LR finder `lesson term` — Exponentially increasing the learning rate over one epoch and picking the rate just before loss diverges
- [[Concepts/Data Leakage|Data Leakage]] `glossary` — When information from the test set contaminates training, producing artificially high accuracy
- Activation statistics `lesson term` — Tracking mean, std, and zero-fraction of each layer's output to detect dead, saturated, or exploding neurons
- [[Concepts/Gradient Clipping|Gradient Clipping]] `glossary` — Scaling gradients down when their norm exceeds a threshold, preventing exploding gradient updates

## Ships

- [[Artifacts/03-13 prompt-nn-debugger|prompt-nn-debugger]] `prompt` — Diagnose neural network training failures from symptoms -- loss curves, gradient stats, and activation patterns
- [[Artifacts/03-13 skill-debug-checklist|skill-debug-checklist]] `skill` — Decision-tree checklist for debugging neural network training failures


%% ── my notes ── %%
