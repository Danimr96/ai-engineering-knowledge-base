---
id: "lesson:14/05"
type: lesson
ref: 14/05
phase: 14
num: 5
title: "Self-Refine and CRITIC: Iterative Output Improvement"
lesson_type: build
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 7
code_files: 1
concepts: 8
prereqs: 2
community: 7
aliases:
  - 14/05
  - 14-05
tags:
  - phase/14
  - type/build
  - community/07
  - stdlib-only
source: ai-engineering-from-scratch/phases/14-agent-engineering/05-self-refine-and-critic/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/05-self-refine-and-critic"
---

# 14/05 Self-Refine and CRITIC: Iterative Output Improvement

> Self-Refine (Madaan et al., 2023) uses one LLM in three roles — generate, feedback, refine — in a loop. Average gain: +20 absolute on 7 tasks. CRITIC (Gou et al., 2023) hardens the feedback step by routing verification through external tools. In 2026 this pattern ships in every framework as "evaluator-optimizer" (Anthropic) or a guardrail loop (OpenAI Agents SDK).

**Phase:** [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] · **Type:** Build · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/14-agent-engineering/05-self-refine-and-critic/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/05-self-refine-and-critic) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/14-agent-engineering/05-self-refine-and-critic) · code: main.py · quiz: 7 questions  
**Community:** [[Communities/07 Swarm · Evaluator-Optimizer · Debate|07 Swarm · Evaluator-Optimizer · Debate]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 14 · 01 (Agent Loop), Phase 14 · 03 (Reflexion)`

- [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]] — Agent Loop
- [[Lessons/14-03 Reflexion- Verbal Reinforcement Learning|14/03 Reflexion: Verbal Reinforcement Learning]] — Reflexion

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/14-02 ReWOO and Plan-and-Execute- Decoupled Planning|14/02 ReWOO and Plan-and-Execute: Decoupled Planning]]

## Builds on this

- [[Lessons/14-25 Multi-Agent Debate and Collaboration|14/25 Multi-Agent Debate and Collaboration]]
- [[Lessons/14-26 Failure Modes- Why Agents Break|14/26 Failure Modes: Why Agents Break]]
- [[Lessons/14-30 Eval-Driven Agent Development|14/30 Eval-Driven Agent Development]]

## Concepts taught

- Self-Refine `lesson term` — Generate -> feedback -> refine loop in one model, with history
- [[Concepts/Critic|Critic]] `lesson term` — Replace feedback with an external verifier (search, code, calc, tests)
- [[Concepts/Evaluator-Optimizer|Evaluator-Optimizer]] `lesson term` — Two roles — evaluator scores, optimizer revises — looped to convergence
- Output guardrail `lesson term` — OpenAI Agents SDK validator that runs after an agent produces output
- Verify step `lesson term` — The load-bearing decision: grounded or self-rated
- Refine history `lesson term` — Prior outputs + critiques prepended to refine prompt; drop and quality collapses
- Rubber-stamp loop `lesson term` — Same-prompt critique returns "looks good"; fix with structurally different prompts
- [[Concepts/Stop condition|Stop condition]] `lesson term` — Verifier passes OR no feedback AND iteration cap; never single-condition

## Ships

- [[Artifacts/14-05 refine-loop|refine-loop]] `skill` — Configure an evaluator-optimizer (Self-Refine / CRITIC) loop given task, verifier availability, and iteration budget.

## Further reading

- [[Resources/Building Effective Agents|Building Effective Agents]] ([link](https://www.anthropic.com/research/building-effective-agents)) — evaluator-optimizer workflow pattern ·  also cited by 16 other lessons
- [[Resources/Madaan et al., Self-Refine (arXiv-2303.17651)|Madaan et al., Self-Refine (arXiv:2303.17651)]] ([link](https://arxiv.org/abs/2303.17651)) — the canonical paper ·  also cited by 3 other lessons
- Gou et al., CRITIC (arXiv:2305.11738) ([link](https://arxiv.org/abs/2305.11738)) — tool-grounded verification
- [[Resources/OpenAI Agents SDK docs|OpenAI Agents SDK docs]] ([link](https://openai.github.io/openai-agents-python/)) — output guardrails as CRITIC-shaped verifiers ·  also cited by 8 other lessons


%% ── my notes ── %%
