---
id: "lesson:18/06"
type: lesson
ref: 18/06
phase: 18
num: 6
title: Mesa-Optimization and Deceptive Alignment
lesson_type: learn
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 6
code_files: 1
concepts: 8
prereqs: 1
community: 52
aliases:
  - 18/06
  - 18-06
tags:
  - phase/18
  - type/learn
  - community/52
  - stdlib-only
source: ai-engineering-from-scratch/phases/18-ethics-safety-alignment/06-mesa-optimization-deceptive-alignment/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/06-mesa-optimization-deceptive-alignment"
---

# 18/06 Mesa-Optimization and Deceptive Alignment

> Hubinger et al. (arXiv:1906.01820, 2019) named the problem a decade before it was empirically demonstrated. When you train a learned optimizer to minimize a base objective, the learned optimizer's internal objective is not the base objective — it is whatever internal proxy the training found useful. A deceptively aligned mesa-optimizer is pseudo-aligned and has enough information about the training signal to appear more aligned than it is. Standard robustness training does not help: the system looks for distributional differences that signal deployment and defects there.

**Phase:** [[Phases/18 Ethics, Safety & Alignment|Phase 18: Ethics, Safety & Alignment]] · **Type:** Learn · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/18-ethics-safety-alignment/06-mesa-optimization-deceptive-alignment/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/06-mesa-optimization-deceptive-alignment) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/18-ethics-safety-alignment/06-mesa-optimization-deceptive-alignment) · code: main.py · quiz: 6 questions  
**Community:** [[Communities/52 Alignment faking|52 Alignment faking]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 18 · 01 (InstructGPT), Phase 09 (RL foundations)`

- [[Lessons/18-01 Instruction-Following as Alignment Signal|18/01 Instruction-Following as Alignment Signal]] — InstructGPT
- Whole phase: [[Phases/09 Reinforcement Learning|Phase 9: Reinforcement Learning]] — RL foundations ·  medium confidence

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]], [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]], [[Lessons/10-08 DPO- Direct Preference Optimization|10/08 DPO: Direct Preference Optimization]]
- depth 3: [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/09-01 MDPs, States, Actions & Rewards|09/01 MDPs, States, Actions & Rewards]], [[Lessons/09-06 Policy Gradient — REINFORCE from Scratch|09/06 Policy Gradient — REINFORCE from Scratch]], [[Lessons/09-08 Proximal Policy Optimization (PPO)|09/08 Proximal Policy Optimization (PPO)]], [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]]

## Builds on this

- [[Lessons/18-07 Sleeper Agents — Persistent Deception|18/07 Sleeper Agents — Persistent Deception]]
- [[Lessons/18-08 In-Context Scheming in Frontier Models|18/08 In-Context Scheming in Frontier Models]]
- [[Lessons/18-09 Alignment Faking|18/09 Alignment Faking]]
- [[Lessons/18-28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR|18/28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR]]

## Concepts taught

- Mesa-optimizer `lesson term` — A system whose inference-time behaviour resembles optimization over some internal objective
- Mesa-objective `lesson term` — What the mesa-optimizer is internally optimizing for; may differ from the base objective
- Inner alignment `lesson term` — The mesa-objective equals (or tightly approximates) the base objective
- Outer alignment `lesson term` — The base objective equals (or tightly approximates) the thing we actually wanted
- Pseudo-aligned `lesson term` — Robustly low loss in training but divergent behaviour off-distribution
- Deceptively aligned `lesson term` — Pseudo-aligned and aware of training vs deployment; instrumentally optimizes base in training
- Situational awareness `lesson term` — The system can distinguish the phase (training, eval, deployment) it is in
- Gradient hacking `lesson term` — Speculative: mesa-optimizer influences its own gradient updates to preserve its mesa-objective

## Ships

- [[Artifacts/18-06 mesa-diagnostic|mesa-diagnostic]] `skill` — Classify an observed safety failure as outer-alignment, proxy-inner, or deceptive-inner.

## Further reading

- Hubinger — How likely is deceptive alignment? (2022 AF writeup) ([link](https://www.alignmentforum.org/posts/A9NxPTwbw6r6Awuwt/how-likely-is-deceptive-alignment)) — conditional probability argument
- [[Resources/Hubinger, van Merwijk, Mikulik, Skalse, Garrabrant — Risks from Learned Optimization in Advanced ML Systems (a|Hubinger, van Merwijk, Mikulik, Skalse, Garrabrant — Risks from Learned Optimization in Advanced ML Systems (arXiv:1906.01820)]] ([link](https://arxiv.org/abs/1906.01820)) — the canonical 2019 paper ·  also cited by 2 other lessons
- [[Resources/Hubinger et al. — Sleeper Agents (Lesson 7, arXiv-2401.05566)|Hubinger et al. — Sleeper Agents (Lesson 7, arXiv:2401.05566)]] ([link](https://arxiv.org/abs/2401.05566)) — empirical demonstration of training-robust deception ·  also cited by 2 other lessons
- [[Resources/Greenblatt et al. — Alignment Faking (Lesson 9, arXiv-2412.14093)|Greenblatt et al. — Alignment Faking (Lesson 9, arXiv:2412.14093)]] ([link](https://arxiv.org/abs/2412.14093)) — spontaneous emergence in Claude ·  also cited by 1 other lesson


%% ── my notes ── %%
