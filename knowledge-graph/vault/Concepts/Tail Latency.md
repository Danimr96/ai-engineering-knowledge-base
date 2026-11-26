---
id: "concept:tail-latency"
type: concept
name: Tail Latency
canonical: true
category: "Reliability & operations"
taught_in: 1
community: 21
tags:
  - concept/glossary
  - category/reliability-and-operations
  - community/21
source: ai-engineering-from-scratch/glossary/terms.md
---

# Tail Latency

**Community:** [[Communities/21 Time to First Token (TTFT) · Time per Output Token (TPOT) · Prefill|21 Time to First Token (TTFT) · Time per Output Token (TPOT) · Prefill]]

**What it actually means:** The latency experienced by the slowest portion of requests, commonly summarized with a high percentile under a stated workload and time window.

**Why it matters:** Averages can look healthy while a meaningful group of users waits much longer because of queueing, contention, retries, or variable request cost.

**In practice:** Report several percentiles by route and workload, retain timeouts as censored or failed observations according to a documented rule, and trace slow requests across dependencies.

**Common confusion:** Tail latency is not the single slowest request and has no meaning without the percentile, population, and measurement boundary.

**Category:** [[Categories/Reliability & operations|Reliability & operations]]

## Related concepts

- [[Concepts/Chunked Prefill|Chunked Prefill]]
- [[Concepts/Deadline Propagation|Deadline Propagation]]
- [[Concepts/Dynamic Batching|Dynamic Batching]]
- [[Concepts/Goodput|Goodput]]
- [[Concepts/Inter-Token Latency (ITL)|Inter-Token Latency (ITL)]]
- [[Concepts/Saturation|Saturation]]
- [[Concepts/Service Level Indicator (SLI)|Service Level Indicator (SLI)]]
- [[Concepts/Time per Output Token (TPOT)|Time per Output Token (TPOT)]]
- [[Concepts/Time to First Token (TTFT)|Time to First Token (TTFT)]]

## Taught in

- [[Lessons/17-08 Inference Metrics — TTFT, TPOT, ITL, Goodput, P99|17/08 Inference Metrics — TTFT, TPOT, ITL, Goodput, P99]]

## Sources

- The Tail at Scale ([link](https://research.google/pubs/the-tail-at-scale/))


%% ── my notes ── %%
