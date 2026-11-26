---
id: "concept:reward-model"
type: concept
name: Reward Model
canonical: false
aliases:
  - RM
taught_in: 3
community: 75
tags:
  - concept/lesson-term
  - community/75
source: ai-engineering-from-scratch/phases/09-reinforcement-learning/09-reward-modeling-rlhf/docs/en.md
---

# Reward Model

**Community:** [[Communities/75 L2 regularization · PRM · Reward Model|75 L2 regularization · PRM · Reward Model]]

> *What people say:* "The scoring net"

**What it actually means:** Learned scalar function fit to pairwise preferences via Bradley-Terry.

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/09-09 Reward Modeling & RLHF|09/09 Reward Modeling & RLHF]]
- [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]] — A transformer with a scalar output head, trained on pairwise human preferences using the Bradley-Terry loss
- [[Lessons/18-01 Instruction-Following as Alignment Signal|18/01 Instruction-Following as Alignment Signal]] — Scalar regressor over (prompt, response) trained with Bradley-Terry on pairwise labels


%% ── my notes ── %%
