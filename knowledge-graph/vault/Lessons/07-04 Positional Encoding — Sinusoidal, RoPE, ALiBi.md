---
id: "lesson:07/04"
type: lesson
ref: 07/04
phase: 7
num: 4
title: "Positional Encoding — Sinusoidal, RoPE, ALiBi"
lesson_type: build
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 0
code_files: 3
concepts: 8
prereqs: 2
community: 94
aliases:
  - 07/04
  - 07-04
tags:
  - phase/07
  - type/build
  - community/94
  - stdlib-only
source: ai-engineering-from-scratch/phases/07-transformers-deep-dive/04-positional-encoding/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/07-transformers-deep-dive/04-positional-encoding"
---

# 07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi

> Attention is permutation-invariant. "The cat sat on the mat" and "mat the on sat cat the" produce the same output without positional signal. Three algorithms fix it — each with a different bet on what "position" means.

**Phase:** [[Phases/07 Transformers Deep Dive|Phase 7: Transformers Deep Dive]] · **Type:** Build · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/07-transformers-deep-dive/04-positional-encoding/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/07-transformers-deep-dive/04-positional-encoding) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/07-transformers-deep-dive/04-positional-encoding) · code: main.jl, main.py, main.rs  
**Community:** [[Communities/94 Positional encoding · RoPE · YaRN|94 Positional encoding · RoPE · YaRN]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 7 · 02 (Self-Attention), Phase 7 · 03 (Multi-Head Attention)`

- [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]] — Self-Attention
- [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]] — Multi-Head Attention

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]]
- depth 3: [[Lessons/05-09 Sequence-to-Sequence Models|05/09 Sequence-to-Sequence Models]]

## Builds on this

- [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]]
- [[Lessons/07-14 Build a Transformer from Scratch — The Capstone|07/14 Build a Transformer from Scratch — The Capstone]]

## Concepts taught

- [[Concepts/Positional encoding|Positional encoding]] `lesson term` — Any signal added to embeddings or attention that encodes position.
- Sinusoidal `lesson term` — sin/cos at geometric frequencies added to embeddings; doesn't extrapolate.
- [[Concepts/RoPE|RoPE]] `lesson term` — Rotate Q, K by position-dependent angle; dot product encodes relative distance.
- ALiBi `lesson term` — Add -m·|i-j| to attention scores; no embedding needed, great extrapolation.
- base `lesson term` — The frequency scaler in RoPE; increase to extend context at inference.
- NTK-aware `lesson term` — Rescale base so high-frequency dims aren't squeezed when context expands.
- [[Concepts/YaRN|YaRN]] `lesson term` — Per-dimension interpolation+extrapolation that preserves attention entropy.
- Extrapolation `lesson term` — Can the position scheme serve correct output past max_len seen in training?

## Ships

- [[Artifacts/07-04 positional-encoding-picker|positional-encoding-picker]] `skill` — Pick positional encoding (RoPE, ALiBi, sinusoidal) + scaling strategy given context length and training budget.

## Further reading

- [[Resources/Attention Is All You Need|Attention Is All You Need]] ([link](https://arxiv.org/abs/1706.03762)) — original sinusoidal. ·  also cited by 8 other lessons
- [[Resources/Su et al.- RoFormer (2021)|Su et al.: RoFormer (2021)]] ([link](https://arxiv.org/abs/2104.09864)) — RoPE paper. ·  also cited by 3 other lessons
- Press, Smith, Lewis (2021). Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation ([link](https://arxiv.org/abs/2108.12409)) — ALiBi.
- Chen et al. (2023). Extending Context Window of Large Language Models via Positional Interpolation ([link](https://arxiv.org/abs/2306.15595)) — Meta's Llama 2 long-context paper.
- Peng et al. (2023). YaRN: Efficient Context Window Extension of Large Language Models ([link](https://arxiv.org/abs/2309.00071)) — state of the art RoPE scaling.
- Ding et al. (2024). LongRoPE: Extending LLM Context Window Beyond 2 Million Tokens ([link](https://arxiv.org/abs/2402.13753)) — the Microsoft method used by Phi-3-Long and cited in the Use It section.
- HuggingFace Transformers — `modeling_rope_utils.py` ([link](https://github.com/huggingface/transformers/blob/main/src/transformers/modeling_rope_utils.py)) — production-grade implementations of every RoPE scaling scheme (default, linear, dynamic, YaRN, LongRoPE, Llama-3).


%% ── my notes ── %%
