---
id: "lesson:14/06"
type: lesson
ref: 14/06
phase: 14
num: 6
title: Tool Use and Function Calling
lesson_type: build
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 7
code_files: 2
concepts: 9
prereqs: 2
community: 17
aliases:
  - 14/06
  - 14-06
tags:
  - phase/14
  - type/build
  - community/17
  - stdlib-only
source: ai-engineering-from-scratch/phases/14-agent-engineering/06-tool-use-and-function-calling/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/06-tool-use-and-function-calling"
---

# 14/06 Tool Use and Function Calling

> Toolformer (Schick et al., 2023) started self-supervised tool annotation. Berkeley Function Calling Leaderboard V4 (Patil et al., 2025) sets the 2026 bar: 40% agentic, 30% multi-turn, 10% live, 10% non-live, 10% hallucination. Single-turn is solved. Memory, dynamic decision-making, and long-horizon tool chains are not.

**Phase:** [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] · **Type:** Build · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/14-agent-engineering/06-tool-use-and-function-calling/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/06-tool-use-and-function-calling) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/14-agent-engineering/06-tool-use-and-function-calling) · code: main.py, main.ts · quiz: 7 questions  
**Community:** [[Communities/17 Tool Contract · Agent · Function Calling|17 Tool Contract · Agent · Function Calling]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 14 · 01 (Agent Loop), Phase 13 · 01 (Function Calling Deep Dive)`

- [[Lessons/13-01 The Tool Interface — Why Agents Need Structured I-O|13/01 The Tool Interface — Why Agents Need Structured I/O]] — Function Calling Deep Dive
- [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]] — Agent Loop

## Builds on this

- [[Lessons/14-07 Agent Memory — Virtual Context and Memory Paging|14/07 Agent Memory — Virtual Context and Memory Paging]]
- [[Lessons/14-16 OpenAI Agents SDK- Handoffs, Guardrails, Tracing|14/16 OpenAI Agents SDK: Handoffs, Guardrails, Tracing]]
- [[Lessons/14-19 Benchmarks- SWE-bench, GAIA, AgentBench|14/19 Benchmarks: SWE-bench, GAIA, AgentBench]]
- [[Lessons/14-27 Prompt Injection and the PVE Defense|14/27 Prompt Injection and the PVE Defense]]
- [[Lessons/14-30 Eval-Driven Agent Development|14/30 Eval-Driven Agent Development]]

## Concepts taught

- [[Concepts/Function Calling|Function Calling]] `glossary` — Structured-output tool invocation with validated schema
- Toolformer `lesson term` — Schick 2023 — keep tool calls whose results reduce next-token loss
- BFCL `lesson term` — 2026 benchmark: 40% agentic, 30% multi-turn, 10% live, 10% non-live, 10% hallucination
- [[Concepts/Tool schema|Tool schema]] `lesson term` — name, description, JSON Schema of arguments
- tool_use_id `lesson term` — Ties a tool call to its result; essential for parallel dispatch
- Hallucination detection `lesson term` — V4 category: refuse to call when no tool fits
- Argument coercion `lesson term` — Narrow fixes for predictable schema-mismatch; reject if ambiguous
- Sandboxing `lesson term` — Per-tool read/write surface, network, timeout, memory cap
- [[Concepts/Tool Contract|Tool Contract]] `glossary` — The complete agreement for a tool boundary: purpose, typed inputs, outputs, validation, permissions, side effects, errors, timeouts, idempotency, and evidence returned to the caller.

## Ships

- [[Artifacts/14-06 tool-registry|tool-registry]] `skill` — Build a production tool catalog and registry with JSON Schema validation, parallel dispatch, and observability.

## Further reading

- [[Resources/Schick et al., 2023 - -Toolformer- Language Models Can Teach Themselves to Use Tools|Schick et al., 2023 -- "Toolformer: Language Models Can Teach Themselves to Use Tools]] ([link](https://arxiv.org/abs/2302.04761)) — self-supervised tool annotation ·  also cited by 1 other lesson
- [[Resources/Berkeley Function Calling Leaderboard|Berkeley Function Calling Leaderboard]] ([link](https://gorilla.cs.berkeley.edu/leaderboard.html)) — 2026 eval benchmark ·  also cited by 2 other lessons
- [[Resources/OpenAI Agents SDK docs|OpenAI Agents SDK docs]] ([link](https://openai.github.io/openai-agents-python/)) — function tool type and Guardrails ·  also cited by 8 other lessons
- [[Resources/Claude Agent SDK overview|Claude Agent SDK overview]] ([link](https://platform.claude.com/docs/en/agent-sdk/overview)) — production tool schema in the Claude Agent SDK ·  also cited by 6 other lessons

## In learning paths

- [[Paths/Agent Systems Engineering|Agent Systems Engineering]] — step 5, required


%% ── my notes ── %%
