---
id: "lesson:05/29"
type: lesson
ref: 05/29
phase: 5
num: 29
title: Dialogue State Tracking
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 8
code_files: 1
concepts: 7
prereqs: 2
community: 74
aliases:
  - 05/29
  - 05-29
tags:
  - phase/05
  - type/build
  - community/74
  - stdlib-only
source: ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/29-dialogue-state-tracking/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/29-dialogue-state-tracking"
---

# 05/29 Dialogue State Tracking

> "I want a cheap restaurant in the north... actually make it moderate... and add Italian." Three turns, three state updates. DST keeps the slot-value dict in sync so the booking works.

**Phase:** [[Phases/05 NLP, Foundations to Advanced|Phase 5: NLP, Foundations to Advanced]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/05-nlp-foundations-to-advanced/29-dialogue-state-tracking/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/29-dialogue-state-tracking) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/29-dialogue-state-tracking) · code: main.py · quiz: 8 questions  
**Community:** [[Communities/74 Slot · JSON mode|74 Slot · JSON mode]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 5 · 17 (Chatbots), Phase 5 · 20 (Structured Outputs)`

- [[Lessons/05-17 Chatbots — Rule-Based to Neural to LLM Agents|05/17 Chatbots — Rule-Based to Neural to LLM Agents]] — Chatbots
- [[Lessons/05-20 Structured Outputs & Constrained Decoding|05/20 Structured Outputs & Constrained Decoding]] — Structured Outputs

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/05-13 Question Answering Systems|05/13 Question Answering Systems]], [[Lessons/05-14 Information Retrieval and Search|05/14 Information Retrieval and Search]], [[Lessons/05-19 Subword Tokenization — BPE, WordPiece, Unigram, SentencePiece|05/19 Subword Tokenization — BPE, WordPiece, Unigram, SentencePiece]]
- depth 3: [[Lessons/05-01 Text Processing — Tokenization, Stemming, Lemmatization|05/01 Text Processing — Tokenization, Stemming, Lemmatization]], [[Lessons/05-02 Bag of Words, TF-IDF, and Text Representation|05/02 Bag of Words, TF-IDF, and Text Representation]], [[Lessons/05-04 GloVe, FastText, and Subword Embeddings|05/04 GloVe, FastText, and Subword Embeddings]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]], [[Lessons/05-11 Machine Translation|05/11 Machine Translation]]

## Concepts taught

- DST `lesson term` — Maintain the slot-value dict across dialogue turns.
- [[Concepts/Slot|Slot]] `lesson term` — Named parameter the backend needs (cuisine, date).
- Domain `lesson term` — Restaurant, hotel, taxi — sets of slots.
- JGA `lesson term` — Fraction of turns where every slot is correct. All-or-nothing.
- MultiWOZ `lesson term` — Multi-domain WOZ dataset; standard DST evaluation.
- Ontology-free DST `lesson term` — Generate slot names and values directly, no fixed list.
- Correction `lesson term` — Turn that overwrites a previously-filled slot.

## Ships

- [[Artifacts/05-29 dst-designer|dst-designer]] `skill` — Design a dialogue state tracker — schema, extractor, update policy, evaluation.

## Further reading

- Budzianowski et al. (2018). MultiWOZ — A Large-Scale Multi-Domain Wizard-of-Oz ([link](https://arxiv.org/abs/1810.00278)) — the canonical benchmark.
- Heck et al. (2020). TripPy — A Triple Copy Strategy for Value Independent Neural Dialog State Tracking ([link](https://arxiv.org/abs/2005.02877)) — the copy-based DST workhorse.
- Feng et al. (2023). Towards LLM-driven Dialogue State Tracking (LDST) ([link](https://arxiv.org/abs/2310.14970)) — LLaMA + LoRA instruction tuning for DST.
- King, Flanigan (2024). Unsupervised End-to-End Task-Oriented Dialogue with LLMs ([link](https://arxiv.org/abs/2404.10753)) — EM-based unsupervised TOD.
- MultiWOZ leaderboard ([link](https://github.com/budzianowski/multiwoz)) — canonical DST results.


%% ── my notes ── %%
