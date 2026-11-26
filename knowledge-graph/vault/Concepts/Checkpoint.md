---
id: "concept:checkpoint"
type: concept
name: Checkpoint
canonical: true
category: "Agents & tools"
taught_in: 6
community: 35
tags:
  - concept/glossary
  - category/agents-and-tools
  - community/35
source: ai-engineering-from-scratch/glossary/terms.md
---

# Checkpoint

**Community:** [[Communities/35 Checkpoint · Durable Execution · Idempotency|35 Checkpoint · Durable Execution · Idempotency]]

**What it actually means:** A durable snapshot used to resume from a known boundary. In a workflow, it stores operational state and artifact references. In model training, it can store parameters, optimizer state, scheduler state, and the training position.

**Why it matters:** Long-running workflows and training runs can recover from interruption without replaying completed work or losing expensive progress.

**In practice:** Save an agent's accepted patch and test evidence after a verified step, or save a training run's weights, optimizer state, random state, and data position before shutdown.

**Common confusion:** A workflow checkpoint and a model-training checkpoint serve the same recovery goal but preserve different state. Neither is merely a transcript or a weights file with no resume metadata.

**Category:** [[Categories/Agents & tools|Agents & tools]]

## Related concepts

- [[Concepts/Activation Checkpointing|Activation Checkpointing]]
- [[Concepts/Agent Memory|Agent Memory]]
- [[Concepts/Agent State|Agent State]]
- [[Concepts/Compensating Action|Compensating Action]]
- [[Concepts/Durable Execution|Durable Execution]]
- [[Concepts/Handoff|Handoff]]
- [[Concepts/Idempotency|Idempotency]]
- [[Concepts/Optimizer|Optimizer]]
- [[Concepts/Parameter|Parameter]]
- [[Concepts/Rollback|Rollback]]

## Taught in

- [[Lessons/11-16 Agent State Machines — Graphs, Nodes, Checkpoints|11/16 Agent State Machines — Graphs, Nodes, Checkpoints]] — A persisted snapshot of the full graph state after a node transition, keyed on (thread_id, checkpoint_id).
- [[Lessons/14-34 Repo Memory and Durable State|14/34 Repo Memory and Durable State]]
- [[Lessons/15-12 Long-Running Background Agents- Durable Execution|15/12 Long-Running Background Agents: Durable Execution]] — Persisted state keyed by thread_id; latest-wins on resume
- [[Lessons/15-16 Checkpoints and Rollback|15/16 Checkpoints and Rollback]] — Every graph-state transition persists to a durable store
- [[Lessons/16-22 Production Scaling — Queues, Checkpoints, Durability|16/22 Production Scaling — Queues, Checkpoints, Durability]] — Serialized state at a super-step boundary; key for resume.
- [[Lessons/19-47 Checkpoint Save and Resume|19/47 Checkpoint Save and Resume]]


%% ── my notes ── %%
