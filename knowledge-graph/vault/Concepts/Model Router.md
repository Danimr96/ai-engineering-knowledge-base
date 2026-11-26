---
id: "concept:model-router"
type: concept
name: Model Router
canonical: true
category: AI-native development
taught_in: 0
community: 16
tags:
  - concept/glossary
  - category/ai-native-development
  - community/16
source: ai-engineering-from-scratch/glossary/terms.md
---

# Model Router

**Community:** [[Communities/16 Backpressure · Rate Limit · Admission Control|16 Backpressure · Rate Limit · Admission Control]]

**What it actually means:** A component that selects a model or provider for a request using requirements such as capability, latency, cost, context size, policy, and current availability.

**Why it matters:** Different tasks and failure conditions justify different models, and routing can improve outcome quality without sending every request to the largest option.

**In practice:** Send low-risk extraction to a fast model, complex code review to a stronger model, and fail over only to providers that satisfy the same data policy.

**Common confusion:** Routing is a policy decision. Random load balancing only distributes traffic.

**Category:** [[Categories/AI-native development|AI-native development]]

## Related concepts

- [[Concepts/Circuit Breaker|Circuit Breaker]]
- [[Concepts/Cost per Successful Task|Cost per Successful Task]]
- [[Concepts/Evaluation (Eval)|Evaluation (Eval)]]
- [[Concepts/Graceful Degradation|Graceful Degradation]]
- [[Concepts/Model Serving|Model Serving]]
- [[Concepts/MoE (Mixture of Experts)|MoE (Mixture of Experts)]]
- [[Concepts/Rate Limit|Rate Limit]]


%% ── my notes ── %%
