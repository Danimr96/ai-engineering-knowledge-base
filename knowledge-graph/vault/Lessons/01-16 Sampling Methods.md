---
id: "lesson:01/16"
type: lesson
ref: 01/16
phase: 1
num: 16
title: Sampling Methods
lesson_type: build
time_min: 120
on_route: false
quiz_count: 5
code_files: 1
concepts: 18
prereqs: 2
community: 49
libraries:
  - matplotlib
aliases:
  - 01/16
  - 01-16
tags:
  - phase/01
  - type/build
  - community/49
source: ai-engineering-from-scratch/phases/01-math-foundations/16-sampling-methods/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/16-sampling-methods"
---

# 01/16 Sampling Methods

> Sampling is how AI explores the space of possibilities.

**Phase:** [[Phases/01 Math Foundations|Phase 1: Math Foundations]] · **Type:** Build · **Time:** 120 min · **Status:** —  
**Open:** [[Upstream/01-math-foundations/16-sampling-methods/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/16-sampling-methods) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/01-math-foundations/16-sampling-methods) · code: sampling.py · quiz: 5 questions  
**Community:** [[Communities/49 MCMC · Metropolis-Hastings · Importance sampling|49 MCMC · Metropolis-Hastings · Importance sampling]] · **Libraries:** [[Libraries/matplotlib (python)|matplotlib]]  

## Prerequisites

Stated upstream: `Phase 1, Lessons 06-07 (Probability, Bayes' Theorem)`

- **01/06-07** — Probability, Bayes' Theorem:
    - [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]]
    - [[Lessons/01-07 Bayes' Theorem|01/07 Bayes' Theorem]]

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]], [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]], [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]], [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]]

## Concepts taught

- [[Concepts/Sampling|Sampling]] `lesson term` — Generating values according to a probability distribution. The mechanism behind all generative AI
- Uniform distribution `lesson term` — Every value in [a, b] has equal probability density 1/(b-a). The starting point for all sampling methods
- Inverse CDF `lesson term` — F_inverse(U) converts a uniform sample into a sample from any distribution with known CDF. Exact and efficient
- Rejection sampling `lesson term` — Generate from a simple proposal, accept with probability proportional to target/proposal ratio. Exact but wastes samples
- [[Concepts/Importance sampling|Importance sampling]] `lesson term` — Estimate expectations under p(x) using samples from q(x) by weighting each sample by p(x)/q(x). Core to PPO in RL
- [[Concepts/Monte Carlo|Monte Carlo]] `lesson term` — Approximate integrals as sample averages. Error O(1/sqrt(N)) regardless of dimension
- [[Concepts/MCMC|MCMC]] `lesson term` — Construct a Markov chain whose stationary distribution is the target. Metropolis-Hastings is the foundational algorithm
- [[Concepts/Metropolis-Hastings|Metropolis-Hastings]] `lesson term` — Propose moves, accept based on density ratio. Detailed balance ensures convergence to target distribution
- Gibbs sampling `lesson term` — Update each variable from its conditional distribution holding others fixed. 100% acceptance rate
- [[Concepts/Temperature|Temperature]] `glossary` — Divides logits by T before softmax. T<1 sharpens (more confident), T>1 flattens (more diverse)
- [[Concepts/Top-k Sampling|Top-k Sampling]] `glossary` — Zero out all but the k highest-probability tokens, renormalize, sample. Fixed candidate set size
- [[Concepts/Nucleus Sampling (Top-p)|Nucleus Sampling (Top-p)]] `glossary` — Keep the smallest set of tokens whose cumulative probability exceeds p. Adaptive candidate set size
- Reparameterization trick `lesson term` — Write z = mu + sigma epsilon where epsilon ~ N(0,1). Makes sampling differentiable. Essential for VAE training
- Gumbel-Softmax `lesson term` — Differentiable approximation to categorical sampling using Gumbel noise + softmax with temperature
- Stratified sampling `lesson term` — Divide sample space into strata, sample from each. Always lower variance than naive Monte Carlo
- Burn-in `lesson term` — Initial MCMC samples discarded before the chain reaches its stationary distribution
- Detailed balance `lesson term` — p(x) T(x->y) = p(y) T(y->x). Sufficient condition for p to be the stationary distribution of a Markov chain
- Diffusion sampling `lesson term` — Generate data by starting from noise and applying learned denoising steps. Each step is a conditional sampling operation

## Ships

- [[Artifacts/01-16 skill-sampling-strategy|skill-sampling-strategy]] `skill` — Choose the right sampling method for generation, estimation, or inference

## Further reading

- [[Resources/Auto-Encoding Variational Bayes|Auto-Encoding Variational Bayes]] ([link](https://arxiv.org/abs/1312.6114)) — VAE paper introducing the reparameterization trick ·  also cited by 2 other lessons
- Jang, Gu, Poole (2017): Categorical Reparameterization with Gumbel-Softmax ([link](https://arxiv.org/abs/1611.01144)) — original Gumbel-Softmax paper
- The Curious Case of Neural Text Degeneration ([link](https://arxiv.org/abs/1904.09751)) — nucleus (top-p) sampling paper
- [[Resources/Ho, Jain, Abbeel (2020)- Denoising Diffusion Probabilistic Models|Ho, Jain, Abbeel (2020): Denoising Diffusion Probabilistic Models]] ([link](https://arxiv.org/abs/2006.11239)) — DDPM connects sampling to image generation ·  also cited by 3 other lessons
- Holbrook (2023): The Metropolis-Hastings Algorithm ([link](https://arxiv.org/abs/2304.07010)) — detailed tutorial on MCMC foundations


%% ── my notes ── %%
