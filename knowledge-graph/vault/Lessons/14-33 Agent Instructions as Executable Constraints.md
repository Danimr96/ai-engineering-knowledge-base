---
id: "lesson:14/33"
type: lesson
ref: 14/33
phase: 14
num: 33
title: Agent Instructions as Executable Constraints
lesson_type: build
languages:
  - Python
time_min: 50
on_route: false
quiz_count: 7
code_files: 1
concepts: 6
prereqs: 1
community: 15
aliases:
  - 14/33
  - 14-33
tags:
  - phase/14
  - type/build
  - community/15
  - stdlib-only
source: ai-engineering-from-scratch/phases/14-agent-engineering/33-instructions-as-executable-constraints/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/33-instructions-as-executable-constraints"
---

# 14/33 Agent Instructions as Executable Constraints

> Instructions written as prose are wishes. Instructions written as constraints are tests. The workbench turns each rule into something an agent can check at runtime and a reviewer can verify after the fact.

**Phase:** [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] · **Type:** Build · **Time:** 50 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/14-agent-engineering/33-instructions-as-executable-constraints/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/33-instructions-as-executable-constraints) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/14-agent-engineering/33-instructions-as-executable-constraints) · code: main.py · quiz: 7 questions  
**Community:** [[Communities/15 System of record · Block severity · Definition of done|15 System of record · Block severity · Definition of done]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 14 · 32 (Minimal Workbench)`

- [[Lessons/14-32 The Minimal Agent Workbench|14/32 The Minimal Agent Workbench]] — Minimal Workbench

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/14-31 Agent Workbench Engineering- Why Capable Models Still Fail|14/31 Agent Workbench Engineering: Why Capable Models Still Fail]]
- depth 3: [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]], [[Lessons/14-26 Failure Modes- Why Agents Break|14/26 Failure Modes: Why Agents Break]]

## Builds on this

- [[Lessons/14-36 Scope Contracts and Task Boundaries|14/36 Scope Contracts and Task Boundaries]]
- [[Lessons/14-38 Verification Gates|14/38 Verification Gates]]
- [[Lessons/14-41 The Workbench on a Real Repo|14/41 The Workbench on a Real Repo]]
- [[Lessons/14-42 Capstone- Ship a Reusable Agent Workbench Pack|14/42 Capstone: Ship a Reusable Agent Workbench Pack]]
- [[Lessons/19-25 Capstone Lesson 25- Verification Gates and the Observation Budget|19/25 Capstone Lesson 25: Verification Gates and the Observation Budget]]
- [[Lessons/19-26 Capstone Lesson 26- Sandbox Runner with Denylist and Path Jail|19/26 Capstone Lesson 26: Sandbox Runner with Denylist and Path Jail]]

## Concepts taught

- Operational rule `lesson term` — A rule the workbench can check at runtime
- Aspirational rule `lesson term` — A rule with no check; either delete or upgrade
- [[Concepts/Definition of done|Definition of done]] `lesson term` — An objective, file-backed proof the task is complete
- [[Concepts/Block severity|Block severity]] `lesson term` — Violation halts the run; cannot be silenced without an operator
- Rule expiry `lesson term` — A rule with no fails in N days is up for retirement
- [[Concepts/System Prompt|System Prompt]] `glossary` — A provider-defined instruction message or configuration supplied by the application to establish behavior and constraints within that provider's instruction hierarchy.

## Ships

- [[Artifacts/14-33 rule-set-builder|rule-set-builder]] `skill` — Interview a project owner, classify their existing prose instructions into five operational categories, and emit a versioned agent-rules.md plus a Python checker stub.

## Further reading

- [[Resources/Building Effective Agents|Building Effective Agents]] ([link](https://www.anthropic.com/research/building-effective-agents)) ·  also cited by 16 other lessons
- [[Resources/Type-Checked Compliance- Deterministic Guardrails (arXiv 2604.01483)|Type-Checked Compliance: Deterministic Guardrails (arXiv 2604.01483)]] ([link](https://arxiv.org/pdf/2604.01483)) — Lean 4 as the upper bound on rule-as-check ·  also cited by 1 other lesson
- [[Resources/Cloudflare, Orchestrating AI Code Review at Scale|Cloudflare, Orchestrating AI Code Review at Scale]] ([link](https://blog.cloudflare.com/ai-code-review/)) — 131k review runs, rule composition lessons ·  also cited by 2 other lessons
- [[Resources/logi-cmd-agent-guardrails|logi-cmd/agent-guardrails]] ([link](https://github.com/logi-cmd/agent-guardrails)) — merge-gate implementation: scope, mutation testing, violation budgets ·  also cited by 2 other lessons
- LangGraph interrupts ([link](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/))
- Rick Hightower, Agent RuleZ: A Deterministic Policy Engine ([link](https://medium.com/@richardhightower/agent-rulez-a-deterministic-policy-engine-for-ai-coding-agents-9489e0561edf)) — block/warn/info severity in production
- [[Resources/microservices.io, GenAI development platform — part 1- guardrails|microservices.io, GenAI development platform — part 1: guardrails]] ([link](https://microservices.io/post/architecture/2026/03/09/genai-development-platform-part-1-development-guardrails.html)) — defense in depth between rules and CI ·  also cited by 2 other lessons
- [[Resources/OpenAI Agents SDK guardrails|OpenAI Agents SDK guardrails]] ([link](https://openai.github.io/openai-agents-python/guardrails/)) ·  also cited by 1 other lesson

## In learning paths

- [[Paths/Agent-Assisted Engineering|Agent-Assisted Engineering]] — step 5, required


%% ── my notes ── %%
