---
id: "lesson:05/28"
type: lesson
ref: 05/28
phase: 5
num: 28
title: "Long-Context Evaluation — NIAH, RULER, LongBench, MRCR"
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 8
code_files: 1
concepts: 7
prereqs: 2
aliases:
  - 05/28
  - 05-28
tags:
  - phase/05
  - type/learn
  - stdlib-only
source: ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/28-long-context-evaluation/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/28-long-context-evaluation"
---

# 05/28 Long-Context Evaluation — NIAH, RULER, LongBench, MRCR

> Gemini 3 Pro advertises 10M tokens of context. At 1M tokens, 8-needle MRCR drops to 26.3%. Advertised ≠ usable. Long-context evaluation tells you the actual capacity of the model you are shipping on.

**Phase:** [[Phases/05 NLP, Foundations to Advanced|Phase 5: NLP, Foundations to Advanced]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/05-nlp-foundations-to-advanced/28-long-context-evaluation/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/28-long-context-evaluation) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/28-long-context-evaluation) · code: main.py · quiz: 8 questions  
**Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 5 · 13 (Question Answering), Phase 5 · 23 (Chunking Strategies)`

- [[Lessons/05-13 Question Answering Systems|05/13 Question Answering Systems]] — Question Answering
- [[Lessons/05-23 Chunking Strategies for RAG|05/23 Chunking Strategies for RAG]] — Chunking Strategies

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]], [[Lessons/05-11 Machine Translation|05/11 Machine Translation]], [[Lessons/05-14 Information Retrieval and Search|05/14 Information Retrieval and Search]], [[Lessons/05-22 Embedding Models — The 2026 Deep Dive|05/22 Embedding Models — The 2026 Deep Dive]]
- depth 3: [[Lessons/05-02 Bag of Words, TF-IDF, and Text Representation|05/02 Bag of Words, TF-IDF, and Text Representation]], [[Lessons/05-03 Word Embeddings — Word2Vec from Scratch|05/03 Word Embeddings — Word2Vec from Scratch]], [[Lessons/05-04 GloVe, FastText, and Subword Embeddings|05/04 GloVe, FastText, and Subword Embeddings]], [[Lessons/05-09 Sequence-to-Sequence Models|05/09 Sequence-to-Sequence Models]]

## Concepts taught

- NIAH `lesson term` — Plant a fact in filler, ask the model to retrieve it.
- RULER `lesson term` — 13 task types across retrieval / multi-hop / aggregation / QA.
- Effective context `lesson term` — Length at which accuracy still holds above threshold.
- [[Concepts/Lost in the Middle|Lost in the Middle]] `glossary` — Models under-attend to content in the middle of long inputs.
- Multi-needle `lesson term` — Multiple plants; tests attention juggling, not retrieval alone.
- MRCR `lesson term` — 8, 24, or 100-needle coreference; exposes attention saturation.
- NoLiMa `lesson term` — Needle and query share no literal tokens; requires reasoning.

## Ships

- [[Artifacts/05-28 long-context-eval|long-context-eval]] `skill` — Design a long-context evaluation battery for a given model and use case.

## Further reading

- [[Resources/Liu et al. (2024). Lost in the Middle- How Language Models Use Long Contexts|Liu et al. (2024). Lost in the Middle: How Language Models Use Long Contexts]] ([link](https://arxiv.org/abs/2307.03172)) — the depth-bias paper. ·  also cited by 2 other lessons
- Hsieh et al. (2024). RULER: What's the Real Context Size of Your Long-Context LMs? ([link](https://arxiv.org/abs/2404.06654)) — the multi-task benchmark.
- Modarressi et al. (2024). NoLiMa: Non-lexical needles ([link](https://arxiv.org/abs/2404.06666)) — harder needles.
- Kuratov et al. (2024). BABILong ([link](https://arxiv.org/abs/2406.10149)) — reasoning-in-haystack.
- Bai et al. (2024). LongBench v2 ([link](https://arxiv.org/abs/2412.15204)) — real-world long-context eval.
- [[Resources/Kamradt (2023). Needle in a Haystack analysis|Kamradt (2023). Needle in a Haystack analysis]] ([link](https://github.com/gkamradt/LLMTest_NeedleInAHaystack)) — the original NIAH repo. ·  also cited by 1 other lesson


%% ── my notes ── %%
