---
id: "lesson:14/17"
type: lesson
ref: 14/17
phase: 14
num: 17
title: "The Harness as a Library — Subagents and Session Store"
lesson_type: learn+build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 7
code_files: 1
concepts: 8
prereqs: 2
community: 7
aliases:
  - 14/17
  - 14-17
tags:
  - phase/14
  - type/learn+build
  - community/07
  - stdlib-only
source: ai-engineering-from-scratch/phases/14-agent-engineering/17-claude-agent-sdk/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/17-claude-agent-sdk"
---

# 14/17 The Harness as a Library — Subagents and Session Store

> A harness you can import: built-in tools, subagents for context isolation, hooks, W3C trace propagation, session persistence. The Claude Agent SDK is the reference example — the library form of the Claude Code harness — and Claude Managed Agents is the hosted alternative for long-running async work.

**Phase:** [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] · **Type:** Learn + Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/14-agent-engineering/17-claude-agent-sdk/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/17-claude-agent-sdk) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/14-agent-engineering/17-claude-agent-sdk) · code: main.py · quiz: 7 questions  
**Community:** [[Communities/07 Swarm · Evaluator-Optimizer · Debate|07 Swarm · Evaluator-Optimizer · Debate]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 14 · 01 (Agent Loop), Phase 14 · 10 (Skill Libraries)`

- [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]] — Agent Loop
- [[Lessons/14-10 Skill Libraries and Lifelong Learning (Voyager)|14/10 Skill Libraries and Lifelong Learning (Voyager)]] — Skill Libraries

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/14-07 Agent Memory — Virtual Context and Memory Paging|14/07 Agent Memory — Virtual Context and Memory Paging]], [[Lessons/14-08 Memory Blocks and Sleep-Time Compute|14/08 Memory Blocks and Sleep-Time Compute]]
- depth 3: [[Lessons/14-06 Tool Use and Function Calling|14/06 Tool Use and Function Calling]]

## Builds on this

- [[Lessons/14-30 Eval-Driven Agent Development|14/30 Eval-Driven Agent Development]]

## Concepts taught

- Agent SDK `lesson term` — Harness shape: tools, MCP, hooks, subagents, session store
- Subagent `lesson term` — Separate context, own budget; results bubble up
- Session store `lesson term` — Persist, load, list, delete turns with subagent cascade
- [[Concepts/Hook|Hook]] `lesson term` — Pre/post tool, session, prompt submit, compact, stop
- W3C trace context `lesson term` — Parent span propagates into CLI subprocess
- Managed Agents `lesson term` — Anthropic-hosted long-running async work
- --session-mirror `lesson term` — Writes session turns to an external file as they stream
- MCP server `lesson term` — External tool/resource source attached to the agent

## Ships

- [[Artifacts/14-17 claude-agent-scaffold|claude-agent-scaffold]] `skill` — Scaffold a Claude Agent SDK app with subagents, lifecycle hooks, session store, MCP server attachment, and W3C trace propagation.

## Further reading

- [[Resources/Anthropic — Building agents with the Claude Agent SDK|Anthropic — Building agents with the Claude Agent SDK]] ([link](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk)) — production patterns ·  also cited by 2 other lessons
- [[Resources/OpenAI Agents SDK docs|OpenAI Agents SDK docs]] ([link](https://openai.github.io/openai-agents-python/)) — counterpart ·  also cited by 8 other lessons
- [[Resources/Claude Agent SDK overview|Claude Agent SDK overview]] ([link](https://platform.claude.com/docs/en/agent-sdk/overview)) — the library form of Claude Code ·  also cited by 6 other lessons
- [[Resources/Claude Managed Agents overview|Claude Managed Agents overview]] ([link](https://platform.claude.com/docs/en/managed-agents/overview)) — hosted alternative ·  also cited by 3 other lessons


%% ── my notes ── %%
