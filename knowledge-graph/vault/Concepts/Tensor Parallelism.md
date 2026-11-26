---
id: "concept:tensor-parallelism"
type: concept
name: Tensor Parallelism
canonical: true
category: "Infrastructure & serving"
taught_in: 1
community: 1
tags:
  - concept/glossary
  - category/infrastructure-and-serving
  - community/01
source: ai-engineering-from-scratch/glossary/terms.md
---

# Tensor Parallelism

**Community:** [[Communities/01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism|01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism]]

**What it actually means:** Partitioning tensor operations within a model layer across devices, with collective communication combining partial results during the layer computation.

**Why it matters:** It lets one layer use memory and compute from several devices, but frequent communication can dominate when the interconnect or partition is unsuitable.

**In practice:** Match partition dimensions to model shapes, benchmark collective traffic, keep ranks on a fast interconnect, and record the sharding layout with checkpoints and serving configuration.

**Common confusion:** Tensor parallelism splits work inside layers. Pipeline parallelism places different layer groups on different devices.

**Category:** [[Categories/Infrastructure & serving|Infrastructure & serving]]

## Related concepts

- [[Concepts/Expert Parallelism|Expert Parallelism]]
- [[Concepts/Parameter|Parameter]]
- [[Concepts/Pipeline Parallelism|Pipeline Parallelism]]
- [[Concepts/Tensor|Tensor]]

## Taught in

- [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]] — Partition weight matrices so each GPU computes part of the matmul; requires fast NVLink interconnect

## Sources

- Megatron-LM ([link](https://arxiv.org/abs/1909.08053))


%% ── my notes ── %%
