---
id: "concept:time-to-first-token-ttft"
type: concept
name: Time to First Token (TTFT)
canonical: true
category: "Models & inference"
aliases:
  - TTFT
taught_in: 3
community: 21
tags:
  - concept/glossary
  - category/models-and-inference
  - community/21
source: ai-engineering-from-scratch/glossary/terms.md
---

# Time to First Token (TTFT)

**Community:** [[Communities/21 Time to First Token (TTFT) · Time per Output Token (TPOT) · Prefill|21 Time to First Token (TTFT) · Time per Output Token (TPOT) · Prefill]]

**What it actually means:** The elapsed time from submitting a generation request until the client receives the first output token or content event under a defined measurement boundary.

**Why it matters:** TTFT strongly affects perceived responsiveness and can reveal queueing, prompt processing, cache, or network delays.

**In practice:** Record client-side TTFT by model, prompt length, region, and cache status, then separate it from total completion time.

**Common confusion:** TTFT is not tokens per second. One measures startup latency; the other measures generation throughput after output begins.

**Category:** [[Categories/Models & inference|Models & inference]]

## Related concepts

- [[Concepts/Goodput|Goodput]]
- [[Concepts/Inter-Token Latency (ITL)|Inter-Token Latency (ITL)]]
- [[Concepts/Observability|Observability]]
- [[Concepts/Prefill|Prefill]]
- [[Concepts/Prompt Cache|Prompt Cache]]
- [[Concepts/Streaming|Streaming]]
- [[Concepts/Tail Latency|Tail Latency]]
- [[Concepts/Time per Output Token (TPOT)|Time per Output Token (TPOT)]]
- [[Concepts/Token Budget|Token Budget]]
- [[Concepts/Tokens per Second (TPS)|Tokens per Second (TPS)]]
- [[Concepts/Trace|Trace]]

## Taught in

- [[Lessons/10-12 Inference Optimization|10/12 Inference Optimization]] `alias` — Latency from receiving a request to producing the first output token -- dominated by prefill time for long prompts
- [[Lessons/17-04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill|17/04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill]] `alias` — Prefill + queue + network; dominated by prefill at long prompts
- [[Lessons/17-08 Inference Metrics — TTFT, TPOT, ITL, Goodput, P99|17/08 Inference Metrics — TTFT, TPOT, ITL, Goodput, P99]] `alias` — Queue + network + prefill; dominated by prefill at long prompts


%% ── my notes ── %%
