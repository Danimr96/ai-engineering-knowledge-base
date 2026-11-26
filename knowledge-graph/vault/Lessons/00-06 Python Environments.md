---
id: "lesson:00/06"
type: lesson
ref: 00/06
phase: 0
num: 6
title: Python Environments
lesson_type: build
languages:
  - Shell
time_min: 30
on_route: false
quiz_count: 5
code_files: 0
concepts: 5
prereqs: 1
community: 38
aliases:
  - 00/06
  - 00-06
tags:
  - phase/00
  - type/build
  - community/38
source: ai-engineering-from-scratch/phases/00-setup-and-tooling/06-python-environments/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/00-setup-and-tooling/06-python-environments"
---

# 00/06 Python Environments

> Dependency hell is real. Virtual environments are the cure.

**Phase:** [[Phases/00 Setup & Tooling|Phase 0: Setup & Tooling]] · **Type:** Build · **Time:** 30 min · **Languages:** Shell · **Status:** —  
**Open:** [[Upstream/00-setup-and-tooling/06-python-environments/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/00-setup-and-tooling/06-python-environments) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/00-setup-and-tooling/06-python-environments) · quiz: 5 questions  
**Community:** [[Communities/38 Dev Environment · Git & Collaboration · APIs & Keys|38 Dev Environment · Git & Collaboration · APIs & Keys]]  

## Prerequisites

Stated upstream: `Phase 0, Lesson 01`

- [[Lessons/00-01 Dev Environment|00/01 Dev Environment]]

## Concepts taught

- Virtual environment `lesson term` — An isolated directory containing a Python interpreter and packages, separate from the system Python
- Lockfile `lesson term` — A file listing every package and its exact version, guaranteeing identical installs across machines
- pyproject.toml `lesson term` — The standard Python project configuration file, replacing setup.py/setup.cfg/requirements.txt
- Transitive dependency `lesson term` — Package B depends on C; if you install A which depends on B, C is a transitive dependency of A
- CUDA mismatch `lesson term` — PyTorch was compiled for a different CUDA version than what your GPU driver supports

## In learning paths

- [[Paths/Software Engineering Fundamentals|Software Engineering Fundamentals]] — step 3, required


%% ── my notes ── %%
