---
id: "concept:error-budget"
type: concept
name: Error Budget
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

# Error Budget

**Community:** [[Communities/80 Availability · Error Budget · Service Level Indicator (SLI)|80 Availability · Error Budget · Service Level Indicator (SLI)]]

**What it actually means:** The amount of unsuccessful service allowed by a service-level objective over its measurement window before the objective is exhausted.

**Why it matters:** It gives reliability and product work a shared decision boundary: teams can spend remaining budget on change while slowing risk when user-visible failure consumes it.

**In practice:** Derive the budget from the SLO, track burn by cause and user segment, define release actions before exhaustion, and avoid resetting the accounting after an incident.

**Common confusion:** An error budget is not a quota for causing incidents. It is an operating policy derived from a user-facing reliability target.

**Category:** [[Categories/Reliability & operations|Reliability & operations]]

## Related concepts

- [[Concepts/Availability|Availability]]
- [[Concepts/Incident Response|Incident Response]]
- [[Concepts/Retry Budget|Retry Budget]]
- [[Concepts/Service Level Indicator (SLI)|Service Level Indicator (SLI)]]
- [[Concepts/Service Level Objective (SLO)|Service Level Objective (SLO)]]

## Sources

- Google SRE Workbook: Error Budget Policy ([link](https://sre.google/workbook/error-budget-policy/))


%% ── my notes ── %%
