---
id: "lesson:18/01"
type: lesson
ref: 18/01
phase: 18
num: 1
title: Instruction-Following as Alignment Signal
lesson_type: learn
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 6
code_files: 1
concepts: 7
prereqs: 3
community: 32
aliases:
  - 18/01
  - 18-01
tags:
  - phase/18
  - type/learn
  - community/32
  - stdlib-only
source: ai-engineering-from-scratch/phases/18-ethics-safety-alignment/01-instruction-following-alignment-signal/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/01-instruction-following-alignment-signal"
---

# 18/01 Instruction-Following as Alignment Signal

> Every later critique of RLHF argues against this pipeline. Before you study how optimization pressure distorts a proxy, you have to see the proxy. InstructGPT (Ouyang et al., 2022) defined the reference architecture: supervised fine-tuning on instruction-response pairs, a reward model trained on pairwise preference rankings, and PPO against the reward model with a KL penalty to the SFT policy. A 1.3B InstructGPT was preferred over a 175B GPT-3. That single result is the reason every frontier lab in 2026 still ships an RLHF-shaped post-training pipeline.

**Phase:** [[Phases/18 Ethics, Safety & Alignment|Phase 18: Ethics, Safety & Alignment]] · **Type:** Learn · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/18-ethics-safety-alignment/01-instruction-following-alignment-signal/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/01-instruction-following-alignment-signal) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/18-ethics-safety-alignment/01-instruction-following-alignment-signal) · code: main.py · quiz: 6 questions  
**Community:** [[Communities/32 Instruction-Following as Alignment Signal · Reward Hacking and Goodhart's Law · Sycophancy as RLHF Amplific|32 Instruction-Following as Alignment Signal · Reward Hacking and Goodhart's Law · Sycophancy as RLHF Amplification]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 10 · 06 (SFT), Phase 10 · 07 (RLHF), Phase 10 · 08 (DPO)`

- [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]] — SFT
- [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]] — RLHF
- [[Lessons/10-08 DPO- Direct Preference Optimization|10/08 DPO: Direct Preference Optimization]] — DPO

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/09-01 MDPs, States, Actions & Rewards|09/01 MDPs, States, Actions & Rewards]], [[Lessons/09-06 Policy Gradient — REINFORCE from Scratch|09/06 Policy Gradient — REINFORCE from Scratch]], [[Lessons/09-08 Proximal Policy Optimization (PPO)|09/08 Proximal Policy Optimization (PPO)]], [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]]
- depth 3: [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]], [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]], [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]], [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]], [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/09-03 Monte Carlo Methods — Learning from Complete Episodes|09/03 Monte Carlo Methods — Learning from Complete Episodes]], [[Lessons/09-04 Temporal Difference — Q-Learning & SARSA|09/04 Temporal Difference — Q-Learning & SARSA]], [[Lessons/09-07 Actor-Critic — A2C and A3C|09/07 Actor-Critic — A2C and A3C]], [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]], [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]], [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]]

## Builds on this

- [[Lessons/18-02 Reward Hacking and Goodhart's Law|18/02 Reward Hacking and Goodhart's Law]]
- [[Lessons/18-03 The Direct Preference Optimization Family|18/03 The Direct Preference Optimization Family]]
- [[Lessons/18-04 Sycophancy as RLHF Amplification|18/04 Sycophancy as RLHF Amplification]]
- [[Lessons/18-05 Constitutional AI and RLAIF|18/05 Constitutional AI and RLAIF]]
- [[Lessons/18-06 Mesa-Optimization and Deceptive Alignment|18/06 Mesa-Optimization and Deceptive Alignment]]
- [[Lessons/18-11 Scalable Oversight and Weak-to-Strong Generalization|18/11 Scalable Oversight and Weak-to-Strong Generalization]]
- [[Lessons/18-12 Red-Teaming- PAIR and Automated Attacks|18/12 Red-Teaming: PAIR and Automated Attacks]]
- [[Lessons/18-20 Bias and Representational Harm in LLMs|18/20 Bias and Representational Harm in LLMs]]
- [[Lessons/18-28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR|18/28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR]]

## Concepts taught

- [[Concepts/SFT (Supervised Fine-Tuning)|SFT (Supervised Fine-Tuning)]] (as *SFT*) `glossary` — Stage 1: cross-entropy fine-tune on prompt-response pairs
- [[Concepts/Reward Model|Reward Model]] `lesson term` — Scalar regressor over (prompt, response) trained with Bradley-Terry on pairwise labels
- [[Concepts/Bradley-Terry|Bradley-Terry]] `lesson term` — -log sigmoid(r_w - r_l); reduces pairwise ranking to binary classification
- [[Concepts/KL penalty|KL penalty]] `lesson term` — beta KL(pi || pi_SFT) — keeps the RL policy near the SFT anchor
- PPO-ptx `lesson term` — Adds a fraction of pre-training log-likelihood to the PPO objective to offset the alignment tax
- [[Concepts/Alignment tax|Alignment tax]] `lesson term` — Post-RLHF drop on standard benchmarks that RLHF did not target
- Labeler preference `lesson term` — Sample of human rankings; the RM is a statistical proxy for this, not for "human values"

## Ships

- [[Artifacts/18-01 instructgpt-explainer|instructgpt-explainer]] `skill` — Diagnose an RLHF-family paper or pipeline against the three-stage InstructGPT reference.

## Further reading

- [[Resources/Christiano et al. (2017). Deep Reinforcement Learning from Human Preferences|Christiano et al. (2017). Deep Reinforcement Learning from Human Preferences]] ([link](https://arxiv.org/abs/1706.03741)) — the original preference-based RL formulation ·  also cited by 2 other lessons
- [[Resources/Stiennon et al. (2020). Learning to summarize with human feedback|Stiennon et al. (2020). Learning to summarize with human feedback]] ([link](https://arxiv.org/abs/2009.01325)) — the RLHF-for-summarization predecessor ·  also cited by 2 other lessons
- [[Resources/InstructGPT paper|InstructGPT paper]] ([link](https://arxiv.org/abs/2203.02155)) — the InstructGPT paper, foundation for every RLHF pipeline that followed ·  also cited by 4 other lessons
- [[Resources/Anthropic RLHF paper (Bai et al. 2022). Training a Helpful and Harmless Assistant|Anthropic RLHF paper (Bai et al. 2022). Training a Helpful and Harmless Assistant]] ([link](https://arxiv.org/abs/2204.05862)) — Anthropic's HH extension of the InstructGPT pipeline ·  also cited by 2 other lessons


%% ── my notes ── %%
