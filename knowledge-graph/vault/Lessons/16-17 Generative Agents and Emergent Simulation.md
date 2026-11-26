---
id: "lesson:16/17"
type: lesson
ref: 16/17
phase: 16
num: 17
title: Generative Agents and Emergent Simulation
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
  - 16/17
  - 16-17
tags:
  - phase/16
  - type/learn+build
  - community/06
  - stdlib-only
source: ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/17-generative-agents-simulation/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/17-generative-agents-simulation"
---

# 16/17 Generative Agents and Emergent Simulation

> Park et al. 2023 (UIST '23, arXiv:2304.03442) populated **Smallville**, a sandbox of 25 agents, with a three-part architecture: **memory stream** (natural-language log), **reflection** (higher-level syntheses the agent generates about its own stream), and **plan** (day-level behavior, then sub-plans). The landmark result was the Valentine's Day party emergence: one agent seeded with "wants to throw a Valentine's Day party," without further scripting, produced invitations spread through the population, coordinated dates, and the party happened — from 24 agents who started with no knowledge of it. Ablations show all three components are required for believability. The documented failures are spatial-norm errors (entering closed stores, sharing single-person bathrooms). This is the reference architecture for agent simulations and multi-agent social evaluation in 2026.

**Phase:** [[Phases/16 Multi-Agent & Swarms|Phase 16: Multi-Agent & Swarms]] · **Type:** Learn + Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/16-multi-agent-and-swarms/17-generative-agents-simulation/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/17-generative-agents-simulation) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/17-generative-agents-simulation) · code: main.py  
**Community:** [[Communities/06 Communicative dehallucination · Consensus · Contract Net|06 Communicative dehallucination · Consensus · Contract Net]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 16 · 04 (Primitive Model), Phase 16 · 13 (Shared Memory)`

- [[Lessons/16-04 The Multi-Agent Primitive Model|16/04 The Multi-Agent Primitive Model]] — Primitive Model
- [[Lessons/16-13 Shared Memory and Blackboard Patterns|16/13 Shared Memory and Blackboard Patterns]] — Shared Memory

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/16-01 Why Multi-Agent|16/01 Why Multi-Agent?]], [[Lessons/16-09 Parallel - Swarm - Networked Architectures|16/09 Parallel / Swarm / Networked Architectures]]
- depth 3: [[Lessons/16-05 Supervisor - Orchestrator-Worker Pattern|16/05 Supervisor / Orchestrator-Worker Pattern]]

## Builds on this

- [[Lessons/16-18 Theory of Mind and Emergent Coordination|16/18 Theory of Mind and Emergent Coordination]]
- [[Lessons/16-25 Case Studies and the 2026 State of the Art|16/25 Case Studies and the 2026 State of the Art]]

## Concepts taught

- Memory stream `lesson term` — Append-only log of observations, actions, reflections, plans.
- Recency `lesson term` — Exponential-decay score by age.
- Importance `lesson term` — Self-rated 1-10 at write time. Cached.
- Relevance `lesson term` — Cosine similarity (embedding-based).
- [[Concepts/Reflection|Reflection]] `lesson term` — Synthesis generated from recent memories, re-ingested as a new memory.
- Plan `lesson term` — Top-down plan tree. Revisable when observations contradict.
- Smallville `lesson term` — 25-agent simulation that produced the Valentine's Day emergence.
- Believability `lesson term` — Human-rater score for whether behavior seems like a plausible agent.

## Ships

- [[Artifacts/16-17 simulation-designer|simulation-designer]] `skill` — Design a generative-agent simulation (Smallville-style) for a given scenario. Specifies memory schema, reflection cadence, plan horizon, spatial/social constraints, and evaluation metrics.

## Further reading

- [[Resources/Generative Agents|Generative Agents]] ([link](https://arxiv.org/abs/2304.03442)) — the reference architecture ·  also cited by 1 other lesson
- UIST '23 paper page ([link](https://dl.acm.org/doi/10.1145/3586183.3606763)) — publication venue
- Smallville code release ([link](https://github.com/joonspk-research/generative_agents)) — reference Python implementation
- Hayes-Roth 1985 — A Blackboard Architecture for Control ([link](https://www.sciencedirect.com/science/article/abs/pii/0004370285900639)) — prior art for structured-memory agents


%% ── my notes ── %%
