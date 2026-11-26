---
id: "lesson:19/76"
type: lesson
ref: 19/76
phase: 19
num: 76
title: Collective Ops From Scratch
lesson_type: build
languages:
  - Python
time_min: 90
on_route: false
quiz_count: 6
code_files: 1
concepts: 6
prereqs: 8
community: 2
libraries:
  - torch
aliases:
  - 19/76
  - 19-76
tags:
  - phase/19
  - type/build
  - community/02
source: ai-engineering-from-scratch/phases/19-capstone-projects/76-collective-ops-from-scratch/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/76-collective-ops-from-scratch"
---

# 19/76 Collective Ops From Scratch

> The four collective operations that hold distributed training together are allreduce, broadcast, allgather, and reduce_scatter. Every other primitive a training framework offers is a wrapper around these. Build them once over a `multiprocessing.Queue` mesh, verify them against a reference implementation, and the rest of the track becomes plumbing.

**Phase:** [[Phases/19 Capstone Projects|Phase 19: Capstone Projects]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/19-capstone-projects/76-collective-ops-from-scratch/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/76-collective-ops-from-scratch) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/19-capstone-projects/76-collective-ops-from-scratch) · code: main.py · quiz: 6 questions  
**Community:** [[Communities/02 Bucket · Causal mask · Manifest|02 Bucket · Causal mask · Manifest]] · **Libraries:** [[Libraries/torch (python)|torch]]  

## Prerequisites

Stated upstream: `Phase 19 Track C lessons 42-49`

- **19/42-49**:
    - [[Lessons/19-42 Large Corpus Downloader|19/42 Large Corpus Downloader]]
    - [[Lessons/19-43 HDF5 Tokenized Corpus|19/43 HDF5 Tokenized Corpus]]
    - [[Lessons/19-44 Cosine LR with Linear Warmup|19/44 Cosine LR with Linear Warmup]]
    - [[Lessons/19-45 Gradient Clipping and Mixed Precision|19/45 Gradient Clipping and Mixed Precision]]
    - [[Lessons/19-46 Gradient Accumulation|19/46 Gradient Accumulation]]
    - [[Lessons/19-47 Checkpoint Save and Resume|19/47 Checkpoint Save and Resume]]
    - [[Lessons/19-48 Distributed Data Parallel and FSDP from Scratch|19/48 Distributed Data Parallel and FSDP from Scratch]]
    - [[Lessons/19-49 Language Model Evaluation Harness|19/49 Language Model Evaluation Harness]]

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/19-30 BPE Tokenizer From Scratch|19/30 BPE Tokenizer From Scratch]], [[Lessons/19-31 Tokenized Dataset with Sliding Window|19/31 Tokenized Dataset with Sliding Window]], [[Lessons/19-32 Token and Positional Embeddings|19/32 Token and Positional Embeddings]], [[Lessons/19-33 Multi-Head Self-Attention|19/33 Multi-Head Self-Attention]], [[Lessons/19-34 Transformer Block from Scratch|19/34 Transformer Block from Scratch]], [[Lessons/19-35 GPT Model Assembly|19/35 GPT Model Assembly]], [[Lessons/19-36 Training Loop and Evaluation|19/36 Training Loop and Evaluation]], [[Lessons/19-37 Loading Pretrained Weights|19/37 Loading Pretrained Weights]]

## Concepts taught

- Allreduce `lesson term` — After the call every rank holds the same reduced tensor
- Ring `lesson term` — N-1 chunks of size T/N flow around the cycle twice
- Tree `lesson term` — Reduction follows a binary tree; depth is log2(N) hops
- Allgather `lesson term` — Every rank ends with every other rank's shard
- [[Concepts/Reduce-scatter|Reduce-scatter]] (as *Reduce_scatter*) `lesson term` — Each rank ends with the sum of one chunk only
- [[Concepts/Bucket|Bucket]] `lesson term` — Coalesce N small allreduces into one large one

## Further reading

- Horovod ring allreduce paper ([link](https://arxiv.org/abs/1802.05799))
- Patarasuk and Yuan, Bandwidth optimal allreduce algorithms ([link](https://www.cs.fsu.edu/~xyuan/paper/09jpdc.pdf))
- NCCL topology and algorithm selection ([link](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/index.html))
- PyTorch Distributed: NCCL collectives ([link](https://pytorch.org/docs/stable/distributed.html#collective-functions))


%% ── my notes ── %%
