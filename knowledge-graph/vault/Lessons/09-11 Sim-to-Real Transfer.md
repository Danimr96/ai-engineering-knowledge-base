---
id: "lesson:09/11"
type: lesson
ref: 09/11
phase: 9
num: 11
title: Sim-to-Real Transfer
lesson_type: learn
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 2
community: 60
aliases:
  - 09/11
  - 09-11
tags:
  - phase/09
  - type/learn
  - community/60
  - stdlib-only
source: ai-engineering-from-scratch/phases/09-reinforcement-learning/11-sim-to-real-transfer/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/09-reinforcement-learning/11-sim-to-real-transfer"
---

# 09/11 Sim-to-Real Transfer

> A policy trained in a simulator that fails on hardware is a policy that memorized the simulator. Domain randomization, domain adaptation, and system identification are the three tools to make learned controllers cross the reality gap.

**Phase:** [[Phases/09 Reinforcement Learning|Phase 9: Reinforcement Learning]] · **Type:** Learn · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/09-reinforcement-learning/11-sim-to-real-transfer/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/09-reinforcement-learning/11-sim-to-real-transfer) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/09-reinforcement-learning/11-sim-to-real-transfer) · code: main.py  
**Community:** [[Communities/60 GRPO · KL penalty · League play|60 GRPO · KL penalty · League play]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 9 · 08 (PPO), Phase 2 · 10 (Bias/Variance)`

- [[Lessons/02-10 Bias-Variance Tradeoff|02/10 Bias-Variance Tradeoff]] — Bias/Variance
- [[Lessons/09-08 Proximal Policy Optimization (PPO)|09/08 Proximal Policy Optimization (PPO)]] — PPO

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]], [[Lessons/02-02 Linear Regression|02/02 Linear Regression]], [[Lessons/02-03 Logistic Regression|02/03 Logistic Regression]], [[Lessons/02-04 Decision Trees and Random Forests|02/04 Decision Trees and Random Forests]], [[Lessons/02-05 Support Vector Machines|02/05 Support Vector Machines]], [[Lessons/02-06 K-Nearest Neighbors and Distances|02/06 K-Nearest Neighbors and Distances]], [[Lessons/02-07 Unsupervised Learning|02/07 Unsupervised Learning]], [[Lessons/02-08 Feature Engineering & Selection|02/08 Feature Engineering & Selection]], [[Lessons/02-09 Model Evaluation|02/09 Model Evaluation]], [[Lessons/09-06 Policy Gradient — REINFORCE from Scratch|09/06 Policy Gradient — REINFORCE from Scratch]], [[Lessons/09-07 Actor-Critic — A2C and A3C|09/07 Actor-Critic — A2C and A3C]]
- depth 3: [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/01-08 Optimization|01/08 Optimization]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/01-14 Norms and Distances|01/14 Norms and Distances]], [[Lessons/01-18 Convex Optimization|01/18 Convex Optimization]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/09-03 Monte Carlo Methods — Learning from Complete Episodes|09/03 Monte Carlo Methods — Learning from Complete Episodes]], [[Lessons/09-04 Temporal Difference — Q-Learning & SARSA|09/04 Temporal Difference — Q-Learning & SARSA]]

## Concepts taught

- Reality gap `lesson term` — Distribution shift between training and deployment physics/sensing.
- Domain randomization (as *Domain randomization (DR)*) `lesson term` — Randomize sim parameters during training so policy generalizes.
- System identification (as *System identification (SI)*) `lesson term` — Estimate real physical parameters; set sim to match.
- Domain adaptation `lesson term` — Small real-world fine-tune after sim training; may adapt obs or dynamics.
- Privileged info `lesson term` — Information only the sim has; student must infer it from obs history.
- Teacher/student `lesson term` — Teacher trained with shortcuts; student learns to mimic without them.
- ADR `lesson term` — Curriculum that widens DR ranges as the policy improves.
- Real2Sim `lesson term` — Learn a residual to make the sim mimic real rollouts.

## Ships

- [[Artifacts/09-11 sim2real-planner|sim2real-planner]] `skill` — Plan a sim-to-real transfer pipeline for a given robot + task, covering DR, SI, and safety.

## Further reading

- Tobin et al. (2017). Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World ([link](https://arxiv.org/abs/1703.06907)) — the original DR paper (vision for robotics).
- Peng et al. (2018). Sim-to-Real Transfer of Robotic Control with Dynamics Randomization ([link](https://arxiv.org/abs/1710.06537)) — DR for dynamics, quadruped locomotion.
- OpenAI et al. (2019). Solving Rubik's Cube with a Robot Hand ([link](https://arxiv.org/abs/1910.07113)) — Dactyl, ADR at scale.
- Zhao, Queralta & Westerlund (2020). Sim-to-Real Transfer in Deep Reinforcement Learning for Robotics: a Survey ([link](https://arxiv.org/abs/2009.13303)) — taxonomy of sim-to-real methods with benchmark results.
- Makoviychuk et al. (2021). Isaac Gym: High Performance GPU Based Physics Simulation for Robot Learning ([link](https://arxiv.org/abs/2108.10470)) — the massively parallel sim that drives 2025–2026 deployments.
- [[Resources/Sutton & Barto (2018). Reinforcement Learning- An Introduction, 2nd ed|Sutton & Barto (2018). Reinforcement Learning: An Introduction, 2nd ed.]] ([link](http://incompleteideas.net/book/RLbook2020.pdf)) — the Dyna framing (use a model for planning + rollouts) that underpins modern sim-to-real pipelines. ·  also cited by 10 other lessons
- Miki et al. (2022). Learning robust perceptive locomotion for quadrupedal robots in the wild ([link](https://www.science.org/doi/10.1126/scirobotics.abk2822)) — teacher-student for ANYmal.


%% ── my notes ── %%
