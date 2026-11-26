---
id: "lesson:16/09"
type: lesson
ref: 16/09
phase: 16
num: 9
title: Parallel / Swarm / Networked Architectures
lesson_type: learn+build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 2
community: 6
aliases:
  - 16/09
  - 16-09
tags:
  - phase/16
  - type/learn+build
  - community/06
  - stdlib-only
source: ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/09-parallel-swarm-networks/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/09-parallel-swarm-networks"
---

# 16/09 Parallel / Swarm / Networked Architectures

> Contrast with supervisor: no central decider. Agents read a shared event bus, pick up work asynchronously, write results back. LangGraph explicitly supports "Swarm Architecture" for decentralized, dynamic environments. Matrix (arXiv:2511.21686) represents both control and data flow as serialized messages passed through distributed queues to eliminate the orchestrator bottleneck. The tradeoff is explicit: determinism and traceability for scalability. Swarm fits tasks with many independent sub-problems; it does not fit tasks that need a single coherent plan.

**Phase:** [[Phases/16 Multi-Agent & Swarms|Phase 16: Multi-Agent & Swarms]] · **Type:** Learn + Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/16-multi-agent-and-swarms/09-parallel-swarm-networks/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/09-parallel-swarm-networks) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/09-parallel-swarm-networks) · code: main.py  
**Community:** [[Communities/06 Communicative dehallucination · Consensus · Contract Net|06 Communicative dehallucination · Consensus · Contract Net]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 16 · 05 (Supervisor Pattern), Phase 16 · 04 (Primitive Model)`

- [[Lessons/16-04 The Multi-Agent Primitive Model|16/04 The Multi-Agent Primitive Model]] — Primitive Model
- [[Lessons/16-05 Supervisor - Orchestrator-Worker Pattern|16/05 Supervisor / Orchestrator-Worker Pattern]] — Supervisor Pattern

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/16-01 Why Multi-Agent|16/01 Why Multi-Agent?]]

## Builds on this

- [[Lessons/16-13 Shared Memory and Blackboard Patterns|16/13 Shared Memory and Blackboard Patterns]]
- [[Lessons/16-16 Negotiation and Bargaining|16/16 Negotiation and Bargaining]]
- [[Lessons/16-19 Swarm Optimization for LLMs (PSO, ACO)|16/19 Swarm Optimization for LLMs (PSO, ACO)]]
- [[Lessons/16-20 MARL — MADDPG, QMIX, MAPPO|16/20 MARL — MADDPG, QMIX, MAPPO]]
- [[Lessons/16-21 Agent Economies, Token Incentives, Reputation|16/21 Agent Economies, Token Incentives, Reputation]]
- [[Lessons/16-22 Production Scaling — Queues, Checkpoints, Durability|16/22 Production Scaling — Queues, Checkpoints, Durability]]
- [[Lessons/16-25 Case Studies and the 2026 State of the Art|16/25 Case Studies and the 2026 State of the Art]]

## Concepts taught

- Swarm architecture `lesson term` — Workers pull from shared queue; no central orchestrator.
- Event bus `lesson term` — Message broker that routes tasks to workers by type or content.
- Starvation `lesson term` — Low-priority task never gets picked because higher-priority work arrives continuously.
- Hot-spotting `lesson term` — Load imbalance where one worker gets most tasks.
- Back-pressure `lesson term` — Mechanism that signals upstream to stop producing when the queue fills up.
- Idempotent worker `lesson term` — A task processed twice produces the same result. Required because workers may crash mid-run.
- Durable queue `lesson term` — Queue backed by disk or replicated storage; tasks are not lost when a worker crashes.
- Matrix framework `lesson term` — Both data and control flow are serialized messages on distributed queues.

## Ships

- [[Artifacts/16-09 swarm-fit|swarm-fit]] `skill` — Decide whether a task fits a swarm (decentralized) architecture or a supervisor (centralized) one.

## Further reading

- [[Resources/Anthropic engineering — How we built our multi-agent research system|Anthropic engineering — How we built our multi-agent research system]] ([link](https://www.anthropic.com/engineering/multi-agent-research-system)) — why a specific production system explicitly chose supervisor over swarm ·  also cited by 6 other lessons
- [[Resources/Matrix — A Decentralized Framework for Multi-Agent Systems|Matrix — A Decentralized Framework for Multi-Agent Systems]] ([link](https://arxiv.org/abs/2511.21686)) — full message-passing swarm ·  also cited by 2 other lessons
- [[Resources/LangGraph workflows and agents|LangGraph workflows and agents]] ([link](https://docs.langchain.com/oss/python/langgraph/workflows-agents)) — explicit swarm support ·  also cited by 4 other lessons
- [[Resources/AutoGen stable docs|AutoGen stable docs]] ([link](https://microsoft.github.io/autogen/stable/)) — the event-driven actor rewrite, closer to swarm than v0.2's GroupChat ·  also cited by 2 other lessons


%% ── my notes ── %%
