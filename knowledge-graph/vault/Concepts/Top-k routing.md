---
id: "concept:top-k-routing"
type: concept
name: Top-k routing
canonical: false
taught_in: 2
community: 1
tags:
  - concept/lesson-term
  - community/01
source: ai-engineering-from-scratch/phases/07-transformers-deep-dive/11-mixture-of-experts/docs/en.md
---

# Top-k routing

**Community:** [[Communities/01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism|01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism]]

> *What people say:* "k active experts per token"

**What it actually means:** Each token's FFN computation goes through exactly k experts, weighted by gate.

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/07-11 Mixture of Experts (MoE)|07/11 Mixture of Experts (MoE)]]
- [[Lessons/10-14 Open Models- Architecture Walkthroughs|10/14 Open Models: Architecture Walkthroughs]] — The router computes a score per expert and activates the k highest — typical k is 2 (Mixtral) to 8 (DeepSeek)


%% ── my notes ── %%
