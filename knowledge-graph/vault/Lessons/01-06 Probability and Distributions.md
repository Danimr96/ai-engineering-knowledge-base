---
id: "lesson:01/06"
type: lesson
ref: 01/06
phase: 1
num: 6
title: Probability and Distributions
lesson_type: learn
time_min: 75
on_route: false
quiz_count: 5
code_files: 2
concepts: 16
prereqs: 4
community: 8
libraries:
  - matplotlib
aliases:
  - 01/06
  - 01-06
tags:
  - phase/01
  - type/learn
  - community/08
source: ai-engineering-from-scratch/phases/01-math-foundations/06-probability-and-distributions/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/06-probability-and-distributions"
---

# 01/06 Probability and Distributions

> Probability is the language AI uses to express uncertainty.

**Phase:** [[Phases/01 Math Foundations|Phase 1: Math Foundations]] · **Type:** Learn · **Time:** 75 min · **Status:** —  
**Open:** [[Upstream/01-math-foundations/06-probability-and-distributions/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/06-probability-and-distributions) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/01-math-foundations/06-probability-and-distributions) · code: main.jl, probability.py · quiz: 5 questions  
**Community:** [[Communities/08 Backpropagation · Gradient · Activation Function|08 Backpropagation · Gradient · Activation Function]] · **Libraries:** [[Libraries/matplotlib (python)|matplotlib]]  

## Prerequisites

Stated upstream: `Phase 1, Lessons 01-04`

- **01/01-04**:
    - [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]]
    - [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]]
    - [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]]
    - [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]]

## Builds on this

- [[Lessons/01-07 Bayes' Theorem|01/07 Bayes' Theorem]]
- [[Lessons/01-09 Information Theory|01/09 Information Theory]]
- [[Lessons/01-10 Dimensionality Reduction|01/10 Dimensionality Reduction]]
- [[Lessons/01-15 Statistics for Machine Learning|01/15 Statistics for Machine Learning]]
- [[Lessons/01-16 Sampling Methods|01/16 Sampling Methods]]
- [[Lessons/01-22 Stochastic Processes|01/22 Stochastic Processes]]
- [[Lessons/02-04 Decision Trees and Random Forests|02/04 Decision Trees and Random Forests]]
- [[Lessons/04-10 Image Generation — Diffusion Models|04/10 Image Generation — Diffusion Models]]
- [[Lessons/06-01 Audio Fundamentals — Waveforms, Sampling, Fourier Transform|06/01 Audio Fundamentals — Waveforms, Sampling, Fourier Transform]]
- [[Lessons/09-01 MDPs, States, Actions & Rewards|09/01 MDPs, States, Actions & Rewards]]

## Concepts taught

- Sample space `lesson term` — The set S of every possible outcome of an experiment
- PMF `lesson term` — A function that gives the exact probability of each discrete outcome, summing to 1
- PDF `lesson term` — A density function for continuous variables. Integrate it over an interval to get probability
- Conditional probability `lesson term` — P(A|B) = P(A and B) / P(B). The foundation of Bayesian thinking and Bayes' theorem
- Independence `lesson term` — P(A and B) = P(A) P(B). Knowing one event tells you nothing about the other
- Expected value `lesson term` — The probability-weighted sum of all outcomes. The loss function is an expected value
- [[Concepts/Variance|Variance]] `lesson term` — The expected squared deviation from the mean. High variance = noisy, unstable estimates
- Normal distribution `lesson term` — f(x) = (1/sqrt(2pisigma^2)) exp(-(x-mu)^2/(2sigma^2)). Appears everywhere due to the CLT
- [[Concepts/Central Limit Theorem|Central Limit Theorem]] `lesson term` — The mean of many independent samples converges to a normal distribution regardless of the source
- Joint distribution `lesson term` — P(X, Y) describes the probability of every combination of X and Y outcomes
- Marginal distribution `lesson term` — P(X) = sum_y P(X, Y). Recovers one variable's distribution from the joint
- [[Concepts/Log probability|Log probability]] `lesson term` — log P(x). Turns products into sums, preventing numerical underflow in long sequences
- [[Concepts/Softmax|Softmax]] `glossary` — softmax(z_i) = exp(z_i) / sum(exp(z_j)). Maps real-valued logits to a valid probability distribution
- [[Concepts/Cross-Entropy|Cross-Entropy]] `glossary` — -sum(p_true log(p_predicted)). Measures how different two distributions are. Lower is better
- [[Concepts/Logits|Logits]] `glossary` — Unnormalized scores before softmax. Named after the logistic function
- [[Concepts/Sampling|Sampling]] `lesson term` — Generating values according to a probability distribution. How models generate output

## Ships

- [[Artifacts/01-06 skill-probability-reasoning|skill-probability-reasoning]] `skill` — Choose the right probability distribution for a given ML problem

## Further reading

- Stanford CS229 Probability Review ([link](https://cs229.stanford.edu/section/cs229-prob.pdf)) — concise reference covering everything here and more
- The Log-Sum-Exp Trick ([link](https://gregorygundersen.com/blog/2020/02/09/log-sum-exp/)) — why numerical stability matters and how to achieve it
- 3Blue1Brown: But what is the Central Limit Theorem? ([link](https://www.youtube.com/watch?v=zeJD6dqJ5lo)) — visual proof of why averages become normal


%% ── my notes ── %%
