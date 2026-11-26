---
id: "concept:pagedattention"
type: concept
name: PagedAttention
canonical: false
taught_in: 3
community: 5
tags:
  - concept/lesson-term
  - community/05
source: ai-engineering-from-scratch/phases/07-transformers-deep-dive/12-kv-cache-flash-attention/docs/en.md
---

# PagedAttention

**Community:** [[Communities/05 Temperature · Autoregressive · Logits|05 Temperature · Autoregressive · Logits]]

> *What people say:* "vLLM's headline"

**What it actually means:** KV cache allocated in fixed blocks with a page table; eliminates fragmentation.

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/07-12 KV Cache, Flash Attention & Inference Optimization|07/12 KV Cache, Flash Attention & Inference Optimization]]
- [[Lessons/10-12 Inference Optimization|10/12 Inference Optimization]] — Allocating KV cache in fixed-size pages instead of contiguous blocks, eliminating memory fragmentation and enabling copy-on-write for shared prefixes
- [[Lessons/17-04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill|17/04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill]] — Fixed-size block allocator for KV cache; fragmentation <4%


%% ── my notes ── %%
