---
id: "concept:expert-parallelism"
type: concept
name: Expert Parallelism
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

# Expert Parallelism

**Community:** [[Communities/01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism|01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism]]

**What it actually means:** Distributing mixture-of-experts subnetworks across devices and routing each token's activations to the devices that host its selected experts.

**Why it matters:** Sparse experts increase model capacity without executing every expert for every token, but routing introduces communication, load-balance, and placement constraints.

**In practice:** Measure token distribution by expert, provision communication bandwidth, cap or route overflow deliberately, and test quality when traffic produces uneven expert demand.

**Common confusion:** Expert parallelism partitions experts selected by a router. Tensor parallelism partitions the tensor operations inside layers.

**Category:** [[Categories/Infrastructure & serving|Infrastructure & serving]]

## Related concepts

- [[Concepts/Model Serving|Model Serving]]
- [[Concepts/MoE (Mixture of Experts)|MoE (Mixture of Experts)]]
- [[Concepts/Pipeline Parallelism|Pipeline Parallelism]]
- [[Concepts/Tensor Parallelism|Tensor Parallelism]]

## Taught in

- [[Lessons/07-11 Mixture of Experts (MoE)|07/11 Mixture of Experts (MoE)]] — Distribute different experts to different GPUs; route tokens across the network.
- [[Lessons/10-19 DualPipe Parallelism|10/19 DualPipe Parallelism]] `normalized` — Shards MoE experts across ranks so different GPUs hold different experts

## Sources

- GShard ([link](https://arxiv.org/abs/2006.16668))


%% ── my notes ── %%
