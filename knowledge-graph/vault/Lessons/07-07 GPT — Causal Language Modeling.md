---
id: "lesson:07/07"
type: lesson
ref: 07/07
phase: 7
num: 7
title: "GPT — Causal Language Modeling"
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 0
code_files: 1
concepts: 9
prereqs: 3
community: 5
aliases:
  - 07/07
  - 07-07
tags:
  - phase/07
  - type/build
  - community/05
  - stdlib-only
source: ai-engineering-from-scratch/phases/07-transformers-deep-dive/07-gpt-causal-language-modeling/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/07-transformers-deep-dive/07-gpt-causal-language-modeling"
---

# 07/07 GPT — Causal Language Modeling

> BERT sees both sides. GPT sees only the past. The triangle mask is the most consequential single line of code in modern AI.

**Phase:** [[Phases/07 Transformers Deep Dive|Phase 7: Transformers Deep Dive]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/07-transformers-deep-dive/07-gpt-causal-language-modeling/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/07-transformers-deep-dive/07-gpt-causal-language-modeling) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/07-transformers-deep-dive/07-gpt-causal-language-modeling) · code: main.py  
**Community:** [[Communities/05 Temperature · Autoregressive · Logits|05 Temperature · Autoregressive · Logits]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 7 · 02 (Self-Attention), Phase 7 · 05 (Full Transformer), Phase 7 · 06 (BERT)`

- [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]] — Self-Attention
- [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]] — Full Transformer
- [[Lessons/07-06 BERT — Masked Language Modeling|07/06 BERT — Masked Language Modeling]] — BERT

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/05-02 Bag of Words, TF-IDF, and Text Representation|05/02 Bag of Words, TF-IDF, and Text Representation]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]]
- depth 3: [[Lessons/02-02 Linear Regression|02/02 Linear Regression]], [[Lessons/05-01 Text Processing — Tokenization, Stemming, Lemmatization|05/01 Text Processing — Tokenization, Stemming, Lemmatization]], [[Lessons/05-09 Sequence-to-Sequence Models|05/09 Sequence-to-Sequence Models]]

## Builds on this

- [[Lessons/07-08 T5, BART — Encoder-Decoder Models|07/08 T5, BART — Encoder-Decoder Models]]
- [[Lessons/07-11 Mixture of Experts (MoE)|07/11 Mixture of Experts (MoE)]]
- [[Lessons/07-12 KV Cache, Flash Attention & Inference Optimization|07/12 KV Cache, Flash Attention & Inference Optimization]]
- [[Lessons/07-13 Scaling Laws|07/13 Scaling Laws]]
- [[Lessons/07-14 Build a Transformer from Scratch — The Capstone|07/14 Build a Transformer from Scratch — The Capstone]]
- [[Lessons/07-16 Speculative Decoding — Draft, Verify, Repeat|07/16 Speculative Decoding — Draft, Verify, Repeat]]

## Concepts taught

- [[Concepts/Causal mask|Causal mask]] `lesson term` — Upper-triangular -inf matrix added to attention scores so position i only sees positions ≤ i.
- [[Concepts/Next-token prediction|Next-token prediction]] `lesson term` — Cross-entropy of the model's distribution against the true next token at every position.
- [[Concepts/Autoregressive|Autoregressive]] `glossary` — Feed output back as input; parallelism only during training, not during generation.
- [[Concepts/Logits|Logits]] `glossary` — Raw output of the LM head before softmax; sampling happens on these.
- [[Concepts/Temperature|Temperature]] `glossary` — Divide logits by T; T→0 = greedy, T→∞ = uniform.
- [[Concepts/Nucleus Sampling (Top-p)|Nucleus Sampling (Top-p)]] (as *Top-p*) `glossary` — Truncate distribution to smallest set summing to ≥p; sample from what remains.
- Min-p `lesson term` — Keep tokens where p ≥ min_p × max_p; adapts cutoff to sharpness of distribution.
- [[Concepts/Speculative Decoding|Speculative Decoding]] `glossary` — Cheap model proposes N tokens; big model verifies in parallel.
- [[Concepts/Teacher forcing|Teacher forcing]] `lesson term` — During training, feed the true previous token, not the model's prediction. Standard for every seq2seq LM.

## Ships

- [[Artifacts/07-07 sampling-tuner|sampling-tuner]] `skill` — Pick decoding strategy (greedy / temperature / top-k / top-p / min-p / speculative) for a given generation task.

## Further reading

- Language Models are Few-Shot Learners ([link](https://arxiv.org/abs/2005.14165)) — GPT-3 and in-context learning.
- [[Resources/Leviathan, Kalman, Matias (2023). Fast Inference from Transformers via Speculative Decoding|Leviathan, Kalman, Matias (2023). Fast Inference from Transformers via Speculative Decoding]] ([link](https://arxiv.org/abs/2211.17192)) — spec decoding paper. ·  also cited by 7 other lessons
- [[Resources/Radford et al. (2019). Language Models are Unsupervised Multitask Learners|Radford et al. (2019). Language Models are Unsupervised Multitask Learners]] ([link](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)) — GPT-2. ·  also cited by 1 other lesson
- Radford et al. (2018). Improving Language Understanding by Generative Pre-Training ([link](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf)) — GPT-1.
- [[Resources/HuggingFace `modeling_llama.py`|HuggingFace `modeling_llama.py`]] ([link](https://github.com/huggingface/transformers/blob/main/src/transformers/models/llama/modeling_llama.py)) — canonical causal-LM reference code. ·  also cited by 1 other lesson


%% ── my notes ── %%
