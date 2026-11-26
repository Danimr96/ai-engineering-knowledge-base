---
id: "lesson:14/25"
type: lesson
ref: 14/25
phase: 14
num: 25
title: Multi-Agent Debate and Collaboration
lesson_type: learn+build
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 7
code_files: 1
concepts: 6
prereqs: 2
community: 7
aliases:
  - 14/25
  - 14-25
tags:
  - phase/14
  - type/learn+build
  - community/07
  - stdlib-only
source: ai-engineering-from-scratch/phases/14-agent-engineering/25-multi-agent-debate/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/25-multi-agent-debate"
---

# 14/25 Multi-Agent Debate and Collaboration

> Du et al. (ICML 2024, "Society of Minds") run N model instances that independently propose answers, then iteratively critique each other over R rounds to converge. Improves factuality, rule-following, reasoning. Sparse topology beats full mesh on token cost.

**Phase:** [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] · **Type:** Learn + Build · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/14-agent-engineering/25-multi-agent-debate/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/25-multi-agent-debate) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/14-agent-engineering/25-multi-agent-debate) · code: main.py · quiz: 7 questions  
**Community:** [[Communities/07 Swarm · Evaluator-Optimizer · Debate|07 Swarm · Evaluator-Optimizer · Debate]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 14 · 12 (Workflow Patterns), Phase 14 · 05 (Self-Refine and CRITIC)`

- [[Lessons/14-05 Self-Refine and CRITIC- Iterative Output Improvement|14/05 Self-Refine and CRITIC: Iterative Output Improvement]] — Self-Refine and CRITIC
- [[Lessons/14-12 Anthropic's Workflow Patterns- Simple Over Complex|14/12 Anthropic's Workflow Patterns: Simple Over Complex]] — Workflow Patterns

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]], [[Lessons/14-03 Reflexion- Verbal Reinforcement Learning|14/03 Reflexion: Verbal Reinforcement Learning]]
- depth 3: [[Lessons/14-02 ReWOO and Plan-and-Execute- Decoupled Planning|14/02 ReWOO and Plan-and-Execute: Decoupled Planning]]

## Builds on this

- [[Lessons/14-28 Orchestration Patterns- Supervisor, Swarm, Hierarchical|14/28 Orchestration Patterns: Supervisor, Swarm, Hierarchical]]
- [[Lessons/14-30 Eval-Driven Agent Development|14/30 Eval-Driven Agent Development]]

## Concepts taught

- [[Concepts/Debate|Debate]] `lesson term` — N proposers, R rounds of cross-critique, converge
- Full mesh `lesson term` — Every debater reads every peer each round
- Sparse topology `lesson term` — Debaters read only a subset of peers
- Hub-and-spoke `lesson term` — One central debater, N-1 spokes read only the hub
- [[Concepts/Convergence|Convergence]] `lesson term` — Debaters converge on a shared answer
- Society of Minds `lesson term` — ICML 2024 multi-agent debate method

## Ships

- [[Artifacts/14-25 debate|debate]] `skill` — Scaffold a multi-agent debate with N debaters, R rounds, configurable topology (full mesh, star, ring), and a convergence rule.

## Further reading

- [[Resources/Building Effective Agents|Building Effective Agents]] ([link](https://www.anthropic.com/research/building-effective-agents)) — orchestrator-workers as a debate variant ·  also cited by 16 other lessons
- [[Resources/Madaan et al., Self-Refine (arXiv-2303.17651)|Madaan et al., Self-Refine (arXiv:2303.17651)]] ([link](https://arxiv.org/abs/2303.17651)) — single-model self-critique counterpart ·  also cited by 3 other lessons
- [[Resources/Du et al., Society of Minds (arXiv-2305.14325)|Du et al., Society of Minds (arXiv:2305.14325)]] ([link](https://arxiv.org/abs/2305.14325)) — canonical multi-agent debate ·  also cited by 3 other lessons
- Sparse Communication Topology (arXiv:2406.11776) ([link](https://arxiv.org/abs/2406.11776)) — sparse topology results


%% ── my notes ── %%
