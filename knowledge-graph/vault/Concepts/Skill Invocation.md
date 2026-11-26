---
id: "concept:skill-invocation"
type: concept
name: Skill Invocation
canonical: true
category: "Agents & tools"
taught_in: 1
community: 39
tags:
  - concept/glossary
  - category/agents-and-tools
  - community/39
source: ai-engineering-from-scratch/glossary/terms.md
---

# Skill Invocation

**Community:** [[Communities/39 Skill Catalog · Agent Skill · Progressive Disclosure|39 Skill Catalog · Agent Skill · Progressive Disclosure]]

**What it actually means:** The runtime-mediated process in which an eligible human, model, application, or other skill selects a skill and causes its instructions to enter the working context.

**Why it matters:** Explicit user access, implicit model routing, activation, argument binding, tool permission, and execution are separate decisions with different failure modes.

**In practice:** Define actor policy, evaluate descriptions with positive and near-miss requests, record the selected package identity, and keep host-specific invocation fields in tested adapters.

**Common confusion:** Invocation activates instructions. It does not automatically execute a command or bypass approval and sandbox policy.

**Category:** [[Categories/Agents & tools|Agents & tools]]

## Related concepts

- [[Concepts/Agent Skill|Agent Skill]]
- [[Concepts/Approval Gate|Approval Gate]]
- [[Concepts/Sandbox|Sandbox]]
- [[Concepts/Skill Catalog|Skill Catalog]]

## Taught in

- [[Lessons/13-25 Skill Invocation and Routing|13/25 Skill Invocation and Routing]]

## Sources

- [[Resources/Evaluating Agent Skills|Evaluating Agent Skills]] ([link](https://agentskills.io/skill-creation/evaluating-skills))


%% ── my notes ── %%
