---
id: "lesson:09/01"
type: lesson
ref: 09/01
phase: 9
num: 1
title: "MDPs, States, Actions & Rewards"
lesson_type: learn
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 2
community: 50
aliases:
  - 09/01
  - 09-01
tags:
  - phase/09
  - type/learn
  - community/50
  - stdlib-only
source: ai-engineering-from-scratch/phases/09-reinforcement-learning/01-mdps-states-actions-rewards/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/09-reinforcement-learning/01-mdps-states-actions-rewards"
---

# 09/01 MDPs, States, Actions & Rewards

> A Markov Decision Process is five things: states, actions, transitions, rewards, a discount. Everything in RL — Q-learning, PPO, DPO, GRPO — optimizes over this shape. Learn it once, read the rest of reinforcement learning for free.

**Phase:** [[Phases/09 Reinforcement Learning|Phase 9: Reinforcement Learning]] · **Type:** Learn · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/09-reinforcement-learning/01-mdps-states-actions-rewards/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/09-reinforcement-learning/01-mdps-states-actions-rewards) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/09-reinforcement-learning/01-mdps-states-actions-rewards) · code: main.py  
**Community:** [[Communities/50 On-policy · Policy|50 On-policy · Policy]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 1 · 06 (Probability & Distributions), Phase 2 · 01 (ML Taxonomy)`

- [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]] — Probability & Distributions
- [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]] — ML Taxonomy

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]], [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]], [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]], [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]]

## Builds on this

- [[Lessons/09-02 Dynamic Programming — Policy Iteration & Value Iteration|09/02 Dynamic Programming — Policy Iteration & Value Iteration]]
- [[Lessons/09-03 Monte Carlo Methods — Learning from Complete Episodes|09/03 Monte Carlo Methods — Learning from Complete Episodes]]
- [[Lessons/09-04 Temporal Difference — Q-Learning & SARSA|09/04 Temporal Difference — Q-Learning & SARSA]]

## Concepts taught

- MDP `lesson term` — Tuple (S, A, P, R, γ) satisfying the Markov property.
- State `lesson term` — Sufficient statistic for future dynamics under the chosen policy class.
- [[Concepts/Policy|Policy]] `lesson term` — Conditional distribution π(a | s) or deterministic map s → a.
- Return `lesson term` — Discounted sum Σ γ^t r_t from the current step.
- [[Concepts/Value|Value]] `lesson term` — Expected return under π starting from s.
- Q-value `lesson term` — Expected return under π starting from s with first action a.
- Bellman equation `lesson term` — Fixed-point decomposition of value / Q into one-step reward plus discounted successor value.
- Discount γ `lesson term` — Geometric weight on far-future reward; effective horizon ~1/(1-γ).

## Ships

- [[Artifacts/09-01 mdp-modeler|mdp-modeler]] `skill` — Given a task description, produce a Markov Decision Process spec and flag formulation risks before training.

## Further reading

- Littman (1996). Algorithms for Sequential Decision Making (PhD thesis) ([link](https://www.cs.rutgers.edu/~mlittman/papers/thesis-main.pdf)) — the cleanest derivation of MDPs as a dynamic-programming specialization.
- [[Resources/Sutton & Barto (2018). Reinforcement Learning- An Introduction, 2nd ed|Sutton & Barto (2018). Reinforcement Learning: An Introduction, 2nd ed.]] ([link](http://incompleteideas.net/book/RLbook2020.pdf)) — the textbook. Ch. 3 covers MDPs and Bellman equations; Ch. 1 motivates the reward hypothesis that underlies every subsequent lesson. ·  also cited by 10 other lessons
- [[Resources/Puterman (2005). Markov Decision Processes|Puterman (2005). Markov Decision Processes]] ([link](https://onlinelibrary.wiley.com/doi/book/10.1002/9780470316887)) — the operations-research reference on MDPs and exact solution methods. ·  also cited by 1 other lesson
- Bellman (1957). Dynamic Programming ([link](https://press.princeton.edu/books/paperback/9780691146683/dynamic-programming)) — the origin of the Bellman equation.
- OpenAI Spinning Up — Part 1: Key Concepts ([link](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html)) — concise MDP primer from a deep-RL angle.


%% ── my notes ── %%
