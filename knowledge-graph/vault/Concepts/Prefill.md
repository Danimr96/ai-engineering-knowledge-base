---
id: "concept:prefill"
type: concept
name: Prefill
canonical: true
category: "Infrastructure & serving"
aliases:
  - Prefill Phase
taught_in: 3
community: 21
tags:
  - concept/glossary
  - category/infrastructure-and-serving
  - community/21
source: ai-engineering-from-scratch/glossary/terms.md
---

# Prefill

**Community:** [[Communities/21 Time to First Token (TTFT) · Time per Output Token (TPOT) · Prefill|21 Time to First Token (TTFT) · Time per Output Token (TPOT) · Prefill]]

**What it actually means:** The initial inference stage that processes all supplied input tokens to produce their representations and the attention state required for subsequent autoregressive generation.

**Why it matters:** Prompt shape, queueing, and cache reuse affect prefill cost, and prefill competes differently for compute than decode, so it strongly influences startup latency and serving schedules.

**In practice:** Record prompt tokens and prefill latency, separate queue time from execution time, compare cached and uncached prefixes, and test long prompts beside active decode traffic.

**Common confusion:** Prefill is the runtime prompt-processing stage, not the first generated token itself. The first token appears only after prefill and any queueing complete.

**Category:** [[Categories/Infrastructure & serving|Infrastructure & serving]]

## Related concepts

- [[Concepts/Chunked Prefill|Chunked Prefill]]
- [[Concepts/Decode Phase|Decode Phase]]
- [[Concepts/Disaggregated Serving|Disaggregated Serving]]
- [[Concepts/KV Cache|KV Cache]]
- [[Concepts/Time to First Token (TTFT)|Time to First Token (TTFT)]]
- [[Concepts/Tokens per Second (TPS)|Tokens per Second (TPS)]]

## Taught in

- [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]] — The first inference phase where all prompt tokens are processed in parallel -- compute-bound on GPU FLOPS
- [[Lessons/10-12 Inference Optimization|10/12 Inference Optimization]] — Computing attention over all input tokens in parallel -- compute-bound because the full matrix multiplication keeps GPU cores busy
- [[Lessons/17-17 Disaggregated Prefill-Decode — NVIDIA Dynamo and llm-d|17/17 Disaggregated Prefill/Decode — NVIDIA Dynamo and llm-d]]

## Sources

- DistServe ([link](https://arxiv.org/abs/2401.09670))
- Sarathi-Serve ([link](https://www.usenix.org/system/files/osdi24-agrawal.pdf))


%% ── my notes ── %%
