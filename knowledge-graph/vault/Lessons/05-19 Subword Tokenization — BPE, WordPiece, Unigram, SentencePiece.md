---
id: "lesson:05/19"
type: lesson
ref: 05/19
phase: 5
num: 19
title: "Subword Tokenization — BPE, WordPiece, Unigram, SentencePiece"
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 8
code_files: 2
concepts: 7
prereqs: 2
community: 1
aliases:
  - 05/19
  - 05-19
tags:
  - phase/05
  - type/learn
  - community/01
  - stdlib-only
source: ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/19-subword-tokenization/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/19-subword-tokenization"
---

# 05/19 Subword Tokenization — BPE, WordPiece, Unigram, SentencePiece

> Word tokenizers choke on unseen words. Character tokenizers blow up sequence length. Subword tokenizers split the difference. Every modern LLM ships on one.

**Phase:** [[Phases/05 NLP, Foundations to Advanced|Phase 5: NLP, Foundations to Advanced]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/05-nlp-foundations-to-advanced/19-subword-tokenization/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/19-subword-tokenization) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/19-subword-tokenization) · code: main.py, main.ts · quiz: 8 questions  
**Community:** [[Communities/01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism|01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 5 · 01 (Text Processing), Phase 5 · 04 (GloVe / FastText / Subword)`

- [[Lessons/05-01 Text Processing — Tokenization, Stemming, Lemmatization|05/01 Text Processing — Tokenization, Stemming, Lemmatization]] — Text Processing
- [[Lessons/05-04 GloVe, FastText, and Subword Embeddings|05/04 GloVe, FastText, and Subword Embeddings]] — GloVe / FastText / Subword

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/02-14 Naive Bayes|02/14 Naive Bayes]], [[Lessons/05-03 Word Embeddings — Word2Vec from Scratch|05/03 Word Embeddings — Word2Vec from Scratch]]
- depth 3: [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]], [[Lessons/02-02 Linear Regression|02/02 Linear Regression]], [[Lessons/02-03 Logistic Regression|02/03 Logistic Regression]], [[Lessons/02-04 Decision Trees and Random Forests|02/04 Decision Trees and Random Forests]], [[Lessons/02-05 Support Vector Machines|02/05 Support Vector Machines]], [[Lessons/02-06 K-Nearest Neighbors and Distances|02/06 K-Nearest Neighbors and Distances]], [[Lessons/02-07 Unsupervised Learning|02/07 Unsupervised Learning]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/05-02 Bag of Words, TF-IDF, and Text Representation|05/02 Bag of Words, TF-IDF, and Text Representation]]

## Builds on this

- [[Lessons/05-20 Structured Outputs & Constrained Decoding|05/20 Structured Outputs & Constrained Decoding]]
- [[Lessons/06-13 Neural Audio Codecs — EnCodec, SNAC, Mimi, DAC and the Semantic-Acoustic Split|06/13 Neural Audio Codecs — EnCodec, SNAC, Mimi, DAC and the Semantic-Acoustic Split]]

## Concepts taught

- [[Concepts/Byte Pair Encoding (BPE)|Byte Pair Encoding (BPE)]] (as *BPE*) `glossary` — Greedy merge of most-frequent character pairs until target vocab size hit.
- [[Concepts/Byte-level BPE|Byte-level BPE]] `lesson term` — BPE over raw 256 bytes; GPT-2 / Llama use this.
- Unigram `lesson term` — Prunes from a large candidate set using log-likelihood; used by T5, Gemma.
- [[Concepts/SentencePiece|SentencePiece]] `lesson term` — Library that trains BPE/Unigram on raw text; space encoded as ▁.
- [[Concepts/tiktoken|tiktoken]] `lesson term` — OpenAI's Rust-backed BPE encoder for pre-built vocabs. No training.
- Merge list `lesson term` — Ordered list of (a, b) → ab merges; inference applies in order.
- Character coverage `lesson term` — Fraction of characters in training corpus the tokenizer must cover; ~0.9995 typical.

## Ships

- [[Artifacts/05-19 skill-bpe-vs-wordpiece|skill-bpe-vs-wordpiece]] `skill` — Pick tokenizer algorithm, vocab size, library for a given corpus and deployment target.

## Further reading

- [[Resources/Neural Machine Translation of Rare Words with Subword Units|Neural Machine Translation of Rare Words with Subword Units]] ([link](https://arxiv.org/abs/1508.07909)) — the BPE paper. ·  also cited by 2 other lessons
- Kudo (2018). Subword Regularization with Unigram Language Model ([link](https://arxiv.org/abs/1804.10959)) — the Unigram paper.
- [[Resources/Kudo, Richardson (2018). SentencePiece- A simple and language independent subword tokenizer|Kudo, Richardson (2018). SentencePiece: A simple and language independent subword tokenizer]] ([link](https://arxiv.org/abs/1808.06226)) — the library. ·  also cited by 2 other lessons
- [[Resources/OpenAI tiktoken repo|OpenAI tiktoken repo]] ([link](https://github.com/openai/tiktoken)) — cookbook + encoding list. ·  also cited by 2 other lessons
- [[Resources/Hugging Face tokenizer summary|Hugging Face tokenizer summary]] ([link](https://huggingface.co/docs/transformers/tokenizer_summary)) — concise reference. ·  also cited by 1 other lesson


%% ── my notes ── %%
