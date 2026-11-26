---
id: "concept:postmortem"
type: concept
name: Postmortem
canonical: true
category: "Reliability & operations"
taught_in: 0
community: 46
tags:
  - concept/glossary
  - category/reliability-and-operations
  - community/46
source: ai-engineering-from-scratch/glossary/terms.md
---

# Postmortem

**Community:** [[Communities/46 Audit Log · Observability · Incident Response|46 Audit Log · Observability · Incident Response]]

**What it actually means:** A durable incident record that explains impact, detection, response, contributing conditions, recovery, and owned follow-up actions without assigning blame as a substitute for analysis.

**Why it matters:** A resolved outage still has value as evidence. Capturing system conditions and decisions turns one event into improvements that reduce recurrence and response time.

**In practice:** Build the timeline from traces and logs, distinguish triggering events from contributing conditions, assign dated actions, and review whether each action changed the relevant control.

**Common confusion:** A postmortem is not a meeting transcript or a search for one person's mistake. It should produce testable system improvements.

**Category:** [[Categories/Reliability & operations|Reliability & operations]]

## Related concepts

- [[Concepts/Audit Log|Audit Log]]
- [[Concepts/Incident Response|Incident Response]]
- [[Concepts/Observability|Observability]]
- [[Concepts/Regression Test|Regression Test]]

## Sources

- Google SRE: Postmortem Culture ([link](https://sre.google/sre-book/postmortem-culture/))


%% ── my notes ── %%
