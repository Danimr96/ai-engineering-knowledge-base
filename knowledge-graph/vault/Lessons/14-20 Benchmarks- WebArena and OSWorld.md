---
id: "lesson:14/20"
type: lesson
ref: 14/20
phase: 14
num: 20
title: "Benchmarks: WebArena and OSWorld"
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 7
code_files: 1
concepts: 8
prereqs: 1
community: 31
aliases:
  - 14/20
  - 14-20
tags:
  - phase/14
  - type/learn
  - community/31
  - stdlib-only
source: ai-engineering-from-scratch/phases/14-agent-engineering/20-benchmarks-webarena-osworld/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/20-benchmarks-webarena-osworld"
---

# 14/20 Benchmarks: WebArena and OSWorld

> WebArena tests web-agent capability across four self-hosted apps. OSWorld tests desktop-agent capability across Ubuntu, Windows, macOS. At release (2023–2024) both showed a big gap between best-in-class agents and humans. The gap is narrowing; the failure modes haven't changed.

**Phase:** [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/14-agent-engineering/20-benchmarks-webarena-osworld/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/20-benchmarks-webarena-osworld) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/14-agent-engineering/20-benchmarks-webarena-osworld) · code: main.py · quiz: 7 questions  
**Community:** [[Communities/31 GUI grounding · VisualWebArena · OSWorld|31 GUI grounding · VisualWebArena · OSWorld]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 14 · 19 (SWE-bench, GAIA)`

- [[Lessons/14-19 Benchmarks- SWE-bench, GAIA, AgentBench|14/19 Benchmarks: SWE-bench, GAIA, AgentBench]] — SWE-bench, GAIA

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/14-06 Tool Use and Function Calling|14/06 Tool Use and Function Calling]]
- depth 3: [[Lessons/13-01 The Tool Interface — Why Agents Need Structured I-O|13/01 The Tool Interface — Why Agents Need Structured I/O]], [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]]

## Builds on this

- [[Lessons/14-21 Computer Use- Claude, OpenAI CUA, Gemini|14/21 Computer Use: Claude, OpenAI CUA, Gemini]]
- [[Lessons/14-30 Eval-Driven Agent Development|14/30 Eval-Driven Agent Development]]

## Concepts taught

- WebArena `lesson term` — 812 tasks across 4 self-hosted apps; gym-style evaluation
- [[Concepts/VisualWebArena|VisualWebArena]] `lesson term` — Visually grounded WebArena; screenshots are observations
- [[Concepts/OSWorld|OSWorld]] `lesson term` — 369 tasks on real Ubuntu/Windows/macOS
- [[Concepts/GUI grounding|GUI grounding]] `lesson term` — Model localizing UI elements in 1920x1080
- Operational knowledge `lesson term` — Which menu, which shortcut, which preference pane
- OSWorld-G `lesson term` — 564 grounding-only samples + training set
- OSWorld-Human `lesson term` — Manual expert action sequences to measure efficiency
- [[Concepts/Trajectory efficiency|Trajectory efficiency]] `lesson term` — Agent step count divided by human minimum

## Ships

- [[Artifacts/14-20 web-desktop-harness|web-desktop-harness]] `skill` — Build a WebArena/OSWorld-style harness with execution-based evaluation and trajectory-efficiency metrics.

## Further reading

- [[Resources/Anthropic, Introducing computer use|Anthropic, Introducing computer use]] ([link](https://www.anthropic.com/news/3-5-models-and-computer-use)) — Claude's benchmark-shaped capability ·  also cited by 2 other lessons
- Zhou et al., WebArena (arXiv:2307.13854) ([link](https://arxiv.org/abs/2307.13854)) — four-app web benchmark
- Xie et al., OSWorld (arXiv:2404.07972) ([link](https://arxiv.org/abs/2404.07972)) — cross-OS desktop benchmark
- [[Resources/OpenAI, Computer-Using Agent|OpenAI, Computer-Using Agent]] ([link](https://openai.com/index/computer-using-agent/)) — OSWorld and WebArena numbers ·  also cited by 3 other lessons


%% ── my notes ── %%
