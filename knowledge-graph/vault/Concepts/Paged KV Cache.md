---
id: "concept:paged-kv-cache"
type: concept
name: Paged KV Cache
canonical: true
category: "Infrastructure & serving"
taught_in: 1
community: 5
tags:
  - concept/glossary
  - category/infrastructure-and-serving
  - community/05
source: ai-engineering-from-scratch/glossary/terms.md
---

# Paged KV Cache

**Community:** [[Communities/05 Temperature · Autoregressive · Logits|05 Temperature · Autoregressive · Logits]]

**What it actually means:** A KV-cache memory manager that stores attention state in fixed-size blocks and maps logical sequence positions to physical blocks instead of requiring one contiguous allocation per sequence.

**Why it matters:** Variable sequence lengths create fragmentation and unpredictable growth, so block-based allocation can improve usable memory and enable flexible sharing.

**In practice:** Select block size from workload measurements, track allocation and eviction, isolate state between requests, and test cancellation and prefix sharing under memory pressure.

**Common confusion:** Paged KV cache manages runtime attention-state memory. It does not move model parameters to disk or extend the model's trained context limit.

**Category:** [[Categories/Infrastructure & serving|Infrastructure & serving]]

## Related concepts

- [[Concepts/Context Window|Context Window]]
- [[Concepts/KV Cache|KV Cache]]
- [[Concepts/Model Serving|Model Serving]]
- [[Concepts/Prefix Caching|Prefix Caching]]

## Taught in

- [[Lessons/17-04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill|17/04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill]]

## Sources

- [[Resources/Efficient Memory Management for Large Language Model Serving with PagedAttention|Efficient Memory Management for Large Language Model Serving with PagedAttention]] ([link](https://arxiv.org/abs/2309.06180))


%% ── my notes ── %%
