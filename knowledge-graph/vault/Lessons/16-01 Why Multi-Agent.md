---
id: "lesson:16/01"
type: lesson
ref: 16/01
phase: 16
num: 1
title: "Why Multi-Agent?"
lesson_type: learn
languages:
  - TypeScript
time_min: 60
on_route: false
quiz_count: 5
code_files: 1
concepts: 7
prereqs: 0
community: 6
aliases:
  - 16/01
  - 16-01
tags:
  - phase/16
  - type/learn
  - community/06
source: ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/01-why-multi-agent/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/01-why-multi-agent"
---

# 16/01 Why Multi-Agent?

> One agent hits a wall. The smart move is not a bigger agent - it is more agents.

**Phase:** [[Phases/16 Multi-Agent & Swarms|Phase 16: Multi-Agent & Swarms]] · **Type:** Learn · **Time:** 60 min · **Languages:** TypeScript · **Status:** —  
**Open:** [[Upstream/16-multi-agent-and-swarms/01-why-multi-agent/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/01-why-multi-agent) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/01-why-multi-agent) · code: single_vs_multi.ts · quiz: 5 questions  
**Community:** [[Communities/06 Communicative dehallucination · Consensus · Contract Net|06 Communicative dehallucination · Consensus · Contract Net]]  

## Prerequisites

Stated upstream: `Phase 14 (Agent Engineering)`

- Whole phase: [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] — Agent Engineering ·  medium confidence

## Builds on this

- [[Lessons/16-02 Heritage of FIPA-ACL and Speech Acts|16/02 Heritage of FIPA-ACL and Speech Acts]]
- [[Lessons/16-03 Communication Protocols|16/03 Communication Protocols]]
- [[Lessons/16-04 The Multi-Agent Primitive Model|16/04 The Multi-Agent Primitive Model]]
- [[Lessons/16-25 Case Studies and the 2026 State of the Art|16/25 Case Studies and the 2026 State of the Art]]

## Concepts taught

- [[Concepts/Swarm|Swarm]] `glossary` — A set of peer agents with shared state and no fixed leader. Behavior emerges from local interactions.
- [[Concepts/Orchestrator|Orchestrator]] `lesson term` — An agent whose tools include spawning and managing other agents. It plans and delegates but may not do the actual work.
- Coordinator `lesson term` — A non-agent component (often just code, not an LLM) that routes messages between agents based on rules.
- [[Concepts/Consensus|Consensus]] `lesson term` — A protocol where multiple agents must reach agreement before proceeding. Used when conflicting outputs need resolution.
- Emergent behavior `lesson term` — System-level patterns that arise from agent interactions but were not explicitly programmed. Can be useful or harmful.
- Fan-out / fan-in `lesson term` — Splitting a task across parallel agents (fan-out), then combining their results (fan-in).
- [[Concepts/Message passing|Message passing]] `lesson term` — The communication mechanism between agents: structured data sent from one agent to another, replacing shared context windows.

## Ships

- [[Artifacts/16-01 prompt-multi-agent-decision|prompt-multi-agent-decision]] `prompt` — Decide whether a task needs a multi-agent system or a single agent

## Further reading

- [[Resources/AutoGen|AutoGen]] ([link](https://arxiv.org/abs/2308.08155)) — Microsoft's multi-agent conversation framework ·  also cited by 1 other lesson
- The Landscape of Emerging AI Agent Architectures ([link](https://arxiv.org/abs/2409.02977)) — survey of multi-agent patterns
- [[Resources/Claude Code subagents documentation|Claude Code subagents documentation]] ([link](https://docs.anthropic.com/en/docs/claude-code)) — how Claude Code delegates with Task ·  also cited by 2 other lessons
- [[Resources/CrewAI documentation|CrewAI documentation]] ([link](https://docs.crewai.com/)) — role-based multi-agent framework ·  also cited by 1 other lesson


%% ── my notes ── %%
