---
id: "concept:least-privilege"
type: concept
name: Least Privilege
canonical: true
category: "Evaluation & safety"
taught_in: 0
community: 14
tags:
  - concept/glossary
  - category/evaluation-and-safety
  - community/14
source: ai-engineering-from-scratch/glossary/terms.md
---

# Least Privilege

**Community:** [[Communities/14 Least Privilege · Prompt Injection · Sandbox|14 Least Privilege · Prompt Injection · Sandbox]]

**What it actually means:** Giving a model, agent, tool, or user only the permissions required for the current task, for only as long as those permissions are needed.

**Why it matters:** Models can make mistakes or follow malicious instructions. Narrow permissions reduce the damage any one failure can cause.

**In practice:** Give a documentation agent read access to source files and write access to one branch, but no production credentials or merge permission.

**Common confusion:** Authentication proves identity. Least privilege limits what that identity can do.

**Category:** [[Categories/Evaluation & safety|Evaluation & safety]]

## Related concepts

- [[Concepts/Approval Gate|Approval Gate]]
- [[Concepts/Data Classification|Data Classification]]
- [[Concepts/Data Exfiltration|Data Exfiltration]]
- [[Concepts/Data Minimization|Data Minimization]]
- [[Concepts/Defense in Depth|Defense in Depth]]
- [[Concepts/Guardrails|Guardrails]]
- [[Concepts/Instruction Hierarchy|Instruction Hierarchy]]
- [[Concepts/MCP (Model Context Protocol)|MCP (Model Context Protocol)]]
- [[Concepts/Prompt Injection|Prompt Injection]]
- [[Concepts/Sandbox|Sandbox]]
- [[Concepts/Separation of Duties|Separation of Duties]]
- [[Concepts/Threat Model|Threat Model]]
- [[Concepts/Tool Contract|Tool Contract]]
- [[Concepts/Trust Boundary|Trust Boundary]]
- [[Concepts/Zero Trust|Zero Trust]]


%% ── my notes ── %%
