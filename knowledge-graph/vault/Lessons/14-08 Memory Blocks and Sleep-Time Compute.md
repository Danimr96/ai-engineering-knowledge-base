---
id: "lesson:14/08"
type: lesson
ref: 14/08
phase: 14
num: 8
title: Memory Blocks and Sleep-Time Compute
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 7
code_files: 1
concepts: 8
prereqs: 1
community: 61
aliases:
  - 14/08
  - 14-08
tags:
  - phase/14
  - type/build
  - community/61
  - stdlib-only
source: ai-engineering-from-scratch/phases/14-agent-engineering/08-memory-blocks-sleep-time-compute/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/08-memory-blocks-sleep-time-compute"
---

# 14/08 Memory Blocks and Sleep-Time Compute

> Discrete functional memory blocks the model can edit directly, and a sleep-time agent that consolidates memory asynchronously while the primary agent is idle. These two ideas are how you scale memory beyond one conversation.

**Phase:** [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/14-agent-engineering/08-memory-blocks-sleep-time-compute/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/08-memory-blocks-sleep-time-compute) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/14-agent-engineering/08-memory-blocks-sleep-time-compute) · code: main.py · quiz: 7 questions  
**Community:** [[Communities/61 Interrupt · Memory rot|61 Interrupt · Memory rot]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 14 · 07 (MemGPT)`

- [[Lessons/14-07 Agent Memory — Virtual Context and Memory Paging|14/07 Agent Memory — Virtual Context and Memory Paging]] — MemGPT

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]], [[Lessons/14-06 Tool Use and Function Calling|14/06 Tool Use and Function Calling]]
- depth 3: [[Lessons/13-01 The Tool Interface — Why Agents Need Structured I-O|13/01 The Tool Interface — Why Agents Need Structured I/O]]

## Builds on this

- [[Lessons/14-09 Hybrid Memory- Vector + Graph + KV|14/09 Hybrid Memory: Vector + Graph + KV]]
- [[Lessons/14-10 Skill Libraries and Lifelong Learning (Voyager)|14/10 Skill Libraries and Lifelong Learning (Voyager)]]
- [[Lessons/14-30 Eval-Driven Agent Development|14/30 Eval-Driven Agent Development]]

## Concepts taught

- Memory block `lesson term` — Typed, persistent, LLM-editable segment of core memory
- Human block `lesson term` — Facts about the user, pinned in core
- Persona block `lesson term` — Self-concept, tone, constraints, pinned in core
- Sleep-time compute `lesson term` — Second agent doing consolidation off the critical path
- Core / Recall / Archival `lesson term` — Three-layer memory split: always-visible / conversation / external
- Block limit `lesson term` — Character limit per block; forces summarization
- Native reasoning `lesson term` — Provider-level reasoning output, not prompt-level Thought:
- Learned context `lesson term` — Facts the sleep-time agent writes into shared blocks

## Ships

- [[Artifacts/14-08 memory-blocks|memory-blocks]] `skill` — Generate a Letta-shaped three-tier memory system (core blocks, recall, archival) with a sleep-time consolidation agent off the critical path.

## Further reading

- [[Resources/Packer et al., MemGPT (arXiv-2310.08560)|Packer et al., MemGPT (arXiv:2310.08560)]] ([link](https://arxiv.org/abs/2310.08560)) — the origin ·  also cited by 2 other lessons
- [[Resources/Letta, Rearchitecting the Agent Loop|Letta, Rearchitecting the Agent Loop]] ([link](https://www.letta.com/blog/letta-v1-agent)) — native reasoning rewrite ·  also cited by 1 other lesson
- [[Resources/Letta, Memory Blocks blog|Letta, Memory Blocks blog]] ([link](https://www.letta.com/blog/memory-blocks)) — the block pattern ·  also cited by 2 other lessons
- [[Resources/Letta, Sleep-time Compute|Letta, Sleep-time Compute]] ([link](https://www.letta.com/blog/sleep-time-compute)) — async consolidation ·  also cited by 1 other lesson


%% ── my notes ── %%
