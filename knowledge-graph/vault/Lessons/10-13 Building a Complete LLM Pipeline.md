---
id: "lesson:10/13"
type: lesson
ref: 10/13
phase: 10
num: 13
title: Building a Complete LLM Pipeline
lesson_type: build
languages:
  - Python
time_min: 120
status: planned
status_auto: planned
on_route: true
route_order: 13
quiz_count: 0
code_files: 1
concepts: 10
prereqs: 12
community: 1
aliases:
  - 10/13
  - 10-13
tags:
  - phase/10
  - type/build
  - status/planned
  - route
  - community/01
  - stdlib-only
source: ai-engineering-from-scratch/phases/10-llms-from-scratch/13-building-complete-llm-pipeline/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/10-llms-from-scratch/13-building-complete-llm-pipeline"
---

# 10/13 Building a Complete LLM Pipeline

> Everything from Lessons 01 to 12 is one stage of one pipeline. This lesson is the scaffold that turns those stages into a single end-to-end run: tokenize, pre-train, scale, SFT, align, evaluate, quantize, serve. You will not train a 70B model on a laptop. You will produce the orchestration layer, the manifest, the eval gate, and the rollback plan that a 2026 frontier team uses to decide what gets shipped. This is the capstone.

**Phase:** [[Phases/10 LLMs from Scratch|Phase 10: LLMs from Scratch]] · **Type:** Build · **Time:** 120 min · **Languages:** Python · **Status:** planned  
**Open:** [[Upstream/10-llms-from-scratch/13-building-complete-llm-pipeline/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/10-llms-from-scratch/13-building-complete-llm-pipeline) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/10-llms-from-scratch/13-building-complete-llm-pipeline) · code: main.py  
**Community:** [[Communities/01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism|01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `All Phase 10 lessons 01-12`

- **10/01-12**:
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
    - [[Lessons/10-11 Quantization- Making Models Fit|10/11 Quantization: Making Models Fit]]
    - [[Lessons/10-12 Inference Optimization|10/12 Inference Optimization]]

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]], [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/01-13 Numerical Stability|01/13 Numerical Stability]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/07-12 KV Cache, Flash Attention & Inference Optimization|07/12 KV Cache, Flash Attention & Inference Optimization]], [[Lessons/09-01 MDPs, States, Actions & Rewards|09/01 MDPs, States, Actions & Rewards]], [[Lessons/09-06 Policy Gradient — REINFORCE from Scratch|09/06 Policy Gradient — REINFORCE from Scratch]], [[Lessons/09-08 Proximal Policy Optimization (PPO)|09/08 Proximal Policy Optimization (PPO)]], [[Lessons/19-76 Collective Ops From Scratch|19/76 Collective Ops From Scratch]]
- depth 3: [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]], [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]], [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]], [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]], [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]], [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]], [[Lessons/03-05 Loss Functions|03/05 Loss Functions]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]], [[Lessons/07-07 GPT — Causal Language Modeling|07/07 GPT — Causal Language Modeling]], [[Lessons/09-03 Monte Carlo Methods — Learning from Complete Episodes|09/03 Monte Carlo Methods — Learning from Complete Episodes]], [[Lessons/09-04 Temporal Difference — Q-Learning & SARSA|09/04 Temporal Difference — Q-Learning & SARSA]], [[Lessons/09-07 Actor-Critic — A2C and A3C|09/07 Actor-Critic — A2C and A3C]], [[Lessons/19-42 Large Corpus Downloader|19/42 Large Corpus Downloader]], [[Lessons/19-43 HDF5 Tokenized Corpus|19/43 HDF5 Tokenized Corpus]], [[Lessons/19-44 Cosine LR with Linear Warmup|19/44 Cosine LR with Linear Warmup]], [[Lessons/19-45 Gradient Clipping and Mixed Precision|19/45 Gradient Clipping and Mixed Precision]], [[Lessons/19-46 Gradient Accumulation|19/46 Gradient Accumulation]], [[Lessons/19-47 Checkpoint Save and Resume|19/47 Checkpoint Save and Resume]], [[Lessons/19-48 Distributed Data Parallel and FSDP from Scratch|19/48 Distributed Data Parallel and FSDP from Scratch]], [[Lessons/19-49 Language Model Evaluation Harness|19/49 Language Model Evaluation Harness]]

## Builds on this

- [[Lessons/17-07 Hardware-Specialized Inference Compilation — FP8 and NVFP4 on Blackwell|17/07 Hardware-Specialized Inference Compilation — FP8 and NVFP4 on Blackwell]]
- [[Lessons/17-09 Production Quantization — AWQ, GPTQ, GGUF K-quants, FP8, MXFP4-NVFP4|17/09 Production Quantization — AWQ, GPTQ, GGUF K-quants, FP8, MXFP4/NVFP4]]

## Concepts taught

- [[Concepts/Manifest|Manifest]] `lesson term` — YAML or JSON describing pipeline version, seed, per-stage config, and gate thresholds — sufficient to replay a run
- Content-addressed `lesson term` — Artifacts stored by SHA-256 of their contents, so you can never confuse version A with version B
- Eval gate `lesson term` — Numeric thresholds on benchmark metrics and safety scores that must pass before an artifact is marked shippable
- [[Concepts/KL budget|KL budget]] `lesson term` — reference) across alignment stages, enforced as a gate
- [[Concepts/MFU|MFU]] `lesson term` — Model FLOPs Utilization — achieved FLOPs divided by theoretical peak. 40% is typical at 70B scale, 55% at 7B
- [[Concepts/Rollback plan|Rollback plan]] `lesson term` — Pre-written set of actions per stage on failure: re-run, fall back, retrain with revised inputs
- [[Concepts/Orchestrator|Orchestrator]] `lesson term` — The process that reads the manifest, dispatches stages, verifies hashes, halts on any contract violation
- Artifact store `lesson term` — Immutable content-addressed object store — single source of truth for checkpoints, datasets, eval reports
- Reproducible `lesson term` — Different bit-level weights but equivalent downstream metrics — the realistic target for distributed LLM training
- Cost gate `lesson term` — Pre-run cost estimate plus in-run tracker — the pipeline refuses to start if the estimate exceeds budget

## Ships

- [[Artifacts/10-13 llm-pipeline-reviewer|llm-pipeline-reviewer]] `skill` — Review an end-to-end LLM training pipeline manifest before a multi-million-dollar run.

## Further reading

- [[Resources/Kaplan et al. (2020). Scaling Laws for Neural Language Models|Kaplan et al. (2020). Scaling Laws for Neural Language Models]] ([link](https://arxiv.org/abs/2001.08361)) — the original compute-data-params scaling relationship ·  also cited by 1 other lesson
- [[Resources/Hoffmann et al. (2022). Training Compute-Optimal Large Language Models|Hoffmann et al. (2022). Training Compute-Optimal Large Language Models]] ([link](https://arxiv.org/abs/2203.15556)) — the correction to Kaplan that recalibrated modern data budgets ·  also cited by 2 other lessons
- [[Resources/Llama 3 paper (Meta, 2024)|Llama 3 paper (Meta, 2024)]] ([link](https://arxiv.org/abs/2407.21783)) — the most detailed public description of a frontier pipeline including data, training, alignment, eval ·  also cited by 7 other lessons
- [[Resources/DeepSeek-AI (2024). DeepSeek-V3 Technical Report|DeepSeek-AI (2024). DeepSeek-V3 Technical Report]] ([link](https://arxiv.org/abs/2412.19437)) — efficiency-first pipeline at roughly 1/10th the cost of Llama 3 class training ·  also cited by 7 other lessons
- [[Resources/PyTorch FSDP2 documentation|PyTorch FSDP2 documentation]] ([link](https://pytorch.org/docs/stable/fsdp.html)) — the distributed training primitive replacing FSDP1 in PyTorch 2.4+ ·  also cited by 1 other lesson
- Weights & Biases LLM Reports ([link](https://wandb.ai/site/llms)) — real manifests and experiment tracker output for open-source LLM runs, useful as plagiarizable templates

## My route

- Step 13 in *Route: Phase 10 core (about 20 h, plus bridges)*
- Plan note: Complete LLM pipeline (capstone)
- Previous: [[Lessons/10-12 Inference Optimization|10/12 Inference Optimization]]
- Next: [[Lessons/10-14 Open Models- Architecture Walkthroughs|10/14 Open Models: Architecture Walkthroughs]]


%% ── my notes ── %%
