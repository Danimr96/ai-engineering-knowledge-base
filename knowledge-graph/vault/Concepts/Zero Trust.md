---
id: "concept:zero-trust"
type: concept
name: Zero Trust
canonical: true
category: "Security & governance"
taught_in: 1
community: 14
tags:
  - concept/glossary
  - category/security-and-governance
  - community/14
source: ai-engineering-from-scratch/glossary/terms.md
---

# Zero Trust

**Community:** [[Communities/14 Least Privilege · Prompt Injection · Sandbox|14 Least Privilege · Prompt Injection · Sandbox]]

**What it actually means:** A security model that grants no implicit trust from network location or asset ownership and instead evaluates each access request against identity, device, resource, policy, and current context.

**Why it matters:** AI tools and agents span local files, cloud services, models, and external content, so a trusted internal network is too broad a basis for authority.

**In practice:** Authenticate every actor and workload, authorize each resource action, issue short-lived credentials, segment access, and continuously record and reevaluate policy-relevant signals.

**Common confusion:** Zero trust does not mean trusting nothing or blocking all automation. It means making trust decisions explicit, scoped, and continuously verifiable.

**Category:** [[Categories/Security & governance|Security & governance]]

## Related concepts

- [[Concepts/Approval Gate|Approval Gate]]
- [[Concepts/Audit Log|Audit Log]]
- [[Concepts/Least Privilege|Least Privilege]]
- [[Concepts/Trust Boundary|Trust Boundary]]

## Taught in

- [[Lessons/17-25 Security — Secrets, API Key Rotation, Audit Logs, Guardrails|17/25 Security — Secrets, API Key Rotation, Audit Logs, Guardrails]]

## Sources

- NIST SP 800-207 ([link](https://csrc.nist.gov/pubs/sp/800/207/final))


%% ── my notes ── %%
