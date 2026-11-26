---
id: "lesson:11/08"
type: lesson
ref: 11/08
phase: 11
num: 8
title: "Fine-Tuning with LoRA & QLoRA"
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 0
code_files: 1
concepts: 13
prereqs: 1
community: 48
libraries:
  - torch
aliases:
  - 11/08
  - 11-08
tags:
  - phase/11
  - type/build
  - community/48
source: ai-engineering-from-scratch/phases/11-llm-engineering/08-fine-tuning-lora/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/11-llm-engineering/08-fine-tuning-lora"
---

# 11/08 Fine-Tuning with LoRA & QLoRA

> Full fine-tuning a 7B model requires 56GB of VRAM. You don't have that. Neither do most companies. LoRA lets you fine-tune the same model in 6GB by training less than 1% of the parameters. This isn't a compromise -- it matches full fine-tuning quality on most tasks. The entire open-source fine-tuning ecosystem runs on this one trick.

**Phase:** [[Phases/11 LLM Engineering|Phase 11: LLM Engineering]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/11-llm-engineering/08-fine-tuning-lora/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/11-llm-engineering/08-fine-tuning-lora) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/11-llm-engineering/08-fine-tuning-lora) · code: lora.py  
**Community:** [[Communities/48 Fine-tuning · QLoRA · LoRA (Low-Rank Adaptation)|48 Fine-tuning · QLoRA · LoRA (Low-Rank Adaptation)]] · **Libraries:** [[Libraries/torch (python)|torch]]  

## Prerequisites

Stated upstream: `Phase 10, Lesson 06 (Instruction Tuning / SFT)`

- [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]] — Instruction Tuning / SFT

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]]
- depth 3: [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]], [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]], [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]]

## Builds on this

- [[Lessons/11-13 Building a Production LLM Application|11/13 Building a Production LLM Application]]

## Concepts taught

- [[Concepts/LoRA (Low-Rank Adaptation)|LoRA (Low-Rank Adaptation)]] (as *LoRA*) `glossary` — Low-Rank Adaptation: freeze base weights, train two small matrices A and B whose product approximates the full weight update
- [[Concepts/QLoRA|QLoRA]] `glossary` — Quantized LoRA: load the base model in 4-bit NF4, train LoRA adapters in fp16 on top, enabling 7B fine-tuning in 6GB VRAM
- [[Concepts/Rank|Rank]] (as *Rank (r)*) `lesson term` — The inner dimension of the A and B matrices; controls expressiveness vs. parameter count
- Alpha `lesson term` — Scaling factor applied to the LoRA output; alpha/r scales the adaptation's contribution to the final output
- NF4 `lesson term` — Normal Float 4: a 4-bit data type with quantization levels at normal distribution quantiles, optimal for neural network weights
- [[Concepts/Adapter|Adapter]] `lesson term` — The LoRA A and B matrices saved as a separate file (10-100MB), loadable on top of any copy of the base model
- Target modules `lesson term` — The specific linear layers (q_proj, v_proj, etc.) where LoRA adapters are injected
- Merging `lesson term` — Computing W + (alpha/r) BA and replacing the original weight, eliminating the adapter overhead at inference
- Paged optimizers `lesson term` — Offloading optimizer states (Adam momentum, variance) to CPU when GPU memory is exhausted
- [[Concepts/Catastrophic forgetting|Catastrophic forgetting]] `lesson term` — When updating all weights causes the model to lose previously learned capabilities
- [[Concepts/Fine-tuning|Fine-tuning]] `glossary` — Continuing training from pretrained parameters on a narrower dataset or objective. Depending on the method, you may update all parameters, selected parameters, or added adapter parameters.

## Ships

- [[Artifacts/11-08 prompt-lora-advisor|prompt-lora-advisor]] `prompt` — Decide LoRA rank, target modules, and hyperparameters for a specific fine-tuning task
- [[Artifacts/11-08 skill-fine-tuning-guide|skill-fine-tuning-guide]] `skill` — Decision tree for when and how to fine-tune LLMs with LoRA and QLoRA

## Further reading

- [[Resources/Direct Preference Optimization paper|Direct Preference Optimization paper]] ([link](https://arxiv.org/abs/2305.18290)) — DPO derivation; the preference-tuning stage that comes after SFT, no reward model needed. ·  also cited by 3 other lessons
- [[Resources/Axolotl documentation|Axolotl documentation]] ([link](https://axolotl-ai-cloud.github.io/axolotl/)) — YAML-configured multi-GPU SFT/DPO/QLoRA trainer; the config-as-code alternative to hand-written scripts. ·  also cited by 1 other lesson
- Unsloth documentation ([link](https://docs.unsloth.ai/)) — fused kernels that double fine-tuning throughput and halve memory; the performance layer under TRL.
- [[Resources/Hugging Face TRL library|Hugging Face TRL library]] ([link](https://huggingface.co/docs/trl)) — official reference for `SFTTrainer`, `DPOTrainer`, `KTOTrainer`, and the integration surface with PEFT/bitsandbytes/Unsloth. ·  also cited by 2 other lessons


%% ── my notes ── %%
