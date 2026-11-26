---
id: "lesson:10/04"
type: lesson
ref: 10/04
phase: 10
num: 4
title: Pre-Training a Mini GPT (124M Parameters)
lesson_type: build
languages:
  - Python
time_min: 120
status: planned
status_auto: planned
on_route: true
route_order: 4
quiz_count: 0
code_files: 2
concepts: 10
prereqs: 3
community: 1
libraries:
  - numpy
aliases:
  - 10/04
  - 10-04
tags:
  - phase/10
  - type/build
  - status/planned
  - route
  - community/01
source: ai-engineering-from-scratch/phases/10-llms-from-scratch/04-pre-training-mini-gpt/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/10-llms-from-scratch/04-pre-training-mini-gpt"
---

# 10/04 Pre-Training a Mini GPT (124M Parameters)

> GPT-2 Small has 124 million parameters. That's 12 transformer layers, 12 attention heads, and 768-dimensional embeddings. You can train it from scratch on a single GPU in a few hours. Most people never do this. They use pre-trained checkpoints. But if you don't train one yourself, you don't actually understand what's happening inside the model you're building products on.

**Phase:** [[Phases/10 LLMs from Scratch|Phase 10: LLMs from Scratch]] · **Type:** Build · **Time:** 120 min · **Languages:** Python · **Status:** planned  
**Open:** [[Upstream/10-llms-from-scratch/04-pre-training-mini-gpt/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/10-llms-from-scratch/04-pre-training-mini-gpt) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/10-llms-from-scratch/04-pre-training-mini-gpt) · code: main.py, main.rs  
**Community:** [[Communities/01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism|01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism]] · **Libraries:** [[Libraries/numpy (python)|numpy]]  

## Prerequisites

Stated upstream: `Phase 10, Lessons 01-03 (Tokenizers, Building a Tokenizer, Data Pipelines)`

- **10/01-03** — Tokenizers, Building a Tokenizer, Data Pipelines:
    - [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]]
    - [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]]
    - [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]]

### Bridges to check first (my plan)

- [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]] — chain rule and autodiff
- [[Lessons/01-09 Information Theory|01/09 Information Theory]] — information theory (cross-entropy)
- [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]] — backprop
- [[Lessons/03-06 Optimizers|03/06 Optimizers]] — optimizers (Adam)
- [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]] — self-attention
- [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]] — multi-head
- [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]] — positional encoding
- [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]] — full transformer

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]], [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]], [[Lessons/03-05 Loss Functions|03/05 Loss Functions]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]]
- depth 3: [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]], [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]], [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]], [[Lessons/03-01 The Perceptron|03/01 The Perceptron]], [[Lessons/03-04 Activation Functions|03/04 Activation Functions]], [[Lessons/05-09 Sequence-to-Sequence Models|05/09 Sequence-to-Sequence Models]]

## Builds on this

- [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]]
- [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]]
- [[Lessons/10-10 Evaluation- Benchmarks, Evals, LM Harness|10/10 Evaluation: Benchmarks, Evals, LM Harness]]
- [[Lessons/10-11 Quantization- Making Models Fit|10/11 Quantization: Making Models Fit]]
- [[Lessons/10-12 Inference Optimization|10/12 Inference Optimization]]
- [[Lessons/10-13 Building a Complete LLM Pipeline|10/13 Building a Complete LLM Pipeline]]
- [[Lessons/10-14 Open Models- Architecture Walkthroughs|10/14 Open Models: Architecture Walkthroughs]]
- [[Lessons/10-18 Multi-Token Prediction (MTP)|10/18 Multi-Token Prediction (MTP)]]
- [[Lessons/10-25 Speculative Decoding and EAGLE|10/25 Speculative Decoding and EAGLE]]
- [[Lessons/10-34 Gradient Checkpointing and Activation Recomputation|10/34 Gradient Checkpointing and Activation Recomputation]]
- [[Lessons/11-01 Prompt Engineering- Techniques & Patterns|11/01 Prompt Engineering: Techniques & Patterns]]
- [[Lessons/11-03 Structured Outputs- JSON, Schema Validation, Constrained Decoding|11/03 Structured Outputs: JSON, Schema Validation, Constrained Decoding]]
- [[Lessons/18-13 Many-Shot Jailbreaking|18/13 Many-Shot Jailbreaking]]
- [[Lessons/18-23 Watermarking — SynthID, Stable Signature, C2PA|18/23 Watermarking — SynthID, Stable Signature, C2PA]]

## Concepts taught

- [[Concepts/Autoregressive|Autoregressive]] `glossary` — Each output token is conditioned on all previous tokens -- the model predicts P(token_n | token_0, ..., token{n-1})
- [[Concepts/Causal mask|Causal mask]] `lesson term` — An upper-triangular matrix of -infinity values that prevents attention to future positions during training
- [[Concepts/Multi-head attention|Multi-head attention]] `lesson term` — Splitting Q, K, V into parallel heads (e.g., 12 heads of 64 dims each for GPT-2) so each head can learn different relationship types
- [[Concepts/KV Cache|KV Cache]] `glossary` — Storing computed Key and Value tensors from previous tokens to avoid redundant computation during autoregressive generation
- [[Concepts/Prefill|Prefill]] `glossary` — The first inference phase where all prompt tokens are processed in parallel -- compute-bound on GPU FLOPS
- [[Concepts/Decode|Decode]] `lesson term` — The second inference phase where tokens are generated one at a time -- memory-bound on GPU bandwidth
- [[Concepts/Weight tying|Weight tying]] `lesson term` — Using the same matrix for input token embeddings and the output projection head -- saves 38M params in GPT-2
- [[Concepts/Residual connection|Residual connection]] `lesson term` — Adding the input directly to the output of a sublayer (x + sublayer(x)) -- enables gradient flow in deep networks
- [[Concepts/Layer normalization|Layer normalization]] `lesson term` — Normalizing across the feature dimension to mean 0 and variance 1, with learnable scale and bias parameters
- Cross-entropy loss `lesson term` — -log(probability assigned to the correct next token), averaged over all positions -- the standard LLM training objective

## Ships

- [[Artifacts/10-04 prompt-gpt-architecture-analyzer|prompt-gpt-architecture-analyzer]] `prompt` — Analyze architecture choices in any GPT-style transformer model

## Further reading

- [[Resources/Attention Is All You Need|Attention Is All You Need]] ([link](https://arxiv.org/abs/1706.03762)) — the original transformer paper with scaled dot-product attention and multi-head attention ·  also cited by 8 other lessons
- [[Resources/Pope et al., 2022 - -Efficiently Scaling Transformer Inference|Pope et al., 2022 -- "Efficiently Scaling Transformer Inference]] ([link](https://arxiv.org/abs/2211.05102)) — the paper that formalized prefill vs decode and KV cache analysis ·  also cited by 2 other lessons
- [[Resources/Llama 3 paper (Meta, 2024)|Llama 3 paper (Meta, 2024)]] ([link](https://arxiv.org/abs/2407.21783)) — how Meta scaled the GPT architecture to 405B parameters with 16K GPUs ·  also cited by 7 other lessons
- [[Resources/Radford et al. (2019). Language Models are Unsupervised Multitask Learners|Radford et al. (2019). Language Models are Unsupervised Multitask Learners]] ([link](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)) — the GPT-2 paper that introduced the 124M to 1.5B parameter family ·  also cited by 1 other lesson

## My route

- Step 4 in *Route: Phase 10 core (about 20 h, plus bridges)*
- Plan note: **Pre-training a mini GPT** (numpy, backward pass written by hand)
- Previous: [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]]
- Next: [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]]


%% ── my notes ── %%
