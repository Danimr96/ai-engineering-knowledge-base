---
id: "concept:autograd"
type: concept
name: Autograd
canonical: true
category: "Math & training"
taught_in: 3
community: 8
tags:
  - concept/glossary
  - category/math-and-training
  - community/08
source: ai-engineering-from-scratch/glossary/terms.md
---

# Autograd

**Community:** [[Communities/08 Backpropagation · Gradient · Activation Function|08 Backpropagation · Gradient · Activation Function]]

> *What people say:* Automatic gradients.

**What it actually means:** A system that records or transforms tensor operations so it can compute derivatives, usually with reverse-mode automatic differentiation. You write the forward computation and the framework derives the gradients needed for backpropagation.

**Category:** [[Categories/Math & training|Math & training]]

## Related concepts

- [[Concepts/Activation Checkpointing|Activation Checkpointing]]
- [[Concepts/Backpropagation|Backpropagation]]
- [[Concepts/Gradient|Gradient]]
- [[Concepts/JAX|JAX]]
- [[Concepts/Tensor|Tensor]]

## Taught in

- [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]] — A system that records operations on values, builds a graph, and computes exact gradients via the chain rule
- [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]] — A system that builds computational graphs during forward computation and automatically computes gradients -- what PyTorch's engine does
- [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]] — A tape-based system that records operations during forward pass, then replays them in reverse to compute exact gradients


%% ── my notes ── %%
