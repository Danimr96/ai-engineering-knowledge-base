---
id: "lesson:03/07"
type: lesson
ref: 03/07
phase: 3
num: 7
title: Regularization
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 0
code_files: 1
concepts: 10
prereqs: 1
community: 72
aliases:
  - 03/07
  - 03-07
tags:
  - phase/03
  - type/build
  - community/72
  - stdlib-only
source: ai-engineering-from-scratch/phases/03-deep-learning-core/07-regularization/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/07-regularization"
---

# 03/07 Regularization

> Your model gets 99% on training data and 60% on test data. It memorized instead of learning. Regularization is the tax you impose on complexity to force generalization.

**Phase:** [[Phases/03 Deep Learning Core|Phase 3: Deep Learning Core]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/03-deep-learning-core/07-regularization/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/07-regularization) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/03-deep-learning-core/07-regularization) · code: main.py  
**Community:** [[Communities/72 Early stopping · Layer normalization · RMSNorm|72 Early stopping · Layer normalization · RMSNorm]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Lesson 03.06 (Optimizers)`

- [[Lessons/03-06 Optimizers|03/06 Optimizers]] — Optimizers

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/03-05 Loss Functions|03/05 Loss Functions]]
- depth 3: [[Lessons/03-04 Activation Functions|03/04 Activation Functions]]

## Builds on this

- [[Lessons/03-08 Weight Initialization and Training Stability|03/08 Weight Initialization and Training Stability]]
- [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]]
- [[Lessons/03-12 Introduction to JAX|03/12 Introduction to JAX]]
- [[Lessons/03-13 Debugging Neural Networks|03/13 Debugging Neural Networks]]
- [[Lessons/04-09 Image Generation — GANs|04/09 Image Generation — GANs]]
- [[Lessons/08-02 Autoencoders & Variational Autoencoders (VAE)|08/02 Autoencoders & Variational Autoencoders (VAE)]]
- [[Lessons/08-04 Conditional GANs & Pix2Pix|08/04 Conditional GANs & Pix2Pix]]
- [[Lessons/08-05 StyleGAN|08/05 StyleGAN]]

## Concepts taught

- [[Concepts/Overfitting|Overfitting]] `glossary` — When a model's training performance significantly exceeds its test performance, indicating it learned noise rather than signal
- [[Concepts/Regularization|Regularization]] `lesson term` — Any technique that constrains model complexity to improve generalization: dropout, weight decay, normalization, augmentation
- [[Concepts/Dropout|Dropout]] `glossary` — Zeroing random neurons during training with probability p, forcing redundant representations; equivalent to training an ensemble
- [[Concepts/Weight Decay|Weight Decay]] `glossary` — Shrinking all weights toward zero by subtracting lambda w at each step; penalizes complexity through weight magnitude
- Batch normalization `lesson term` — Normalizing layer outputs across the batch dimension using batch statistics during training and running averages during inference
- [[Concepts/Layer normalization|Layer normalization]] `lesson term` — Normalizing across features within each sample; batch-independent, used in transformers where batch size varies
- [[Concepts/RMSNorm|RMSNorm]] `lesson term` — Root mean square normalization; drops the mean subtraction from LayerNorm for 10% speedup with equal accuracy
- [[Concepts/Early stopping|Early stopping]] `lesson term` — Halting training when validation loss stops improving; the simplest regularizer, often used alongside others
- [[Concepts/Data Augmentation|Data Augmentation]] `glossary` — Transforming training inputs (flip, crop, noise) to increase effective dataset size and force invariance learning
- Generalization gap `lesson term` — The difference between training and test performance; regularization aims to minimize this gap

## Ships

- [[Artifacts/03-07 prompt-regularization-advisor|prompt-regularization-advisor]] `prompt` — A diagnostic prompt for choosing regularization strategies based on overfitting symptoms


%% ── my notes ── %%
