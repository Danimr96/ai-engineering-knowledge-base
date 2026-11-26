---
id: "lesson:19/49"
type: lesson
ref: 19/49
phase: 19
num: 49
title: Language Model Evaluation Harness
lesson_type: build
languages:
  - Python
time_min: 90
on_route: false
quiz_count: 6
code_files: 2
concepts: 5
prereqs: 4
community: 2
aliases:
  - 19/49
  - 19-49
tags:
  - phase/19
  - type/build
  - community/02
  - stdlib-only
source: ai-engineering-from-scratch/phases/19-capstone-projects/49-lm-eval-harness/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/49-lm-eval-harness"
---

# 19/49 Language Model Evaluation Harness

> A model that does well on a task you cannot define is a model that does well by accident. The harness is the task definition, the metric, the runner, and the leaderboard, in one short, swappable shape.

**Phase:** [[Phases/19 Capstone Projects|Phase 19: Capstone Projects]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/19-capstone-projects/49-lm-eval-harness/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/49-lm-eval-harness) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/19-capstone-projects/49-lm-eval-harness) · code: main.py, test_main.py · quiz: 6 questions  
**Track:** [[Tracks/19-C Large-scale pre-training infrastructure|Phase 19 Track C: Large-scale pre-training infrastructure]]  
**Community:** [[Communities/02 Bucket · Causal mask · Manifest|02 Bucket · Causal mask · Manifest]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 19 lessons 42 to 45`

- **19/42-45**:
    - [[Lessons/19-42 Large Corpus Downloader|19/42 Large Corpus Downloader]]
    - [[Lessons/19-43 HDF5 Tokenized Corpus|19/43 HDF5 Tokenized Corpus]]
    - [[Lessons/19-44 Cosine LR with Linear Warmup|19/44 Cosine LR with Linear Warmup]]
    - [[Lessons/19-45 Gradient Clipping and Mixed Precision|19/45 Gradient Clipping and Mixed Precision]]

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/19-30 BPE Tokenizer From Scratch|19/30 BPE Tokenizer From Scratch]], [[Lessons/19-31 Tokenized Dataset with Sliding Window|19/31 Tokenized Dataset with Sliding Window]], [[Lessons/19-32 Token and Positional Embeddings|19/32 Token and Positional Embeddings]], [[Lessons/19-33 Multi-Head Self-Attention|19/33 Multi-Head Self-Attention]], [[Lessons/19-34 Transformer Block from Scratch|19/34 Transformer Block from Scratch]], [[Lessons/19-35 GPT Model Assembly|19/35 GPT Model Assembly]], [[Lessons/19-36 Training Loop and Evaluation|19/36 Training Loop and Evaluation]], [[Lessons/19-37 Loading Pretrained Weights|19/37 Loading Pretrained Weights]]

## Builds on this

- [[Lessons/19-76 Collective Ops From Scratch|19/76 Collective Ops From Scratch]]
- [[Lessons/19-77 Data Parallel DDP From Scratch|19/77 Data Parallel DDP From Scratch]]
- [[Lessons/19-78 ZeRO Optimizer State Sharding|19/78 ZeRO Optimizer State Sharding]]
- [[Lessons/19-79 Pipeline Parallel and Bubble Analysis|19/79 Pipeline Parallel and Bubble Analysis]]
- [[Lessons/19-80 Sharded Checkpoint and Atomic Resume|19/80 Sharded Checkpoint and Atomic Resume]]
- [[Lessons/19-81 End-to-End Distributed Training|19/81 End-to-End Distributed Training]]

## Concepts taught

- Task spec `lesson term` — JSONL file with prompt, targets, metric, optional extras per example
- Metric `lesson term` — Function from (prediction, targets, extras) to a float in [0, 1]
- [[Concepts/Adapter|Adapter]] `lesson term` — Object with a generate(prompts) -> list[str] method; the only model-specific code
- Leaderboard `lesson term` — JSON with per-task scores, total counts, latency, and an overall average
- Code exec metric `lesson term` — Execute the prediction in a restricted namespace, compare against input-output pairs

## Ships

- [[Artifacts/19-49 lm-eval-harness|lm-eval-harness]] `skill` — Minimal language model evaluation harness with JSONL task spec, five metrics, swappable adapter, and leaderboard JSON output.


%% ── my notes ── %%
