---
id: "lesson:05/04"
type: lesson
ref: 05/04
phase: 5
num: 4
title: "GloVe, FastText, and Subword Embeddings"
lesson_type: build
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 8
code_files: 1
concepts: 5
prereqs: 1
community: 56
aliases:
  - 05/04
  - 05-04
tags:
  - phase/05
  - type/build
  - community/56
  - stdlib-only
source: ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/04-glove-fasttext-subword/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/04-glove-fasttext-subword"
---

# 05/04 GloVe, FastText, and Subword Embeddings

> Word2Vec trained one embedding per word. GloVe factorized the co-occurrence matrix. FastText embedded the pieces. BPE bridged to transformers.

**Phase:** [[Phases/05 NLP, Foundations to Advanced|Phase 5: NLP, Foundations to Advanced]] · **Type:** Build · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/05-nlp-foundations-to-advanced/04-glove-fasttext-subword/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/04-glove-fasttext-subword) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/04-glove-fasttext-subword) · code: main.py · quiz: 8 questions  
**Community:** [[Communities/56 NLLB · Constrained decoding · OOV|56 NLLB · Constrained decoding · OOV]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 5 · 03 (Word2Vec from Scratch)`

- [[Lessons/05-03 Word Embeddings — Word2Vec from Scratch|05/03 Word Embeddings — Word2Vec from Scratch]] — Word2Vec from Scratch

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/05-02 Bag of Words, TF-IDF, and Text Representation|05/02 Bag of Words, TF-IDF, and Text Representation]]
- depth 3: [[Lessons/02-02 Linear Regression|02/02 Linear Regression]], [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]], [[Lessons/05-01 Text Processing — Tokenization, Stemming, Lemmatization|05/01 Text Processing — Tokenization, Stemming, Lemmatization]]

## Builds on this

- [[Lessons/05-11 Machine Translation|05/11 Machine Translation]]
- [[Lessons/05-14 Information Retrieval and Search|05/14 Information Retrieval and Search]]
- [[Lessons/05-18 Multilingual NLP|05/18 Multilingual NLP]]
- [[Lessons/05-19 Subword Tokenization — BPE, WordPiece, Unigram, SentencePiece|05/19 Subword Tokenization — BPE, WordPiece, Unigram, SentencePiece]]

## Concepts taught

- Co-occurrence matrix `lesson term` — X[i][j] = how often word j appears in a window around word i.
- Subword `lesson term` — A character n-gram (FastText) or learned token (BPE/WordPiece/SentencePiece).
- [[Concepts/Byte Pair Encoding (BPE)|Byte Pair Encoding (BPE)]] (as *BPE*) `glossary` — Iterative merging of most-frequent adjacent pairs until vocabulary hits target size.
- [[Concepts/OOV|OOV]] `lesson term` — Word the model has never seen. Word2Vec/GloVe fail. FastText and BPE handle it.
- [[Concepts/Byte-level BPE|Byte-level BPE]] `lesson term` — GPT-2's scheme. Vocabulary starts with 256 bytes, so nothing is ever OOV.

## Ships

- [[Artifacts/05-04 skill-embeddings-picker|skill-embeddings-picker]] `skill` — Pick a tokenization approach for a new language model or text pipeline.

## Further reading

- [[Resources/Neural Machine Translation of Rare Words with Subword Units|Neural Machine Translation of Rare Words with Subword Units]] ([link](https://arxiv.org/abs/1508.07909)) — the paper that introduced BPE to modern NLP. ·  also cited by 2 other lessons
- Bojanowski et al. (2017). Enriching Word Vectors with Subword Information ([link](https://arxiv.org/abs/1607.04606)) — FastText.
- [[Resources/Hugging Face tokenizer summary|Hugging Face tokenizer summary]] ([link](https://huggingface.co/docs/transformers/tokenizer_summary)) — how BPE, WordPiece, and SentencePiece actually differ in practice. ·  also cited by 1 other lesson
- Pennington, Socher, Manning (2014). GloVe: Global Vectors for Word Representation ([link](https://nlp.stanford.edu/pubs/glove.pdf)) — the GloVe paper, seven pages, still the best derivation of the loss.


%% ── my notes ── %%
