---
id: "lesson:07/14"
type: lesson
ref: 07/14
phase: 7
num: 14
title: "Build a Transformer from Scratch — The Capstone"
lesson_type: build
languages:
  - Python
time_min: 120
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 13
community: 5
libraries:
  - torch
aliases:
  - 07/14
  - 07-14
tags:
  - phase/07
  - type/build
  - community/05
source: ai-engineering-from-scratch/phases/07-transformers-deep-dive/14-build-a-transformer-capstone/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/07-transformers-deep-dive/14-build-a-transformer-capstone"
---

# 07/14 Build a Transformer from Scratch — The Capstone

> Thirteen lessons. One model. No shortcuts.

**Phase:** [[Phases/07 Transformers Deep Dive|Phase 7: Transformers Deep Dive]] · **Type:** Build · **Time:** 120 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/07-transformers-deep-dive/14-build-a-transformer-capstone/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/07-transformers-deep-dive/14-build-a-transformer-capstone) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/07-transformers-deep-dive/14-build-a-transformer-capstone) · code: main.py  
**Community:** [[Communities/05 Temperature · Autoregressive · Logits|05 Temperature · Autoregressive · Logits]] · **Libraries:** [[Libraries/torch (python)|torch]]  

## Prerequisites

Stated upstream: `Phase 7 · 01 through 13. Don't skip.`

- **07/01-13**:
    - [[Lessons/07-01 Why Transformers — The Problems with RNNs|07/01 Why Transformers — The Problems with RNNs]]
    - [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]]
    - [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]]
    - [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]]
    - [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]]
    - [[Lessons/07-06 BERT — Masked Language Modeling|07/06 BERT — Masked Language Modeling]]
    - [[Lessons/07-07 GPT — Causal Language Modeling|07/07 GPT — Causal Language Modeling]]
    - [[Lessons/07-08 T5, BART — Encoder-Decoder Models|07/08 T5, BART — Encoder-Decoder Models]]
    - [[Lessons/07-09 Vision Transformers (ViT)|07/09 Vision Transformers (ViT)]]
    - [[Lessons/07-10 Audio Transformers — Whisper Architecture|07/10 Audio Transformers — Whisper Architecture]]
    - [[Lessons/07-11 Mixture of Experts (MoE)|07/11 Mixture of Experts (MoE)]]
    - [[Lessons/07-12 KV Cache, Flash Attention & Inference Optimization|07/12 KV Cache, Flash Attention & Inference Optimization]]
    - [[Lessons/07-13 Scaling Laws|07/13 Scaling Laws]]
- Not understood by the parser: `Don't skip`

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/04-03 CNNs — LeNet to ResNet|04/03 CNNs — LeNet to ResNet]], [[Lessons/04-14 Vision Transformers (ViT)|04/14 Vision Transformers (ViT)]], [[Lessons/05-02 Bag of Words, TF-IDF, and Text Representation|05/02 Bag of Words, TF-IDF, and Text Representation]], [[Lessons/05-09 Sequence-to-Sequence Models|05/09 Sequence-to-Sequence Models]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]]
- depth 3: [[Lessons/02-02 Linear Regression|02/02 Linear Regression]], [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]], [[Lessons/04-01 Image Fundamentals — Pixels, Channels, Color Spaces|04/01 Image Fundamentals — Pixels, Channels, Color Spaces]], [[Lessons/04-02 Convolutions from Scratch|04/02 Convolutions from Scratch]], [[Lessons/04-04 Image Classification|04/04 Image Classification]], [[Lessons/05-01 Text Processing — Tokenization, Stemming, Lemmatization|05/01 Text Processing — Tokenization, Stemming, Lemmatization]], [[Lessons/05-08 CNNs and RNNs for Text|05/08 CNNs and RNNs for Text]]

## Builds on this

- [[Lessons/08-01 Generative Models — Taxonomy & History|08/01 Generative Models — Taxonomy & History]]

## Concepts taught

- nanoGPT `lesson term` — Minimal decoder-only transformer training code, ~300 LOC; the canonical reference.
- tinyshakespeare `lesson term` — ~1.1 MB of text; every character-LM tutorial since 2015 uses it.
- Tied embeddings `lesson term` — LM head weight = transpose of token embedding matrix; saves parameters, improves quality.
- bf16 autocast `lesson term` — Run forward/back in bf16, keep optimizer state in fp32; standard since 2021.
- [[Concepts/Gradient Clipping|Gradient Clipping]] `glossary` — Cap global grad norm at 1.0; prevents training blowups.
- Cosine LR schedule `lesson term` — LR ramps up linearly (warmup) then decays cosine-shaped to 10% of peak.
- [[Concepts/MFU|MFU]] `lesson term` — Achieved FLOPs / theoretical peak; 40% dense, 30% MoE is strong in 2026.
- Val loss `lesson term` — Cross-entropy on data the model never saw; overfit detector.

## Ships

- [[Artifacts/07-14 transformer-review|transformer-review]] `skill` — Review a transformer-from-scratch implementation against the 13 Phase 7 lessons.

## Further reading

- [[Resources/The Annotated Transformer (Harvard NLP)|The Annotated Transformer (Harvard NLP)]] ([link](https://nlp.seas.harvard.edu/annotated-transformer/)) — the classic annotated implementation. ·  also cited by 1 other lesson


%% ── my notes ── %%
