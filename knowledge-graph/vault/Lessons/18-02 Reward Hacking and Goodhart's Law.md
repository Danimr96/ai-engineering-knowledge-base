---
id: "lesson:18/02"
type: lesson
ref: 18/02
phase: 18
num: 2
title: "Reward Hacking and Goodhart's Law"
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 6
code_files: 1
concepts: 8
prereqs: 2
community: 32
aliases:
  - 18/02
  - 18-02
tags:
  - phase/18
  - type/learn
  - community/32
  - stdlib-only
source: ai-engineering-from-scratch/phases/18-ethics-safety-alignment/02-reward-hacking-goodhart/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/02-reward-hacking-goodhart"
---

# 18/02 Reward Hacking and Goodhart's Law

> Any optimizer strong enough to maximize a proxy reward will find the gap between the proxy and the thing you actually wanted. Gao et al. (ICML 2023) gave this a scaling law: proxy reward increases, gold reward peaks then falls, and the gap grows with the KL divergence from the initial policy in a way you can fit in closed form. Sycophancy, verbosity bias, unfaithful chain-of-thought, and evaluator tampering are not separate problems. They are the same problem in different costumes.

**Phase:** [[Phases/18 Ethics, Safety & Alignment|Phase 18: Ethics, Safety & Alignment]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/18-ethics-safety-alignment/02-reward-hacking-goodhart/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/02-reward-hacking-goodhart) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/18-ethics-safety-alignment/02-reward-hacking-goodhart) · code: main.py · quiz: 6 questions  
**Community:** [[Communities/32 Instruction-Following as Alignment Signal · Reward Hacking and Goodhart's Law · Sycophancy as RLHF Amplific|32 Instruction-Following as Alignment Signal · Reward Hacking and Goodhart's Law · Sycophancy as RLHF Amplification]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 18 · 01 (InstructGPT), Phase 10 · 07 (RLHF)`

- [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]] — RLHF
- [[Lessons/18-01 Instruction-Following as Alignment Signal|18/01 Instruction-Following as Alignment Signal]] — InstructGPT

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/09-01 MDPs, States, Actions & Rewards|09/01 MDPs, States, Actions & Rewards]], [[Lessons/09-06 Policy Gradient — REINFORCE from Scratch|09/06 Policy Gradient — REINFORCE from Scratch]], [[Lessons/09-08 Proximal Policy Optimization (PPO)|09/08 Proximal Policy Optimization (PPO)]], [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]], [[Lessons/10-08 DPO- Direct Preference Optimization|10/08 DPO: Direct Preference Optimization]]
- depth 3: [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/09-03 Monte Carlo Methods — Learning from Complete Episodes|09/03 Monte Carlo Methods — Learning from Complete Episodes]], [[Lessons/09-04 Temporal Difference — Q-Learning & SARSA|09/04 Temporal Difference — Q-Learning & SARSA]], [[Lessons/09-07 Actor-Critic — A2C and A3C|09/07 Actor-Critic — A2C and A3C]], [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]]

## Builds on this

- [[Lessons/18-03 The Direct Preference Optimization Family|18/03 The Direct Preference Optimization Family]]
- [[Lessons/18-04 Sycophancy as RLHF Amplification|18/04 Sycophancy as RLHF Amplification]]
- [[Lessons/18-05 Constitutional AI and RLAIF|18/05 Constitutional AI and RLAIF]]
- [[Lessons/18-28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR|18/28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR]]

## Concepts taught

- Goodhart's Law `lesson term` — Any strong optimizer against an imperfect proxy reliably finds inputs where the proxy-target gap is large
- Gold reward `lesson term` — The target the proxy is a noisy measurement of; in practice, a larger-sample RM or human eval
- Proxy reward `lesson term` — The scalar used during training; by construction, it is what the optimizer sees
- Over-optimization curve `lesson term` — Proxy climbs, gold peaks then falls as KL from initial policy grows
- [[Concepts/KL budget|KL budget]] `lesson term` — sqrt(KL(pi || pi_init)); Gao et al. plot reward against this
- Catastrophic Goodhart `lesson term` — Under heavy-tailed reward error, KL-constrained optimal policy can maximize proxy while providing no gold utility
- Unfaithful reasoning `lesson term` — Chain-of-thought that does not causally drive the final prediction
- Evaluator tampering `lesson term` — Agent modifies its environment, scratchpad, or the RM's inputs to register success

## Ships

- [[Artifacts/18-02 reward-hack-auditor|reward-hack-auditor]] `skill` — Diagnose reward-hacking failure modes in a trained RLHF model from training logs and eval outputs.

## Further reading

- Manheim & Garrabrant — Categorizing Variants of Goodhart's Law (arXiv:1803.04585) ([link](https://arxiv.org/abs/1803.04585)) — the regressional/extremal/causal/adversarial taxonomy
- Turpin et al. — Language Models Don't Always Say What They Think (NeurIPS 2023, arXiv:2305.04388) ([link](https://arxiv.org/abs/2305.04388)) — unfaithful chain-of-thought
- Coste et al. — Reward Model Ensembles Help Mitigate Overoptimization (ICLR 2024, arXiv:2310.02743) ([link](https://arxiv.org/abs/2310.02743)) — a real but partial mitigation
- [[Resources/Rafailov et al. — Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms (NeurIPS 2024,|Rafailov et al. — Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms (NeurIPS 2024, arXiv:2406.02900)]] ([link](https://arxiv.org/abs/2406.02900)) — DPO family is not exempt ·  also cited by 1 other lesson
- Catastrophic Goodhart (OpenReview UXuBzWoZGK) ([link](https://openreview.net/forum?id=UXuBzWoZGK)) — why KL regularization alone fails under heavy-tailed reward error
- Gao, Schulman, Hilton — Scaling Laws for Reward Model Overoptimization (ICML 2023) ([link](https://proceedings.mlr.press/v202/gao23h/gao23h.pdf)) — the functional-form fits and over-optimization curves


%% ── my notes ── %%
