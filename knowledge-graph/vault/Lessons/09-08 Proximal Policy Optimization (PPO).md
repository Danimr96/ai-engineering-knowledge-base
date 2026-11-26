---
id: "lesson:09/08"
type: lesson
ref: 09/08
phase: 9
num: 8
title: Proximal Policy Optimization (PPO)
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 2
community: 60
aliases:
  - 09/08
  - 09-08
tags:
  - phase/09
  - type/build
  - community/60
  - stdlib-only
source: ai-engineering-from-scratch/phases/09-reinforcement-learning/08-ppo/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/09-reinforcement-learning/08-ppo"
---

# 09/08 Proximal Policy Optimization (PPO)

> A2C throws away each rollout after one update. PPO wraps the policy gradient in a clipped importance ratio so you can do 10+ epochs on the same data without the policy exploding. Schulman et al. (2017). Still the default policy-gradient algorithm in 2026.

**Phase:** [[Phases/09 Reinforcement Learning|Phase 9: Reinforcement Learning]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/09-reinforcement-learning/08-ppo/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/09-reinforcement-learning/08-ppo) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/09-reinforcement-learning/08-ppo) · code: main.py  
**Community:** [[Communities/60 GRPO · KL penalty · League play|60 GRPO · KL penalty · League play]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 9 · 06 (REINFORCE), Phase 9 · 07 (Actor-Critic)`

- [[Lessons/09-06 Policy Gradient — REINFORCE from Scratch|09/06 Policy Gradient — REINFORCE from Scratch]] — REINFORCE
- [[Lessons/09-07 Actor-Critic — A2C and A3C|09/07 Actor-Critic — A2C and A3C]] — Actor-Critic

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/09-03 Monte Carlo Methods — Learning from Complete Episodes|09/03 Monte Carlo Methods — Learning from Complete Episodes]], [[Lessons/09-04 Temporal Difference — Q-Learning & SARSA|09/04 Temporal Difference — Q-Learning & SARSA]]
- depth 3: [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]], [[Lessons/09-01 MDPs, States, Actions & Rewards|09/01 MDPs, States, Actions & Rewards]], [[Lessons/09-02 Dynamic Programming — Policy Iteration & Value Iteration|09/02 Dynamic Programming — Policy Iteration & Value Iteration]]

## Builds on this

- [[Lessons/09-09 Reward Modeling & RLHF|09/09 Reward Modeling & RLHF]]
- [[Lessons/09-11 Sim-to-Real Transfer|09/11 Sim-to-Real Transfer]]
- [[Lessons/09-12 RL for Games — AlphaZero, MuZero, and the LLM-Reasoning Era|09/12 RL for Games — AlphaZero, MuZero, and the LLM-Reasoning Era]]

## Concepts taught

- Importance ratio `lesson term` — πθ(a|s) / πold(a|s); deviation from the policy that collected the data.
- Clipped surrogate `lesson term` — min(r·A, clip(r, 1-ε, 1+ε)·A); flat gradient past the clip on beneficial side.
- Trust region `lesson term` — Limit each update's KL to guarantee monotone improvement.
- [[Concepts/KL penalty|KL penalty]] `lesson term` — Alternative PPO: L - β · KL(πθ || πold). Adaptive β.
- Clip fraction `lesson term` — Diagnostic — should be 0.1-0.3; outside means mistuned.
- Multi-epoch training `lesson term` — K epochs on each rollout; variance cost traded for sample efficiency.
- On-policy-ish `lesson term` — PPO is nominally on-policy but K>1 epochs uses slightly-off-policy data safely.
- PPO-KL `lesson term` — KL-penalty variant; used in RLHF where KL-to-reference is already a constraint.

## Ships

- [[Artifacts/09-08 ppo-trainer|ppo-trainer]] `skill` — Produce a PPO training config and a diagnostic plan for a given environment.

## Further reading

- Schulman et al. (2015). Trust Region Policy Optimization ([link](https://arxiv.org/abs/1502.05477)) — TRPO, PPO's predecessor.
- [[Resources/Schulman et al. (2017). Proximal Policy Optimization Algorithms|Schulman et al. (2017). Proximal Policy Optimization Algorithms]] ([link](https://arxiv.org/abs/1707.06347)) — the paper. ·  also cited by 1 other lesson
- Engstrom et al. (2020). Implementation Matters in Deep Policy Gradients ([link](https://arxiv.org/abs/2005.12729)) — the "37 code-level optimizations" paper; which PPO tricks are load-bearing and which are folklore.
- Andrychowicz et al. (2021). What Matters In On-Policy RL? A Large-Scale Empirical Study ([link](https://arxiv.org/abs/2006.05990)) — every PPO hyperparameter ablated.
- [[Resources/InstructGPT paper|InstructGPT paper]] ([link](https://arxiv.org/abs/2203.02155)) — InstructGPT; the PPO-in-RLHF recipe. ·  also cited by 4 other lessons
- CleanRL PPO implementation ([link](https://github.com/vwxyzjn/cleanrl)) — reference single-file PPO used by many papers.
- Hugging Face TRL — PPOTrainer ([link](https://huggingface.co/docs/trl/main/en/ppo_trainer)) — the production recipe for PPO on language models; read alongside Lesson 09 (RLHF).
- OpenAI Spinning Up — PPO ([link](https://spinningup.openai.com/en/latest/algorithms/ppo.html)) — clean modern exposition with PyTorch.


%% ── my notes ── %%
