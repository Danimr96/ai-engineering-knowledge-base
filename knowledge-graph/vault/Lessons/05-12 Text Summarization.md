---
id: "lesson:05/12"
type: lesson
ref: 05/12
phase: 5
num: 12
title: Text Summarization
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 8
code_files: 1
concepts: 6
prereqs: 2
community: 63
aliases:
  - 05/12
  - 05-12
tags:
  - phase/05
  - type/build
  - community/63
  - stdlib-only
source: ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/12-text-summarization/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/12-text-summarization"
---

# 05/12 Text Summarization

> Extractive systems tell you what the document said. Abstractive systems tell you what the author meant. Different tasks, different pitfalls.

**Phase:** [[Phases/05 NLP, Foundations to Advanced|Phase 5: NLP, Foundations to Advanced]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/05-nlp-foundations-to-advanced/12-text-summarization/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/12-text-summarization) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/12-text-summarization) · code: main.py · quiz: 8 questions  
**Community:** [[Communities/63 Topic · UMAP|63 Topic · UMAP]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 5 · 02 (BoW + TF-IDF), Phase 5 · 11 (Machine Translation)`

- [[Lessons/05-02 Bag of Words, TF-IDF, and Text Representation|05/02 Bag of Words, TF-IDF, and Text Representation]] — BoW + TF-IDF
- [[Lessons/05-11 Machine Translation|05/11 Machine Translation]] — Machine Translation

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/02-02 Linear Regression|02/02 Linear Regression]], [[Lessons/05-01 Text Processing — Tokenization, Stemming, Lemmatization|05/01 Text Processing — Tokenization, Stemming, Lemmatization]], [[Lessons/05-04 GloVe, FastText, and Subword Embeddings|05/04 GloVe, FastText, and Subword Embeddings]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]]
- depth 3: [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]], [[Lessons/02-14 Naive Bayes|02/14 Naive Bayes]], [[Lessons/05-03 Word Embeddings — Word2Vec from Scratch|05/03 Word Embeddings — Word2Vec from Scratch]], [[Lessons/05-09 Sequence-to-Sequence Models|05/09 Sequence-to-Sequence Models]]

## Concepts taught

- Extractive `lesson term` — Return sentences verbatim from the source. Never hallucinates.
- Abstractive `lesson term` — Generate new text conditioned on source. Can hallucinate.
- [[Concepts/ROUGE|ROUGE]] `glossary` — N-gram / LCS overlap between system output and reference.
- TextRank `lesson term` — PageRank over sentence similarity graph.
- Factuality `lesson term` — Whether summary claims are supported by the source.
- [[Concepts/Hallucination|Hallucination]] `glossary` — Content in the summary that the source does not support.

## Ships

- [[Artifacts/05-12 summary-picker|summary-picker]] `skill` — Pick extractive or abstractive, name the library, add a factuality check.

## Further reading

- Lin (2004). ROUGE: A Package for Automatic Evaluation of Summaries ([link](https://aclanthology.org/W04-1013/)) — ROUGE paper.
- Mihalcea and Tarau (2004). TextRank: Bringing Order into Texts ([link](https://aclanthology.org/W04-3252/)) — the extractive canonical paper.
- [[Resources/Lewis et al. (2019). BART- Denoising Sequence-to-Sequence Pre-training|Lewis et al. (2019). BART: Denoising Sequence-to-Sequence Pre-training]] ([link](https://arxiv.org/abs/1910.13461)) — the BART paper. ·  also cited by 1 other lesson
- Zhang et al. (2019). PEGASUS: Pre-training with Extracted Gap-sentences ([link](https://arxiv.org/abs/1912.08777)) — Pegasus and the gap-sentence objective.
- Maynez et al. (2020). On Faithfulness and Factuality in Abstractive Summarization ([link](https://arxiv.org/abs/2005.00661)) — the factuality landscape paper.


%% ── my notes ── %%
