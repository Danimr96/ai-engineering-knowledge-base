---
id: "lesson:03/11"
type: lesson
ref: 03/11
phase: 3
num: 11
title: Introduction to PyTorch
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 0
code_files: 1
concepts: 10
prereqs: 1
community: 85
libraries:
  - torch
aliases:
  - 03/11
  - 03-11
tags:
  - phase/03
  - type/build
  - community/85
source: ai-engineering-from-scratch/phases/03-deep-learning-core/11-intro-to-pytorch/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/11-intro-to-pytorch"
---

# 03/11 Introduction to PyTorch

> You built the engine from pistons and crankshafts. Now learn the one everyone actually drives.

**Phase:** [[Phases/03 Deep Learning Core|Phase 3: Deep Learning Core]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/03-deep-learning-core/11-intro-to-pytorch/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/11-intro-to-pytorch) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/03-deep-learning-core/11-intro-to-pytorch) · code: pytorch_intro.py  
**Community:** [[Communities/85 DataLoader · Zero grad · state_dict|85 DataLoader · Zero grad · state_dict]] · **Libraries:** [[Libraries/torch (python)|torch]]  

## Prerequisites

Stated upstream: `Lesson 03.10 (Build Your Own Mini Framework)`

- [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]] — Build Your Own Mini Framework

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/03-01 The Perceptron|03/01 The Perceptron]], [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-04 Activation Functions|03/04 Activation Functions]], [[Lessons/03-05 Loss Functions|03/05 Loss Functions]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/03-07 Regularization|03/07 Regularization]], [[Lessons/03-08 Weight Initialization and Training Stability|03/08 Weight Initialization and Training Stability]], [[Lessons/03-09 Learning Rate Schedules and Warmup|03/09 Learning Rate Schedules and Warmup]]

## Builds on this

- [[Lessons/04-01 Image Fundamentals — Pixels, Channels, Color Spaces|04/01 Image Fundamentals — Pixels, Channels, Color Spaces]]
- [[Lessons/04-03 CNNs — LeNet to ResNet|04/03 CNNs — LeNet to ResNet]]
- [[Lessons/05-08 CNNs and RNNs for Text|05/08 CNNs and RNNs for Text]]
- [[Lessons/05-09 Sequence-to-Sequence Models|05/09 Sequence-to-Sequence Models]]

## Concepts taught

- [[Concepts/Tensor|Tensor]] `glossary` — A typed, device-aware array with automatic differentiation support baked into every operation
- [[Concepts/Autograd|Autograd]] `glossary` — A tape-based system that records operations during forward pass, then replays them in reverse to compute exact gradients
- nn.Module `lesson term` — The base class for any differentiable computation block -- registers parameters, supports nesting, handles train/eval modes
- [[Concepts/state_dict|state_dict]] `lesson term` — An OrderedDict mapping parameter names to tensors -- the portable, serializable representation of a trained model
- .backward (as *.backward()*) `lesson term` — Traverse the computational graph in reverse, computing and accumulating gradients for every leaf tensor with requires_grad=True
- .to (as *.to(device)*) `lesson term` — Recursively transfer all parameters and buffers to the specified device (CPU, CUDA, MPS)
- [[Concepts/DataLoader|DataLoader]] `lesson term` — An iterator that batches, shuffles, and optionally parallelizes data loading from a Dataset
- [[Concepts/Mixed Precision|Mixed Precision]] `glossary` — Train with float16 forward/backward for speed while keeping float32 master weights for numerical stability
- Eager execution `lesson term` — Operations execute immediately when called, not deferred to a later compilation step -- the core design choice that differentiates PyTorch from TF 1.x
- [[Concepts/Zero grad|Zero grad]] (as *zero_grad*) `lesson term` — Set all parameter gradients to zero before the next backward pass, since PyTorch accumulates gradients by default

## Ships

- [[Artifacts/03-11 prompt-pytorch-debugger|prompt-pytorch-debugger]] `prompt` — Diagnose and fix common PyTorch training failures from symptoms
- [[Artifacts/03-11 skill-pytorch-patterns|skill-pytorch-patterns]] `skill` — Reference patterns for PyTorch training, evaluation, and deployment


%% ── my notes ── %%
