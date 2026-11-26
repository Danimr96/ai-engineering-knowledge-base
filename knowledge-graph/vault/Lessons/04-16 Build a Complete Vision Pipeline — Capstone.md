---
id: "lesson:04/16"
type: lesson
ref: 04/16
phase: 4
num: 16
title: "Build a Complete Vision Pipeline — Capstone"
lesson_type: build
languages:
  - Python
time_min: 120
on_route: false
quiz_count: 5
code_files: 1
concepts: 8
prereqs: 15
community: 13
libraries:
  - numpy
  - pydantic
  - torch
aliases:
  - 04/16
  - 04-16
tags:
  - phase/04
  - type/build
  - community/13
source: ai-engineering-from-scratch/phases/04-computer-vision/16-vision-pipeline-capstone/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/16-vision-pipeline-capstone"
---

# 04/16 Build a Complete Vision Pipeline — Capstone

> A production vision system is a chain of models and rules stitched with data contracts. The pieces are already in this phase; the capstone wires them together end-to-end.

**Phase:** [[Phases/04 Computer Vision|Phase 4: Computer Vision]] · **Type:** Build · **Time:** 120 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/04-computer-vision/16-vision-pipeline-capstone/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/16-vision-pipeline-capstone) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/04-computer-vision/16-vision-pipeline-capstone) · code: main.py · quiz: 5 questions  
**Community:** [[Communities/13 Object Multiplex · Clip · Divided attention|13 Object Multiplex · Clip · Divided attention]] · **Libraries:** [[Libraries/numpy (python)|numpy]], [[Libraries/pydantic (python)|pydantic]], [[Libraries/torch (python)|torch]]  

## Prerequisites

Stated upstream: `Phase 4 Lessons 01-15`

- **04/01-15**:
    - [[Lessons/04-01 Image Fundamentals — Pixels, Channels, Color Spaces|04/01 Image Fundamentals — Pixels, Channels, Color Spaces]]
    - [[Lessons/04-02 Convolutions from Scratch|04/02 Convolutions from Scratch]]
    - [[Lessons/04-03 CNNs — LeNet to ResNet|04/03 CNNs — LeNet to ResNet]]
    - [[Lessons/04-04 Image Classification|04/04 Image Classification]]
    - [[Lessons/04-05 Transfer Learning & Fine-Tuning|04/05 Transfer Learning & Fine-Tuning]]
    - [[Lessons/04-06 Object Detection — YOLO from Scratch|04/06 Object Detection — YOLO from Scratch]]
    - [[Lessons/04-07 Semantic Segmentation — U-Net|04/07 Semantic Segmentation — U-Net]]
    - [[Lessons/04-08 Instance Segmentation — Mask R-CNN|04/08 Instance Segmentation — Mask R-CNN]]
    - [[Lessons/04-09 Image Generation — GANs|04/09 Image Generation — GANs]]
    - [[Lessons/04-10 Image Generation — Diffusion Models|04/10 Image Generation — Diffusion Models]]
    - [[Lessons/04-11 Stable Diffusion — Architecture & Fine-Tuning|04/11 Stable Diffusion — Architecture & Fine-Tuning]]
    - [[Lessons/04-12 Video Understanding — Temporal Modeling|04/12 Video Understanding — Temporal Modeling]]
    - [[Lessons/04-13 3D Vision — Point Clouds & NeRFs|04/13 3D Vision — Point Clouds & NeRFs]]
    - [[Lessons/04-14 Vision Transformers (ViT)|04/14 Vision Transformers (ViT)]]
    - [[Lessons/04-15 Real-Time Vision — Edge Deployment|04/15 Real-Time Vision — Edge Deployment]]

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/01-12 Tensor Operations|01/12 Tensor Operations]], [[Lessons/02-09 Model Evaluation|02/09 Model Evaluation]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/03-07 Regularization|03/07 Regularization]], [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]], [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/10-11 Quantization- Making Models Fit|10/11 Quantization: Making Models Fit]]
- depth 3: [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]], [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]], [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]], [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]], [[Lessons/01-13 Numerical Stability|01/13 Numerical Stability]], [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]], [[Lessons/02-02 Linear Regression|02/02 Linear Regression]], [[Lessons/02-03 Logistic Regression|02/03 Logistic Regression]], [[Lessons/02-04 Decision Trees and Random Forests|02/04 Decision Trees and Random Forests]], [[Lessons/02-05 Support Vector Machines|02/05 Support Vector Machines]], [[Lessons/02-06 K-Nearest Neighbors and Distances|02/06 K-Nearest Neighbors and Distances]], [[Lessons/02-07 Unsupervised Learning|02/07 Unsupervised Learning]], [[Lessons/02-08 Feature Engineering & Selection|02/08 Feature Engineering & Selection]], [[Lessons/03-01 The Perceptron|03/01 The Perceptron]], [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-04 Activation Functions|03/04 Activation Functions]], [[Lessons/03-05 Loss Functions|03/05 Loss Functions]], [[Lessons/03-08 Weight Initialization and Training Stability|03/08 Weight Initialization and Training Stability]], [[Lessons/03-09 Learning Rate Schedules and Warmup|03/09 Learning Rate Schedules and Warmup]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]], [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]], [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]], [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]], [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]], [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]], [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]], [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]], [[Lessons/10-08 DPO- Direct Preference Optimization|10/08 DPO: Direct Preference Optimization]], [[Lessons/10-09 Constitutional AI and Self-Improvement|10/09 Constitutional AI and Self-Improvement]], [[Lessons/10-10 Evaluation- Benchmarks, Evals, LM Harness|10/10 Evaluation: Benchmarks, Evals, LM Harness]]

## Concepts taught

- [[Concepts/Pipeline|Pipeline]] `lesson term` — An ordered chain of preprocessing, inference, and postprocessing steps with a typed interface between each pair
- Data contract `lesson term` — Pydantic / dataclass definitions that every stage input and output conforms to; catches integration bugs at the boundary
- Preprocessing `lesson term` — Decoding, colour conversion, resizing, normalising; usually the biggest CPU time sink
- Postprocessing `lesson term` — NMS, mask resize, threshold, RLE encode; cheap on GPU, expensive on CPU
- Microbatcher `lesson term` — Aggregator that waits a fixed window for multiple requests, runs a single batched forward pass
- Trace ID `lesson term` — Per-request identifier logged at every stage so slow requests can be traced end-to-end
- Failure code `lesson term` — Specific error code per failure class instead of generic 500; enables client retry logic
- [[Concepts/Health check|Health check]] `lesson term` — Cheap endpoint that reports whether the service can answer; loadbalancers rely on this

## Ships

- [[Artifacts/04-16 prompt-vision-service-shape-reviewer|prompt-vision-service-shape-reviewer]] `prompt` — Review a vision service's code for contract/response shape violations and name the first breaking bug
- [[Artifacts/04-16 skill-pipeline-budget-planner|skill-pipeline-budget-planner]] `skill` — Given target latency and throughput, assign a time budget to every pipeline stage and flag which stage will miss its budget first

## Further reading

- NVIDIA Triton Inference Server ([link](https://developer.nvidia.com/triton-inference-server)) — high-throughput serving with batching and multi-model support
- BentoML docs ([link](https://docs.bentoml.com)) — serving framework with batching, versioning, and metrics
- Full Stack Deep Learning — Deploying Models ([link](https://fullstackdeeplearning.com/course/2022/lecture-5-deployment/)) — the canonical overview of production ML deployment
- torchserve docs ([link](https://pytorch.org/serve/)) — PyTorch's official serving library


%% ── my notes ── %%
