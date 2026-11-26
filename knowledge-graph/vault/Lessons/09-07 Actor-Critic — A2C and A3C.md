---
id: "lesson:09/07"
type: lesson
ref: 09/07
phase: 9
num: 7
title: "Actor-Critic — A2C and A3C"
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 2
community: 33
aliases:
  - 09/07
  - 09-07
tags:
  - phase/09
  - type/build
  - community/33
  - stdlib-only
source: ai-engineering-from-scratch/phases/09-reinforcement-learning/07-actor-critic-a2c-a3c/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/09-reinforcement-learning/07-actor-critic-a2c-a3c"
---

# 09/07 Actor-Critic — A2C and A3C

> REINFORCE is noisy. Add a critic that learns `V̂(s)`, subtract it from the return, and you get an advantage that has the same expectation but far lower variance. That is actor-critic. A2C runs it synchronously; A3C runs it across threads. Both are the mental model for every modern deep-RL method.

**Phase:** [[Phases/09 Reinforcement Learning|Phase 9: Reinforcement Learning]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/09-reinforcement-learning/07-actor-critic-a2c-a3c/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/09-reinforcement-learning/07-actor-critic-a2c-a3c) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/09-reinforcement-learning/07-actor-critic-a2c-a3c) · code: main.py  
**Community:** [[Communities/33 Advantage · Baseline · Actor|33 Advantage · Baseline · Actor]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 9 · 04 (TD Learning), Phase 9 · 06 (REINFORCE)`

- [[Lessons/09-04 Temporal Difference — Q-Learning & SARSA|09/04 Temporal Difference — Q-Learning & SARSA]] — TD Learning
- [[Lessons/09-06 Policy Gradient — REINFORCE from Scratch|09/06 Policy Gradient — REINFORCE from Scratch]] — REINFORCE

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/09-01 MDPs, States, Actions & Rewards|09/01 MDPs, States, Actions & Rewards]], [[Lessons/09-02 Dynamic Programming — Policy Iteration & Value Iteration|09/02 Dynamic Programming — Policy Iteration & Value Iteration]], [[Lessons/09-03 Monte Carlo Methods — Learning from Complete Episodes|09/03 Monte Carlo Methods — Learning from Complete Episodes]]
- depth 3: [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]], [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]]

## Builds on this

- [[Lessons/09-08 Proximal Policy Optimization (PPO)|09/08 Proximal Policy Optimization (PPO)]]
- [[Lessons/09-10 Multi-Agent RL|09/10 Multi-Agent RL]]

## Concepts taught

- [[Concepts/Actor|Actor]] `lesson term` — πθ(a|s), updated by policy gradient.
- [[Concepts/Critic|Critic]] `lesson term` — Vφ(s), updated by MSE regression to returns / TD targets.
- [[Concepts/Advantage|Advantage]] `lesson term` — A(s, a) = Q(s, a) - V(s) or its estimators. Multiplier for ∇ log π.
- TD residual `lesson term` — δt = r + γ V(s') - V(s); one-step advantage estimate.
- GAE `lesson term` — Exponentially weighted sum of n-step advantages, parameterized by λ.
- A2C `lesson term` — Batched across envs; one gradient step per rollout.
- A3C `lesson term` — Worker threads push gradients to a shared param server. Original paper; less common in 2026.
- [[Concepts/Bootstrap|Bootstrap]] `lesson term` — Truncate the rollout, add γ^n V(s{t+n}) to close the sum.

## Ships

- [[Artifacts/09-07 actor-critic-trainer|actor-critic-trainer]] `skill` — Produce an A2C / A3C / GAE configuration for a given environment, with advantage estimation and loss weights specified.

## Further reading

- Schulman et al. (2016). High-Dimensional Continuous Control Using Generalized Advantage Estimation ([link](https://arxiv.org/abs/1506.02438)) — GAE.
- Mnih et al. (2016). Asynchronous Methods for Deep Reinforcement Learning ([link](https://arxiv.org/abs/1602.01783)) — A3C, the original async actor-critic paper.
- Espeholt et al. (2018). IMPALA ([link](https://arxiv.org/abs/1802.01561)) — scalable distributed actor-critic with V-trace off-policy correction.
- [[Resources/Sutton & Barto (2018). Reinforcement Learning- An Introduction, 2nd ed|Sutton & Barto (2018). Reinforcement Learning: An Introduction, 2nd ed.]] ([link](http://incompleteideas.net/book/RLbook2020.pdf)) — foundations; pair this with Ch. 9 on function approximation when the critic is a neural net. ·  also cited by 10 other lessons
- Konda & Tsitsiklis (2000). Actor-Critic Algorithms ([link](https://papers.nips.cc/paper/1786-actor-critic-algorithms)) — the foundational convergence result for the two-timescale actor-critic decomposition.
- OpenAI Baselines / Stable-Baselines3 ([link](https://stable-baselines3.readthedocs.io/)) — production A2C/PPO implementations worth reading.


%% ── my notes ── %%
