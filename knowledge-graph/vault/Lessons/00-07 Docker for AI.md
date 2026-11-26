---
id: "lesson:00/07"
type: lesson
ref: 00/07
phase: 0
num: 7
title: Docker for AI
lesson_type: build
languages:
  - Docker
time_min: 60
on_route: false
quiz_count: 5
code_files: 0
concepts: 5
prereqs: 2
aliases:
  - 00/07
  - 00-07
tags:
  - phase/00
  - type/build
source: ai-engineering-from-scratch/phases/00-setup-and-tooling/07-docker-for-ai/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/00-setup-and-tooling/07-docker-for-ai"
---

# 00/07 Docker for AI

> Containers make "works on my machine" a thing of the past.

**Phase:** [[Phases/00 Setup & Tooling|Phase 0: Setup & Tooling]] · **Type:** Build · **Time:** 60 min · **Languages:** Docker · **Status:** —  
**Open:** [[Upstream/00-setup-and-tooling/07-docker-for-ai/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/00-setup-and-tooling/07-docker-for-ai) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/00-setup-and-tooling/07-docker-for-ai) · quiz: 5 questions  

## Prerequisites

Stated upstream: `Phase 0, Lessons 01 and 03`

- [[Lessons/00-01 Dev Environment|00/01 Dev Environment]]
- [[Lessons/00-03 GPU Setup & Cloud|00/03 GPU Setup & Cloud]]

## Concepts taught

- Container `lesson term` — An isolated process using the host kernel, with its own filesystem and network
- Image layer `lesson term` — Each Dockerfile instruction creates a layer. Unchanged layers are cached, so rebuilds are fast.
- NVIDIA Container Toolkit `lesson term` — A runtime hook that exposes host GPUs to containers via --gpus flag
- Volume mount `lesson term` — A directory on the host mapped into the container. Changes persist after the container stops.
- Base image `lesson term` — The FROM image your Dockerfile builds on top of. Determines what is pre-installed.

## In learning paths

- [[Paths/Software Engineering Fundamentals|Software Engineering Fundamentals]] — step 4, required


%% ── my notes ── %%
