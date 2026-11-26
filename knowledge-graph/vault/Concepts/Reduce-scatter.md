---
id: "concept:reduce-scatter"
type: concept
name: Reduce-scatter
canonical: false
taught_in: 3
community: 2
tags:
  - concept/lesson-term
  - community/02
source: ai-engineering-from-scratch/phases/10-llms-from-scratch/05-scaling-distributed/docs/en.md
---

# Reduce-scatter

**Community:** [[Communities/02 Bucket · Causal mask · Manifest|02 Bucket · Causal mask · Manifest]]

> *What people say:* "Sum and distribute"

**What it actually means:** Collective operation that reduces (sums) data and scatters different chunks to different GPUs -- used in FSDP for gradient sharding

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]]
- [[Lessons/19-76 Collective Ops From Scratch|19/76 Collective Ops From Scratch]] — Each rank ends with the sum of one chunk only
- [[Lessons/19-78 ZeRO Optimizer State Sharding|19/78 ZeRO Optimizer State Sharding]] — Deliver each rank only its shard's summed gradient


%% ── my notes ── %%
