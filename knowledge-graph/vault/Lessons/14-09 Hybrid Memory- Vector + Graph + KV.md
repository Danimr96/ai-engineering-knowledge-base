---
id: "lesson:14/09"
type: lesson
ref: 14/09
phase: 14
num: 9
title: "Hybrid Memory: Vector + Graph + KV"
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
  - 14/09
  - 14-09
tags:
  - phase/14
  - type/build
  - community/61
  - stdlib-only
source: ai-engineering-from-scratch/phases/14-agent-engineering/09-hybrid-memory-mem0/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/09-hybrid-memory-mem0"
---

# 14/09 Hybrid Memory: Vector + Graph + KV

> Hybrid memory runs three stores in parallel — vector for semantic similarity, KV for fast fact lookup, graph for entity-relationship reasoning — with a scoring layer that fuses them on retrieval. This is a widely used production pattern for external memory; Mem0 (Chhikara et al., 2025) is one reference implementation.

**Phase:** [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/14-agent-engineering/09-hybrid-memory-mem0/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/09-hybrid-memory-mem0) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/14-agent-engineering/09-hybrid-memory-mem0) · code: main.py · quiz: 7 questions  
**Community:** [[Communities/61 Interrupt · Memory rot|61 Interrupt · Memory rot]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 14 · 07 (MemGPT), Phase 14 · 08 (Letta Blocks)`

- [[Lessons/14-07 Agent Memory — Virtual Context and Memory Paging|14/07 Agent Memory — Virtual Context and Memory Paging]] — MemGPT
- [[Lessons/14-08 Memory Blocks and Sleep-Time Compute|14/08 Memory Blocks and Sleep-Time Compute]] — Letta Blocks

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]], [[Lessons/14-06 Tool Use and Function Calling|14/06 Tool Use and Function Calling]]
- depth 3: [[Lessons/13-01 The Tool Interface — Why Agents Need Structured I-O|13/01 The Tool Interface — Why Agents Need Structured I/O]]

## Builds on this

- [[Lessons/14-30 Eval-Driven Agent Development|14/30 Eval-Driven Agent Development]]

## Concepts taught

- Hybrid memory `lesson term` — Three stores written in parallel, fused on retrieval
- Fact extraction `lesson term` — LLM step that breaks text into (entity, relation, fact) tuples
- Fusion scoring `lesson term` — Weighted sum of relevance, importance, recency
- Scope `lesson term` — user / session / agent — determines who sees what
- Mem0g `lesson term` — Typed edges with temporal validity for relationship queries
- Temporal invalidation `lesson term` — Mark contradicted edges invalid; never delete
- Embedding drift `lesson term` — Vector quality degrades as corpus grows; re-embed periodically

## Ships

- [[Artifacts/14-09 hybrid-memory|hybrid-memory]] `skill` — Generate a Mem0-shaped three-store memory system (vector + KV + graph) with a fusion scorer, scope taxonomy, and temporal invalidation.

## Further reading

- [[Resources/Packer et al., MemGPT (arXiv-2310.08560)|Packer et al., MemGPT (arXiv:2310.08560)]] ([link](https://arxiv.org/abs/2310.08560)) — the virtual-context predecessor ·  also cited by 2 other lessons
- [[Resources/Chhikara et al., Mem0 (arXiv-2504.19413)|Chhikara et al., Mem0 (arXiv:2504.19413)]] ([link](https://arxiv.org/abs/2504.19413)) — the original paper ·  also cited by 1 other lesson
- Mem0 docs ([link](https://docs.mem0.ai/platform/overview)) — production API, SDKs, managed cloud
- [[Resources/Letta, Memory Blocks blog|Letta, Memory Blocks blog]] ([link](https://www.letta.com/blog/memory-blocks)) — the three-tier sibling design ·  also cited by 2 other lessons


%% ── my notes ── %%
