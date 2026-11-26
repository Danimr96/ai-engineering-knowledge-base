---
id: "lesson:07/06"
type: lesson
ref: 07/06
phase: 7
num: 6
title: "BERT — Masked Language Modeling"
lesson_type: build
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 2
community: 5
aliases:
  - 07/06
  - 07-06
tags:
  - phase/07
  - type/build
  - community/05
  - stdlib-only
source: ai-engineering-from-scratch/phases/07-transformers-deep-dive/06-bert-masked-language-modeling/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/07-transformers-deep-dive/06-bert-masked-language-modeling"
---

# 07/06 BERT — Masked Language Modeling

> GPT predicts the next word. BERT predicts a missing word. One sentence of difference — and half a decade of everything embedding-shaped.

**Phase:** [[Phases/07 Transformers Deep Dive|Phase 7: Transformers Deep Dive]] · **Type:** Build · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/07-transformers-deep-dive/06-bert-masked-language-modeling/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/07-transformers-deep-dive/06-bert-masked-language-modeling) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/07-transformers-deep-dive/06-bert-masked-language-modeling) · code: main.py  
**Community:** [[Communities/05 Temperature · Autoregressive · Logits|05 Temperature · Autoregressive · Logits]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 7 · 05 (Full Transformer), Phase 5 · 02 (Text Representation)`

- [[Lessons/05-02 Bag of Words, TF-IDF, and Text Representation|05/02 Bag of Words, TF-IDF, and Text Representation]] — Text Representation
- [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]] — Full Transformer

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/02-02 Linear Regression|02/02 Linear Regression]], [[Lessons/05-01 Text Processing — Tokenization, Stemming, Lemmatization|05/01 Text Processing — Tokenization, Stemming, Lemmatization]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]]
- depth 3: [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]], [[Lessons/02-14 Naive Bayes|02/14 Naive Bayes]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]]

## Builds on this

- [[Lessons/07-07 GPT — Causal Language Modeling|07/07 GPT — Causal Language Modeling]]
- [[Lessons/07-08 T5, BART — Encoder-Decoder Models|07/08 T5, BART — Encoder-Decoder Models]]
- [[Lessons/07-14 Build a Transformer from Scratch — The Capstone|07/14 Build a Transformer from Scratch — The Capstone]]

## Concepts taught

- MLM `lesson term` — Training signal: randomly replace 15% of tokens with [MASK], predict the originals.
- [[Concepts/Bidirectional|Bidirectional]] `lesson term` — Encoder attention has no causal mask — every position sees every other position.
- [CLS] `lesson term` — A special token prepended to every sequence; its final embedding is used as the sentence-level representation.
- [SEP] `lesson term` — Separates paired sequences (e.g. query/doc, sentence A/B).
- NSP `lesson term` — BERT's second pretraining task; shown to be useless in RoBERTa, dropped after 2019.
- [[Concepts/Fine-tuning|Fine-tuning]] `glossary` — Keep the encoder mostly frozen; train a small head on top for the downstream task.
- [[Concepts/Cross-encoder|Cross-encoder]] `lesson term` — A BERT that takes both query and doc as input, outputs a relevance score.
- ModernBERT `lesson term` — Encoder rebuilt with RoPE, RMSNorm, GeGLU, alternating local/global attention, 8K context.

## Ships

- [[Artifacts/07-06 bert-finetuner|bert-finetuner]] `skill` — Scope a BERT fine-tune for a new classification, extraction, or retrieval task.

## Further reading

- [[Resources/Devlin et al. (2018). BERT- Pre-training of Deep Bidirectional Transformers|Devlin et al. (2018). BERT: Pre-training of Deep Bidirectional Transformers]] ([link](https://arxiv.org/abs/1810.04805)) — original paper. ·  also cited by 1 other lesson
- Liu et al. (2019). RoBERTa: A Robustly Optimized BERT Pretraining Approach ([link](https://arxiv.org/abs/1907.11692)) — how to train BERT right; kills NSP.
- Clark et al. (2020). ELECTRA: Pre-training Text Encoders as Discriminators Rather Than Generators ([link](https://arxiv.org/abs/2003.10555)) — replaced-token detection beats MLM at matched compute.
- Warner et al. (2024). Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder ([link](https://arxiv.org/abs/2412.13663)) — ModernBERT paper.
- HuggingFace `modeling_bert.py` ([link](https://github.com/huggingface/transformers/blob/main/src/transformers/models/bert/modeling_bert.py)) — canonical encoder reference.


%% ── my notes ── %%
