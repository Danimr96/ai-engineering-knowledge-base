---
id: "concept:disaggregated-serving"
type: concept
name: Disaggregated Serving
canonical: true
category: "Infrastructure & serving"
taught_in: 2
community: 21
tags:
  - concept/glossary
  - category/infrastructure-and-serving
  - community/21
source: ai-engineering-from-scratch/glossary/terms.md
---

# Disaggregated Serving

**Community:** [[Communities/21 Time to First Token (TTFT) · Time per Output Token (TPOT) · Prefill|21 Time to First Token (TTFT) · Time per Output Token (TPOT) · Prefill]]

**What it actually means:** A serving architecture that runs prefill and decode work in separately provisioned worker pools and transfers the required attention state between them.

**Why it matters:** Prefill and decode stress hardware differently, so independent pools can be sized and scheduled for their own bottlenecks instead of competing in one queue.

**In practice:** Measure state-transfer cost, route requests through compatible model versions, scale each pool from its own demand signal, and test failure recovery between phases.

**Common confusion:** Disaggregation separates runtime stages. It does not split one model into tensor or pipeline-parallel shards within a stage.

**Category:** [[Categories/Infrastructure & serving|Infrastructure & serving]]

## Related concepts

- [[Concepts/Decode Phase|Decode Phase]]
- [[Concepts/Goodput|Goodput]]
- [[Concepts/Model Serving|Model Serving]]
- [[Concepts/Prefill|Prefill]]

## Taught in

- [[Lessons/17-07 Hardware-Specialized Inference Compilation — FP8 and NVFP4 on Blackwell|17/07 Hardware-Specialized Inference Compilation — FP8 and NVFP4 on Blackwell]] — Prefill and decode on separate GPU pools; KV transferred over NVLink/IB
- [[Lessons/17-17 Disaggregated Prefill-Decode — NVIDIA Dynamo and llm-d|17/17 Disaggregated Prefill/Decode — NVIDIA Dynamo and llm-d]] — Separate GPU pools for each phase

## Sources

- DistServe ([link](https://arxiv.org/abs/2401.09670))


%% ── my notes ── %%
