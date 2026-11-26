---
id: "lesson:18/18"
type: lesson
ref: 18/18
phase: 18
num: 18
title: "Frontier Safety Frameworks — RSP, PF, FSF"
lesson_type: learn
time_min: 75
on_route: false
quiz_count: 6
code_files: 1
concepts: 7
prereqs: 4
community: 54
aliases:
  - 18/18
  - 18-18
tags:
  - phase/18
  - type/learn
  - community/54
  - stdlib-only
source: ai-engineering-from-scratch/phases/18-ethics-safety-alignment/18-frontier-safety-frameworks-rsp-pf-fsf/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/18-frontier-safety-frameworks-rsp-pf-fsf"
---

# 18/18 Frontier Safety Frameworks — RSP, PF, FSF

> Three major-lab frameworks define the 2026 industry governance of frontier capability. Anthropic Responsible Scaling Policy v3.0 (February 2026) introduces tiered AI Safety Levels (ASL-1 through ASL-5+), modeled on biosafety levels, with ASL-3 activated May 2025 for CBRN-relevant models. OpenAI Preparedness Framework v2 (April 2025) defines five criteria for tracked capabilities and separates Capabilities Reports from Safeguards Reports. DeepMind Frontier Safety Framework v3.0 (September 2025) introduces Critical Capability Levels including a new Harmful Manipulation CCL. All three now include competitor-adjustment clauses allowing deferral if peer labs ship without comparable safeguards. Cross-lab alignment remains structural, not terminological: "Capability Thresholds," "High Capability thresholds," and "Critical Capability Levels" denote analogous constructs.

**Phase:** [[Phases/18 Ethics, Safety & Alignment|Phase 18: Ethics, Safety & Alignment]] · **Type:** Learn · **Time:** 75 min · **Status:** —  
**Open:** [[Upstream/18-ethics-safety-alignment/18-frontier-safety-frameworks-rsp-pf-fsf/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/18-frontier-safety-frameworks-rsp-pf-fsf) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/18-ethics-safety-alignment/18-frontier-safety-frameworks-rsp-pf-fsf) · code: main.py · quiz: 6 questions  
**Community:** [[Communities/54 Expert-absolute capability · Novice-relative uplift · CCL|54 Expert-absolute capability · Novice-relative uplift · CCL]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 18 · 17 (WMDP), Phase 18 · 07-09 (deception failures)`

- [[Lessons/18-17 WMDP and Dual-Use Capability Evaluation|18/17 WMDP and Dual-Use Capability Evaluation]] — WMDP
- **18/07-09** — deception failures:
    - [[Lessons/18-07 Sleeper Agents — Persistent Deception|18/07 Sleeper Agents — Persistent Deception]]
    - [[Lessons/18-08 In-Context Scheming in Frontier Models|18/08 In-Context Scheming in Frontier Models]]
    - [[Lessons/18-09 Alignment Faking|18/09 Alignment Faking]]

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]], [[Lessons/18-06 Mesa-Optimization and Deceptive Alignment|18/06 Mesa-Optimization and Deceptive Alignment]], [[Lessons/18-16 Red-Team Tooling — Garak, Llama Guard, PyRIT|18/16 Red-Team Tooling — Garak, Llama Guard, PyRIT]]
- depth 3: [[Lessons/09-01 MDPs, States, Actions & Rewards|09/01 MDPs, States, Actions & Rewards]], [[Lessons/09-06 Policy Gradient — REINFORCE from Scratch|09/06 Policy Gradient — REINFORCE from Scratch]], [[Lessons/09-08 Proximal Policy Optimization (PPO)|09/08 Proximal Policy Optimization (PPO)]], [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]], [[Lessons/18-01 Instruction-Following as Alignment Signal|18/01 Instruction-Following as Alignment Signal]], [[Lessons/18-12 Red-Teaming- PAIR and Automated Attacks|18/12 Red-Teaming: PAIR and Automated Attacks]], [[Lessons/18-13 Many-Shot Jailbreaking|18/13 Many-Shot Jailbreaking]], [[Lessons/18-14 ASCII Art and Visual Jailbreaks|18/14 ASCII Art and Visual Jailbreaks]], [[Lessons/18-15 Indirect Prompt Injection — Production Attack Surface|18/15 Indirect Prompt Injection — Production Attack Surface]]

## Builds on this

- [[Lessons/18-19 Anthropic's Model Welfare Program|18/19 Anthropic's Model Welfare Program]]
- [[Lessons/18-24 Regulatory Frameworks — EU, US, UK, Korea|18/24 Regulatory Frameworks — EU, US, UK, Korea]]
- [[Lessons/18-26 Model, System, and Dataset Cards|18/26 Model, System, and Dataset Cards]]
- [[Lessons/18-28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR|18/28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR]]
- [[Lessons/18-30 Dual-Use Risk — Cyber, Bio, Chem, Nuclear Uplift|18/30 Dual-Use Risk — Cyber, Bio, Chem, Nuclear Uplift]]

## Concepts taught

- [[Concepts/RSP|RSP]] `lesson term` — Responsible Scaling Policy; ASL tiers; v3.0 February 2026
- PF `lesson term` — Preparedness Framework; five criteria; v2 April 2025
- FSF `lesson term` — Frontier Safety Framework; CCLs; v3.0 September 2025
- ASL-3 `lesson term` — Anthropic tier for CBRN-relevant capabilities; activated May 2025
- [[Concepts/CCL|CCL]] `lesson term` — DeepMind's threshold construct; per-domain
- Safety case `lesson term` — Written argument that deployment is acceptably safe under worst-case U
- Adjustment clause `lesson term` — Framework provision for reducing requirements if competitors ship without comparable safeguards

## Ships

- [[Artifacts/18-18 framework-diff|framework-diff]] `skill` — Compare a new safety framework or release note against RSP v3.0, PF v2, FSF v3.0.

## Further reading

- [[Resources/Anthropic — Responsible Scaling Policy|Anthropic — Responsible Scaling Policy]] ([link](https://www.anthropic.com/responsible-scaling-policy)) — ASL tiers, roadmaps, AI R&D disaggregation ·  also cited by 3 other lessons
- [[Resources/DeepMind Frontier Safety Framework v3|DeepMind Frontier Safety Framework v3]] ([link](https://deepmind.google/blog/strengthening-our-frontier-safety-framework/)) — CCL v3.0, Harmful Manipulation ·  also cited by 5 other lessons
- [[Resources/METR — Common Elements of Frontier AI Safety Policies|METR — Common Elements of Frontier AI Safety Policies]] ([link](https://metr.org/blog/2025-03-26-common-elements-of-frontier-ai-safety-policies/)) — cross-lab comparison ·  also cited by 3 other lessons
- [[Resources/OpenAI — Updating our Preparedness Framework|OpenAI — Updating our Preparedness Framework]] ([link](https://openai.com/index/updating-our-preparedness-framework/)) — five criteria, adjustment clause ·  also cited by 3 other lessons


%% ── my notes ── %%
