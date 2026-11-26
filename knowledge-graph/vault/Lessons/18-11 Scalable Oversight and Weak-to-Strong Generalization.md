---
id: "lesson:18/11"
type: lesson
ref: 18/11
phase: 18
num: 11
title: Scalable Oversight and Weak-to-Strong Generalization
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 6
code_files: 1
concepts: 7
prereqs: 2
community: 32
aliases:
  - 18/11
  - 18-11
tags:
  - phase/18
  - type/learn
  - community/32
  - stdlib-only
source: ai-engineering-from-scratch/phases/18-ethics-safety-alignment/11-scalable-oversight-weak-to-strong/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/11-scalable-oversight-weak-to-strong"
---

# 18/11 Scalable Oversight and Weak-to-Strong Generalization

> Burns et al. (OpenAI Superalignment, "Weak-to-Strong Generalization", 2023) proposed a proxy for the superalignment problem: fine-tune a strong model using labels produced by a weaker model. If the strong model generalizes correctly from imperfect weak supervision, current human-scale alignment methods may extend to superhuman systems. Scalable oversight and W2SG are complementary. Scalable oversight (debate, recursive reward modeling, task decomposition) increases the overseer's effective capability so it can keep up with the model under oversight. W2SG ensures the strong model generalizes correctly from whatever imperfect supervision the overseer provides. Debate Helps W2SG (arXiv:2501.13124, January 2025) combines them.

**Phase:** [[Phases/18 Ethics, Safety & Alignment|Phase 18: Ethics, Safety & Alignment]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/18-ethics-safety-alignment/11-scalable-oversight-weak-to-strong/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/11-scalable-oversight-weak-to-strong) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/18-ethics-safety-alignment/11-scalable-oversight-weak-to-strong) · code: main.py · quiz: 6 questions  
**Community:** [[Communities/32 Instruction-Following as Alignment Signal · Reward Hacking and Goodhart's Law · Sycophancy as RLHF Amplific|32 Instruction-Following as Alignment Signal · Reward Hacking and Goodhart's Law · Sycophancy as RLHF Amplification]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 18 · 01 (instruction-following), Phase 18 · 10 (AI Control), Phase 09 (RL foundations)`

- [[Lessons/18-01 Instruction-Following as Alignment Signal|18/01 Instruction-Following as Alignment Signal]] — instruction-following
- [[Lessons/18-10 AI Control — Safety Despite Subversion|18/10 AI Control — Safety Despite Subversion]] — AI Control
- Whole phase: [[Phases/09 Reinforcement Learning|Phase 9: Reinforcement Learning]] — RL foundations ·  medium confidence

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]], [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]], [[Lessons/10-08 DPO- Direct Preference Optimization|10/08 DPO: Direct Preference Optimization]], [[Lessons/18-07 Sleeper Agents — Persistent Deception|18/07 Sleeper Agents — Persistent Deception]], [[Lessons/18-08 In-Context Scheming in Frontier Models|18/08 In-Context Scheming in Frontier Models]], [[Lessons/18-09 Alignment Faking|18/09 Alignment Faking]]
- depth 3: [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/09-01 MDPs, States, Actions & Rewards|09/01 MDPs, States, Actions & Rewards]], [[Lessons/09-06 Policy Gradient — REINFORCE from Scratch|09/06 Policy Gradient — REINFORCE from Scratch]], [[Lessons/09-08 Proximal Policy Optimization (PPO)|09/08 Proximal Policy Optimization (PPO)]], [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]], [[Lessons/18-06 Mesa-Optimization and Deceptive Alignment|18/06 Mesa-Optimization and Deceptive Alignment]]

## Builds on this

- [[Lessons/18-28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR|18/28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR]]

## Concepts taught

- Scalable oversight `lesson term` — Mechanisms that increase an overseer's ability to evaluate a more-capable model
- W2SG `lesson term` — Fine-tuning a strong model on weak labels and measuring the capability recovered
- PGR `lesson term` — (fine-tuned - weak) / (ceiling - weak); 1.0 = fully closed, 0 = no help
- [[Concepts/Debate|Debate]] `lesson term` — Scalable oversight mechanism where a weak judge picks between two U defenders
- RRM `lesson term` — U helps train the reward model for U+1; overseer capability tracks U
- Task decomposition `lesson term` — Break a hard task into sub-tasks the human can verify, recursively
- Superalignment `lesson term` — The research agenda concerned with aligning models the human cannot directly evaluate

## Ships

- [[Artifacts/18-11 w2sg-pgr|w2sg-pgr]] `skill` — Audit a scalable-oversight or W2SG claim via the performance-gap-recovered metric.

## Further reading

- Irving, Christiano, Amodei — AI safety via debate (arXiv:1805.00899) ([link](https://arxiv.org/abs/1805.00899)) — the debate mechanism
- Leike et al. — Scalable agent alignment via reward modeling (arXiv:1811.07871) ([link](https://arxiv.org/abs/1811.07871)) — recursive reward modeling
- Khan et al. — Debating with More Persuasive LLMs Leads to More Truthful Answers (arXiv:2402.06782) ([link](https://arxiv.org/abs/2402.06782)) — 2024 empirical study of debate with stronger debaters
- Lang et al. — Debate Helps Weak-to-Strong Generalization (arXiv:2501.13124) ([link](https://arxiv.org/abs/2501.13124)) — 2025 combination of debate + W2SG
- [[Resources/Burns et al. (2023). Weak-to-Strong Generalization (OpenAI)|Burns et al. (2023). Weak-to-Strong Generalization (OpenAI)]] ([link](https://openai.com/index/weak-to-strong-generalization/)) — the W2SG paper ·  also cited by 1 other lesson


%% ── my notes ── %%
