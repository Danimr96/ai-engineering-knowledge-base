---
id: "concept:chunked-prefill"
type: concept
name: Chunked Prefill
canonical: true
category: "Infrastructure & serving"
taught_in: 1
community: 21
tags:
  - concept/glossary
  - category/infrastructure-and-serving
  - community/21
source: ai-engineering-from-scratch/glossary/terms.md
---

# Chunked Prefill

**Community:** [[Communities/21 Time to First Token (TTFT) · Time per Output Token (TPOT) · Prefill|21 Time to First Token (TTFT) · Time per Output Token (TPOT) · Prefill]]

**What it actually means:** A serving technique that divides a long prompt's prefill work into smaller schedulable pieces so prompt processing can interleave with decode work from other requests.

**Why it matters:** One long prompt can otherwise occupy the accelerator and delay active generations, producing poor tail latency even when total throughput looks healthy.

**In practice:** Choose a chunk policy from measured workloads, account for scheduling overhead, and compare prefill completion, decode latency, and goodput under mixed prompt lengths.

**Common confusion:** Chunked prefill changes how prompt computation is scheduled. It does not split the user's context into independent semantic chunks or change the model's context window.

**Category:** [[Categories/Infrastructure & serving|Infrastructure & serving]]

## Related concepts

- [[Concepts/Decode Phase|Decode Phase]]
- [[Concepts/Dynamic Batching|Dynamic Batching]]
- [[Concepts/Prefill|Prefill]]
- [[Concepts/Tail Latency|Tail Latency]]

## Taught in

- [[Lessons/17-04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill|17/04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill]] — Break long prefill into 512-token slices interleaved with decode

## Sources

- Sarathi-Serve ([link](https://arxiv.org/abs/2403.02310))


%% ── my notes ── %%
