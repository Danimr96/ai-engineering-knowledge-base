---
id: "concept:dpo-direct-preference-optimization"
type: concept
name: DPO (Direct Preference Optimization)
canonical: true
category: "Math & training"
taught_in: 2
community: 66
tags:
  - concept/glossary
  - category/math-and-training
  - community/66
source: ai-engineering-from-scratch/glossary/terms.md
---

# DPO (Direct Preference Optimization)

**Community:** [[Communities/66 Alignment · DPO (Direct Preference Optimization) · RLHF (Reinforcement Learning from Human Feedback)|66 Alignment · DPO (Direct Preference Optimization) · RLHF (Reinforcement Learning from Human Feedback)]]

> *What people say:* Preference training without a separate reward-model stage.

**What it actually means:** A preference-optimization objective that trains a policy directly from preferred and rejected response pairs relative to a reference policy. It avoids running an explicit reward model and reinforcement-learning loop during this stage.

**Common confusion:** DPO still depends on the quality and coverage of preference data and does not eliminate evaluation or alignment risk.

**Category:** [[Categories/Math & training|Math & training]]

## Related concepts

- [[Concepts/Alignment|Alignment]]
- [[Concepts/RLHF (Reinforcement Learning from Human Feedback)|RLHF (Reinforcement Learning from Human Feedback)]]
- [[Concepts/SFT (Supervised Fine-Tuning)|SFT (Supervised Fine-Tuning)]]

## Taught in

- [[Lessons/10-08 DPO- Direct Preference Optimization|10/08 DPO: Direct Preference Optimization]] — Direct Preference Optimization: a supervised learning algorithm that optimizes the language model directly on preference pairs, bypassing the reward model and PPO
- [[Lessons/18-03 The Direct Preference Optimization Family|18/03 The Direct Preference Optimization Family]] `alias` — Loss derived from the closed-form RLHF optimum; policy parameters only

## Sources

- [[Resources/Direct Preference Optimization paper|Direct Preference Optimization paper]] ([link](https://arxiv.org/abs/2305.18290))


%% ── my notes ── %%
