---
id: "lesson:14/14"
type: lesson
ref: 14/14
phase: 14
num: 14
title: "The Actor Model for Agents — Async Messages and Typed Runtimes"
lesson_type: learn+build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 7
code_files: 1
concepts: 9
prereqs: 2
community: 7
aliases:
  - 14/14
  - 14-14
tags:
  - phase/14
  - type/learn+build
  - community/07
  - stdlib-only
source: ai-engineering-from-scratch/phases/14-agent-engineering/14-autogen-actor-model/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/14-autogen-actor-model"
---

# 14/14 The Actor Model for Agents — Async Messages and Typed Runtimes

> Agents as actors: async message exchange, event-driven handlers, fault isolation, natural concurrency. AutoGen v0.4 (Microsoft Research, Jan 2025) redesigned agent orchestration around this model; the framework is now in maintenance mode, with Microsoft Agent Framework (public preview Oct 2025) as its production successor.

**Phase:** [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] · **Type:** Learn + Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/14-agent-engineering/14-autogen-actor-model/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/14-autogen-actor-model) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/14-agent-engineering/14-autogen-actor-model) · code: main.py · quiz: 7 questions  
**Community:** [[Communities/07 Swarm · Evaluator-Optimizer · Debate|07 Swarm · Evaluator-Optimizer · Debate]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 14 · 01 (Agent Loop), Phase 14 · 12 (Workflow Patterns)`

- [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]] — Agent Loop
- [[Lessons/14-12 Anthropic's Workflow Patterns- Simple Over Complex|14/12 Anthropic's Workflow Patterns: Simple Over Complex]] — Workflow Patterns

## Builds on this

- [[Lessons/14-15 Role-Based Agent Teams — Roles, Tasks, Processes|14/15 Role-Based Agent Teams — Roles, Tasks, Processes]]
- [[Lessons/14-30 Eval-Driven Agent Development|14/30 Eval-Driven Agent Development]]

## Concepts taught

- [[Concepts/Actor|Actor]] `lesson term` — Private state + inbox + handler; no shared memory
- [[Concepts/Message|Message]] `lesson term` — Typed payload; the only way actors interact
- Inbox `lesson term` — Per-actor queue of pending messages
- Runtime `lesson term` — Event loop that routes messages and isolates failures
- [[Concepts/Topic|Topic]] `lesson term` — Named publish-subscribe route between actors
- Fault isolation `lesson term` — One actor failing does not crash others
- RoundRobinGroupChat `lesson term` — Agents take turns in order
- SelectorGroupChat `lesson term` — Selector picks who goes next
- Magentic-One `lesson term` — Multi-agent squad for web + code + files

## Ships

- [[Artifacts/14-14 actor-runtime|actor-runtime]] `skill` — Build an AutoGen v0.4-shaped actor runtime with private state, inbox-per-actor, message-only IPC, fault isolation, and a dead-letter queue.

## Further reading

- [[Resources/LangGraph Plan-and-Execute tutorial|LangGraph Plan-and-Execute tutorial]] ([link](https://docs.langchain.com/oss/python/langgraph/overview)) — graph-shaped alternative ·  also cited by 9 other lessons
- [[Resources/AutoGen v0.4, Microsoft Research|AutoGen v0.4, Microsoft Research]] ([link](https://www.microsoft.com/en-us/research/articles/autogen-v0-4-reimagining-the-foundation-of-agentic-ai-for-scale-extensibility-and-robustness/)) — the redesign post ·  also cited by 3 other lessons
- [[Resources/OpenTelemetry — GenAI semconv|OpenTelemetry — GenAI semconv]] ([link](https://opentelemetry.io/docs/specs/semconv/gen-ai/)) — spans AutoGen emits by default ·  also cited by 9 other lessons


%% ── my notes ── %%
