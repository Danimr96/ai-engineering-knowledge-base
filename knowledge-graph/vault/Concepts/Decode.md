---
id: "concept:decode"
type: concept
name: Decode
canonical: false
taught_in: 2
community: 1
tags:
  - concept/lesson-term
  - community/01
source: ai-engineering-from-scratch/phases/10-llms-from-scratch/04-pre-training-mini-gpt/docs/en.md
---

# Decode

**Community:** [[Communities/01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism|01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism]]

> *What people say:* "Generating tokens"

**What it actually means:** The second inference phase where tokens are generated one at a time -- memory-bound on GPU bandwidth

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]]
- [[Lessons/10-12 Inference Optimization|10/12 Inference Optimization]] — Producing one token per forward pass, reading the full model weights each time -- memory-bound because compute finishes before the next weights arrive


%% ── my notes ── %%
