---
id: "lesson:09/10"
type: lesson
ref: 09/10
phase: 9
num: 10
title: Multi-Agent RL
lesson_type: build
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 3
aliases:
  - 09/10
  - 09-10
tags:
  - phase/09
  - type/build
  - stdlib-only
source: ai-engineering-from-scratch/phases/09-reinforcement-learning/10-multi-agent-rl/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/09-reinforcement-learning/10-multi-agent-rl"
---

# 09/10 Multi-Agent RL

> Single-agent RL assumes the environment is stationary. Put two learning agents in the same world and that assumption breaks: each agent is part of the other's environment, and both are changing. Multi-agent RL is the set of tricks to make learning converge when the Markov assumption no longer holds.

**Phase:** [[Phases/09 Reinforcement Learning|Phase 9: Reinforcement Learning]] · **Type:** Build · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/09-reinforcement-learning/10-multi-agent-rl/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/09-reinforcement-learning/10-multi-agent-rl) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/09-reinforcement-learning/10-multi-agent-rl) · code: main.py  
**Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 9 · 04 (Q-learning), Phase 9 · 06 (REINFORCE), Phase 9 · 07 (Actor-Critic)`

- [[Lessons/09-04 Temporal Difference — Q-Learning & SARSA|09/04 Temporal Difference — Q-Learning & SARSA]] — Q-learning
- [[Lessons/09-06 Policy Gradient — REINFORCE from Scratch|09/06 Policy Gradient — REINFORCE from Scratch]] — REINFORCE
- [[Lessons/09-07 Actor-Critic — A2C and A3C|09/07 Actor-Critic — A2C and A3C]] — Actor-Critic

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/09-01 MDPs, States, Actions & Rewards|09/01 MDPs, States, Actions & Rewards]], [[Lessons/09-02 Dynamic Programming — Policy Iteration & Value Iteration|09/02 Dynamic Programming — Policy Iteration & Value Iteration]], [[Lessons/09-03 Monte Carlo Methods — Learning from Complete Episodes|09/03 Monte Carlo Methods — Learning from Complete Episodes]]
- depth 3: [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]], [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]]

## Builds on this

- [[Lessons/09-12 RL for Games — AlphaZero, MuZero, and the LLM-Reasoning Era|09/12 RL for Games — AlphaZero, MuZero, and the LLM-Reasoning Era]]

## Concepts taught

- Markov game `lesson term` — (S, A_1, …, A_n, P, R_1, …, R_n); each agent has its own reward.
- [[Concepts/CTDE|CTDE]] `lesson term` — Joint critic at training time; each agent's policy uses only local obs.
- IPPO `lesson term` — Each agent runs PPO separately. Simple baseline; often underrated.
- [[Concepts/MAPPO|MAPPO]] `lesson term` — PPO with a centralized value function conditioned on global state.
- [[Concepts/QMIX|QMIX]] `lesson term` — Q_tot = f_monotone(Q_1, …, Q_n) allows decentralized argmax.
- COMA `lesson term` — Advantage = my Q minus expected Q marginalizing over my action.
- [[Concepts/Self-play|Self-play]] `lesson term` — Single agent, two roles; standard for zero-sum games.
- [[Concepts/League play|League play]] `lesson term` — Cache past policies, sample opponents from the pool; handles strategy cycles.

## Ships

- [[Artifacts/09-10 marl-architect|marl-architect]] `skill` — Pick the right multi-agent RL regime (IPPO, CTDE, self-play, league) for a given task.

## Further reading

- Foerster et al. (2017). Counterfactual Multi-Agent Policy Gradients (COMA) ([link](https://arxiv.org/abs/1705.08926)) — counterfactual baselines for credit assignment.
- [[Resources/Lowe et al. (2017). Multi-Agent Actor-Critic for Mixed Cooperative-Competitive Environments (MADDPG)|Lowe et al. (2017). Multi-Agent Actor-Critic for Mixed Cooperative-Competitive Environments (MADDPG)]] ([link](https://arxiv.org/abs/1706.02275)) — CTDE with a centralized critic. ·  also cited by 1 other lesson
- [[Resources/Rashid et al. (2018). QMIX- Monotonic Value Function Factorisation|Rashid et al. (2018). QMIX: Monotonic Value Function Factorisation]] ([link](https://arxiv.org/abs/1803.11485)) — value decomposition with monotonicity. ·  also cited by 1 other lesson
- Zhang, Yang & Başar (2021). Multi-Agent Reinforcement Learning: A Selective Overview ([link](https://arxiv.org/abs/1911.10635)) — survey covering cooperative, competitive, and mixed MARL with convergence results.
- [[Resources/Yu et al. (2022). The Surprising Effectiveness of PPO in Cooperative Multi-Agent Games (MAPPO)|Yu et al. (2022). The Surprising Effectiveness of PPO in Cooperative Multi-Agent Games (MAPPO)]] ([link](https://arxiv.org/abs/2103.01955)) — PPO is surprisingly strong for MARL. ·  also cited by 1 other lesson
- [[Resources/Sutton & Barto (2018). Reinforcement Learning- An Introduction, 2nd ed|Sutton & Barto (2018). Reinforcement Learning: An Introduction, 2nd ed.]] ([link](http://incompleteideas.net/book/RLbook2020.pdf)) — includes the textbook's short treatment of multi-agent settings and the non-stationarity problem that CTDE is designed to solve. ·  also cited by 10 other lessons
- [[Resources/Silver et al. (2017). Mastering the game of Go without human knowledge (AlphaGo Zero)|Silver et al. (2017). Mastering the game of Go without human knowledge (AlphaGo Zero)]] ([link](https://www.nature.com/articles/nature24270)) — pure self-play in zero-sum games. ·  also cited by 1 other lesson
- [[Resources/Vinyals et al. (2019). Grandmaster level in StarCraft II using multi-agent reinforcement learning (AlphaStar)|Vinyals et al. (2019). Grandmaster level in StarCraft II using multi-agent reinforcement learning (AlphaStar)]] ([link](https://www.nature.com/articles/s41586-019-1724-z)) — league play at scale. ·  also cited by 1 other lesson


%% ── my notes ── %%
