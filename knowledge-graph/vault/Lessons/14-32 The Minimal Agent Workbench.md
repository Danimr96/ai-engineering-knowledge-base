---
id: "lesson:14/32"
type: lesson
ref: 14/32
phase: 14
num: 32
title: The Minimal Agent Workbench
lesson_type: build
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 7
code_files: 1
concepts: 5
prereqs: 1
community: 15
aliases:
  - 14/32
  - 14-32
tags:
  - phase/14
  - type/build
  - community/15
  - stdlib-only
source: ai-engineering-from-scratch/phases/14-agent-engineering/32-minimal-agent-workbench/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/32-minimal-agent-workbench"
---

# 14/32 The Minimal Agent Workbench

> The smallest useful workbench is three files: a root instructions router, a state file, and a task board. Everything else is layered on top. If a repo cannot carry these three, no model will save it.

**Phase:** [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] · **Type:** Build · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/14-agent-engineering/32-minimal-agent-workbench/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/32-minimal-agent-workbench) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/14-agent-engineering/32-minimal-agent-workbench) · code: main.py · quiz: 7 questions  
**Community:** [[Communities/15 System of record · Block severity · Definition of done|15 System of record · Block severity · Definition of done]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 14 · 31 (Why Capable Models Still Fail)`

- [[Lessons/14-31 Agent Workbench Engineering- Why Capable Models Still Fail|14/31 Agent Workbench Engineering: Why Capable Models Still Fail]] — Why Capable Models Still Fail

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]], [[Lessons/14-26 Failure Modes- Why Agents Break|14/26 Failure Modes: Why Agents Break]]
- depth 3: [[Lessons/14-05 Self-Refine and CRITIC- Iterative Output Improvement|14/05 Self-Refine and CRITIC: Iterative Output Improvement]], [[Lessons/14-24 Agent Observability- Langfuse, Phoenix, Opik|14/24 Agent Observability: Langfuse, Phoenix, Opik]]

## Builds on this

- [[Lessons/14-33 Agent Instructions as Executable Constraints|14/33 Agent Instructions as Executable Constraints]]
- [[Lessons/14-34 Repo Memory and Durable State|14/34 Repo Memory and Durable State]]
- [[Lessons/14-35 Initialization Scripts for Agents|14/35 Initialization Scripts for Agents]]
- [[Lessons/14-36 Scope Contracts and Task Boundaries|14/36 Scope Contracts and Task Boundaries]]
- [[Lessons/14-37 Runtime Feedback Loops|14/37 Runtime Feedback Loops]]
- [[Lessons/14-41 The Workbench on a Real Repo|14/41 The Workbench on a Real Repo]]
- [[Lessons/14-42 Capstone- Ship a Reusable Agent Workbench Pack|14/42 Capstone: Ship a Reusable Agent Workbench Pack]]

## Concepts taught

- [[Concepts/Router|Router]] `lesson term` — Short root file that points the agent at deeper docs and files
- State file `lesson term` — Machine-readable record of where the agent is, written every turn
- [[Concepts/Task board|Task board]] `lesson term` — JSON queue of work with status, owner, acceptance
- [[Concepts/System of record|System of record]] `lesson term` — The file the workbench treats as authoritative when chat is gone
- [[Concepts/Agent Harness|Agent Harness]] `glossary` — The runtime around a model that assembles context, exposes tools, manages state, enforces limits, records traces, and decides when the agent should continue, retry, ask, or stop.

## Ships

- [[Artifacts/14-32 minimal-workbench|minimal-workbench]] `skill` — Lay down the three-file minimum viable agent workbench for any repo — short AGENTS.md router, durable agent_state.json, and a JSON task_board.json keyed to the project's current backlog.

## Further reading

- [[Resources/AGENTS.md specification|AGENTS.md specification]] ([link](https://agents.md/)) — adopted by Cursor, Codex, Claude Code, Copilot, Gemini, OpenCode ·  also cited by 1 other lesson
- [[Resources/Augment Code, A good AGENTS.md is a model upgrade. A bad one is worse than no docs at all|Augment Code, A good AGENTS.md is a model upgrade. A bad one is worse than no docs at all]] ([link](https://www.augmentcode.com/blog/how-to-write-good-agents-dot-md-files)) — measured quality jumps ·  also cited by 1 other lesson
- Blake Crosley, AGENTS.md Patterns: What Actually Changes Agent Behavior ([link](https://blakecrosley.com/blog/agents-md-patterns)) — what works empirically, what does not
- [[Resources/Anthropic, Claude Code subagents|Anthropic, Claude Code subagents]] ([link](https://code.claude.com/docs/en/sub-agents)) ·  also cited by 1 other lesson
- Datadog Frontend, Steering AI Agents in Monorepos with AGENTS.md ([link](https://dev.to/datadog-frontend-dev/steering-ai-agents-in-monorepos-with-agentsmd-13g0)) — nested precedence in practice
- [[Resources/Nx Blog, Teach Your AI Agent How to Work in a Monorepo|Nx Blog, Teach Your AI Agent How to Work in a Monorepo]] ([link](https://nx.dev/blog/nx-ai-agent-skills)) — single-source generation across six tools ·  also cited by 1 other lesson
- The Prompt Shelf, AGENTS.md Best Practices: Structure, Scope, and Real Examples ([link](https://thepromptshelf.dev/blog/agents-md-best-practices/)) — section ordering that survives review

## In learning paths

- [[Paths/Agent-Assisted Engineering|Agent-Assisted Engineering]] — step 4, required


%% ── my notes ── %%
