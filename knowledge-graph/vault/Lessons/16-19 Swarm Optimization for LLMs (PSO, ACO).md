---
id: "lesson:16/19"
type: lesson
ref: 16/19
phase: 16
num: 19
title: "Swarm Optimization for LLMs (PSO, ACO)"
lesson_type: learn+build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 0
code_files: 1
concepts: 9
prereqs: 2
community: 6
aliases:
  - 16/19
  - 16-19
tags:
  - phase/16
  - type/learn+build
  - community/06
  - stdlib-only
source: ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/19-swarm-optimization-pso-aco/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/19-swarm-optimization-pso-aco"
---

# 16/19 Swarm Optimization for LLMs (PSO, ACO)

> Bio-inspired optimization is making an LLM comeback. **LMPSO** (arXiv:2504.09247) uses PSO where each particle's velocity is a prompt and the LLM generates the next candidate; works well on structured-sequence outputs (math expressions, programs). **Model Swarms** (arXiv:2410.11163) treats each LLM expert as a PSO particle on a model-weight manifold and reports **13.3% average gain** over 12 baselines on 9 datasets with just 200 instances. **SwarmPrompt** (ICAART 2025) hybridizes PSO + Grey Wolf for prompt optimization. **AMRO-S** (arXiv:2603.12933) is ACO-inspired pheromone specialists for multi-agent LLM routing — **4.7x speedup**, interpretable routing evidence, quality-gated asynchronous update that decouples inference from learning. This lesson implements PSO on prompt parameter space and ACO on agent routing, measures why these classical algorithms fit the LLM era, and when they do not.

**Phase:** [[Phases/16 Multi-Agent & Swarms|Phase 16: Multi-Agent & Swarms]] · **Type:** Learn + Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/16-multi-agent-and-swarms/19-swarm-optimization-pso-aco/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/19-swarm-optimization-pso-aco) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/19-swarm-optimization-pso-aco) · code: main.py  
**Community:** [[Communities/06 Communicative dehallucination · Consensus · Contract Net|06 Communicative dehallucination · Consensus · Contract Net]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 16 · 09 (Parallel Swarm Networks), Phase 16 · 14 (Consensus and BFT)`

- [[Lessons/16-09 Parallel - Swarm - Networked Architectures|16/09 Parallel / Swarm / Networked Architectures]] — Parallel Swarm Networks
- [[Lessons/16-14 Consensus and Byzantine Fault Tolerance for Agents|16/14 Consensus and Byzantine Fault Tolerance for Agents]] — Consensus and BFT

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/16-04 The Multi-Agent Primitive Model|16/04 The Multi-Agent Primitive Model]], [[Lessons/16-05 Supervisor - Orchestrator-Worker Pattern|16/05 Supervisor / Orchestrator-Worker Pattern]], [[Lessons/16-07 Society of Mind and Multi-Agent Debate|16/07 Society of Mind and Multi-Agent Debate]], [[Lessons/16-13 Shared Memory and Blackboard Patterns|16/13 Shared Memory and Blackboard Patterns]]
- depth 3: [[Lessons/16-01 Why Multi-Agent|16/01 Why Multi-Agent?]]

## Builds on this

- [[Lessons/16-25 Case Studies and the 2026 State of the Art|16/25 Case Studies and the 2026 State of the Art]]

## Concepts taught

- PSO `lesson term` — Kennedy-Eberhart 1995. Population-based gradient-free optimizer.
- ACO `lesson term` — Dorigo 1992. Path/route optimization via pheromone trails.
- LMPSO `lesson term` — arXiv:2504.09247. Velocity is a prompt; LLM produces candidates.
- Model Swarms `lesson term` — arXiv:2410.11163. Gradient-free update on model parameter subspace.
- AMRO-S `lesson term` — arXiv:2603.12933. Pheromone matrix over task-type × agent.
- p_best / g_best `lesson term` — Per-particle and swarm-wide best solutions found so far.
- Pheromone `lesson term` — Strength on an edge; decays over time; deposits on quality.
- Quality-gated update `lesson term` — Pheromone deposit conditioned on quality check.
- Catastrophic drift `lesson term` — Fitness landscape changes; old p_best and pheromones become stale.

## Ships

- [[Artifacts/16-19 swarm-optimizer|swarm-optimizer]] `skill` — Choose between PSO, ACO, genetic algorithms, and gradient-based optimizers for a given LLM or agent optimization problem. Bio-inspired swarm algorithms are gradient-free and suit LLM-era workloads where the search space is discrete or the fitness function is black-box.

## Further reading

- Dorigo — Ant Colony Optimization ([link](https://www.aco-metaheuristic.org/about.html)) — 1992 ACO foundations
- Model Swarms — gradient-free LLM expert optimization ([link](https://arxiv.org/abs/2410.11163)) — PSO on model-weight subspace
- LMPSO — Language Model Particle Swarm Optimization ([link](https://arxiv.org/abs/2504.09247)) — PSO for structured LLM outputs
- AMRO-S — ant-colony multi-agent routing ([link](https://arxiv.org/abs/2603.12933)) — pheromone-driven routing with quality gate
- Kennedy & Eberhart — Particle Swarm Optimization ([link](https://ieeexplore.ieee.org/document/488968)) — the 1995 PSO paper


%% ── my notes ── %%
