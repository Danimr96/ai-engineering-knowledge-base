---
id: "lesson:14/01"
type: lesson
ref: 14/01
phase: 14
num: 1
title: "The Agent Loop: Observe, Think, Act"
lesson_type: build
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 7
code_files: 2
concepts: 9
prereqs: 0
community: 7
aliases:
  - 14/01
  - 14-01
tags:
  - phase/14
  - type/build
  - community/07
  - stdlib-only
source: ai-engineering-from-scratch/phases/14-agent-engineering/01-the-agent-loop/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/01-the-agent-loop"
---

# 14/01 The Agent Loop: Observe, Think, Act

> Every agent in 2026 is a variant of the ReAct loop from 2022 — Claude Code, Cursor, Devin, Operator included. Reasoning tokens interleave with tool calls and observations until a stop condition fires. Learn this loop cold before touching any framework.

**Phase:** [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] · **Type:** Build · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/14-agent-engineering/01-the-agent-loop/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/01-the-agent-loop) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/14-agent-engineering/01-the-agent-loop) · code: main.py, main.ts · quiz: 7 questions  
**Community:** [[Communities/07 Swarm · Evaluator-Optimizer · Debate|07 Swarm · Evaluator-Optimizer · Debate]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 11 (LLM Engineering), Phase 13 (Tools and Protocols)`

- Whole phase: [[Phases/11 LLM Engineering|Phase 11: LLM Engineering]] — LLM Engineering ·  medium confidence
- Whole phase: [[Phases/13 Tools & Protocols|Phase 13: Tools & Protocols]] — Tools and Protocols ·  medium confidence

## Builds on this

- [[Lessons/06-12 Build a Voice Assistant Pipeline — The Phase 6 Capstone|06/12 Build a Voice Assistant Pipeline — The Phase 6 Capstone]]
- [[Lessons/14-02 ReWOO and Plan-and-Execute- Decoupled Planning|14/02 ReWOO and Plan-and-Execute: Decoupled Planning]]
- [[Lessons/14-03 Reflexion- Verbal Reinforcement Learning|14/03 Reflexion: Verbal Reinforcement Learning]]
- [[Lessons/14-04 Tree of Thoughts and LATS- Deliberate Search|14/04 Tree of Thoughts and LATS: Deliberate Search]]
- [[Lessons/14-05 Self-Refine and CRITIC- Iterative Output Improvement|14/05 Self-Refine and CRITIC: Iterative Output Improvement]]
- [[Lessons/14-06 Tool Use and Function Calling|14/06 Tool Use and Function Calling]]
- [[Lessons/14-07 Agent Memory — Virtual Context and Memory Paging|14/07 Agent Memory — Virtual Context and Memory Paging]]
- [[Lessons/14-12 Anthropic's Workflow Patterns- Simple Over Complex|14/12 Anthropic's Workflow Patterns: Simple Over Complex]]
- [[Lessons/14-13 Stateful Graph Orchestration — Durable Execution and Checkpoints|14/13 Stateful Graph Orchestration — Durable Execution and Checkpoints]]
- [[Lessons/14-14 The Actor Model for Agents — Async Messages and Typed Runtimes|14/14 The Actor Model for Agents — Async Messages and Typed Runtimes]]
- [[Lessons/14-16 OpenAI Agents SDK- Handoffs, Guardrails, Tracing|14/16 OpenAI Agents SDK: Handoffs, Guardrails, Tracing]]
- [[Lessons/14-17 The Harness as a Library — Subagents and Session Store|14/17 The Harness as a Library — Subagents and Session Store]]
- [[Lessons/14-18 Production Agent Runtimes — Fast Instantiation and Typed Workflows|14/18 Production Agent Runtimes — Fast Instantiation and Typed Workflows]]
- [[Lessons/14-22 Voice Agents- Pipecat and LiveKit|14/22 Voice Agents: Pipecat and LiveKit]]
- [[Lessons/14-30 Eval-Driven Agent Development|14/30 Eval-Driven Agent Development]]
- [[Lessons/14-31 Agent Workbench Engineering- Why Capable Models Still Fail|14/31 Agent Workbench Engineering: Why Capable Models Still Fail]]
- [[Lessons/15-01 The Shift from Chatbots to Long-Horizon Agents|15/01 The Shift from Chatbots to Long-Horizon Agents]]
- [[Lessons/15-04 Darwin Godel Machine — Open-Ended Self-Modifying Agents|15/04 Darwin Godel Machine — Open-Ended Self-Modifying Agents]]
- [[Lessons/19-20 Agent Harness Loop Contract|19/20 Agent Harness Loop Contract]]
- [[Lessons/19-21 Tool Registry with Schema Validation|19/21 Tool Registry with Schema Validation]]
- [[Lessons/19-22 JSON-RPC 2.0 Over Newline-Delimited Stdio|19/22 JSON-RPC 2.0 Over Newline-Delimited Stdio]]
- [[Lessons/19-23 Function Call Dispatcher|19/23 Function Call Dispatcher]]
- [[Lessons/19-24 Plan-Execute Control Flow|19/24 Plan-Execute Control Flow]]

## Concepts taught

- [[Concepts/Agent|Agent]] `glossary` — A loop: LLM thinks, picks a tool, result feeds back, repeat until stop
- [[Concepts/ReAct|ReAct]] `glossary` — Yao et al. 2022 — interleave Thought, Action, Observation in one stream
- [[Concepts/Tool call|Tool call]] `lesson term` — Structured output the runtime dispatches to an executable
- Observation `lesson term` — The string representation of tool output fed back into the next prompt
- Reasoning channel `lesson term` — Native reasoning output on a separate stream, passed through across turns
- [[Concepts/Stop condition|Stop condition]] `lesson term` — Explicit finish, no tool calls emitted, max turns, max tokens, or guardrail trip
- Turn budget `lesson term` — Hard cap on loop iterations — agents run 40–400 steps per task in 2026
- [[Concepts/Trace|Trace]] `glossary` — Full record of thought, action, observation tuples for a run

## Ships

- [[Artifacts/14-01 agent-loop|agent-loop]] `skill` — Write a correct, minimal ReAct agent loop in any target language/runtime with tools, stop condition, and turn budget.

## Further reading

- [[Resources/Building Effective Agents|Building Effective Agents]] ([link](https://www.anthropic.com/research/building-effective-agents)) — when to use an agent loop vs a workflow ·  also cited by 16 other lessons
- [[Resources/ReAct|ReAct]] ([link](https://arxiv.org/abs/2210.03629)) — the canonical paper ·  also cited by 5 other lessons
- [[Resources/Letta, Rearchitecting the Agent Loop|Letta, Rearchitecting the Agent Loop]] ([link](https://www.letta.com/blog/letta-v1-agent)) — the native-reasoning rewrite of MemGPT's loop ·  also cited by 1 other lesson
- [[Resources/OpenAI Agents SDK docs|OpenAI Agents SDK docs]] ([link](https://openai.github.io/openai-agents-python/)) — Handoffs, Guardrails, Sessions, Tracing ·  also cited by 8 other lessons
- [[Resources/Claude Agent SDK overview|Claude Agent SDK overview]] ([link](https://platform.claude.com/docs/en/agent-sdk/overview)) — the 2026 harness shape ·  also cited by 6 other lessons

## In learning paths

- [[Paths/Agent Systems Engineering|Agent Systems Engineering]] — step 4, required


%% ── my notes ── %%
