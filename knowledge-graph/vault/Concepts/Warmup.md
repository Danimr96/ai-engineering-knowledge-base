---
id: "concept:warmup"
type: concept
name: Warmup
canonical: true
category: "Math & training"
taught_in: 3
community: 11
tags:
  - concept/glossary
  - category/math-and-training
  - community/11
source: ai-engineering-from-scratch/glossary/terms.md
---

# Warmup

**Community:** [[Communities/11 Learning Rate · Optimizer · Batch Size|11 Learning Rate · Optimizer · Batch Size]]

**What it actually means:** An initial training phase in which the learning rate rises from a smaller value toward the main schedule's target value.

**Why it matters:** Early gradients and optimizer statistics can be unstable, especially in large-batch or transformer training, so abrupt full-size updates may damage optimization.

**In practice:** Define warmup in steps or processed tokens, log the realized curve, and tune it with the batch, optimizer, and total training budget held visible.

**Common confusion:** Warmup is not required for every model and does not make an otherwise unsuitable learning rate safe.

**Category:** [[Categories/Math & training|Math & training]]

## Related concepts

- [[Concepts/AdamW|AdamW]]
- [[Concepts/Batch Size|Batch Size]]
- [[Concepts/Learning Rate|Learning Rate]]
- [[Concepts/Learning Rate Schedule|Learning Rate Schedule]]

## Taught in

- [[Lessons/03-09 Learning Rate Schedules and Warmup|03/09 Learning Rate Schedules and Warmup]] — Linearly ramping the LR from near-zero to the target value over the first N steps to stabilize optimizer statistics
- [[Lessons/19-36 Training Loop and Evaluation|19/36 Training Loop and Evaluation]] — The learning rate climbs from zero to its target over a fixed number of steps so the optimizer state can populate
- [[Lessons/19-44 Cosine LR with Linear Warmup|19/44 Cosine LR with Linear Warmup]] — Linear ramp from zero to lr_max over the first warmup_steps updates

## Sources

- Accurate, Large Minibatch SGD ([link](https://arxiv.org/abs/1706.02677))


%% ── my notes ── %%
