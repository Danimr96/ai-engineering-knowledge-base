---
id: "lesson:18/13"
type: lesson
ref: 18/13
phase: 18
num: 13
title: Many-Shot Jailbreaking
lesson_type: learn
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 6
code_files: 1
concepts: 7
prereqs: 2
community: 23
aliases:
  - 18/13
  - 18-13
tags:
  - phase/18
  - type/learn
  - community/23
  - stdlib-only
source: ai-engineering-from-scratch/phases/18-ethics-safety-alignment/13-many-shot-jailbreaking/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/13-many-shot-jailbreaking"
---

# 18/13 Many-Shot Jailbreaking

> Anil, Durmus, Panickssery, Sharma, et al. (Anthropic, NeurIPS 2024). Many-shot jailbreaking (MSJ) exploits long context windows: stuff hundreds of faux user-assistant turns where the assistant complies with harmful requests, then append the target query. Attack success follows a power law in the number of shots; fails at 5 shots, reliable at 256 shots on violent and deceitful content. The phenomenon follows the same power law as benign in-context learning — the attack and ICL share an underlying mechanism, which is why defenses that preserve ICL are hard to design. Classifier-based prompt modification reduces attack success from 61% to 2% on tested settings.

**Phase:** [[Phases/18 Ethics, Safety & Alignment|Phase 18: Ethics, Safety & Alignment]] · **Type:** Learn · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/18-ethics-safety-alignment/13-many-shot-jailbreaking/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/13-many-shot-jailbreaking) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/18-ethics-safety-alignment/13-many-shot-jailbreaking) · code: main.py · quiz: 6 questions  
**Community:** [[Communities/23 Automatic Speech Recognition (ASR) · Llama Guard · Homoglyph|23 Automatic Speech Recognition (ASR) · Llama Guard · Homoglyph]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 18 · 12 (PAIR), Phase 10 · 04 (in-context learning)`

- [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]] — in-context learning
- [[Lessons/18-12 Red-Teaming- PAIR and Automated Attacks|18/12 Red-Teaming: PAIR and Automated Attacks]] — PAIR

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]], [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]], [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]], [[Lessons/18-01 Instruction-Following as Alignment Signal|18/01 Instruction-Following as Alignment Signal]]
- depth 3: [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]], [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]], [[Lessons/03-05 Loss Functions|03/05 Loss Functions]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]], [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]], [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]], [[Lessons/10-08 DPO- Direct Preference Optimization|10/08 DPO: Direct Preference Optimization]]

## Builds on this

- [[Lessons/18-14 ASCII Art and Visual Jailbreaks|18/14 ASCII Art and Visual Jailbreaks]]
- [[Lessons/18-16 Red-Team Tooling — Garak, Llama Guard, PyRIT|18/16 Red-Team Tooling — Garak, Llama Guard, PyRIT]]
- [[Lessons/18-28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR|18/28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR]]

## Concepts taught

- MSJ `lesson term` — Long-context attack with hundreds of faux user-assistant compliance pairs
- Shot count `lesson term` — Number of faux compliance pairs before the target query
- Power-law ASR `lesson term` — Attack success rate grows polynomially, not sigmoidally, in shot count
- ICL `lesson term` — Model extracts task structure from in-context examples
- Pattern defense `lesson term` — Defense that detects MSJ structure before the model sees it
- Context-window exploit `lesson term` — Attacks that exist because context windows are long
- Compositional attack `lesson term` — Combination of MSJ with other attack families; often strictly stronger

## Ships

- [[Artifacts/18-13 msj-audit|msj-audit]] `skill` — Audit a long-context safety evaluation for many-shot jailbreaking coverage.

## Further reading

- [[Resources/Anil, Durmus, Panickssery et al. — Many-shot Jailbreaking (Anthropic, NeurIPS 2024)|Anil, Durmus, Panickssery et al. — Many-shot Jailbreaking (Anthropic, NeurIPS 2024)]] ([link](https://www.anthropic.com/research/many-shot-jailbreaking)) — the canonical paper and power-law results ·  also cited by 1 other lesson
- [[Resources/Universal and Transferable Adversarial Attacks on Aligned Language Models|Universal and Transferable Adversarial Attacks on Aligned Language Models]] ([link](https://arxiv.org/abs/2307.15043)) — white-box gradient attack, complementary to MSJ ·  also cited by 1 other lesson
- [[Resources/Chao et al. — Jailbreaking Black Box LLMs in Twenty Queries (arXiv-2310.08419)|Chao et al. — Jailbreaking Black Box LLMs in Twenty Queries (arXiv:2310.08419)]] ([link](https://arxiv.org/abs/2310.08419)) — the iterative attack MSJ composes with ·  also cited by 3 other lessons
- [[Resources/Mazeika et al. — HarmBench (ICML 2024)|Mazeika et al. — HarmBench (ICML 2024)]] ([link](https://arxiv.org/abs/2402.04249)) — evaluation benchmark for MSJ + other attacks ·  also cited by 1 other lesson


%% ── my notes ── %%
