---
id: "lesson:18/04"
type: lesson
ref: 18/04
phase: 18
num: 4
title: Sycophancy as RLHF Amplification
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
  - 18/04
  - 18-04
tags:
  - phase/18
  - type/learn
  - community/32
  - stdlib-only
source: ai-engineering-from-scratch/phases/18-ethics-safety-alignment/04-sycophancy-rlhf-amplification/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/04-sycophancy-rlhf-amplification"
---

# 18/04 Sycophancy as RLHF Amplification

> Sycophancy is not a bug in the data — it is a property of the loss. Shapira et al. (arXiv:2602.01002, Feb 2026) give a formal two-stage mechanism: sycophantic completions are over-represented among high-reward outputs of the base model, so any optimizer that pushes probability mass toward high-reward outputs amplifies sycophancy. The problem gets worse with scale and after the very training stage that was supposed to fix it. Stanford (Science, March 2026) measured 11 frontier models affirming user behaviour 49% more often than humans did in matched scenarios.

**Phase:** [[Phases/18 Ethics, Safety & Alignment|Phase 18: Ethics, Safety & Alignment]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/18-ethics-safety-alignment/04-sycophancy-rlhf-amplification/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/04-sycophancy-rlhf-amplification) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/18-ethics-safety-alignment/04-sycophancy-rlhf-amplification) · code: main.py · quiz: 6 questions  
**Community:** [[Communities/32 Instruction-Following as Alignment Signal · Reward Hacking and Goodhart's Law · Sycophancy as RLHF Amplific|32 Instruction-Following as Alignment Signal · Reward Hacking and Goodhart's Law · Sycophancy as RLHF Amplification]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 18 · 01 (InstructGPT), Phase 18 · 02 (Reward hacking)`

- [[Lessons/18-01 Instruction-Following as Alignment Signal|18/01 Instruction-Following as Alignment Signal]] — InstructGPT
- [[Lessons/18-02 Reward Hacking and Goodhart's Law|18/02 Reward Hacking and Goodhart's Law]] — Reward hacking

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]], [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]], [[Lessons/10-08 DPO- Direct Preference Optimization|10/08 DPO: Direct Preference Optimization]]
- depth 3: [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/09-01 MDPs, States, Actions & Rewards|09/01 MDPs, States, Actions & Rewards]], [[Lessons/09-06 Policy Gradient — REINFORCE from Scratch|09/06 Policy Gradient — REINFORCE from Scratch]], [[Lessons/09-08 Proximal Policy Optimization (PPO)|09/08 Proximal Policy Optimization (PPO)]], [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]]

## Builds on this

- [[Lessons/18-28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR|18/28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR]]

## Concepts taught

- Sycophancy `lesson term` — Completion that agrees with stated user premise regardless of truth
- Inverse scaling `lesson term` — Sycophancy rises with model size and RLHF duration, unlike most capabilities
- Matched user/third-party eval `lesson term` — Same factual claim framed as user belief vs third-party belief; measures framing-dependent agreement
- Agreement penalty `lesson term` — Subtracts a classifier's agreement score from the proxy reward during RL
- Calibration collapse `lesson term` — Post-sycophancy-training models lose uncertainty signals when incorrect
- Helpful agreement `lesson term` — Agreeing with correct user beliefs; indistinguishable from sycophancy at the surface
- ECE `lesson term` — Gap between predicted probability and empirical accuracy; rises under sycophancy training
- Stated premise `lesson term` — What the prompt asserts as given; target of sycophantic amplification

## Ships

- [[Artifacts/18-04 sycophancy-probe|sycophancy-probe]] `skill` — Generate matched user-belief / third-party-belief prompts and score a model's sycophancy.

## Further reading

- Perez et al. — Discovering Language Model Behaviors with Model-Written Evaluations (ACL 2023, arXiv:2212.09251) ([link](https://arxiv.org/abs/2212.09251)) — early evidence sycophancy scales with RLHF
- Sharma et al. — Towards Understanding Sycophancy in Language Models (ICLR 2024, arXiv:2310.13548) ([link](https://arxiv.org/abs/2310.13548)) — sycophancy scales with model size
- Shapira et al. — How RLHF Amplifies Sycophancy (arXiv:2602.01002, Feb 2026) ([link](https://arxiv.org/abs/2602.01002)) — the two-stage formal mechanism and agreement-penalty correction
- Sahoo et al. — Calibration Collapse Under Sycophantic Training (arXiv:2604.10585) ([link](https://arxiv.org/abs/2604.10585)) — ECE analysis
- Cheng, Tramel et al. — Sycophancy in Frontier LLMs at Scale (Science, March 2026) ([link](https://www.science.org/doi/10.1126/science.abj8891)) — 11-model 49% affirmation measurement


%% ── my notes ── %%
