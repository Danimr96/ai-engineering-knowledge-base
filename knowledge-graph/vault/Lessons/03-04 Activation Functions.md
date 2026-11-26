---
id: "lesson:03/04"
type: lesson
ref: 03/04
phase: 3
num: 4
title: Activation Functions
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 0
code_files: 2
concepts: 13
prereqs: 1
community: 22
aliases:
  - 03/04
  - 03-04
tags:
  - phase/03
  - type/build
  - community/22
  - stdlib-only
source: ai-engineering-from-scratch/phases/03-deep-learning-core/04-activation-functions/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/04-activation-functions"
---

# 03/04 Activation Functions

> Without nonlinearity, your 100-layer network is a fancy matrix multiply. Activations are the gates that let neural networks think in curves.

**Phase:** [[Phases/03 Deep Learning Core|Phase 3: Deep Learning Core]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/03-deep-learning-core/04-activation-functions/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/04-activation-functions) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/03-deep-learning-core/04-activation-functions) · code: main.jl, main.py  
**Community:** [[Communities/22 Backward pass · Forward pass · Vanishing gradient|22 Backward pass · Forward pass · Vanishing gradient]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Lesson 03.03 (Backpropagation)`

- [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]] — Backpropagation

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]]
- depth 3: [[Lessons/03-01 The Perceptron|03/01 The Perceptron]]

## Builds on this

- [[Lessons/03-05 Loss Functions|03/05 Loss Functions]]
- [[Lessons/03-08 Weight Initialization and Training Stability|03/08 Weight Initialization and Training Stability]]
- [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]]
- [[Lessons/03-12 Introduction to JAX|03/12 Introduction to JAX]]
- [[Lessons/03-13 Debugging Neural Networks|03/13 Debugging Neural Networks]]

## Concepts taught

- [[Concepts/Activation Function|Activation Function]] `glossary` — A function applied to each neuron's output that breaks linearity, enabling the network to learn nonlinear mappings
- [[Concepts/Vanishing gradient|Vanishing gradient]] `lesson term` — Gradients shrink exponentially through layers when the activation's derivative is less than 1, making early layers untrainable
- Exploding gradient `lesson term` — Gradients grow exponentially through layers when the effective multiplier exceeds 1, causing unstable training
- Dead neuron `lesson term` — A ReLU neuron whose input is permanently negative, producing zero output and zero gradient
- [[Concepts/Sigmoid|Sigmoid]] `lesson term` — The logistic function 1/(1+e^-x), historically important but causes vanishing gradients in deep networks
- [[Concepts/ReLU|ReLU]] `glossary` — max(0, x) -- the activation that made deep learning practical by preserving gradient magnitude
- GELU `lesson term` — Gaussian Error Linear Unit, a smooth activation that weights inputs by their probability of being positive
- Swish/SiLU `lesson term` — x sigmoid(x), discovered through automated search, used in EfficientNet
- [[Concepts/Softmax|Softmax]] `glossary` — Normalizes a vector of logits into a probability distribution where all values are in (0,1) and sum to 1
- Leaky ReLU `lesson term` — max(alphax, x) where alpha is small (0.01), preventing dead neurons by allowing small negative gradients
- [[Concepts/Saturation|Saturation]] `glossary` — Regions where an activation's derivative approaches zero, blocking gradient flow
- [[Concepts/Logits|Logits]] (as *Logit*) `glossary` — The unnormalized output of the final layer before applying softmax or sigmoid

## Ships

- [[Artifacts/03-04 prompt-activation-selector|prompt-activation-selector]] `prompt` — A decision prompt for choosing the right activation function for any neural network architecture


%% ── my notes ── %%
