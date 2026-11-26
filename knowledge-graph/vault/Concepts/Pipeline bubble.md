---
id: "concept:pipeline-bubble"
type: concept
name: Pipeline bubble
canonical: false
taught_in: 2
community: 1
tags:
  - concept/lesson-term
  - community/01
source: ai-engineering-from-scratch/phases/10-llms-from-scratch/05-scaling-distributed/docs/en.md
---

# Pipeline bubble

**Community:** [[Communities/01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism|01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism]]

> *What people say:* "Idle time in the pipeline"

**What it actually means:** Fraction of time GPUs sit idle waiting for data from the previous stage -- reduced by using more micro-batches

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]]
- [[Lessons/10-19 DualPipe Parallelism|10/19 DualPipe Parallelism]] — GPU cycles wasted because a pipeline stage is waiting for its input or gradient


%% ── my notes ── %%
