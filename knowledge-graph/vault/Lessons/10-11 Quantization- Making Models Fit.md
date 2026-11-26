---
id: "lesson:10/11"
type: lesson
ref: 10/11
phase: 10
num: 11
title: "Quantization: Making Models Fit"
lesson_type: build
languages:
  - Python
time_min: 120
status: planned
status_auto: planned
on_route: true
route_order: 11
quiz_count: 0
code_files: 2
concepts: 14
prereqs: 10
community: 1
libraries:
  - numpy
aliases:
  - 10/11
  - 10-11
tags:
  - phase/10
  - type/build
  - status/planned
  - route
  - community/01
source: ai-engineering-from-scratch/phases/10-llms-from-scratch/11-quantization/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/10-llms-from-scratch/11-quantization"
---

# 10/11 Quantization: Making Models Fit

> A 70B model in FP16 needs 140GB. Two A100s just for weights. Quantize to FP8: one 80GB GPU. INT4: a MacBook.

**Phase:** [[Phases/10 LLMs from Scratch|Phase 10: LLMs from Scratch]] · **Type:** Build · **Time:** 120 min · **Languages:** Python · **Status:** planned  
**Open:** [[Upstream/10-llms-from-scratch/11-quantization/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/10-llms-from-scratch/11-quantization) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/10-llms-from-scratch/11-quantization) · code: main.py, main.rs  
**Community:** [[Communities/01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism|01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism]] · **Libraries:** [[Libraries/numpy (python)|numpy]]  

## Prerequisites

Stated upstream: `Phase 10, Lessons 01-10 (LLMs from Scratch)`

- **10/01-10** — LLMs from Scratch:
    - [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]]
    - [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]]
    - [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]]
    - [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]]
    - [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]]
    - [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]]
    - [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]]
    - [[Lessons/10-08 DPO- Direct Preference Optimization|10/08 DPO: Direct Preference Optimization]]
    - [[Lessons/10-09 Constitutional AI and Self-Improvement|10/09 Constitutional AI and Self-Improvement]]
    - [[Lessons/10-10 Evaluation- Benchmarks, Evals, LM Harness|10/10 Evaluation: Benchmarks, Evals, LM Harness]]

### Bridges to check first (my plan)

- [[Lessons/01-13 Numerical Stability|01/13 Numerical Stability]] — numerical stability (floating-point formats)

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]], [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]], [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]], [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]], [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]], [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/09-01 MDPs, States, Actions & Rewards|09/01 MDPs, States, Actions & Rewards]], [[Lessons/09-06 Policy Gradient — REINFORCE from Scratch|09/06 Policy Gradient — REINFORCE from Scratch]], [[Lessons/09-08 Proximal Policy Optimization (PPO)|09/08 Proximal Policy Optimization (PPO)]], [[Lessons/19-76 Collective Ops From Scratch|19/76 Collective Ops From Scratch]]
- depth 3: [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]], [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]], [[Lessons/03-05 Loss Functions|03/05 Loss Functions]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]], [[Lessons/09-03 Monte Carlo Methods — Learning from Complete Episodes|09/03 Monte Carlo Methods — Learning from Complete Episodes]], [[Lessons/09-04 Temporal Difference — Q-Learning & SARSA|09/04 Temporal Difference — Q-Learning & SARSA]], [[Lessons/09-07 Actor-Critic — A2C and A3C|09/07 Actor-Critic — A2C and A3C]], [[Lessons/19-42 Large Corpus Downloader|19/42 Large Corpus Downloader]], [[Lessons/19-43 HDF5 Tokenized Corpus|19/43 HDF5 Tokenized Corpus]], [[Lessons/19-44 Cosine LR with Linear Warmup|19/44 Cosine LR with Linear Warmup]], [[Lessons/19-45 Gradient Clipping and Mixed Precision|19/45 Gradient Clipping and Mixed Precision]], [[Lessons/19-46 Gradient Accumulation|19/46 Gradient Accumulation]], [[Lessons/19-47 Checkpoint Save and Resume|19/47 Checkpoint Save and Resume]], [[Lessons/19-48 Distributed Data Parallel and FSDP from Scratch|19/48 Distributed Data Parallel and FSDP from Scratch]], [[Lessons/19-49 Language Model Evaluation Harness|19/49 Language Model Evaluation Harness]]

## Builds on this

- [[Lessons/04-15 Real-Time Vision — Edge Deployment|04/15 Real-Time Vision — Edge Deployment]]
- [[Lessons/06-13 Neural Audio Codecs — EnCodec, SNAC, Mimi, DAC and the Semantic-Acoustic Split|06/13 Neural Audio Codecs — EnCodec, SNAC, Mimi, DAC and the Semantic-Acoustic Split]]
- [[Lessons/10-13 Building a Complete LLM Pipeline|10/13 Building a Complete LLM Pipeline]]

## Concepts taught

- [[Concepts/fp16|fp16]] `lesson term` — 16-bit float with 5 exponent bits and 10 mantissa bits, max value 65,504, standard inference format
- BF16 `lesson term` — 16-bit float with 8 exponent bits (same range as FP32) and 7 mantissa bits, designed by Google for training
- [[Concepts/FP8|FP8]] `lesson term` — Two variants: E4M3 (inference, more precision) and E5M2 (training, more range), native on H100
- INT8 `lesson term` — 256 uniformly spaced values from -128 to 127, needs a scale factor to map from floats
- INT4 `lesson term` — 16 levels total, requires sophisticated methods (GPTQ, AWQ) to maintain quality
- Per-channel quantization `lesson term` — Uses a separate scale factor for each output channel instead of one for the whole tensor, dramatically reduces error
- [[Concepts/GPTQ|GPTQ]] `lesson term` — Post-training quantization using second-order information to minimize output error, one layer at a time
- [[Concepts/AWQ|AWQ]] `lesson term` — Scales salient weights (those multiplied by large activations) before quantization to protect them
- [[Concepts/GGUF|GGUF]] `lesson term` — Self-contained model file with mixed-precision layers, optimized for CPU and Apple Silicon inference
- [[Concepts/PTQ|PTQ]] `lesson term` — Convert a trained model's weights to lower precision without retraining, fast but limited at extreme compression
- [[Concepts/QAT|QAT]] `lesson term` — Insert fake quantization into the forward pass so the model learns to tolerate rounding, better at INT4/INT2
- Calibration data `lesson term` — A small dataset run through the model to compute activation statistics for setting scale factors
- Scale factor `lesson term` — Converts between floating-point range and integer range: float_val = int_val scale
- Perplexity delta `lesson term` — Difference in perplexity between original and quantized model, < 0.5 is excellent, > 2.0 is a problem

## Ships

- [[Artifacts/10-11 skill-quantization|skill-quantization]] `skill` — Choose the right quantization strategy for deploying LLMs based on hardware, quality, and latency constraints

## Further reading

- Dettmers et al., 2022 -- "LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale ([link](https://arxiv.org/abs/2208.07339)) — mixed-precision INT8 that keeps outlier features in FP16, enabling INT8 inference without quality loss
- Micikevicius et al., 2022 -- "FP8 Formats for Deep Learning ([link](https://arxiv.org/abs/2209.05433)) — the NVIDIA/ARM/Intel paper defining E4M3 and E5M2 formats now native on H100
- [[Resources/Frantar et al., 2022 - -GPTQ- Accurate Post-Training Quantization for Generative Pre-trained Transformers|Frantar et al., 2022 -- "GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers]] ([link](https://arxiv.org/abs/2210.17323)) — the paper that made INT4 quantization practical for LLMs using Hessian-guided weight rounding ·  also cited by 1 other lesson
- Xiao et al., 2023 -- "SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models ([link](https://arxiv.org/abs/2211.10438)) — migrating quantization difficulty from activations to weights for W8A8 deployment
- [[Resources/Lin et al., 2023 - -AWQ- Activation-aware Weight Quantization for LLM Compression and Acceleration|Lin et al., 2023 -- "AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration]] ([link](https://arxiv.org/abs/2306.00978)) — protecting salient weights by scaling before quantization, matching or beating GPTQ ·  also cited by 1 other lesson

## My route

- Step 11 in *Route: Phase 10 core (about 20 h, plus bridges)*
- Plan note: Quantization
- Previous: [[Lessons/10-10 Evaluation- Benchmarks, Evals, LM Harness|10/10 Evaluation: Benchmarks, Evals, LM Harness]]
- Next: [[Lessons/10-12 Inference Optimization|10/12 Inference Optimization]]


%% ── my notes ── %%
