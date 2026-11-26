---
id: "lesson:00/03"
type: lesson
ref: 00/03
phase: 0
num: 3
title: "GPU Setup & Cloud"
lesson_type: build
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 5
code_files: 1
concepts: 4
prereqs: 1
libraries:
  - torch
aliases:
  - 00/03
  - 00-03
tags:
  - phase/00
  - type/build
source: ai-engineering-from-scratch/phases/00-setup-and-tooling/03-gpu-setup-and-cloud/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/00-setup-and-tooling/03-gpu-setup-and-cloud"
---

# 00/03 GPU Setup & Cloud

> Training on CPU is fine for learning. Training for real needs a GPU.

**Phase:** [[Phases/00 Setup & Tooling|Phase 0: Setup & Tooling]] · **Type:** Build · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/00-setup-and-tooling/03-gpu-setup-and-cloud/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/00-setup-and-tooling/03-gpu-setup-and-cloud) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/00-setup-and-tooling/03-gpu-setup-and-cloud) · code: gpu_check.py · quiz: 5 questions  
**Libraries:** [[Libraries/torch (python)|torch]]  

## Prerequisites

Stated upstream: `Phase 0, Lesson 01`

- [[Lessons/00-01 Dev Environment|00/01 Dev Environment]]

## Builds on this

- [[Lessons/00-07 Docker for AI|00/07 Docker for AI]]

## Concepts taught

- [[Concepts/CUDA|CUDA]] `glossary` — NVIDIA's parallel computing platform that lets you run code on the GPU
- VRAM `lesson term` — Video RAM on the GPU, separate from system RAM. Limits model size.
- [[Concepts/fp16|fp16]] `lesson term` — 16-bit floating point, uses half the memory of fp32 with minimal accuracy loss
- Tensor Core `lesson term` — Specialized GPU cores for matrix multiplication, 4-8x faster than regular cores


%% ── my notes ── %%
