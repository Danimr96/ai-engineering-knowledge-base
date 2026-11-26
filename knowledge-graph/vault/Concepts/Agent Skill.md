---
id: "concept:agent-skill"
type: concept
name: Agent Skill
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

# Agent Skill

**Community:** [[Communities/39 Skill Catalog · Agent Skill · Progressive Disclosure|39 Skill Catalog · Agent Skill · Progressive Disclosure]]

**What it actually means:** A discoverable directory of procedural instructions whose entry point is `SKILL.md`, with optional references, scripts, and assets that a compatible runtime can load in stages.

**Why it matters:** It packages reusable task knowledge separately from one conversation while keeping deeper context and deterministic helpers available on demand.

**In practice:** Publish a compact name and routing description, load the workflow only after activation, and read branch-specific references when the task reaches them.

**Common confusion:** Activating a skill supplies context. It does not expose a tool, grant permission, create a sandbox, or prove that the resulting work is correct.

**Category:** [[Categories/Agents & tools|Agents & tools]]

## Related concepts

- [[Concepts/MCP (Model Context Protocol)|MCP (Model Context Protocol)]]
- [[Concepts/Progressive Disclosure|Progressive Disclosure]]
- [[Concepts/Skill Bundle|Skill Bundle]]
- [[Concepts/Skill Catalog|Skill Catalog]]
- [[Concepts/Skill Invocation|Skill Invocation]]

## Taught in

- [[Lessons/13-22 Agent Skills- Portable Contract and Runtime Boundary|13/22 Agent Skills: Portable Contract and Runtime Boundary]] — A discoverable directory of procedural instructions and optional resources

## Sources

- [[Resources/Agent Skills specification|Agent Skills specification]] ([link](https://agentskills.io/specification))


%% ── my notes ── %%
