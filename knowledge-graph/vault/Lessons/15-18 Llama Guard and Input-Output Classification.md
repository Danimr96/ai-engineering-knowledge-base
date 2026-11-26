---
id: "lesson:15/18"
type: lesson
ref: 15/18
phase: 15
num: 18
title: Llama Guard and Input/Output Classification
lesson_type: learn
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 2
community: 23
aliases:
  - 15/18
  - 15-18
tags:
  - phase/15
  - type/learn
  - community/23
  - stdlib-only
source: ai-engineering-from-scratch/phases/15-autonomous-systems/18-llama-guard/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/15-autonomous-systems/18-llama-guard"
---

# 15/18 Llama Guard and Input/Output Classification

> Llama Guard 3 (Meta, Llama-3.1-8B base, fine-tuned for content safety) classifies both LLM inputs and outputs against an MLCommons 13-hazard taxonomy across 8 languages. A 1B-INT4 quantized variant runs at over 30 tokens/sec on mobile CPUs. Llama Guard 4 is multimodal (image + text), expands to the S1–S14 category set (including S14 Code Interpreter Abuse), and is a drop-in replacement for Llama Guard 3 8B/11B. NVIDIA NeMo Guardrails v0.20.0 (January 2026) adds Colang dialog-flow rails on top of input and output rails. The honest note: "Bypassing Prompt Injection and Jailbreak Detection in LLM Guardrails" (Huang et al., arXiv:2504.11168) showed Emoji Smuggling hit 100% attack success rate on six prominent guard systems; NeMo Guard Detect recorded 72.54% ASR on jailbreaks. Classifiers are a layer, not a solution.

**Phase:** [[Phases/15 Autonomous Systems|Phase 15: Autonomous Systems]] · **Type:** Learn · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/15-autonomous-systems/18-llama-guard/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/15-autonomous-systems/18-llama-guard) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/15-autonomous-systems/18-llama-guard) · code: main.py  
**Community:** [[Communities/23 Automatic Speech Recognition (ASR) · Llama Guard · Homoglyph|23 Automatic Speech Recognition (ASR) · Llama Guard · Homoglyph]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 15 · 10 (Permission modes), Phase 15 · 17 (Constitution)`

- [[Lessons/15-10 Permission Modes for Autonomous Agents|15/10 Permission Modes for Autonomous Agents]] — Permission modes
- [[Lessons/15-17 Constitutional AI and Rule Overrides|15/17 Constitutional AI and Rule Overrides]] — Constitution

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/15-01 The Shift from Chatbots to Long-Horizon Agents|15/01 The Shift from Chatbots to Long-Horizon Agents]], [[Lessons/15-06 Automated Alignment Research (Anthropic AAR)|15/06 Automated Alignment Research (Anthropic AAR)]], [[Lessons/15-09 The Autonomous Coding Agent Landscape (2026)|15/09 The Autonomous Coding Agent Landscape (2026)]]
- depth 3: [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]], [[Lessons/14-07 Agent Memory — Virtual Context and Memory Paging|14/07 Agent Memory — Virtual Context and Memory Paging]], [[Lessons/15-04 Darwin Godel Machine — Open-Ended Self-Modifying Agents|15/04 Darwin Godel Machine — Open-Ended Self-Modifying Agents]], [[Lessons/15-05 AI Scientist v2 — Workshop-Level Autonomous Research|15/05 AI Scientist v2 — Workshop-Level Autonomous Research]]

## Concepts taught

- [[Concepts/Llama Guard|Llama Guard]] `lesson term` — Llama-3.1-8B fine-tuned for input/output classification
- MLCommons taxonomy `lesson term` — Shared vocabulary for content-safety categories
- S1–S14 `lesson term` — Expanded taxonomy; S14 is Code Interpreter Abuse
- [[Concepts/NeMo Guardrails|NeMo Guardrails]] `lesson term` — Input + output + dialog rails; Colang for flows
- Emoji Smuggling `lesson term` — Non-printable emoji between chars; 100% ASR on six guards
- [[Concepts/Homoglyph|Homoglyph]] `lesson term` — Cyrillic for Latin; classifier trained on English misses
- [[Concepts/Automatic Speech Recognition (ASR)|Automatic Speech Recognition (ASR)]] (as *ASR*) `glossary` — Fraction of attacks that bypass the classifier
- Dialog rail `lesson term` — Conversation-level rule that persists across turns

## Ships

- [[Artifacts/15-18 classifier-stack-audit|classifier-stack-audit]] `skill` — Audit a deployment's input/output classifier stack (model, taxonomy, input rails, output rails, dialog rails) and flag adversarial-attack gaps.

## Further reading

- Inan et al. — Llama Guard: LLM-based Input-Output Safeguard ([link](https://ai.meta.com/research/publications/llama-guard-llm-based-input-output-safeguard-for-human-ai-conversations/)) — the original paper.
- [[Resources/Anthropic — Measuring AI agent autonomy in practice|Anthropic — Measuring AI agent autonomy in practice]] ([link](https://www.anthropic.com/research/measuring-agent-autonomy)) — classifier-plus-runtime framing. ·  also cited by 16 other lessons
- Huang et al. — Bypassing Prompt Injection and Jailbreak Detection in LLM Guardrails ([link](https://arxiv.org/abs/2504.11168)) — ASR numbers across guard systems.
- NVIDIA NeMo Guardrails (GitHub) ([link](https://github.com/NVIDIA-NeMo/Guardrails)) — v0.20.0 January 2026.
- [[Resources/Meta — Llama Guard 4 model card|Meta — Llama Guard 4 model card]] ([link](https://www.llama.com/docs/model-cards-and-prompt-formats/llama-guard-4/)) — multimodal, S1–S14 taxonomy. ·  also cited by 2 other lessons


%% ── my notes ── %%
