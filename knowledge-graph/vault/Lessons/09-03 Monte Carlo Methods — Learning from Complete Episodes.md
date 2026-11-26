---
id: "lesson:09/03"
type: lesson
ref: 09/03
phase: 9
num: 3
title: "Monte Carlo Methods — Learning from Complete Episodes"
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
  - 09/03
  - 09-03
tags:
  - phase/09
  - type/build
  - community/50
  - stdlib-only
source: ai-engineering-from-scratch/phases/09-reinforcement-learning/03-monte-carlo-methods/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/09-reinforcement-learning/03-monte-carlo-methods"
---

# 09/03 Monte Carlo Methods — Learning from Complete Episodes

> Dynamic programming needs a model. Monte Carlo needs nothing but episodes. Run the policy, watch the returns, average them. The simplest idea in RL — and the one that unlocks everything downstream.

**Phase:** [[Phases/09 Reinforcement Learning|Phase 9: Reinforcement Learning]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/09-reinforcement-learning/03-monte-carlo-methods/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/09-reinforcement-learning/03-monte-carlo-methods) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/09-reinforcement-learning/03-monte-carlo-methods) · code: main.py  
**Community:** [[Communities/50 On-policy · Policy|50 On-policy · Policy]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 9 · 01 (MDPs), Phase 9 · 02 (Dynamic Programming)`

- [[Lessons/09-01 MDPs, States, Actions & Rewards|09/01 MDPs, States, Actions & Rewards]] — MDPs
- [[Lessons/09-02 Dynamic Programming — Policy Iteration & Value Iteration|09/02 Dynamic Programming — Policy Iteration & Value Iteration]] — Dynamic Programming

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]]
- depth 3: [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]], [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]], [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]], [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]]

## Builds on this

- [[Lessons/09-04 Temporal Difference — Q-Learning & SARSA|09/04 Temporal Difference — Q-Learning & SARSA]]
- [[Lessons/09-06 Policy Gradient — REINFORCE from Scratch|09/06 Policy Gradient — REINFORCE from Scratch]]

## Concepts taught

- [[Concepts/Monte Carlo|Monte Carlo]] `lesson term` — Estimate expectations by averaging over iid samples from the distribution.
- Return G_t `lesson term` — Sum of discounted rewards from step t to episode end: Σ{k≥0} γ^k r{t+k+1}.
- First-visit MC `lesson term` — Only the first visit in an episode contributes to the value estimate.
- Every-visit MC `lesson term` — Every visit contributes; slightly biased but more sample-efficient.
- ε-greedy `lesson term` — Pick greedy action with prob 1-ε; random action with prob ε.
- [[Concepts/Importance sampling|Importance sampling]] `lesson term` — Reweight returns by π(a|s)/μ(a|s) products to estimate V^π from μ data.
- [[Concepts/On-policy|On-policy]] `lesson term` — Target policy = behavior policy. Vanilla MC, PPO, SARSA.
- Off-policy `lesson term` — Target policy ≠ behavior policy. Importance-sampled MC, Q-learning, DQN.

## Ships

- [[Artifacts/09-03 mc-evaluator|mc-evaluator]] `skill` — Evaluate a policy via Monte Carlo rollouts and produce a convergence report with DP-comparison if available.

## Further reading

- Mahmood et al. (2014). Weighted Importance Sampling for Off-Policy Learning ([link](https://arxiv.org/abs/1404.6362)) — modern low-variance IS estimators.
- [[Resources/Tesauro (1995). TD-Gammon, A Self-Teaching Backgammon Program|Tesauro (1995). TD-Gammon, A Self-Teaching Backgammon Program]] ([link](https://dl.acm.org/doi/10.1145/203330.203343)) — the first large-scale empirical demonstration of MC/TD self-play converging to superhuman play; conceptual precursor to every lesson in the second half of this phase. ·  also cited by 1 other lesson
- [[Resources/Sutton & Barto (2018). Reinforcement Learning- An Introduction, 2nd ed|Sutton & Barto (2018). Reinforcement Learning: An Introduction, 2nd ed.]] ([link](http://incompleteideas.net/book/RLbook2020.pdf)) — the canonical treatment. ·  also cited by 10 other lessons
- Precup, Sutton, Singh (2000). Eligibility Traces for Off-Policy Policy Evaluation ([link](http://incompleteideas.net/papers/PSS-00.pdf)) — off-policy MC and variance control.
- Singh & Sutton (1996). Reinforcement Learning with Replacing Eligibility Traces ([link](https://link.springer.com/article/10.1007/BF00114726)) — first-visit vs every-visit analysis.


%% ── my notes ── %%
