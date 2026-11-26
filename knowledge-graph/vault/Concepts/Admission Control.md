---
id: "concept:admission-control"
type: concept
name: Admission Control
canonical: true
category: "Reliability & operations"
taught_in: 0
community: 16
tags:
  - concept/glossary
  - category/reliability-and-operations
  - community/16
source: ai-engineering-from-scratch/glossary/terms.md
---

# Admission Control

**Community:** [[Communities/16 Backpressure · Rate Limit · Admission Control|16 Backpressure · Rate Limit · Admission Control]]

**What it actually means:** A pre-acceptance gate that decides whether a request may enter a bounded queue or service under the system's current capacity, priority, and policy.

**Why it matters:** Rejecting excess work at a controlled boundary protects admitted requests from queue growth, timeout cascades, and resource exhaustion.

**In practice:** Estimate the request's cost, check tenant and system capacity, reserve the required budget atomically, and identify the overloaded scope when rejecting. Give retry guidance only when the condition is transient and the caller's retry budget permits another attempt.

**Common confusion:** Admission control acts before acceptance. Load shedding can reject or remove work at ingress, in queues, at dependencies, or at other overload boundaries.

**Category:** [[Categories/Reliability & operations|Reliability & operations]]

## Related concepts

- [[Concepts/Backpressure|Backpressure]]
- [[Concepts/Dynamic Batching|Dynamic Batching]]
- [[Concepts/Load Shedding|Load Shedding]]
- [[Concepts/Rate Limit|Rate Limit]]
- [[Concepts/Retry Budget|Retry Budget]]
- [[Concepts/Saturation|Saturation]]

## Sources

- Google SRE: Handling Overload ([link](https://sre.google/sre-book/handling-overload/))


%% ── my notes ── %%
