---
id: "lesson:14/02"
type: lesson
ref: 14/02
phase: 14
num: 2
title: "ReWOO and Plan-and-Execute: Decoupled Planning"
lesson_type: build
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 7
code_files: 1
concepts: 7
prereqs: 1
community: 7
aliases:
  - 14/02
  - 14-02
tags:
  - phase/14
  - type/build
  - community/07
  - stdlib-only
source: ai-engineering-from-scratch/phases/14-agent-engineering/02-rewoo-plan-and-execute/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/02-rewoo-plan-and-execute"
---

# 14/02 ReWOO and Plan-and-Execute: Decoupled Planning

> ReAct interleaves thought and action in one stream. ReWOO separates them: one big plan up front, then execute. 5x fewer tokens, +4% accuracy on HotpotQA, and you can distill the planner into a 7B model. Plan-and-Execute generalized it; Plan-and-Act scaled it to web navigation.

**Phase:** [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] · **Type:** Build · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/14-agent-engineering/02-rewoo-plan-and-execute/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/02-rewoo-plan-and-execute) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/14-agent-engineering/02-rewoo-plan-and-execute) · code: main.py · quiz: 7 questions  
**Community:** [[Communities/07 Swarm · Evaluator-Optimizer · Debate|07 Swarm · Evaluator-Optimizer · Debate]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 14 · 01 (Agent Loop)`

- [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]] — Agent Loop

## Builds on this

- [[Lessons/14-03 Reflexion- Verbal Reinforcement Learning|14/03 Reflexion: Verbal Reinforcement Learning]]
- [[Lessons/14-11 Planning with HTN and Evolutionary Search|14/11 Planning with HTN and Evolutionary Search]]
- [[Lessons/14-30 Eval-Driven Agent Development|14/30 Eval-Driven Agent Development]]

## Concepts taught

- ReWOO `lesson term` — Plan, then fetch evidence in parallel, then solve — no observations in the planning prompt
- Plan-and-Execute `lesson term` — ReWOO with an optional replanner node after execution
- Plan-and-Act `lesson term` — Explicit planner/executor split with synthetic plan training data for long-horizon tasks
- Evidence reference `lesson term` — Plan-node placeholder substituted with prior worker output at dispatch time
- Planner distillation `lesson term` — Fine-tune a small model on planner traces from a large teacher
- Token efficiency `lesson term` — 5x fewer tokens on HotpotQA vs ReAct in the paper
- DAG executor `lesson term` — Runs plan nodes in dependency order; parallel at each level

## Ships

- [[Artifacts/14-02 rewoo-planner|rewoo-planner]] `skill` — Generate a validated ReWOO plan DAG from a user request and tool catalog.

## Further reading

- [[Resources/Building Effective Agents|Building Effective Agents]] ([link](https://www.anthropic.com/research/building-effective-agents)) — pick the simplest pattern that works ·  also cited by 16 other lessons
- Xu et al., ReWOO: Decoupling Reasoning from Observations (arXiv:2305.18323) ([link](https://arxiv.org/abs/2305.18323)) — the canonical paper
- Erdogan et al., Plan-and-Act (arXiv:2503.09572) ([link](https://arxiv.org/abs/2503.09572)) — scaled planner-executor with synthetic plans
- [[Resources/LangGraph Plan-and-Execute tutorial|LangGraph Plan-and-Execute tutorial]] ([link](https://docs.langchain.com/oss/python/langgraph/overview)) — the framework recipe ·  also cited by 9 other lessons


%% ── my notes ── %%
