---
id: "concept:rate-limit"
type: concept
name: Rate Limit
canonical: true
category: AI-native development
taught_in: 2
community: 16
tags:
  - concept/glossary
  - category/ai-native-development
  - community/16
source: ai-engineering-from-scratch/glossary/terms.md
---

# Rate Limit

**Community:** [[Communities/16 Backpressure · Rate Limit · Admission Control|16 Backpressure · Rate Limit · Admission Control]]

**What it actually means:** A policy that caps requests, tokens, concurrent work, or another resource within a defined time or capacity window.

**Why it matters:** It protects providers and your own system from overload, uncontrolled spend, and unfair resource use.

**In practice:** Enforce per-tenant token and concurrency limits, read provider retry metadata, and queue or reject excess work predictably.

**Common confusion:** A rate limit controls allowed usage. Backpressure propagates downstream capacity constraints through a system.

**Category:** [[Categories/AI-native development|AI-native development]]

## Related concepts

- [[Concepts/Admission Control|Admission Control]]
- [[Concepts/Backpressure|Backpressure]]
- [[Concepts/Circuit Breaker|Circuit Breaker]]
- [[Concepts/Continuous Batching|Continuous Batching]]
- [[Concepts/Load Shedding|Load Shedding]]
- [[Concepts/Model Router|Model Router]]
- [[Concepts/Retry Budget|Retry Budget]]
- [[Concepts/Retry with Backoff|Retry with Backoff]]

## Taught in

- [[Lessons/00-04 APIs & Keys|00/04 APIs & Keys]] — Maximum requests per minute/hour to prevent abuse and ensure fair usage
- [[Lessons/17-27 FinOps for LLMs — Unit Economics and Multi-Tenant Attribution|17/27 FinOps for LLMs — Unit Economics and Multi-Tenant Attribution]] — Per-tenant ceiling enforced at gateway


%% ── my notes ── %%
