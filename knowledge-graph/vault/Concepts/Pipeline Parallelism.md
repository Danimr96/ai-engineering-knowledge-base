---
id: "concept:pipeline-parallelism"
type: concept
name: Pipeline Parallelism
canonical: true
category: "Infrastructure & serving"
taught_in: 2
community: 1
tags:
  - concept/glossary
  - category/infrastructure-and-serving
  - community/01
source: ai-engineering-from-scratch/glossary/terms.md
---

# Pipeline Parallelism

**Community:** [[Communities/01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism|01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism]]

**What it actually means:** Partitioning sequential groups of model layers across devices and moving microbatches or requests through those stages as a pipeline.

**Why it matters:** It lets models exceed one device's memory, but stage imbalance, pipeline bubbles, activation transfers, and failure coordination affect usable performance.

**In practice:** Balance stage cost, choose a microbatch schedule, measure idle time and interconnect traffic, and keep model and checkpoint partition metadata versioned.

**Common confusion:** Pipeline parallelism divides layers by depth. Tensor parallelism divides tensor operations within a layer.

**Category:** [[Categories/Infrastructure & serving|Infrastructure & serving]]

## Related concepts

- [[Concepts/Batch Size|Batch Size]]
- [[Concepts/Expert Parallelism|Expert Parallelism]]
- [[Concepts/Model Serving|Model Serving]]
- [[Concepts/Tensor Parallelism|Tensor Parallelism]]

## Taught in

- [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]] — Each GPU runs a different group of layers; data flows through the pipeline with micro-batches to reduce bubbles
- [[Lessons/10-19 DualPipe Parallelism|10/19 DualPipe Parallelism]] `normalized` — Shards model layers across ranks; the dimension DualPipe schedules

## Sources

- [[Resources/GPipe|GPipe]] ([link](https://arxiv.org/abs/1811.06965))


%% ── my notes ── %%
