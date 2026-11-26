---
id: "lesson:05/06"
type: lesson
ref: 05/06
phase: 5
num: 6
title: Named Entity Recognition
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 8
code_files: 1
concepts: 6
prereqs: 2
community: 76
aliases:
  - 05/06
  - 05-06
tags:
  - phase/05
  - type/build
  - community/76
  - stdlib-only
source: ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/06-named-entity-recognition/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/06-named-entity-recognition"
---

# 05/06 Named Entity Recognition

> Pull the names out. Sounds easy until you deal with ambiguous boundaries, nested entities, and domain jargon.

**Phase:** [[Phases/05 NLP, Foundations to Advanced|Phase 5: NLP, Foundations to Advanced]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/05-nlp-foundations-to-advanced/06-named-entity-recognition/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/06-named-entity-recognition) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/06-named-entity-recognition) · code: main.py · quiz: 8 questions  
**Community:** [[Communities/76 Provenance|76 Provenance]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 5 · 02 (BoW + TF-IDF), Phase 5 · 03 (Word Embeddings)`

- [[Lessons/05-02 Bag of Words, TF-IDF, and Text Representation|05/02 Bag of Words, TF-IDF, and Text Representation]] — BoW + TF-IDF
- [[Lessons/05-03 Word Embeddings — Word2Vec from Scratch|05/03 Word Embeddings — Word2Vec from Scratch]] — Word Embeddings

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/02-02 Linear Regression|02/02 Linear Regression]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/05-01 Text Processing — Tokenization, Stemming, Lemmatization|05/01 Text Processing — Tokenization, Stemming, Lemmatization]]
- depth 3: [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]], [[Lessons/02-14 Naive Bayes|02/14 Naive Bayes]], [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]]

## Builds on this

- [[Lessons/05-24 Coreference Resolution|05/24 Coreference Resolution]]
- [[Lessons/05-25 Entity Linking & Disambiguation|05/25 Entity Linking & Disambiguation]]
- [[Lessons/05-26 Relation Extraction & Knowledge Graph Construction|05/26 Relation Extraction & Knowledge Graph Construction]]

## Concepts taught

- NER `lesson term` — Label token spans with types (PERSON, ORG, GPE, DATE, ...).
- BIO `lesson term` — B-X begins, I-X continues, O outside.
- BILOU `lesson term` — Adds L-X (last), U-X (unit) for cleaner boundaries.
- CRF `lesson term` — Models transitions between labels, not just emissions. Enforces valid sequences.
- Nested NER `lesson term` — One span is a different entity than a sub-span of it. BIO cannot express this.
- Entity-level F1 `lesson term` — Predicted span must match true span exactly. Token-level F1 overstates accuracy.

## Ships

- [[Artifacts/05-06 ner-picker|ner-picker]] `skill` — Pick the right NER approach for a given extraction task.

## Further reading

- Lample et al. (2016). Neural Architectures for Named Entity Recognition ([link](https://arxiv.org/abs/1603.01360)) — the BiLSTM-CRF paper. Canonical.
- [[Resources/Devlin et al. (2018). BERT- Pre-training of Deep Bidirectional Transformers|Devlin et al. (2018). BERT: Pre-training of Deep Bidirectional Transformers]] ([link](https://arxiv.org/abs/1810.04805)) — introduces the token-classification pattern that became standard. ·  also cited by 1 other lesson
- seqeval ([link](https://github.com/chakki-works/seqeval)) — the correct metric library. Use it always.
- [[Resources/spaCy 101 — linguistic features|spaCy 101 — linguistic features]] ([link](https://spacy.io/usage/linguistic-features)) — practical reference for every attribute on `Doc.ents` and `Span`. ·  also cited by 2 other lessons


%% ── my notes ── %%
