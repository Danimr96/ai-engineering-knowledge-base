---
id: "lesson:05/27"
type: lesson
ref: 05/27
phase: 5
num: 27
title: "LLM Evaluation — RAGAS, DeepEval, G-Eval"
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 8
code_files: 1
concepts: 7
prereqs: 2
community: 26
aliases:
  - 05/27
  - 05-27
tags:
  - phase/05
  - type/build
  - community/26
  - stdlib-only
source: ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/27-llm-evaluation-frameworks/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/27-llm-evaluation-frameworks"
---

# 05/27 LLM Evaluation — RAGAS, DeepEval, G-Eval

> Exact-match and F1 miss semantic equivalence. Human review does not scale. LLM-as-judge is the production answer — with enough calibration to trust the number.

**Phase:** [[Phases/05 NLP, Foundations to Advanced|Phase 5: NLP, Foundations to Advanced]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/05-nlp-foundations-to-advanced/27-llm-evaluation-frameworks/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/27-llm-evaluation-frameworks) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/27-llm-evaluation-frameworks) · code: main.py · quiz: 8 questions  
**Community:** [[Communities/26 BM25 · Reciprocal Rank Fusion (RRF) · Bi-encoder|26 BM25 · Reciprocal Rank Fusion (RRF) · Bi-encoder]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 5 · 13 (Question Answering), Phase 5 · 14 (Information Retrieval)`

- [[Lessons/05-13 Question Answering Systems|05/13 Question Answering Systems]] — Question Answering
- [[Lessons/05-14 Information Retrieval and Search|05/14 Information Retrieval and Search]] — Information Retrieval

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/05-02 Bag of Words, TF-IDF, and Text Representation|05/02 Bag of Words, TF-IDF, and Text Representation]], [[Lessons/05-04 GloVe, FastText, and Subword Embeddings|05/04 GloVe, FastText, and Subword Embeddings]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]], [[Lessons/05-11 Machine Translation|05/11 Machine Translation]]
- depth 3: [[Lessons/02-02 Linear Regression|02/02 Linear Regression]], [[Lessons/05-01 Text Processing — Tokenization, Stemming, Lemmatization|05/01 Text Processing — Tokenization, Stemming, Lemmatization]], [[Lessons/05-03 Word Embeddings — Word2Vec from Scratch|05/03 Word Embeddings — Word2Vec from Scratch]], [[Lessons/05-09 Sequence-to-Sequence Models|05/09 Sequence-to-Sequence Models]]

## Concepts taught

- [[Concepts/LLM-as-a-Judge|LLM-as-a-Judge]] (as *LLM-as-judge*) `glossary` — Prompt a judge model to score outputs 0-1 given a rubric.
- [[Concepts/RAGAS|RAGAS]] `lesson term` — Open-source eval framework with 4 reference-free RAG metrics.
- [[Concepts/Faithfulness|Faithfulness]] `lesson term` — Fraction of answer claims entailed by retrieved context.
- Context precision `lesson term` — Fraction of top-K chunks that actually mattered.
- Context recall `lesson term` — Fraction of gold-answer claims supported by retrieved chunks.
- G-Eval `lesson term` — Rubric + chain-of-thought eval steps + 0-1 score.
- [[Concepts/Calibration|Calibration]] `glossary` — Spearman correlation between judge score and human score.

## Ships

- [[Artifacts/05-27 eval-architect|eval-architect]] `skill` — Design an LLM evaluation plan with calibrated judge and CI gates.

## Further reading

- [[Resources/Liu et al. (2023). G-Eval- NLG Evaluation using GPT-4 with Better Human Alignment|Liu et al. (2023). G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment]] ([link](https://arxiv.org/abs/2303.16634)) — the G-Eval paper. ·  also cited by 1 other lesson
- [[Resources/Zheng et al. (2023). Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena|Zheng et al. (2023). Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena]] ([link](https://arxiv.org/abs/2306.05685)) — biases, calibration, limits. ·  also cited by 2 other lessons
- [[Resources/Es et al. (2023). RAGAS- Automated Evaluation of Retrieval Augmented Generation|Es et al. (2023). RAGAS: Automated Evaluation of Retrieval Augmented Generation]] ([link](https://arxiv.org/abs/2309.15217)) — the RAGAS paper. ·  also cited by 1 other lesson
- DeepEval docs ([link](https://deepeval.com/docs/metrics-introduction)) — open production stack.
- MLflow GenAI Scorer ([link](https://mlflow.org/blog/third-party-scorers)) — unifying framework that integrates RAGAS, DeepEval, Phoenix.


%% ── my notes ── %%
