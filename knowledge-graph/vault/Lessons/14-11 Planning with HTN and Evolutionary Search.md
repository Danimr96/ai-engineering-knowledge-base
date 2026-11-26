---
id: "lesson:14/11"
type: lesson
ref: 14/11
phase: 14
num: 11
title: Planning with HTN and Evolutionary Search
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 7
code_files: 1
concepts: 7
prereqs: 1
community: 7
aliases:
  - 14/11
  - 14-11
tags:
  - phase/14
  - type/build
  - community/07
  - stdlib-only
source: ai-engineering-from-scratch/phases/14-agent-engineering/11-planning-htn-and-evolutionary/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/11-planning-htn-and-evolutionary"
---

# 14/11 Planning with HTN and Evolutionary Search

> Symbolic planning handles the cases where the plan is provably correct. Evolutionary code search handles the cases where the fitness function is machine-checkable. ChatHTN (2025) and AlphaEvolve (2025) show what each unlocks when paired with an LLM.

**Phase:** [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/14-agent-engineering/11-planning-htn-and-evolutionary/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/11-planning-htn-and-evolutionary) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/14-agent-engineering/11-planning-htn-and-evolutionary) · code: main.py · quiz: 7 questions  
**Community:** [[Communities/07 Swarm · Evaluator-Optimizer · Debate|07 Swarm · Evaluator-Optimizer · Debate]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 14 · 02 (ReWOO and Plan-and-Execute)`

- [[Lessons/14-02 ReWOO and Plan-and-Execute- Decoupled Planning|14/02 ReWOO and Plan-and-Execute: Decoupled Planning]] — ReWOO and Plan-and-Execute

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]]

## Builds on this

- [[Lessons/14-30 Eval-Driven Agent Development|14/30 Eval-Driven Agent Development]]

## Concepts taught

- HTN `lesson term` — Task decomposition with operators, preconditions, effects
- Method `lesson term` — Way to break a compound task into subtasks
- Operator `lesson term` — Concrete step with precondition and effect
- ChatHTN `lesson term` — Symbolic planner asks LLM when no method matches
- [[Concepts/AlphaEvolve|AlphaEvolve]] `lesson term` — Ensemble LLMs mutate code; deterministic evaluator selects
- Fitness function `lesson term` — Deterministic, machine-checkable score over outputs
- Online method learning `lesson term` — Store + generalize LLM plans to cut query cost

## Ships

- [[Artifacts/14-11 hybrid-planner|hybrid-planner]] `skill` — Build a hybrid planner — ChatHTN for provably-sound plans, AlphaEvolve for code search with a machine-checkable evaluator — and pick the right one for the problem.

## Further reading

- [[Resources/Building Effective Agents|Building Effective Agents]] ([link](https://www.anthropic.com/research/building-effective-agents)) — when to reach for a planner vs a simple loop ·  also cited by 16 other lessons
- Gopalakrishnan et al., ChatHTN (arXiv:2505.11814) ([link](https://arxiv.org/abs/2505.11814)) — symbolic + LLM hybrid planner
- [[Resources/AlphaEvolve (arXiv-2506.13131)|AlphaEvolve (arXiv:2506.13131)]] ([link](https://arxiv.org/abs/2506.13131)) — evolutionary code search with LLM mutations ·  also cited by 2 other lessons


%% ── my notes ── %%
