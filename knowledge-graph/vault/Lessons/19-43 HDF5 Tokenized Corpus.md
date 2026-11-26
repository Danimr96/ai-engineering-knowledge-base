---
id: "lesson:19/43"
type: lesson
ref: 19/43
phase: 19
num: 43
title: HDF5 Tokenized Corpus
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
  - h5py
  - numpy
aliases:
  - 19/43
  - 19-43
tags:
  - phase/19
  - type/build
  - community/02
source: ai-engineering-from-scratch/phases/19-capstone-projects/43-hdf5-tokenized-corpus/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/43-hdf5-tokenized-corpus"
---

# 19/43 HDF5 Tokenized Corpus

> The downloaded corpus has to land in a layout the trainer can stream from at line speed. JSONL on disk does not survive 16 dataloader workers. HDF5 with a resizable, chunked integer dataset does. This lesson builds streaming tokenization into a resizable HDF5 dataset, sharded write across multiple files, memory-mapped read at training time, and a sliding-window dataloader that produces fixed-length sequences with the right packing.

**Phase:** [[Phases/19 Capstone Projects|Phase 19: Capstone Projects]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/19-capstone-projects/43-hdf5-tokenized-corpus/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/43-hdf5-tokenized-corpus) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/19-capstone-projects/43-hdf5-tokenized-corpus) · code: main.py, tests/__init__.py, tests/test_hdf5_corpus.py · quiz: 6 questions  
**Track:** [[Tracks/19-C Large-scale pre-training infrastructure|Phase 19 Track C: Large-scale pre-training infrastructure]]  
**Community:** [[Communities/02 Bucket · Causal mask · Manifest|02 Bucket · Causal mask · Manifest]] · **Libraries:** [[Libraries/h5py (python)|h5py]], [[Libraries/numpy (python)|numpy]]  

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

- Resizable dataset `lesson term` — An HDF5 dataset with maxshape=(None,) that grows via resize calls in chunk-sized strides
- Chunked layout `lesson term` — Fixed-size on-disk pages that the kernel can memory-map and the dataloader can read contiguously
- swmr mode `lesson term` — Single-Writer-Multiple-Reader mode that lets dataloader workers share the file safely
- Shard index `lesson term` — The durable index of all token shards with offsets and content hashes
- [[Concepts/Sliding window|Sliding window]] `lesson term` — A fixed-length slice of the global token stream that the trainer pairs with its shift-by-one target

## Further reading

- h5py user guide ([link](https://docs.h5py.org/en/stable/)) — Python bindings for HDF5
- NumPy memory mapping ([link](https://numpy.org/doc/stable/reference/generated/numpy.memmap.html)) — the read-side primitive HDF5 exposes through h5py
- HDF5 chunking documentation ([link](https://support.hdfgroup.org/documentation/hdf5/latest/hdf5_chunking.html)) — the chunked, resizable dataset layout this lesson uses


%% ── my notes ── %%
