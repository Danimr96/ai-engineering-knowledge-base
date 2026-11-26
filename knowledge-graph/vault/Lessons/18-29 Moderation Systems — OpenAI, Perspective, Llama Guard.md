---
id: "lesson:18/29"
type: lesson
ref: 18/29
phase: 18
num: 29
title: "Moderation Systems — OpenAI, Perspective, Llama Guard"
lesson_type: build
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 6
code_files: 1
concepts: 7
prereqs: 1
community: 23
aliases:
  - 18/29
  - 18-29
tags:
  - phase/18
  - type/build
  - community/23
  - stdlib-only
source: ai-engineering-from-scratch/phases/18-ethics-safety-alignment/29-moderation-systems-openai-perspective-llamaguard/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/29-moderation-systems-openai-perspective-llamaguard"
---

# 18/29 Moderation Systems — OpenAI, Perspective, Llama Guard

> Production moderation systems operationalize the safety policies defined in Lessons 12-16. OpenAI Moderation API: `omni-moderation-latest` (2024) built on GPT-4o classifies text + images in one call; 42% better on multilingual test set than prior version; the response schema returns 13 category booleans — harassment, harassment/threatening, hate, hate/threatening, illicit, illicit/violent, self-harm, self-harm/intent, self-harm/instructions, sexual, sexual/minors, violence, violence/graphic; free for most developers. Layered patterns: Input moderation (pre-generation), Output moderation (post-generation), Custom moderation (domain rules). Async parallel calls hide latency; placeholder responses on flag. Llama Guard 3/4 (Lesson 16): 14 MLCommons hazards, Code Interpreter Abuse, 8 languages (v3), multi-image (v4). Perspective API (Google Jigsaw): toxicity scoring predating the LLM-as-moderator wave; primarily single-dimension toxicity with severe-toxicity/insult/profanity variants; baseline for content-moderation research. Deprecations: Azure Content Moderator deprecated February 2024, retired February 2027, replaced by Azure AI Content Safety.

**Phase:** [[Phases/18 Ethics, Safety & Alignment|Phase 18: Ethics, Safety & Alignment]] · **Type:** Build · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/18-ethics-safety-alignment/29-moderation-systems-openai-perspective-llamaguard/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/29-moderation-systems-openai-perspective-llamaguard) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/18-ethics-safety-alignment/29-moderation-systems-openai-perspective-llamaguard) · code: main.py · quiz: 6 questions  
**Community:** [[Communities/23 Automatic Speech Recognition (ASR) · Llama Guard · Homoglyph|23 Automatic Speech Recognition (ASR) · Llama Guard · Homoglyph]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 18 · 16 (Llama Guard / Garak / PyRIT)`

- [[Lessons/18-16 Red-Team Tooling — Garak, Llama Guard, PyRIT|18/16 Red-Team Tooling — Garak, Llama Guard, PyRIT]] — Llama Guard / Garak / PyRIT

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/18-12 Red-Teaming- PAIR and Automated Attacks|18/12 Red-Teaming: PAIR and Automated Attacks]], [[Lessons/18-13 Many-Shot Jailbreaking|18/13 Many-Shot Jailbreaking]], [[Lessons/18-14 ASCII Art and Visual Jailbreaks|18/14 ASCII Art and Visual Jailbreaks]], [[Lessons/18-15 Indirect Prompt Injection — Production Attack Surface|18/15 Indirect Prompt Injection — Production Attack Surface]]
- depth 3: [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]], [[Lessons/18-01 Instruction-Following as Alignment Signal|18/01 Instruction-Following as Alignment Signal]]

## Concepts taught

- OpenAI Moderation `lesson term` — GPT-4o-based 13-category (text) classifier with partial multimodal support
- Perspective API `lesson term` — Pre-LLM-era toxicity scoring baseline
- [[Concepts/Llama Guard|Llama Guard]] `lesson term` — Meta's hazard classifier (v3: 8B text, 8 langs; v4: 12B multimodal)
- Input moderation `lesson term` — Classifier on user prompt before model call
- Output moderation `lesson term` — Classifier on model output before delivery
- Custom moderation `lesson term` — Deployment-specific rules (regex, allowlist, policy)
- Layered moderation `lesson term` — Standard production deployment pattern

## Ships

- [[Artifacts/18-29 moderation-stack|moderation-stack]] `skill` — Recommend a moderation stack configuration for a production deployment.

## Further reading

- Meta PurpleLlama + Llama Guard ([link](https://github.com/meta-llama/PurpleLlama)) — Llama Guard repo
- Azure AI Content Safety ([link](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/)) — Azure replacement
- Google Jigsaw Perspective API ([link](https://perspectiveapi.com/)) — toxicity scoring
- OpenAI Moderation API docs ([link](https://platform.openai.com/docs/api-reference/moderations)) — omni-moderation endpoint


%% ── my notes ── %%
