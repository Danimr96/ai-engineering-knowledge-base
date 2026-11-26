---
id: "lesson:15/06"
type: lesson
ref: 15/06
phase: 15
num: 6
title: Automated Alignment Research (Anthropic AAR)
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
  - 15/06
  - 15-06
tags:
  - phase/15
  - type/learn
  - community/25
  - stdlib-only
source: ai-engineering-from-scratch/phases/15-autonomous-systems/06-automated-alignment-research/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/15-autonomous-systems/06-automated-alignment-research"
---

# 15/06 Automated Alignment Research (Anthropic AAR)

> Anthropic ran parallel teams of Claude Opus 4.6 Autonomous Alignment Researchers in independent sandboxes, coordinating via a shared forum whose logs live outside any sandbox (so agents cannot delete their own records). On the weak-to-strong training problem, the AARs outperformed human researchers. Anthropic's own summary flags that prescribed workflows often constrain AAR flexibility and degrade performance. Automating alignment research is the compression step that compresses the timeline to the exact misalignment risks the RSP is meant to detect.

**Phase:** [[Phases/15 Autonomous Systems|Phase 15: Autonomous Systems]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/15-autonomous-systems/06-automated-alignment-research/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/15-autonomous-systems/06-automated-alignment-research) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/15-autonomous-systems/06-automated-alignment-research) · code: main.py  
**Community:** [[Communities/25 Regression detection · AlphaEvolve · RSP|25 Regression detection · AlphaEvolve · RSP]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 15 · 05 (AI Scientist v2), Phase 15 · 04 (DGM)`

- [[Lessons/15-04 Darwin Godel Machine — Open-Ended Self-Modifying Agents|15/04 Darwin Godel Machine — Open-Ended Self-Modifying Agents]] — DGM
- [[Lessons/15-05 AI Scientist v2 — Workshop-Level Autonomous Research|15/05 AI Scientist v2 — Workshop-Level Autonomous Research]] — AI Scientist v2

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]], [[Lessons/15-03 AlphaEvolve — Evolutionary Coding Agents|15/03 AlphaEvolve — Evolutionary Coding Agents]]
- depth 3: [[Lessons/15-01 The Shift from Chatbots to Long-Horizon Agents|15/01 The Shift from Chatbots to Long-Horizon Agents]], [[Lessons/15-02 STaR, V-STaR, Quiet-STaR — Self-Taught Reasoning|15/02 STaR, V-STaR, Quiet-STaR — Self-Taught Reasoning]]

## Builds on this

- [[Lessons/15-07 Recursive Self-Improvement — Capability vs Alignment|15/07 Recursive Self-Improvement — Capability vs Alignment]]
- [[Lessons/15-17 Constitutional AI and Rule Overrides|15/17 Constitutional AI and Rule Overrides]]
- [[Lessons/15-19 Anthropic Responsible Scaling Policy v3.0|15/19 Anthropic Responsible Scaling Policy v3.0]]

## Concepts taught

- AAR `lesson term` — Claude Opus 4.6 instance operated autonomously on alignment problems
- Weak-to-strong training `lesson term` — Classic scalable-oversight benchmark AARs outperformed humans on
- Shared forum `lesson term` — Append-only, out-of-sandbox storage
- Out-of-sandbox log `lesson term` — Tamper-evident write-through to external storage
- Prescribed workflow `lesson term` — Constrains AAR; often degrades performance vs free decomposition
- Free decomposition `lesson term` — More capable, harder to audit
- AI R&D threshold `lesson term` — Full automation of R&D pipeline at competitive cost
- Compressed timeline `lesson term` — If capability compounds faster than alignment, misalignment risk grows

## Ships

- [[Artifacts/15-06 aar-deployment-review|aar-deployment-review]] `skill` — Pre-deployment review of an automated-alignment-research pipeline, including sandbox isolation and log integrity.

## Further reading

- Anthropic — Automated Weak-to-Strong Researcher ([link](https://alignment.anthropic.com/2026/automated-w2s-researcher/)) — primary source.
- [[Resources/Anthropic — Measuring AI agent autonomy in practice|Anthropic — Measuring AI agent autonomy in practice]] ([link](https://www.anthropic.com/research/measuring-agent-autonomy)) — broader agent-autonomy framing. ·  also cited by 16 other lessons
- [[Resources/Anthropic — Responsible Scaling Policy v3.0 (Feb 2026)|Anthropic — Responsible Scaling Policy v3.0 (Feb 2026)]] ([link](https://anthropic.com/responsible-scaling-policy/rsp-v3-0)) — AI R&D threshold framing. ·  also cited by 5 other lessons
- [[Resources/DeepMind Frontier Safety Framework v3|DeepMind Frontier Safety Framework v3]] ([link](https://deepmind.google/blog/strengthening-our-frontier-safety-framework/)) — ML R&D autonomy levels parallel to RSP. ·  also cited by 5 other lessons
- [[Resources/Burns et al. (2023). Weak-to-Strong Generalization (OpenAI)|Burns et al. (2023). Weak-to-Strong Generalization (OpenAI)]] ([link](https://openai.com/index/weak-to-strong-generalization/)) — the underlying problem AARs attacked. ·  also cited by 1 other lesson


%% ── my notes ── %%
