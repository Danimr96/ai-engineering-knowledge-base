---
id: "lesson:02/14"
type: lesson
ref: 02/14
phase: 2
num: 14
title: Naive Bayes
lesson_type: build
time_min: 75
on_route: false
quiz_count: 0
code_files: 1
concepts: 9
prereqs: 7
community: 4
libraries:
  - numpy
aliases:
  - 02/14
  - 02-14
tags:
  - phase/02
  - type/build
  - community/04
source: ai-engineering-from-scratch/phases/02-ml-fundamentals/14-naive-bayes/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/02-ml-fundamentals/14-naive-bayes"
---

# 02/14 Naive Bayes

> The "naive" assumption is wrong, and it works anyway. That's the beauty of it.

**Phase:** [[Phases/02 ML Fundamentals|Phase 2: ML Fundamentals]] · **Type:** Build · **Time:** 75 min · **Status:** —  
**Open:** [[Upstream/02-ml-fundamentals/14-naive-bayes/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/02-ml-fundamentals/14-naive-bayes) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/02-ml-fundamentals/14-naive-bayes) · code: naive_bayes.py  
**Community:** [[Communities/04 Overfitting · Underfitting · Data Leakage|04 Overfitting · Underfitting · Data Leakage]] · **Libraries:** [[Libraries/numpy (python)|numpy]]  

## Prerequisites

Stated upstream: `Phase 2, Lessons 01-07 (classification, Bayes' theorem)`

- **02/01-07** — classification, Bayes' theorem:
    - [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]]
    - [[Lessons/02-02 Linear Regression|02/02 Linear Regression]]
    - [[Lessons/02-03 Logistic Regression|02/03 Logistic Regression]]
    - [[Lessons/02-04 Decision Trees and Random Forests|02/04 Decision Trees and Random Forests]]
    - [[Lessons/02-05 Support Vector Machines|02/05 Support Vector Machines]]
    - [[Lessons/02-06 K-Nearest Neighbors and Distances|02/06 K-Nearest Neighbors and Distances]]
    - [[Lessons/02-07 Unsupervised Learning|02/07 Unsupervised Learning]]

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/01-08 Optimization|01/08 Optimization]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/01-14 Norms and Distances|01/14 Norms and Distances]], [[Lessons/01-18 Convex Optimization|01/18 Convex Optimization]]
- depth 3: [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]], [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]], [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]], [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]], [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]]

## Builds on this

- [[Lessons/05-01 Text Processing — Tokenization, Stemming, Lemmatization|05/01 Text Processing — Tokenization, Stemming, Lemmatization]]
- [[Lessons/05-05 Sentiment Analysis|05/05 Sentiment Analysis]]
- [[Lessons/05-07 POS Tagging and Syntactic Parsing|05/07 POS Tagging and Syntactic Parsing]]
- [[Lessons/05-16 Text Generation Before Transformers — N-gram Language Models|05/16 Text Generation Before Transformers — N-gram Language Models]]

## Concepts taught

- [[Concepts/Naive Bayes|Naive Bayes]] `lesson term` — A classifier that applies Bayes' theorem with the assumption that features are conditionally independent given the class
- Conditional independence `lesson term` — P(A, B | C) = P(A | C) P(B | C) -- knowing B tells you nothing new about A once you know C
- [[Concepts/Laplace smoothing|Laplace smoothing]] `lesson term` — Adding a small count to every feature to prevent zero probabilities from dominating the prediction
- [[Concepts/Prior|Prior]] `lesson term` — P(class) -- the probability of each class before observing any features
- [[Concepts/Likelihood|Likelihood]] `lesson term` — P(features | class) -- the probability of observing these features if the class is known
- [[Concepts/Posterior|Posterior]] `lesson term` — P(class | features) -- the updated probability of the class after observing the features
- [[Concepts/Generative model|Generative model]] `lesson term` — A model that learns P(X | Y) and P(Y), then uses Bayes' theorem to get P(Y | X)
- Discriminative model `lesson term` — A model that directly learns P(Y | X) without modeling how X is generated
- [[Concepts/Log probability|Log probability]] `lesson term` — Working with log P instead of P to prevent the product of many small numbers from becoming zero in floating point

## Ships

- [[Artifacts/02-14 skill-naive-bayes-chooser|skill-naive-bayes-chooser]] `skill` — Choose the right Naive Bayes variant for your classification task

## Further reading

- Ng and Jordan, On Discriminative vs. Generative Classifiers (2001) ([link](https://ai.stanford.edu/~ang/papers/nips01-discriminativegenerative.pdf)) — proves NB converges faster than LR with less data
- McCallum and Nigam, A Comparison of Event Models for Naive Bayes Text Classification (1998) ([link](https://www.cs.cmu.edu/~knigam/papers/multinomial-aaaiws98.pdf)) — the classic comparison of Multinomial vs Bernoulli for text
- Rennie et al., Tackling the Poor Assumptions of Naive Bayes Text Classifiers (2003) ([link](https://people.csail.mit.edu/jrennie/papers/icml03-nb.pdf)) — improvements to NB for text
- [[Resources/scikit-learn Naive Bayes|scikit-learn Naive Bayes]] ([link](https://scikit-learn.org/stable/modules/naive_bayes.html)) — all three variants with mathematical details ·  also cited by 1 other lesson


%% ── my notes ── %%
