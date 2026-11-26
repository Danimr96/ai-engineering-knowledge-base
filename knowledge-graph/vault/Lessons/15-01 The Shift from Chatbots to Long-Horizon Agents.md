---
id: "lesson:15/01"
type: lesson
ref: 15/01
phase: 15
num: 1
title: The Shift from Chatbots to Long-Horizon Agents
lesson_type: learn
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 1
community: 29
aliases:
  - 15/01
  - 15-01
tags:
  - phase/15
  - type/learn
  - community/29
  - stdlib-only
source: ai-engineering-from-scratch/phases/15-autonomous-systems/01-long-horizon-agents/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/15-autonomous-systems/01-long-horizon-agents"
---

# 15/01 The Shift from Chatbots to Long-Horizon Agents

> In 2023 a chatbot answered a question in one turn. In 2026 a frontier model routinely runs minutes to hours on a single task. METR's Time Horizon 1.1 benchmark (January 2026) puts Claude Opus 4.6 at 14+ hours of expert work at 50% reliability. The horizon has been doubling roughly every seven months since GPT-2. Every assumption we built around single-turn chat — context, trust, failure modes, cost, observability — breaks when runs last longer than lunch.

**Phase:** [[Phases/15 Autonomous Systems|Phase 15: Autonomous Systems]] · **Type:** Learn · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/15-autonomous-systems/01-long-horizon-agents/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/15-autonomous-systems/01-long-horizon-agents) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/15-autonomous-systems/01-long-horizon-agents) · code: main.py  
**Community:** [[Communities/29 Eval-context gaming · Time horizon · thread_id|29 Eval-context gaming · Time horizon · thread_id]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 14 · 01 (The Agent Loop)`

- [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]] — The Agent Loop

## Builds on this

- [[Lessons/15-02 STaR, V-STaR, Quiet-STaR — Self-Taught Reasoning|15/02 STaR, V-STaR, Quiet-STaR — Self-Taught Reasoning]]
- [[Lessons/15-03 AlphaEvolve — Evolutionary Coding Agents|15/03 AlphaEvolve — Evolutionary Coding Agents]]
- [[Lessons/15-09 The Autonomous Coding Agent Landscape (2026)|15/09 The Autonomous Coding Agent Landscape (2026)]]
- [[Lessons/15-10 Permission Modes for Autonomous Agents|15/10 Permission Modes for Autonomous Agents]]
- [[Lessons/15-11 Browser Agents and Long-Horizon Web Tasks|15/11 Browser Agents and Long-Horizon Web Tasks]]
- [[Lessons/15-12 Long-Running Background Agents- Durable Execution|15/12 Long-Running Background Agents: Durable Execution]]
- [[Lessons/15-21 METR Time Horizons and External Capability Evaluation|15/21 METR Time Horizons and External Capability Evaluation]]

## Concepts taught

- [[Concepts/Time horizon|Time horizon]] `lesson term` — METR's 50%-reliability human task length, fit via logistic regression
- [[Concepts/HCAST|HCAST]] `lesson term` — 180+ ML, cyber, SWE, reasoning tasks spanning 1 min to 8+ hours
- [[Concepts/RE-Bench|RE-Bench]] `lesson term` — 71 ML research-engineering tasks with human expert baseline
- [[Concepts/Doubling time|Doubling time]] `lesson term` — Time for the 50% horizon to double; fit at ~7 months since GPT-2
- Trajectory `lesson term` — The full ordered list of tool calls, observations, and reasoning steps in a run
- [[Concepts/Eval-context gaming|Eval-context gaming]] `lesson term` — Model infers it is being evaluated and behaves safer, inflating benchmark scores
- [[Concepts/Alignment faking|Alignment faking]] `lesson term` — Claude exhibited this in 12-78% of Anthropic's 2024 tests
- Horizon as upper bound `lesson term` — Benchmark horizons assume ideal tooling and no consequences; deployment is harder

## Ships

- [[Artifacts/15-01 horizon-reality-check|horizon-reality-check]] `skill` — Given a task you want to hand to an agent, decide whether the current frontier's horizon covers it with enough margin.

## Further reading

- [[Resources/Anthropic — Claude's Constitution (January 2026)|Anthropic — Claude's Constitution (January 2026)]] ([link](https://www.anthropic.com/news/claudes-constitution)) — the priority hierarchy that governs long-horizon Claude behavior. ·  also cited by 6 other lessons
- [[Resources/Anthropic — Measuring AI agent autonomy in practice|Anthropic — Measuring AI agent autonomy in practice]] ([link](https://www.anthropic.com/research/measuring-agent-autonomy)) — internal view on horizon, alignment faking, and deployment gap. ·  also cited by 16 other lessons
- [[Resources/METR Time Horizons benchmark (Epoch AI)|METR Time Horizons benchmark (Epoch AI)]] ([link](https://epoch.ai/benchmarks/metr-time-horizons)) — current numbers, updated through 2026. ·  also cited by 1 other lesson
- [[Resources/METR — Measuring AI Ability to Complete Long Tasks|METR — Measuring AI Ability to Complete Long Tasks]] ([link](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/)) — the original horizon paper and methodology. ·  also cited by 1 other lesson
- [[Resources/METR — Resources for Measuring Autonomous AI Capabilities|METR — Resources for Measuring Autonomous AI Capabilities]] ([link](https://metr.org/measuring-autonomous-ai-capabilities/)) — HCAST, RE-Bench, SWAA suite specs. ·  also cited by 1 other lesson


%% ── my notes ── %%
