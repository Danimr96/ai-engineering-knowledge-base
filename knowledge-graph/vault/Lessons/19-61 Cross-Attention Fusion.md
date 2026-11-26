---
id: "lesson:19/61"
type: lesson
ref: 19/61
phase: 19
num: 61
title: Cross-Attention Fusion
lesson_type: build
languages:
  - Python
time_min: 90
on_route: false
quiz_count: 6
code_files: 2
concepts: 8
prereqs: 8
community: 2
libraries:
  - torch
aliases:
  - 19/61
  - 19-61
tags:
  - phase/19
  - type/build
  - community/02
source: ai-engineering-from-scratch/phases/19-capstone-projects/61-cross-attention-fusion/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/61-cross-attention-fusion"
---

# 19/61 Cross-Attention Fusion

> The projection layer aligns one image vector with one caption vector. A real vision-language decoder needs every text token to attend to every patch token, so the model can ground each word in a region. Cross-attention is how that grounding happens. The text queries; the vision keys and values answer. This lesson builds the cross-attention block, the causal text self-attention, and the mask shapes that keep both legal.

**Phase:** [[Phases/19 Capstone Projects|Phase 19: Capstone Projects]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/19-capstone-projects/61-cross-attention-fusion/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/61-cross-attention-fusion) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/19-capstone-projects/61-cross-attention-fusion) · code: main.py, test_main.py · quiz: 6 questions  
**Track:** [[Tracks/19-E Vision-language model from scratch|Phase 19 Track E: Vision-language model from scratch]]  
**Community:** [[Communities/02 Bucket · Causal mask · Manifest|02 Bucket · Causal mask · Manifest]] · **Libraries:** [[Libraries/torch (python)|torch]]  

## Prerequisites

Stated upstream: `Phase 19 lessons 30-37 (Track B foundations)`

- **19/30-37** — Track B foundations:
    - [[Lessons/19-30 BPE Tokenizer From Scratch|19/30 BPE Tokenizer From Scratch]]
    - [[Lessons/19-31 Tokenized Dataset with Sliding Window|19/31 Tokenized Dataset with Sliding Window]]
    - [[Lessons/19-32 Token and Positional Embeddings|19/32 Token and Positional Embeddings]]
    - [[Lessons/19-33 Multi-Head Self-Attention|19/33 Multi-Head Self-Attention]]
    - [[Lessons/19-34 Transformer Block from Scratch|19/34 Transformer Block from Scratch]]
    - [[Lessons/19-35 GPT Model Assembly|19/35 GPT Model Assembly]]
    - [[Lessons/19-36 Training Loop and Evaluation|19/36 Training Loop and Evaluation]]
    - [[Lessons/19-37 Loading Pretrained Weights|19/37 Loading Pretrained Weights]]

## Builds on this

- [[Lessons/19-63 Multimodal Evaluation|19/63 Multimodal Evaluation]]

## Concepts taught

- [[Concepts/Late Fusion|Late Fusion]] `glossary` — Text and vision stay in separate streams; cross-attention bridges them at every block
- [[Concepts/Cross-Attention|Cross-Attention]] `glossary` — Q comes from one stream, K and V from another
- [[Concepts/Causal mask|Causal mask]] `lesson term` — Lower-triangular boolean mask that prevents looking ahead during autoregression
- [[Concepts/KV Cache|KV Cache]] `glossary` — Image keys and values stored once and reused for every decode step
- Memory tokens `lesson term` — The frozen image tokens that the decoder reaches into
- [[Concepts/Multimodal Fusion|Multimodal Fusion]] `glossary` — Combining evidence or learned representations from more than one modality to produce a joint representation, prediction, or generated output.
- [[Concepts/Visual Grounding|Visual Grounding]] `glossary` — Connecting a language expression to spatial evidence in an image or video, such as a region, object, mask, or tracked entity.


%% ── my notes ── %%
