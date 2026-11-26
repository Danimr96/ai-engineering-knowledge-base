---
id: "concept:weight-tying"
type: concept
name: Weight tying
canonical: false
taught_in: 3
community: 1
tags:
  - concept/lesson-term
  - community/01
source: ai-engineering-from-scratch/phases/10-llms-from-scratch/04-pre-training-mini-gpt/docs/en.md
---

# Weight tying

**Community:** [[Communities/01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism|01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism]]

> *What people say:* "Sharing embeddings"

**What it actually means:** Using the same matrix for input token embeddings and the output projection head -- saves 38M params in GPT-2

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]]
- [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]] — Using the same matrix for input token embeddings and output prediction head, saving parameters and improving coherence
- [[Lessons/19-35 GPT Model Assembly|19/35 GPT Model Assembly]] — The LM head and the token embedding share the same parameter tensor; saves vocab times d_model parameters and matches the GPT-2 reference


%% ── my notes ── %%
