---
id: "concept:rank"
type: concept
name: Rank
canonical: false
aliases:
  - r
taught_in: 5
community: 8
tags:
  - concept/lesson-term
  - community/08
source: ai-engineering-from-scratch/phases/01-math-foundations/01-linear-algebra-intuition/docs/en.md
---

# Rank

**Community:** [[Communities/08 Backpropagation · Gradient · Activation Function|08 Backpropagation · Gradient · Activation Function]]

> *What people say:* "How many dimensions"

**What it actually means:** The number of linearly independent columns (or rows) in a matrix

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]]
- [[Lessons/01-11 Singular Value Decomposition|01/11 Singular Value Decomposition]] — The number of non-zero singular values. Tells you how many independent directions the matrix actually uses.
- [[Lessons/01-12 Tensor Operations|01/12 Tensor Operations]] — The number of axes. A matrix has rank 2, not rank equal to its matrix rank
- [[Lessons/11-08 Fine-Tuning with LoRA & QLoRA|11/08 Fine-Tuning with LoRA & QLoRA]] — The inner dimension of the A and B matrices; controls expressiveness vs. parameter count
- [[Lessons/19-48 Distributed Data Parallel and FSDP from Scratch|19/48 Distributed Data Parallel and FSDP from Scratch]] — Process identifier within the group, zero indexed


%% ── my notes ── %%
