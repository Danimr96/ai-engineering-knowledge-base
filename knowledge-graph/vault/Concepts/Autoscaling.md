---
id: "concept:autoscaling"
type: concept
name: Autoscaling
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

# Autoscaling

**Community:** [[Communities/16 Backpressure · Rate Limit · Admission Control|16 Backpressure · Rate Limit · Admission Control]]

**What it actually means:** A control loop that changes the number or capacity of serving workers from observed demand, resource use, or application metrics within configured bounds.

**Why it matters:** AI workloads can change faster than manual provisioning, but scaling decisions must account for model-load time, accelerator availability, queueing, and request cost.

**In practice:** Scale from a demand signal tied to useful work, set minimum warm capacity, bound scale-down churn, and verify that new replicas pass readiness checks before receiving traffic.

**Common confusion:** Autoscaling adds or removes capacity. It does not make an overloaded dependency faster or guarantee that enough hardware can be acquired in time.

**Category:** [[Categories/Infrastructure & serving|Infrastructure & serving]]

## Related concepts

- [[Concepts/Backpressure|Backpressure]]
- [[Concepts/Model Serving|Model Serving]]
- [[Concepts/Readiness Probe|Readiness Probe]]
- [[Concepts/Saturation|Saturation]]

## Taught in

- [[Lessons/17-03 GPU Autoscaling on Kubernetes — Karpenter, KAI Scheduler, Gang Scheduling|17/03 GPU Autoscaling on Kubernetes — Karpenter, KAI Scheduler, Gang Scheduling]]

## Sources

- Kubernetes Horizontal Pod Autoscaling ([link](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/))


%% ── my notes ── %%
