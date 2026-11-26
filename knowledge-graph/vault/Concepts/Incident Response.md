---
id: "concept:incident-response"
type: concept
name: Incident Response
canonical: true
category: "Reliability & operations"
taught_in: 1
community: 46
tags:
  - concept/glossary
  - category/reliability-and-operations
  - community/46
source: ai-engineering-from-scratch/glossary/terms.md
---

# Incident Response

**Community:** [[Communities/46 Audit Log · Observability · Incident Response|46 Audit Log · Observability · Incident Response]]

**What it actually means:** The coordinated process for detecting, analyzing, containing, recovering from, communicating, and learning from an event that threatens service, data, safety, or security.

**Why it matters:** During an incident, clear roles and evidence matter more than improvised heroics, especially when model behavior and distributed dependencies obscure the failing boundary.

**In practice:** Define severity and command roles, preserve traces and audit records, stop harmful actions, communicate impact, verify recovery, and track corrective work to completion.

**Common confusion:** Incident response manages the event and its consequences. Root-cause analysis and long-term prevention continue after immediate service is restored.

**Category:** [[Categories/Reliability & operations|Reliability & operations]]

## Related concepts

- [[Concepts/Audit Log|Audit Log]]
- [[Concepts/Availability|Availability]]
- [[Concepts/Error Budget|Error Budget]]
- [[Concepts/Observability|Observability]]
- [[Concepts/Postmortem|Postmortem]]

## Taught in

- [[Lessons/17-23 SRE for AI — Multi-Agent Incident Response, Runbooks, Predictive Detection|17/23 SRE for AI — Multi-Agent Incident Response, Runbooks, Predictive Detection]]

## Sources

- NIST SP 800-61 Rev. 3 ([link](https://csrc.nist.gov/pubs/sp/800/61/r3/final))
- Google SRE: Managing Incidents ([link](https://sre.google/sre-book/managing-incidents/))


%% ── my notes ── %%
