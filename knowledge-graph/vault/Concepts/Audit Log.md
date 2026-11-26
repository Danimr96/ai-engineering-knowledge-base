---
id: "concept:audit-log"
type: concept
name: Audit Log
canonical: true
category: "Security & governance"
taught_in: 2
community: 46
tags:
  - concept/glossary
  - category/security-and-governance
  - community/46
source: ai-engineering-from-scratch/glossary/terms.md
---

# Audit Log

**Community:** [[Communities/46 Audit Log · Observability · Incident Response|46 Audit Log · Observability · Incident Response]]

**What it actually means:** A durable, access-controlled record of security- or accountability-relevant events, including who or what acted, what changed, when it happened, and the resulting status.

**Why it matters:** Consequential agent actions need evidence that supports investigation, policy review, and responsibility beyond performance debugging.

**In practice:** Record tool authorization, approval decisions, external writes, policy versions, and artifact identifiers while redacting secrets and restricting log access.

**Common confusion:** A trace helps diagnose one execution path. An audit log preserves events required for accountability across executions and over time.

**Category:** [[Categories/Security & governance|Security & governance]]

## Related concepts

- [[Concepts/Approval Gate|Approval Gate]]
- [[Concepts/Content Provenance|Content Provenance]]
- [[Concepts/Data Classification|Data Classification]]
- [[Concepts/Data Exfiltration|Data Exfiltration]]
- [[Concepts/Data Lineage|Data Lineage]]
- [[Concepts/Incident Response|Incident Response]]
- [[Concepts/Observability|Observability]]
- [[Concepts/Postmortem|Postmortem]]
- [[Concepts/Provenance Attestation|Provenance Attestation]]
- [[Concepts/Purpose Limitation|Purpose Limitation]]
- [[Concepts/Separation of Duties|Separation of Duties]]
- [[Concepts/Software Bill of Materials (SBOM)|Software Bill of Materials (SBOM)]]
- [[Concepts/Trace|Trace]]
- [[Concepts/Zero Trust|Zero Trust]]

## Taught in

- [[Lessons/17-25 Security — Secrets, API Key Rotation, Audit Logs, Guardrails|17/25 Security — Secrets, API Key Rotation, Audit Logs, Guardrails]] — Append-only record for compliance
- [[Lessons/19-06 Capstone 06 — DevOps Troubleshooting Agent for Kubernetes|19/06 Capstone 06 — DevOps Troubleshooting Agent for Kubernetes]] — Append-only record of every candidate command, whether it ran, who approved

## Sources

- NIST SP 800-92 ([link](https://csrc.nist.gov/pubs/sp/800/92/final))


%% ── my notes ── %%
