---
id: "concept:inter-token-latency-itl"
type: concept
name: Inter-Token Latency (ITL)
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

# Inter-Token Latency (ITL)

**Community:** [[Communities/21 Time to First Token (TTFT) · Time per Output Token (TPOT) · Prefill|21 Time to First Token (TTFT) · Time per Output Token (TPOT) · Prefill]]

**What it actually means:** The elapsed time between two consecutive output-token arrival events for one request, calculated as `t_i - t_(i-1)` for an output token after the first.

**Why it matters:** Individual gaps expose decode stalls and streaming jitter that a per-request average can hide, especially under batching, preemption, or mixed workloads.

**In practice:** Record each post-first-token interval with its request and token position, then report distributions by workload, output length, and concurrency without pooling away request boundaries.

**Common confusion:** ITL is one interval between consecutive tokens. Time per output token is a per-request average across those intervals, while time to first token covers the wait before streaming begins.

**Category:** [[Categories/Infrastructure & serving|Infrastructure & serving]]

## Related concepts

- [[Concepts/Decode Phase|Decode Phase]]
- [[Concepts/Tail Latency|Tail Latency]]
- [[Concepts/Time per Output Token (TPOT)|Time per Output Token (TPOT)]]
- [[Concepts/Time to First Token (TTFT)|Time to First Token (TTFT)]]

## Taught in

- [[Lessons/17-04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill|17/04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill]] `alias` — Time between consecutive decode tokens; dominated by batch size
- [[Lessons/17-08 Inference Metrics — TTFT, TPOT, ITL, Goodput, P99|17/08 Inference Metrics — TTFT, TPOT, ITL, Goodput, P99]] — Same as TPOT in most tools (not all — see GenAI-Perf)

## Sources

- DistServe ([link](https://arxiv.org/abs/2401.09670))


%% ── my notes ── %%
