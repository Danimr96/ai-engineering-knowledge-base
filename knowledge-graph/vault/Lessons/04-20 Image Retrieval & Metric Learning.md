---
id: "lesson:04/20"
type: lesson
ref: 04/20
phase: 4
num: 20
title: "Image Retrieval & Metric Learning"
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
  - 04/20
  - 04-20
tags:
  - phase/04
  - type/build
  - community/12
source: ai-engineering-from-scratch/phases/04-computer-vision/20-image-retrieval-metric/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/20-image-retrieval-metric"
---

# 04/20 Image Retrieval & Metric Learning

> A retrieval system ranks candidates by a distance in embedding space. Metric learning is the discipline of shaping that space so the distances mean what you want.

**Phase:** [[Phases/04 Computer Vision|Phase 4: Computer Vision]] · **Type:** Build · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/04-computer-vision/20-image-retrieval-metric/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/20-image-retrieval-metric) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/04-computer-vision/20-image-retrieval-metric) · code: main.py · quiz: 5 questions  
**Community:** [[Communities/12 Attention · Cross-Attention · Self-Attention|12 Attention · Cross-Attention · Self-Attention]] · **Libraries:** [[Libraries/torch (python)|torch]]  

## Prerequisites

Stated upstream: `Phase 4 Lesson 14 (ViT), Phase 4 Lesson 18 (CLIP)`

- [[Lessons/04-14 Vision Transformers (ViT)|04/14 Vision Transformers (ViT)]] — ViT
- [[Lessons/04-18 Open-Vocabulary Vision — CLIP|04/18 Open-Vocabulary Vision — CLIP]] — CLIP

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/04-04 Image Classification|04/04 Image Classification]], [[Lessons/04-17 Self-Supervised Vision — SimCLR, DINO, MAE|04/17 Self-Supervised Vision — SimCLR, DINO, MAE]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]]
- depth 3: [[Lessons/02-09 Model Evaluation|02/09 Model Evaluation]], [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]], [[Lessons/04-03 CNNs — LeNet to ResNet|04/03 CNNs — LeNet to ResNet]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]]

## Concepts taught

- Metric learning `lesson term` — Training an encoder so distances in its output space reflect a target similarity
- [[Concepts/Triplet loss|Triplet loss]] `lesson term` — L = max(0, d(a, p) - d(a, n) + margin); the canonical metric-learning loss
- Semi-hard mining `lesson term` — Negatives further from the anchor than the positive but within margin; empirically the most informative
- Proxy-based loss `lesson term` — One learned proxy per class; cross-entropy over similarity-to-proxies; no pair mining
- [[Concepts/Recall@K|Recall@K]] `glossary` — Fraction of queries with at least one correct result in the top K
- Instance retrieval `lesson term` — Fine-grained matching; off-the-shelf features usually underperform
- FAISS `lesson term` — Facebook's nearest-neighbour library; supports exact and approximate indexes
- [[Concepts/HNSW|HNSW]] `glossary` — Hierarchical navigable small world; fast approximate NN with small memory overhead

## Ships

- [[Artifacts/04-20 prompt-retrieval-loss-picker|prompt-retrieval-loss-picker]] `prompt` — Pick triplet / InfoNCE / ProxyNCA for a given retrieval problem
- [[Artifacts/04-20 skill-recall-at-k-runner|skill-recall-at-k-runner]] `skill` — Write a clean evaluation harness for recall@K with train/val/gallery splits and proper data contract

## Further reading

- FaceNet: A Unified Embedding for Face Recognition (Schroff et al., 2015) ([link](https://arxiv.org/abs/1503.03832)) — the triplet loss / semi-hard mining paper
- In Defense of the Triplet Loss for Person Re-Identification (Hermans et al., 2017) ([link](https://arxiv.org/abs/1703.07737)) — practical guide to triplet fine-tuning
- SMoT: Metric Learning Taxonomy (Kim et al., 2021) ([link](https://arxiv.org/abs/2010.06927)) — survey of modern losses and their connections
- FAISS documentation ([link](https://github.com/facebookresearch/faiss/wiki)) — every index, every trade-off


%% ── my notes ── %%
