---
id: "concept:durable-execution"
type: concept
name: Durable Execution
canonical: true
category: "Agents & tools"
taught_in: 3
community: 35
tags:
  - concept/glossary
  - category/agents-and-tools
  - community/35
source: ai-engineering-from-scratch/glossary/terms.md
---

# Durable Execution

**Community:** [[Communities/35 Checkpoint · Durable Execution · Idempotency|35 Checkpoint · Durable Execution · Idempotency]]

**What it actually means:** Running a workflow so its state and completed steps survive process crashes, restarts, or long waits without redoing confirmed side effects.

**Why it matters:** Agent tasks often span model calls, tools, approvals, and external systems. A transient process should not be the only record of progress.

**In practice:** Persist each workflow transition, use idempotency keys for external writes, and resume from the latest checkpoint after a worker restarts.

**Common confusion:** Durable execution does not make every operation safe automatically. Side effects still need idempotency and compensation rules.

**Category:** [[Categories/Agents & tools|Agents & tools]]

## Related concepts

- [[Concepts/Agent State|Agent State]]
- [[Concepts/Approval Gate|Approval Gate]]
- [[Concepts/Checkpoint|Checkpoint]]
- [[Concepts/Compensating Action|Compensating Action]]
- [[Concepts/Idempotency|Idempotency]]
- [[Concepts/Orchestration|Orchestration]]
- [[Concepts/Rollback|Rollback]]

## Taught in

- [[Lessons/14-13 Stateful Graph Orchestration — Durable Execution and Checkpoints|14/13 Stateful Graph Orchestration — Durable Execution and Checkpoints]] — Restart at the last successful node with exact state
- [[Lessons/14-29 Production Runtimes- Queue, Event, Cron|14/29 Production Runtimes: Queue, Event, Cron]] — Checkpointed state; restart at last step
- [[Lessons/16-22 Production Scaling — Queues, Checkpoints, Durability|16/22 Production Scaling — Queues, Checkpoints, Durability]] — Engine writes state after each super-step; crash recovery is deterministic.


%% ── my notes ── %%
