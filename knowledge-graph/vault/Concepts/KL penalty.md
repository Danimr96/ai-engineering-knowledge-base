---
id: "concept:kl-penalty"
type: concept
name: KL penalty
canonical: false
taught_in: 4
community: 60
tags:
  - concept/lesson-term
  - community/60
source: ai-engineering-from-scratch/phases/09-reinforcement-learning/08-ppo/docs/en.md
---

# KL penalty

**Community:** [[Communities/60 GRPO · KL penalty · League play|60 GRPO · KL penalty · League play]]

> *What people say:* "Soft trust region"

**What it actually means:** Alternative PPO: L - β · KL(πθ || πold). Adaptive β.

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/09-08 Proximal Policy Optimization (PPO)|09/08 Proximal Policy Optimization (PPO)]]
- [[Lessons/09-09 Reward Modeling & RLHF|09/09 Reward Modeling & RLHF]] — β · KL(πθ || πref) in the reward; the anti-reward-hacking regularizer.
- [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]] — Beta KL(policy || reference) subtracted from the reward signal -- prevents the policy from diverging too far from the SFT checkpoint
- [[Lessons/18-01 Instruction-Following as Alignment Signal|18/01 Instruction-Following as Alignment Signal]] — beta KL(pi || pi_SFT) — keeps the RL policy near the SFT anchor


%% ── my notes ── %%
