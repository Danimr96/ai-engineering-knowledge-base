---
id: "lesson:14/27"
type: lesson
ref: 14/27
phase: 14
num: 27
title: Prompt Injection and the PVE Defense
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 7
code_files: 1
concepts: 8
prereqs: 2
community: 14
aliases:
  - 14/27
  - 14-27
tags:
  - phase/14
  - type/build
  - community/14
  - stdlib-only
source: ai-engineering-from-scratch/phases/14-agent-engineering/27-prompt-injection-defense/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/27-prompt-injection-defense"
---

# 14/27 Prompt Injection and the PVE Defense

> Greshake et al. (AISec 2023) established indirect prompt injection as the defining agent security problem. Attacker plants instructions in data the agent retrieves; on ingest, those instructions override the developer prompt. Treat all retrieved content as arbitrary code execution on the tool-use surface.

**Phase:** [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/14-agent-engineering/27-prompt-injection-defense/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/27-prompt-injection-defense) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/14-agent-engineering/27-prompt-injection-defense) · code: main.py · quiz: 7 questions  
**Community:** [[Communities/14 Least Privilege · Prompt Injection · Sandbox|14 Least Privilege · Prompt Injection · Sandbox]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 14 · 06 (Tool Use), Phase 14 · 21 (Computer Use)`

- [[Lessons/14-06 Tool Use and Function Calling|14/06 Tool Use and Function Calling]] — Tool Use
- [[Lessons/14-21 Computer Use- Claude, OpenAI CUA, Gemini|14/21 Computer Use: Claude, OpenAI CUA, Gemini]] — Computer Use

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/13-01 The Tool Interface — Why Agents Need Structured I-O|13/01 The Tool Interface — Why Agents Need Structured I/O]], [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]], [[Lessons/14-20 Benchmarks- WebArena and OSWorld|14/20 Benchmarks: WebArena and OSWorld]]
- depth 3: [[Lessons/14-19 Benchmarks- SWE-bench, GAIA, AgentBench|14/19 Benchmarks: SWE-bench, GAIA, AgentBench]]

## Builds on this

- [[Lessons/14-21 Computer Use- Claude, OpenAI CUA, Gemini|14/21 Computer Use: Claude, OpenAI CUA, Gemini]]
- [[Lessons/14-30 Eval-Driven Agent Development|14/30 Eval-Driven Agent Development]]

## Concepts taught

- [[Concepts/Indirect Prompt Injection|Indirect Prompt Injection]] `glossary` — Instructions embedded in data the agent retrieves
- Direct prompt injection `lesson term` — User-supplied prompt bypasses guardrails
- PVE `lesson term` — Cheap fast validator before expensive main inference
- Source tag `lesson term` — Metadata marking where content came from
- Allowlist navigation `lesson term` — Agent can only visit approved destinations
- Worming `lesson term` — Injected content includes instructions to propagate
- [[Concepts/Memory poisoning|Memory poisoning]] `lesson term` — Injected content stored as memory; re-poisons next session
- [[Concepts/Prompt Injection|Prompt Injection]] `glossary` — An attack or failure mode in which untrusted content influences a model to disregard intended instructions, expose data, misuse tools, or take actions outside the user's goal. The content can arrive directly from a user or indirectly through retrieved pages, files, messages, or tool output.

## Ships

- [[Artifacts/14-27 injection-defense|injection-defense]] `skill` — Build a PVE (Prompt-Validator-Executor) layer with source-tagged content, injection-marker scanning, and allowlist navigation for any agent runtime.

## Further reading

- [[Resources/Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection|Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection]] ([link](https://arxiv.org/abs/2302.12173)) — canonical attack paper ·  also cited by 4 other lessons
- [[Resources/Google, Gemini 2.5 Computer Use|Google, Gemini 2.5 Computer Use]] ([link](https://blog.google/technology/google-deepmind/gemini-computer-use-model/)) — per-step safety service ·  also cited by 1 other lesson
- [[Resources/OpenAI, Computer-Using Agent|OpenAI, Computer-Using Agent]] ([link](https://openai.com/index/computer-using-agent/)) — "only direct instructions from the user count as permission" ·  also cited by 3 other lessons
- [[Resources/OpenAI Agents SDK docs|OpenAI Agents SDK docs]] ([link](https://openai.github.io/openai-agents-python/)) — guardrails as PVE ·  also cited by 8 other lessons

## In learning paths

- [[Paths/Agent Systems Engineering|Agent Systems Engineering]] — step 11, required


%% ── my notes ── %%
