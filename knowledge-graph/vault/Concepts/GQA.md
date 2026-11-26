---
id: "concept:gqa"
type: concept
name: GQA
canonical: false
taught_in: 2
community: 1
tags:
  - concept/lesson-term
  - community/01
source: ai-engineering-from-scratch/phases/07-transformers-deep-dive/03-multi-head-attention/docs/en.md
---

# GQA

**Community:** [[Communities/01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism|01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism]]

> *What people say:* "The default since Llama 2"

**What it actually means:** Grouped-Query Attention with n_kv_heads < n_heads; repeats to match Q.

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]]
- [[Lessons/10-14 Open Models- Architecture Walkthroughs|10/14 Open Models: Architecture Walkthroughs]] — Grouped-Query Attention: G groups of Q heads share one K and one V head — shrinks KV cache without MQA's accuracy hit


%% ── my notes ── %%
