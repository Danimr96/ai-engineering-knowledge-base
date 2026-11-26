---
id: "lesson:07/01"
type: lesson
ref: 07/01
phase: 7
num: 1
title: "Why Transformers — The Problems with RNNs"
lesson_type: learn
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 0
code_files: 2
concepts: 7
prereqs: 2
community: 12
aliases:
  - 07/01
  - 07-01
tags:
  - phase/07
  - type/learn
  - community/12
  - stdlib-only
source: ai-engineering-from-scratch/phases/07-transformers-deep-dive/01-why-transformers/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/07-transformers-deep-dive/01-why-transformers"
---

# 07/01 Why Transformers — The Problems with RNNs

> RNNs process tokens one at a time. Transformers process all tokens at once. That single architectural bet changed every scaling curve in deep learning after 2017.

**Phase:** [[Phases/07 Transformers Deep Dive|Phase 7: Transformers Deep Dive]] · **Type:** Learn · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/07-transformers-deep-dive/01-why-transformers/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/07-transformers-deep-dive/01-why-transformers) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/07-transformers-deep-dive/01-why-transformers) · code: main.jl, main.py  
**Community:** [[Communities/12 Attention · Cross-Attention · Self-Attention|12 Attention · Cross-Attention · Self-Attention]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 3 (Deep Learning Core), Phase 5 · 09 (Sequence-to-Sequence), Phase 5 · 10 (Attention Mechanism)`

- [[Lessons/05-09 Sequence-to-Sequence Models|05/09 Sequence-to-Sequence Models]] — Sequence-to-Sequence
- [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]] — Attention Mechanism
- Whole phase: [[Phases/03 Deep Learning Core|Phase 3: Deep Learning Core]] — Deep Learning Core ·  medium confidence

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]], [[Lessons/05-08 CNNs and RNNs for Text|05/08 CNNs and RNNs for Text]]
- depth 3: [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]], [[Lessons/04-02 Convolutions from Scratch|04/02 Convolutions from Scratch]], [[Lessons/05-03 Word Embeddings — Word2Vec from Scratch|05/03 Word Embeddings — Word2Vec from Scratch]]

## Builds on this

- [[Lessons/07-14 Build a Transformer from Scratch — The Capstone|07/14 Build a Transformer from Scratch — The Capstone]]

## Concepts taught

- Recurrence `lesson term` — Computation where step t depends on step t-1, forcing serial execution along the time axis.
- Serial depth `lesson term` — Longest chain of dependent ops; bounds wall-clock even on infinite hardware.
- [[Concepts/Attention|Attention]] `glossary` — Weighted sum sum_j a_ij v_j where a_ij comes from a similarity score between positions i and j.
- [[Concepts/Context Window|Context Window]] `glossary` — Number of positions an attention layer can take as input; quadratic memory cost scales here.
- [[Concepts/Inductive Bias|Inductive Bias]] `glossary` — Prior about what the data looks like; CNNs assume translation invariance, RNNs assume recency.
- [[Concepts/State-space model|State-space model]] `lesson term` — Recurrence parameterized for parallel training via structured state-space matrices.
- Quadratic bottleneck `lesson term` — Attention memory = O(N²) in sequence length; Flash Attention hides the constants, not the scaling.

## Ships

- [[Artifacts/07-01 sequence-architecture-picker|sequence-architecture-picker]] `skill` — Pick sequence architecture (RNN, transformer, SSM, hybrid) given length, throughput, and training budget.

## Further reading

- [[Resources/Bahdanau, Cho, Bengio (2014). Neural Machine Translation by Jointly Learning to Align and Translate|Bahdanau, Cho, Bengio (2014). Neural Machine Translation by Jointly Learning to Align and Translate]] ([link](https://arxiv.org/abs/1409.0473)) — where attention was born, bolted onto an RNN. ·  also cited by 2 other lessons
- [[Resources/Attention Is All You Need|Attention Is All You Need]] ([link](https://arxiv.org/abs/1706.03762)) — the paper that killed recurrence in mainstream NLP. ·  also cited by 8 other lessons
- [[Resources/Gu, Dao (2023). Mamba- Linear-Time Sequence Modeling with Selective State Spaces|Gu, Dao (2023). Mamba: Linear-Time Sequence Modeling with Selective State Spaces]] ([link](https://arxiv.org/abs/2312.00752)) — modern recurrent answer to transformers. ·  also cited by 1 other lesson
- [[Resources/Hochreiter, S. and Schmidhuber, J. (1997). Long Short-Term Memory|Hochreiter, S. and Schmidhuber, J. (1997). Long Short-Term Memory]] ([link](https://www.bioinf.jku.at/publications/older/2604.pdf)) — the original LSTM paper, for the record. ·  also cited by 1 other lesson


%% ── my notes ── %%
