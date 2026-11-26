---
id: "lesson:14/12"
type: lesson
ref: 14/12
phase: 14
num: 12
title: "Anthropic's Workflow Patterns: Simple Over Complex"
lesson_type: learn+build
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 7
code_files: 1
concepts: 8
prereqs: 1
community: 7
aliases:
  - 14/12
  - 14-12
tags:
  - phase/14
  - type/learn+build
  - community/07
  - stdlib-only
source: ai-engineering-from-scratch/phases/14-agent-engineering/12-anthropic-workflow-patterns/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/12-anthropic-workflow-patterns"
---

# 14/12 Anthropic's Workflow Patterns: Simple Over Complex

> Schluntz and Zhang (Anthropic, Dec 2024) distinguish workflows (predefined paths) from agents (dynamic tool-use). Five workflow patterns cover most cases. Start with direct API calls. Add agents only when steps cannot be predicted.

**Phase:** [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] · **Type:** Learn + Build · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/14-agent-engineering/12-anthropic-workflow-patterns/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/12-anthropic-workflow-patterns) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/14-agent-engineering/12-anthropic-workflow-patterns) · code: main.py · quiz: 7 questions  
**Community:** [[Communities/07 Swarm · Evaluator-Optimizer · Debate|07 Swarm · Evaluator-Optimizer · Debate]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 14 · 01 (Agent Loop)`

- [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]] — Agent Loop

## Builds on this

- [[Lessons/14-13 Stateful Graph Orchestration — Durable Execution and Checkpoints|14/13 Stateful Graph Orchestration — Durable Execution and Checkpoints]]
- [[Lessons/14-14 The Actor Model for Agents — Async Messages and Typed Runtimes|14/14 The Actor Model for Agents — Async Messages and Typed Runtimes]]
- [[Lessons/14-15 Role-Based Agent Teams — Roles, Tasks, Processes|14/15 Role-Based Agent Teams — Roles, Tasks, Processes]]
- [[Lessons/14-22 Voice Agents- Pipecat and LiveKit|14/22 Voice Agents: Pipecat and LiveKit]]
- [[Lessons/14-25 Multi-Agent Debate and Collaboration|14/25 Multi-Agent Debate and Collaboration]]
- [[Lessons/14-28 Orchestration Patterns- Supervisor, Swarm, Hierarchical|14/28 Orchestration Patterns: Supervisor, Swarm, Hierarchical]]
- [[Lessons/14-30 Eval-Driven Agent Development|14/30 Eval-Driven Agent Development]]

## Concepts taught

- [[Concepts/Workflow|Workflow]] `lesson term` — Engineer-owned graph of LLM and tool calls
- [[Concepts/Agent|Agent]] `glossary` — Model-owned graph; dynamic tool direction
- Augmented LLM `lesson term` — LLM + search + tools + memory; the atomic unit
- [[Concepts/Prompt chaining|Prompt chaining]] `lesson term` — Output of call N is input to call N+1
- Routing `lesson term` — Pick which chain/model handles the input
- Parallelization `lesson term` — N concurrent calls; aggregate by sectioning or voting
- Orchestrator-workers `lesson term` — Orchestrator LLM picks specialist LLMs dynamically
- [[Concepts/Evaluator-Optimizer|Evaluator-Optimizer]] `lesson term` — Iterate until evaluator passes; Self-Refine generalized

## Ships

- [[Artifacts/14-12 workflow-picker|workflow-picker]] `skill` — Pick the right pattern (prompt chain, router, parallel, orchestrator-workers, evaluator-optimizer, or full agent) for a given task and produce the minimal implementation.

## Further reading

- [[Resources/Anthropic, Effective context engineering for AI agents|Anthropic, Effective context engineering for AI agents]] ([link](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)) — the companion discipline ·  also cited by 2 other lessons
- [[Resources/Building Effective Agents|Building Effective Agents]] ([link](https://www.anthropic.com/research/building-effective-agents)) — the five workflow patterns ·  also cited by 16 other lessons
- [[Resources/LangGraph Plan-and-Execute tutorial|LangGraph Plan-and-Execute tutorial]] ([link](https://docs.langchain.com/oss/python/langgraph/overview)) — when stateful graphs earn their cost ·  also cited by 9 other lessons
- [[Resources/OpenAI Agents SDK docs|OpenAI Agents SDK docs]] ([link](https://openai.github.io/openai-agents-python/)) — the orchestrator-workers pattern, productized ·  also cited by 8 other lessons


%% ── my notes ── %%
