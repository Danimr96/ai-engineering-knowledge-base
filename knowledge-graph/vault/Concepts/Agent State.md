---
id: "concept:agent-state"
type: concept
name: Agent State
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

# Agent State

**Community:** [[Communities/17 Tool Contract · Agent · Function Calling|17 Tool Contract · Agent · Function Calling]]

**What it actually means:** The explicit data an agent carries across steps, such as the current objective, completed actions, tool results, open questions, budgets, approvals, and artifact references.

**Why it matters:** Explicit state makes long tasks resumable, inspectable, and less dependent on the model reconstructing progress from a transcript.

**In practice:** Store the selected issue, changed files, latest test result, and remaining checks in a typed object that is updated after each action.

**Common confusion:** State is not the same as conversation history. A transcript is evidence; state is the compact operational record used to decide what happens next.

**Category:** [[Categories/Agents & tools|Agents & tools]]

## Related concepts

- [[Concepts/Agent|Agent]]
- [[Concepts/Agent Harness|Agent Harness]]
- [[Concepts/Agent Memory|Agent Memory]]
- [[Concepts/Checkpoint|Checkpoint]]
- [[Concepts/Context Engineering|Context Engineering]]
- [[Concepts/Context Window|Context Window]]
- [[Concepts/Durable Execution|Durable Execution]]
- [[Concepts/Handoff|Handoff]]
- [[Concepts/Observability|Observability]]
- [[Concepts/Planning|Planning]]
- [[Concepts/Swarm|Swarm]]
- [[Concepts/Trace|Trace]]

## Taught in

- [[Lessons/14-34 Repo Memory and Durable State|14/34 Repo Memory and Durable State]]


%% ── my notes ── %%
