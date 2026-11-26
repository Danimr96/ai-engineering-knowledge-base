---
id: "concept:continuous-batching"
type: concept
name: Continuous Batching
canonical: true
category: "Infrastructure & serving"
taught_in: 3
community: 16
tags:
  - concept/glossary
  - category/infrastructure-and-serving
  - community/16
source: ai-engineering-from-scratch/glossary/terms.md
---

# Continuous Batching

**Community:** [[Communities/16 Backpressure · Rate Limit · Admission Control|16 Backpressure · Rate Limit · Admission Control]]

**What it actually means:** A serving scheduler that adds and removes generation requests at iteration boundaries instead of waiting for every request in a fixed batch to finish.

**Why it matters:** Autoregressive requests produce different output lengths, so continuous batching can keep accelerators utilized without forcing short requests to wait for the longest one.

**In practice:** Admit new requests when capacity becomes available, track per-request latency, and apply backpressure when the live batch or KV-cache budget is full.

**Common confusion:** Continuous batching is an inference scheduling policy, not gradient accumulation or a training batch-size technique.

**Category:** [[Categories/Infrastructure & serving|Infrastructure & serving]]

## Related concepts

- [[Concepts/Backpressure|Backpressure]]
- [[Concepts/Decode Phase|Decode Phase]]
- [[Concepts/Dynamic Batching|Dynamic Batching]]
- [[Concepts/Rate Limit|Rate Limit]]

## Taught in

- [[Lessons/07-12 KV Cache, Flash Attention & Inference Optimization|07/12 KV Cache, Flash Attention & Inference Optimization]] — Swap finished sequences out, new ones in, without draining the batch.
- [[Lessons/10-12 Inference Optimization|10/12 Inference Optimization]] — Inserting new requests into the running batch as soon as any request finishes, evaluated at every decode iteration rather than waiting for the whole batch
- [[Lessons/17-04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill|17/04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill]] — Admit/release decisions made every decode iteration

## Sources

- Orca ([link](https://www.usenix.org/conference/osdi22/presentation/yu))


%% ── my notes ── %%
