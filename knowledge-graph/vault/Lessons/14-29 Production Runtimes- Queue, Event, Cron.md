---
id: "lesson:14/29"
type: lesson
ref: 14/29
phase: 14
num: 29
title: "Production Runtimes: Queue, Event, Cron"
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 7
code_files: 1
concepts: 8
prereqs: 2
community: 7
aliases:
  - 14/29
  - 14-29
tags:
  - phase/14
  - type/learn
  - community/07
  - stdlib-only
source: ai-engineering-from-scratch/phases/14-agent-engineering/29-production-runtimes/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/29-production-runtimes"
---

# 14/29 Production Runtimes: Queue, Event, Cron

> Production agents run on six runtime shapes: request-response, streaming, durable execution, queue-based background, event-driven, and scheduled. Pick the shape before you pick the framework. Observability is load-bearing at every shape.

**Phase:** [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/14-agent-engineering/29-production-runtimes/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/29-production-runtimes) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/14-agent-engineering/29-production-runtimes) · code: main.py · quiz: 7 questions  
**Community:** [[Communities/07 Swarm · Evaluator-Optimizer · Debate|07 Swarm · Evaluator-Optimizer · Debate]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 14 · 13 (LangGraph), Phase 14 · 22 (Voice)`

- [[Lessons/14-13 Stateful Graph Orchestration — Durable Execution and Checkpoints|14/13 Stateful Graph Orchestration — Durable Execution and Checkpoints]] — LangGraph
- [[Lessons/14-22 Voice Agents- Pipecat and LiveKit|14/22 Voice Agents: Pipecat and LiveKit]] — Voice

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]], [[Lessons/14-12 Anthropic's Workflow Patterns- Simple Over Complex|14/12 Anthropic's Workflow Patterns: Simple Over Complex]]

## Builds on this

- [[Lessons/14-30 Eval-Driven Agent Development|14/30 Eval-Driven Agent Development]]

## Concepts taught

- Request-response `lesson term` — User waits; short tasks only
- [[Concepts/Streaming|Streaming]] `glossary` — Progressive output; better UX; latency observable per chunk
- [[Concepts/Durable Execution|Durable Execution]] `glossary` — Checkpointed state; restart at last step
- Queue-based `lesson term` — Producer / worker pool / DLQ
- Event-driven `lesson term` — Agent reacts to external events
- DLQ `lesson term` — Parking lot for failed jobs
- Claude Managed Agents `lesson term` — Anthropic-hosted long-running async with caching + compaction
- [[Concepts/Sandbox|Sandbox]] `glossary` — An isolated execution environment that restricts an agent's access to files, processes, network destinations, credentials, and host resources.

## Ships

- [[Artifacts/14-29 runtime-shape|runtime-shape]] `skill` — Pick a production runtime shape (request-response, streaming, queue, event, cron, durable) and wire observability.

## Further reading

- [[Resources/Anthropic, Introducing computer use|Anthropic, Introducing computer use]] ([link](https://www.anthropic.com/news/3-5-models-and-computer-use)) — "dozens-to-hundreds of steps per task" ·  also cited by 2 other lessons
- [[Resources/LangGraph Plan-and-Execute tutorial|LangGraph Plan-and-Execute tutorial]] ([link](https://docs.langchain.com/oss/python/langgraph/overview)) — durable execution details ·  also cited by 9 other lessons
- [[Resources/AutoGen v0.4, Microsoft Research|AutoGen v0.4, Microsoft Research]] ([link](https://www.microsoft.com/en-us/research/articles/autogen-v0-4-reimagining-the-foundation-of-agentic-ai-for-scale-extensibility-and-robustness/)) — actor-model fault isolation ·  also cited by 3 other lessons
- [[Resources/Claude Managed Agents overview|Claude Managed Agents overview]] ([link](https://platform.claude.com/docs/en/managed-agents/overview)) — hosted long-running async ·  also cited by 3 other lessons

## In learning paths

- [[Paths/Agent Systems Engineering|Agent Systems Engineering]] — step 13, required


%% ── my notes ── %%
