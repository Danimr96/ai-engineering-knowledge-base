---
id: "lesson:16/15"
type: lesson
ref: 16/15
phase: 16
num: 15
title: "Voting, Self-Consistency, and Debate Topology"
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
  - 16/15
  - 16-15
tags:
  - phase/16
  - type/learn+build
  - community/06
  - stdlib-only
source: ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/15-voting-debate-topology/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/15-voting-debate-topology"
---

# 16/15 Voting, Self-Consistency, and Debate Topology

> The cheapest aggregation: sample N independent agents, majority-vote. Wang et al. 2022 self-consistency did this with one model sampled N times. Multi-agent extends it with **heterogeneous** agents to escape monoculture — different models, different prompts, different temperatures, different contexts. Beyond majority vote, debate topology matters: MultiAgentBench (arXiv:2503.01935, ACL 2025) evaluated star / chain / tree / graph coordination and found **graph best for research**, with a "coordination tax" past ~4 agents. AgentVerse (ICLR 2024) documents two emergent patterns — volunteer behaviors and conformity behaviors — and conformity is both a feature (finding consensus) and a risk (groupthink, Lesson 24). This lesson maps the topology space, builds each variant, and measures the coordination tax.

**Phase:** [[Phases/16 Multi-Agent & Swarms|Phase 16: Multi-Agent & Swarms]] · **Type:** Learn + Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/16-multi-agent-and-swarms/15-voting-debate-topology/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/15-voting-debate-topology) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/15-voting-debate-topology) · code: main.py  
**Community:** [[Communities/06 Communicative dehallucination · Consensus · Contract Net|06 Communicative dehallucination · Consensus · Contract Net]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 16 · 07 (Society of Mind and Debate), Phase 16 · 14 (Consensus and BFT)`

- [[Lessons/16-07 Society of Mind and Multi-Agent Debate|16/07 Society of Mind and Multi-Agent Debate]] — Society of Mind and Debate
- [[Lessons/16-14 Consensus and Byzantine Fault Tolerance for Agents|16/14 Consensus and Byzantine Fault Tolerance for Agents]] — Consensus and BFT

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/16-04 The Multi-Agent Primitive Model|16/04 The Multi-Agent Primitive Model]], [[Lessons/16-13 Shared Memory and Blackboard Patterns|16/13 Shared Memory and Blackboard Patterns]]
- depth 3: [[Lessons/16-01 Why Multi-Agent|16/01 Why Multi-Agent?]], [[Lessons/16-09 Parallel - Swarm - Networked Architectures|16/09 Parallel / Swarm / Networked Architectures]]

## Builds on this

- [[Lessons/16-23 Failure Modes — MAST, Groupthink, Monoculture, Cascading Errors|16/23 Failure Modes — MAST, Groupthink, Monoculture, Cascading Errors]]
- [[Lessons/16-24 Evaluation and Coordination Benchmarks|16/24 Evaluation and Coordination Benchmarks]]
- [[Lessons/16-25 Case Studies and the 2026 State of the Art|16/25 Case Studies and the 2026 State of the Art]]

## Concepts taught

- [[Concepts/Self-Consistency|Self-Consistency]] `lesson term` — Wang 2022. Single model, N temperature>0 samples, majority vote on reasoning paths.
- Heterogeneity `lesson term` — Ensemble of different base models or prompt families. Breaks monoculture.
- MAD `lesson term` — Generic term for agents exchanging critiques over rounds. See Du 2023.
- A-HMAD `lesson term` — MAD variant emphasizing different models + adversarial structure.
- Topology `lesson term` — Star, chain, tree, graph. Determines information flow.
- Coordination tax `lesson term` — Above ~4 agents on graph, cost grows faster than quality.
- Volunteer behavior `lesson term` — AgentVerse emergent pattern: an agent offers to take a step.
- Conformity behavior `lesson term` — AgentVerse emergent pattern: an agent aligns with a critic.
- Jury `lesson term` — Sibyl-style ensemble with roles (examiner, context, scorer).

## Ships

- [[Artifacts/16-15 topology-picker|topology-picker]] `skill` — Pick a multi-agent debate topology (star / chain / tree / graph), an N of agents, a heterogeneity profile, and a round bound for a given task.

## Further reading

- [[Resources/Self-Consistency Improves Chain of Thought Reasoning in Language Models|Self-Consistency Improves Chain of Thought Reasoning in Language Models]] ([link](https://arxiv.org/abs/2203.11171)) — single-model baseline ·  also cited by 1 other lesson
- [[Resources/Du et al., Society of Minds (arXiv-2305.14325)|Du et al., Society of Minds (arXiv:2305.14325)]] ([link](https://arxiv.org/abs/2305.14325)) — both agents AND rounds matter independently ·  also cited by 3 other lessons
- [[Resources/Should we be going MAD- A Look at Multi-Agent Debate Strategies for LLMs|Should we be going MAD? A Look at Multi-Agent Debate Strategies for LLMs]] ([link](https://arxiv.org/abs/2311.17371)) — MAD-strategy survey; finds MAD often loses to self-consistency at equal budget ·  also cited by 1 other lesson
- [[Resources/MultiAgentBench - MARBLE|MultiAgentBench / MARBLE]] ([link](https://arxiv.org/abs/2503.01935)) — topology benchmark showing graph best for research, chain for pipelines ·  also cited by 1 other lesson
- [[Resources/MARBLE repo|MARBLE repo]] ([link](https://github.com/ulab-uiuc/MARBLE)) — reference benchmark implementation ·  also cited by 1 other lesson
- AgentVerse (ICLR 2024) ([link](https://proceedings.iclr.cc/paper_files/paper/2024/file/578e65cdee35d00c708d4c64bce32971-Paper-Conference.pdf)) — volunteer and conformity emergent patterns


%% ── my notes ── %%
