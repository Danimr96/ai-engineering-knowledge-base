---
id: "lesson:15/17"
type: lesson
ref: 15/17
phase: 15
num: 17
title: Constitutional AI and Rule Overrides
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 2
aliases:
  - 15/17
  - 15-17
tags:
  - phase/15
  - type/learn
  - stdlib-only
source: ai-engineering-from-scratch/phases/15-autonomous-systems/17-constitutional-ai/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/15-autonomous-systems/17-constitutional-ai"
---

# 15/17 Constitutional AI and Rule Overrides

> Anthropic's January 22, 2026 Claude Constitution runs 79 pages and is CC0. It moves from rule-based to reason-based alignment and establishes a four-tier priority hierarchy: (1) safety and supporting human oversight, (2) ethics, (3) Anthropic guidelines, (4) helpfulness. Behaviours split into hardcoded prohibitions (bioweapons uplift, CSAM) that operators and users cannot override and soft-coded defaults that operators can adjust within defined bounds. The 2022 original (Bai et al.) trained harmlessness via self-critique and RLAIF against a constitution. The honest caveat: reason-based alignment relies on the model generalising principles to unanticipated situations. Anthropic's own 2023 participatory experiment showed ~50% divergence between public-sourced and corporate principles; the 2026 version did not incorporate those findings.

**Phase:** [[Phases/15 Autonomous Systems|Phase 15: Autonomous Systems]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/15-autonomous-systems/17-constitutional-ai/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/15-autonomous-systems/17-constitutional-ai) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/15-autonomous-systems/17-constitutional-ai) · code: main.py  
**Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 15 · 06 (Automated alignment research), Phase 15 · 10 (Permission modes)`

- [[Lessons/15-06 Automated Alignment Research (Anthropic AAR)|15/06 Automated Alignment Research (Anthropic AAR)]] — Automated alignment research
- [[Lessons/15-10 Permission Modes for Autonomous Agents|15/10 Permission Modes for Autonomous Agents]] — Permission modes

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/15-01 The Shift from Chatbots to Long-Horizon Agents|15/01 The Shift from Chatbots to Long-Horizon Agents]], [[Lessons/15-04 Darwin Godel Machine — Open-Ended Self-Modifying Agents|15/04 Darwin Godel Machine — Open-Ended Self-Modifying Agents]], [[Lessons/15-05 AI Scientist v2 — Workshop-Level Autonomous Research|15/05 AI Scientist v2 — Workshop-Level Autonomous Research]], [[Lessons/15-09 The Autonomous Coding Agent Landscape (2026)|15/09 The Autonomous Coding Agent Landscape (2026)]]
- depth 3: [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]], [[Lessons/14-07 Agent Memory — Virtual Context and Memory Paging|14/07 Agent Memory — Virtual Context and Memory Paging]], [[Lessons/15-03 AlphaEvolve — Evolutionary Coding Agents|15/03 AlphaEvolve — Evolutionary Coding Agents]]

## Builds on this

- [[Lessons/15-18 Llama Guard and Input-Output Classification|15/18 Llama Guard and Input/Output Classification]]

## Concepts taught

- [[Concepts/Constitutional AI|Constitutional AI]] `lesson term` — Self-critique + RLAIF against a written constitution
- Reason-based alignment `lesson term` — Model reasons over principles to handle unseen cases
- Hardcoded prohibition `lesson term` — Rule-based prohibition no operator or user can override
- Soft-coded default `lesson term` — Behaviour within a declared bound, operator controls
- Four-tier hierarchy `lesson term` — safety > ethics > guidelines > helpfulness
- [[Concepts/RLAIF|RLAIF]] `lesson term` — RL where the reward comes from model-generated critiques
- Participatory constitution `lesson term` — 2023 Anthropic experiment; ~50% divergence from corporate
- Principle drift `lesson term` — Slow change in how the model reads a fixed principle text

## Ships

- [[Artifacts/15-17 constitution-review|constitution-review]] `skill` — Audit a deployment's constitutional layer — hardcoded prohibitions, soft-coded defaults, operator-adjustable bounds, and four-tier hierarchy resolution.

## Further reading

- [[Resources/Anthropic — Claude's Constitution (January 2026)|Anthropic — Claude's Constitution (January 2026)]] ([link](https://www.anthropic.com/news/claudes-constitution)) — the 79-page CC0 document. ·  also cited by 6 other lessons
- Anthropic — Collective Constitutional AI (2023) ([link](https://www.anthropic.com/research/collective-constitutional-ai-aligning-a-language-model-with-public-input)) — participatory experiment.
- Bai et al. — Constitutional AI: Harmlessness from AI Feedback ([link](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback)) — 2022 original.
- [[Resources/Anthropic — Measuring AI agent autonomy in practice|Anthropic — Measuring AI agent autonomy in practice]] ([link](https://www.anthropic.com/research/measuring-agent-autonomy)) — Constitution's role in long-horizon deployments. ·  also cited by 16 other lessons
- [[Resources/Anthropic — Responsible Scaling Policy v3.0 (Feb 2026)|Anthropic — Responsible Scaling Policy v3.0 (Feb 2026)]] ([link](https://anthropic.com/responsible-scaling-policy/rsp-v3-0)) — where the Constitution sits in the RSP stack. ·  also cited by 5 other lessons


%% ── my notes ── %%
