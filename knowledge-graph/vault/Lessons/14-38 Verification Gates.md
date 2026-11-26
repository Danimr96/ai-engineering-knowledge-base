---
id: "lesson:14/38"
type: lesson
ref: 14/38
phase: 14
num: 38
title: Verification Gates
lesson_type: build
languages:
  - Python
time_min: 55
on_route: false
quiz_count: 7
code_files: 1
concepts: 7
prereqs: 3
community: 15
aliases:
  - 14/38
  - 14-38
tags:
  - phase/14
  - type/build
  - community/15
  - stdlib-only
source: ai-engineering-from-scratch/phases/14-agent-engineering/38-verification-gates/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/38-verification-gates"
---

# 14/38 Verification Gates

> The agent does not get to mark its own work as done. A verification gate reads the scope contract, the feedback log, the rule report, and the diff, and answers a single question: is this task actually complete? If the gate says no, the task is not done, no matter what the chat says.

**Phase:** [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] · **Type:** Build · **Time:** 55 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/14-agent-engineering/38-verification-gates/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/38-verification-gates) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/14-agent-engineering/38-verification-gates) · code: main.py · quiz: 7 questions  
**Community:** [[Communities/15 System of record · Block severity · Definition of done|15 System of record · Block severity · Definition of done]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 14 · 33 (Rules), Phase 14 · 36 (Scope), Phase 14 · 37 (Feedback)`

- [[Lessons/14-33 Agent Instructions as Executable Constraints|14/33 Agent Instructions as Executable Constraints]] — Rules
- [[Lessons/14-36 Scope Contracts and Task Boundaries|14/36 Scope Contracts and Task Boundaries]] — Scope
- [[Lessons/14-37 Runtime Feedback Loops|14/37 Runtime Feedback Loops]] — Feedback

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/14-32 The Minimal Agent Workbench|14/32 The Minimal Agent Workbench]], [[Lessons/14-35 Initialization Scripts for Agents|14/35 Initialization Scripts for Agents]]
- depth 3: [[Lessons/14-31 Agent Workbench Engineering- Why Capable Models Still Fail|14/31 Agent Workbench Engineering: Why Capable Models Still Fail]], [[Lessons/14-34 Repo Memory and Durable State|14/34 Repo Memory and Durable State]]

## Builds on this

- [[Lessons/14-39 Reviewer Agent- Separate Builder from Marker|14/39 Reviewer Agent: Separate Builder from Marker]]
- [[Lessons/14-40 Multi-Session Handoff|14/40 Multi-Session Handoff]]
- [[Lessons/14-41 The Workbench on a Real Repo|14/41 The Workbench on a Real Repo]]
- [[Lessons/14-42 Capstone- Ship a Reusable Agent Workbench Pack|14/42 Capstone: Ship a Reusable Agent Workbench Pack]]
- [[Lessons/14-46 Turn Every Agent Correction into a System Improvement|14/46 Turn Every Agent Correction into a System Improvement]]
- [[Lessons/19-25 Capstone Lesson 25- Verification Gates and the Observation Budget|19/25 Capstone Lesson 25: Verification Gates and the Observation Budget]]
- [[Lessons/19-26 Capstone Lesson 26- Sandbox Runner with Denylist and Path Jail|19/26 Capstone Lesson 26: Sandbox Runner with Denylist and Path Jail]]
- [[Lessons/19-29 Capstone Lesson 29- End-to-End Coding Agent on the Harness|19/29 Capstone Lesson 29: End-to-End Coding Agent on the Harness]]

## Concepts taught

- [[Concepts/Verification Gate|Verification Gate]] `glossary` — Deterministic function over workbench artifacts producing a pass/fail verdict
- [[Concepts/Block severity|Block severity]] `lesson term` — A finding that prevents passed: true and requires a signed override
- Override log `lesson term` — Signed entries with reason and user id, audited by review
- Acceptance command `lesson term` — A shell command whose zero exit is what done means
- One report path `lesson term` — outputs/verification/<task_id>.json, consumed by CI and humans alike
- [[Concepts/Approval Gate|Approval Gate]] `glossary` — A control point that blocks a consequential action until an authorized person or policy grants permission.

## Ships

- [[Artifacts/14-38 verification-gate|verification-gate]] `skill` — Generate a deterministic verification gate that combines scope, rule, and feedback artifacts into a single verification_report.json per task, plus CI wiring that refuses to merge without a green verdict.

## Further reading

- Akira, Real-Time Guardrails for Agentic Systems ([link](https://www.akira.ai/blog/real-time-guardrails-agentic-systems)) — pre/post-tool gates
- [[Resources/Anthropic, Harness design for long-running application development|Anthropic, Harness design for long-running application development]] ([link](https://www.anthropic.com/engineering/harness-design-long-running-apps)) ·  also cited by 2 other lessons
- [[Resources/Type-Checked Compliance- Deterministic Guardrails (arXiv 2604.01483)|Type-Checked Compliance: Deterministic Guardrails (arXiv 2604.01483)]] ([link](https://arxiv.org/pdf/2604.01483)) — Lean 4 as the upper bound of deterministic gating ·  also cited by 1 other lesson
- [[Resources/logi-cmd-agent-guardrails|logi-cmd/agent-guardrails]] ([link](https://github.com/logi-cmd/agent-guardrails)) — scope + mutation-testing gates ·  also cited by 2 other lessons
- [[Resources/Guardrails AI x MLflow — deterministic safety, PII, quality validators|Guardrails AI x MLflow — deterministic safety, PII, quality validators]] ([link](https://guardrailsai.com/blog/guardrails-mlflow)) — deterministic validators as CI scorers ·  also cited by 1 other lesson
- ICMD, The 2026 Playbook for Agentic AI Ops ([link](https://icmd.app/article/the-2026-playbook-for-agentic-ai-ops-guardrails-costs-and-reliability-at-scale-1776661990431)) — approval-gate ladder (draft → approval → auto under thresholds)
- [[Resources/microservices.io, GenAI development platform — part 1- guardrails|microservices.io, GenAI development platform — part 1: guardrails]] ([link](https://microservices.io/post/architecture/2026/03/09/genai-development-platform-part-1-development-guardrails.html)) — defense in depth between pre-commit and CI ·  also cited by 2 other lessons
- [[Resources/OpenAI Agents SDK guardrails|OpenAI Agents SDK guardrails]] ([link](https://openai.github.io/openai-agents-python/guardrails/)) ·  also cited by 1 other lesson

## In learning paths

- [[Paths/Software Engineering Fundamentals|Software Engineering Fundamentals]] — step 10, required
- [[Paths/Agent-Assisted Engineering|Agent-Assisted Engineering]] — step 10, required


%% ── my notes ── %%
