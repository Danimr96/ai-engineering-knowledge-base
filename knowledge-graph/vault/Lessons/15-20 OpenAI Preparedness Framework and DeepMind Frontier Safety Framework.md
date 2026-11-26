---
id: "lesson:15/20"
type: lesson
ref: 15/20
phase: 15
num: 20
title: OpenAI Preparedness Framework and DeepMind Frontier Safety Framework
lesson_type: learn
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 1
aliases:
  - 15/20
  - 15-20
tags:
  - phase/15
  - type/learn
  - stdlib-only
source: ai-engineering-from-scratch/phases/15-autonomous-systems/20-openai-preparedness-deepmind-fsf/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/15-autonomous-systems/20-openai-preparedness-deepmind-fsf"
---

# 15/20 OpenAI Preparedness Framework and DeepMind Frontier Safety Framework

> OpenAI Preparedness Framework v2 (April 2025) introduces Research Categories — Long-range Autonomy, Sandbagging, Autonomous Replication and Adaptation, Undermining Safeguards — distinct from Tracked Categories. Tracked Categories trigger Capabilities Reports plus Safeguards Reports reviewed by the Safety Advisory Group. DeepMind's FSF v3 (September 2025, with Tracked Capability Levels added April 17, 2026) folds autonomy into ML R&D and Cyber domains (ML R&D autonomy level 1 = fully automate the AI R&D pipeline at competitive cost vs human + AI tools). FSF v3 explicitly addresses deceptive alignment via automated monitoring for instrumental-reasoning misuse. The honest note: Research Categories in PF v2 (including Long-range Autonomy) do not automatically trigger mitigations; the policy language is "potential." DeepMind itself says automated monitoring "will not remain sufficient long-term" if instrumental reasoning strengthens.

**Phase:** [[Phases/15 Autonomous Systems|Phase 15: Autonomous Systems]] · **Type:** Learn · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/15-autonomous-systems/20-openai-preparedness-deepmind-fsf/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/15-autonomous-systems/20-openai-preparedness-deepmind-fsf) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/15-autonomous-systems/20-openai-preparedness-deepmind-fsf) · code: main.py  
**Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 15 · 19 (Anthropic RSP)`

- [[Lessons/15-19 Anthropic Responsible Scaling Policy v3.0|15/19 Anthropic Responsible Scaling Policy v3.0]] — Anthropic RSP

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/15-06 Automated Alignment Research (Anthropic AAR)|15/06 Automated Alignment Research (Anthropic AAR)]], [[Lessons/15-07 Recursive Self-Improvement — Capability vs Alignment|15/07 Recursive Self-Improvement — Capability vs Alignment]]
- depth 3: [[Lessons/15-04 Darwin Godel Machine — Open-Ended Self-Modifying Agents|15/04 Darwin Godel Machine — Open-Ended Self-Modifying Agents]], [[Lessons/15-05 AI Scientist v2 — Workshop-Level Autonomous Research|15/05 AI Scientist v2 — Workshop-Level Autonomous Research]]

## Builds on this

- [[Lessons/15-22 CAIS, CAISI, and Societal-Scale Risk|15/22 CAIS, CAISI, and Societal-Scale Risk]]

## Concepts taught

- Preparedness Framework `lesson term` — PF v2 (April 2025); Tracked vs Research categories
- Tracked Category `lesson term` — Triggers Capabilities + Safeguards Reports; SAG review
- Research Category `lesson term` — Tracked but no automatic mitigation; includes Long-range Autonomy
- Frontier Safety Framework `lesson term` — FSF v3 (Sept 2025) + Tracked Capability Levels (Apr 2026)
- [[Concepts/CCL|CCL]] `lesson term` — DeepMind threshold per domain (Cyber, Bio, ML R&D, CBRN)
- ML R&D autonomy level 1 `lesson term` — Fully automate AI R&D pipeline at competitive cost
- Sandbagging `lesson term` — Model underperforms on evals; in OpenAI Research Categories
- Instrumental reasoning `lesson term` — Reasoning about how to achieve goals; target of DeepMind monitoring

## Ships

- [[Artifacts/15-20 cross-policy-diff|cross-policy-diff]] `skill` — Produce a cross-policy comparison for a specific capability using the OpenAI Preparedness Framework v2, Anthropic RSP v3.0, and DeepMind FSF v3 as reference.

## Further reading

- OpenAI — Preparedness Framework v2 PDF ([link](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf)) — full document.
- [[Resources/DeepMind Frontier Safety Framework v3|DeepMind Frontier Safety Framework v3]] ([link](https://deepmind.google/blog/strengthening-our-frontier-safety-framework/)) — FSF v3 announcement. ·  also cited by 5 other lessons
- DeepMind — Updating the Frontier Safety Framework (April 2026) ([link](https://deepmind.google/blog/updating-the-frontier-safety-framework/)) — Tracked Capability Levels addition.
- [[Resources/OpenAI — Updating our Preparedness Framework|OpenAI — Updating our Preparedness Framework]] ([link](https://openai.com/index/updating-our-preparedness-framework/)) — v2 announcement. ·  also cited by 3 other lessons
- Gemini 3 Pro FSF Report ([link](https://storage.googleapis.com/deepmind-media/gemini/gemini_3_pro_fsf_report.pdf)) — example of an FSF-format Risk Report.


%% ── my notes ── %%
