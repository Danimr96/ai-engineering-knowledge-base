---
id: "concept:circuit-breaker"
type: concept
name: Circuit Breaker
canonical: true
category: AI-native development
taught_in: 3
community: 16
tags:
  - concept/glossary
  - category/ai-native-development
  - community/16
source: ai-engineering-from-scratch/glossary/terms.md
---

# Circuit Breaker

**Community:** [[Communities/16 Backpressure · Rate Limit · Admission Control|16 Backpressure · Rate Limit · Admission Control]]

**What it actually means:** A reliability control that temporarily stops calls to a dependency after failures cross a threshold, then probes whether the dependency has recovered.

**Why it matters:** It prevents repeated model or tool failures from consuming latency, budget, and capacity across the rest of the system.

**In practice:** Open the breaker after repeated provider timeouts, fail over or return a controlled response, then allow a limited health probe after a cooldown.

**Common confusion:** A circuit breaker reacts to dependency health. A rate limit controls allowed request volume.

**Category:** [[Categories/AI-native development|AI-native development]]

## Related concepts

- [[Concepts/Backpressure|Backpressure]]
- [[Concepts/Graceful Degradation|Graceful Degradation]]
- [[Concepts/Model Router|Model Router]]
- [[Concepts/Rate Limit|Rate Limit]]
- [[Concepts/Retry with Backoff|Retry with Backoff]]

## Taught in

- [[Lessons/11-11 Caching, Rate Limiting & Cost Optimization|11/11 Caching, Rate Limiting & Cost Optimization]] — Automatically degrading service (cheaper models, cached-only) or stopping requests entirely when spending approaches the budget limit
- [[Lessons/15-14 Kill Switches, Circuit Breakers, and Canary Tokens|15/14 Kill Switches, Circuit Breakers, and Canary Tokens]] — Action-specific trip on repetition, failure rate, or rate-limit
- [[Lessons/16-23 Failure Modes — MAST, Groupthink, Monoculture, Cascading Errors|16/23 Failure Modes — MAST, Groupthink, Monoculture, Cascading Errors]] — Open when error rate exceeds threshold; short-circuit with default.


%% ── my notes ── %%
