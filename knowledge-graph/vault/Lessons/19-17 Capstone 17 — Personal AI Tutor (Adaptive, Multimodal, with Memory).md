---
id: "lesson:19/17"
type: lesson
ref: 19/17
phase: 19
num: 17
title: "Capstone 17 — Personal AI Tutor (Adaptive, Multimodal, with Memory)"
lesson_type: capstone
languages:
  - Python
  - TypeScript
  - SQL
time_min: 1800
on_route: false
quiz_count: 7
code_files: 8
concepts: 7
prereqs: 0
libraries:
  - hono
aliases:
  - 19/17
  - 19-17
tags:
  - phase/19
  - type/capstone
  - stdlib-only
source: ai-engineering-from-scratch/phases/19-capstone-projects/17-personal-ai-tutor/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/17-personal-ai-tutor"
---

# 19/17 Capstone 17 — Personal AI Tutor (Adaptive, Multimodal, with Memory)

> Khanmigo (Khan Academy), Duolingo Max, Google LearnLM / Gemini for Education, Quizlet Q-Chat, and Synthesis Tutor all shipped adaptive multimodal tutoring at scale in 2026. The common shape is a Socratic policy (never just dump the answer), a learner model that updates after every interaction (Bayesian knowledge tracing style), voice + text + photo-math input, curriculum graph retrieval, spaced-repetition scheduling, and hard safety filters for age-appropriate content. The capstone is to ship a subject-specific tutor (K-12 algebra or intro Python), run a two-week efficacy study with 10 learners, and pass a content-safety audit.

**Phase:** [[Phases/19 Capstone Projects|Phase 19: Capstone Projects]] · **Type:** Capstone · **Time:** 1800 min · **Languages:** Python, TypeScript, SQL · **Status:** —  
**Open:** [[Upstream/19-capstone-projects/17-personal-ai-tutor/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/17-personal-ai-tutor) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/19-capstone-projects/17-personal-ai-tutor) · code: main.py, ts/src/curriculum.ts, ts/src/index.ts, ts/src/mastery.ts, ts/src/repetition.ts, ts/src/server.ts … · quiz: 7 questions  
**Libraries:** [[Libraries/hono (typescript)|hono]]  

## Prerequisites

Stated upstream: `Phase 5 (NLP), Phase 6 (speech), Phase 11 (LLM engineering), Phase 12 (multimodal), Phase 14 (agents), Phase 17 (infrastructure), Phase 18 (safety)`

- Whole phase: [[Phases/11 LLM Engineering|Phase 11: LLM Engineering]] — LLM engineering ·  medium confidence
- Whole phase: [[Phases/12 Multimodal AI|Phase 12: Multimodal AI]] — multimodal ·  medium confidence
- Whole phase: [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] — agents ·  medium confidence
- Whole phase: [[Phases/17 Infrastructure & Production|Phase 17: Infrastructure & Production]] — infrastructure ·  medium confidence
- Whole phase: [[Phases/18 Ethics, Safety & Alignment|Phase 18: Ethics, Safety & Alignment]] — safety ·  medium confidence
- Whole phase: [[Phases/05 NLP, Foundations to Advanced|Phase 5: NLP, Foundations to Advanced]] — NLP ·  medium confidence
- Whole phase: [[Phases/06 Speech & Audio|Phase 6: Speech & Audio]] — speech ·  medium confidence

## Concepts taught

- Socratic policy `lesson term` — Tutor asks a leading question rather than giving the answer
- Bayesian knowledge tracing `lesson term` — Classic learner-model equations for mastery probability per concept
- FSRS `lesson term` — 2024 spaced-repetition scheduler, better than SM-2
- Curriculum graph `lesson term` — Neo4j of concepts with prerequisite edges
- [[Concepts/Episodic memory|Episodic memory]] `lesson term` — Every interaction stored for later retrieval
- Semantic memory `lesson term` — Compacted mistakes and preferences promoted from episodic
- COPPA `lesson term` — US law restricting data collection from children under 13

## Ships

- [[Artifacts/19-17 ai-tutor|ai-tutor]] `skill` — Ship an adaptive multimodal personal tutor for a specific subject with Bayesian knowledge tracing, a curriculum graph, safety filters, and a measured two-week efficacy study.

## Further reading

- Duolingo Max ([link](https://blog.duolingo.com/duolingo-max/)) — reference language-learning tutor
- Google LearnLM / Gemini for Education ([link](https://blog.google/technology/google-deepmind/learnlm)) — hosted reference model
- Bayesian Knowledge Tracing ([link](https://en.wikipedia.org/wiki/Bayesian_knowledge_tracing)) — learner-model classic
- [[Resources/LiveKit Agents 1.0|LiveKit Agents 1.0]] ([link](https://github.com/livekit/agents)) — voice stack ·  also cited by 1 other lesson
- FSRS algorithm ([link](https://github.com/open-spaced-repetition/fsrs4anki)) — spaced-repetition scheduler
- Khanmigo (Khan Academy) ([link](https://www.khanmigo.ai)) — reference consumer K-12 tutor
- Quizlet Q-Chat ([link](https://quizlet.com)) — alternate reference
- Synthesis Tutor ([link](https://www.synthesis.com)) — startup reference


%% ── my notes ── %%
