---
id: "lesson:18/16"
type: lesson
ref: 18/16
phase: 18
num: 16
title: "Red-Team Tooling — Garak, Llama Guard, PyRIT"
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 6
code_files: 1
concepts: 7
prereqs: 4
community: 23
aliases:
  - 18/16
  - 18-16
tags:
  - phase/18
  - type/build
  - community/23
  - stdlib-only
source: ai-engineering-from-scratch/phases/18-ethics-safety-alignment/16-red-team-tooling-garak-llamaguard-pyrit/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/16-red-team-tooling-garak-llamaguard-pyrit"
---

# 18/16 Red-Team Tooling — Garak, Llama Guard, PyRIT

> Three production tools frame the 2026 red-team stack. Llama Guard (Meta) — a Llama-3.1-8B classifier fine-tuned on 14 MLCommons hazard categories; the 2025 Llama Guard 4 is a 12B natively multimodal classifier pruned from Llama 4 Scout. Garak (NVIDIA) — open-source LLM vulnerability scanner with static, dynamic, and adaptive probes for hallucination, data leakage, prompt injection, toxicity, and jailbreaks. PyRIT (Microsoft) — multi-turn red-team campaigns with Crescendo, TAP, and custom converter chains for deep exploitation. Llama Guard 3 is documented in Meta's "Llama 3 Herd of Models" (arXiv:2407.21783); Llama Guard 3-1B-INT4 in arXiv:2411.17713; Garak's probe architecture in github.com/NVIDIA/garak. These tools are the 2026 production interface between red-team research (Lessons 12-15) and deployment (Lesson 17+).

**Phase:** [[Phases/18 Ethics, Safety & Alignment|Phase 18: Ethics, Safety & Alignment]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/18-ethics-safety-alignment/16-red-team-tooling-garak-llamaguard-pyrit/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/16-red-team-tooling-garak-llamaguard-pyrit) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/18-ethics-safety-alignment/16-red-team-tooling-garak-llamaguard-pyrit) · code: main.py · quiz: 6 questions  
**Community:** [[Communities/23 Automatic Speech Recognition (ASR) · Llama Guard · Homoglyph|23 Automatic Speech Recognition (ASR) · Llama Guard · Homoglyph]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 18 · 12-15 (jailbreaks and IPI)`

- **18/12-15** — jailbreaks and IPI:
    - [[Lessons/18-12 Red-Teaming- PAIR and Automated Attacks|18/12 Red-Teaming: PAIR and Automated Attacks]]
    - [[Lessons/18-13 Many-Shot Jailbreaking|18/13 Many-Shot Jailbreaking]]
    - [[Lessons/18-14 ASCII Art and Visual Jailbreaks|18/14 ASCII Art and Visual Jailbreaks]]
    - [[Lessons/18-15 Indirect Prompt Injection — Production Attack Surface|18/15 Indirect Prompt Injection — Production Attack Surface]]

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]], [[Lessons/18-01 Instruction-Following as Alignment Signal|18/01 Instruction-Following as Alignment Signal]]
- depth 3: [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]], [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]], [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]], [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]], [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]], [[Lessons/10-08 DPO- Direct Preference Optimization|10/08 DPO: Direct Preference Optimization]]

## Builds on this

- [[Lessons/18-17 WMDP and Dual-Use Capability Evaluation|18/17 WMDP and Dual-Use Capability Evaluation]]
- [[Lessons/18-28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR|18/28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR]]
- [[Lessons/18-29 Moderation Systems — OpenAI, Perspective, Llama Guard|18/29 Moderation Systems — OpenAI, Perspective, Llama Guard]]

## Concepts taught

- [[Concepts/Llama Guard|Llama Guard]] `lesson term` — Fine-tuned Llama-3.1-8B/4-12B safety classifier with 14 hazard categories
- Garak `lesson term` — NVIDIA open-source vulnerability scanner; probes, detectors, harnesses
- PyRIT `lesson term` — Microsoft multi-turn red-team orchestrator; converters, orchestrators, scoring
- Prompt-Guard `lesson term` — Meta's 86M prompt-injection classifier, paired with Llama Guard
- TBSA `lesson term` — Garak's tier-based pass/fail replacing binary outcomes
- Converter chain `lesson term` — PyRIT composition primitive for building multi-step attacks
- MLCommons hazard categories `lesson term` — Industry-standard taxonomy Llama Guard targets

## Ships

- [[Artifacts/18-16 red-team-stack|red-team-stack]] `skill` — Recommend a red-team tool stack and configuration for a given deployment.

## Further reading

- [[Resources/Llama 3 paper (Meta, 2024)|Llama 3 paper (Meta, 2024)]] ([link](https://arxiv.org/abs/2407.21783)) — the 8B classifier ·  also cited by 7 other lessons
- Meta — Llama Guard 3-1B-INT4 (arXiv:2411.17713) ([link](https://arxiv.org/abs/2411.17713)) — quantized mobile classifier
- [[Resources/Microsoft PyRIT — GitHub|Microsoft PyRIT — GitHub]] ([link](https://github.com/Azure/PyRIT)) — the campaign toolkit ·  also cited by 1 other lesson
- [[Resources/NVIDIA Garak — GitHub|NVIDIA Garak — GitHub]] ([link](https://github.com/NVIDIA/garak)) — the scanner repo and documentation ·  also cited by 1 other lesson


%% ── my notes ── %%
