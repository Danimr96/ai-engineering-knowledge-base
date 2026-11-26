---
id: "lesson:00/09"
type: lesson
ref: 00/09
phase: 0
num: 9
title: Data Management
lesson_type: build
time_min: 45
on_route: false
quiz_count: 5
code_files: 1
concepts: 7
prereqs: 1
community: 86
libraries:
  - datasets
  - huggingface_hub
aliases:
  - 00/09
  - 00-09
tags:
  - phase/00
  - type/build
  - community/86
source: ai-engineering-from-scratch/phases/00-setup-and-tooling/09-data-management/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/00-setup-and-tooling/09-data-management"
---

# 00/09 Data Management

> Data is the fuel. How you manage it determines how fast you go.

**Phase:** [[Phases/00 Setup & Tooling|Phase 0: Setup & Tooling]] · **Type:** Build · **Time:** 45 min · **Status:** —  
**Open:** [[Upstream/00-setup-and-tooling/09-data-management/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/00-setup-and-tooling/09-data-management) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/00-setup-and-tooling/09-data-management) · code: data_utils.py · quiz: 5 questions  
**Community:** [[Communities/86 DVC · Pipeline|86 DVC · Pipeline]] · **Libraries:** [[Libraries/datasets (python)|datasets]], [[Libraries/huggingface_hub (python)|huggingface_hub]]  

## Prerequisites

Stated upstream: `Phase 0, Lesson 01`

- [[Lessons/00-01 Dev Environment|00/01 Dev Environment]]

## Concepts taught

- [[Concepts/Dataset Split|Dataset Split]] `glossary` — A named subset (train/val/test) used at different stages of the ML lifecycle
- [[Concepts/Streaming|Streaming]] `glossary` — Processing data row by row from a remote source without downloading the full dataset
- Parquet `lesson term` — A columnar file format optimized for analytical queries and storage efficiency
- Arrow `lesson term` — An in-memory columnar format used internally by the datasets library for zero-copy reads
- Git LFS `lesson term` — An extension that stores large files outside the git repo while keeping pointers in version control
- [[Concepts/DVC|DVC]] `lesson term` — A version control system for datasets and models that integrates with cloud storage
- Cache `lesson term` — A local copy of previously fetched data, stored at ~/.cache/huggingface/ by default

## Ships

- [[Artifacts/00-09 prompt-data-helper|prompt-data-helper]] `prompt` — Find and load the right dataset for an AI/ML task

## In learning paths

- [[Paths/AI Data Systems|AI Data Systems]] — step 1, required
- [[Paths/Software Engineering Fundamentals|Software Engineering Fundamentals]] — step 5, required


%% ── my notes ── %%
