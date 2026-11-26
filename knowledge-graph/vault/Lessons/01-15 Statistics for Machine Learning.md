---
id: "lesson:01/15"
type: lesson
ref: 01/15
phase: 1
num: 15
title: Statistics for Machine Learning
lesson_type: build
time_min: 120
on_route: false
quiz_count: 5
code_files: 1
concepts: 22
prereqs: 2
community: 67
aliases:
  - 01/15
  - 01-15
tags:
  - phase/01
  - type/build
  - community/67
  - stdlib-only
source: ai-engineering-from-scratch/phases/01-math-foundations/15-statistics-for-ml/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/15-statistics-for-ml"
---

# 01/15 Statistics for Machine Learning

> Statistics is how you know if your model actually works or just got lucky.

**Phase:** [[Phases/01 Math Foundations|Phase 1: Math Foundations]] · **Type:** Build · **Time:** 120 min · **Status:** —  
**Open:** [[Upstream/01-math-foundations/15-statistics-for-ml/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/15-statistics-for-ml) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/01-math-foundations/15-statistics-for-ml) · code: statistics.py · quiz: 5 questions  
**Community:** [[Communities/67 Central Limit Theorem · Confidence interval · Covariance matrix|67 Central Limit Theorem · Confidence interval · Covariance matrix]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 1, Lessons 06 (Probability and Distributions), 07 (Bayes' Theorem)`

- [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]] — Probability and Distributions
- [[Lessons/01-07 Bayes' Theorem|01/07 Bayes' Theorem]] — Bayes' Theorem

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]], [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]], [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]], [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]]

## Concepts taught

- Mean `lesson term` — Sum of values divided by count. Sensitive to outliers.
- Median `lesson term` — Middle value of sorted data. Robust to outliers.
- Standard deviation `lesson term` — Square root of variance. Measures spread in original units.
- Percentile `lesson term` — Value below which a given percentage of data falls.
- [[Concepts/IQR|IQR]] `lesson term` — Interquartile range. Q3 minus Q1. The spread of the middle 50%.
- Pearson correlation `lesson term` — Measures linear association between two variables. Range [-1, 1].
- Spearman correlation `lesson term` — Measures monotonic association using ranks.
- [[Concepts/Covariance matrix|Covariance matrix]] `lesson term` — Matrix of pairwise covariances between all features.
- Null hypothesis `lesson term` — Default assumption of no effect or no difference.
- p-value `lesson term` — Probability of data this extreme given the null hypothesis is true.
- [[Concepts/Confidence interval|Confidence interval]] `lesson term` — Range of plausible values for a parameter at a given confidence level.
- t-test `lesson term` — Tests whether means differ significantly. Uses the t-distribution.
- Chi-squared test `lesson term` — Tests whether observed frequencies differ from expected frequencies.
- Effect size `lesson term` — Magnitude of a difference, independent of sample size. Cohen's d is common.
- Bonferroni correction `lesson term` — Divides significance threshold by number of tests to control false positives.
- [[Concepts/Bootstrap|Bootstrap]] `lesson term` — Resampling with replacement to estimate sampling distributions.
- Type I error `lesson term` — False positive. Rejecting H0 when it is true.
- Type II error `lesson term` — False negative. Failing to reject H0 when it is false.
- Statistical power `lesson term` — Probability of correctly rejecting a false H0. Power = 1 minus Type II error rate.
- [[Concepts/Central Limit Theorem|Central Limit Theorem]] `lesson term` — Sample means converge to a normal distribution as sample size grows.
- Parametric test `lesson term` — Assumes a specific distribution for the data (usually normal).
- Non-parametric test `lesson term` — Makes no distributional assumptions. Works on ranks or signs.

## Ships

- [[Artifacts/01-15 skill-statistical-testing|skill-statistical-testing]] `skill` — Choose the right statistical test for comparing ML models and evaluating experiments


%% ── my notes ── %%
