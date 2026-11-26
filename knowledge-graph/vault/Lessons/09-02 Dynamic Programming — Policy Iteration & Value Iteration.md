---
id: "lesson:09/02"
type: lesson
ref: 09/02
phase: 9
num: 2
title: "Dynamic Programming — Policy Iteration & Value Iteration"
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 0
code_files: 1
concepts: 7
prereqs: 1
community: 50
aliases:
  - 09/02
  - 09-02
tags:
  - phase/09
  - type/build
  - community/50
  - stdlib-only
source: ai-engineering-from-scratch/phases/09-reinforcement-learning/02-dynamic-programming/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/09-reinforcement-learning/02-dynamic-programming"
---

# 09/02 Dynamic Programming — Policy Iteration & Value Iteration

> Dynamic programming is RL with cheating. You already know the transition and reward functions; you just iterate the Bellman equation until `V` or `π` stops moving. It is the benchmark every sampling-based method tries to approach.

**Phase:** [[Phases/09 Reinforcement Learning|Phase 9: Reinforcement Learning]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/09-reinforcement-learning/02-dynamic-programming/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/09-reinforcement-learning/02-dynamic-programming) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/09-reinforcement-learning/02-dynamic-programming) · code: main.py  
**Community:** [[Communities/50 On-policy · Policy|50 On-policy · Policy]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 9 · 01 (MDPs)`

- [[Lessons/09-01 MDPs, States, Actions & Rewards|09/01 MDPs, States, Actions & Rewards]] — MDPs

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]]
- depth 3: [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]], [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]], [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]], [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]]

## Builds on this

- [[Lessons/09-03 Monte Carlo Methods — Learning from Complete Episodes|09/03 Monte Carlo Methods — Learning from Complete Episodes]]
- [[Lessons/09-04 Temporal Difference — Q-Learning & SARSA|09/04 Temporal Difference — Q-Learning & SARSA]]

## Concepts taught

- Policy iteration `lesson term` — Alternating evaluation (V^π) and improvement (greedy π w.r.t. V^π) until the policy stops changing.
- Value iteration `lesson term` — Bellman optimality backup applied in one sweep; converges to V geometrically.
- Bellman operator `lesson term` — (T V)(s) = max_a Σ P (r + γ V(s')); a γ-contraction in sup-norm.
- [[Concepts/Contraction|Contraction]] `lesson term` — Any operator T with ||T x - T y|| ≤ γ ||x - y|| has a unique fixed point.
- GPI `lesson term` — Generalized Policy Iteration: any method driving V and π to mutual consistency.
- Synchronous update `lesson term` — Use old V throughout a sweep; cleanly analyzable but slower.
- In-place update `lesson term` — Use V as it's being updated; converges faster in practice.

## Ships

- [[Artifacts/09-02 dp-solver|dp-solver]] `skill` — Solve a small tabular MDP exactly via policy iteration or value iteration. Report convergence behavior.

## Further reading

- Bertsekas & Tsitsiklis (1996). Neuro-Dynamic Programming ([link](http://www.athenasc.com/ndpbook.html)) — the bridge from DP to approximate-DP / deep RL used by every subsequent lesson.
- Bertsekas (2019). Reinforcement Learning and Optimal Control ([link](http://www.athenasc.com/rlbook.html)) — rigorous treatment of contraction-mapping arguments.
- [[Resources/Sutton & Barto (2018). Reinforcement Learning- An Introduction, 2nd ed|Sutton & Barto (2018). Reinforcement Learning: An Introduction, 2nd ed.]] ([link](http://incompleteideas.net/book/RLbook2020.pdf)) — the canonical presentation of policy iteration and value iteration. ·  also cited by 10 other lessons
- Howard (1960). Dynamic Programming and Markov Processes ([link](https://mitpress.mit.edu/9780262582300/dynamic-programming-and-markov-processes/)) — the original policy iteration paper.
- [[Resources/Puterman (2005). Markov Decision Processes|Puterman (2005). Markov Decision Processes]] ([link](https://onlinelibrary.wiley.com/doi/book/10.1002/9780470316887)) — modified policy iteration and its convergence analysis. ·  also cited by 1 other lesson


%% ── my notes ── %%
