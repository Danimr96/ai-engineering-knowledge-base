---
id: "lesson:05/20"
type: lesson
ref: 05/20
phase: 5
num: 20
title: "Structured Outputs & Constrained Decoding"
lesson_type: build
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 8
code_files: 1
concepts: 7
prereqs: 2
community: 74
aliases:
  - 05/20
  - 05-20
tags:
  - phase/05
  - type/build
  - community/74
  - stdlib-only
source: ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/20-structured-outputs-constrained-decoding/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/20-structured-outputs-constrained-decoding"
---

# 05/20 Structured Outputs & Constrained Decoding

> Ask an LLM for JSON. Get JSON most of the time. In production, "most" is the problem. Constrained decoding turns "most" into "always" by editing the logits before sampling.

**Phase:** [[Phases/05 NLP, Foundations to Advanced|Phase 5: NLP, Foundations to Advanced]] · **Type:** Build · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/05-nlp-foundations-to-advanced/20-structured-outputs-constrained-decoding/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/20-structured-outputs-constrained-decoding) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/20-structured-outputs-constrained-decoding) · code: main.py · quiz: 8 questions  
**Community:** [[Communities/74 Slot · JSON mode|74 Slot · JSON mode]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 5 · 17 (Chatbots), Phase 5 · 19 (Subword Tokenization)`

- [[Lessons/05-17 Chatbots — Rule-Based to Neural to LLM Agents|05/17 Chatbots — Rule-Based to Neural to LLM Agents]] — Chatbots
- [[Lessons/05-19 Subword Tokenization — BPE, WordPiece, Unigram, SentencePiece|05/19 Subword Tokenization — BPE, WordPiece, Unigram, SentencePiece]] — Subword Tokenization

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/05-01 Text Processing — Tokenization, Stemming, Lemmatization|05/01 Text Processing — Tokenization, Stemming, Lemmatization]], [[Lessons/05-04 GloVe, FastText, and Subword Embeddings|05/04 GloVe, FastText, and Subword Embeddings]], [[Lessons/05-13 Question Answering Systems|05/13 Question Answering Systems]], [[Lessons/05-14 Information Retrieval and Search|05/14 Information Retrieval and Search]]
- depth 3: [[Lessons/02-14 Naive Bayes|02/14 Naive Bayes]], [[Lessons/05-02 Bag of Words, TF-IDF, and Text Representation|05/02 Bag of Words, TF-IDF, and Text Representation]], [[Lessons/05-03 Word Embeddings — Word2Vec from Scratch|05/03 Word Embeddings — Word2Vec from Scratch]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]], [[Lessons/05-11 Machine Translation|05/11 Machine Translation]]

## Builds on this

- [[Lessons/05-29 Dialogue State Tracking|05/29 Dialogue State Tracking]]

## Concepts taught

- [[Concepts/Constrained decoding|Constrained decoding]] `lesson term` — Mask invalid-token logits at every generation step.
- Logit processor `lesson term` — Function: (logits, state) -> masked_logits.
- FSM `lesson term` — Compiled grammar representation; O(1) valid-next-token lookup.
- [[Concepts/CFG|CFG]] `lesson term` — Grammar that handles recursion; slower but more expressive than FSM.
- Schema field order `lesson term` — Yes — first field commits; always put reasoning before answer.
- Guided decoding `lesson term` — Same concept, integrated into the inference server.
- [[Concepts/JSON mode|JSON mode]] `lesson term` — Guarantees JSON syntax; does NOT guarantee schema match.

## Ships

- [[Artifacts/05-20 structured-output-picker|structured-output-picker]] `skill` — Choose a structured output approach, schema design, and validation plan.

## Further reading

- [[Resources/Willard, Louf (2023). Efficient Guided Generation for LLMs|Willard, Louf (2023). Efficient Guided Generation for LLMs]] ([link](https://arxiv.org/abs/2307.09702)) — the Outlines paper. ·  also cited by 1 other lesson
- [[Resources/XGrammar paper (2024)|XGrammar paper (2024)]] ([link](https://arxiv.org/abs/2411.15100)) — fast CFG-based constrained decoding. ·  also cited by 1 other lesson
- JSONSchemaBench (2025) ([link](https://arxiv.org/abs/2501.10868)) — benchmarking 6 constrained decoding frameworks.
- vLLM — Structured Outputs ([link](https://docs.vllm.ai/en/latest/features/structured_outputs.html)) — inference server integration.
- [[Resources/OpenAI — Structured Outputs guide|OpenAI — Structured Outputs guide]] ([link](https://platform.openai.com/docs/guides/structured-outputs)) — API reference + gotchas. ·  also cited by 3 other lessons
- [[Resources/Instructor library|Instructor library]] ([link](https://python.useinstructor.com/)) — Pydantic + retries across providers. ·  also cited by 1 other lesson


%% ── my notes ── %%
