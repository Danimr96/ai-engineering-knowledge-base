---
id: "concept:goodput"
type: concept
name: Goodput
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

# Goodput

**Community:** [[Communities/21 Time to First Token (TTFT) · Time per Output Token (TPOT) · Prefill|21 Time to First Token (TTFT) · Time per Output Token (TPOT) · Prefill]]

**What it actually means:** The rate of completed requests that satisfy defined service constraints, such as both time-to-first-token and per-token latency objectives, under a stated workload.

**Why it matters:** Raw throughput can rise while users experience more slow requests. Goodput counts only work that meets the service contract.

**In practice:** Declare the request distribution and latency thresholds, count only compliant completions, report percentiles beside the aggregate rate, and avoid comparing systems under different objectives.

**Common confusion:** Goodput is not all completed throughput and is not a universal property of a model. It depends on workload and success thresholds.

**Category:** [[Categories/Infrastructure & serving|Infrastructure & serving]]

## Related concepts

- [[Concepts/Cost per Successful Task|Cost per Successful Task]]
- [[Concepts/Disaggregated Serving|Disaggregated Serving]]
- [[Concepts/Service Level Objective (SLO)|Service Level Objective (SLO)]]
- [[Concepts/Tail Latency|Tail Latency]]
- [[Concepts/Time per Output Token (TPOT)|Time per Output Token (TPOT)]]
- [[Concepts/Time to First Token (TTFT)|Time to First Token (TTFT)]]

## Taught in

- [[Lessons/17-04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill|17/04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill]] — Tokens/sec where every request still hit TTFT and ITL targets
- [[Lessons/17-08 Inference Metrics — TTFT, TPOT, ITL, Goodput, P99|17/08 Inference Metrics — TTFT, TPOT, ITL, Goodput, P99]] — Fraction of requests meeting every SLO constraint simultaneously

## Sources

- DistServe ([link](https://arxiv.org/abs/2401.09670))


%% ── my notes ── %%
