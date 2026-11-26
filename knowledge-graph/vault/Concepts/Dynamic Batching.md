---
id: "concept:dynamic-batching"
type: concept
name: Dynamic Batching
canonical: true
category: "Infrastructure & serving"
taught_in: 1
community: 16
tags:
  - concept/glossary
  - category/infrastructure-and-serving
  - community/16
source: ai-engineering-from-scratch/glossary/terms.md
---

# Dynamic Batching

**Community:** [[Communities/16 Backpressure · Rate Limit · Admission Control|16 Backpressure · Rate Limit · Admission Control]]

**What it actually means:** A runtime policy that forms inference batches from queued requests according to compatible shapes, maximum size, priority, and allowed queue delay.

**Why it matters:** Grouping requests can improve hardware utilization, but waiting for a batch can make latency worse when traffic is sparse or requests differ sharply.

**In practice:** Set queue-delay and batch limits from measured latency objectives, separate incompatible request shapes, and compare throughput with tail latency at realistic arrival rates.

**Common confusion:** Dynamic batching assembles batches from queued work. Continuous batching changes membership while autoregressive generation is already running.

**Category:** [[Categories/Infrastructure & serving|Infrastructure & serving]]

## Related concepts

- [[Concepts/Admission Control|Admission Control]]
- [[Concepts/Chunked Prefill|Chunked Prefill]]
- [[Concepts/Continuous Batching|Continuous Batching]]
- [[Concepts/Saturation|Saturation]]
- [[Concepts/Tail Latency|Tail Latency]]

## Taught in

- [[Lessons/17-04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill|17/04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill]]

## Sources

- NVIDIA Triton: Models and Schedulers ([link](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/model_configuration.html#scheduling-and-batching))


%% ── my notes ── %%
