---
id: "lesson:01/22"
type: lesson
ref: 01/22
phase: 1
num: 22
title: Stochastic Processes
lesson_type: learn
time_min: 75
on_route: false
quiz_count: 5
code_files: 1
concepts: 10
prereqs: 2
community: 49
libraries:
  - numpy
aliases:
  - 01/22
  - 01-22
tags:
  - phase/01
  - type/learn
  - community/49
source: ai-engineering-from-scratch/phases/01-math-foundations/22-stochastic-processes/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/22-stochastic-processes"
---

# 01/22 Stochastic Processes

> Randomness with structure. The math behind random walks, Markov chains, and diffusion models.

**Phase:** [[Phases/01 Math Foundations|Phase 1: Math Foundations]] · **Type:** Learn · **Time:** 75 min · **Status:** —  
**Open:** [[Upstream/01-math-foundations/22-stochastic-processes/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/22-stochastic-processes) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/01-math-foundations/22-stochastic-processes) · code: stochastic.py · quiz: 5 questions  
**Community:** [[Communities/49 MCMC · Metropolis-Hastings · Importance sampling|49 MCMC · Metropolis-Hastings · Importance sampling]] · **Libraries:** [[Libraries/numpy (python)|numpy]]  

## Prerequisites

Stated upstream: `Phase 1, Lessons 06-07 (probability, Bayes)`

- **01/06-07** — probability, Bayes:
    - [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]]
    - [[Lessons/01-07 Bayes' Theorem|01/07 Bayes' Theorem]]

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]], [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]], [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]], [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]]

## Concepts taught

- Random walk `lesson term` — A process where position changes by random increments at each step
- Markov property `lesson term` — The future depends only on the present state, not on the history
- Transition matrix `lesson term` — P[i][j] = probability of moving from state i to state j
- Stationary distribution `lesson term` — The distribution pi where piP = pi -- the chain's equilibrium
- Brownian motion `lesson term` — The continuous-time limit of a random walk, B(t) ~ N(0, t)
- Langevin dynamics `lesson term` — Update rule that combines deterministic gradient and random perturbation
- [[Concepts/MCMC|MCMC]] `lesson term` — Constructing a Markov chain whose stationary distribution is the one you want
- [[Concepts/Metropolis-Hastings|Metropolis-Hastings]] `lesson term` — MCMC algorithm that uses acceptance ratios to ensure convergence
- [[Concepts/Temperature|Temperature]] `glossary` — Parameter controlling the tradeoff between exploration and exploitation
- Diffusion process `lesson term` — Forward: gradually add noise. Reverse: gradually remove it. Generates data.

## Ships

- [[Artifacts/01-22 prompt-stochastic-process-advisor|prompt-stochastic-process-advisor]] `prompt` — Identify which stochastic process framework applies to a given problem and recommend implementation


%% ── my notes ── %%
