---
id: "lesson:16/22"
type: lesson
ref: 16/22
phase: 16
num: 22
title: "Production Scaling — Queues, Checkpoints, Durability"
lesson_type: learn+build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 0
code_files: 1
concepts: 9
prereqs: 2
community: 6
aliases:
  - 16/22
  - 16-22
tags:
  - phase/16
  - type/learn+build
  - community/06
  - stdlib-only
source: ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/22-production-scaling-queues-checkpoints/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/22-production-scaling-queues-checkpoints"
---

# 16/22 Production Scaling — Queues, Checkpoints, Durability

> Scaling multi-agent systems to thousands of concurrent runs requires **durable execution** — work queues plus checkpoints, so any worker can resume any run after any crash, provided lease handling, idempotent side effects, and deterministic replay are in place. LangGraph's runtime is the reference example: it writes a checkpoint after each super-step keyed by `thread_id` (Postgres by default); worker crashes release a lease and another worker resumes. Agents can sleep indefinitely waiting for human input. **MegaAgent** (arXiv:2408.09955) ran a per-agent producer-consumer queue with three states (Idle / Processing / Response) and two-layer coordination (intra-group chat + inter-group admin chat). **Fiber/async** beats thread-per-job for LLM streaming: threads sit idle 99% of the time waiting for tokens, fibers cooperatively yield on I/O. Counterpoint: Ashpreet Bedi's "Scaling Agentic Software" argues for **FastAPI + Postgres + nothing else** until load proves otherwise — simple architectures go further than expected. This lesson builds a durable checkpoint log, a per-agent work queue with state transitions, an async-vs-thread demo, and lands the pragmatic "start simple" rule.

**Phase:** [[Phases/16 Multi-Agent & Swarms|Phase 16: Multi-Agent & Swarms]] · **Type:** Learn + Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/16-multi-agent-and-swarms/22-production-scaling-queues-checkpoints/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/22-production-scaling-queues-checkpoints) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/22-production-scaling-queues-checkpoints) · code: main.py  
**Community:** [[Communities/06 Communicative dehallucination · Consensus · Contract Net|06 Communicative dehallucination · Consensus · Contract Net]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 16 · 09 (Parallel Swarm Networks), Phase 16 · 13 (Shared Memory)`

- [[Lessons/16-09 Parallel - Swarm - Networked Architectures|16/09 Parallel / Swarm / Networked Architectures]] — Parallel Swarm Networks
- [[Lessons/16-13 Shared Memory and Blackboard Patterns|16/13 Shared Memory and Blackboard Patterns]] — Shared Memory

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/16-04 The Multi-Agent Primitive Model|16/04 The Multi-Agent Primitive Model]], [[Lessons/16-05 Supervisor - Orchestrator-Worker Pattern|16/05 Supervisor / Orchestrator-Worker Pattern]]
- depth 3: [[Lessons/16-01 Why Multi-Agent|16/01 Why Multi-Agent?]]

## Builds on this

- [[Lessons/16-25 Case Studies and the 2026 State of the Art|16/25 Case Studies and the 2026 State of the Art]]

## Concepts taught

- [[Concepts/Durable Execution|Durable Execution]] `glossary` — Engine writes state after each super-step; crash recovery is deterministic.
- Super-step `lesson term` — Unit of work between checkpoints. LangGraph term.
- [[Concepts/thread_id|thread_id]] `lesson term` — Key that binds checkpoints and resume logic.
- [[Concepts/Idempotency|Idempotency]] `glossary` — Repeating a side effect produces the same result as one attempt.
- Outbox pattern `lesson term` — Write intent to a table; a separate executor performs and marks done.
- At-least-once delivery `lesson term` — Message queue semantics; dedup key makes consumer effective-once.
- [[Concepts/Rainbow deploy|Rainbow deploy]] `lesson term` — Multiple runtime versions concurrent during long-running workloads.
- Async fiber `lesson term` — User-mode concurrency; cheap compared to threads for I/O-bound loads.
- [[Concepts/Checkpoint|Checkpoint]] `glossary` — Serialized state at a super-step boundary; key for resume.

## Ships

- [[Artifacts/16-22 scaling-advisor|scaling-advisor]] `skill` — Advise on durable-execution choice for a multi-agent production system. Picks between FastAPI + Postgres, LangGraph runtime, Temporal, Restate, or custom based on concrete load and state-retention needs.

## Further reading

- [[Resources/Anthropic engineering — How we built our multi-agent research system|Anthropic engineering — How we built our multi-agent research system]] ([link](https://www.anthropic.com/engineering/multi-agent-research-system)) — production lessons including rainbow deployment ·  also cited by 6 other lessons
- MegaAgent ([link](https://arxiv.org/abs/2408.09955)) — per-agent producer-consumer queue; two-layer coordination at thousands of concurrent agents
- [[Resources/Matrix — A Decentralized Framework for Multi-Agent Systems|Matrix — A Decentralized Framework for Multi-Agent Systems]] ([link](https://arxiv.org/abs/2511.21686)) — decentralized framework with message queues as the coordination substrate ·  also cited by 2 other lessons
- Temporal docs ([link](https://docs.temporal.io/)) — the reference workflow engine for durable execution
- [[Resources/LangChain — The Runtime Behind Production Deep Agents|LangChain — The Runtime Behind Production Deep Agents]] ([link](https://www.langchain.com/conceptual-guides/runtime-behind-production-deep-agents)) — LangGraph runtime design ·  also cited by 1 other lesson


%% ── my notes ── %%
