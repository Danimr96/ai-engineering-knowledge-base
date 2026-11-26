---
id: "lesson:18/03"
type: lesson
ref: 18/03
phase: 18
num: 3
title: The Direct Preference Optimization Family
lesson_type: learn
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 6
code_files: 1
concepts: 9
prereqs: 3
community: 45
aliases:
  - 18/03
  - 18-03
tags:
  - phase/18
  - type/learn
  - community/45
  - stdlib-only
source: ai-engineering-from-scratch/phases/18-ethics-safety-alignment/03-direct-preference-optimization-family/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/03-direct-preference-optimization-family"
---

# 18/03 The Direct Preference Optimization Family

> Rafailov et al. (2023) showed RLHF's optimum has a closed form in terms of the preference data, so you can skip the explicit reward model and optimize the policy directly. That insight spawned a family — IPO, KTO, SimPO, ORPO, BPO — each fixing a failure mode of DPO. In 2026, direct alignment algorithms ship more frontier post-training runs than PPO. But the over-optimization curve from Lesson 2 still applies: DAAs do not escape Goodhart, they just move where it bites.

**Phase:** [[Phases/18 Ethics, Safety & Alignment|Phase 18: Ethics, Safety & Alignment]] · **Type:** Learn · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/18-ethics-safety-alignment/03-direct-preference-optimization-family/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/03-direct-preference-optimization-family) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/18-ethics-safety-alignment/03-direct-preference-optimization-family) · code: main.py · quiz: 6 questions  
**Community:** [[Communities/45 Implicit reward · KTO · ORPO|45 Implicit reward · KTO · ORPO]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 18 · 01 (InstructGPT), Phase 18 · 02 (Reward hacking), Phase 10 · 08 (DPO basics)`

- [[Lessons/10-08 DPO- Direct Preference Optimization|10/08 DPO: Direct Preference Optimization]] — DPO basics
- [[Lessons/18-01 Instruction-Following as Alignment Signal|18/01 Instruction-Following as Alignment Signal]] — InstructGPT
- [[Lessons/18-02 Reward Hacking and Goodhart's Law|18/02 Reward Hacking and Goodhart's Law]] — Reward hacking

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]], [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]]
- depth 3: [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]], [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]], [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]], [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]], [[Lessons/09-01 MDPs, States, Actions & Rewards|09/01 MDPs, States, Actions & Rewards]], [[Lessons/09-06 Policy Gradient — REINFORCE from Scratch|09/06 Policy Gradient — REINFORCE from Scratch]], [[Lessons/09-08 Proximal Policy Optimization (PPO)|09/08 Proximal Policy Optimization (PPO)]], [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]]

## Builds on this

- [[Lessons/18-28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR|18/28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR]]

## Concepts taught

- [[Concepts/DPO (Direct Preference Optimization)|DPO (Direct Preference Optimization)]] (as *DPO*) `glossary` — Loss derived from the closed-form RLHF optimum; policy parameters only
- [[Concepts/Implicit reward|Implicit reward]] `lesson term` — beta log(pi(y|x) / pi_ref(y|x)) — the DPO-implied reward
- IPO `lesson term` — Replaces log-sigmoid with identity; implicit reward gap capped by 1/(2 beta)
- [[Concepts/KTO|KTO]] `lesson term` — Prospect-theory utility over single labels with loss aversion
- [[Concepts/SimPO|SimPO]] `lesson term` — Length-normalized log-likelihood + margin; no reference policy
- [[Concepts/ORPO|ORPO]] `lesson term` — NLL + odds-ratio preference term; trains from base model in one pass
- BPO `lesson term` — DPO plus a penalty for decreasing the chosen response's absolute log-prob
- Degraded Chosen `lesson term` — DPO decreases chosen log-prob so long as rejected falls faster
- DAA `lesson term` — Any preference-loss method that skips an explicit RM

## Ships

- [[Artifacts/18-03 preference-loss-selector|preference-loss-selector]] `skill` — Recommend a direct-alignment-algorithm loss given dataset shape and target stage.

## Further reading

- [[Resources/Direct Preference Optimization paper|Direct Preference Optimization paper]] ([link](https://arxiv.org/abs/2305.18290)) ·  also cited by 3 other lessons
- Azar et al. — A General Theoretical Paradigm to Understand Learning from Human Preferences (AISTATS 2024, arXiv:2310.12036) ([link](https://arxiv.org/abs/2310.12036)) — IPO
- [[Resources/Ethayarajh et al., 2024 - -KTO- Model Alignment as Prospect Theoretic Optimization|Ethayarajh et al., 2024 -- "KTO: Model Alignment as Prospect Theoretic Optimization]] ([link](https://arxiv.org/abs/2402.01306)) ·  also cited by 1 other lesson
- [[Resources/Hong et al., 2024 - -ORPO- Monolithic Preference Optimization without Reference Model|Hong et al., 2024 -- "ORPO: Monolithic Preference Optimization without Reference Model]] ([link](https://arxiv.org/abs/2403.07691)) ·  also cited by 1 other lesson
- [[Resources/Meng et al., 2024 - -SimPO- Simple Preference Optimization with a Reference-Free Reward|Meng et al., 2024 -- "SimPO: Simple Preference Optimization with a Reference-Free Reward]] ([link](https://arxiv.org/abs/2405.14734)) ·  also cited by 1 other lesson
- [[Resources/Rafailov et al. — Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms (NeurIPS 2024,|Rafailov et al. — Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms (NeurIPS 2024, arXiv:2406.02900)]] ([link](https://arxiv.org/abs/2406.02900)) ·  also cited by 1 other lesson
- BPO — Behavior Preservation Optimization (ICLR 2026 OpenReview b97EwMUWu7) ([link](https://openreview.net/forum?id=b97EwMUWu7))


%% ── my notes ── %%
