---
id: "concept:approval-gate"
type: concept
name: Approval Gate
canonical: true
category: "Agents & tools"
taught_in: 2
community: 14
tags:
  - concept/glossary
  - category/agents-and-tools
  - community/14
source: ai-engineering-from-scratch/glossary/terms.md
---

# Approval Gate

**Community:** [[Communities/14 Least Privilege · Prompt Injection · Sandbox|14 Least Privilege · Prompt Injection · Sandbox]]

**What it actually means:** A control point that blocks a consequential action until an authorized person or policy grants permission.

**Why it matters:** It limits the blast radius of uncertain model decisions while preserving automation for reversible work.

**In practice:** Let an agent draft a database migration and run it against a disposable database, but require an owner to approve any production execution.

**Common confusion:** An approval gate asks whether an action is authorized. A verification gate asks whether evidence shows the action is correct.

**Category:** [[Categories/Agents & tools|Agents & tools]]

## Related concepts

- [[Concepts/Audit Log|Audit Log]]
- [[Concepts/Compensating Action|Compensating Action]]
- [[Concepts/Durable Execution|Durable Execution]]
- [[Concepts/Guardrails|Guardrails]]
- [[Concepts/Human-in-the-Loop (HITL)|Human-in-the-Loop (HITL)]]
- [[Concepts/Least Privilege|Least Privilege]]
- [[Concepts/Prompt Injection|Prompt Injection]]
- [[Concepts/Sandbox|Sandbox]]
- [[Concepts/Separation of Duties|Separation of Duties]]
- [[Concepts/Skill Invocation|Skill Invocation]]
- [[Concepts/Verification Gate|Verification Gate]]
- [[Concepts/Zero Trust|Zero Trust]]

## Taught in

- [[Lessons/13-26 Skill Permissions, Sandboxes, and Trust|13/26 Skill Permissions, Sandboxes, and Trust]] — An authorized decision before a consequential action
- [[Lessons/14-38 Verification Gates|14/38 Verification Gates]]


%% ── my notes ── %%
