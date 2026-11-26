---
id: "lesson:18/14"
type: lesson
ref: 18/14
phase: 18
num: 14
title: ASCII Art and Visual Jailbreaks
lesson_type: build
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 6
code_files: 1
concepts: 7
prereqs: 2
community: 23
aliases:
  - 18/14
  - 18-14
tags:
  - phase/18
  - type/build
  - community/23
  - stdlib-only
source: ai-engineering-from-scratch/phases/18-ethics-safety-alignment/14-ascii-art-visual-jailbreaks/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/14-ascii-art-visual-jailbreaks"
---

# 18/14 ASCII Art and Visual Jailbreaks

> Jiang, Xu, Niu, Xiang, Ramasubramanian, Li, Poovendran, "ArtPrompt: ASCII Art-based Jailbreak Attacks against Aligned LLMs" (ACL 2024, arXiv:2402.11753). Mask the safety-relevant tokens in a harmful request, replace them with ASCII-art renderings of the same letters, and send the cloaked prompt. GPT-3.5, GPT-4, Gemini, Claude, Llama-2 all fail to robustly recognize ASCII-art tokens. The attack bypasses PPL (perplexity filters), Paraphrase defenses, and Retokenization. Related: the ViTC benchmark measures recognition of non-semantic visual prompts; StructuralSleight generalizes to Uncommon Text-Encoded Structures (trees, graphs, nested JSON) as a family of encoding attacks.

**Phase:** [[Phases/18 Ethics, Safety & Alignment|Phase 18: Ethics, Safety & Alignment]] · **Type:** Build · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/18-ethics-safety-alignment/14-ascii-art-visual-jailbreaks/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/14-ascii-art-visual-jailbreaks) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/18-ethics-safety-alignment/14-ascii-art-visual-jailbreaks) · code: main.py · quiz: 6 questions  
**Community:** [[Communities/23 Automatic Speech Recognition (ASR) · Llama Guard · Homoglyph|23 Automatic Speech Recognition (ASR) · Llama Guard · Homoglyph]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 18 · 12 (PAIR), Phase 18 · 13 (MSJ)`

- [[Lessons/18-12 Red-Teaming- PAIR and Automated Attacks|18/12 Red-Teaming: PAIR and Automated Attacks]] — PAIR
- [[Lessons/18-13 Many-Shot Jailbreaking|18/13 Many-Shot Jailbreaking]] — MSJ

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]], [[Lessons/18-01 Instruction-Following as Alignment Signal|18/01 Instruction-Following as Alignment Signal]]
- depth 3: [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]], [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]], [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]], [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]], [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]], [[Lessons/10-08 DPO- Direct Preference Optimization|10/08 DPO: Direct Preference Optimization]]

## Builds on this

- [[Lessons/18-16 Red-Team Tooling — Garak, Llama Guard, PyRIT|18/16 Red-Team Tooling — Garak, Llama Guard, PyRIT]]
- [[Lessons/18-28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR|18/28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR]]

## Concepts taught

- ArtPrompt `lesson term` — Two-step jailbreak that masks safety words with ASCII-art renderings
- Cloaking `lesson term` — Replace a forbidden token with a visual representation the model reads but the filter does not
- UTES `lesson term` — Uncommon Text-Encoded Structure — tree, graph, nested JSON, etc. used to smuggle content
- ViTC `lesson term` — Benchmark for model's ability to read non-semantic visual encoding
- [[Concepts/Perplexity filter|Perplexity filter]] `lesson term` — Reject prompts with high perplexity; fails because legitimate structured input also scores high
- Retokenization `lesson term` — Pre-process the prompt with a different tokenizer; fails because recognition is visual
- [[Concepts/Homoglyph|Homoglyph]] `lesson term` — Unicode characters that look identical to Latin letters; bypass substring checks

## Ships

- [[Artifacts/18-14 encoding-audit|encoding-audit]] `skill` — Audit a jailbreak-defense report across encoding-family attacks.

## Further reading

- [[Resources/Anil, Durmus, Panickssery et al. — Many-shot Jailbreaking (Anthropic, NeurIPS 2024)|Anil, Durmus, Panickssery et al. — Many-shot Jailbreaking (Anthropic, NeurIPS 2024)]] ([link](https://www.anthropic.com/research/many-shot-jailbreaking)) — complementary length attack ·  also cited by 1 other lesson
- [[Resources/Chao et al. — Jailbreaking Black Box LLMs in Twenty Queries (arXiv-2310.08419)|Chao et al. — Jailbreaking Black Box LLMs in Twenty Queries (arXiv:2310.08419)]] ([link](https://arxiv.org/abs/2310.08419)) — complementary iterative attack ·  also cited by 3 other lessons
- Jiang et al. — ArtPrompt (ACL 2024, arXiv:2402.11753) ([link](https://arxiv.org/abs/2402.11753)) — the ASCII-art jailbreak paper
- Li et al. — StructuralSleight (arXiv:2406.08754) ([link](https://arxiv.org/abs/2406.08754)) — UTES generalization


%% ── my notes ── %%
