---
id: "lesson:14/10"
type: lesson
ref: 14/10
phase: 14
num: 10
title: Skill Libraries and Lifelong Learning (Voyager)
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 7
code_files: 1
concepts: 7
prereqs: 2
community: 61
aliases:
  - 14/10
  - 14-10
tags:
  - phase/14
  - type/build
  - community/61
  - stdlib-only
source: ai-engineering-from-scratch/phases/14-agent-engineering/10-skill-libraries-voyager/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/10-skill-libraries-voyager"
---

# 14/10 Skill Libraries and Lifelong Learning (Voyager)

> Voyager (Wang et al., TMLR 2024) treats executable code as a skill. Skills are named, retrievable, composable, and refined by environment feedback. This is the reference architecture for Claude Agent SDK skills, skillkit, and the 2026 skill-library pattern.

**Phase:** [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/14-agent-engineering/10-skill-libraries-voyager/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/10-skill-libraries-voyager) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/14-agent-engineering/10-skill-libraries-voyager) · code: main.py · quiz: 7 questions  
**Community:** [[Communities/61 Interrupt · Memory rot|61 Interrupt · Memory rot]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 14 · 07 (MemGPT), Phase 14 · 08 (Letta Blocks)`

- [[Lessons/14-07 Agent Memory — Virtual Context and Memory Paging|14/07 Agent Memory — Virtual Context and Memory Paging]] — MemGPT
- [[Lessons/14-08 Memory Blocks and Sleep-Time Compute|14/08 Memory Blocks and Sleep-Time Compute]] — Letta Blocks

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]], [[Lessons/14-06 Tool Use and Function Calling|14/06 Tool Use and Function Calling]]
- depth 3: [[Lessons/13-01 The Tool Interface — Why Agents Need Structured I-O|13/01 The Tool Interface — Why Agents Need Structured I/O]]

## Builds on this

- [[Lessons/14-17 The Harness as a Library — Subagents and Session Store|14/17 The Harness as a Library — Subagents and Session Store]]
- [[Lessons/14-30 Eval-Driven Agent Development|14/30 Eval-Driven Agent Development]]

## Concepts taught

- [[Concepts/Skill|Skill]] `lesson term` — Named chunk of code + description, retrievable by similarity
- Skill library `lesson term` — Persistent store of skills, searchable and composable
- [[Concepts/Curriculum|Curriculum]] `lesson term` — Bottom-up goal generator driven by current capability gap
- [[Concepts/Composition|Composition]] `lesson term` — Skills invoking skills; topologically sorted on execution
- Iterative refinement `lesson term` — Env feedback + errors + self-verification fold back into the next version
- Action-space-as-code `lesson term` — Emit functions, not primitive commands, for temporally extended behavior
- Dedup on write `lesson term` — Near-duplicate descriptions collapse to one canonical skill

## Ships

- [[Artifacts/14-10 skill-library|skill-library]] `skill` — Generate a Voyager-shaped skill library with registration, retrieval by similarity, compositional execution, and failure-driven refinement.

## Further reading

- [[Resources/Anthropic — Building agents with the Claude Agent SDK|Anthropic — Building agents with the Claude Agent SDK]] ([link](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk)) — skills and subagents in practice ·  also cited by 2 other lessons
- [[Resources/Madaan et al., Self-Refine (arXiv-2303.17651)|Madaan et al., Self-Refine (arXiv:2303.17651)]] ([link](https://arxiv.org/abs/2303.17651)) — the refinement loop underneath Voyager ·  also cited by 3 other lessons
- Wang et al., Voyager (arXiv:2305.16291) ([link](https://arxiv.org/abs/2305.16291)) — the original skill-library paper
- [[Resources/Claude Agent SDK overview|Claude Agent SDK overview]] ([link](https://platform.claude.com/docs/en/agent-sdk/overview)) — skills as the 2026 productization ·  also cited by 6 other lessons


%% ── my notes ── %%
