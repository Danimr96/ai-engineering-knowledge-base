---
id: "lesson:14/21"
type: lesson
ref: 14/21
phase: 14
num: 21
title: "Computer Use: Claude, OpenAI CUA, Gemini"
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 7
code_files: 1
concepts: 7
prereqs: 2
community: 31
aliases:
  - 14/21
  - 14-21
tags:
  - phase/14
  - type/learn
  - community/31
  - stdlib-only
source: ai-engineering-from-scratch/phases/14-agent-engineering/21-computer-use-agents/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/21-computer-use-agents"
---

# 14/21 Computer Use: Claude, OpenAI CUA, Gemini

> Three production computer-use models in 2026. All three are vision-based. All three treat screenshots, DOM text, and tool outputs as untrusted input. Only direct user instructions count as permission. Per-step safety services are the norm.

**Phase:** [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/14-agent-engineering/21-computer-use-agents/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/21-computer-use-agents) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/14-agent-engineering/21-computer-use-agents) · code: main.py · quiz: 7 questions  
**Community:** [[Communities/31 GUI grounding · VisualWebArena · OSWorld|31 GUI grounding · VisualWebArena · OSWorld]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 14 · 20 (WebArena, OSWorld), Phase 14 · 27 (Prompt Injection)`

- [[Lessons/14-20 Benchmarks- WebArena and OSWorld|14/20 Benchmarks: WebArena and OSWorld]] — WebArena, OSWorld
- [[Lessons/14-27 Prompt Injection and the PVE Defense|14/27 Prompt Injection and the PVE Defense]] — Prompt Injection

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/14-06 Tool Use and Function Calling|14/06 Tool Use and Function Calling]], [[Lessons/14-19 Benchmarks- SWE-bench, GAIA, AgentBench|14/19 Benchmarks: SWE-bench, GAIA, AgentBench]]
- depth 3: [[Lessons/13-01 The Tool Interface — Why Agents Need Structured I-O|13/01 The Tool Interface — Why Agents Need Structured I/O]], [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]]

## Builds on this

- [[Lessons/14-27 Prompt Injection and the PVE Defense|14/27 Prompt Injection and the PVE Defense]]
- [[Lessons/14-30 Eval-Driven Agent Development|14/30 Eval-Driven Agent Development]]

## Concepts taught

- Computer use `lesson term` — Vision-based input + keyboard/mouse output
- Accessibility APIs `lesson term` — Not used by Claude / OpenAI CUA / Gemini — pure vision
- Per-step safety `lesson term` — Classifier runs before every action, blocks unsafe ones
- Untrusted input `lesson term` — Screenshots, DOM, tool outputs; not permission
- Virtual display `lesson term` — Headless X server used to render screens for the agent
- Online-Mind2Web `lesson term` — Real web navigation benchmark Gemini 2.5 reports against
- Sensitive action `lesson term` — Login, purchase, delete — require human-in-the-loop

## Ships

- [[Artifacts/14-21 computer-use-safety|computer-use-safety]] `skill` — Build per-step safety classifier + confirmation gate for a computer-use agent, with allowlist navigation and injection-marker filtering.

## Further reading

- [[Resources/Anthropic, Introducing computer use|Anthropic, Introducing computer use]] ([link](https://www.anthropic.com/news/3-5-models-and-computer-use)) — Claude's design ·  also cited by 2 other lessons
- [[Resources/Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection|Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection]] ([link](https://arxiv.org/abs/2302.12173)) — the untrusted-input threat model ·  also cited by 4 other lessons
- [[Resources/Google, Gemini 2.5 Computer Use|Google, Gemini 2.5 Computer Use]] ([link](https://blog.google/technology/google-deepmind/gemini-computer-use-model/)) — browser-only, per-step safety ·  also cited by 1 other lesson
- [[Resources/OpenAI, Computer-Using Agent|OpenAI, Computer-Using Agent]] ([link](https://openai.com/index/computer-using-agent/)) — CUA / Operator launch ·  also cited by 3 other lessons


%% ── my notes ── %%
