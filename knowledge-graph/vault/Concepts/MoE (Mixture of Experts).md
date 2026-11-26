---
id: "concept:moe-mixture-of-experts"
type: concept
name: MoE (Mixture of Experts)
canonical: true
category: "Models & inference"
taught_in: 2
community: 1
tags:
  - concept/glossary
  - category/models-and-inference
  - community/01
source: ai-engineering-from-scratch/glossary/terms.md
---

# MoE (Mixture of Experts)

**Community:** [[Communities/01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism|01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism]]

> *What people say:* A large model that activates only part of its parameters for each token.

**What it actually means:** An architecture with multiple expert subnetworks and a learned router that selects a subset for each input unit, often each token. Sparse activation can increase total parameter capacity without using every expert on every forward pass.

**Why it matters:** Compute, memory, communication, routing balance, and quality depend on the specific architecture and serving system.

**Common confusion:** Product names do not prove an MoE architecture unless the model developer discloses it.

**Category:** [[Categories/Models & inference|Models & inference]]

## Related concepts

- [[Concepts/Expert Parallelism|Expert Parallelism]]
- [[Concepts/Model Router|Model Router]]
- [[Concepts/Parameter|Parameter]]
- [[Concepts/Transformer|Transformer]]

## Taught in

- [[Lessons/07-11 Mixture of Experts (MoE)|07/11 Mixture of Experts (MoE)]]
- [[Lessons/10-14 Open Models- Architecture Walkthroughs|10/14 Open Models: Architecture Walkthroughs]] `alias` — Mixture of Experts: N MLPs per block, router picks top-k per token — huge total params, small active params


%% ── my notes ── %%
