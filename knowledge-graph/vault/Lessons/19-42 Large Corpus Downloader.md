---
id: "lesson:19/42"
type: lesson
ref: 19/42
phase: 19
num: 42
title: Large Corpus Downloader
lesson_type: build
languages:
  - Python
time_min: 90
on_route: false
quiz_count: 6
code_files: 3
concepts: 5
prereqs: 8
community: 2
libraries:
  - zstandard
aliases:
  - 19/42
  - 19-42
tags:
  - phase/19
  - type/build
  - community/02
source: ai-engineering-from-scratch/phases/19-capstone-projects/42-large-corpus-downloader/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/42-large-corpus-downloader"
---

# 19/42 Large Corpus Downloader

> Training a language model begins long before the first forward pass. The corpus has to land on disk, decompressed, deduplicated, and addressable, with the resume story already worked out before the network drops at 4 percent. This lesson builds a streaming downloader that pulls compressed shards, decompresses on the fly with Zstandard, fingerprints near-duplicates via MinHash plus locality-sensitive hashing, and writes a shard manifest the rest of the pipeline can trust.

**Phase:** [[Phases/19 Capstone Projects|Phase 19: Capstone Projects]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/19-capstone-projects/42-large-corpus-downloader/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/42-large-corpus-downloader) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/19-capstone-projects/42-large-corpus-downloader) · code: main.py, tests/__init__.py, tests/test_downloader.py · quiz: 6 questions  
**Track:** [[Tracks/19-C Large-scale pre-training infrastructure|Phase 19 Track C: Large-scale pre-training infrastructure]]  
**Community:** [[Communities/02 Bucket · Causal mask · Manifest|02 Bucket · Causal mask · Manifest]] · **Libraries:** [[Libraries/zstandard (python)|zstandard]]  

## Prerequisites

Stated upstream: `Phase 19 lessons 30-37`

- **19/30-37**:
    - [[Lessons/19-30 BPE Tokenizer From Scratch|19/30 BPE Tokenizer From Scratch]]
    - [[Lessons/19-31 Tokenized Dataset with Sliding Window|19/31 Tokenized Dataset with Sliding Window]]
    - [[Lessons/19-32 Token and Positional Embeddings|19/32 Token and Positional Embeddings]]
    - [[Lessons/19-33 Multi-Head Self-Attention|19/33 Multi-Head Self-Attention]]
    - [[Lessons/19-34 Transformer Block from Scratch|19/34 Transformer Block from Scratch]]
    - [[Lessons/19-35 GPT Model Assembly|19/35 GPT Model Assembly]]
    - [[Lessons/19-36 Training Loop and Evaluation|19/36 Training Loop and Evaluation]]
    - [[Lessons/19-37 Loading Pretrained Weights|19/37 Loading Pretrained Weights]]

## Builds on this

- [[Lessons/19-46 Gradient Accumulation|19/46 Gradient Accumulation]]
- [[Lessons/19-47 Checkpoint Save and Resume|19/47 Checkpoint Save and Resume]]
- [[Lessons/19-48 Distributed Data Parallel and FSDP from Scratch|19/48 Distributed Data Parallel and FSDP from Scratch]]
- [[Lessons/19-49 Language Model Evaluation Harness|19/49 Language Model Evaluation Harness]]
- [[Lessons/19-76 Collective Ops From Scratch|19/76 Collective Ops From Scratch]]
- [[Lessons/19-77 Data Parallel DDP From Scratch|19/77 Data Parallel DDP From Scratch]]
- [[Lessons/19-78 ZeRO Optimizer State Sharding|19/78 ZeRO Optimizer State Sharding]]
- [[Lessons/19-79 Pipeline Parallel and Bubble Analysis|19/79 Pipeline Parallel and Bubble Analysis]]
- [[Lessons/19-80 Sharded Checkpoint and Atomic Resume|19/80 Sharded Checkpoint and Atomic Resume]]
- [[Lessons/19-81 End-to-End Distributed Training|19/81 End-to-End Distributed Training]]

## Concepts taught

- Shard `lesson term` — A self-contained slice of the corpus with its own sha256, used as the unit of resume and dedup
- MinHash signature `lesson term` — A k-component sketch of a set, where each component is the minimum of one independent hash over the set
- LSH band `lesson term` — A group of r signature components used as a single bucket key for collision detection
- Verified bytes `lesson term` — Bytes on disk whose sha256 prefix matches the checkpoint; the only safe offset to resume from
- [[Concepts/Manifest|Manifest]] `lesson term` — The single durable record of what the downloader produced, including content hashes

## Further reading

- RFC 7233 ([link](https://datatracker.ietf.org/doc/html/rfc7233)) — HTTP Range requests, the resume protocol
- Zstandard format specification ([link](https://datatracker.ietf.org/doc/html/rfc8478)) — frame format that makes streaming decompression safe
- Locality-sensitive hashing ([link](https://en.wikipedia.org/wiki/Locality-sensitive_hashing)) — the banding scheme behind the dedup threshold
- MinHash ([link](https://en.wikipedia.org/wiki/MinHash)) — the signature family this lesson uses


%% ── my notes ── %%
