---
id: "lesson:07/02"
type: lesson
ref: 07/02
phase: 7
num: 2
title: Self-Attention from Scratch
lesson_type: build
languages:
  - Python
time_min: 90
on_route: false
quiz_count: 5
code_files: 3
concepts: 9
prereqs: 1
community: 12
libraries:
  - numpy
aliases:
  - 07/02
  - 07-02
tags:
  - phase/07
  - type/build
  - community/12
source: ai-engineering-from-scratch/phases/07-transformers-deep-dive/02-self-attention-from-scratch/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/07-transformers-deep-dive/02-self-attention-from-scratch"
---

# 07/02 Self-Attention from Scratch

> Attention is a lookup table where every word asks "who matters to me?" - and learns the answer.

**Phase:** [[Phases/07 Transformers Deep Dive|Phase 7: Transformers Deep Dive]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/07-transformers-deep-dive/02-self-attention-from-scratch/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/07-transformers-deep-dive/02-self-attention-from-scratch) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/07-transformers-deep-dive/02-self-attention-from-scratch) · code: main.jl, main.rs, self_attention.py · quiz: 5 questions  
**Community:** [[Communities/12 Attention · Cross-Attention · Self-Attention|12 Attention · Cross-Attention · Self-Attention]] · **Libraries:** [[Libraries/numpy (python)|numpy]]  

## Prerequisites

Stated upstream: `Phase 3 (Deep Learning Core), Phase 5 Lesson 10 (Sequence-to-Sequence)`

- [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]] — Sequence-to-Sequence
- Whole phase: [[Phases/03 Deep Learning Core|Phase 3: Deep Learning Core]] — Deep Learning Core ·  medium confidence

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/05-09 Sequence-to-Sequence Models|05/09 Sequence-to-Sequence Models]]
- depth 3: [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]], [[Lessons/05-08 CNNs and RNNs for Text|05/08 CNNs and RNNs for Text]]

## Builds on this

- [[Lessons/04-11 Stable Diffusion — Architecture & Fine-Tuning|04/11 Stable Diffusion — Architecture & Fine-Tuning]]
- [[Lessons/04-14 Vision Transformers (ViT)|04/14 Vision Transformers (ViT)]]
- [[Lessons/04-19 OCR & Document Understanding|04/19 OCR & Document Understanding]]
- [[Lessons/04-23 Diffusion Transformers & Rectified Flow|04/23 Diffusion Transformers & Rectified Flow]]
- [[Lessons/04-25 Vision-Language Models — The ViT-MLP-LLM Pattern|04/25 Vision-Language Models — The ViT-MLP-LLM Pattern]]
- [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]]
- [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]]
- [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]]
- [[Lessons/07-07 GPT — Causal Language Modeling|07/07 GPT — Causal Language Modeling]]
- [[Lessons/07-12 KV Cache, Flash Attention & Inference Optimization|07/12 KV Cache, Flash Attention & Inference Optimization]]
- [[Lessons/07-14 Build a Transformer from Scratch — The Capstone|07/14 Build a Transformer from Scratch — The Capstone]]
- [[Lessons/07-15 Attention Variants — Sliding Window, Sparse, Differential|07/15 Attention Variants — Sliding Window, Sparse, Differential]]
- [[Lessons/10-16 Differential Attention (V2)|10/16 Differential Attention (V2)]]

## Concepts taught

- Query (as *Query (Q)*) `lesson term` — A learned projection of the input that represents what information this token is looking for
- Key (as *Key (K)*) `lesson term` — A learned projection that represents what information this token contains, matched against queries
- [[Concepts/Value|Value]] (as *Value (V)*) `lesson term` — A learned projection carrying the actual information that gets aggregated based on attention scores
- Scaled dot-product attention `lesson term` — softmax(QK^T / sqrt(dk)) @ V - scaling prevents softmax saturation in high dimensions
- [[Concepts/Self-Attention|Self-Attention]] `glossary` — Attention where Q, K, V all come from the same sequence, letting every position attend to every other position
- Attention weights `lesson term` — A probability distribution over positions, produced by softmax over scaled dot products
- [[Concepts/Multi-head attention|Multi-head attention]] `lesson term` — Running multiple attention functions with different projections, then concatenating results for richer representations
- [[Concepts/Attention|Attention]] `glossary` — A mechanism that forms contextual representations by comparing query vectors with key vectors, normalizing the resulting scores, and using them to combine value vectors. Masks, position rules, or sparse patterns can restrict which positions participate.

## Ships

- [[Artifacts/07-02 prompt-attention-explainer|prompt-attention-explainer]] `prompt` — Explain the attention mechanism through the database lookup analogy

## Further reading

- [[Resources/Attention Is All You Need|Attention Is All You Need]] ([link](https://arxiv.org/abs/1706.03762)) — the original transformer paper ·  also cited by 8 other lessons
- [[Resources/The Illustrated Transformer|The Illustrated Transformer]] ([link](https://jalammar.github.io/illustrated-transformer/)) — best visual walkthrough of the full architecture ·  also cited by 1 other lesson
- [[Resources/The Annotated Transformer (Harvard NLP)|The Annotated Transformer (Harvard NLP)]] ([link](https://nlp.seas.harvard.edu/annotated-transformer/)) — line-by-line PyTorch implementation with explanations ·  also cited by 1 other lesson


%% ── my notes ── %%
