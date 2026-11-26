---
id: "concept:all-reduce"
type: concept
name: All-reduce
canonical: false
taught_in: 2
community: 1
tags:
  - concept/lesson-term
  - community/01
source: ai-engineering-from-scratch/phases/10-llms-from-scratch/05-scaling-distributed/docs/en.md
---

# All-reduce

**Community:** [[Communities/01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism|01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism]]

> *What people say:* "Average across GPUs"

**What it actually means:** Collective operation where every GPU ends with the sum (or average) of all GPUs' inputs -- typically implemented as ring all-reduce

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]]
- [[Lessons/19-48 Distributed Data Parallel and FSDP from Scratch|19/48 Distributed Data Parallel and FSDP from Scratch]] — Sum a tensor across all ranks, every rank ends with the same result


%% ── my notes ── %%
