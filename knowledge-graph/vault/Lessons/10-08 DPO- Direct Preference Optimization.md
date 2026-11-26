---
id: "lesson:10/08"
type: lesson
ref: 10/08
phase: 10
num: 8
title: "DPO: Direct Preference Optimization"
lesson_type: build
languages:
  - Python
time_min: 90
status: planned
status_auto: planned
on_route: true
route_order: 8
quiz_count: 0
code_files: 1
concepts: 10
prereqs: 1
community: 45
libraries:
  - numpy
aliases:
  - 10/08
  - 10-08
tags:
  - phase/10
  - type/build
  - status/planned
  - route
  - community/45
source: ai-engineering-from-scratch/phases/10-llms-from-scratch/08-dpo/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/10-llms-from-scratch/08-dpo"
---

# 10/08 DPO: Direct Preference Optimization

> RLHF works. It also requires training three models (SFT, reward model, policy), managing PPO's instability, and tuning a KL penalty. DPO asks: what if you could skip all of that? DPO directly optimizes the language model on preference pairs. No reward model. No PPO. One training loop. Same results.

**Phase:** [[Phases/10 LLMs from Scratch|Phase 10: LLMs from Scratch]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** planned  
**Open:** [[Upstream/10-llms-from-scratch/08-dpo/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/10-llms-from-scratch/08-dpo) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/10-llms-from-scratch/08-dpo) · code: main.py  
**Community:** [[Communities/45 Implicit reward · KTO · ORPO|45 Implicit reward · KTO · ORPO]] · **Libraries:** [[Libraries/numpy (python)|numpy]]  

## Prerequisites

Stated upstream: `Phase 10, Lesson 07 (RLHF)`

- [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]] — RLHF

### Bridges to check first (my plan)

- [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]] — probability (Bradley-Terry, log-likelihood)

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]], [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]], [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]], [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]], [[Lessons/09-01 MDPs, States, Actions & Rewards|09/01 MDPs, States, Actions & Rewards]], [[Lessons/09-06 Policy Gradient — REINFORCE from Scratch|09/06 Policy Gradient — REINFORCE from Scratch]], [[Lessons/09-08 Proximal Policy Optimization (PPO)|09/08 Proximal Policy Optimization (PPO)]], [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]]
- depth 3: [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/09-03 Monte Carlo Methods — Learning from Complete Episodes|09/03 Monte Carlo Methods — Learning from Complete Episodes]], [[Lessons/09-04 Temporal Difference — Q-Learning & SARSA|09/04 Temporal Difference — Q-Learning & SARSA]], [[Lessons/09-07 Actor-Critic — A2C and A3C|09/07 Actor-Critic — A2C and A3C]], [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]]

## Builds on this

- [[Lessons/10-09 Constitutional AI and Self-Improvement|10/09 Constitutional AI and Self-Improvement]]
- [[Lessons/10-11 Quantization- Making Models Fit|10/11 Quantization: Making Models Fit]]
- [[Lessons/10-12 Inference Optimization|10/12 Inference Optimization]]
- [[Lessons/10-13 Building a Complete LLM Pipeline|10/13 Building a Complete LLM Pipeline]]
- [[Lessons/18-01 Instruction-Following as Alignment Signal|18/01 Instruction-Following as Alignment Signal]]
- [[Lessons/18-03 The Direct Preference Optimization Family|18/03 The Direct Preference Optimization Family]]

## Concepts taught

- [[Concepts/DPO (Direct Preference Optimization)|DPO (Direct Preference Optimization)]] (as *DPO*) `glossary` — Direct Preference Optimization: a supervised learning algorithm that optimizes the language model directly on preference pairs, bypassing the reward model and PPO
- [[Concepts/Implicit reward|Implicit reward]] `lesson term` — The reward function is determined by the log-probability ratio between the policy and reference models -- no separate reward model needed
- Log-probability ratio `lesson term` — log pi(y|x) - log pi_ref(y|x) -- positive means the current model assigns higher probability than the reference
- [[Concepts/Reference model|Reference model]] `lesson term` — A copy of the SFT model whose weights never change -- serves as the anchor for computing probability ratios
- [[Concepts/KTO|KTO]] `lesson term` — Kahneman-Tversky Optimization: works with unpaired "good" or "bad" labels instead of requiring preference pairs
- [[Concepts/ORPO|ORPO]] `lesson term` — Odds Ratio Preference Optimization: combines SFT and alignment into a single training loop by adding a preference term to the SFT loss
- [[Concepts/SimPO|SimPO]] `lesson term` — Simple Preference Optimization: eliminates the reference model by using length-normalized average log-probability as the implicit reward
- [[Concepts/Alignment tax|Alignment tax]] `lesson term` — The additional compute, data, and complexity required to go from a base model to an aligned model -- DPO reduces this significantly

## Ships

- [[Artifacts/10-08 prompt-alignment-method-selector|prompt-alignment-method-selector]] `prompt` — Choose the right alignment method (SFT, RLHF, DPO, KTO, ORPO, SimPO) for your use case

## Further reading

- [[Resources/Direct Preference Optimization paper|Direct Preference Optimization paper]] ([link](https://arxiv.org/abs/2305.18290)) — the DPO paper that simplified alignment from RLHF to supervised learning ·  also cited by 3 other lessons
- Tunstall et al., 2023 -- "Zephyr: Direct Distillation of LM Alignment ([link](https://arxiv.org/abs/2310.16944)) — Zephyr-7B, showing DPO on UltraFeedback matches RLHF on benchmarks
- [[Resources/Ethayarajh et al., 2024 - -KTO- Model Alignment as Prospect Theoretic Optimization|Ethayarajh et al., 2024 -- "KTO: Model Alignment as Prospect Theoretic Optimization]] ([link](https://arxiv.org/abs/2402.01306)) — eliminating the need for paired preferences ·  also cited by 1 other lesson
- [[Resources/Hong et al., 2024 - -ORPO- Monolithic Preference Optimization without Reference Model|Hong et al., 2024 -- "ORPO: Monolithic Preference Optimization without Reference Model]] ([link](https://arxiv.org/abs/2403.07691)) — combining SFT and alignment in one step ·  also cited by 1 other lesson
- [[Resources/Meng et al., 2024 - -SimPO- Simple Preference Optimization with a Reference-Free Reward|Meng et al., 2024 -- "SimPO: Simple Preference Optimization with a Reference-Free Reward]] ([link](https://arxiv.org/abs/2405.14734)) — eliminating the reference model entirely ·  also cited by 1 other lesson
- [[Resources/Llama 3 paper (Meta, 2024)|Llama 3 paper (Meta, 2024)]] ([link](https://arxiv.org/abs/2407.21783)) — Meta's alignment pipeline combining RLHF and DPO ·  also cited by 7 other lessons

## My route

- Step 8 in *Route: Phase 10 core (about 20 h, plus bridges)*
- Plan note: DPO
- Previous: [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]]
- Next: [[Lessons/10-09 Constitutional AI and Self-Improvement|10/09 Constitutional AI and Self-Improvement]]


%% ── my notes ── %%
