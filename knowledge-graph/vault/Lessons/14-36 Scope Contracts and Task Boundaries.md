---
id: "lesson:14/36"
type: lesson
ref: 14/36
phase: 14
num: 36
title: Scope Contracts and Task Boundaries
lesson_type: build
languages:
  - Python
time_min: 50
on_route: false
quiz_count: 7
code_files: 1
concepts: 6
prereqs: 2
community: 15
aliases:
  - 14/36
  - 14-36
tags:
  - phase/14
  - type/build
  - community/15
  - stdlib-only
source: ai-engineering-from-scratch/phases/14-agent-engineering/36-scope-contracts/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/36-scope-contracts"
---

# 14/36 Scope Contracts and Task Boundaries

> The model does not know where the work ends. A scope contract is a per-task file that says where the work begins, where it ends, and how to roll back if it spills. The contract turns "stay in scope" from a wish into a check.

**Phase:** [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] · **Type:** Build · **Time:** 50 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/14-agent-engineering/36-scope-contracts/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/36-scope-contracts) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/14-agent-engineering/36-scope-contracts) · code: main.py · quiz: 7 questions  
**Community:** [[Communities/15 System of record · Block severity · Definition of done|15 System of record · Block severity · Definition of done]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 14 · 32 (Minimal Workbench), Phase 14 · 33 (Rules as Constraints)`

- [[Lessons/14-32 The Minimal Agent Workbench|14/32 The Minimal Agent Workbench]] — Minimal Workbench
- [[Lessons/14-33 Agent Instructions as Executable Constraints|14/33 Agent Instructions as Executable Constraints]] — Rules as Constraints

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/14-31 Agent Workbench Engineering- Why Capable Models Still Fail|14/31 Agent Workbench Engineering: Why Capable Models Still Fail]]
- depth 3: [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]], [[Lessons/14-26 Failure Modes- Why Agents Break|14/26 Failure Modes: Why Agents Break]]

## Builds on this

- [[Lessons/14-38 Verification Gates|14/38 Verification Gates]]
- [[Lessons/14-41 The Workbench on a Real Repo|14/41 The Workbench on a Real Repo]]
- [[Lessons/14-42 Capstone- Ship a Reusable Agent Workbench Pack|14/42 Capstone: Ship a Reusable Agent Workbench Pack]]
- [[Lessons/14-43 Frame the Task Before the Agent Writes Code|14/43 Frame the Task Before the Agent Writes Code]]
- [[Lessons/19-25 Capstone Lesson 25- Verification Gates and the Observation Budget|19/25 Capstone Lesson 25: Verification Gates and the Observation Budget]]

## Concepts taught

- [[Concepts/Scope Contract|Scope Contract]] `glossary` — Per-task JSON listing allowed/forbidden files, acceptance, rollback
- [[Concepts/Scope creep|Scope creep]] `lesson term` — Files outside the contract changed in the same task
- [[Concepts/Rollback plan|Rollback plan]] `lesson term` — The one-paragraph operator runbook for halting
- Approval boundary `lesson term` — An action listed in the contract as requiring explicit human approval
- Diff check `lesson term` — Comparing touched files against the contract globs

## Ships

- [[Artifacts/14-36 scope-contract|scope-contract]] `skill` — Generate per-task scope contracts with allowed/forbidden globs, acceptance criteria, and rollback plan, plus a CI-ready glob-aware checker that runs on every agent diff.

## Further reading

- Augment Code, AI Spec Template ([link](https://www.augmentcode.com/guides/ai-spec-template)) — three-tier boundary system (must/ask/never)
- Agentic Coding Is Not a Trap (production logs) ([link](https://dev.to/jtorchia/agentic-coding-is-not-a-trap-i-answered-the-viral-hn-post-with-my-own-production-logs-33d9)) — specsmaxxing receipts: 52% → 21%
- Dev|Journal, Preventing AI Agent Configuration Drift with Agent Contract Testing ([link](https://earezki.com/ai-news/2026-05-05-i-built-a-tiny-ci-tool-to-keep-ai-agent-configs-from-drifting-in-my-repo/)) — `--strict` mode without external deps
- [[Resources/logi-cmd-agent-guardrails|logi-cmd/agent-guardrails]] ([link](https://github.com/logi-cmd/agent-guardrails)) — violation budgets, severity tiers ·  also cited by 2 other lessons
- Knostic, AI Coding Agent Security: Threat Models and Protection Strategies ([link](https://www.knostic.ai/blog/ai-coding-agent-security)) — scope as part of least privilege
- [[Resources/LangGraph Human-in-the-loop|LangGraph Human-in-the-loop]] ([link](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/)) ·  also cited by 1 other lesson
- OpenCode permission globs ([link](https://opencode.ai/docs/agents/)) — fine-grained per-permission scope
- OpenAI Agents SDK tool approval policies ([link](https://platform.openai.com/docs/guides/agents-sdk))

## In learning paths

- [[Paths/Agent-Assisted Engineering|Agent-Assisted Engineering]] — step 8, required


%% ── my notes ── %%
