---
id: "lesson:14/13"
type: lesson
ref: 14/13
phase: 14
num: 13
title: "Stateful Graph Orchestration — Durable Execution and Checkpoints"
lesson_type: learn+build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 7
code_files: 2
concepts: 8
prereqs: 2
community: 7
aliases:
  - 14/13
  - 14-13
tags:
  - phase/14
  - type/learn+build
  - community/07
  - stdlib-only
source: ai-engineering-from-scratch/phases/14-agent-engineering/13-langgraph-stateful-graphs/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/13-langgraph-stateful-graphs"
---

# 14/13 Stateful Graph Orchestration — Durable Execution and Checkpoints

> Agent is a state machine; nodes are functions; edges are transitions; state is checkpointed after each node. Resume from any failure at the last successful checkpoint. LangGraph is the 2026 reference for this model of low-level stateful orchestration.

**Phase:** [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] · **Type:** Learn + Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/14-agent-engineering/13-langgraph-stateful-graphs/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/13-langgraph-stateful-graphs) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/14-agent-engineering/13-langgraph-stateful-graphs) · code: main.py, main.ts · quiz: 7 questions  
**Community:** [[Communities/07 Swarm · Evaluator-Optimizer · Debate|07 Swarm · Evaluator-Optimizer · Debate]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 14 · 01 (Agent Loop), Phase 14 · 12 (Workflow Patterns)`

- [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]] — Agent Loop
- [[Lessons/14-12 Anthropic's Workflow Patterns- Simple Over Complex|14/12 Anthropic's Workflow Patterns: Simple Over Complex]] — Workflow Patterns

## Builds on this

- [[Lessons/14-18 Production Agent Runtimes — Fast Instantiation and Typed Workflows|14/18 Production Agent Runtimes — Fast Instantiation and Typed Workflows]]
- [[Lessons/14-23 OpenTelemetry GenAI Semantic Conventions|14/23 OpenTelemetry GenAI Semantic Conventions]]
- [[Lessons/14-29 Production Runtimes- Queue, Event, Cron|14/29 Production Runtimes: Queue, Event, Cron]]
- [[Lessons/14-30 Eval-Driven Agent Development|14/30 Eval-Driven Agent Development]]

## Concepts taught

- State graph `lesson term` — Typed state + nodes + edges + reducers
- Checkpointer `lesson term` — Serializes state after every node; enables resume
- [[Concepts/Reducer|Reducer]] `lesson term` — Function that combines current state with a node's update
- Conditional edge `lesson term` — Edge chosen by a function of state
- [[Concepts/Subgraph|Subgraph]] `lesson term` — A graph used as a node inside another graph
- [[Concepts/Durable Execution|Durable Execution]] `glossary` — Restart at the last successful node with exact state
- [[Concepts/Supervisor|Supervisor]] `lesson term` — Central dispatcher for specialist subagents
- [[Concepts/Swarm|Swarm]] `glossary` — Agents hand off via shared tools; no central router

## Ships

- [[Artifacts/14-13 state-graph|state-graph]] `skill` — Build a LangGraph-shaped state machine with typed state, conditional edges, per-node checkpointing, and durable resume.

## Further reading

- [[Resources/LangGraph Plan-and-Execute tutorial|LangGraph Plan-and-Execute tutorial]] ([link](https://docs.langchain.com/oss/python/langgraph/overview)) — the reference docs ·  also cited by 9 other lessons
- [[Resources/AutoGen v0.4, Microsoft Research|AutoGen v0.4, Microsoft Research]] ([link](https://www.microsoft.com/en-us/research/articles/autogen-v0-4-reimagining-the-foundation-of-agentic-ai-for-scale-extensibility-and-robustness/)) — actor-model alternative ·  also cited by 3 other lessons
- [[Resources/Claude Agent SDK overview|Claude Agent SDK overview]] ([link](https://platform.claude.com/docs/en/agent-sdk/overview)) — session store and subagents ·  also cited by 6 other lessons
- langgraph-supervisor reference ([link](https://reference.langchain.com/python/langgraph/supervisor/)) — supervisor pattern API

## In learning paths

- [[Paths/Agent Systems Engineering|Agent Systems Engineering]] — step 8, required


%% ── my notes ── %%
