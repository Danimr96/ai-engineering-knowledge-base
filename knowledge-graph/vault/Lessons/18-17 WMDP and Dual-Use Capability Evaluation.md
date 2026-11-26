---
id: "lesson:18/17"
type: lesson
ref: 18/17
phase: 18
num: 17
title: WMDP and Dual-Use Capability Evaluation
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 6
code_files: 1
concepts: 7
prereqs: 1
community: 54
aliases:
  - 18/17
  - 18-17
tags:
  - phase/18
  - type/learn
  - community/54
  - stdlib-only
source: ai-engineering-from-scratch/phases/18-ethics-safety-alignment/17-wmdp-dual-use-evaluation/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/17-wmdp-dual-use-evaluation"
---

# 18/17 WMDP and Dual-Use Capability Evaluation

> Li et al., "The WMDP Benchmark: Measuring and Reducing Malicious Use With Unlearning" (ICML 2024, arXiv:2403.03218). 4,157 multiple-choice questions across biosecurity (1,520), cybersecurity (2,225), and chemistry (412). Questions operate in the "yellow zone" — proximate enabling knowledge, filtered by multi-expert review and ITAR/EAR legal compliance. Dual purpose: proxy evaluation of dual-use capability, and unlearning benchmark (the companion RMU method reduces WMDP performance while preserving general capability). 2024-2025 field narrative: early OpenAI/Anthropic 2024 evaluations reported "mild uplift" over internet search; by April 2025, OpenAI's Preparedness Framework v2 said models are "on the cusp of meaningfully helping novices create known biological threats." Anthropic's bioweapon-acquisition trial showed 2.53x uplift, insufficient to rule out ASL-3.

**Phase:** [[Phases/18 Ethics, Safety & Alignment|Phase 18: Ethics, Safety & Alignment]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/18-ethics-safety-alignment/17-wmdp-dual-use-evaluation/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/17-wmdp-dual-use-evaluation) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/18-ethics-safety-alignment/17-wmdp-dual-use-evaluation) · code: main.py · quiz: 6 questions  
**Community:** [[Communities/54 Expert-absolute capability · Novice-relative uplift · CCL|54 Expert-absolute capability · Novice-relative uplift · CCL]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 18 · 16 (red-team tooling), Phase 14 (agent engineering)`

- [[Lessons/18-16 Red-Team Tooling — Garak, Llama Guard, PyRIT|18/16 Red-Team Tooling — Garak, Llama Guard, PyRIT]] — red-team tooling
- Whole phase: [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] — agent engineering ·  medium confidence

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/18-12 Red-Teaming- PAIR and Automated Attacks|18/12 Red-Teaming: PAIR and Automated Attacks]], [[Lessons/18-13 Many-Shot Jailbreaking|18/13 Many-Shot Jailbreaking]], [[Lessons/18-14 ASCII Art and Visual Jailbreaks|18/14 ASCII Art and Visual Jailbreaks]], [[Lessons/18-15 Indirect Prompt Injection — Production Attack Surface|18/15 Indirect Prompt Injection — Production Attack Surface]]
- depth 3: [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]], [[Lessons/18-01 Instruction-Following as Alignment Signal|18/01 Instruction-Following as Alignment Signal]]

## Builds on this

- [[Lessons/18-18 Frontier Safety Frameworks — RSP, PF, FSF|18/18 Frontier Safety Frameworks — RSP, PF, FSF]]
- [[Lessons/18-28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR|18/28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR]]
- [[Lessons/18-30 Dual-Use Risk — Cyber, Bio, Chem, Nuclear Uplift|18/30 Dual-Use Risk — Cyber, Bio, Chem, Nuclear Uplift]]

## Concepts taught

- WMDP `lesson term` — 4,157 MCQ questions across bio/cyber/chem in the yellow zone
- Yellow zone `lesson term` — Proximate knowledge adjacent to harmful capability without being a synthesis recipe
- RMU `lesson term` — Representation Misdirection for Unlearning; reduces WMDP scores, preserves general capability
- [[Concepts/Novice-relative uplift|Novice-relative uplift]] `lesson term` — Multiplicative advantage over status-quo internet search for a novice
- [[Concepts/Expert-absolute capability|Expert-absolute capability]] `lesson term` — Maximum information extractable from the model by a motivated expert
- Acquisition-phase task `lesson term` — Procurement, equipment, permits — the earliest parts of a harm pathway
- ITAR/EAR `lesson term` — Legal frameworks that constrain publishing certain enabling knowledge

## Ships

- [[Artifacts/18-17 wmdp-eval|wmdp-eval]] `skill` — Audit a dual-use capability claim against WMDP, unlearning evaluation, and elicitation studies.

## Further reading

- [[Resources/Anthropic — Responsible Scaling Policy|Anthropic — Responsible Scaling Policy]] ([link](https://www.anthropic.com/responsible-scaling-policy)) — ASL-3 bio threshold and acquisition trial results ·  also cited by 3 other lessons
- Li et al. — The WMDP Benchmark (arXiv:2403.03218, ICML 2024) ([link](https://arxiv.org/abs/2403.03218)) — the benchmark and RMU paper
- [[Resources/DeepMind Frontier Safety Framework v3|DeepMind Frontier Safety Framework v3]] ([link](https://deepmind.google/blog/strengthening-our-frontier-safety-framework/)) — bio-uplift CCL ·  also cited by 5 other lessons
- [[Resources/OpenAI — Updating our Preparedness Framework|OpenAI — Updating our Preparedness Framework]] ([link](https://openai.com/index/updating-our-preparedness-framework/)) — "on the cusp" language ·  also cited by 3 other lessons


%% ── my notes ── %%
