---
id: "concept:gradient-accumulation"
type: concept
name: Gradient Accumulation
canonical: true
category: "Math & training"
taught_in: 1
community: 11
tags:
  - concept/glossary
  - category/math-and-training
  - community/11
source: ai-engineering-from-scratch/glossary/terms.md
---

# Gradient Accumulation

**Community:** [[Communities/11 Learning Rate · Optimizer · Batch Size|11 Learning Rate · Optimizer · Batch Size]]

**What it actually means:** Summing or averaging gradients from several microbatches before performing one optimizer update.

**Why it matters:** It lets you approximate a larger effective batch when one device cannot hold all examples and activations at once.

**In practice:** Scale the loss consistently, call the optimizer only after the chosen number of microbatches, and measure whether normalization or distributed synchronization changes behavior.

**Common confusion:** Gradient accumulation reduces per-step activation memory, but it does not reproduce every property of processing the full batch simultaneously.

**Category:** [[Categories/Math & training|Math & training]]

## Related concepts

- [[Concepts/Backpropagation|Backpropagation]]
- [[Concepts/Batch Size|Batch Size]]
- [[Concepts/Mixed Precision|Mixed Precision]]
- [[Concepts/Optimizer|Optimizer]]

## Taught in

- [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]] — When a value feeds into multiple operations, its gradient is the sum of all incoming gradient contributions

## Sources

- PyTorch AMP examples: Gradient accumulation ([link](https://docs.pytorch.org/docs/stable/notes/amp_examples.html#gradient-accumulation))


%% ── my notes ── %%
