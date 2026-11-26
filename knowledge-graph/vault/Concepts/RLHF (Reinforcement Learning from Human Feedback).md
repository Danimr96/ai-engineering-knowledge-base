---
id: "concept:rlhf-reinforcement-learning-from-human-feedback"
type: concept
name: RLHF (Reinforcement Learning from Human Feedback)
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

# RLHF (Reinforcement Learning from Human Feedback)

**Community:** [[Communities/66 Alignment · DPO (Direct Preference Optimization) · RLHF (Reinforcement Learning from Human Feedback)|66 Alignment · DPO (Direct Preference Optimization) · RLHF (Reinforcement Learning from Human Feedback)]]

> *What people say:* Training a model from human preferences.

**What it actually means:** A family of pipelines that uses human feedback to learn a reward or preference signal and then optimizes a model policy against that signal. Implementations vary and need not all use the same reinforcement-learning algorithm.

**Common confusion:** RLHF optimizes a proxy learned from collected feedback. It does not guarantee broad alignment with every user or situation.

**Category:** [[Categories/Math & training|Math & training]]

## Related concepts

- [[Concepts/Alignment|Alignment]]
- [[Concepts/DPO (Direct Preference Optimization)|DPO (Direct Preference Optimization)]]
- [[Concepts/SFT (Supervised Fine-Tuning)|SFT (Supervised Fine-Tuning)]]

## Taught in

- [[Lessons/09-09 Reward Modeling & RLHF|09/09 Reward Modeling & RLHF]] `alias` — Three-stage SFT + RM + PPO pipeline (Christiano 2017, Ouyang 2022).
- [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]] — Reinforcement Learning from Human Feedback: a three-stage pipeline (SFT, reward model, PPO) that optimizes language model outputs using human preference signals

## Sources

- [[Resources/InstructGPT paper|InstructGPT paper]] ([link](https://arxiv.org/abs/2203.02155))


%% ── my notes ── %%
