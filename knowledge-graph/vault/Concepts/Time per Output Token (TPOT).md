---
id: "concept:time-per-output-token-tpot"
type: concept
name: Time per Output Token (TPOT)
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

# Time per Output Token (TPOT)

**Community:** [[Communities/21 Time to First Token (TTFT) · Time per Output Token (TPOT) · Prefill|21 Time to First Token (TTFT) · Time per Output Token (TPOT) · Prefill]]

**What it actually means:** For one request with `N > 1` output tokens, the average post-first-token interval: `(t_N - t_1) / (N - 1)`. System distributions then aggregate those per-request averages.

**Why it matters:** Users can receive the first token quickly while the rest of the answer streams slowly, so startup latency alone does not describe generation responsiveness.

**In practice:** Compute TPOT separately for each request, report percentiles across requests by output length and concurrency, and avoid pooling all token intervals or comparing systems with different tokenizers and measurement boundaries.

**Common confusion:** TPOT is a per-request average. An individual inter-token latency is one gap between consecutive tokens, while time to first token includes the wait before output starts.

**Category:** [[Categories/Infrastructure & serving|Infrastructure & serving]]

## Related concepts

- [[Concepts/Decode Phase|Decode Phase]]
- [[Concepts/Goodput|Goodput]]
- [[Concepts/Inter-Token Latency (ITL)|Inter-Token Latency (ITL)]]
- [[Concepts/Streaming|Streaming]]
- [[Concepts/Tail Latency|Tail Latency]]
- [[Concepts/Time to First Token (TTFT)|Time to First Token (TTFT)]]

## Taught in

- [[Lessons/17-08 Inference Metrics — TTFT, TPOT, ITL, Goodput, P99|17/08 Inference Metrics — TTFT, TPOT, ITL, Goodput, P99]] — Memory-bound decode cost per token after first

## Sources

- DistServe ([link](https://arxiv.org/abs/2401.09670))


%% ── my notes ── %%
