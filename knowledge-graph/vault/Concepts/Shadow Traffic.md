---
id: "concept:shadow-traffic"
type: concept
name: Shadow Traffic
canonical: true
category: "Reliability & operations"
taught_in: 1
community: 10
tags:
  - concept/glossary
  - category/reliability-and-operations
  - community/10
source: ai-engineering-from-scratch/glossary/terms.md
---

# Shadow Traffic

**Community:** [[Communities/10 Trace · Shadow Traffic · requestState|10 Trace · Shadow Traffic · requestState]]

**What it actually means:** A copy of live request traffic sent to a candidate system for observation while the candidate response remains outside the primary user response path. Because the copied request still executes, its side effects must be isolated.

**Why it matters:** It exposes the candidate to real input shapes and load while limiting user impact, which can reveal failures absent from synthetic tests.

**In practice:** Remove or tokenize sensitive fields, route tools and dependencies to sandboxed or no-op targets, block writes at capability boundaries, preserve request correlation, and prevent shadow load from competing with user traffic.

**Common confusion:** Keeping a candidate response off the primary path does not make execution side-effect-free. A canary release differs because it serves real users from the candidate for a controlled share of traffic.

**Category:** [[Categories/Reliability & operations|Reliability & operations]]

## Related concepts

- [[Concepts/Canary Release|Canary Release]]
- [[Concepts/Evaluation (Eval)|Evaluation (Eval)]]
- [[Concepts/Model Serving|Model Serving]]
- [[Concepts/Trace|Trace]]

## Taught in

- [[Lessons/17-20 Shadow Traffic, Canary Rollout, and Progressive Deployment for LLMs|17/20 Shadow Traffic, Canary Rollout, and Progressive Deployment for LLMs]]

## Sources

- Istio Traffic Mirroring ([link](https://istio.io/latest/docs/tasks/traffic-management/mirroring/))


%% ── my notes ── %%
