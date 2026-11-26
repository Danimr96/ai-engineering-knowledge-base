---
id: "concept:reward-hacking"
type: concept
name: Reward hacking
canonical: false
taught_in: 3
community: 1
tags:
  - concept/lesson-term
  - community/01
source: ai-engineering-from-scratch/phases/09-reinforcement-learning/09-reward-modeling-rlhf/docs/en.md
---

# Reward hacking

**Community:** [[Communities/01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism|01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism]]

> *What people say:* "Goodhart's law"

**What it actually means:** Policy exploits RM flaws; symptoms: reward up, human eval flat.

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/09-09 Reward Modeling & RLHF|09/09 Reward Modeling & RLHF]]
- [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]] — When the policy finds degenerate high-reward outputs by exploiting weaknesses in the reward model instead of genuinely improving
- [[Lessons/15-03 AlphaEvolve — Evolutionary Coding Agents|15/03 AlphaEvolve — Evolutionary Coding Agents]] — Loop finds a way to maximize score without doing the intended task


%% ── my notes ── %%
