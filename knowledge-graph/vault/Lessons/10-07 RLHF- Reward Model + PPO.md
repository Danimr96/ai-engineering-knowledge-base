---
id: "lesson:10/07"
type: lesson
ref: 10/07
phase: 10
num: 7
title: "RLHF: Reward Model + PPO"
lesson_type: build
languages:
  - Python
time_min: 90
status: planned
status_auto: planned
on_route: true
route_order: 7
quiz_count: 0
code_files: 1
concepts: 10
prereqs: 1
community: 1
libraries:
  - numpy
aliases:
  - 10/07
  - 10-07
tags:
  - phase/10
  - type/build
  - status/planned
  - route
  - community/01
source: ai-engineering-from-scratch/phases/10-llms-from-scratch/07-rlhf/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/10-llms-from-scratch/07-rlhf"
---

# 10/07 RLHF: Reward Model + PPO

> SFT teaches the model to follow instructions. But it doesn't teach the model which response is BETTER. Two grammatically correct, factually accurate answers can differ enormously in helpfulness. RLHF is how you encode human judgment into the model's behavior. It's what makes Claude helpful and GPT polite.

**Phase:** [[Phases/10 LLMs from Scratch|Phase 10: LLMs from Scratch]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** planned  
**Open:** [[Upstream/10-llms-from-scratch/07-rlhf/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/10-llms-from-scratch/07-rlhf) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/10-llms-from-scratch/07-rlhf) · code: main.py  
**Community:** [[Communities/01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism|01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism]] · **Libraries:** [[Libraries/numpy (python)|numpy]]  

## Prerequisites

Stated upstream: `Phase 10, Lesson 06 (Instruction Tuning / SFT)`

- [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]] — Instruction Tuning / SFT

### Bridges to check first (my plan)

- [[Lessons/09-01 MDPs, States, Actions & Rewards|09/01 MDPs, States, Actions & Rewards]] — MDPs
- [[Lessons/09-06 Policy Gradient — REINFORCE from Scratch|09/06 Policy Gradient — REINFORCE from Scratch]] — policy gradients
- [[Lessons/09-08 Proximal Policy Optimization (PPO)|09/08 Proximal Policy Optimization (PPO)]] — PPO

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/09-03 Monte Carlo Methods — Learning from Complete Episodes|09/03 Monte Carlo Methods — Learning from Complete Episodes]], [[Lessons/09-04 Temporal Difference — Q-Learning & SARSA|09/04 Temporal Difference — Q-Learning & SARSA]], [[Lessons/09-07 Actor-Critic — A2C and A3C|09/07 Actor-Critic — A2C and A3C]], [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]]
- depth 3: [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]], [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]], [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]], [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]], [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/09-02 Dynamic Programming — Policy Iteration & Value Iteration|09/02 Dynamic Programming — Policy Iteration & Value Iteration]], [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]], [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]], [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]]

## Builds on this

- [[Lessons/10-08 DPO- Direct Preference Optimization|10/08 DPO: Direct Preference Optimization]]
- [[Lessons/10-09 Constitutional AI and Self-Improvement|10/09 Constitutional AI and Self-Improvement]]
- [[Lessons/10-11 Quantization- Making Models Fit|10/11 Quantization: Making Models Fit]]
- [[Lessons/10-12 Inference Optimization|10/12 Inference Optimization]]
- [[Lessons/10-13 Building a Complete LLM Pipeline|10/13 Building a Complete LLM Pipeline]]
- [[Lessons/18-01 Instruction-Following as Alignment Signal|18/01 Instruction-Following as Alignment Signal]]
- [[Lessons/18-02 Reward Hacking and Goodhart's Law|18/02 Reward Hacking and Goodhart's Law]]
- [[Lessons/18-07 Sleeper Agents — Persistent Deception|18/07 Sleeper Agents — Persistent Deception]]

## Concepts taught

- [[Concepts/RLHF (Reinforcement Learning from Human Feedback)|RLHF (Reinforcement Learning from Human Feedback)]] (as *RLHF*) `glossary` — Reinforcement Learning from Human Feedback: a three-stage pipeline (SFT, reward model, PPO) that optimizes language model outputs using human preference signals
- [[Concepts/Reward Model|Reward Model]] `lesson term` — A transformer with a scalar output head, trained on pairwise human preferences using the Bradley-Terry loss
- [[Concepts/Bradley-Terry|Bradley-Terry]] `lesson term` — A probabilistic model where P(A > B) = sigmoid(score(A) - score(B)), converting pairwise preferences into a consistent scoring function
- PPO `lesson term` — Proximal Policy Optimization: updates the policy to maximize reward while clipping the update magnitude to prevent instability
- [[Concepts/KL divergence|KL divergence]] `lesson term` — A measure of the difference between the policy model's token distribution and the reference model's -- used as a penalty to prevent reward hacking
- [[Concepts/KL penalty|KL penalty]] `lesson term` — Beta KL(policy || reference) subtracted from the reward signal -- prevents the policy from diverging too far from the SFT checkpoint
- [[Concepts/Reward hacking|Reward hacking]] `lesson term` — When the policy finds degenerate high-reward outputs by exploiting weaknesses in the reward model instead of genuinely improving
- Preference pair `lesson term` — A training example consisting of (prompt, preferred_response, rejected_response) -- the fundamental unit of RLHF training data
- [[Concepts/Reference model|Reference model]] `lesson term` — A copy of the SFT model whose weights never change -- used as the anchor for KL divergence computation

## Ships

- [[Artifacts/10-07 prompt-reward-model-designer|prompt-reward-model-designer]] `prompt` — Design reward model training pipelines for RLHF alignment

## Further reading

- [[Resources/Christiano et al. (2017). Deep Reinforcement Learning from Human Preferences|Christiano et al. (2017). Deep Reinforcement Learning from Human Preferences]] ([link](https://arxiv.org/abs/1706.03741)) — the foundational work on learning reward functions from human comparisons ·  also cited by 2 other lessons
- [[Resources/Schulman et al. (2017). Proximal Policy Optimization Algorithms|Schulman et al. (2017). Proximal Policy Optimization Algorithms]] ([link](https://arxiv.org/abs/1707.06347)) — the original PPO paper from OpenAI ·  also cited by 1 other lesson
- [[Resources/Stiennon et al. (2020). Learning to summarize with human feedback|Stiennon et al. (2020). Learning to summarize with human feedback]] ([link](https://arxiv.org/abs/2009.01325)) — RLHF applied to summarization, showing reward models can capture nuanced quality judgments ·  also cited by 2 other lessons
- [[Resources/InstructGPT paper|InstructGPT paper]] ([link](https://arxiv.org/abs/2203.02155)) — the paper that made RLHF practical for large language models ·  also cited by 4 other lessons
- [[Resources/Anthropic RLHF paper (Bai et al. 2022). Training a Helpful and Harmless Assistant|Anthropic RLHF paper (Bai et al. 2022). Training a Helpful and Harmless Assistant]] ([link](https://arxiv.org/abs/2204.05862)) — Anthropic's RLHF paper with detailed analysis of reward hacking and KL penalty ·  also cited by 2 other lessons

## My route

- Step 7 in *Route: Phase 10 core (about 20 h, plus bridges)*
- Plan note: RLHF: reward model and PPO
- Previous: [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]]
- Next: [[Lessons/10-08 DPO- Direct Preference Optimization|10/08 DPO: Direct Preference Optimization]]


%% ── my notes ── %%
