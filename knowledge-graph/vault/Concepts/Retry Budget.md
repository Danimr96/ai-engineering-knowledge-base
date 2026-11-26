---
id: "concept:retry-budget"
type: concept
name: Retry Budget
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

# Retry Budget

**Community:** [[Communities/16 Backpressure · Rate Limit · Admission Control|16 Backpressure · Rate Limit · Admission Control]]

**What it actually means:** A bound on retry traffic, usually expressed relative to original requests or over a time window, that prevents retries from consuming unbounded capacity.

**Why it matters:** When a dependency slows or fails, unrestricted retries multiply load exactly when the system has the least spare capacity.

**In practice:** Count retries separately from first attempts, cap them by service and tenant, honor deadlines, use jittered backoff, and stop retrying non-transient or non-idempotent failures.

**Common confusion:** A retry budget limits extra attempts. An error budget measures user-visible unreliability allowed by an SLO.

**Category:** [[Categories/Reliability & operations|Reliability & operations]]

## Related concepts

- [[Concepts/Admission Control|Admission Control]]
- [[Concepts/Deadline Propagation|Deadline Propagation]]
- [[Concepts/Error Budget|Error Budget]]
- [[Concepts/Rate Limit|Rate Limit]]
- [[Concepts/Retry with Backoff|Retry with Backoff]]

## Sources

- Google SRE: Addressing Cascading Failures ([link](https://sre.google/sre-book/addressing-cascading-failures/))


%% ── my notes ── %%
