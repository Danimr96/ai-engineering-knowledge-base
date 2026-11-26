---
id: "concept:readiness-probe"
type: concept
name: Readiness Probe
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

# Readiness Probe

**Community:** [[Communities/16 Backpressure · Rate Limit · Admission Control|16 Backpressure · Rate Limit · Admission Control]]

**What it actually means:** A diagnostic that tells the traffic-routing layer whether a service instance is currently able to accept requests.

**Why it matters:** A process can be alive while its model is unloaded, dependencies are unavailable, or warmup is incomplete, so sending traffic too early creates avoidable failures.

**In practice:** Check the minimum dependencies required to serve, fail readiness during startup and draining, keep the probe inexpensive, and do not restart the process solely because readiness is false.

**Common confusion:** Readiness controls traffic eligibility. Liveness decides whether the process should be restarted, and neither proves that every model response will be correct.

**Category:** [[Categories/Reliability & operations|Reliability & operations]]

## Related concepts

- [[Concepts/Autoscaling|Autoscaling]]
- [[Concepts/Availability|Availability]]
- [[Concepts/Graceful Degradation|Graceful Degradation]]
- [[Concepts/Model Serving|Model Serving]]

## Taught in

- [[Lessons/11-13 Building a Production LLM Application|11/13 Building a Production LLM Application]]

## Sources

- Kubernetes Liveness, Readiness, and Startup Probes ([link](https://kubernetes.io/docs/concepts/configuration/liveness-readiness-startup-probes/))


%% ── my notes ── %%
