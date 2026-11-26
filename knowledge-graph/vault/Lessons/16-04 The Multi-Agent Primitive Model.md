---
id: "lesson:16/04"
type: lesson
ref: 16/04
phase: 16
num: 4
title: The Multi-Agent Primitive Model
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 1
community: 6
aliases:
  - 16/04
  - 16-04
tags:
  - phase/16
  - type/learn
  - community/06
  - stdlib-only
source: ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/04-primitive-model/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/04-primitive-model"
---

# 16/04 The Multi-Agent Primitive Model

> Four primitives, nothing more — the agent, the handoff, the shared state, the orchestrator — span a four-dimensional design space, and the major multi-agent frameworks shipping in 2026 (AutoGen, LangGraph, CrewAI, OpenAI Agents SDK, Microsoft Agent Framework) are points in it. This lesson builds them from zero, runs a toy system on all four, then maps every major framework onto the same axes so you can read any new release in one paragraph.

**Phase:** [[Phases/16 Multi-Agent & Swarms|Phase 16: Multi-Agent & Swarms]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/16-multi-agent-and-swarms/04-primitive-model/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/04-primitive-model) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/04-primitive-model) · code: main.py  
**Community:** [[Communities/06 Communicative dehallucination · Consensus · Contract Net|06 Communicative dehallucination · Consensus · Contract Net]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 14 (Agent Engineering), Phase 16 · 01 (Why Multi-Agent)`

- [[Lessons/16-01 Why Multi-Agent|16/01 Why Multi-Agent?]] — Why Multi-Agent
- Whole phase: [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] — Agent Engineering ·  medium confidence

## Builds on this

- [[Lessons/16-05 Supervisor - Orchestrator-Worker Pattern|16/05 Supervisor / Orchestrator-Worker Pattern]]
- [[Lessons/16-07 Society of Mind and Multi-Agent Debate|16/07 Society of Mind and Multi-Agent Debate]]
- [[Lessons/16-08 Role Specialization — Planner, Critic, Executor, Verifier|16/08 Role Specialization — Planner, Critic, Executor, Verifier]]
- [[Lessons/16-09 Parallel - Swarm - Networked Architectures|16/09 Parallel / Swarm / Networked Architectures]]
- [[Lessons/16-10 Group Chat and Speaker Selection|16/10 Group Chat and Speaker Selection]]
- [[Lessons/16-11 Handoffs and Routines — Stateless Orchestration|16/11 Handoffs and Routines — Stateless Orchestration]]
- [[Lessons/16-12 A2A — The Agent-to-Agent Protocol|16/12 A2A — The Agent-to-Agent Protocol]]
- [[Lessons/16-13 Shared Memory and Blackboard Patterns|16/13 Shared Memory and Blackboard Patterns]]
- [[Lessons/16-17 Generative Agents and Emergent Simulation|16/17 Generative Agents and Emergent Simulation]]
- [[Lessons/16-25 Case Studies and the 2026 State of the Art|16/25 Case Studies and the 2026 State of the Art]]

## Concepts taught

- [[Concepts/Agent|Agent]] `glossary` — A (system_prompt, tools, model) triple. Stateless.
- [[Concepts/Handoff|Handoff]] `glossary` — A structured call that names the next agent and optional payload. Three implementations: function return, graph edge, speaker selection.
- Shared state `lesson term` — The only stateful part of a multi-agent system. Message pool or blackboard.
- [[Concepts/Orchestrator|Orchestrator]] `lesson term` — Whoever decides who runs next. Static graph, LLM selector, handoff-driven, or queue-driven.
- Primitive `lesson term` — One of the four axes every framework parameterizes. Not a framework feature.
- [[Concepts/Message pool|Message pool]] `lesson term` — Full-history shared state. Easy to reason about, scales badly.
- Projected state `lesson term` — Role-specific view into shared state. Scales, requires schema design.
- [[Concepts/Speaker selection|Speaker selection]] `lesson term` — Orchestrator pattern where a function (often an LLM) picks the next agent from a group.

## Ships

- [[Artifacts/16-04 primitive-mapper|primitive-mapper]] `skill` — Map any multi-agent framework or codebase to the four primitive axes (agent, handoff, shared state, orchestrator).

## Further reading

- [[Resources/OpenAI cookbook- Orchestrating Agents — Routines and Handoffs|OpenAI cookbook: Orchestrating Agents — Routines and Handoffs]] ([link](https://developers.openai.com/cookbook/examples/orchestrating_agents)) — the clearest articulation of handoff-driven orchestration ·  also cited by 2 other lessons
- [[Resources/CrewAI docs introduction|CrewAI docs introduction]] ([link](https://docs.crewai.com/en/introduction)) — role-goal-backstory agents, Sequential / Hierarchical processes ·  also cited by 5 other lessons
- [[Resources/LangGraph workflows and agents|LangGraph workflows and agents]] ([link](https://docs.langchain.com/oss/python/langgraph/workflows-agents)) — graph-edge orchestration and reducer-based shared state ·  also cited by 4 other lessons
- [[Resources/AG2 (community AutoGen continuation)|AG2 (community AutoGen continuation)]] ([link](https://github.com/ag2ai/ag2)) — the live AutoGen v0.2 line after Microsoft moved v0.4 into maintenance ·  also cited by 1 other lesson
- [[Resources/AutoGen stable docs|AutoGen stable docs]] ([link](https://microsoft.github.io/autogen/stable/)) — GroupChat + speaker selection is the reference for LLM-selected orchestration ·  also cited by 2 other lessons


%% ── my notes ── %%
