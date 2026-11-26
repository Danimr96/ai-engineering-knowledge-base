---
id: "lesson:05/26"
type: lesson
ref: 05/26
phase: 5
num: 26
title: "Relation Extraction & Knowledge Graph Construction"
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
  - 05/26
  - 05-26
tags:
  - phase/05
  - type/build
  - community/76
  - stdlib-only
source: ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/26-relation-extraction-kg/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/26-relation-extraction-kg"
---

# 05/26 Relation Extraction & Knowledge Graph Construction

> NER found the entities. Entity linking anchored them. Relation extraction finds the edges between them. A knowledge graph is the sum of nodes, edges, and their provenance.

**Phase:** [[Phases/05 NLP, Foundations to Advanced|Phase 5: NLP, Foundations to Advanced]] · **Type:** Build · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/05-nlp-foundations-to-advanced/26-relation-extraction-kg/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/26-relation-extraction-kg) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/26-relation-extraction-kg) · code: main.py · quiz: 8 questions  
**Community:** [[Communities/76 Provenance|76 Provenance]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 5 · 06 (NER), Phase 5 · 25 (Entity Linking)`

- [[Lessons/05-06 Named Entity Recognition|05/06 Named Entity Recognition]] — NER
- [[Lessons/05-25 Entity Linking & Disambiguation|05/25 Entity Linking & Disambiguation]] — Entity Linking

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/05-02 Bag of Words, TF-IDF, and Text Representation|05/02 Bag of Words, TF-IDF, and Text Representation]], [[Lessons/05-03 Word Embeddings — Word2Vec from Scratch|05/03 Word Embeddings — Word2Vec from Scratch]], [[Lessons/05-24 Coreference Resolution|05/24 Coreference Resolution]]
- depth 3: [[Lessons/02-02 Linear Regression|02/02 Linear Regression]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/05-01 Text Processing — Tokenization, Stemming, Lemmatization|05/01 Text Processing — Tokenization, Stemming, Lemmatization]], [[Lessons/05-07 POS Tagging and Syntactic Parsing|05/07 POS Tagging and Syntactic Parsing]]

## Concepts taught

- Triple `lesson term` — (s, r, o) tuple that is the atomic unit of a KG.
- Open IE `lesson term` — Open-vocabulary relation phrases; high recall, low precision.
- Closed ontology `lesson term` — Bounded set of relation types (Wikidata, UMLS, FIBO).
- Canonicalization `lesson term` — Map surface names / relations to canonical ids.
- AEVS `lesson term` — Anchor-Extraction-Verification-Supplement pipeline (2026).
- [[Concepts/Provenance|Provenance]] `lesson term` — Every triple carries a doc id + char-span to its source.
- Distant supervision `lesson term` — Align text with an existing KG to create training data.

## Ships

- [[Artifacts/05-26 re-designer|re-designer]] `skill` — Design a relation extraction pipeline with provenance and canonicalization.

## Further reading

- Huguet Cabot, Navigli (2021). REBEL: Relation Extraction By End-to-end Language generation ([link](https://aclanthology.org/2021.findings-emnlp.204.pdf)) — seq2seq RE workhorse.
- Mintz et al. (2009). Distant supervision for relation extraction without labeled data ([link](https://www.aclweb.org/anthology/P09-1113.pdf)) — the distant-supervision paper.
- Wadden et al. (2019). Entity, Relation, and Event Extraction with Contextualized Span Representations (DyGIE++) ([link](https://arxiv.org/abs/1909.03546)) — joint IE.
- AEVS — Anchor-Extraction-Verification-Supplement framework ([link](https://www.mdpi.com/2073-431X/15/3/178)) — 2026 hallucination-mitigation design.
- Wikidata SPARQL tutorial ([link](https://www.wikidata.org/wiki/Wikidata:SPARQL_tutorial)) — canonical graph queries.


%% ── my notes ── %%
