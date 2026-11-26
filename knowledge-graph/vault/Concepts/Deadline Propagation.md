---
id: "concept:deadline-propagation"
type: concept
name: Deadline Propagation
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

# Deadline Propagation

**Community:** [[Communities/16 Backpressure · Rate Limit · Admission Control|16 Backpressure · Rate Limit · Admission Control]]

**What it actually means:** Passing the remaining end-to-end time budget to downstream calls so each dependency knows how long the original request can still usefully wait.

**Why it matters:** Independent timeouts can exceed the user's deadline and leave abandoned work consuming capacity after the result is no longer useful.

**In practice:** Set one request deadline at ingress, subtract elapsed time for each downstream call, cancel expired work, and record which boundary exhausted the budget.

**Common confusion:** A deadline is an absolute or remaining completion boundary. A retry delay controls when another attempt begins and must fit inside that same budget.

**Category:** [[Categories/Reliability & operations|Reliability & operations]]

## Related concepts

- [[Concepts/Retry Budget|Retry Budget]]
- [[Concepts/Retry with Backoff|Retry with Backoff]]
- [[Concepts/Service Level Objective (SLO)|Service Level Objective (SLO)]]
- [[Concepts/Tail Latency|Tail Latency]]

## Sources

- gRPC Deadlines ([link](https://grpc.io/docs/guides/deadlines/))


%% ── my notes ── %%
