---
id: "lesson:05/25"
type: lesson
ref: 05/25
phase: 5
num: 25
title: "Entity Linking & Disambiguation"
lesson_type: build
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 8
code_files: 1
concepts: 7
prereqs: 2
community: 76
aliases:
  - 05/25
  - 05-25
tags:
  - phase/05
  - type/build
  - community/76
  - stdlib-only
source: ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/25-entity-linking/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/25-entity-linking"
---

# 05/25 Entity Linking & Disambiguation

> NER found "Paris." Entity linking decides: Paris, France? Paris Hilton? Paris, Texas? Paris (the Trojan prince)? Without linking, your knowledge graph stays ambiguous.

**Phase:** [[Phases/05 NLP, Foundations to Advanced|Phase 5: NLP, Foundations to Advanced]] · **Type:** Build · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/05-nlp-foundations-to-advanced/25-entity-linking/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/25-entity-linking) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/25-entity-linking) · code: main.py · quiz: 8 questions  
**Community:** [[Communities/76 Provenance|76 Provenance]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 5 · 06 (NER), Phase 5 · 24 (Coreference Resolution)`

- [[Lessons/05-06 Named Entity Recognition|05/06 Named Entity Recognition]] — NER
- [[Lessons/05-24 Coreference Resolution|05/24 Coreference Resolution]] — Coreference Resolution

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/05-02 Bag of Words, TF-IDF, and Text Representation|05/02 Bag of Words, TF-IDF, and Text Representation]], [[Lessons/05-03 Word Embeddings — Word2Vec from Scratch|05/03 Word Embeddings — Word2Vec from Scratch]], [[Lessons/05-07 POS Tagging and Syntactic Parsing|05/07 POS Tagging and Syntactic Parsing]]
- depth 3: [[Lessons/02-02 Linear Regression|02/02 Linear Regression]], [[Lessons/02-14 Naive Bayes|02/14 Naive Bayes]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/05-01 Text Processing — Tokenization, Stemming, Lemmatization|05/01 Text Processing — Tokenization, Stemming, Lemmatization]]

## Builds on this

- [[Lessons/05-26 Relation Extraction & Knowledge Graph Construction|05/26 Relation Extraction & Knowledge Graph Construction]]

## Concepts taught

- Entity linking (as *Entity linking (EL)*) `lesson term` — Map a mention to a unique KB entry.
- Candidate generation `lesson term` — Return a shortlist of plausible KB entries for a mention.
- Disambiguation `lesson term` — Score candidates using context, pick the winner.
- Alias index `lesson term` — Map from surface form → candidate entities.
- NIL `lesson term` — Explicit prediction that no KB entry matches.
- KB `lesson term` — Wikidata, Wikipedia, DBpedia, or your domain KB.
- AIDA-CoNLL `lesson term` — 1,393 Reuters articles with gold entity links.

## Ships

- [[Artifacts/05-25 entity-linker|entity-linker]] `skill` — Design an entity linking pipeline — KB, candidate generator, disambiguator, evaluation.

## Further reading

- Hoffart et al. (2011). Robust Disambiguation of Named Entities in Text (AIDA) ([link](https://www.aclweb.org/anthology/D11-1072.pdf)) — the benchmark paper.
- Wu et al. (2020). Zero-shot Entity Linking with Dense Entity Retrieval (BLINK) ([link](https://arxiv.org/abs/1911.03814)) — the embedding-based workhorse.
- REL: An Entity Linker Standing on the Shoulders of Giants (2020) ([link](https://arxiv.org/abs/2006.01969)) — the open production stack.
- De Cao et al. (2021). Autoregressive Entity Retrieval (GENRE) ([link](https://arxiv.org/abs/2010.00904)) — generative EL with constrained decoding.
- Milne, Witten (2008). Learning to Link with Wikipedia ([link](https://www.cs.waikato.ac.nz/~ihw/papers/08-DM-IHW-LearningToLinkWithWikipedia.pdf)) — the foundational prior+context approach.


%% ── my notes ── %%
