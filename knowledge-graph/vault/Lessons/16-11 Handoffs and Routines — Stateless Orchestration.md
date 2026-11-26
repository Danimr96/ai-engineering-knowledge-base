---
id: "lesson:16/11"
type: lesson
ref: 16/11
phase: 16
num: 11
title: "Handoffs and Routines — Stateless Orchestration"
lesson_type: learn+build
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
  - 16/11
  - 16-11
tags:
  - phase/16
  - type/learn+build
  - community/06
  - stdlib-only
source: ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/11-handoffs-and-routines/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/11-handoffs-and-routines"
---

# 16/11 Handoffs and Routines — Stateless Orchestration

> OpenAI's Swarm (October 2024) distilled multi-agent orchestration to two primitives: **routines** (instructions + tools as a system prompt) and **handoffs** (a tool that returns another Agent). No state machine, no branching DSL — the LLM routes by calling the right handoff tool. The OpenAI Agents SDK (March 2025) is the production successor. Swarm itself remains the cleanest conceptual reference — its entire source fits in a few hundred lines. The pattern is viral because the API surface is roughly "agent = prompt + tools; handoff = function returning agent." Limitation: stateless, so memory is the caller's problem.

**Phase:** [[Phases/16 Multi-Agent & Swarms|Phase 16: Multi-Agent & Swarms]] · **Type:** Learn + Build · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/16-multi-agent-and-swarms/11-handoffs-and-routines/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/11-handoffs-and-routines) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/11-handoffs-and-routines) · code: main.py  
**Community:** [[Communities/06 Communicative dehallucination · Consensus · Contract Net|06 Communicative dehallucination · Consensus · Contract Net]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 16 · 04 (Primitive Model)`

- [[Lessons/16-04 The Multi-Agent Primitive Model|16/04 The Multi-Agent Primitive Model]] — Primitive Model

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/16-01 Why Multi-Agent|16/01 Why Multi-Agent?]]

## Builds on this

- [[Lessons/16-25 Case Studies and the 2026 State of the Art|16/25 Case Studies and the 2026 State of the Art]]

## Concepts taught

- Routine `lesson term` — System prompt + tool list. Defines role and available handoffs.
- [[Concepts/Handoff|Handoff]] `glossary` — A tool the active agent can call that returns a new Agent. The runtime switches active agent.
- Stateless `lesson term` — Swarm does not persist anything; memory is the caller's responsibility.
- Active agent `lesson term` — The agent currently holding the conversation. Handoff changes this.
- Context transfer `lesson term` — Policy for what history the incoming agent sees: full, last N, or summarized.
- Handoff loop `lesson term` — Failure mode where two agents keep handing back to each other.
- OpenAI Agents SDK `lesson term` — March 2025 successor; adds sessions, guardrails, tracing on top of the handoff primitive.
- Handoff filter `lesson term` — SDK feature to inspect and modify context at the handoff boundary.

## Ships

- [[Artifacts/16-11 handoff-designer|handoff-designer]] `skill` — Design a handoff topology for a Swarm/Agents-SDK-style system: which agents exist, which handoffs they can call, what context transfers.

## Further reading

- [[Resources/OpenAI cookbook- Orchestrating Agents — Routines and Handoffs|OpenAI cookbook: Orchestrating Agents — Routines and Handoffs]] ([link](https://developers.openai.com/cookbook/examples/orchestrating_agents)) — the reference articulation ·  also cited by 2 other lessons
- [[Resources/Claude Code subagents documentation|Claude Code subagents documentation]] ([link](https://docs.anthropic.com/en/docs/claude-code)) — how Claude Code subagents use a handoff-like pattern via `Task` ·  also cited by 2 other lessons
- OpenAI Swarm repo ([link](https://github.com/openai/swarm)) — original implementation, kept as conceptual reference
- [[Resources/OpenAI Agents SDK docs|OpenAI Agents SDK docs]] ([link](https://openai.github.io/openai-agents-python/)) — production successor with sessions and tracing ·  also cited by 8 other lessons


%% ── my notes ── %%
