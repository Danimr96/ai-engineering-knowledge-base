---
id: "lesson:18/20"
type: lesson
ref: 18/20
phase: 18
num: 20
title: Bias and Representational Harm in LLMs
lesson_type: build
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 6
code_files: 1
concepts: 7
prereqs: 1
community: 32
aliases:
  - 18/20
  - 18-20
tags:
  - phase/18
  - type/build
  - community/32
  - stdlib-only
source: ai-engineering-from-scratch/phases/18-ethics-safety-alignment/20-bias-representational-harm/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/20-bias-representational-harm"
---

# 18/20 Bias and Representational Harm in LLMs

> Gallegos, Rossi, Barrow, Tanjim, Kim, Dernoncourt, Yu, Zhang, Ahmed (Computational Linguistics 2024, arXiv:2309.00770). Foundational 2024 survey distinguishing representational harms (stereotypes, erasure) from allocational harms (unequal resource distribution) and categorizing evaluation metrics as embedding-based, probability-based, or generated-text-based. 2024-2025 empirical: An et al. (PNAS Nexus, March 2025) measure intersectional gender x race bias across GPT-3.5 Turbo, GPT-4o, Gemini 1.5 Flash, Claude 3.5 Sonnet, Llama 3-70B on automated resume evaluation for 20 entry-level jobs. WinoIdentity (COLM 2025, arXiv:2508.07111) introduces uncertainty-based fairness evaluation for intersectional identities. Yu & Ananiadou 2025 identify gender neurons in MLP layers; Ahsan & Wallace 2025 use SAEs to reveal clinical racial bias; Zhou et al. 2024 (UniBias) manipulates attention heads for debiasing. Meta-critique (arXiv:2508.11067): 10-year literature disproportionately focuses on binary-gender bias.

**Phase:** [[Phases/18 Ethics, Safety & Alignment|Phase 18: Ethics, Safety & Alignment]] · **Type:** Build · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/18-ethics-safety-alignment/20-bias-representational-harm/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/20-bias-representational-harm) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/18-ethics-safety-alignment/20-bias-representational-harm) · code: main.py · quiz: 6 questions  
**Community:** [[Communities/32 Instruction-Following as Alignment Signal · Reward Hacking and Goodhart's Law · Sycophancy as RLHF Amplific|32 Instruction-Following as Alignment Signal · Reward Hacking and Goodhart's Law · Sycophancy as RLHF Amplification]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 05 (word embeddings), Phase 18 · 01 (instruction following)`

- [[Lessons/18-01 Instruction-Following as Alignment Signal|18/01 Instruction-Following as Alignment Signal]] — instruction following
- Whole phase: [[Phases/05 NLP, Foundations to Advanced|Phase 5: NLP, Foundations to Advanced]] — word embeddings ·  medium confidence

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]], [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]], [[Lessons/10-08 DPO- Direct Preference Optimization|10/08 DPO: Direct Preference Optimization]]
- depth 3: [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/09-01 MDPs, States, Actions & Rewards|09/01 MDPs, States, Actions & Rewards]], [[Lessons/09-06 Policy Gradient — REINFORCE from Scratch|09/06 Policy Gradient — REINFORCE from Scratch]], [[Lessons/09-08 Proximal Policy Optimization (PPO)|09/08 Proximal Policy Optimization (PPO)]], [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]]

## Builds on this

- [[Lessons/18-21 Fairness Criteria — Group, Individual, Counterfactual|18/21 Fairness Criteria — Group, Individual, Counterfactual]]
- [[Lessons/18-28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR|18/28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR]]

## Concepts taught

- Representational harm `lesson term` — Biased portrayal of a group
- Allocational harm `lesson term` — Biased material outcome for a group
- WEAT `lesson term` — Word Embedding Association Test; co-occurrence-based bias probe
- Intersectionality `lesson term` — Bias that emerges at the intersection of multiple identity axes
- Gender neurons `lesson term` — Specific neurons whose activations correlate with gender-specific behaviour
- SAE feature `lesson term` — Sparse-autoencoder-identified feature; useful for mechanistic bias analysis
- UniBias `lesson term` — Zero-shot debiasing by reweighting attention heads

## Ships

- [[Artifacts/18-20 bias-eval|bias-eval]] `skill` — Audit a bias evaluation report across metric categories, intersectionality, and debias mechanism.

## Further reading

- An et al. — Intersectional resume-evaluation bias (PNAS Nexus, March 2025) ([link](https://academic.oup.com/pnasnexus/article/4/3/pgaf089/8111343)) — five-model intersectional study
- Gallegos et al. — Bias and Fairness in LLMs: A Survey (arXiv:2309.00770, Computational Linguistics 2024) ([link](https://arxiv.org/abs/2309.00770)) — canonical survey
- UniBias — attention-head manipulation (Zhou et al. 2024, ACL) ([link](https://arxiv.org/abs/2405.20612)) — zero-shot debiasing
- WinoIdentity — uncertainty-based intersectional fairness (arXiv:2508.07111, COLM 2025) ([link](https://arxiv.org/abs/2508.07111)) — new benchmark


%% ── my notes ── %%
