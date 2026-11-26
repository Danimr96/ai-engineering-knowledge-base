---
id: "lesson:10/09"
type: lesson
ref: 10/09
phase: 10
num: 9
title: Constitutional AI and Self-Improvement
lesson_type: build
languages:
  - Python
time_min: 45
status: planned
status_auto: planned
on_route: true
route_order: 9
quiz_count: 0
code_files: 1
concepts: 10
prereqs: 3
community: 1
libraries:
  - numpy
aliases:
  - 10/09
  - 10-09
tags:
  - phase/10
  - type/build
  - status/planned
  - route
  - community/01
source: ai-engineering-from-scratch/phases/10-llms-from-scratch/09-constitutional-ai-self-improvement/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/10-llms-from-scratch/09-constitutional-ai-self-improvement"
---

# 10/09 Constitutional AI and Self-Improvement

> RLHF needs humans in the loop. Constitutional AI replaces most of them with the model itself. Write a list of principles, have the model critique its own outputs against those principles, and train on the critiques. DeepSeek-R1 pushed this further in 2025: let the model generate millions of reasoning traces, grade them with a rule, and run GRPO on the outcome. Most of the "alignment work" in a 2026 frontier model is the model alignment itself. This lesson builds both loops.

**Phase:** [[Phases/10 LLMs from Scratch|Phase 10: LLMs from Scratch]] · **Type:** Build · **Time:** 45 min · **Languages:** Python · **Status:** planned  
**Open:** [[Upstream/10-llms-from-scratch/09-constitutional-ai-self-improvement/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/10-llms-from-scratch/09-constitutional-ai-self-improvement) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/10-llms-from-scratch/09-constitutional-ai-self-improvement) · code: main.py  
**Community:** [[Communities/01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism|01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism]] · **Libraries:** [[Libraries/numpy (python)|numpy]]  

## Prerequisites

Stated upstream: `Phase 10, Lessons 06-08 (SFT, RLHF, DPO)`

- **10/06-08** — SFT, RLHF, DPO:
    - [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]]
    - [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]]
    - [[Lessons/10-08 DPO- Direct Preference Optimization|10/08 DPO: Direct Preference Optimization]]

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/09-01 MDPs, States, Actions & Rewards|09/01 MDPs, States, Actions & Rewards]], [[Lessons/09-06 Policy Gradient — REINFORCE from Scratch|09/06 Policy Gradient — REINFORCE from Scratch]], [[Lessons/09-08 Proximal Policy Optimization (PPO)|09/08 Proximal Policy Optimization (PPO)]], [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]]
- depth 3: [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]], [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]], [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]], [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]], [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/09-03 Monte Carlo Methods — Learning from Complete Episodes|09/03 Monte Carlo Methods — Learning from Complete Episodes]], [[Lessons/09-04 Temporal Difference — Q-Learning & SARSA|09/04 Temporal Difference — Q-Learning & SARSA]], [[Lessons/09-07 Actor-Critic — A2C and A3C|09/07 Actor-Critic — A2C and A3C]], [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]], [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]], [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]]

## Builds on this

- [[Lessons/10-11 Quantization- Making Models Fit|10/11 Quantization: Making Models Fit]]
- [[Lessons/10-13 Building a Complete LLM Pipeline|10/13 Building a Complete LLM Pipeline]]

## Concepts taught

- [[Concepts/Constitutional AI|Constitutional AI]] `lesson term` — A two-stage pipeline (self-critique + RLAIF) that replaces most human preference labels with model self-judgments against a written constitution
- [[Concepts/RLAIF|RLAIF]] `lesson term` — Reinforcement Learning from AI Feedback -- PPO or DPO on preferences generated by the model itself
- [[Concepts/GRPO|GRPO]] `lesson term` — Group-Relative Policy Optimization -- sample G responses per prompt, use z-scored group rewards as advantages
- ORM `lesson term` — Outcome Reward Model -- a single scalar reward on the final answer only
- [[Concepts/PRM|PRM]] `lesson term` — Process Reward Model -- reward on every intermediate reasoning step, often trained from step-labeled data
- Rule-based reward `lesson term` — A verifier (regex, sympy, test suite) that returns a binary or numeric score without a learned model
- Rejection sampling FT `lesson term` — Sample many responses, filter to the highest-reward ones, add to SFT data, retrain
- [[Concepts/Mode collapse|Mode collapse]] `lesson term` — Post-training policy concentrates on a narrow region of the response space; measured as falling reward std across a group
- [[Concepts/KL budget|KL budget]] `lesson term` — The total KL divergence from the reference model that the optimizer is allowed to accumulate before training stops
- R1 moment `lesson term` — DeepSeek's reported behavior where a policy trained only on outcome rewards spontaneously developed self-checking and backtracking in its chain-of-thought

## Ships

- [[Artifacts/10-09 self-improvement-auditor|self-improvement-auditor]] `skill` — Audit a proposed self-improvement or constitutional AI pipeline before it runs at scale.

## Further reading

- [[Resources/Bai et al. (2022). Constitutional AI- Harmlessness from AI Feedback|Bai et al. (2022). Constitutional AI: Harmlessness from AI Feedback]] ([link](https://arxiv.org/abs/2212.08073)) — Anthropic's original CAI paper with the two-stage SL-CAI + RLAIF pipeline ·  also cited by 2 other lessons
- [[Resources/Lightman et al., 2023 - -Let's Verify Step by Step|Lightman et al., 2023 -- "Let's Verify Step by Step]] ([link](https://arxiv.org/abs/2305.20050)) — OpenAI's PRM800K and the case for process reward models ·  also cited by 2 other lessons
- Huang et al., 2024 -- "Large Language Models Cannot Self-Correct Reasoning Yet ([link](https://arxiv.org/abs/2310.01798)) — the skeptical counterpoint on self-improvement without external grounding
- Wang et al., 2024 -- "Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations ([link](https://arxiv.org/abs/2312.08935)) — auto-labeled PRM via Monte Carlo rollouts
- [[Resources/DeepSeek-AI (2024). DeepSeekMath- Pushing the Limits of Mathematical Reasoning in Open Language Models (GRPO)|DeepSeek-AI (2024). DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models (GRPO)]] ([link](https://arxiv.org/abs/2402.03300)) — introduces GRPO ·  also cited by 1 other lesson
- [[Resources/DeepSeek-AI (2025). DeepSeek-R1- Incentivizing Reasoning Capability in LLMs via Reinforcement Learning|DeepSeek-AI (2025). DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning]] ([link](https://arxiv.org/abs/2501.12948)) — R1 and R1-Zero, GRPO + rule rewards at scale ·  also cited by 4 other lessons

## My route

- Step 9 in *Route: Phase 10 core (about 20 h, plus bridges)*
- Plan note: Constitutional AI and self-improvement
- Previous: [[Lessons/10-08 DPO- Direct Preference Optimization|10/08 DPO: Direct Preference Optimization]]
- Next: [[Lessons/10-10 Evaluation- Benchmarks, Evals, LM Harness|10/10 Evaluation: Benchmarks, Evals, LM Harness]]


%% ── my notes ── %%
