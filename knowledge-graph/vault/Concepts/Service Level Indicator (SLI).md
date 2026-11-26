---
id: "concept:service-level-indicator-sli"
type: concept
name: Service Level Indicator (SLI)
canonical: true
category: "Reliability & operations"
taught_in: 0
community: 80
tags:
  - concept/glossary
  - category/reliability-and-operations
  - community/80
source: ai-engineering-from-scratch/glossary/terms.md
---

# Service Level Indicator (SLI)

**Community:** [[Communities/80 Availability · Error Budget · Service Level Indicator (SLI)|80 Availability · Error Budget · Service Level Indicator (SLI)]]

**What it actually means:** A quantitative measure of service behavior at a defined user-relevant boundary, such as successful request ratio or latency below a threshold.

**Why it matters:** Reliability discussions become actionable only when the observed behavior, eligible events, and measurement point are explicit.

**In practice:** Define numerator, denominator, exclusions, data source, and aggregation window, then validate that the indicator tracks an outcome users actually experience.

**Common confusion:** An SLI is the measurement. An SLO is the target applied to that measurement over a defined period.

**Category:** [[Categories/Reliability & operations|Reliability & operations]]

## Related concepts

- [[Concepts/Availability|Availability]]
- [[Concepts/Error Budget|Error Budget]]
- [[Concepts/Observability|Observability]]
- [[Concepts/Service Level Objective (SLO)|Service Level Objective (SLO)]]
- [[Concepts/Tail Latency|Tail Latency]]

## Sources

- Google SRE: Service Level Objectives ([link](https://sre.google/sre-book/service-level-objectives/))


%% ── my notes ── %%
