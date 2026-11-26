---
id: "concept:reducer"
type: concept
name: Reducer
canonical: false
taught_in: 2
community: 7
tags:
  - concept/lesson-term
  - community/07
source: ai-engineering-from-scratch/phases/11-llm-engineering/16-langgraph-state-machines/docs/en.md
---

# Reducer

**Community:** [[Communities/07 Swarm · Evaluator-Optimizer · Debate|07 Swarm · Evaluator-Optimizer · Debate]]

> *What people say:* "How the field merges"

**What it actually means:** A function (old, new) -> merged applied when a node returns an update for that field; default is overwrite, add_messages appends.

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/11-16 Agent State Machines — Graphs, Nodes, Checkpoints|11/16 Agent State Machines — Graphs, Nodes, Checkpoints]]
- [[Lessons/14-13 Stateful Graph Orchestration — Durable Execution and Checkpoints|14/13 Stateful Graph Orchestration — Durable Execution and Checkpoints]] — Function that combines current state with a node's update


%% ── my notes ── %%
