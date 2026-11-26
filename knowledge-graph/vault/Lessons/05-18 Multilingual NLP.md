---
id: "lesson:05/18"
type: lesson
ref: 05/18
phase: 5
num: 18
title: Multilingual NLP
lesson_type: learn
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 8
code_files: 1
concepts: 7
prereqs: 2
community: 56
aliases:
  - 05/18
  - 05-18
tags:
  - phase/05
  - type/learn
  - community/56
  - stdlib-only
source: ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/18-multilingual-nlp/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/18-multilingual-nlp"
---

# 05/18 Multilingual NLP

> One model, 100+ languages, zero training data for most of them. Cross-lingual transfer is the practical miracle of the 2020s.

**Phase:** [[Phases/05 NLP, Foundations to Advanced|Phase 5: NLP, Foundations to Advanced]] · **Type:** Learn · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/05-nlp-foundations-to-advanced/18-multilingual-nlp/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/18-multilingual-nlp) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/18-multilingual-nlp) · code: main.py · quiz: 8 questions  
**Community:** [[Communities/56 NLLB · Constrained decoding · OOV|56 NLLB · Constrained decoding · OOV]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 5 · 04 (GloVe, FastText, Subword), Phase 5 · 11 (Machine Translation)`

- [[Lessons/05-04 GloVe, FastText, and Subword Embeddings|05/04 GloVe, FastText, and Subword Embeddings]] — GloVe, FastText, Subword
- [[Lessons/05-11 Machine Translation|05/11 Machine Translation]] — Machine Translation

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/05-03 Word Embeddings — Word2Vec from Scratch|05/03 Word Embeddings — Word2Vec from Scratch]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]]
- depth 3: [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/05-02 Bag of Words, TF-IDF, and Text Representation|05/02 Bag of Words, TF-IDF, and Text Representation]], [[Lessons/05-09 Sequence-to-Sequence Models|05/09 Sequence-to-Sequence Models]]

## Concepts taught

- Multilingual model `lesson term` — Shared vocabulary and parameters across languages.
- Cross-lingual transfer `lesson term` — Fine-tune on source, evaluate on target without target-language labels.
- [[Concepts/Zero-Shot|Zero-Shot]] `glossary` — Transfer without fine-tuning on the target language.
- [[Concepts/Few-Shot|Few-Shot]] `glossary` — 100-500 target-language examples used for fine-tuning.
- mBERT `lesson term` — 104-language BERT pretrained on Wikipedia.
- XLM-R `lesson term` — 100-language RoBERTa pretrained on CommonCrawl.
- [[Concepts/NLLB|NLLB]] `lesson term` — No Language Left Behind. Includes 55 low-resource languages.

## Ships

- [[Artifacts/05-18 multilingual-picker|multilingual-picker]] `skill` — Pick source language, target model, and evaluation plan for a multilingual NLP task.

## Further reading

- Pires, Schlinger, Garrette (2019). How Multilingual is Multilingual BERT? ([link](https://arxiv.org/abs/1906.01502)) — the analysis paper that started the cross-lingual transfer research line.
- Conneau et al. (2019). Unsupervised Cross-lingual Representation Learning at Scale ([link](https://arxiv.org/abs/1911.02116)) — the XLM-R paper.
- [[Resources/Costa-jussà et al. (2022). No Language Left Behind- Scaling Human-Centered Machine Translation|Costa-jussà et al. (2022). No Language Left Behind: Scaling Human-Centered Machine Translation]] ([link](https://arxiv.org/abs/2207.04672)) — NLLB-200 paper. ·  also cited by 1 other lesson
- Üstün et al. (2024). Aya Model: An Instruction Finetuned Open-Access Multilingual Language Model ([link](https://arxiv.org/abs/2402.07827)) — Aya, Cohere's multilingual LLM.
- Language Similarity Predicts Cross-Lingual Transfer Learning Performance (2026) ([link](https://www.mdpi.com/2504-4990/8/3/65)) — the qWALS / LANGRANK source-language paper.


%% ── my notes ── %%
