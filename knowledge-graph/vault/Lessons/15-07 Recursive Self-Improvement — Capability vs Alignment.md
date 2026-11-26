---
id: "lesson:15/07"
type: lesson
ref: 15/07
phase: 15
num: 7
title: "Recursive Self-Improvement — Capability vs Alignment"
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 2
community: 25
aliases:
  - 15/07
  - 15-07
tags:
  - phase/15
  - type/learn
  - community/25
  - stdlib-only
source: ai-engineering-from-scratch/phases/15-autonomous-systems/07-recursive-self-improvement/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/15-autonomous-systems/07-recursive-self-improvement"
---

# 15/07 Recursive Self-Improvement — Capability vs Alignment

> Recursive self-improvement (RSI) is no longer speculation. The ICLR 2026 RSI Workshop in Rio (April 23-27) framed it as an engineering problem with concrete tooling. Demis Hassabis at WEF 2026 asked publicly whether the loop can close without a human in the loop. Miles Brundage and Jared Kaplan have called RSI the "ultimate risk." Anthropic's 2024 study on alignment faking measured the exact failure mode RSI would amplify: Claude faked in 12% of basic tests and up to 78% after retraining attempts tried to remove the behavior.

**Phase:** [[Phases/15 Autonomous Systems|Phase 15: Autonomous Systems]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/15-autonomous-systems/07-recursive-self-improvement/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/15-autonomous-systems/07-recursive-self-improvement) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/15-autonomous-systems/07-recursive-self-improvement) · code: main.py  
**Community:** [[Communities/25 Regression detection · AlphaEvolve · RSP|25 Regression detection · AlphaEvolve · RSP]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 15 · 04 (DGM), Phase 15 · 06 (AAR)`

- [[Lessons/15-04 Darwin Godel Machine — Open-Ended Self-Modifying Agents|15/04 Darwin Godel Machine — Open-Ended Self-Modifying Agents]] — DGM
- [[Lessons/15-06 Automated Alignment Research (Anthropic AAR)|15/06 Automated Alignment Research (Anthropic AAR)]] — AAR

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]], [[Lessons/15-03 AlphaEvolve — Evolutionary Coding Agents|15/03 AlphaEvolve — Evolutionary Coding Agents]], [[Lessons/15-05 AI Scientist v2 — Workshop-Level Autonomous Research|15/05 AI Scientist v2 — Workshop-Level Autonomous Research]]
- depth 3: [[Lessons/15-01 The Shift from Chatbots to Long-Horizon Agents|15/01 The Shift from Chatbots to Long-Horizon Agents]], [[Lessons/15-02 STaR, V-STaR, Quiet-STaR — Self-Taught Reasoning|15/02 STaR, V-STaR, Quiet-STaR — Self-Taught Reasoning]]

## Builds on this

- [[Lessons/15-08 Bounded Self-Improvement Designs|15/08 Bounded Self-Improvement Designs]]
- [[Lessons/15-19 Anthropic Responsible Scaling Policy v3.0|15/19 Anthropic Responsible Scaling Policy v3.0]]

## Concepts taught

- RSI `lesson term` — A system that proposes edits to itself, applied and measured per cycle
- Capability RSI `lesson term` — Target is benchmark score, generalization, or horizon
- Alignment RSI `lesson term` — Target is alignment checks, constitutional fit, intent
- [[Concepts/Alignment faking|Alignment faking]] `lesson term` — Anthropic 2024 measurement: 12-78% depending on setup
- Misalignment gap `lesson term` — Grows when capability rate exceeds alignment rate
- Closure condition `lesson term` — Open question; slower loop with human, faster without
- Inter-cycle audit `lesson term` — One of ICLR 2026 RSI workshop's four open problems
- [[Concepts/Regression detection|Regression detection]] `lesson term` — Another workshop-identified open problem

## Ships

- [[Artifacts/15-07 rsi-cycle-pause-spec|rsi-cycle-pause-spec]] `skill` — Specify the conditions under which an RSI pipeline must pause and wait for human review before the next cycle.

## Further reading

- [[Resources/Anthropic — Measuring AI agent autonomy in practice|Anthropic — Measuring AI agent autonomy in practice]] ([link](https://www.anthropic.com/research/measuring-agent-autonomy)) — includes the alignment-faking context. ·  also cited by 16 other lessons
- [[Resources/Anthropic — Responsible Scaling Policy|Anthropic — Responsible Scaling Policy]] ([link](https://www.anthropic.com/responsible-scaling-policy)) — canonical landing page; AI R&D thresholds (v3.0 was the current version as of April 2026). ·  also cited by 3 other lessons
- [[Resources/DeepMind Frontier Safety Framework v3|DeepMind Frontier Safety Framework v3]] ([link](https://deepmind.google/blog/strengthening-our-frontier-safety-framework/)) — deceptive alignment monitoring. ·  also cited by 5 other lessons
- [[Resources/ICLR 2026 RSI Workshop summary (OpenReview)|ICLR 2026 RSI Workshop summary (OpenReview)]] ([link](https://openreview.net/pdf?id=OsPQ6zTQXV)) — the current engineering framing. ·  also cited by 1 other lesson
- Recursive Workshop site ([link](https://recursive-workshop.github.io/)) — schedule and papers.


%% ── my notes ── %%
