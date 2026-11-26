---
id: "lesson:09/06"
type: lesson
ref: 09/06
phase: 9
num: 6
title: "Policy Gradient — REINFORCE from Scratch"
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 3
community: 33
aliases:
  - 09/06
  - 09-06
tags:
  - phase/09
  - type/build
  - community/33
  - stdlib-only
source: ai-engineering-from-scratch/phases/09-reinforcement-learning/06-policy-gradients-reinforce/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/09-reinforcement-learning/06-policy-gradients-reinforce"
---

# 09/06 Policy Gradient — REINFORCE from Scratch

> Stop estimating value. Parameterize the policy directly, compute the gradient of expected return, step uphill. Williams (1992) wrote it in one theorem. It is why PPO, GRPO, and every LLM RL loop exist.

**Phase:** [[Phases/09 Reinforcement Learning|Phase 9: Reinforcement Learning]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/09-reinforcement-learning/06-policy-gradients-reinforce/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/09-reinforcement-learning/06-policy-gradients-reinforce) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/09-reinforcement-learning/06-policy-gradients-reinforce) · code: main.py  
**Community:** [[Communities/33 Advantage · Baseline · Actor|33 Advantage · Baseline · Actor]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 3 · 03 (Backpropagation), Phase 9 · 03 (Monte Carlo), Phase 9 · 04 (TD Learning)`

- [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]] — Backpropagation
- [[Lessons/09-03 Monte Carlo Methods — Learning from Complete Episodes|09/03 Monte Carlo Methods — Learning from Complete Episodes]] — Monte Carlo
- [[Lessons/09-04 Temporal Difference — Q-Learning & SARSA|09/04 Temporal Difference — Q-Learning & SARSA]] — TD Learning

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]], [[Lessons/09-01 MDPs, States, Actions & Rewards|09/01 MDPs, States, Actions & Rewards]], [[Lessons/09-02 Dynamic Programming — Policy Iteration & Value Iteration|09/02 Dynamic Programming — Policy Iteration & Value Iteration]]
- depth 3: [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]], [[Lessons/03-01 The Perceptron|03/01 The Perceptron]]

## Builds on this

- [[Lessons/09-07 Actor-Critic — A2C and A3C|09/07 Actor-Critic — A2C and A3C]]
- [[Lessons/09-08 Proximal Policy Optimization (PPO)|09/08 Proximal Policy Optimization (PPO)]]
- [[Lessons/09-10 Multi-Agent RL|09/10 Multi-Agent RL]]

## Concepts taught

- Policy gradient `lesson term` — ∇J(θ) = E[G · ∇ log πθ(a|s)]; derived from the log-derivative trick.
- REINFORCE `lesson term` — Williams (1992); Monte Carlo returns multiplied by log-policy gradient.
- Log-derivative trick `lesson term` — ∇P(τ;θ) = P(τ;θ) · ∇ log P(τ;θ); makes gradients of expectations tractable.
- [[Concepts/Baseline|Baseline]] `lesson term` — Any b(s) subtracted from G; unbiased because E[b · ∇ log π] = 0.
- Reward-to-go `lesson term` — G_t^{from t} instead of the full G_0; correct and lower-variance.
- Entropy bonus `lesson term` — +β · H(π(·|s)) term keeps the policy from collapsing.
- [[Concepts/On-policy|On-policy]] `lesson term` — Gradient expectation is w.r.t. the current policy — cannot reuse old data directly.
- [[Concepts/Advantage|Advantage]] `lesson term` — A(s, a) = G(s, a) - V(s); the signed quantity REINFORCE-with-baseline multiplies.

## Ships

- [[Artifacts/09-06 policy-gradient-trainer|policy-gradient-trainer]] `skill` — Produce a REINFORCE / actor-critic / PPO training config for a given task and diagnose variance issues.

## Further reading

- Peters & Schaal (2008). Reinforcement Learning of Motor Skills with Policy Gradients ([link](https://homes.cs.washington.edu/~todorov/courses/amath579/reading/PolicyGradient.pdf)) — variance-reduction and the natural-gradient view that connects REINFORCE to the trust-region family (TRPO, PPO).
- [[Resources/Sutton & Barto (2018). Reinforcement Learning- An Introduction, 2nd ed|Sutton & Barto (2018). Reinforcement Learning: An Introduction, 2nd ed.]] ([link](http://incompleteideas.net/book/RLbook2020.pdf)) — textbook presentation. ·  also cited by 10 other lessons
- Williams (1992). Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning ([link](https://link.springer.com/article/10.1007/BF00992696)) — the original REINFORCE paper.
- Sutton et al. (2000). Policy Gradient Methods for Reinforcement Learning with Function Approximation ([link](https://papers.nips.cc/paper_files/paper/1999/hash/464d828b85b0bed98e80ade0a5c43b0f-Abstract.html)) — the modern policy-gradient theorem with function approximation.
- OpenAI Spinning Up — VPG / REINFORCE ([link](https://spinningup.openai.com/en/latest/algorithms/vpg.html)) — clear pedagogical exposition with PyTorch code.


%% ── my notes ── %%
