---
id: "lesson:15/19"
type: lesson
ref: 15/19
phase: 15
num: 19
title: Anthropic Responsible Scaling Policy v3.0
lesson_type: learn
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 2
community: 25
aliases:
  - 15/19
  - 15-19
tags:
  - phase/15
  - type/learn
  - community/25
  - stdlib-only
source: ai-engineering-from-scratch/phases/15-autonomous-systems/19-anthropic-rsp/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/15-autonomous-systems/19-anthropic-rsp"
---

# 15/19 Anthropic Responsible Scaling Policy v3.0

> RSP v3.0 went into effect February 24, 2026, replacing the 2023 policy. Two-tier mitigation: what Anthropic will do unilaterally vs what is framed as an industry-wide recommendation (including RAND SL-4 security standards). Adds Frontier Safety Roadmaps and Risk Reports as standing documents rather than one-off deliverables. Drops the 2023 pause commitment. Introduces the AI R&D-4 threshold: once crossed, Anthropic must publish an affirmative case identifying misalignment risks and mitigations. Claude Opus 4.6 does not cross it. Anthropic states in the v3.0 announcement that "confidently ruling this out is becoming difficult." SaferAI rated the 2023 RSP at 2.2; they downgraded v3.0 to 1.9, putting Anthropic in the "weak" RSP category alongside OpenAI and DeepMind. Qualitative thresholds replaced the 2023 quantitative commitments; removing the pause clause is the sharpest regression.

**Phase:** [[Phases/15 Autonomous Systems|Phase 15: Autonomous Systems]] · **Type:** Learn · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/15-autonomous-systems/19-anthropic-rsp/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/15-autonomous-systems/19-anthropic-rsp) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/15-autonomous-systems/19-anthropic-rsp) · code: main.py  
**Community:** [[Communities/25 Regression detection · AlphaEvolve · RSP|25 Regression detection · AlphaEvolve · RSP]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 15 · 06 (AAR), Phase 15 · 07 (RSI)`

- [[Lessons/15-06 Automated Alignment Research (Anthropic AAR)|15/06 Automated Alignment Research (Anthropic AAR)]] — AAR
- [[Lessons/15-07 Recursive Self-Improvement — Capability vs Alignment|15/07 Recursive Self-Improvement — Capability vs Alignment]] — RSI

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/15-04 Darwin Godel Machine — Open-Ended Self-Modifying Agents|15/04 Darwin Godel Machine — Open-Ended Self-Modifying Agents]], [[Lessons/15-05 AI Scientist v2 — Workshop-Level Autonomous Research|15/05 AI Scientist v2 — Workshop-Level Autonomous Research]]
- depth 3: [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]], [[Lessons/15-03 AlphaEvolve — Evolutionary Coding Agents|15/03 AlphaEvolve — Evolutionary Coding Agents]]

## Builds on this

- [[Lessons/15-20 OpenAI Preparedness Framework and DeepMind Frontier Safety Framework|15/20 OpenAI Preparedness Framework and DeepMind Frontier Safety Framework]]
- [[Lessons/15-21 METR Time Horizons and External Capability Evaluation|15/21 METR Time Horizons and External Capability Evaluation]]
- [[Lessons/15-22 CAIS, CAISI, and Societal-Scale Risk|15/22 CAIS, CAISI, and Societal-Scale Risk]]

## Concepts taught

- [[Concepts/RSP|RSP]] `lesson term` — Responsible Scaling Policy; v3.0 effective Feb 24, 2026
- AI R&D-4 `lesson term` — Capability to automate substantial AI research at competitive cost
- Affirmative case `lesson term` — Published argument that risks are identified and mitigations adequate
- Frontier Safety Roadmap `lesson term` — Standing document on planned safety work and expected capabilities
- Risk Report `lesson term` — Standing document on observed capability and residual risk after release
- Two-tier mitigation `lesson term` — Anthropic commitments vs industry recommendations, separated
- Pause commitment `lesson term` — Explicit promise to pause training; removed in v3.0
- SaferAI rating `lesson term` — Third-party rubric; v3.0 scored 1.9 (v2 was 2.2)

## Ships

- [[Artifacts/15-19 scaling-policy-review|scaling-policy-review]] `skill` — Review a frontier-lab scaling policy (Anthropic RSP, OpenAI Preparedness, DeepMind FSF, internal) against the RSP v3.0 reference shape.

## Further reading

- Anthropic — RSP v3.0 announcement ([link](https://www.anthropic.com/news/responsible-scaling-policy-v3)) — summary of changes from v2.
- Anthropic — Frontier Safety Roadmap ([link](https://www.anthropic.com/research/frontier-safety)) — standing document linked from RSP v3.0.
- [[Resources/Anthropic — Measuring AI agent autonomy in practice|Anthropic — Measuring AI agent autonomy in practice]] ([link](https://www.anthropic.com/research/measuring-agent-autonomy)) — connects AI R&D-4 to measured autonomy. ·  also cited by 16 other lessons
- Anthropic — Risk Report: Claude Opus 4.6 ([link](https://www.anthropic.com/research/risk-report-claude-opus-4-6)) — retrospective on the current frontier model.
- [[Resources/Anthropic — Responsible Scaling Policy v3.0 (Feb 2026)|Anthropic — Responsible Scaling Policy v3.0 (Feb 2026)]] ([link](https://anthropic.com/responsible-scaling-policy/rsp-v3-0)) — the full 32-page policy. ·  also cited by 5 other lessons


%% ── my notes ── %%
