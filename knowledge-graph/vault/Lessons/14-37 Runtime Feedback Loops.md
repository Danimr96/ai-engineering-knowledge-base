---
id: "lesson:14/37"
type: lesson
ref: 14/37
phase: 14
num: 37
title: Runtime Feedback Loops
lesson_type: build
languages:
  - Python
time_min: 50
on_route: false
quiz_count: 7
code_files: 1
concepts: 5
prereqs: 2
community: 15
aliases:
  - 14/37
  - 14-37
tags:
  - phase/14
  - type/build
  - community/15
  - stdlib-only
source: ai-engineering-from-scratch/phases/14-agent-engineering/37-runtime-feedback-loops/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/37-runtime-feedback-loops"
---

# 14/37 Runtime Feedback Loops

> Agents that do not see real command output guess. A feedback runner captures stdout, stderr, exit code, and timing into a structured record the next turn can read. Then the agent reacts to facts instead of to its own prediction of facts.

**Phase:** [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] · **Type:** Build · **Time:** 50 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/14-agent-engineering/37-runtime-feedback-loops/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/37-runtime-feedback-loops) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/14-agent-engineering/37-runtime-feedback-loops) · code: main.py · quiz: 7 questions  
**Community:** [[Communities/15 System of record · Block severity · Definition of done|15 System of record · Block severity · Definition of done]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 14 · 32 (Minimal Workbench), Phase 14 · 35 (Init Script)`

- [[Lessons/14-32 The Minimal Agent Workbench|14/32 The Minimal Agent Workbench]] — Minimal Workbench
- [[Lessons/14-35 Initialization Scripts for Agents|14/35 Initialization Scripts for Agents]] — Init Script

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/14-31 Agent Workbench Engineering- Why Capable Models Still Fail|14/31 Agent Workbench Engineering: Why Capable Models Still Fail]], [[Lessons/14-34 Repo Memory and Durable State|14/34 Repo Memory and Durable State]]
- depth 3: [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]], [[Lessons/14-26 Failure Modes- Why Agents Break|14/26 Failure Modes: Why Agents Break]]

## Builds on this

- [[Lessons/14-38 Verification Gates|14/38 Verification Gates]]
- [[Lessons/14-41 The Workbench on a Real Repo|14/41 The Workbench on a Real Repo]]
- [[Lessons/14-42 Capstone- Ship a Reusable Agent Workbench Pack|14/42 Capstone: Ship a Reusable Agent Workbench Pack]]
- [[Lessons/14-46 Turn Every Agent Correction into a System Improvement|14/46 Turn Every Agent Correction into a System Improvement]]

## Concepts taught

- Feedback record `lesson term` — Structured JSONL entry with command, output, exit, duration
- Tail truncation `lesson term` — Deterministic head+tail capture so records fit in token budget
- Refuse-on-null `lesson term` — The loop must not advance when exit_code is null
- Agent note `lesson term` — The one-line prediction the agent writes before reading the result
- Telemetry split `lesson term` — Feedback for the next turn, telemetry for the operator

## Ships

- [[Artifacts/14-37 feedback-runner|feedback-runner]] `skill` — Wrap shell commands with deterministic stdout/stderr/exit/duration capture, persist a JSONL record per command, and refuse to advance the agent loop when feedback is missing.

## Further reading

- Andrii Furmanets, AI Agents in 2026: Practical Architecture for Tools, Memory, Evals, Guardrails ([link](https://andriifurmanets.com/blogs/ai-agents-2026-practical-architecture-tools-memory-evals-guardrails)) — observability surfaces
- [[Resources/Anthropic, Effective harnesses for long-running agents|Anthropic, Effective harnesses for long-running agents]] ([link](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)) ·  also cited by 4 other lessons
- Aport.io, Best AI Agent Guardrails 2026: Pre-Action Authorization Compared ([link](https://aport.io/blog/best-ai-agent-guardrails-2026-pre-action-authorization-compared/)) — pre/post-tool capture
- [[Resources/Guardrails AI x MLflow — deterministic safety, PII, quality validators|Guardrails AI x MLflow — deterministic safety, PII, quality validators]] ([link](https://guardrailsai.com/blog/guardrails-mlflow)) — redaction patterns as regression tests ·  also cited by 1 other lesson
- [[Resources/OpenTelemetry — GenAI semconv|OpenTelemetry — GenAI semconv]] ([link](https://opentelemetry.io/docs/specs/semconv/gen-ai/)) ·  also cited by 9 other lessons

## In learning paths

- [[Paths/Agent-Assisted Engineering|Agent-Assisted Engineering]] — step 9, required


%% ── my notes ── %%
