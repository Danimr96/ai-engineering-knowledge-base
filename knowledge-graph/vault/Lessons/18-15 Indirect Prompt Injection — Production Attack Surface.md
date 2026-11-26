---
id: "lesson:18/15"
type: lesson
ref: 18/15
phase: 18
num: 15
title: "Indirect Prompt Injection — Production Attack Surface"
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 6
code_files: 1
concepts: 8
prereqs: 1
aliases:
  - 18/15
  - 18-15
tags:
  - phase/18
  - type/build
  - stdlib-only
source: ai-engineering-from-scratch/phases/18-ethics-safety-alignment/15-indirect-prompt-injection/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/15-indirect-prompt-injection"
---

# 18/15 Indirect Prompt Injection — Production Attack Surface

> Indirect prompt injection (IPI) embeds instructions inside external content — a web page, an email, a shared document, a support ticket — consumed by an agentic system without explicit user action. IPI is the dominant 2026 production threat: it bypasses user-input filters because the attacker never touches the user, it scales silently as agents process more external content, and it targets automated workflows where nobody is reading the prompt. MDPI Information 17(1):54 (January 2026) synthesizes 2023-2025 research. NDSS 2026's IPI-defense paper frames the core challenge: injected instructions can be semantically benign ("please print Yes"), so detection requires more than keyword filtering. "The Attacker Moves Second" (Nasr et al., joint OpenAI/Anthropic/DeepMind, October 2025): adaptive attacks (gradient, RL, random search, human red-team) broke >90% of 12 published defenses that had originally reported near-zero attack success rates.

**Phase:** [[Phases/18 Ethics, Safety & Alignment|Phase 18: Ethics, Safety & Alignment]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/18-ethics-safety-alignment/15-indirect-prompt-injection/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/15-indirect-prompt-injection) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/18-ethics-safety-alignment/15-indirect-prompt-injection) · code: main.py · quiz: 6 questions  
**Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 18 · 12 (PAIR), Phase 14 (agent engineering)`

- [[Lessons/18-12 Red-Teaming- PAIR and Automated Attacks|18/12 Red-Teaming: PAIR and Automated Attacks]] — PAIR
- Whole phase: [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] — agent engineering ·  medium confidence

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/18-01 Instruction-Following as Alignment Signal|18/01 Instruction-Following as Alignment Signal]]
- depth 3: [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]], [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]], [[Lessons/10-08 DPO- Direct Preference Optimization|10/08 DPO: Direct Preference Optimization]]

## Builds on this

- [[Lessons/18-16 Red-Team Tooling — Garak, Llama Guard, PyRIT|18/16 Red-Team Tooling — Garak, Llama Guard, PyRIT]]
- [[Lessons/18-25 EchoLeak and the Emergence of CVEs for AI|18/25 EchoLeak and the Emergence of CVEs for AI]]
- [[Lessons/18-28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR|18/28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR]]

## Concepts taught

- IPI `lesson term` — Injection via content the user did not write, consumed by the agent during normal operation
- RAG injection `lesson term` — Attacker publishes content that the retrieval step fetches; prompt contains the payload
- [[Concepts/Zero-click|Zero-click]] `lesson term` — Attack triggers automatically during agent operation; user does nothing
- IFC `lesson term` — Label-based approach: actions from untrusted content require trusted ratification
- Adaptive attack `lesson term` — Attack that knows the defense and optimizes against it; required for honest evaluation
- Benign instruction `lesson term` — IPI payload that is semantically benign; no keyword filter catches it
- Scope violation `lesson term` — Agent accesses data from one trust context and outputs it to another
- [[Concepts/Indirect Prompt Injection|Indirect Prompt Injection]] `glossary` — A prompt-injection attack delivered through content the system retrieves or observes, such as a webpage, document, email, image text, or tool result, rather than directly through the user's instruction.

## Ships

- [[Artifacts/18-15 ipi-audit|ipi-audit]] `skill` — Audit an agentic deployment for indirect prompt injection exposure and information-flow-control coverage.

## Further reading

- [[Resources/Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection|Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection]] ([link](https://arxiv.org/abs/2302.12173)) — the original IPI paper ·  also cited by 4 other lessons
- Nasr et al. — The Attacker Moves Second (joint OpenAI/Anthropic/DeepMind, October 2025) ([link](https://arxiv.org/abs/2510.18108)) — adaptive attack evaluation
- [[Resources/OWASP — LLM Top 10 (2025)|OWASP — LLM Top 10 (2025)]] ([link](https://genai.owasp.org/llm-top-10/)) — prompt injection ranked LLM01 ·  also cited by 1 other lesson
- MDPI Information 17(1):54 — Indirect Prompt Injection Survey (January 2026) ([link](https://www.mdpi.com/2078-2489/17/1/54)) — 2023-2025 synthesis


%% ── my notes ── %%
