---
id: "lesson:04/25"
type: lesson
ref: 04/25
phase: 4
num: 25
title: "Vision-Language Models — The ViT-MLP-LLM Pattern"
lesson_type: learn
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 5
code_files: 1
concepts: 10
prereqs: 3
community: 12
libraries:
  - torch
aliases:
  - 04/25
  - 04-25
tags:
  - phase/04
  - type/learn
  - community/12
source: ai-engineering-from-scratch/phases/04-computer-vision/25-vision-language-models/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/25-vision-language-models"
---

# 04/25 Vision-Language Models — The ViT-MLP-LLM Pattern

> A vision encoder converts an image into tokens. An MLP projector maps those tokens into the LLM's embedding space. A language model does the rest. That pattern — ViT-MLP-LLM — is every production VLM in 2026.

**Phase:** [[Phases/04 Computer Vision|Phase 4: Computer Vision]] · **Type:** Learn + Use · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/04-computer-vision/25-vision-language-models/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/25-vision-language-models) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/04-computer-vision/25-vision-language-models) · code: main.py · quiz: 5 questions  
**Community:** [[Communities/12 Attention · Cross-Attention · Self-Attention|12 Attention · Cross-Attention · Self-Attention]] · **Libraries:** [[Libraries/torch (python)|torch]]  

## Prerequisites

Stated upstream: `Phase 4 Lesson 14 (ViT), Phase 4 Lesson 18 (CLIP), Phase 7 Lesson 02 (Self-Attention)`

- [[Lessons/04-14 Vision Transformers (ViT)|04/14 Vision Transformers (ViT)]] — ViT
- [[Lessons/04-18 Open-Vocabulary Vision — CLIP|04/18 Open-Vocabulary Vision — CLIP]] — CLIP
- [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]] — Self-Attention

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/04-04 Image Classification|04/04 Image Classification]], [[Lessons/04-17 Self-Supervised Vision — SimCLR, DINO, MAE|04/17 Self-Supervised Vision — SimCLR, DINO, MAE]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]]
- depth 3: [[Lessons/02-09 Model Evaluation|02/09 Model Evaluation]], [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]], [[Lessons/04-03 CNNs — LeNet to ResNet|04/03 CNNs — LeNet to ResNet]], [[Lessons/05-09 Sequence-to-Sequence Models|05/09 Sequence-to-Sequence Models]]

## Concepts taught

- ViT-MLP-LLM `lesson term` — Vision encoder + projector + language model; every 2026 VLM
- [[Concepts/Projector|Projector]] `lesson term` — 2-4 layer MLP (or Q-former) that maps vision tokens into LLM embedding space
- DeepStack `lesson term` — Multi-level ViT features stacked rather than last-layer only
- [[Concepts/Image Token|Image Token]] `glossary` — Special token in the text stream replaced by projected vision embeddings
- CMER `lesson term` — Cross-Modal Error Rate; high when text confidence is high but image-text similarity is low
- Visual agent `lesson term` — VLM operating GUIs (OSWorld, mobile, web) with tool calls
- [[Concepts/Q-former|Q-former]] `lesson term` — BLIP-2 style projector producing a fixed number of visual query tokens
- Alignment / pre-training / instruction tuning `lesson term` — Standard VLM training pipeline
- [[Concepts/Vision-Language Model (VLM)|Vision-Language Model (VLM)]] `glossary` — A model that learns relationships between, or jointly processes, visual and language representations for tasks such as retrieval, description, question answering, or grounded generation.

## Ships

- [[Artifacts/04-25 prompt-vlm-selector|prompt-vlm-selector]] `prompt` — Pick Qwen3-VL / InternVL3.5 / LLaVA-Next / API given accuracy, latency, context length, and budget
- [[Artifacts/04-25 skill-cmer-monitor|skill-cmer-monitor]] `skill` — Instrument a production VLM endpoint with Cross-Modal Error Rate monitoring, dashboards, and alerts

## Further reading

- [[Resources/InternVL3.5 Advancing Open-Source Multimodal Models (arXiv 2508.18265)|InternVL3.5 Advancing Open-Source Multimodal Models (arXiv 2508.18265)]] ([link](https://arxiv.org/html/2508.18265v1)) ·  also cited by 1 other lesson
- [[Resources/Qwen3-VL Technical Report (arXiv 2511.21631)|Qwen3-VL Technical Report (arXiv 2511.21631)]] ([link](https://arxiv.org/abs/2511.21631)) ·  also cited by 1 other lesson
- BentoML: Best Open-Source VLMs 2026 ([link](https://www.bentoml.com/blog/multimodal-ai-a-guide-to-open-source-vision-language-models))
- LLaVA-Next series ([link](https://llava-vl.github.io/blog/2024-05-10-llava-next-stronger-llms/))
- MMMU: Multi-discipline Multimodal Understanding benchmark ([link](https://mmmu-benchmark.github.io/))
- VLMs in manufacturing (Robotics Tomorrow, March 2026) ([link](https://www.roboticstomorrow.com/story/2026/03/when-machines-learn-to-see-like-experts-the-rise-of-vision-language-models-in-manufacturing/26335/))


%% ── my notes ── %%
