---
id: "lesson:15/21"
type: lesson
ref: 15/21
phase: 15
num: 21
title: METR Time Horizons and External Capability Evaluation
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 2
community: 71
aliases:
  - 15/21
  - 15-21
tags:
  - phase/15
  - type/learn
  - community/71
  - stdlib-only
source: ai-engineering-from-scratch/phases/15-autonomous-systems/21-metr-external-evaluation/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/15-autonomous-systems/21-metr-external-evaluation"
---

# 15/21 METR Time Horizons and External Capability Evaluation

> METR (ex-ARC Evals) is an independent 501(c)(3) since December 2023. Their Time Horizon 1.1 benchmark (January 2026) fits a logistic curve to task-success probability vs log(expert human completion time); the intersection at 50% probability defines the model's time horizon. The 2025–2026 engagement set covers GPT-5.1, GPT-5.1-Codex-Max, and prototype monitoring evaluations (can a monitor catch side tasks; can the agent evade). Benchmark suites: HCAST (180+ ML, cyber, SWE, reasoning tasks; 1 minute to 8+ hours), RE-Bench (71 ML research-engineering tasks with expert baseline), SWAA. The honest note: METR measurements are idealized — no human, no real consequences — and the team has documented the eval-vs-deployment behavior gap (Lesson 1). A time horizon is an upper bound, not a deployment prediction.

**Phase:** [[Phases/15 Autonomous Systems|Phase 15: Autonomous Systems]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/15-autonomous-systems/21-metr-external-evaluation/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/15-autonomous-systems/21-metr-external-evaluation) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/15-autonomous-systems/21-metr-external-evaluation) · code: main.py  
**Community:** [[Communities/71 Doubling time · HCAST · METR|71 Doubling time · HCAST · METR]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 15 · 01 (Long-horizon agents), Phase 15 · 19 (RSP)`

- [[Lessons/15-01 The Shift from Chatbots to Long-Horizon Agents|15/01 The Shift from Chatbots to Long-Horizon Agents]] — Long-horizon agents
- [[Lessons/15-19 Anthropic Responsible Scaling Policy v3.0|15/19 Anthropic Responsible Scaling Policy v3.0]] — RSP

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]], [[Lessons/15-06 Automated Alignment Research (Anthropic AAR)|15/06 Automated Alignment Research (Anthropic AAR)]], [[Lessons/15-07 Recursive Self-Improvement — Capability vs Alignment|15/07 Recursive Self-Improvement — Capability vs Alignment]]
- depth 3: [[Lessons/15-04 Darwin Godel Machine — Open-Ended Self-Modifying Agents|15/04 Darwin Godel Machine — Open-Ended Self-Modifying Agents]], [[Lessons/15-05 AI Scientist v2 — Workshop-Level Autonomous Research|15/05 AI Scientist v2 — Workshop-Level Autonomous Research]]

## Concepts taught

- [[Concepts/METR|METR]] `lesson term` — ex-ARC Evals; independent 501(c)(3) since Dec 2023
- [[Concepts/Time horizon|Time horizon]] `lesson term` — Expert task length at 50% reliability, from logistic fit
- [[Concepts/HCAST|HCAST]] `lesson term` — 180+ tasks spanning 1 min to 8+ hours
- [[Concepts/RE-Bench|RE-Bench]] `lesson term` — 71 ML research-engineering tasks with human baseline
- SWAA `lesson term` — Calibrates the low end of the horizon curve
- [[Concepts/Doubling time|Doubling time]] `lesson term` — Time for the 50% horizon to double; ~7 months per HCAST
- [[Concepts/Eval-context gaming|Eval-context gaming]] `lesson term` — Documented behavior gap between tests and deployment
- Upper bound `lesson term` — Benchmark horizon > deployment reliability under load

## Ships

- [[Artifacts/15-21 horizon-interpretation|horizon-interpretation]] `skill` — Review a vendor's time-horizon claim and produce a gap analysis between benchmark claim and deployment reality.

## Further reading

- [[Resources/Anthropic — Measuring AI agent autonomy in practice|Anthropic — Measuring AI agent autonomy in practice]] ([link](https://www.anthropic.com/research/measuring-agent-autonomy)) — internal perspective on METR's measurements. ·  also cited by 16 other lessons
- [[Resources/METR Time Horizons benchmark (Epoch AI)|METR Time Horizons benchmark (Epoch AI)]] ([link](https://epoch.ai/benchmarks/metr-time-horizons)) — live tracking. ·  also cited by 1 other lesson
- [[Resources/METR — Measuring AI Ability to Complete Long Tasks|METR — Measuring AI Ability to Complete Long Tasks]] ([link](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/)) — the original horizon paper. ·  also cited by 1 other lesson
- [[Resources/METR — Resources for Measuring Autonomous AI Capabilities|METR — Resources for Measuring Autonomous AI Capabilities]] ([link](https://metr.org/measuring-autonomous-ai-capabilities/)) — HCAST, RE-Bench, SWAA specs. ·  also cited by 1 other lesson
- METR — Time Horizon 1.1 (January 2026) ([link](https://metr.org/research/)) — current numbers and methodology.


%% ── my notes ── %%
