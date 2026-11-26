---
id: "lesson:01/12"
type: lesson
ref: 01/12
phase: 1
num: 12
title: Tensor Operations
lesson_type: build
time_min: 90
on_route: false
quiz_count: 5
code_files: 1
concepts: 10
prereqs: 2
community: 34
libraries:
  - numpy
aliases:
  - 01/12
  - 01-12
tags:
  - phase/01
  - type/build
  - community/34
source: ai-engineering-from-scratch/phases/01-math-foundations/12-tensor-operations/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/12-tensor-operations"
---

# 01/12 Tensor Operations

> Tensors are the common language between data and deep learning. Every image, every sentence, every gradient flows through them.

**Phase:** [[Phases/01 Math Foundations|Phase 1: Math Foundations]] · **Type:** Build · **Time:** 90 min · **Status:** —  
**Open:** [[Upstream/01-math-foundations/12-tensor-operations/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/12-tensor-operations) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/01-math-foundations/12-tensor-operations) · code: tensors.py · quiz: 5 questions  
**Community:** [[Communities/34 Tensor · CUDA · Mixed Precision|34 Tensor · CUDA · Mixed Precision]] · **Libraries:** [[Libraries/numpy (python)|numpy]]  

## Prerequisites

Stated upstream: `Phase 1, Lessons 01 (Linear Algebra Intuition), 02 (Vectors, Matrices & Operations)`

- [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]] — Linear Algebra Intuition
- [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]] — Vectors, Matrices & Operations

## Builds on this

- [[Lessons/04-01 Image Fundamentals — Pixels, Channels, Color Spaces|04/01 Image Fundamentals — Pixels, Channels, Color Spaces]]
- [[Lessons/04-13 3D Vision — Point Clouds & NeRFs|04/13 3D Vision — Point Clouds & NeRFs]]
- [[Lessons/04-22 3D Gaussian Splatting from Scratch|04/22 3D Gaussian Splatting from Scratch]]

## Concepts taught

- [[Concepts/Tensor|Tensor]] `glossary` — A multi-dimensional array with uniform type and defined shape, strides, and operations
- [[Concepts/Rank|Rank]] `lesson term` — The number of axes. A matrix has rank 2, not rank equal to its matrix rank
- Shape `lesson term` — A tuple listing the size along each axis. (2, 3) means 2 rows, 3 columns
- [[Concepts/Stride|Stride]] `lesson term` — The number of elements to skip to advance one position along each axis
- [[Concepts/Broadcasting|Broadcasting]] `lesson term` — A strict set of rules: align from right, dimensions must be equal or one must be 1
- Contiguous `lesson term` — Elements stored sequentially in memory with no gaps or reordering from the logical layout
- Einsum `lesson term` — A general notation that expresses any tensor contraction, outer product, trace, or transpose in one line
- View `lesson term` — A tensor sharing the same memory buffer but with different shape/stride metadata. Fails on non-contiguous data
- [[Concepts/Contraction|Contraction]] `lesson term` — The general operation where a shared index between tensors is multiplied and summed, producing a lower-rank result
- NCHW / NHWC `lesson term` — Memory layout conventions for image tensors. NCHW puts channels before spatial dims, NHWC puts them after

## Ships

- [[Artifacts/01-12 prompt-tensor-debugger|prompt-tensor-debugger]] `prompt` — Step-by-step debugging prompt for tensor shape errors in deep learning code
- [[Artifacts/01-12 prompt-tensor-shapes|prompt-tensor-shapes]] `prompt` — Debug tensor shape mismatches and recommend fixes for common deep learning operations

## Further reading

- einops ([link](https://github.com/arogozhnikov/einops)) — A library that makes tensor reshaping readable and safe
- [[Resources/The Illustrated Transformer|The Illustrated Transformer]] ([link](https://jalammar.github.io/illustrated-transformer/)) — Visualizes the tensor shapes flowing through attention ·  also cited by 1 other lesson
- Einstein Summation in NumPy ([link](https://numpy.org/doc/stable/reference/generated/numpy.einsum.html)) — Full einsum documentation with examples
- [[Resources/NumPy documentation on broadcasting|NumPy documentation on broadcasting]] ([link](https://numpy.org/doc/stable/user/basics.broadcasting.html)) — The canonical rules with visual examples ·  also cited by 1 other lesson
- PyTorch Tensor Views ([link](https://pytorch.org/docs/stable/tensor_view.html)) — When views work and when they copy


%% ── my notes ── %%
