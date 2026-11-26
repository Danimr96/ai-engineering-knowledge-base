---
id: "lesson:05/11"
type: lesson
ref: 05/11
phase: 5
num: 11
title: Machine Translation
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 8
code_files: 1
concepts: 6
prereqs: 2
community: 56
aliases:
  - 05/11
  - 05-11
tags:
  - phase/05
  - type/build
  - community/56
  - stdlib-only
source: ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/11-machine-translation/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/11-machine-translation"
---

# 05/11 Machine Translation

> Translation is the task that paid for NLP research for thirty years and keeps paying now.

**Phase:** [[Phases/05 NLP, Foundations to Advanced|Phase 5: NLP, Foundations to Advanced]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/05-nlp-foundations-to-advanced/11-machine-translation/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/11-machine-translation) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/11-machine-translation) · code: main.py · quiz: 8 questions  
**Community:** [[Communities/56 NLLB · Constrained decoding · OOV|56 NLLB · Constrained decoding · OOV]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 5 · 10 (Attention Mechanism), Phase 5 · 04 (GloVe, FastText, Subword)`

- [[Lessons/05-04 GloVe, FastText, and Subword Embeddings|05/04 GloVe, FastText, and Subword Embeddings]] — GloVe, FastText, Subword
- [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]] — Attention Mechanism

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/05-03 Word Embeddings — Word2Vec from Scratch|05/03 Word Embeddings — Word2Vec from Scratch]], [[Lessons/05-09 Sequence-to-Sequence Models|05/09 Sequence-to-Sequence Models]]
- depth 3: [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]], [[Lessons/05-02 Bag of Words, TF-IDF, and Text Representation|05/02 Bag of Words, TF-IDF, and Text Representation]], [[Lessons/05-08 CNNs and RNNs for Text|05/08 CNNs and RNNs for Text]]

## Builds on this

- [[Lessons/05-12 Text Summarization|05/12 Text Summarization]]
- [[Lessons/05-13 Question Answering Systems|05/13 Question Answering Systems]]
- [[Lessons/05-18 Multilingual NLP|05/18 Multilingual NLP]]

## Concepts taught

- BLEU `lesson term` — N-gram precision with brevity penalty. [0, 100].
- chrF `lesson term` — Character-level F-score. More sensitive for morphologically rich languages.
- NMT `lesson term` — Transformer encoder-decoder trained on parallel text. The 2017+ default.
- [[Concepts/NLLB|NLLB]] `lesson term` — Meta's 200-language MT model family.
- [[Concepts/Constrained decoding|Constrained decoding]] `lesson term` — Force specific tokens or n-grams to appear / not appear in the output.
- [[Concepts/Hallucination|Hallucination]] `glossary` — Model output that is not supported by the source.

## Ships

- [[Artifacts/05-11 mt-evaluator|mt-evaluator]] `skill` — Evaluate a machine translation output for shipping.

## Further reading

- Popović (2015). chrF: character n-gram F-score for automatic MT evaluation ([link](https://aclanthology.org/W15-3049/)) — the chrF paper.
- Post (2018). A Call for Clarity in Reporting BLEU Scores ([link](https://aclanthology.org/W18-6319/)) — why `sacrebleu` is the only correct way to report BLEU.
- [[Resources/Costa-jussà et al. (2022). No Language Left Behind- Scaling Human-Centered Machine Translation|Costa-jussà et al. (2022). No Language Left Behind: Scaling Human-Centered Machine Translation]] ([link](https://arxiv.org/abs/2207.04672)) — the NLLB paper. ·  also cited by 1 other lesson
- Hugging Face MT guide ([link](https://huggingface.co/docs/transformers/tasks/translation)) — practical fine-tuning walkthrough.


%% ── my notes ── %%
