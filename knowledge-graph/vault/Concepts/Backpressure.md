---
id: "concept:backpressure"
type: concept
name: Backpressure
canonical: true
category: AI-native development
taught_in: 1
community: 16
tags:
  - concept/glossary
  - category/ai-native-development
  - community/16
source: ai-engineering-from-scratch/glossary/terms.md
---

# Backpressure

**Community:** [[Communities/16 Backpressure · Rate Limit · Admission Control|16 Backpressure · Rate Limit · Admission Control]]

**What it actually means:** A flow-control mechanism that slows or rejects upstream work when a downstream component cannot process it safely at the current rate.

**Why it matters:** Without backpressure, queued agent runs, tool calls, or streamed events can exhaust memory, exceed rate limits, and amplify retries.

**In practice:** When the evaluator queue reaches its limit, pause new agent jobs or return a retryable response instead of accepting unbounded work.

**Common confusion:** Backpressure protects capacity before failure. A circuit breaker stops calls after failures show a dependency is unhealthy.

**Category:** [[Categories/AI-native development|AI-native development]]

## Related concepts

- [[Concepts/Admission Control|Admission Control]]
- [[Concepts/Autoscaling|Autoscaling]]
- [[Concepts/Circuit Breaker|Circuit Breaker]]
- [[Concepts/Continuous Batching|Continuous Batching]]
- [[Concepts/Load Shedding|Load Shedding]]
- [[Concepts/Rate Limit|Rate Limit]]
- [[Concepts/Retry with Backoff|Retry with Backoff]]
- [[Concepts/Saturation|Saturation]]

## Taught in

- [[Lessons/13-29 MCP Reliability, Cancellation, and Flow Control|13/29 MCP Reliability, Cancellation, and Flow Control]] — Control applied when producers outpace consumers


%% ── my notes ── %%
