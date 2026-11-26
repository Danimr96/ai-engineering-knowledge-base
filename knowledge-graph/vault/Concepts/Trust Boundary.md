---
id: "concept:trust-boundary"
type: concept
name: Trust Boundary
canonical: true
category: "Security & governance"
taught_in: 2
community: 14
tags:
  - concept/glossary
  - category/security-and-governance
  - community/14
source: ai-engineering-from-scratch/glossary/terms.md
---

# Trust Boundary

**Community:** [[Communities/14 Least Privilege · Prompt Injection · Sandbox|14 Least Privilege · Prompt Injection · Sandbox]]

**What it actually means:** An interface where data, instructions, identity, or authority crosses between components or principals that operate under different trust assumptions.

**Why it matters:** A boundary crossing is where the system must authenticate actors, validate data, constrain permissions, and decide which claims can influence action.

**In practice:** Draw boundaries around users, model context, retrieval sources, tools, networks, and data stores, then specify validation and authorization for every crossing.

**Common confusion:** A network boundary is only one kind of trust boundary. Untrusted document text entering a privileged agent context also crosses one.

**Category:** [[Categories/Security & governance|Security & governance]]

## Related concepts

- [[Concepts/Data Classification|Data Classification]]
- [[Concepts/Data Exfiltration|Data Exfiltration]]
- [[Concepts/Defense in Depth|Defense in Depth]]
- [[Concepts/Indirect Prompt Injection|Indirect Prompt Injection]]
- [[Concepts/Least Privilege|Least Privilege]]
- [[Concepts/Sandbox|Sandbox]]
- [[Concepts/Skill Discovery|Skill Discovery]]
- [[Concepts/Threat Model|Threat Model]]
- [[Concepts/Zero Trust|Zero Trust]]

## Taught in

- [[Lessons/13-26 Skill Permissions, Sandboxes, and Trust|13/26 Skill Permissions, Sandboxes, and Trust]] — An interface where data or authority crosses between different trust assumptions
- [[Lessons/19-82 Capstone 82 — Jailbreak Taxonomy|19/82 Capstone 82 — Jailbreak Taxonomy]]

## Sources

- Microsoft Learn: Trust Boundary, the Trust Zone Change Element ([link](https://learn.microsoft.com/en-us/training/modules/tm-create-a-threat-model-using-foundational-data-flow-diagram-elements/6-trust-boundary-the-trust-zone-change-element))
- OWASP Threat Modeling ([link](https://owasp.org/www-community/Threat_Modeling))


%% ── my notes ── %%
