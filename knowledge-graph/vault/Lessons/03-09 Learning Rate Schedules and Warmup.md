---
id: "lesson:03/09"
type: lesson
ref: 03/09
phase: 3
num: 9
title: Learning Rate Schedules and Warmup
lesson_type: build
languages:
  - Python
time_min: 90
on_route: false
quiz_count: 0
code_files: 1
concepts: 10
prereqs: 2
community: 11
aliases:
  - 03/09
  - 03-09
tags:
  - phase/03
  - type/build
  - community/11
  - stdlib-only
source: ai-engineering-from-scratch/phases/03-deep-learning-core/09-learning-rate-schedules/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/09-learning-rate-schedules"
---

# 03/09 Learning Rate Schedules and Warmup

> The learning rate is the single most important hyperparameter. Not the architecture. Not the dataset size. Not the activation function. The learning rate. If you tune nothing else, tune this.

**Phase:** [[Phases/03 Deep Learning Core|Phase 3: Deep Learning Core]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/03-deep-learning-core/09-learning-rate-schedules/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/09-learning-rate-schedules) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/03-deep-learning-core/09-learning-rate-schedules) · code: main.py  
**Community:** [[Communities/11 Learning Rate · Optimizer · Batch Size|11 Learning Rate · Optimizer · Batch Size]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Lesson 03.06 (Optimizers), Lesson 03.08 (Weight Initialization)`

- [[Lessons/03-06 Optimizers|03/06 Optimizers]] — Optimizers
- [[Lessons/03-08 Weight Initialization and Training Stability|03/08 Weight Initialization and Training Stability]] — Weight Initialization

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/03-04 Activation Functions|03/04 Activation Functions]], [[Lessons/03-05 Loss Functions|03/05 Loss Functions]], [[Lessons/03-07 Regularization|03/07 Regularization]]
- depth 3: [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]]

## Builds on this

- [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]]
- [[Lessons/03-12 Introduction to JAX|03/12 Introduction to JAX]]
- [[Lessons/03-13 Debugging Neural Networks|03/13 Debugging Neural Networks]]

## Concepts taught

- [[Concepts/Learning Rate|Learning Rate]] `glossary` — The scalar that multiplies the gradient to determine the parameter update size
- [[Concepts/Schedule|Schedule]] `lesson term` — A function that maps training step to learning rate, designed to optimize convergence
- [[Concepts/Warmup|Warmup]] `glossary` — Linearly ramping the LR from near-zero to the target value over the first N steps to stabilize optimizer statistics
- Cosine annealing `lesson term` — Decreasing the LR following a cosine curve from lr_max to lr_min over training
- Step decay `lesson term` — Multiplying the LR by a factor (usually 0.1) at fixed epoch intervals
- 1cycle policy `lesson term` — Leslie Smith's method of ramping LR up then down in a single cycle for faster convergence
- LR range test `lesson term` — Training briefly while increasing LR to find the value where loss starts diverging
- Cosine with warm restarts `lesson term` — Periodically resetting the LR to lr_max and decaying again (SGDR)
- Eta min `lesson term` — The minimum learning rate that the schedule decays to
- Peak learning rate `lesson term` — The highest LR reached during training, typically after warmup

## Ships

- [[Artifacts/03-09 prompt-lr-schedule-advisor|prompt-lr-schedule-advisor]] `prompt` — Recommend the right learning rate schedule and hyperparameters for any training setup


%% ── my notes ── %%
