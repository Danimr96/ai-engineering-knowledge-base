---
id: "lesson:10/06"
type: lesson
ref: 10/06
phase: 10
num: 6
title: Instruction Tuning (SFT)
lesson_type: build
languages:
  - Python
time_min: 90
status: planned
status_auto: planned
on_route: true
route_order: 6
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 1
community: 1
libraries:
  - numpy
aliases:
  - 10/06
  - 10-06
tags:
  - phase/10
  - type/build
  - status/planned
  - route
  - community/01
source: ai-engineering-from-scratch/phases/10-llms-from-scratch/06-instruction-tuning-sft/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/10-llms-from-scratch/06-instruction-tuning-sft"
---

# 10/06 Instruction Tuning (SFT)

> A base model predicts the next token. That's it. It doesn't follow instructions, answer questions, or refuse harmful requests. SFT is the bridge between a token predictor and a useful assistant. Every model you've ever talked to -- Claude, GPT, Llama Chat -- went through this step.

**Phase:** [[Phases/10 LLMs from Scratch|Phase 10: LLMs from Scratch]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** planned  
**Open:** [[Upstream/10-llms-from-scratch/06-instruction-tuning-sft/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/10-llms-from-scratch/06-instruction-tuning-sft) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/10-llms-from-scratch/06-instruction-tuning-sft) · code: main.py  
**Community:** [[Communities/01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism|01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism]] · **Libraries:** [[Libraries/numpy (python)|numpy]]  

## Prerequisites

Stated upstream: `Phase 10, Lesson 04 (Pre-Training a Mini GPT)`

- [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]] — Pre-Training a Mini GPT

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]], [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]], [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]]
- depth 3: [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]], [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]], [[Lessons/03-05 Loss Functions|03/05 Loss Functions]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]]

## Builds on this

- [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]]
- [[Lessons/10-09 Constitutional AI and Self-Improvement|10/09 Constitutional AI and Self-Improvement]]
- [[Lessons/10-11 Quantization- Making Models Fit|10/11 Quantization: Making Models Fit]]
- [[Lessons/10-12 Inference Optimization|10/12 Inference Optimization]]
- [[Lessons/10-13 Building a Complete LLM Pipeline|10/13 Building a Complete LLM Pipeline]]
- [[Lessons/11-08 Fine-Tuning with LoRA & QLoRA|11/08 Fine-Tuning with LoRA & QLoRA]]
- [[Lessons/18-01 Instruction-Following as Alignment Signal|18/01 Instruction-Following as Alignment Signal]]

## Concepts taught

- [[Concepts/SFT (Supervised Fine-Tuning)|SFT (Supervised Fine-Tuning)]] (as *SFT*) `glossary` — Supervised Fine-Tuning: continuing training on (instruction, response) pairs with loss computed only on response tokens
- Instruction tuning `lesson term` — Training on explicit instruction-response pairs so the base model learns the conversation pattern, not new knowledge
- Loss masking `lesson term` — Setting loss to zero for instruction tokens so gradients only flow from response token predictions
- ChatML `lesson term` — A token format using <|im_start|> and <|im_end|> delimiters to mark speaker roles in conversation data
- Alpaca format `lesson term` — A JSON format with instruction/input/output fields, used for 52K GPT-3.5-generated examples that cost $600
- [[Concepts/Catastrophic forgetting|Catastrophic forgetting]] `lesson term` — Fine-tuning destroys pre-trained capabilities because gradient updates overwrite general knowledge with task-specific patterns
- [[Concepts/Weight tying|Weight tying]] `lesson term` — Using the same matrix for input token embeddings and output prediction head, saving parameters and improving coherence
- [[Concepts/Chat template|Chat template]] `lesson term` — The specific token sequence (role markers, delimiters) that structures a conversation for the model

## Ships

- [[Artifacts/10-06 prompt-sft-data-curator|prompt-sft-data-curator]] `prompt` — Design and curate instruction datasets for supervised fine-tuning

## Further reading

- [[Resources/InstructGPT paper|InstructGPT paper]] ([link](https://arxiv.org/abs/2203.02155)) — the paper that introduced instruction tuning + RLHF at OpenAI ·  also cited by 4 other lessons
- Zhou et al., 2023 -- "LIMA: Less Is More for Alignment ([link](https://arxiv.org/abs/2305.11206)) — proving that 1,000 carefully curated examples can match SFT on much larger datasets
- [[Resources/Touvron et al., 2023 - Llama 2- Open Foundation and Fine-Tuned Chat Models|Touvron et al., 2023 -- Llama 2: Open Foundation and Fine-Tuned Chat Models]] ([link](https://arxiv.org/abs/2307.09288)) — Meta's SFT + RLHF pipeline with 27K high-quality examples ·  also cited by 1 other lesson
- Taori et al., 2023 -- "Stanford Alpaca: An Instruction-following LLaMA Model ([link](https://github.com/tatsu-lab/stanford_alpaca)) — 52K instruction examples for $600, proving SFT works on small datasets
- Chiang et al., 2023 -- "Vicuna: An Open-Source Chatbot Impressing GPT-4 ([link](https://lmsys.org/blog/2023-03-30-vicuna/)) — training on 70K ShareGPT conversations

## My route

- Step 6 in *Route: Phase 10 core (about 20 h, plus bridges)*
- Plan note: Instruction tuning (SFT)
- Previous: [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]]
- Next: [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]]


%% ── my notes ── %%
