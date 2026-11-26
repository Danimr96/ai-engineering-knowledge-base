---
id: "concept:availability"
type: concept
name: Availability
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

# Availability

**Community:** [[Communities/80 Availability · Error Budget · Service Level Indicator (SLI)|80 Availability · Error Budget · Service Level Indicator (SLI)]]

**What it actually means:** The proportion of eligible service interactions or time windows in which users can obtain the defined acceptable service under a stated measurement boundary.

**Why it matters:** A service can be running while users still cannot complete useful requests, so availability must be tied to user-visible success rather than process uptime alone.

**In practice:** Define eligible events and acceptable outcomes, exclude only documented cases, calculate the indicator over a fixed window, and investigate both total failures and prolonged partial degradation.

**Common confusion:** Availability is one reliability outcome. It does not describe latency, correctness, safety, or the experience of every user segment.

**Category:** [[Categories/Reliability & operations|Reliability & operations]]

## Related concepts

- [[Concepts/Error Budget|Error Budget]]
- [[Concepts/Graceful Degradation|Graceful Degradation]]
- [[Concepts/Incident Response|Incident Response]]
- [[Concepts/Readiness Probe|Readiness Probe]]
- [[Concepts/Service Level Indicator (SLI)|Service Level Indicator (SLI)]]
- [[Concepts/Service Level Objective (SLO)|Service Level Objective (SLO)]]

## Sources

- Google SRE: Service Level Objectives ([link](https://sre.google/sre-book/service-level-objectives/))


%% ── my notes ── %%
