---
id: "concept:bradley-terry"
type: concept
name: Bradley-Terry
canonical: false
taught_in: 3
community: 1
tags:
  - concept/lesson-term
  - community/01
source: ai-engineering-from-scratch/phases/09-reinforcement-learning/09-reward-modeling-rlhf/docs/en.md
---

# Bradley-Terry

**Community:** [[Communities/01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism|01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism]]

> *What people say:* "Pairwise logistic loss"

**What it actually means:** P(y+ ≻ y-) = σ(R(y+) - R(y-)); the standard RM objective.

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/09-09 Reward Modeling & RLHF|09/09 Reward Modeling & RLHF]]
- [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]] — A probabilistic model where P(A > B) = sigmoid(score(A) - score(B)), converting pairwise preferences into a consistent scoring function
- [[Lessons/18-01 Instruction-Following as Alignment Signal|18/01 Instruction-Following as Alignment Signal]] — -log sigmoid(r_w - r_l); reduces pairwise ranking to binary classification


%% ── my notes ── %%
