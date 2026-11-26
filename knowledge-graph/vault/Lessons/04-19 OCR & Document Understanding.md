---
id: "lesson:04/19"
type: lesson
ref: 04/19
phase: 4
num: 19
title: "OCR & Document Understanding"
lesson_type: learn
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 5
code_files: 1
concepts: 8
prereqs: 2
community: 13
libraries:
  - numpy
  - torch
aliases:
  - 04/19
  - 04-19
tags:
  - phase/04
  - type/learn
  - community/13
source: ai-engineering-from-scratch/phases/04-computer-vision/19-ocr-document-understanding/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/19-ocr-document-understanding"
---

# 04/19 OCR & Document Understanding

> OCR is a three-stage pipeline — detect text boxes, recognise the characters, then lay them out. Every modern OCR system reorders these stages or merges them.

**Phase:** [[Phases/04 Computer Vision|Phase 4: Computer Vision]] · **Type:** Learn + Use · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/04-computer-vision/19-ocr-document-understanding/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/19-ocr-document-understanding) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/04-computer-vision/19-ocr-document-understanding) · code: main.py · quiz: 5 questions  
**Community:** [[Communities/13 Object Multiplex · Clip · Divided attention|13 Object Multiplex · Clip · Divided attention]] · **Libraries:** [[Libraries/numpy (python)|numpy]], [[Libraries/torch (python)|torch]]  

## Prerequisites

Stated upstream: `Phase 4 Lesson 06 (Detection), Phase 7 Lesson 02 (Self-Attention)`

- [[Lessons/04-06 Object Detection — YOLO from Scratch|04/06 Object Detection — YOLO from Scratch]] — Detection
- [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]] — Self-Attention

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/04-03 CNNs — LeNet to ResNet|04/03 CNNs — LeNet to ResNet]], [[Lessons/04-04 Image Classification|04/04 Image Classification]], [[Lessons/04-05 Transfer Learning & Fine-Tuning|04/05 Transfer Learning & Fine-Tuning]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]]
- depth 3: [[Lessons/02-09 Model Evaluation|02/09 Model Evaluation]], [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]], [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]], [[Lessons/04-01 Image Fundamentals — Pixels, Channels, Color Spaces|04/01 Image Fundamentals — Pixels, Channels, Color Spaces]], [[Lessons/04-02 Convolutions from Scratch|04/02 Convolutions from Scratch]], [[Lessons/05-09 Sequence-to-Sequence Models|05/09 Sequence-to-Sequence Models]]

## Concepts taught

- OCR `lesson term` — Turning image regions into character sequences
- [[Concepts/CTC|CTC]] `lesson term` — Loss that trains a sequence model without per-timestep labels; marginalises over alignments
- CRNN `lesson term` — Conv feature extractor + BiLSTM + CTC; the 2015 baseline still used in production
- Donut `lesson term` — ViT encoder + text decoder; emits JSON directly from image
- Layout parsing `lesson term` — Detect and label Title/Table/Figure/Paragraph regions in a document
- Reading order `lesson term` — Ordering of recognised regions into a sentence; trivial for Latin, non-trivial for mixed layouts
- CER / WER `lesson term` — Levenshtein distance / reference length at character or word granularity
- VLM-OCR `lesson term` — A vision-language model trained or prompted for OCR tasks; current SOTA on complex documents

## Ships

- [[Artifacts/04-19 prompt-ocr-stack-picker|prompt-ocr-stack-picker]] `prompt` — Pick Tesseract / PaddleOCR / Donut / VLM-OCR given document type, language, and structure
- [[Artifacts/04-19 skill-ctc-decoder|skill-ctc-decoder]] `skill` — Write greedy and beam-search CTC decoders from scratch, including length normalisation

## Further reading

- CRNN (Shi et al., 2015) ([link](https://arxiv.org/abs/1507.05717)) — the original CNN+RNN+CTC architecture
- [[Resources/Donut (Kim et al., 2022)|Donut (Kim et al., 2022)]] ([link](https://arxiv.org/abs/2111.15664)) — OCR-free document understanding transformer ·  also cited by 1 other lesson
- [[Resources/Connectionist Temporal Classification|Connectionist Temporal Classification]] ([link](https://www.cs.toronto.edu/~graves/icml_2006.pdf)) — the original CTC paper; densely packed with the algorithmic ideas ·  also cited by 1 other lesson
- PaddleOCR ([link](https://github.com/PaddlePaddle/PaddleOCR)) — the open-source production OCR stack


%% ── my notes ── %%
