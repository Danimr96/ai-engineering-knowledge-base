---
id: "concept:mla"
type: concept
name: MLA
canonical: false
taught_in: 3
community: 1
tags:
  - concept/lesson-term
  - community/01
source: ai-engineering-from-scratch/phases/07-transformers-deep-dive/03-multi-head-attention/docs/en.md
---

# MLA

**Community:** [[Communities/01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism|01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism]]

> *What people say:* "DeepSeek's trick"

**What it actually means:** Multi-head Latent Attention: K,V compressed to low-rank latent, decompressed at attend time.

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]]
- [[Lessons/10-14 Open Models- Architecture Walkthroughs|10/14 Open Models: Architecture Walkthroughs]] — Multi-Head Latent Attention: compress K/V into a shared low-rank latent, decompress per head — smallest KV cache for large models
- [[Lessons/10-20 DeepSeek-V3 Architecture Walkthrough|10/20 DeepSeek-V3 Architecture Walkthrough]] — Compress K and V into a shared low-rank latent (kv_lora_rank, typically 512), decompress per head on-the-fly; KV cache stores only the latent


%% ── my notes ── %%
