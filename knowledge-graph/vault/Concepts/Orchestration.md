---
id: "concept:orchestration"
type: concept
name: Orchestration
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

# Orchestration

**Community:** [[Communities/17 Tool Contract · Agent · Function Calling|17 Tool Contract · Agent · Function Calling]]

**What it actually means:** The control logic that sequences, branches, delegates, retries, pauses, resumes, and terminates work across model and tool steps.

**Why it matters:** Reliable agent behavior depends on explicit workflow decisions outside the model, especially when tasks have dependencies or consequential side effects.

**In practice:** Encode stable steps as a workflow or state machine, expose bounded decisions to the model, and persist transitions before external writes.

**Common confusion:** Orchestration is not synonymous with autonomy or multi-agent systems; one agent can be orchestrated through a deterministic workflow.

**Category:** [[Categories/Agents & tools|Agents & tools]]

## Related concepts

- [[Concepts/Agent Harness|Agent Harness]]
- [[Concepts/Delegation|Delegation]]
- [[Concepts/Durable Execution|Durable Execution]]
- [[Concepts/Planning|Planning]]

## Taught in

- [[Lessons/11-17 Agent Framework Tradeoffs — Graph, Role, and Actor Orchestration|11/17 Agent Framework Tradeoffs — Graph, Role, and Actor Orchestration]] — The layer that decides which node/role/agent runs next.

## Sources

- [[Resources/Building Effective Agents|Building Effective Agents]] ([link](https://www.anthropic.com/research/building-effective-agents))


%% ── my notes ── %%
