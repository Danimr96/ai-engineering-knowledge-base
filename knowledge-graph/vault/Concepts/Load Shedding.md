---
id: "concept:load-shedding"
type: concept
name: Load Shedding
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

# Load Shedding

**Community:** [[Communities/16 Backpressure · Rate Limit · Admission Control|16 Backpressure · Rate Limit · Admission Control]]

**What it actually means:** Deliberately rejecting, dropping, or cancelling selected work at one or more overload boundaries when demand exceeds the capacity available to produce useful results.

**Why it matters:** Continuing to accept every request during overload can increase queueing until nearly all requests miss their deadlines and recovery becomes harder.

**In practice:** Shed at the earliest informed boundary, preserve high-priority and already-admitted work when possible, identify the overloaded scope, and mark a response retryable only when the condition is transient and the request remains within its retry budget.

**Common confusion:** Load shedding is not confined to work that has already been accepted. Admission control is specifically the pre-acceptance gate, while rate limiting can enforce a usage policy even when capacity remains.

**Category:** [[Categories/Reliability & operations|Reliability & operations]]

## Related concepts

- [[Concepts/Admission Control|Admission Control]]
- [[Concepts/Backpressure|Backpressure]]
- [[Concepts/Graceful Degradation|Graceful Degradation]]
- [[Concepts/Rate Limit|Rate Limit]]

## Sources

- Google SRE: Handling Overload ([link](https://sre.google/sre-book/handling-overload/))


%% ── my notes ── %%
