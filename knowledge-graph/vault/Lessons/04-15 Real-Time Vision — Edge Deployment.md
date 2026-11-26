---
id: "lesson:04/15"
type: lesson
ref: 04/15
phase: 4
num: 15
title: "Real-Time Vision — Edge Deployment"
lesson_type: learn+build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 5
code_files: 2
concepts: 8
prereqs: 2
libraries:
  - torch
  - torchvision
aliases:
  - 04/15
  - 04-15
tags:
  - phase/04
  - type/learn+build
source: ai-engineering-from-scratch/phases/04-computer-vision/15-real-time-edge/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/15-real-time-edge"
---

# 04/15 Real-Time Vision — Edge Deployment

> Edge inference is the discipline of getting a 90-accuracy model to run at 30 fps on a device with 2 GB of RAM. Every percentage point of accuracy is traded against milliseconds of latency.

**Phase:** [[Phases/04 Computer Vision|Phase 4: Computer Vision]] · **Type:** Learn + Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/04-computer-vision/15-real-time-edge/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/15-real-time-edge) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/04-computer-vision/15-real-time-edge) · code: main.py, main.rs · quiz: 5 questions  
**Libraries:** [[Libraries/torch (python)|torch]], [[Libraries/torchvision (python)|torchvision]]  

## Prerequisites

Stated upstream: `Phase 4 Lesson 04 (Image Classification), Phase 10 Lesson 11 (Quantization)`

- [[Lessons/04-04 Image Classification|04/04 Image Classification]] — Image Classification
- [[Lessons/10-11 Quantization- Making Models Fit|10/11 Quantization: Making Models Fit]] — Quantization

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-13 Numerical Stability|01/13 Numerical Stability]], [[Lessons/02-09 Model Evaluation|02/09 Model Evaluation]], [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]], [[Lessons/04-03 CNNs — LeNet to ResNet|04/03 CNNs — LeNet to ResNet]], [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]], [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]], [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]], [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]], [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]], [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]], [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]], [[Lessons/10-08 DPO- Direct Preference Optimization|10/08 DPO: Direct Preference Optimization]], [[Lessons/10-09 Constitutional AI and Self-Improvement|10/09 Constitutional AI and Self-Improvement]], [[Lessons/10-10 Evaluation- Benchmarks, Evals, LM Harness|10/10 Evaluation: Benchmarks, Evals, LM Harness]]
- depth 3: [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]], [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]], [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]], [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]], [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]], [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]], [[Lessons/02-02 Linear Regression|02/02 Linear Regression]], [[Lessons/02-03 Logistic Regression|02/03 Logistic Regression]], [[Lessons/02-04 Decision Trees and Random Forests|02/04 Decision Trees and Random Forests]], [[Lessons/02-05 Support Vector Machines|02/05 Support Vector Machines]], [[Lessons/02-06 K-Nearest Neighbors and Distances|02/06 K-Nearest Neighbors and Distances]], [[Lessons/02-07 Unsupervised Learning|02/07 Unsupervised Learning]], [[Lessons/02-08 Feature Engineering & Selection|02/08 Feature Engineering & Selection]], [[Lessons/03-01 The Perceptron|03/01 The Perceptron]], [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-04 Activation Functions|03/04 Activation Functions]], [[Lessons/03-05 Loss Functions|03/05 Loss Functions]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/03-07 Regularization|03/07 Regularization]], [[Lessons/03-08 Weight Initialization and Training Stability|03/08 Weight Initialization and Training Stability]], [[Lessons/03-09 Learning Rate Schedules and Warmup|03/09 Learning Rate Schedules and Warmup]], [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]], [[Lessons/04-01 Image Fundamentals — Pixels, Channels, Color Spaces|04/01 Image Fundamentals — Pixels, Channels, Color Spaces]], [[Lessons/04-02 Convolutions from Scratch|04/02 Convolutions from Scratch]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/09-01 MDPs, States, Actions & Rewards|09/01 MDPs, States, Actions & Rewards]], [[Lessons/09-06 Policy Gradient — REINFORCE from Scratch|09/06 Policy Gradient — REINFORCE from Scratch]], [[Lessons/09-08 Proximal Policy Optimization (PPO)|09/08 Proximal Policy Optimization (PPO)]], [[Lessons/19-76 Collective Ops From Scratch|19/76 Collective Ops From Scratch]]

## Builds on this

- [[Lessons/04-16 Build a Complete Vision Pipeline — Capstone|04/16 Build a Complete Vision Pipeline — Capstone]]

## Concepts taught

- Latency `lesson term` — Time from input to output; p50/p95/p99 percentiles, not mean
- FLOPs `lesson term` — Floating-point ops per forward pass; rough proxy for compute cost
- INT8 quantisation `lesson term` — Replace FP32 weights/activations with 8-bit integers; ~4x smaller, 2-4x faster
- [[Concepts/PTQ|PTQ]] `lesson term` — Quantise a trained model without retraining; easy, usually enough
- [[Concepts/QAT|QAT]] `lesson term` — Simulate quantisation during training; best accuracy, requires labelled data
- ONNX `lesson term` — Model exchange format supported by every mainstream inference runtime
- TensorRT `lesson term` — Compiles ONNX into an optimised engine for NVIDIA GPUs
- [[Concepts/Knowledge Distillation|Knowledge Distillation]] (as *Distillation*) `glossary` — Train a small model to mimic a big model's logits; recovers most lost accuracy

## Ships

- [[Artifacts/04-15 prompt-edge-deployment-planner|prompt-edge-deployment-planner]] `prompt` — Pick backbone, quantisation strategy, and runtime given target device and latency SLA
- [[Artifacts/04-15 skill-latency-profiler|skill-latency-profiler]] `skill` — Write a complete latency-benchmarking script with warmup, synchronisation, percentiles, and memory tracking

## Further reading

- MobileNetV3 (Howard et al., 2019) ([link](https://arxiv.org/abs/1905.02244)) — mobile-first architecture with h-swish and squeeze-excite
- EfficientNet (Tan & Le, 2019) ([link](https://arxiv.org/abs/1905.11946)) — compound scaling for efficient architectures
- A Practical Guide to TensorRT Optimization (NVIDIA) ([link](https://developer.nvidia.com/blog/accelerating-model-inference-with-tensorrt-tips-and-best-practices-for-pytorch-users/)) — how to actually get the throughput numbers in the paper
- ONNX Runtime docs ([link](https://onnxruntime.ai/docs/)) — quantisation, graph optimisation, provider selection


%% ── my notes ── %%
