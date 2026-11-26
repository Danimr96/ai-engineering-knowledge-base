---
id: "lesson:02/13"
type: lesson
ref: 02/13
phase: 2
num: 13
title: ML Pipelines
lesson_type: build
time_min: 120
on_route: false
quiz_count: 0
code_files: 1
concepts: 9
prereqs: 1
community: 86
libraries:
  - numpy
  - pandas
  - scikit-learn
aliases:
  - 02/13
  - 02-13
tags:
  - phase/02
  - type/build
  - community/86
source: ai-engineering-from-scratch/phases/02-ml-fundamentals/13-ml-pipelines/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/02-ml-fundamentals/13-ml-pipelines"
---

# 02/13 ML Pipelines

> A model is not a product. A pipeline is. The pipeline is everything from raw data to deployed prediction, and every step must be reproducible.

**Phase:** [[Phases/02 ML Fundamentals|Phase 2: ML Fundamentals]] · **Type:** Build · **Time:** 120 min · **Status:** —  
**Open:** [[Upstream/02-ml-fundamentals/13-ml-pipelines/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/02-ml-fundamentals/13-ml-pipelines) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/02-ml-fundamentals/13-ml-pipelines) · code: pipeline.py  
**Community:** [[Communities/86 DVC · Pipeline|86 DVC · Pipeline]] · **Libraries:** [[Libraries/numpy (python)|numpy]], [[Libraries/pandas (python)|pandas]], [[Libraries/scikit-learn (python)|scikit-learn]]  

## Prerequisites

Stated upstream: `Phase 2, Lesson 12 (Hyperparameter Tuning)`

- [[Lessons/02-12 Hyperparameter Tuning|02/12 Hyperparameter Tuning]] — Hyperparameter Tuning

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/02-11 Ensemble Methods|02/11 Ensemble Methods]]
- depth 3: [[Lessons/02-10 Bias-Variance Tradeoff|02/10 Bias-Variance Tradeoff]]

## Concepts taught

- [[Concepts/Pipeline|Pipeline]] `lesson term` — An ordered sequence of fitted transformers and a model, applied as one unit to prevent leakage
- [[Concepts/Data Leakage|Data Leakage]] `glossary` — Using information from outside the training set to build the model, inflating performance estimates
- ColumnTransformer `lesson term` — Applies different pipelines to different subsets of columns, combining results
- Experiment tracking `lesson term` — Recording parameters, metrics, artifacts, and code versions for every training run
- MLflow `lesson term` — Open-source platform for experiment tracking, model registry, and deployment
- [[Concepts/DVC|DVC]] `lesson term` — Version control system for large data files, storing hashes in git and data in remote storage
- Model registry `lesson term` — A system that tracks model versions with stage labels (staging, production, archived)
- Training/serving skew `lesson term` — Differences between how data is processed during training versus inference, causing silent errors
- Reproducibility `lesson term` — The ability to get identical results from the same code, data, and configuration

## Ships

- [[Artifacts/02-13 prompt-ml-pipeline|prompt-ml-pipeline]] `prompt` — Build, debug, and deploy reproducible ML pipelines

## Further reading

- Google ML Best Practices: Rules of ML ([link](https://developers.google.com/machine-learning/guides/rules-of-ml)) — practical production ML advice
- DVC documentation ([link](https://dvc.org/doc)) — data versioning
- MLflow documentation ([link](https://mlflow.org/docs/latest/index.html)) — experiment tracking and model registry
- Sculley et al., Hidden Technical Debt in Machine Learning Systems (2015) ([link](https://papers.nips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html)) — the seminal paper on ML systems complexity
- scikit-learn Pipeline docs ([link](https://scikit-learn.org/stable/modules/compose.html)) — the official pipeline reference

## In learning paths

- [[Paths/AI Data Systems|AI Data Systems]] — step 3, required


%% ── my notes ── %%
