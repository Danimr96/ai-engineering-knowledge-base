---
id: "concept:agent-memory"
type: concept
name: Agent Memory
canonical: true
category: "Agents & tools"
taught_in: 0
tags:
  - concept/glossary
  - category/agents-and-tools
source: ai-engineering-from-scratch/glossary/terms.md
---

# Agent Memory

**What it actually means:** Information stored outside the model and selected for use in later agent steps, such as prior decisions, user preferences, task episodes, or verified facts.

**Why it matters:** It gives an agent continuity beyond one context window without forcing every past event into every prompt.

**In practice:** Store a compact task outcome with provenance, retrieve it only when relevant, and let the user inspect or correct durable personal information.

**Common confusion:** Agent memory is not the same as agent state. State tracks the current run; memory preserves selected information for possible future runs.

**Category:** [[Categories/Agents & tools|Agents & tools]]

## Related concepts

- [[Concepts/Agent State|Agent State]]
- [[Concepts/Checkpoint|Checkpoint]]
- [[Concepts/Context Engineering|Context Engineering]]
- [[Concepts/Semantic Cache|Semantic Cache]]

## Sources

- [[Resources/Generative Agents|Generative Agents]] ([link](https://arxiv.org/abs/2304.03442))


%% ── my notes ── %%
