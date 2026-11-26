---
id: "lesson:05/10"
type: lesson
ref: 05/10
phase: 5
num: 10
title: "Attention Mechanism — The Breakthrough"
lesson_type: build
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 8
code_files: 1
concepts: 5
prereqs: 1
community: 12
aliases:
  - 05/10
  - 05-10
tags:
  - phase/05
  - type/build
  - community/12
  - stdlib-only
source: ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/10-attention-mechanism/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/10-attention-mechanism"
---

# 05/10 Attention Mechanism — The Breakthrough

> The decoder stops squinting at a compressed summary and starts looking at the whole source. Everything after this is attention plus engineering.

**Phase:** [[Phases/05 NLP, Foundations to Advanced|Phase 5: NLP, Foundations to Advanced]] · **Type:** Build · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/05-nlp-foundations-to-advanced/10-attention-mechanism/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/10-attention-mechanism) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/10-attention-mechanism) · code: main.py · quiz: 8 questions  
**Community:** [[Communities/12 Attention · Cross-Attention · Self-Attention|12 Attention · Cross-Attention · Self-Attention]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 5 · 09 (Sequence-to-Sequence Models)`

- [[Lessons/05-09 Sequence-to-Sequence Models|05/09 Sequence-to-Sequence Models]] — Sequence-to-Sequence Models

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]], [[Lessons/05-08 CNNs and RNNs for Text|05/08 CNNs and RNNs for Text]]
- depth 3: [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]], [[Lessons/04-02 Convolutions from Scratch|04/02 Convolutions from Scratch]], [[Lessons/05-03 Word Embeddings — Word2Vec from Scratch|05/03 Word Embeddings — Word2Vec from Scratch]]

## Builds on this

- [[Lessons/05-11 Machine Translation|05/11 Machine Translation]]
- [[Lessons/05-13 Question Answering Systems|05/13 Question Answering Systems]]
- [[Lessons/06-04 Speech Recognition (ASR) — CTC, RNN-T, Attention|06/04 Speech Recognition (ASR) — CTC, RNN-T, Attention]]
- [[Lessons/06-05 Whisper — Architecture & Fine-Tuning|06/05 Whisper — Architecture & Fine-Tuning]]
- [[Lessons/07-01 Why Transformers — The Problems with RNNs|07/01 Why Transformers — The Problems with RNNs]]
- [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]]

## Concepts taught

- [[Concepts/Attention|Attention]] `glossary` — Weighted average of a value sequence, weights computed from a query-key similarity.
- Query, Key, Value `lesson term` — Three projections: Q asks, K is what to match, V is what to return.
- Additive attention `lesson term` — Feed-forward score: v^T tanh(W q + U k).
- Multiplicative attention `lesson term` — Score is q^T k or q^T W k. Cheaper, same accuracy on most tasks.
- Alignment matrix `lesson term` — Attention weights as a (T_dec, T_enc) grid. Read it to see what the model attended to.

## Ships

- [[Artifacts/05-10 attention-shapes|attention-shapes]] `prompt` — Debug shape bugs in attention implementations.

## Further reading

- [[Resources/Bahdanau, Cho, Bengio (2014). Neural Machine Translation by Jointly Learning to Align and Translate|Bahdanau, Cho, Bengio (2014). Neural Machine Translation by Jointly Learning to Align and Translate]] ([link](https://arxiv.org/abs/1409.0473)) — the paper. ·  also cited by 2 other lessons
- Luong, Pham, Manning (2015). Effective Approaches to Attention-based Neural Machine Translation ([link](https://arxiv.org/abs/1508.04025)) — the three score variants and their comparison.
- Jain and Wallace (2019). Attention is not Explanation ([link](https://arxiv.org/abs/1902.10186)) — the interpretability caveat.
- Dive into Deep Learning — Bahdanau Attention ([link](https://d2l.ai/chapter_attention-mechanisms-and-transformers/bahdanau-attention.html)) — runnable walkthrough with PyTorch.


%% ── my notes ── %%
