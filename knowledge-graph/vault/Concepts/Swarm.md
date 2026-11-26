---
id: "concept:swarm"
type: concept
name: Swarm
canonical: true
category: "Agents & tools"
taught_in: 3
community: 7
tags:
  - concept/glossary
  - category/agents-and-tools
  - community/07
source: ai-engineering-from-scratch/glossary/terms.md
---

# Swarm

**Community:** [[Communities/07 Swarm · Evaluator-Optimizer · Debate|07 Swarm · Evaluator-Optimizer · Debate]]

> *What people say:* Many agents collaborating without one fixed controller.

**What it actually means:** A loosely coordinated multi-agent pattern in which local agent decisions and message exchange produce system-level behavior. The term is used inconsistently, so the actual topology, state ownership, and termination rules must be specified.

**Common confusion:** Multiple named agents do not guarantee useful specialization or emergent coordination.

**Category:** [[Categories/Agents & tools|Agents & tools]]

## Related concepts

- [[Concepts/Agent|Agent]]
- [[Concepts/Agent State|Agent State]]
- [[Concepts/Handoff|Handoff]]
- [[Concepts/Reviewer Agent|Reviewer Agent]]

## Taught in

- [[Lessons/14-13 Stateful Graph Orchestration — Durable Execution and Checkpoints|14/13 Stateful Graph Orchestration — Durable Execution and Checkpoints]] — Agents hand off via shared tools; no central router
- [[Lessons/14-28 Orchestration Patterns- Supervisor, Swarm, Hierarchical|14/28 Orchestration Patterns: Supervisor, Swarm, Hierarchical]] — Direct handoffs via shared tools; no central router
- [[Lessons/16-01 Why Multi-Agent|16/01 Why Multi-Agent?]] — A set of peer agents with shared state and no fixed leader. Behavior emerges from local interactions.


%% ── my notes ── %%
