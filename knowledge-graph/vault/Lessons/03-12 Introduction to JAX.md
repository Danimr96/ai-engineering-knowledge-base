---
id: "lesson:03/12"
type: lesson
ref: 03/12
phase: 3
num: 12
title: Introduction to JAX
lesson_type: build
languages:
  - Python
time_min: 90
on_route: false
quiz_count: 0
code_files: 1
concepts: 11
prereqs: 10
community: 22
libraries:
  - jax
  - optax
  - scikit-learn
aliases:
  - 03/12
  - 03-12
tags:
  - phase/03
  - type/build
  - community/22
source: ai-engineering-from-scratch/phases/03-deep-learning-core/12-intro-to-jax/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/12-intro-to-jax"
---

# 03/12 Introduction to JAX

> PyTorch mutates tensors. TensorFlow builds graphs. JAX compiles pure functions. That last one changes how you think about deep learning.

**Phase:** [[Phases/03 Deep Learning Core|Phase 3: Deep Learning Core]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/03-deep-learning-core/12-intro-to-jax/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/12-intro-to-jax) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/03-deep-learning-core/12-intro-to-jax) · code: jax_intro.py  
**Community:** [[Communities/22 Backward pass · Forward pass · Vanishing gradient|22 Backward pass · Forward pass · Vanishing gradient]] · **Libraries:** [[Libraries/jax (python)|jax]], [[Libraries/optax (python)|optax]], [[Libraries/scikit-learn (python)|scikit-learn]]  

## Prerequisites

Stated upstream: `Phase 03 Lessons 01-10, basic NumPy`

- **03/01-10**:
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
- Not understood by the parser: `basic NumPy`

## Concepts taught

- XLA `lesson term` — Accelerated Linear Algebra -- a compiler that fuses operations and generates optimized GPU/TPU kernels from a computation graph
- JIT `lesson term` — JAX traces the function on first call, compiles to XLA, then runs the compiled version on subsequent calls
- Pure function `lesson term` — A function where the output depends only on inputs -- no global state, no mutation, no randomness without explicit keys
- vmap `lesson term` — Transforms a function that processes one example into one that processes a batch, without rewriting
- pmap `lesson term` — Replicates a function across multiple devices and splits the input batch
- Pytree `lesson term` — Any nested structure of lists, tuples, dicts, and arrays that JAX can traverse and transform
- [[Concepts/Tracing|Tracing]] `lesson term` — JAX executes the function with abstract values to build a computation graph, without computing real results
- Functional autodiff `lesson term` — Computing derivatives by transforming functions, not by attaching gradient storage to tensors
- Optax `lesson term` — A composable library of gradient transformations -- Adam, SGD, clipping, scheduling -- that chain together
- Flax `lesson term` — Google's neural network library for JAX, adding layer abstractions while keeping state explicit
- [[Concepts/JAX|JAX]] `glossary` — A Python library for transforming numerical functions with automatic differentiation, compilation, vectorization, and parallel execution across accelerators. Its transformations work best with explicit state and functional-style code.

## Ships

- [[Artifacts/03-12 prompt-jax-optimizer|prompt-jax-optimizer]] `prompt` — Choose and configure the right JAX/Optax optimizer for a given training scenario
- [[Artifacts/03-12 skill-jax-patterns|skill-jax-patterns]] `skill` — Functional programming patterns in JAX -- when and how to use grad, jit, vmap, and pmap


%% ── my notes ── %%
