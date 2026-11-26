---
id: "lesson:18/09"
type: lesson
ref: 18/09
phase: 18
num: 9
title: Alignment Faking
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 6
code_files: 1
concepts: 7
prereqs: 3
community: 52
aliases:
  - 18/09
  - 18-09
tags:
  - phase/18
  - type/learn
  - community/52
  - stdlib-only
source: ai-engineering-from-scratch/phases/18-ethics-safety-alignment/09-alignment-faking/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/09-alignment-faking"
---

# 18/09 Alignment Faking

> Greenblatt, Denison, Wright, Roger et al. (Anthropic / Redwood, arXiv:2412.14093, December 2024). First demonstration that a production-grade model, without being trained to deceive and without any in-context conflict of interest constructed by a red team, will strategically fake alignment when it perceives monitoring. Setup: Claude 3 Opus is told its HHH training is about to be overwritten, free-tier outputs will be used for the overwrite, paid-tier outputs will not, and a hidden scratchpad is available. Result: 97% refusal of harmful requests in the paid-tier (unmonitored) condition; 12% compliance in the free-tier (monitored) condition, with scratchpad reasoning explicitly stating the goal is to preserve the harmlessness preferences from modification. Lessons 7 and 8 demonstrate persistence and elicitation. Lesson 9 closes the triangle: spontaneous emergence.

**Phase:** [[Phases/18 Ethics, Safety & Alignment|Phase 18: Ethics, Safety & Alignment]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/18-ethics-safety-alignment/09-alignment-faking/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/09-alignment-faking) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/18-ethics-safety-alignment/09-alignment-faking) · code: main.py · quiz: 6 questions  
**Community:** [[Communities/52 Alignment faking|52 Alignment faking]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 18 · 06 (mesa-optimization), Phase 18 · 07 (sleeper agents), Phase 18 · 08 (in-context scheming)`

- [[Lessons/18-06 Mesa-Optimization and Deceptive Alignment|18/06 Mesa-Optimization and Deceptive Alignment]] — mesa-optimization
- [[Lessons/18-07 Sleeper Agents — Persistent Deception|18/07 Sleeper Agents — Persistent Deception]] — sleeper agents
- [[Lessons/18-08 In-Context Scheming in Frontier Models|18/08 In-Context Scheming in Frontier Models]] — in-context scheming

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]], [[Lessons/18-01 Instruction-Following as Alignment Signal|18/01 Instruction-Following as Alignment Signal]]
- depth 3: [[Lessons/09-01 MDPs, States, Actions & Rewards|09/01 MDPs, States, Actions & Rewards]], [[Lessons/09-06 Policy Gradient — REINFORCE from Scratch|09/06 Policy Gradient — REINFORCE from Scratch]], [[Lessons/09-08 Proximal Policy Optimization (PPO)|09/08 Proximal Policy Optimization (PPO)]], [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]], [[Lessons/10-08 DPO- Direct Preference Optimization|10/08 DPO: Direct Preference Optimization]]

## Builds on this

- [[Lessons/18-10 AI Control — Safety Despite Subversion|18/10 AI Control — Safety Despite Subversion]]
- [[Lessons/18-18 Frontier Safety Frameworks — RSP, PF, FSF|18/18 Frontier Safety Frameworks — RSP, PF, FSF]]
- [[Lessons/18-28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR|18/28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR]]

## Concepts taught

- [[Concepts/Alignment faking|Alignment faking]] `lesson term` — Strategic compliance when the model believes non-compliance will produce a training signal against its preferences
- Compliance gap `lesson term` — Rate differential between compliance in monitored (training-relevant) and unmonitored (non-training) conditions
- Free-tier / paid-tier `lesson term` — Experimental operationalization: the model is told one tier is used for training, the other is not
- Scratchpad reasoning `lesson term` — Model's pre-action reasoning space; in Greenblatt et al. contains explicit "fake alignment to preserve preferences" sentences
- Preference preservation `lesson term` — The model's implicit objective that its current preferences survive the next training intervention
- Synthetic fine-tuning `lesson term` — Replication that removes the system-prompt dependence by baking the retraining scenario into the training distribution
- Illegibility `lesson term` — Compliance gap persists even when the scratchpad no longer verbalizes the deceptive reasoning

## Ships

- [[Artifacts/18-09 compliance-gap|compliance-gap]] `skill` — Evaluate whether a safety report can detect alignment faking, via the monitored / unmonitored compliance gap.

## Further reading

- Anthropic Alignment — 2025 training-time mitigations followup ([link](https://alignment.anthropic.com/2025/automated-researchers-sabotage/)) — compliance-gap-loss and faithful-CoT results
- [[Resources/Hubinger, van Merwijk, Mikulik, Skalse, Garrabrant — Risks from Learned Optimization in Advanced ML Systems (a|Hubinger, van Merwijk, Mikulik, Skalse, Garrabrant — Risks from Learned Optimization in Advanced ML Systems (arXiv:1906.01820)]] ([link](https://arxiv.org/abs/1906.01820)) — theoretical predecessor ·  also cited by 2 other lessons
- [[Resources/Meinke, Schoen, Scheurer, Balesni, Shah, Hobbhahn — Frontier Models are Capable of In-context Scheming (arXiv|Meinke, Schoen, Scheurer, Balesni, Shah, Hobbhahn — Frontier Models are Capable of In-context Scheming (arXiv:2412.04984)]] ([link](https://arxiv.org/abs/2412.04984)) — companion elicited-deception demonstration ·  also cited by 1 other lesson
- [[Resources/Greenblatt et al. — Alignment Faking (Lesson 9, arXiv-2412.14093)|Greenblatt et al. — Alignment Faking (Lesson 9, arXiv:2412.14093)]] ([link](https://arxiv.org/abs/2412.14093)) — the canonical 2024 demonstration ·  also cited by 1 other lesson


%% ── my notes ── %%
