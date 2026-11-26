---
id: "lesson:14/18"
type: lesson
ref: 14/18
phase: 14
num: 18
title: "Production Agent Runtimes — Fast Instantiation and Typed Workflows"
lesson_type: learn
languages:
  - Python
  - TypeScript
time_min: 45
on_route: false
quiz_count: 7
code_files: 2
concepts: 6
prereqs: 2
community: 7
aliases:
  - 14/18
  - 14-18
tags:
  - phase/14
  - type/learn
  - community/07
  - stdlib-only
source: ai-engineering-from-scratch/phases/14-agent-engineering/18-agno-and-mastra-runtimes/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/18-agno-and-mastra-runtimes"
---

# 14/18 Production Agent Runtimes — Fast Instantiation and Typed Workflows

> A production agent runtime optimizes what prototyping frameworks ignore: instantiation cost, typed workflow surfaces, and a serving-ready backend. The 2026 pairing: Agno (Python) aims at microsecond agent instantiation and stateless FastAPI backends. Mastra ships agents, tools, workflows, unified model routing, and composite storage on the Vercel AI SDK substrate.

**Phase:** [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] · **Type:** Learn · **Time:** 45 min · **Languages:** Python, TypeScript · **Status:** —  
**Open:** [[Upstream/14-agent-engineering/18-agno-and-mastra-runtimes/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/18-agno-and-mastra-runtimes) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/14-agent-engineering/18-agno-and-mastra-runtimes) · code: main.py, main.ts · quiz: 7 questions  
**Community:** [[Communities/07 Swarm · Evaluator-Optimizer · Debate|07 Swarm · Evaluator-Optimizer · Debate]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 14 · 01 (Agent Loop), Phase 14 · 13 (LangGraph)`

- [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]] — Agent Loop
- [[Lessons/14-13 Stateful Graph Orchestration — Durable Execution and Checkpoints|14/13 Stateful Graph Orchestration — Durable Execution and Checkpoints]] — LangGraph

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/14-12 Anthropic's Workflow Patterns- Simple Over Complex|14/12 Anthropic's Workflow Patterns: Simple Over Complex]]

## Builds on this

- [[Lessons/14-30 Eval-Driven Agent Development|14/30 Eval-Driven Agent Development]]

## Concepts taught

- Agno `lesson term` — Stateless session-scoped agent runtime
- Mastra `lesson term` — Agents + Tools + Workflows + Model Router
- Unified Model Router `lesson term` — Single client for 3,300+ models across 94 providers
- Composite storage `lesson term` — Memory/workflows/observability each to a different store
- Mastra Studio `lesson term` — localhost:4111 UI for introspecting agents
- Source-available `lesson term` — License permits source reading but restricts commercial use

## Ships

- [[Artifacts/14-18 runtime-picker|runtime-picker]] `skill` — Pick a production agent runtime (Agno, Mastra, LangGraph, provider SDK) for a given stack, latency budget, and operational shape.

## Further reading

- Agno Agent Framework docs ([link](https://www.agno.com/agent-framework)) — performance targets, FastAPI integration
- [[Resources/Comet Opik|Comet Opik]] ([link](https://www.comet.com/site/products/opik/)) — observability comparisons cited by Mastra integrations ·  also cited by 1 other lesson
- [[Resources/LangGraph Plan-and-Execute tutorial|LangGraph Plan-and-Execute tutorial]] ([link](https://docs.langchain.com/oss/python/langgraph/overview)) — the stateful-graph alternative ·  also cited by 9 other lessons
- Mastra docs ([link](https://mastra.ai/docs)) — primitives, server adapters, Model Router


%% ── my notes ── %%
