---
id: "concept:agent-harness"
type: concept
name: Agent Harness
canonical: true
category: "Agents & tools"
taught_in: 1
community: 17
tags:
  - concept/glossary
  - category/agents-and-tools
  - community/17
source: ai-engineering-from-scratch/glossary/terms.md
---

# Agent Harness

**Community:** [[Communities/17 Tool Contract · Agent · Function Calling|17 Tool Contract · Agent · Function Calling]]

**What it actually means:** The runtime around a model that assembles context, exposes tools, manages state, enforces limits, records traces, and decides when the agent should continue, retry, ask, or stop.

**Why it matters:** Two systems using the same model can perform very differently because their harnesses provide different context, tools, feedback, and safety boundaries.

**In practice:** Your harness can limit an agent to five tool calls, persist a checkpoint after each accepted patch, and require a passing test command before completion.

**Common confusion:** A harness is broader than a prompt template and narrower than the complete product.

**Category:** [[Categories/Agents & tools|Agents & tools]]

## Related concepts

- [[Concepts/Agent|Agent]]
- [[Concepts/Agent State|Agent State]]
- [[Concepts/Coding Agent|Coding Agent]]
- [[Concepts/LLM (Large Language Model)|LLM (Large Language Model)]]
- [[Concepts/Orchestration|Orchestration]]
- [[Concepts/Sandbox|Sandbox]]
- [[Concepts/Termination Condition|Termination Condition]]
- [[Concepts/Tool Contract|Tool Contract]]
- [[Concepts/Verification Gate|Verification Gate]]

## Taught in

- [[Lessons/14-32 The Minimal Agent Workbench|14/32 The Minimal Agent Workbench]]


%% ── my notes ── %%
