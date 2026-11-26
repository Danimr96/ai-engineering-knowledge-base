---
id: "lesson:19/75"
type: lesson
ref: 19/75
phase: 19
num: 75
title: End-to-End Eval Runner
lesson_type: build
languages:
  - Python
time_min: 90
on_route: false
quiz_count: 6
code_files: 2
concepts: 0
prereqs: 17
community: 2
aliases:
  - 19/75
  - 19-75
tags:
  - phase/19
  - type/build
  - community/02
  - stdlib-only
source: ai-engineering-from-scratch/phases/19-capstone-projects/75-end-to-end-eval-runner/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/75-end-to-end-eval-runner"
---

# 19/75 End-to-End Eval Runner

> Five lessons of plumbing, one lesson to glue them. The runner reads the task spec from lesson 70, calls a model through an adapter, scores with lessons 71 and 72, attaches the calibration report from lesson 73, and emits the leaderboard from lesson 74. Demo self-terminates.

**Phase:** [[Phases/19 Capstone Projects|Phase 19: Capstone Projects]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/19-capstone-projects/75-end-to-end-eval-runner/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/75-end-to-end-eval-runner) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/19-capstone-projects/75-end-to-end-eval-runner) · code: main.py, tests/test_runner.py · quiz: 6 questions  
**Community:** [[Communities/02 Bucket · Causal mask · Manifest|02 Bucket · Causal mask · Manifest]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 19 Track B foundations, lessons 70 through 74`

- **Track B** ·  low confidence:
    - [[Lessons/19-30 BPE Tokenizer From Scratch|19/30 BPE Tokenizer From Scratch]]
    - [[Lessons/19-31 Tokenized Dataset with Sliding Window|19/31 Tokenized Dataset with Sliding Window]]
    - [[Lessons/19-32 Token and Positional Embeddings|19/32 Token and Positional Embeddings]]
    - [[Lessons/19-33 Multi-Head Self-Attention|19/33 Multi-Head Self-Attention]]
    - [[Lessons/19-34 Transformer Block from Scratch|19/34 Transformer Block from Scratch]]
    - [[Lessons/19-35 GPT Model Assembly|19/35 GPT Model Assembly]]
    - [[Lessons/19-36 Training Loop and Evaluation|19/36 Training Loop and Evaluation]]
    - [[Lessons/19-37 Loading Pretrained Weights|19/37 Loading Pretrained Weights]]
    - [[Lessons/19-38 Capstone Lesson 38- Classifier Fine-Tuning by Head Swap|19/38 Capstone Lesson 38: Classifier Fine-Tuning by Head Swap]]
    - [[Lessons/19-39 Capstone Lesson 39- Instruction Tuning by Supervised Fine-Tuning|19/39 Capstone Lesson 39: Instruction Tuning by Supervised Fine-Tuning]]
    - [[Lessons/19-40 Capstone Lesson 40- Direct Preference Optimization from Scratch|19/40 Capstone Lesson 40: Direct Preference Optimization from Scratch]]
    - [[Lessons/19-41 Capstone Lesson 41- Full Evaluation Pipeline|19/41 Capstone Lesson 41: Full Evaluation Pipeline]]
- **19/70-74**:
    - [[Lessons/19-70 Task Spec Format|19/70 Task Spec Format]]
    - [[Lessons/19-71 Classical Metrics|19/71 Classical Metrics]]
    - [[Lessons/19-72 Code Exec Metric|19/72 Code Exec Metric]]
    - [[Lessons/19-73 Perplexity and Calibration|19/73 Perplexity and Calibration]]
    - [[Lessons/19-74 Leaderboard Aggregation|19/74 Leaderboard Aggregation]]


%% ── my notes ── %%
