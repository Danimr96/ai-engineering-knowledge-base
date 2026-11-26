---
id: "concept:model-serving"
type: concept
name: Model Serving
canonical: true
category: "Infrastructure & serving"
taught_in: 1
community: 16
tags:
  - concept/glossary
  - category/infrastructure-and-serving
  - community/16
source: ai-engineering-from-scratch/glossary/terms.md
---

# Model Serving

**Community:** [[Communities/16 Backpressure · Rate Limit · Admission Control|16 Backpressure · Rate Limit · Admission Control]]

**What it actually means:** The runtime and API layer that loads versioned model artifacts, accepts inference requests, schedules execution, manages resources, and returns results under an operational contract.

**Why it matters:** A capable model can still produce an unreliable product when queueing, batching, placement, versioning, cancellation, and response boundaries are not engineered explicitly.

**In practice:** Pin model and tokenizer versions, validate request limits, expose readiness and latency signals, control concurrency, and test rollback before routing production traffic.

**Common confusion:** Model serving is broader than calling inference once and narrower than the complete application, which may also include retrieval, tools, policy, and user state.

**Category:** [[Categories/Infrastructure & serving|Infrastructure & serving]]

## Related concepts

- [[Concepts/Autoscaling|Autoscaling]]
- [[Concepts/Disaggregated Serving|Disaggregated Serving]]
- [[Concepts/Expert Parallelism|Expert Parallelism]]
- [[Concepts/Inference|Inference]]
- [[Concepts/Model Router|Model Router]]
- [[Concepts/Observability|Observability]]
- [[Concepts/Paged KV Cache|Paged KV Cache]]
- [[Concepts/Pipeline Parallelism|Pipeline Parallelism]]
- [[Concepts/Readiness Probe|Readiness Probe]]
- [[Concepts/Shadow Traffic|Shadow Traffic]]

## Taught in

- [[Lessons/17-28 Self-Hosted Serving Selection — Matching Engine to Hardware and Scale|17/28 Self-Hosted Serving Selection — Matching Engine to Hardware and Scale]]

## Sources

- Clipper ([link](https://arxiv.org/abs/1612.03079))


%% ── my notes ── %%
