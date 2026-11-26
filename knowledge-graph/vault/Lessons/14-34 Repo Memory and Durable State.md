---
id: "lesson:14/34"
type: lesson
ref: 14/34
phase: 14
num: 34
title: Repo Memory and Durable State
lesson_type: build
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 7
code_files: 1
concepts: 8
prereqs: 1
community: 15
aliases:
  - 14/34
  - 14-34
tags:
  - phase/14
  - type/build
  - community/15
  - stdlib-only
source: ai-engineering-from-scratch/phases/14-agent-engineering/34-repo-memory-and-state/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/34-repo-memory-and-state"
---

# 14/34 Repo Memory and Durable State

> Chat history is volatile. The repo is durable. The workbench stores agent state in versioned files so the next session, the next agent, and the next reviewer all read from the same source of truth.

**Phase:** [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] · **Type:** Build · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/14-agent-engineering/34-repo-memory-and-state/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/34-repo-memory-and-state) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/14-agent-engineering/34-repo-memory-and-state) · code: main.py · quiz: 7 questions  
**Community:** [[Communities/15 System of record · Block severity · Definition of done|15 System of record · Block severity · Definition of done]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 14 · 32 (Minimal Workbench)`

- [[Lessons/14-32 The Minimal Agent Workbench|14/32 The Minimal Agent Workbench]] — Minimal Workbench

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/14-31 Agent Workbench Engineering- Why Capable Models Still Fail|14/31 Agent Workbench Engineering: Why Capable Models Still Fail]]
- depth 3: [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]], [[Lessons/14-26 Failure Modes- Why Agents Break|14/26 Failure Modes: Why Agents Break]]

## Builds on this

- [[Lessons/14-35 Initialization Scripts for Agents|14/35 Initialization Scripts for Agents]]
- [[Lessons/14-40 Multi-Session Handoff|14/40 Multi-Session Handoff]]
- [[Lessons/14-41 The Workbench on a Real Repo|14/41 The Workbench on a Real Repo]]
- [[Lessons/14-42 Capstone- Ship a Reusable Agent Workbench Pack|14/42 Capstone: Ship a Reusable Agent Workbench Pack]]

## Concepts taught

- Repo memory `lesson term` — State stored in tracked files in the repo, under schema
- Schema-first `lesson term` — Define the contract before the writer, refuse drift
- [[Concepts/Atomic write|Atomic write]] `lesson term` — Write to temp, fsync, rename, so partial failures cannot corrupt
- Migration `lesson term` — A script that turns vN state into v(N+1) state
- [[Concepts/System of record|System of record]] `lesson term` — The artifact the workbench treats as authoritative
- [[Concepts/Agent State|Agent State]] `glossary` — The explicit data an agent carries across steps, such as the current objective, completed actions, tool results, open questions, budgets, approvals, and artifact references.
- [[Concepts/Checkpoint|Checkpoint]] `glossary` — A durable snapshot used to resume from a known boundary. In a workflow, it stores operational state and artifact references. In model training, it can store parameters, optimizer state, scheduler state, and the training position.
- [[Concepts/Repository Map|Repository Map]] `glossary` — A compact, maintained description of a repository's important directories, ownership boundaries, entry points, build commands, tests, generated files, and local instructions.

## Ships

- [[Artifacts/14-34 state-schema|state-schema]] `skill` — Generate project-specific JSON Schemas for agent state and task board, a Python StateManager with atomic writes, and a migration scaffold so schema bumps cannot corrupt the workbench.

## Further reading

- Letta memory blocks ([link](https://docs.letta.com/concepts/memory))
- eunomia, Checkpoint/Restore Systems: Evolution, Techniques, Applications ([link](https://eunomia.dev/blog/2025/05/11/checkpointrestore-systems-evolution-techniques-and-applications-in-ai-agents/)) — CR primitives from OS history applied to agents
- Fast.io, AI Agent State Checkpointing: A Practical Guide ([link](https://fast.io/resources/ai-agent-state-checkpointing/)) — schema-first checkpointing with idempotency
- Fast.io, AI Agent Workflow State Persistence: Best Practices 2026 ([link](https://fast.io/resources/ai-agent-workflow-state-persistence/)) — concurrency control, TTL, event sourcing
- Hive Issue #6263 — non-atomic state.json writes silently ignored ([link](https://github.com/aden-hive/hive/issues/6263)) — the failure mode in a real project
- Indium, 7 State Persistence Strategies for Long-Running AI Agents in 2026 ([link](https://www.indium.tech/blog/7-state-persistence-strategies-ai-agents-2026/))
- JSON Schema specification ([link](https://json-schema.org/specification.html))
- [[Resources/LangGraph Persistence and Checkpoints|LangGraph Persistence and Checkpoints]] ([link](https://langchain-ai.github.io/langgraph/concepts/persistence/)) ·  also cited by 1 other lesson
- [[Resources/Microsoft Agent Framework, Compaction|Microsoft Agent Framework, Compaction]] ([link](https://learn.microsoft.com/en-us/agent-framework/agents/conversations/compaction)) — vendor checkpoint manager ·  also cited by 1 other lesson

## In learning paths

- [[Paths/Agent-Assisted Engineering|Agent-Assisted Engineering]] — step 6, required


%% ── my notes ── %%
