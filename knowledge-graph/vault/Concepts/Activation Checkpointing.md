---
id: "concept:activation-checkpointing"
type: concept
name: Activation Checkpointing
canonical: true
category: "Math & training"
taught_in: 0
community: 8
tags:
  - concept/glossary
  - category/math-and-training
  - community/08
source: ai-engineering-from-scratch/glossary/terms.md
---

# Activation Checkpointing

**Community:** [[Communities/08 Backpropagation · Gradient · Activation Function|08 Backpropagation · Gradient · Activation Function]]

**What it actually means:** A training-memory technique that saves only selected forward-pass activations and recomputes the omitted ones during backpropagation.

**Why it matters:** It lets you train larger models or sequences within a fixed memory budget by trading additional computation for lower activation storage.

**In practice:** Checkpoint the memory-heavy transformer blocks, measure the extra step time, and keep recovery checkpoints separate from activation-recomputation settings.

**Common confusion:** Activation checkpointing is not a durable training checkpoint. It helps one forward and backward pass fit in memory but cannot resume a crashed run.

**Category:** [[Categories/Math & training|Math & training]]

## Related concepts

- [[Concepts/Autograd|Autograd]]
- [[Concepts/Backpropagation|Backpropagation]]
- [[Concepts/Checkpoint|Checkpoint]]
- [[Concepts/Mixed Precision|Mixed Precision]]

## Sources

- Training Deep Nets with Sublinear Memory Cost ([link](https://arxiv.org/abs/1604.06174))


%% ── my notes ── %%
