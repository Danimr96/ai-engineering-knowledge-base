---
id: "lesson:03/02"
type: lesson
ref: 03/02
phase: 3
num: 2
title: Multi-Layer Networks and Forward Pass
lesson_type: build
languages:
  - Python
time_min: 90
on_route: false
quiz_count: 0
code_files: 1
concepts: 10
prereqs: 1
community: 27
aliases:
  - 03/02
  - 03-02
tags:
  - phase/03
  - type/build
  - community/27
  - stdlib-only
source: ai-engineering-from-scratch/phases/03-deep-learning-core/02-multi-layer-networks/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/02-multi-layer-networks"
---

# 03/02 Multi-Layer Networks and Forward Pass

> One neuron draws a line. Stack them, and you can draw anything.

**Phase:** [[Phases/03 Deep Learning Core|Phase 3: Deep Learning Core]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/03-deep-learning-core/02-multi-layer-networks/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/02-multi-layer-networks) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/03-deep-learning-core/02-multi-layer-networks) · code: main.py  
**Community:** [[Communities/27 Decision boundary · Bias · ELBO|27 Decision boundary · Bias · ELBO]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 01 (Math Foundations), Lesson 03.01 (The Perceptron)`

- [[Lessons/03-01 The Perceptron|03/01 The Perceptron]] — The Perceptron
- Whole phase: [[Phases/01 Math Foundations|Phase 1: Math Foundations]] — Math Foundations ·  medium confidence

## Builds on this

- [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]]
- [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]]
- [[Lessons/03-12 Introduction to JAX|03/12 Introduction to JAX]]
- [[Lessons/03-13 Debugging Neural Networks|03/13 Debugging Neural Networks]]
- [[Lessons/08-02 Autoencoders & Variational Autoencoders (VAE)|08/02 Autoencoders & Variational Autoencoders (VAE)]]
- [[Lessons/08-03 GANs — Generator vs Discriminator|08/03 GANs — Generator vs Discriminator]]
- [[Lessons/08-06 Diffusion Models — DDPM from Scratch|08/06 Diffusion Models — DDPM from Scratch]]

## Concepts taught

- [[Concepts/Forward pass|Forward pass]] `lesson term` — Pushing input through every layer -- multiply by weights, add bias, activate -- to produce an output
- Hidden layer `lesson term` — Any layer between input and output whose values are not directly observed in the data
- Multi-layer network `lesson term` — Layers of neurons stacked sequentially, where each layer's output feeds the next layer's input
- [[Concepts/Activation Function|Activation Function]] `glossary` — A function applied after the linear transformation that introduces curves into the decision boundary
- [[Concepts/Sigmoid|Sigmoid]] `lesson term` — sigma(z) = 1/(1+e^(-z)), squashes any real number to (0,1), smooth and differentiable everywhere
- Weight matrix `lesson term` — A matrix W of shape (current_layer_neurons, previous_layer_neurons) containing learnable connection strengths
- Bias vector `lesson term` — A vector added after the matrix multiply that lets neurons activate even when all inputs are zero
- Universal approximation `lesson term` — A single hidden layer with enough neurons can approximate any continuous function -- but "enough" can mean billions
- Linear transformation `lesson term` — z = W x + b, the computation before activation, which maps inputs to a new space
- [[Concepts/Decision boundary|Decision boundary]] `lesson term` — The surface in input space where the network output crosses the classification threshold

## Ships

- [[Artifacts/03-02 prompt-network-architect|prompt-network-architect]] `prompt` — Guides the user through designing neural network architectures by choosing layer counts, neuron counts, and activation functions for a given problem


%% ── my notes ── %%
