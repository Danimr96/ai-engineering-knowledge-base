---
id: "lesson:09/04"
type: lesson
ref: 09/04
phase: 9
num: 4
title: "Temporal Difference — Q-Learning & SARSA"
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 3
community: 50
aliases:
  - 09/04
  - 09-04
tags:
  - phase/09
  - type/build
  - community/50
  - stdlib-only
source: ai-engineering-from-scratch/phases/09-reinforcement-learning/04-q-learning-sarsa/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/09-reinforcement-learning/04-q-learning-sarsa"
---

# 09/04 Temporal Difference — Q-Learning & SARSA

> Monte Carlo waits until the episode ends. TD updates after every step by bootstrapping the next value estimate. Q-learning is off-policy and optimistic; SARSA is on-policy and cautious. Both are one line of code. Both underpin every deep-RL method in this phase.

**Phase:** [[Phases/09 Reinforcement Learning|Phase 9: Reinforcement Learning]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/09-reinforcement-learning/04-q-learning-sarsa/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/09-reinforcement-learning/04-q-learning-sarsa) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/09-reinforcement-learning/04-q-learning-sarsa) · code: main.py  
**Community:** [[Communities/50 On-policy · Policy|50 On-policy · Policy]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 9 · 01 (MDPs), Phase 9 · 02 (Dynamic Programming), Phase 9 · 03 (Monte Carlo)`

- [[Lessons/09-01 MDPs, States, Actions & Rewards|09/01 MDPs, States, Actions & Rewards]] — MDPs
- [[Lessons/09-02 Dynamic Programming — Policy Iteration & Value Iteration|09/02 Dynamic Programming — Policy Iteration & Value Iteration]] — Dynamic Programming
- [[Lessons/09-03 Monte Carlo Methods — Learning from Complete Episodes|09/03 Monte Carlo Methods — Learning from Complete Episodes]] — Monte Carlo

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]]
- depth 3: [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]], [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]], [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]], [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]]

## Builds on this

- [[Lessons/09-05 Deep Q-Networks (DQN)|09/05 Deep Q-Networks (DQN)]]
- [[Lessons/09-06 Policy Gradient — REINFORCE from Scratch|09/06 Policy Gradient — REINFORCE from Scratch]]
- [[Lessons/09-07 Actor-Critic — A2C and A3C|09/07 Actor-Critic — A2C and A3C]]
- [[Lessons/09-10 Multi-Agent RL|09/10 Multi-Agent RL]]

## Concepts taught

- TD error `lesson term` — δ = r + γ V(s') - V(s), the bootstrapped residual.
- TD(0) `lesson term` — Update after every transition using only the next state's estimate.
- Q-learning `lesson term` — TD update with max over next-state actions; learns Q regardless of behavior policy.
- SARSA `lesson term` — TD update using the actual next action; learns Q^π for current ε-greedy π.
- Expected SARSA `lesson term` — Replace sampled a' with its expectation under π.
- GLIE `lesson term` — Greedy in the Limit with Infinite Exploration; needed for Q-learning convergence.
- Bootstrapping `lesson term` — What distinguishes TD from MC. Source of bias but massive variance reduction.
- Maximization bias `lesson term` — max over noisy estimates is upward-biased; fixed by Double Q-learning.

## Ships

- [[Artifacts/09-04 td-agent|td-agent]] `skill` — Pick between Q-learning, SARSA, Expected SARSA for a tabular or small-feature RL task.

## Further reading

- Seijen, Hasselt, Whiteson, Wiering (2009). A Theoretical and Empirical Analysis of Expected SARSA ([link](https://ieeexplore.ieee.org/document/4927542)) — expected SARSA motivation.
- [[Resources/Sutton & Barto (2018). Reinforcement Learning- An Introduction, 2nd ed|Sutton & Barto (2018). Reinforcement Learning: An Introduction, 2nd ed.]] ([link](http://incompleteideas.net/book/RLbook2020.pdf)) — TD(0), SARSA, Q-learning, Expected SARSA. ·  also cited by 10 other lessons
- Watkins & Dayan (1992). Q-learning ([link](https://link.springer.com/article/10.1007/BF00992698)) — the original paper and convergence proof.
- Hasselt (2010). Double Q-learning ([link](https://papers.nips.cc/paper_files/paper/2010/hash/091d584fced301b442654dd8c23b3fc9-Abstract.html)) — fix for maximization bias.
- Rummery & Niranjan (1994). On-line Q-learning using connectionist systems ([link](https://www.researchgate.net/publication/2500611_On-Line_Q-Learning_Using_Connectionist_Systems)) — the paper that coined SARSA (then called "modified connectionist Q-learning").


%% ── my notes ── %%
