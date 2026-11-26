---
id: "lesson:14/35"
type: lesson
ref: 14/35
phase: 14
num: 35
title: Initialization Scripts for Agents
lesson_type: build
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 7
code_files: 1
concepts: 5
prereqs: 2
community: 15
aliases:
  - 14/35
  - 14-35
tags:
  - phase/14
  - type/build
  - community/15
  - stdlib-only
source: ai-engineering-from-scratch/phases/14-agent-engineering/35-initialization-scripts/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/35-initialization-scripts"
---

# 14/35 Initialization Scripts for Agents

> Every session that starts cold pays a tax. The agent reads the same files, retries the same probes, and rediscovers the same paths. An init script pays the tax once and writes the answers into state.

**Phase:** [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] · **Type:** Build · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/14-agent-engineering/35-initialization-scripts/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/35-initialization-scripts) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/14-agent-engineering/35-initialization-scripts) · code: main.py · quiz: 7 questions  
**Community:** [[Communities/15 System of record · Block severity · Definition of done|15 System of record · Block severity · Definition of done]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 14 · 32 (Minimal Workbench), Phase 14 · 34 (Repo Memory)`

- [[Lessons/14-32 The Minimal Agent Workbench|14/32 The Minimal Agent Workbench]] — Minimal Workbench
- [[Lessons/14-34 Repo Memory and Durable State|14/34 Repo Memory and Durable State]] — Repo Memory

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/14-31 Agent Workbench Engineering- Why Capable Models Still Fail|14/31 Agent Workbench Engineering: Why Capable Models Still Fail]]
- depth 3: [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]], [[Lessons/14-26 Failure Modes- Why Agents Break|14/26 Failure Modes: Why Agents Break]]

## Builds on this

- [[Lessons/14-37 Runtime Feedback Loops|14/37 Runtime Feedback Loops]]
- [[Lessons/14-41 The Workbench on a Real Repo|14/41 The Workbench on a Real Repo]]
- [[Lessons/14-42 Capstone- Ship a Reusable Agent Workbench Pack|14/42 Capstone: Ship a Reusable Agent Workbench Pack]]

## Concepts taught

- Probe `lesson term` — A deterministic function returning (name, status, detail)
- Init report `lesson term` — JSON written next to state with the probe results
- Idempotent `lesson term` — Two runs in a row produce identical reports modulo timestamp
- Fail loud `lesson term` — Halt and surface to the human; no silent fallback
- Setup tax `lesson term` — The tokens the agent spends per session rediscovering the obvious

## Ships

- [[Artifacts/14-35 init-script|init-script]] `skill` — Interview a project and emit a deterministic init_agent.py with five probes plus a CI workflow that refuses to launch the agent if any probe fails.

## Further reading

- [[Resources/Anthropic, Effective harnesses for long-running agents|Anthropic, Effective harnesses for long-running agents]] ([link](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)) ·  also cited by 4 other lessons
- Augment Code, How to Build Your AGENTS.md (2026) ([link](https://www.augmentcode.com/guides/how-to-build-agents-md)) — init expectations
- [[Resources/Codex Blog, Codex CLI Context Compaction|Codex Blog, Codex CLI Context Compaction]] ([link](https://codex.danielvaughan.com/2026/03/31/codex-cli-context-compaction-architecture/)) — session start as compaction-aware init ·  also cited by 1 other lesson
- GitHub Actions, composite actions for setup ([link](https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-composite-action))
- [[Resources/microservices.io, GenAI development platform — part 1- guardrails|microservices.io, GenAI development platform — part 1: guardrails]] ([link](https://microservices.io/post/architecture/2026/03/09/genai-development-platform-part-1-development-guardrails.html)) — pre-commit + CI checks as init ·  also cited by 2 other lessons

## In learning paths

- [[Paths/Agent-Assisted Engineering|Agent-Assisted Engineering]] — step 7, required


%% ── my notes ── %%
