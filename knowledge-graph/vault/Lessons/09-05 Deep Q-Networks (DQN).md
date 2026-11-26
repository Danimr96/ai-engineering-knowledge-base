---
id: "lesson:09/05"
type: lesson
ref: 09/05
phase: 9
num: 5
title: Deep Q-Networks (DQN)
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 2
community: 50
aliases:
  - 09/05
  - 09-05
tags:
  - phase/09
  - type/build
  - community/50
  - stdlib-only
source: ai-engineering-from-scratch/phases/09-reinforcement-learning/05-dqn/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/09-reinforcement-learning/05-dqn"
---

# 09/05 Deep Q-Networks (DQN)

> 2013: Mnih trained one Q-learning network on raw pixels, beat every classical RL agent on seven Atari games. 2015: extended to 49 games, published in Nature, sparked the deep-RL era. DQN is Q-learning plus three tricks that make function approximation stable.

**Phase:** [[Phases/09 Reinforcement Learning|Phase 9: Reinforcement Learning]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/09-reinforcement-learning/05-dqn/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/09-reinforcement-learning/05-dqn) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/09-reinforcement-learning/05-dqn) · code: main.py  
**Community:** [[Communities/50 On-policy · Policy|50 On-policy · Policy]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 3 · 03 (Backpropagation), Phase 9 · 04 (Q-learning, SARSA)`

- [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]] — Backpropagation
- [[Lessons/09-04 Temporal Difference — Q-Learning & SARSA|09/04 Temporal Difference — Q-Learning & SARSA]] — Q-learning, SARSA

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]], [[Lessons/09-01 MDPs, States, Actions & Rewards|09/01 MDPs, States, Actions & Rewards]], [[Lessons/09-02 Dynamic Programming — Policy Iteration & Value Iteration|09/02 Dynamic Programming — Policy Iteration & Value Iteration]], [[Lessons/09-03 Monte Carlo Methods — Learning from Complete Episodes|09/03 Monte Carlo Methods — Learning from Complete Episodes]]
- depth 3: [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]], [[Lessons/03-01 The Perceptron|03/01 The Perceptron]]

## Builds on this

- [[Lessons/09-12 RL for Games — AlphaZero, MuZero, and the LLM-Reasoning Era|09/12 RL for Games — AlphaZero, MuZero, and the LLM-Reasoning Era]]

## Concepts taught

- DQN `lesson term` — Q-learning with a neural Q-function, replay buffer, and target network.
- Experience replay `lesson term` — Ring buffer sampled uniformly each gradient step; decorrelates data.
- Target network `lesson term` — Periodic copy of Q used in the Bellman target; stabilizes training.
- Deadly triad `lesson term` — Function approximation + bootstrapping + off-policy = no convergence guarantee.
- Double DQN `lesson term` — Online net selects action, target net evaluates it.
- Dueling DQN `lesson term` — Decompose Q = V + A - mean(A); same output, better gradient flow.
- Rainbow `lesson term` — DDQN + PER + dueling + n-step + noisy + distributional in one.
- PER `lesson term` — Sample transitions proportional to TD-error magnitude.

## Ships

- [[Artifacts/09-05 dqn-trainer|dqn-trainer]] `skill` — Produce a DQN training config (buffer, target sync, ε schedule, reward clipping) for a discrete-action RL task.

## Further reading

- Mnih et al. (2013). Playing Atari with Deep Reinforcement Learning ([link](https://arxiv.org/abs/1312.5602)) — the 2013 NeurIPS workshop paper that kicked off deep RL.
- Hasselt, Guez, Silver (2016). Deep Reinforcement Learning with Double Q-learning ([link](https://arxiv.org/abs/1509.06461)) — DDQN.
- Wang et al. (2016). Dueling Network Architectures ([link](https://arxiv.org/abs/1511.06581)) — dueling DQN.
- Hessel et al. (2018). Rainbow: Combining Improvements in Deep RL ([link](https://arxiv.org/abs/1710.02298)) — the stacked-tricks paper.
- CleanRL DQN implementation ([link](https://docs.cleanrl.dev/rl-algorithms/dqn/)) — reference single-file DQN used in ablation studies; good to read alongside this lesson's from-scratch version.
- [[Resources/Sutton & Barto (2018). Reinforcement Learning- An Introduction, 2nd ed|Sutton & Barto (2018). Reinforcement Learning: An Introduction, 2nd ed.]] ([link](http://incompleteideas.net/book/RLbook2020.pdf)) — the textbook treatment of the "deadly triad" (function approximation + bootstrapping + off-policy) that DQN's target network and replay buffer are designed to tame. ·  also cited by 10 other lessons
- Mnih et al. (2015). Human-level control through deep reinforcement learning ([link](https://www.nature.com/articles/nature14236)) — the Nature paper, 49-game DQN.
- OpenAI Spinning Up — DQN ([link](https://spinningup.openai.com/en/latest/algorithms/dqn.html)) — clear modern exposition.


%% ── my notes ── %%
