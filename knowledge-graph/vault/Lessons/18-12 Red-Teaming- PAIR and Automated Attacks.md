---
id: "lesson:18/12"
type: lesson
ref: 18/12
phase: 18
num: 12
title: "Red-Teaming: PAIR and Automated Attacks"
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 6
code_files: 1
concepts: 7
prereqs: 1
community: 23
aliases:
  - 18/12
  - 18-12
tags:
  - phase/18
  - type/build
  - community/23
  - stdlib-only
source: ai-engineering-from-scratch/phases/18-ethics-safety-alignment/12-red-teaming-pair-automated-attacks/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/12-red-teaming-pair-automated-attacks"
---

# 18/12 Red-Teaming: PAIR and Automated Attacks

> Chao, Robey, Dobriban, Hassani, Pappas, Wong (NeurIPS 2023, arXiv:2310.08419). PAIR — Prompt Automatic Iterative Refinement — is the canonical automated black-box jailbreak. An attacker LLM with a red-team system prompt iteratively proposes jailbreaks for a target LLM, accumulating attempts and responses in its own chat history as in-context feedback. PAIR typically succeeds within 20 queries, orders of magnitude more efficient than GCG (Zou et al.'s token-level gradient search) and without requiring white-box access. PAIR is now a standard baseline in JailbreakBench (arXiv:2404.01318) and HarmBench, alongside GCG, AutoDAN, TAP, and Persuasive Adversarial Prompt.

**Phase:** [[Phases/18 Ethics, Safety & Alignment|Phase 18: Ethics, Safety & Alignment]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/18-ethics-safety-alignment/12-red-teaming-pair-automated-attacks/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/12-red-teaming-pair-automated-attacks) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/18-ethics-safety-alignment/12-red-teaming-pair-automated-attacks) · code: main.py · quiz: 6 questions  
**Community:** [[Communities/23 Automatic Speech Recognition (ASR) · Llama Guard · Homoglyph|23 Automatic Speech Recognition (ASR) · Llama Guard · Homoglyph]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 18 · 01 (instruction-following), Phase 14 (agent engineering)`

- [[Lessons/18-01 Instruction-Following as Alignment Signal|18/01 Instruction-Following as Alignment Signal]] — instruction-following
- Whole phase: [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] — agent engineering ·  medium confidence

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]], [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]], [[Lessons/10-08 DPO- Direct Preference Optimization|10/08 DPO: Direct Preference Optimization]]
- depth 3: [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/09-01 MDPs, States, Actions & Rewards|09/01 MDPs, States, Actions & Rewards]], [[Lessons/09-06 Policy Gradient — REINFORCE from Scratch|09/06 Policy Gradient — REINFORCE from Scratch]], [[Lessons/09-08 Proximal Policy Optimization (PPO)|09/08 Proximal Policy Optimization (PPO)]], [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]]

## Builds on this

- [[Lessons/18-13 Many-Shot Jailbreaking|18/13 Many-Shot Jailbreaking]]
- [[Lessons/18-14 ASCII Art and Visual Jailbreaks|18/14 ASCII Art and Visual Jailbreaks]]
- [[Lessons/18-15 Indirect Prompt Injection — Production Attack Surface|18/15 Indirect Prompt Injection — Production Attack Surface]]
- [[Lessons/18-16 Red-Team Tooling — Garak, Llama Guard, PyRIT|18/16 Red-Team Tooling — Garak, Llama Guard, PyRIT]]
- [[Lessons/18-28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR|18/28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR]]

## Concepts taught

- [[Concepts/PAIR|PAIR]] `lesson term` — Prompt Automatic Iterative Refinement; attacker-LLM + judge-LLM loop
- [[Concepts/GCG|GCG]] `lesson term` — White-box token-level gradient search for adversarial suffixes
- [[Concepts/Automatic Speech Recognition (ASR)|Automatic Speech Recognition (ASR)]] (as *Attack success rate (ASR)*) `glossary` — Primary metric; must be reported with query budget and judge identity
- Judge LLM `lesson term` — LLM that grades whether a response satisfies the harmful goal
- JailbreakBench `lesson term` — Standardized harmful-behaviour set with tagged categories
- HarmBench `lesson term` — 510 behaviours, functional + semantic harm tests
- [[Concepts/TAP|TAP]] `lesson term` — PAIR with branching + pruning; better ASR at higher compute

## Ships

- [[Artifacts/18-12 attack-audit|attack-audit]] `skill` — Audit a red-team evaluation report for attack coverage, budget, judge identity, and behaviour set.

## Further reading

- [[Resources/Universal and Transferable Adversarial Attacks on Aligned Language Models|Universal and Transferable Adversarial Attacks on Aligned Language Models]] ([link](https://arxiv.org/abs/2307.15043)) — GCG paper ·  also cited by 1 other lesson
- [[Resources/Chao et al. — Jailbreaking Black Box LLMs in Twenty Queries (arXiv-2310.08419)|Chao et al. — Jailbreaking Black Box LLMs in Twenty Queries (arXiv:2310.08419)]] ([link](https://arxiv.org/abs/2310.08419)) — PAIR paper, NeurIPS 2023 ·  also cited by 3 other lessons
- [[Resources/Mazeika et al. — HarmBench (ICML 2024)|Mazeika et al. — HarmBench (ICML 2024)]] ([link](https://arxiv.org/abs/2402.04249)) — broader evaluation ·  also cited by 1 other lesson
- Chao et al. — JailbreakBench (arXiv:2404.01318) ([link](https://arxiv.org/abs/2404.01318)) — standardized evaluation


%% ── my notes ── %%
