---
id: "concept:jax"
type: concept
name: JAX
canonical: true
category: "Math & training"
taught_in: 1
community: 34
tags:
  - concept/glossary
  - category/math-and-training
  - community/34
source: ai-engineering-from-scratch/glossary/terms.md
---

# JAX

**Community:** [[Communities/34 Tensor · CUDA · Mixed Precision|34 Tensor · CUDA · Mixed Precision]]

> *What people say:* A NumPy-like system for accelerated machine learning.

**What it actually means:** A Python library for transforming numerical functions with automatic differentiation, compilation, vectorization, and parallel execution across accelerators. Its transformations work best with explicit state and functional-style code.

**Common confusion:** JAX does not prohibit all stateful programming, but hidden mutation inside transformed functions can produce incorrect or unsupported behavior.

**Category:** [[Categories/Math & training|Math & training]]

## Related concepts

- [[Concepts/Autograd|Autograd]]
- [[Concepts/CUDA|CUDA]]
- [[Concepts/Tensor|Tensor]]

## Taught in

- [[Lessons/03-12 Introduction to JAX|03/12 Introduction to JAX]]

## Sources

- JAX documentation ([link](https://docs.jax.dev/en/latest/))


%% ── my notes ── %%
