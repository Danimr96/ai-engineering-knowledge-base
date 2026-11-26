---
id: "concept:system-prompt"
type: concept
name: System Prompt
canonical: true
category: "Prompting & context"
taught_in: 1
community: 14
tags:
  - concept/glossary
  - category/prompting-and-context
  - community/14
source: ai-engineering-from-scratch/glossary/terms.md
---

# System Prompt

**Community:** [[Communities/14 Least Privilege · Prompt Injection · Sandbox|14 Least Privilege · Prompt Injection · Sandbox]]

> *What people say:* Developer-controlled instructions for a model interaction.

**What it actually means:** A provider-defined instruction message or configuration supplied by the application to establish behavior and constraints within that provider's instruction hierarchy.

**Why it matters:** System instructions can guide behavior, but they are not guaranteed to remain secret and should not be treated as a security boundary.

**Common confusion:** Priority rules, message roles, persistence, and visibility differ across APIs. Check the current provider contract.

**Category:** [[Categories/Prompting & context|Prompting & context]]

## Related concepts

- [[Concepts/Context Engineering|Context Engineering]]
- [[Concepts/Guardrails|Guardrails]]
- [[Concepts/Instruction Hierarchy|Instruction Hierarchy]]
- [[Concepts/Prompt Engineering|Prompt Engineering]]
- [[Concepts/Prompt Injection|Prompt Injection]]

## Taught in

- [[Lessons/14-33 Agent Instructions as Executable Constraints|14/33 Agent Instructions as Executable Constraints]]


%% ── my notes ── %%
