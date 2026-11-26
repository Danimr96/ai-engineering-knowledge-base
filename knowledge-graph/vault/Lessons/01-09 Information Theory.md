---
id: "lesson:01/09"
type: lesson
ref: 01/09
phase: 1
num: 9
title: Information Theory
lesson_type: learn
time_min: 60
on_route: false
quiz_count: 5
code_files: 1
concepts: 10
prereqs: 1
community: 5
aliases:
  - 01/09
  - 01-09
tags:
  - phase/01
  - type/learn
  - community/05
  - stdlib-only
source: ai-engineering-from-scratch/phases/01-math-foundations/09-information-theory/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/09-information-theory"
---

# 01/09 Information Theory

> Information theory measures surprise. Loss functions are built on it.

**Phase:** [[Phases/01 Math Foundations|Phase 1: Math Foundations]] · **Type:** Learn · **Time:** 60 min · **Status:** —  
**Open:** [[Upstream/01-math-foundations/09-information-theory/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/09-information-theory) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/01-math-foundations/09-information-theory) · code: information_theory.py · quiz: 5 questions  
**Community:** [[Communities/05 Temperature · Autoregressive · Logits|05 Temperature · Autoregressive · Logits]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 1, Lesson 06 (Probability)`

- [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]] — Probability

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]], [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]], [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]], [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]]

## Builds on this

- [[Lessons/02-04 Decision Trees and Random Forests|02/04 Decision Trees and Random Forests]]
- [[Lessons/18-22 Differential Privacy for LLMs|18/22 Differential Privacy for LLMs]]
- [[Lessons/18-23 Watermarking — SynthID, Stable Signature, C2PA|18/23 Watermarking — SynthID, Stable Signature, C2PA]]

## Concepts taught

- Information content `lesson term` — The number of bits (or nats) needed to encode an event: -log(p)
- [[Concepts/Entropy|Entropy]] `lesson term` — The average surprise across all outcomes of a distribution. Measures irreducible uncertainty.
- [[Concepts/Cross-Entropy|Cross-Entropy]] `glossary` — Average surprise when using model distribution Q to encode events from true distribution P.
- [[Concepts/KL divergence|KL divergence]] `lesson term` — Extra bits wasted by using Q instead of P. Equals cross-entropy minus entropy. Not symmetric.
- [[Concepts/Mutual information|Mutual information]] `lesson term` — Reduction in uncertainty about X from knowing Y. Zero means independent.
- [[Concepts/Softmax|Softmax]] `glossary` — Exponentiate and normalize. Maps any real-valued vector to a valid probability distribution.
- [[Concepts/Perplexity|Perplexity]] `glossary` — Exponential of cross-entropy. The effective vocabulary size the model is choosing from at each step.
- Bits `lesson term` — Information measured with log base 2. One bit resolves one fair coin flip.
- Nats `lesson term` — Information measured with natural log. Used by PyTorch and TensorFlow by default.
- Negative log-likelihood `lesson term` — Identical to cross-entropy loss for one-hot labels. Minimizing it maximizes the probability of correct predictions.

## Ships

- [[Artifacts/01-09 skill-information-theory|skill-information-theory]] `skill` — Apply information theory concepts to ML loss functions, model evaluation, and feature selection

## Further reading

- Visual Information Theory (Chris Olah) ([link](https://colah.github.io/posts/2015-09-Visual-Information/)) — best visual explanation of entropy and KL divergence
- [[Resources/Shannon 1948- A Mathematical Theory of Communication|Shannon 1948: A Mathematical Theory of Communication]] ([link](https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf)) — the original paper, still readable ·  also cited by 1 other lesson
- PyTorch CrossEntropyLoss docs ([link](https://pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html)) — how the framework implements what you just built


%% ── my notes ── %%
