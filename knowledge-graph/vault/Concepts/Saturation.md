---
id: "concept:saturation"
type: concept
name: Saturation
canonical: true
category: "Reliability & operations"
taught_in: 1
community: 16
tags:
  - concept/glossary
  - category/reliability-and-operations
  - community/16
source: ai-engineering-from-scratch/glossary/terms.md
---

# Saturation

**Community:** [[Communities/16 Backpressure · Rate Limit · Admission Control|16 Backpressure · Rate Limit · Admission Control]]

**What it actually means:** The degree to which a constrained resource or service has exhausted its capacity, including queued work that cannot begin promptly.

**Why it matters:** Utilization alone can appear acceptable while memory, accelerator slots, queue depth, or a downstream quota is already limiting useful throughput.

**In practice:** Identify each critical resource, measure active and waiting work, relate saturation to tail latency and errors, and alert before the queue enters an unstable growth regime.

**Common confusion:** Saturation is not one universal percentage. The limiting resource and its queueing behavior depend on the workload and architecture.

**Category:** [[Categories/Reliability & operations|Reliability & operations]]

## Related concepts

- [[Concepts/Admission Control|Admission Control]]
- [[Concepts/Autoscaling|Autoscaling]]
- [[Concepts/Backpressure|Backpressure]]
- [[Concepts/Dynamic Batching|Dynamic Batching]]
- [[Concepts/Observability|Observability]]
- [[Concepts/Tail Latency|Tail Latency]]

## Taught in

- [[Lessons/03-04 Activation Functions|03/04 Activation Functions]] — Regions where an activation's derivative approaches zero, blocking gradient flow

## Sources

- Google SRE: Monitoring Distributed Systems ([link](https://sre.google/sre-book/monitoring-distributed-systems/))


%% ── my notes ── %%
