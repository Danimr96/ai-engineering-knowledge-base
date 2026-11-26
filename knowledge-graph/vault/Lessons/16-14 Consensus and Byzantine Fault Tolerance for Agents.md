---
id: "lesson:16/14"
type: lesson
ref: 16/14
phase: 16
num: 14
title: Consensus and Byzantine Fault Tolerance for Agents
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
  - 16/14
  - 16-14
tags:
  - phase/16
  - type/learn+build
  - community/06
  - stdlib-only
source: ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/14-consensus-and-bft/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/14-consensus-and-bft"
---

# 16/14 Consensus and Byzantine Fault Tolerance for Agents

> Classical distributed-systems BFT meets stochastic LLMs. In 2025-2026 three research directions emerged: **CP-WBFT** (arXiv:2511.10400) weighs each vote by a confidence probe; **DecentLLMs** (arXiv:2507.14928) goes leaderless with parallel worker proposals and geometric-median aggregation; **WBFT** (arXiv:2505.05103) combines weighted voting with Hierarchical Structure Clustering to split Core and Edge nodes. The honest empirical result from "Can AI Agents Agree?" (arXiv:2603.01213) is that even scalar agreement is fragile today — a single deceptive agent can compromise a Mixture-of-Agents. BFT is necessary but not sufficient. This lesson builds a minimal BFT protocol, injects three agent-specific attacks (byzantine lie, sycophantic conformity, correlated-error monoculture), and measures how each consensus variant copes.

**Phase:** [[Phases/16 Multi-Agent & Swarms|Phase 16: Multi-Agent & Swarms]] · **Type:** Learn + Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/16-multi-agent-and-swarms/14-consensus-and-bft/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/14-consensus-and-bft) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/14-consensus-and-bft) · code: main.py  
**Community:** [[Communities/06 Communicative dehallucination · Consensus · Contract Net|06 Communicative dehallucination · Consensus · Contract Net]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 16 · 07 (Society of Mind and Debate), Phase 16 · 13 (Shared Memory)`

- [[Lessons/16-07 Society of Mind and Multi-Agent Debate|16/07 Society of Mind and Multi-Agent Debate]] — Society of Mind and Debate
- [[Lessons/16-13 Shared Memory and Blackboard Patterns|16/13 Shared Memory and Blackboard Patterns]] — Shared Memory

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/16-04 The Multi-Agent Primitive Model|16/04 The Multi-Agent Primitive Model]], [[Lessons/16-09 Parallel - Swarm - Networked Architectures|16/09 Parallel / Swarm / Networked Architectures]]
- depth 3: [[Lessons/16-01 Why Multi-Agent|16/01 Why Multi-Agent?]], [[Lessons/16-05 Supervisor - Orchestrator-Worker Pattern|16/05 Supervisor / Orchestrator-Worker Pattern]]

## Builds on this

- [[Lessons/16-15 Voting, Self-Consistency, and Debate Topology|16/15 Voting, Self-Consistency, and Debate Topology]]
- [[Lessons/16-19 Swarm Optimization for LLMs (PSO, ACO)|16/19 Swarm Optimization for LLMs (PSO, ACO)]]
- [[Lessons/16-23 Failure Modes — MAST, Groupthink, Monoculture, Cascading Errors|16/23 Failure Modes — MAST, Groupthink, Monoculture, Cascading Errors]]
- [[Lessons/16-25 Case Studies and the 2026 State of the Art|16/25 Case Studies and the 2026 State of the Art]]

## Concepts taught

- BFT `lesson term` — Castro-Liskov 1999 protocol for consensus with f < n/3 arbitrary faults.
- Byzantine `lesson term` — A node that can lie, drop messages, fail silently — anything but crash safely.
- Confidence probe `lesson term` — Self-reported or calibrator-predicted probability attached to a vote.
- Semantic clustering `lesson term` — Grouping equivalent answers before counting votes.
- Geometric median `lesson term` — The point minimizing sum of distances to sample points. Robust to outliers, unlike the mean.
- Monoculture `lesson term` — Correlated errors when agents share training data or base model.
- Sycophantic conformity `lesson term` — An agent's vote biases toward whoever spoke first/loudest.
- Core/Edge `lesson term` — WBFT split: small Core consensus first, Edge nodes follow. Bounds latency.

## Ships

- [[Artifacts/16-14 consensus-designer|consensus-designer]] `skill` — Design a BFT-aware consensus protocol for a multi-agent ensemble. Picks clustering, weighting, threshold, and escalation policy; attack-tests the design against byzantine, sycophancy, and monoculture patterns.

## Further reading

- WBFT — Weighted BFT with Hierarchical Structure Clustering ([link](https://arxiv.org/abs/2505.05103)) — Core/Edge split for bounded latency
- DecentLLMs — leaderless multi-agent consensus ([link](https://arxiv.org/abs/2507.14928)) — geometric-median aggregation
- CP-WBFT — Confidence-Probe Weighted BFT ([link](https://arxiv.org/abs/2511.10400)) — vote weighting by confidence
- Can AI Agents Agree? ([link](https://arxiv.org/abs/2603.01213)) — scalar-agreement fragility and deceptive-persona attack
- Castro & Liskov — Practical Byzantine Fault Tolerance (OSDI 1999) ([link](https://pmg.csail.mit.edu/papers/osdi99.pdf)) — the foundation


%% ── my notes ── %%
