---
id: "lesson:15/12"
type: lesson
ref: 15/12
phase: 15
num: 12
title: "Long-Running Background Agents: Durable Execution"
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 2
community: 29
aliases:
  - 15/12
  - 15-12
tags:
  - phase/15
  - type/learn
  - community/29
  - stdlib-only
source: ai-engineering-from-scratch/phases/15-autonomous-systems/12-durable-execution/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/15-autonomous-systems/12-durable-execution"
---

# 15/12 Long-Running Background Agents: Durable Execution

> Production long-horizon agents do not run in `while True`. Every LLM call becomes an activity with checkpoint, retry, and replay. Temporal's OpenAI Agents SDK integration went GA March 2026. Claude Code Routines (Anthropic) runs scheduled Claude Code invocations without a persistent local process. Sessions pause on human-input, survive deploys, and resume from the latest checkpoint keyed by `thread_id`. Behind the new ergonomics sits an old pattern — workflow orchestration — with one new input: LLM calls as non-deterministic activities that must be deterministically replayed on recovery.

**Phase:** [[Phases/15 Autonomous Systems|Phase 15: Autonomous Systems]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/15-autonomous-systems/12-durable-execution/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/15-autonomous-systems/12-durable-execution) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/15-autonomous-systems/12-durable-execution) · code: main.py  
**Community:** [[Communities/29 Eval-context gaming · Time horizon · thread_id|29 Eval-context gaming · Time horizon · thread_id]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 15 · 10 (Permission modes), Phase 15 · 01 (Long-horizon agents)`

- [[Lessons/15-01 The Shift from Chatbots to Long-Horizon Agents|15/01 The Shift from Chatbots to Long-Horizon Agents]] — Long-horizon agents
- [[Lessons/15-10 Permission Modes for Autonomous Agents|15/10 Permission Modes for Autonomous Agents]] — Permission modes

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]], [[Lessons/15-09 The Autonomous Coding Agent Landscape (2026)|15/09 The Autonomous Coding Agent Landscape (2026)]]
- depth 3: [[Lessons/14-07 Agent Memory — Virtual Context and Memory Paging|14/07 Agent Memory — Virtual Context and Memory Paging]]

## Builds on this

- [[Lessons/15-13 Action Budgets, Iteration Caps, and Cost Governors|15/13 Action Budgets, Iteration Caps, and Cost Governors]]
- [[Lessons/15-15 Human-in-the-Loop- Propose-Then-Commit|15/15 Human-in-the-Loop: Propose-Then-Commit]]
- [[Lessons/15-16 Checkpoints and Rollback|15/16 Checkpoints and Rollback]]

## Concepts taught

- [[Concepts/Workflow|Workflow]] `lesson term` — Deterministic orchestration code; replayable from event log
- Activity `lesson term` — Non-deterministic unit (LLM call, tool call); logged before and after
- Event log `lesson term` — Durable record of every state transition
- Replay `lesson term` — Re-run workflow; completed activities return logged results without re-execution
- [[Concepts/Checkpoint|Checkpoint]] `glossary` — Persisted state keyed by thread_id; latest-wins on resume
- [[Concepts/thread_id|thread_id]] `lesson term` — Identifier that scopes durable state
- 35-minute degradation `lesson term` — METR: success rate drops ~quadratically with horizon
- [[Concepts/Non-determinism|Non-determinism]] `lesson term` — Wall clock, random, LLM output; must be registered as side effect

## Ships

- [[Artifacts/15-12 durable-execution-review|durable-execution-review]] `skill` — Review a proposed long-running agent deployment for correct durable-execution shape (activities, determinism, checkpoint backend, human-input state, HITL-on-resume).

## Further reading

- [[Resources/Anthropic — Measuring AI agent autonomy in practice|Anthropic — Measuring AI agent autonomy in practice]] ([link](https://www.anthropic.com/research/measuring-agent-autonomy)) — the 35-minute degradation reference. ·  also cited by 16 other lessons
- [[Resources/Anthropic — How the agent loop works|Anthropic — How the agent loop works]] ([link](https://code.claude.com/docs/en/agent-sdk/agent-loop)) — budget, turns, and resume semantics. ·  also cited by 3 other lessons
- [[Resources/LangChain — The Runtime Behind Production Deep Agents|LangChain — The Runtime Behind Production Deep Agents]] ([link](https://www.langchain.com/conceptual-guides/runtime-behind-production-deep-agents)) — concrete runtime requirements. ·  also cited by 1 other lesson
- [[Resources/Microsoft — Agent Framework- human-in-the-loop and checkpointing|Microsoft — Agent Framework: human-in-the-loop and checkpointing]] ([link](https://learn.microsoft.com/en-us/agent-framework/workflows/human-in-the-loop)) — RequestInfoEvent shape. ·  also cited by 4 other lessons
- OpenAI Agents SDK + Temporal integration (Trigger.dev announcement) ([link](https://trigger.dev)) — activity shape for LLM calls.


%% ── my notes ── %%
