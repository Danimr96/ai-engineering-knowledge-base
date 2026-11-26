---
id: "concept:decode-phase"
type: concept
name: Decode Phase
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

# Decode Phase

**Community:** [[Communities/21 Time to First Token (TTFT) · Time per Output Token (TPOT) · Prefill|21 Time to First Token (TTFT) · Time per Output Token (TPOT) · Prefill]]

**What it actually means:** The iterative stage of autoregressive inference that generates new tokens one step at a time after the input prefix has been processed.

**Why it matters:** Decode work has different compute, memory, and scheduling behavior from prefill, so one aggregate latency number can hide the actual serving bottleneck.

**In practice:** Measure inter-token latency and output throughput separately, account for KV-cache occupancy, and test mixed workloads where active decodes share capacity with new prefills.

**Common confusion:** Decode phase is not the decoder component of an encoder-decoder model. It names the runtime generation stage.

**Category:** [[Categories/Infrastructure & serving|Infrastructure & serving]]

## Related concepts

- [[Concepts/Autoregressive|Autoregressive]]
- [[Concepts/Chunked Prefill|Chunked Prefill]]
- [[Concepts/Continuous Batching|Continuous Batching]]
- [[Concepts/Disaggregated Serving|Disaggregated Serving]]
- [[Concepts/Inter-Token Latency (ITL)|Inter-Token Latency (ITL)]]
- [[Concepts/KV Cache|KV Cache]]
- [[Concepts/Prefill|Prefill]]
- [[Concepts/Time per Output Token (TPOT)|Time per Output Token (TPOT)]]

## Taught in

- [[Lessons/17-17 Disaggregated Prefill-Decode — NVIDIA Dynamo and llm-d|17/17 Disaggregated Prefill/Decode — NVIDIA Dynamo and llm-d]]

## Sources

- DistServe ([link](https://arxiv.org/abs/2401.09670))


%% ── my notes ── %%
