---
id: "concept:tokens-per-second-tps"
type: concept
name: Tokens per Second (TPS)
canonical: true
category: "Infrastructure & serving"
aliases:
  - TPS
  - output token throughput
taught_in: 0
community: 21
tags:
  - concept/glossary
  - category/infrastructure-and-serving
  - community/21
source: ai-engineering-from-scratch/glossary/terms.md
---

# Tokens per Second (TPS)

**Community:** [[Communities/21 Time to First Token (TTFT) · Time per Output Token (TPOT) · Prefill|21 Time to First Token (TTFT) · Time per Output Token (TPOT) · Prefill]]

**What it actually means:** A throughput measure reporting how many output tokens a serving system produces per unit time under a stated scope and workload.

**Why it matters:** It complements startup latency by showing how quickly generation proceeds after output begins and how serving behaves under load.

**In practice:** State whether TPS is per request or aggregate, exclude or identify prefill, and report batch, concurrency, sequence lengths, hardware, and percentile latency.

**Common confusion:** TPS is not directly comparable across different tokenizers, workloads, quality settings, or measurement boundaries.

**Category:** [[Categories/Infrastructure & serving|Infrastructure & serving]]

## Related concepts

- [[Concepts/Observability|Observability]]
- [[Concepts/Prefill|Prefill]]
- [[Concepts/Speculative Decoding|Speculative Decoding]]
- [[Concepts/Streaming|Streaming]]
- [[Concepts/Time to First Token (TTFT)|Time to First Token (TTFT)]]

## Sources

- Sarathi-Serve ([link](https://www.usenix.org/system/files/osdi24-agrawal.pdf))


%% ── my notes ── %%
