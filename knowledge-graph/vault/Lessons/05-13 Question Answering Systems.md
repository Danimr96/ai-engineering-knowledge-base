---
id: "lesson:05/13"
type: lesson
ref: 05/13
phase: 5
num: 13
title: Question Answering Systems
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 8
code_files: 1
concepts: 6
prereqs: 2
aliases:
  - 05/13
  - 05-13
tags:
  - phase/05
  - type/build
  - stdlib-only
source: ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/13-question-answering/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/13-question-answering"
---

# 05/13 Question Answering Systems

> Three systems shaped modern QA. Extractive found spans. Retrieval-augmented grounded them in documents. Generative produced answers. Every modern AI assistant is a mix of the three.

**Phase:** [[Phases/05 NLP, Foundations to Advanced|Phase 5: NLP, Foundations to Advanced]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/05-nlp-foundations-to-advanced/13-question-answering/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/13-question-answering) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/13-question-answering) · code: main.py · quiz: 8 questions  
**Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 5 · 11 (Machine Translation), Phase 5 · 10 (Attention Mechanism)`

- [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]] — Attention Mechanism
- [[Lessons/05-11 Machine Translation|05/11 Machine Translation]] — Machine Translation

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/05-04 GloVe, FastText, and Subword Embeddings|05/04 GloVe, FastText, and Subword Embeddings]], [[Lessons/05-09 Sequence-to-Sequence Models|05/09 Sequence-to-Sequence Models]]
- depth 3: [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]], [[Lessons/05-03 Word Embeddings — Word2Vec from Scratch|05/03 Word Embeddings — Word2Vec from Scratch]], [[Lessons/05-08 CNNs and RNNs for Text|05/08 CNNs and RNNs for Text]]

## Builds on this

- [[Lessons/05-17 Chatbots — Rule-Based to Neural to LLM Agents|05/17 Chatbots — Rule-Based to Neural to LLM Agents]]
- [[Lessons/05-21 Natural Language Inference — Textual Entailment|05/21 Natural Language Inference — Textual Entailment]]
- [[Lessons/05-27 LLM Evaluation — RAGAS, DeepEval, G-Eval|05/27 LLM Evaluation — RAGAS, DeepEval, G-Eval]]
- [[Lessons/05-28 Long-Context Evaluation — NIAH, RULER, LongBench, MRCR|05/28 Long-Context Evaluation — NIAH, RULER, LongBench, MRCR]]

## Concepts taught

- Extractive QA `lesson term` — Predict start and end indices of the answer within a given passage.
- Open-domain QA `lesson term` — No given passage; must retrieve then answer.
- [[Concepts/RAG (Retrieval-Augmented Generation)|RAG (Retrieval-Augmented Generation)]] (as *RAG*) `glossary` — Retrieval-augmented generation. Retriever + reader pipeline.
- SQuAD `lesson term` — Stanford Question Answering Dataset. EM + F1 metrics.
- [[Concepts/Hallucination|Hallucination]] `glossary` — Reader output not supported by retrieved context.
- Refusal calibration `lesson term` — System correctly says "I don't know" when unable to answer.

## Ships

- [[Artifacts/05-13 qa-architect|qa-architect]] `skill` — Choose QA architecture, retrieval strategy, and evaluation plan.

## Further reading

- Rajpurkar et al. (2016). SQuAD: 100,000+ Questions for Machine Comprehension of Text ([link](https://arxiv.org/abs/1606.05250)) — the benchmark paper.
- [[Resources/Karpukhin et al. (2020). Dense Passage Retrieval for Open-Domain QA|Karpukhin et al. (2020). Dense Passage Retrieval for Open-Domain QA]] ([link](https://arxiv.org/abs/2004.04906)) — DPR, the canonical dense retriever for QA. ·  also cited by 2 other lessons
- Retrieval-Augmented Generation paper ([link](https://arxiv.org/abs/2005.11401)) — the paper that named RAG.
- Gao et al. (2023). Retrieval-Augmented Generation for Large Language Models: A Survey ([link](https://arxiv.org/abs/2312.10997)) — comprehensive RAG survey.


%% ── my notes ── %%
