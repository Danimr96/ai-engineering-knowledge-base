---
id: "lesson:14/16"
type: lesson
ref: 14/16
phase: 14
num: 16
title: "OpenAI Agents SDK: Handoffs, Guardrails, Tracing"
lesson_type: learn+build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 7
code_files: 1
concepts: 8
prereqs: 2
community: 17
aliases:
  - 14/16
  - 14-16
tags:
  - phase/14
  - type/learn+build
  - community/17
  - stdlib-only
source: ai-engineering-from-scratch/phases/14-agent-engineering/16-openai-agents-sdk/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/16-openai-agents-sdk"
---

# 14/16 OpenAI Agents SDK: Handoffs, Guardrails, Tracing

> OpenAI Agents SDK is the lightweight multi-agent framework built on the Responses API. Five primitives: Agent, Handoff, Guardrail, Session, Tracing. Handoffs are tools named `transfer_to_<agent>`. Guardrails trip on input or output. Tracing is on by default.

**Phase:** [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] · **Type:** Learn + Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/14-agent-engineering/16-openai-agents-sdk/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/16-openai-agents-sdk) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/14-agent-engineering/16-openai-agents-sdk) · code: main.py · quiz: 7 questions  
**Community:** [[Communities/17 Tool Contract · Agent · Function Calling|17 Tool Contract · Agent · Function Calling]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 14 · 01 (Agent Loop), Phase 14 · 06 (Tool Use)`

- [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]] — Agent Loop
- [[Lessons/14-06 Tool Use and Function Calling|14/06 Tool Use and Function Calling]] — Tool Use

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/13-01 The Tool Interface — Why Agents Need Structured I-O|13/01 The Tool Interface — Why Agents Need Structured I/O]]

## Builds on this

- [[Lessons/14-30 Eval-Driven Agent Development|14/30 Eval-Driven Agent Development]]

## Concepts taught

- [[Concepts/Agent|Agent]] `glossary` — Agent type in the SDK; owns tools and handoffs
- [[Concepts/Handoff|Handoff]] `glossary` — Tool the model calls to delegate to another agent
- [[Concepts/Guardrails|Guardrails]] (as *Guardrail*) `glossary` — Validation on input / output / tool invocation
- Tripwire `lesson term` — Exception raised when guardrail rejects
- Session `lesson term` — Conversation memory persisted between runs
- [[Concepts/Tracing|Tracing]] `lesson term` — Built-in observability over LLM + tool + handoff + guardrail
- Blocking guardrail `lesson term` — Guardrail runs first; no token waste on trip
- Parallel guardrail `lesson term` — Guardrail runs alongside; lower latency, wastes tokens on trip

## Ships

- [[Artifacts/14-16 agents-sdk-scaffold|agents-sdk-scaffold]] `skill` — Scaffold an OpenAI Agents SDK app with a triage agent, handoffs, input/output/tool guardrails, session store, and a trace processor.

## Further reading

- [[Resources/Building Effective Agents|Building Effective Agents]] ([link](https://www.anthropic.com/research/building-effective-agents)) — when to reach for handoffs at all ·  also cited by 16 other lessons
- [[Resources/OpenAI Agents SDK docs|OpenAI Agents SDK docs]] ([link](https://openai.github.io/openai-agents-python/)) — primitives, handoffs, guardrails, tracing ·  also cited by 8 other lessons
- [[Resources/OpenTelemetry — GenAI semconv|OpenTelemetry — GenAI semconv]] ([link](https://opentelemetry.io/docs/specs/semconv/gen-ai/)) — the standard Agents SDK spans map to ·  also cited by 9 other lessons
- [[Resources/Claude Agent SDK overview|Claude Agent SDK overview]] ([link](https://platform.claude.com/docs/en/agent-sdk/overview)) — Claude-flavored counterpart ·  also cited by 6 other lessons


%% ── my notes ── %%
