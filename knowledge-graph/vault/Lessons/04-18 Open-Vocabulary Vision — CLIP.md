---
id: "lesson:04/18"
type: lesson
ref: 04/18
phase: 4
num: 18
title: "Open-Vocabulary Vision — CLIP"
lesson_type: build
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 5
code_files: 1
concepts: 8
prereqs: 2
community: 12
libraries:
  - torch
aliases:
  - 04/18
  - 04-18
tags:
  - phase/04
  - type/build
  - community/12
source: ai-engineering-from-scratch/phases/04-computer-vision/18-open-vocab-clip/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/18-open-vocab-clip"
---

# 04/18 Open-Vocabulary Vision — CLIP

> Train an image encoder and a text encoder together so that matching (image, caption) pairs land at the same point in a shared space. That is the whole trick.

**Phase:** [[Phases/04 Computer Vision|Phase 4: Computer Vision]] · **Type:** Build + Use · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/04-computer-vision/18-open-vocab-clip/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/18-open-vocab-clip) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/04-computer-vision/18-open-vocab-clip) · code: main.py · quiz: 5 questions  
**Community:** [[Communities/12 Attention · Cross-Attention · Self-Attention|12 Attention · Cross-Attention · Self-Attention]] · **Libraries:** [[Libraries/torch (python)|torch]]  

## Prerequisites

Stated upstream: `Phase 4 Lesson 14 (ViT), Phase 4 Lesson 17 (Self-Supervised)`

- [[Lessons/04-14 Vision Transformers (ViT)|04/14 Vision Transformers (ViT)]] — ViT
- [[Lessons/04-17 Self-Supervised Vision — SimCLR, DINO, MAE|04/17 Self-Supervised Vision — SimCLR, DINO, MAE]] — Self-Supervised

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/04-04 Image Classification|04/04 Image Classification]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]]
- depth 3: [[Lessons/02-09 Model Evaluation|02/09 Model Evaluation]], [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]], [[Lessons/04-03 CNNs — LeNet to ResNet|04/03 CNNs — LeNet to ResNet]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]]

## Builds on this

- [[Lessons/04-20 Image Retrieval & Metric Learning|04/20 Image Retrieval & Metric Learning]]
- [[Lessons/04-24 SAM 3 & Open-Vocabulary Segmentation|04/24 SAM 3 & Open-Vocabulary Segmentation]]
- [[Lessons/04-25 Vision-Language Models — The ViT-MLP-LLM Pattern|04/25 Vision-Language Models — The ViT-MLP-LLM Pattern]]

## Concepts taught

- Two-tower `lesson term` — Separate image and text encoders ending in a shared-dim projection head
- [[Concepts/Zero-Shot|Zero-Shot]] `glossary` — Classify into classes described only by text at inference; no labels touched
- Temperature / logit_scale `lesson term` — Learned scalar that scales the similarity matrix before softmax
- [[Concepts/Prompt template|Prompt template]] `lesson term` — Natural-language wrapper around class names; averaging many templates boosts zero-shot accuracy
- [[Concepts/Clip|Clip]] `lesson term` — The 2021 OpenAI model; vocabulary of the field in 2026
- [[Concepts/SigLIP|SigLIP]] `lesson term` — Swaps softmax for per-pair sigmoid; trains better at small batches
- OpenCLIP `lesson term` — Community-trained CLIP variants on LAION; production default for open-source pipelines
- [[Concepts/Vision-Language Model (VLM)|Vision-Language Model (VLM)]] (as *VLM*) `glossary` — A CLIP-family encoder plus an LLM, trained to answer questions about images

## Ships

- [[Artifacts/04-18 prompt-zero-shot-class-picker|prompt-zero-shot-class-picker]] `prompt` — Design prompt templates for zero-shot CLIP given a list of classes and a domain
- [[Artifacts/04-18 skill-image-text-retriever|skill-image-text-retriever]] `skill` — Build an image embedding index with any CLIP checkpoint; support query-by-text and query-by-image

## Further reading

- [[Resources/CLIP|CLIP]] ([link](https://arxiv.org/abs/2103.00020)) ·  also cited by 2 other lessons
- [[Resources/SigLIP- Sigmoid Loss for Language-Image Pre-Training (Zhai et al., 2023)|SigLIP: Sigmoid Loss for Language-Image Pre-Training (Zhai et al., 2023)]] ([link](https://arxiv.org/abs/2303.15343)) ·  also cited by 1 other lesson
- OpenCLIP ([link](https://github.com/mlfoundations/open_clip)) — the community codebase
- DINOv2 vs CLIP vs MAE: a features comparison ([link](https://huggingface.co/blog/dinov2)) — HF guide with side-by-side use cases


%% ── my notes ── %%
