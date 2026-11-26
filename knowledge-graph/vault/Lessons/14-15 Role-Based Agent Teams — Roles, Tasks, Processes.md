---
id: "lesson:14/15"
type: lesson
ref: 14/15
phase: 14
num: 15
title: "Role-Based Agent Teams — Roles, Tasks, Processes"
lesson_type: learn+build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 7
code_files: 1
concepts: 13
prereqs: 2
community: 69
libraries:
  - numpy
aliases:
  - 14/15
  - 14-15
tags:
  - phase/14
  - type/learn+build
  - community/69
source: ai-engineering-from-scratch/phases/14-agent-engineering/15-crewai-role-based-crews/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/15-crewai-role-based-crews"
---

# 14/15 Role-Based Agent Teams — Roles, Tasks, Processes

> Four primitives: Agent, Task, Crew, Process. Two top-level shapes: Crews (autonomous, role-based collaboration) and Flows (event-driven, deterministic). CrewAI is the 2026 reference implementation, and its docs are blunt: "for any production-ready application, start with a Flow."

**Phase:** [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] · **Type:** Learn + Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/14-agent-engineering/15-crewai-role-based-crews/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/15-crewai-role-based-crews) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/14-agent-engineering/15-crewai-role-based-crews) · code: main.py · quiz: 7 questions  
**Community:** [[Communities/69 Crew · Flow · Long-term memory|69 Crew · Flow · Long-term memory]] · **Libraries:** [[Libraries/numpy (python)|numpy]]  

## Prerequisites

Stated upstream: `Phase 14 · 12 (Workflow Patterns), Phase 14 · 14 (Actor Model)`

- [[Lessons/14-12 Anthropic's Workflow Patterns- Simple Over Complex|14/12 Anthropic's Workflow Patterns: Simple Over Complex]] — Workflow Patterns
- [[Lessons/14-14 The Actor Model for Agents — Async Messages and Typed Runtimes|14/14 The Actor Model for Agents — Async Messages and Typed Runtimes]] — Actor Model

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]]

## Builds on this

- [[Lessons/14-30 Eval-Driven Agent Development|14/30 Eval-Driven Agent Development]]

## Concepts taught

- [[Concepts/Agent|Agent]] `glossary` — Role + goal + backstory + tools
- [[Concepts/Task|Task]] `lesson term` — Description + expected output + assignee + optional structured output
- [[Concepts/Crew|Crew]] `lesson term` — Container for Agents + Tasks + Process
- Process `lesson term` — Sequential / Hierarchical / Consensus (planned)
- [[Concepts/Flow|Flow]] `lesson term` — Event-driven, code-owned, testable
- Backstory `lesson term` — Tone and judgment shaper for the Agent
- [[Concepts/Tool|Tool]] (as *@tool*) `lesson term` — Decorator that turns a function into a tool the Agent can call
- BaseTool `lesson term` — Class-based tool with args schema, retries, async support
- Entity memory `lesson term` — Memory scoped to a customer / account / issue
- [[Concepts/Long-term memory|Long-term memory]] `lesson term` — Vector-backed memory that survives between kickoffs
- Contextual memory `lesson term` — Memory pulled at the moment the Agent needs it
- [[Concepts/Manager LLM|Manager LLM]] `lesson term` — Extra LLM in Hierarchical process that picks the next task
- expected_output `lesson term` — String that tells the Agent (and audit) what shape to return

## Ships

- [[Artifacts/14-15 crew-or-flow|crew-or-flow]] `skill` — Pick CrewAI Crew or Flow for a given task, and scaffold the minimal implementation.

## Further reading

- [[Resources/Building Effective Agents|Building Effective Agents]] ([link](https://www.anthropic.com/research/building-effective-agents)) — when multi-agent helps and when it does not ·  also cited by 16 other lessons
- CrewAI Flows guide ([link](https://docs.crewai.com/en/concepts/flows)) — event-driven shape, `@start`, `@listen`
- CrewAI memory ([link](https://docs.crewai.com/en/concepts/memory)) — short-term, long-term, entity, contextual
- CrewAI tools reference ([link](https://docs.crewai.com/en/concepts/tools)) — `@tool`, `BaseTool`, built-in toolkits
- [[Resources/CrewAI docs introduction|CrewAI docs introduction]] ([link](https://docs.crewai.com/en/introduction)) — concepts and the recommended production path ·  also cited by 5 other lessons
- [[Resources/LangGraph Plan-and-Execute tutorial|LangGraph Plan-and-Execute tutorial]] ([link](https://docs.langchain.com/oss/python/langgraph/overview)) — the state-machine alternative ·  also cited by 9 other lessons


%% ── my notes ── %%
