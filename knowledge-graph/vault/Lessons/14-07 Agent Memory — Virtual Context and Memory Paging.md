---
id: "lesson:14/07"
type: lesson
ref: 14/07
phase: 14
num: 7
title: "Agent Memory — Virtual Context and Memory Paging"
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 7
code_files: 1
concepts: 8
prereqs: 2
community: 61
aliases:
  - 14/07
  - 14-07
tags:
  - phase/14
  - type/build
  - community/61
  - stdlib-only
source: ai-engineering-from-scratch/phases/14-agent-engineering/07-memory-virtual-context-memgpt/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/07-memory-virtual-context-memgpt"
---

# 14/07 Agent Memory — Virtual Context and Memory Paging

> Context windows are finite. Conversations, documents, and tool traces are not. The fix is OS virtual memory restated — main context is RAM, external store is disk, the agent pages between them. MemGPT (Packer et al., 2023) named the pattern; many production memory systems build on it.

**Phase:** [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/14-agent-engineering/07-memory-virtual-context-memgpt/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/07-memory-virtual-context-memgpt) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/14-agent-engineering/07-memory-virtual-context-memgpt) · code: main.py · quiz: 7 questions  
**Community:** [[Communities/61 Interrupt · Memory rot|61 Interrupt · Memory rot]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 14 · 01 (Agent Loop), Phase 14 · 06 (Tool Use)`

- [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]] — Agent Loop
- [[Lessons/14-06 Tool Use and Function Calling|14/06 Tool Use and Function Calling]] — Tool Use

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/13-01 The Tool Interface — Why Agents Need Structured I-O|13/01 The Tool Interface — Why Agents Need Structured I/O]]

## Builds on this

- [[Lessons/14-08 Memory Blocks and Sleep-Time Compute|14/08 Memory Blocks and Sleep-Time Compute]]
- [[Lessons/14-09 Hybrid Memory- Vector + Graph + KV|14/09 Hybrid Memory: Vector + Graph + KV]]
- [[Lessons/14-10 Skill Libraries and Lifelong Learning (Voyager)|14/10 Skill Libraries and Lifelong Learning (Voyager)]]
- [[Lessons/14-30 Eval-Driven Agent Development|14/30 Eval-Driven Agent Development]]
- [[Lessons/15-09 The Autonomous Coding Agent Landscape (2026)|15/09 The Autonomous Coding Agent Landscape (2026)]]

## Concepts taught

- Virtual context `lesson term` — Main (prompt) + external (searchable) tiers with page in/out
- Main context `lesson term` — The prompt — fixed-size, always visible
- Archival memory `lesson term` — External searchable persistence, retrieved on demand
- Core memory `lesson term` — Named sections pinned inside the main context
- Memory tool `lesson term` — Tool call the agent issues to read/write external memory
- [[Concepts/Interrupt|Interrupt]] `lesson term` — Agent pauses, runtime fetches, result splices into next turn
- [[Concepts/Memory rot|Memory rot]] `lesson term` — Old writes drown retrieval; fix with consolidation
- [[Concepts/Memory poisoning|Memory poisoning]] `lesson term` — Attacker content stored as memory, re-ingested on recall

## Ships

- [[Artifacts/14-07 virtual-memory|virtual-memory]] `skill` — Scaffold a MemGPT-shaped two-tier memory system (main context + archival store + memory tools) for any target runtime with correct eviction, citation, and untrusted-input handling.

## Further reading

- [[Resources/Anthropic, Effective context engineering for AI agents|Anthropic, Effective context engineering for AI agents]] ([link](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)) — treating context as a budget ·  also cited by 2 other lessons
- [[Resources/Packer et al., MemGPT (arXiv-2310.08560)|Packer et al., MemGPT (arXiv:2310.08560)]] ([link](https://arxiv.org/abs/2310.08560)) — OS-inspired virtual context paper ·  also cited by 2 other lessons
- [[Resources/Chhikara et al., Mem0 (arXiv-2504.19413)|Chhikara et al., Mem0 (arXiv:2504.19413)]] ([link](https://arxiv.org/abs/2504.19413)) — hybrid production memory on top of this pattern ·  also cited by 1 other lesson
- Zep (getzep/zep) ([link](https://github.com/getzep/zep)) — temporal knowledge-graph memory from the taxonomy table
- LangMem (langchain-ai/langmem) ([link](https://github.com/langchain-ai/langmem)) — background extraction of facts and behavioral rules
- Mem0 (mem0ai/mem0) ([link](https://github.com/mem0ai/mem0)) — the extraction pipeline behind Lesson 09's hybrid store
- agentmemory (rohitg00/agentmemory) ([link](https://github.com/rohitg00/agentmemory)) — session capture consolidated into typed, searchable records
- [[Resources/Letta, Memory Blocks blog|Letta, Memory Blocks blog]] ([link](https://www.letta.com/blog/memory-blocks)) — the three-tier evolution ·  also cited by 2 other lessons

## In learning paths

- [[Paths/Agent Systems Engineering|Agent Systems Engineering]] — step 7, required


%% ── my notes ── %%
