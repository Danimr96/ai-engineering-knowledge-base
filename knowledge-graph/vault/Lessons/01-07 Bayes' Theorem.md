---
id: "lesson:01/07"
type: lesson
ref: 01/07
phase: 1
num: 7
title: "Bayes' Theorem"
lesson_type: build
time_min: 75
on_route: false
quiz_count: 5
code_files: 1
concepts: 10
prereqs: 1
community: 62
aliases:
  - 01/07
  - 01-07
tags:
  - phase/01
  - type/build
  - community/62
  - stdlib-only
source: ai-engineering-from-scratch/phases/01-math-foundations/07-bayes-theorem/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/07-bayes-theorem"
---

# 01/07 Bayes' Theorem

> Probability is about what you expect. Bayes' theorem is about what you learn.

**Phase:** [[Phases/01 Math Foundations|Phase 1: Math Foundations]] · **Type:** Build · **Time:** 75 min · **Status:** —  
**Open:** [[Upstream/01-math-foundations/07-bayes-theorem/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/07-bayes-theorem) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/01-math-foundations/07-bayes-theorem) · code: bayes.py · quiz: 5 questions  
**Community:** [[Communities/62 Laplace smoothing · Likelihood · Log probability|62 Laplace smoothing · Likelihood · Log probability]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 1, Lesson 06 (Probability Fundamentals)`

- [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]] — Probability Fundamentals

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]], [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]], [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]], [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]]

## Builds on this

- [[Lessons/01-15 Statistics for Machine Learning|01/15 Statistics for Machine Learning]]
- [[Lessons/01-16 Sampling Methods|01/16 Sampling Methods]]
- [[Lessons/01-22 Stochastic Processes|01/22 Stochastic Processes]]

## Concepts taught

- [[Concepts/Prior|Prior]] `lesson term` — P(hypothesis) before observing evidence. In ML: the regularization term.
- [[Concepts/Likelihood|Likelihood]] `lesson term` — P(evidence|hypothesis). How probable the observed data is under a specific hypothesis.
- [[Concepts/Posterior|Posterior]] `lesson term` — P(hypothesis|evidence). The prior multiplied by the likelihood, then normalized.
- Evidence `lesson term` — P(data) across all hypotheses. Ensures the posterior sums to 1.
- [[Concepts/Naive Bayes|Naive Bayes]] `lesson term` — A classifier that assumes features are independent given the class. Works well despite the false assumption.
- [[Concepts/Laplace smoothing|Laplace smoothing]] `lesson term` — Adding a small count to every feature to prevent zero probabilities from unseen data.
- MLE `lesson term` — Choose parameters that maximize P(data|parameters). No prior. Can overfit with small data.
- [[Concepts/MAP|MAP]] `lesson term` — Choose parameters that maximize P(data|parameters) P(parameters). Equivalent to regularized MLE.
- [[Concepts/Log probability|Log probability]] (as *Log-probability*) `lesson term` — Using log(P) instead of P to avoid floating-point underflow when multiplying many small numbers.
- False positive `lesson term` — The test says positive, but the true state is negative. Drives the base rate fallacy.

## Ships

- [[Artifacts/01-07 prompt-bayesian-reasoning|prompt-bayesian-reasoning]] `prompt` — Walk through Bayesian reasoning step by step for any scenario

## Further reading

- Stanford CS229: Generative Learning Algorithms ([link](https://cs229.stanford.edu/notes2022fall/cs229-notes2.pdf)) — naive Bayes and its connection to discriminative models
- Think Bayes ([link](https://greenteapress.com/wp/think-bayes/)) — free book, Bayesian statistics with Python code
- [[Resources/scikit-learn Naive Bayes|scikit-learn Naive Bayes]] ([link](https://scikit-learn.org/stable/modules/naive_bayes.html)) — production implementations and when to use each variant ·  also cited by 1 other lesson
- 3Blue1Brown: Bayes' theorem ([link](https://www.youtube.com/watch?v=HZGCoVF3YvM)) — visual explanation with the medical test example


%% ── my notes ── %%
