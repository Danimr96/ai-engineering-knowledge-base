---
id: "concept:graceful-degradation"
type: concept
name: Graceful Degradation
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

# Graceful Degradation

**Community:** [[Communities/16 Backpressure · Rate Limit · Admission Control|16 Backpressure · Rate Limit · Admission Control]]

**What it actually means:** Preserving a bounded core service when capacity or dependencies are impaired by reducing optional quality, features, freshness, or workload instead of failing every request.

**Why it matters:** AI systems often depend on several slow or fallible components, so an explicit reduced mode can protect essential user outcomes during partial failure.

**In practice:** Predefine which capabilities may be disabled, keep the reduced mode visible to operators, protect safety checks, test the fallback under dependency failure, and restore full service deliberately. Tell users when correctness, safety, freshness, or a promised contract materially changes.

**Common confusion:** Graceful degradation is not silently returning a worse answer as if nothing happened. Operators always need visibility; users need disclosure when the reduced mode materially changes the result or service contract.

**Category:** [[Categories/Reliability & operations|Reliability & operations]]

## Related concepts

- [[Concepts/Availability|Availability]]
- [[Concepts/Circuit Breaker|Circuit Breaker]]
- [[Concepts/Load Shedding|Load Shedding]]
- [[Concepts/Model Router|Model Router]]
- [[Concepts/Readiness Probe|Readiness Probe]]

## Taught in

- [[Lessons/11-13 Building a Production LLM Application|11/13 Building a Production LLM Application]] — When a secondary component fails (cache, RAG, guardrails), the system continues with reduced functionality rather than crashing

## Sources

- Google SRE: Addressing Cascading Failures ([link](https://sre.google/sre-book/addressing-cascading-failures/))


%% ── my notes ── %%
