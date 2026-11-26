---
id: "concept:service-level-objective-slo"
type: concept
name: Service Level Objective (SLO)
canonical: true
category: "Reliability & operations"
taught_in: 1
community: 80
tags:
  - concept/glossary
  - category/reliability-and-operations
  - community/80
source: ai-engineering-from-scratch/glossary/terms.md
---

# Service Level Objective (SLO)

**Community:** [[Communities/80 Availability · Error Budget · Service Level Indicator (SLI)|80 Availability · Error Budget · Service Level Indicator (SLI)]]

**What it actually means:** A target range or threshold for a service-level indicator over a stated population and measurement window.

**Why it matters:** It translates an expected user outcome into an operating boundary for monitoring, capacity, release risk, and incident decisions.

**In practice:** Choose an indicator users care about, set the target from product needs rather than current performance, define the window and exclusions, and attach an error-budget policy.

**Common confusion:** An SLO is an internal reliability objective. A contractual service-level agreement can include remedies and may use different definitions.

**Category:** [[Categories/Reliability & operations|Reliability & operations]]

## Related concepts

- [[Concepts/Availability|Availability]]
- [[Concepts/Deadline Propagation|Deadline Propagation]]
- [[Concepts/Error Budget|Error Budget]]
- [[Concepts/Goodput|Goodput]]
- [[Concepts/Service Level Indicator (SLI)|Service Level Indicator (SLI)]]

## Taught in

- [[Lessons/17-08 Inference Metrics — TTFT, TPOT, ITL, Goodput, P99|17/08 Inference Metrics — TTFT, TPOT, ITL, Goodput, P99]]

## Sources

- Google SRE: Service Level Objectives ([link](https://sre.google/sre-book/service-level-objectives/))


%% ── my notes ── %%
