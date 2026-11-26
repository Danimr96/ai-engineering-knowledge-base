---
id: "lesson:14/40"
type: lesson
ref: 14/40
phase: 14
num: 40
title: Multi-Session Handoff
lesson_type: build
languages:
  - Python
time_min: 50
on_route: false
quiz_count: 7
code_files: 1
concepts: 6
prereqs: 3
community: 15
aliases:
  - 14/40
  - 14-40
tags:
  - phase/14
  - type/build
  - community/15
  - stdlib-only
source: ai-engineering-from-scratch/phases/14-agent-engineering/40-multi-session-handoff/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/40-multi-session-handoff"
---

# 14/40 Multi-Session Handoff

> The session is going to end. The work is not. The handoff packet is the artifact that turns "the agent worked for an hour" into "the next session is productive in the first minute." Build it on purpose, not as an afterthought.

**Phase:** [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] · **Type:** Build · **Time:** 50 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/14-agent-engineering/40-multi-session-handoff/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/40-multi-session-handoff) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/14-agent-engineering/40-multi-session-handoff) · code: main.py · quiz: 7 questions  
**Community:** [[Communities/15 System of record · Block severity · Definition of done|15 System of record · Block severity · Definition of done]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 14 · 34 (Repo Memory), Phase 14 · 38 (Verification), Phase 14 · 39 (Reviewer)`

- [[Lessons/14-34 Repo Memory and Durable State|14/34 Repo Memory and Durable State]] — Repo Memory
- [[Lessons/14-38 Verification Gates|14/38 Verification Gates]] — Verification
- [[Lessons/14-39 Reviewer Agent- Separate Builder from Marker|14/39 Reviewer Agent: Separate Builder from Marker]] — Reviewer

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/14-32 The Minimal Agent Workbench|14/32 The Minimal Agent Workbench]], [[Lessons/14-33 Agent Instructions as Executable Constraints|14/33 Agent Instructions as Executable Constraints]], [[Lessons/14-36 Scope Contracts and Task Boundaries|14/36 Scope Contracts and Task Boundaries]], [[Lessons/14-37 Runtime Feedback Loops|14/37 Runtime Feedback Loops]]
- depth 3: [[Lessons/14-31 Agent Workbench Engineering- Why Capable Models Still Fail|14/31 Agent Workbench Engineering: Why Capable Models Still Fail]], [[Lessons/14-35 Initialization Scripts for Agents|14/35 Initialization Scripts for Agents]]

## Builds on this

- [[Lessons/14-41 The Workbench on a Real Repo|14/41 The Workbench on a Real Repo]]
- [[Lessons/14-42 Capstone- Ship a Reusable Agent Workbench Pack|14/42 Capstone: Ship a Reusable Agent Workbench Pack]]
- [[Lessons/14-46 Turn Every Agent Correction into a System Improvement|14/46 Turn Every Agent Correction into a System Improvement]]

## Concepts taught

- Handoff packet `lesson term` — Generated artifact carrying the seven fields, both markdown and JSON
- Next action `lesson term` — The one concrete step that starts the next session
- Feedback trim `lesson term` — Last K records plus every non-zero exit
- Status report `lesson term` — A document missing next_action; useful, but not a handoff
- Verdict pointer `lesson term` — Path to the verification + review reports for traceability
- [[Concepts/Handoff|Handoff]] `glossary` — A structured transfer of a task between people or agents that preserves the objective, current state, evidence, decisions, constraints, and remaining work.

## Ships

- [[Artifacts/14-40 handoff-generator|handoff-generator]] `skill` — Generate end-of-session handoff packets from workbench artifacts, producing both human-readable Markdown and machine-readable JSON keyed to the seven canonical fields.

## Further reading

- [[Resources/Anthropic, Effective harnesses for long-running agents|Anthropic, Effective harnesses for long-running agents]] ([link](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)) ·  also cited by 4 other lessons
- [[Resources/Codex Blog, Codex CLI Context Compaction|Codex Blog, Codex CLI Context Compaction]] ([link](https://codex.danielvaughan.com/2026/03/31/codex-cli-context-compaction-architecture/)) — POST /v1/responses/compact and local fallback ·  also cited by 1 other lesson
- OpenCode, Context Management and Compaction ([link](https://deepwiki.com/sst/opencode/2.4-context-management-and-compaction))
- Hermes Issue #20372 — automatic fresh-session handoff when compression becomes risky ([link](https://github.com/NousResearch/hermes-agent/issues/20372))
- Hermes Issue #499 — Context Compaction Quality Overhaul ([link](https://github.com/NousResearch/hermes-agent/issues/499)) — handoff-oriented prompts in Codex CLI
- JD Hodges, Claude Handoff Prompt: How to Keep Context Across Sessions (2026) ([link](https://www.jdhodges.com/blog/ai-session-handoffs-keep-context-across-conversations/)) — CLAUDE.md + HANDOVER.md, 50-75% context budget
- Justin3go, Shedding Heavy Memories: Context Compaction in Codex, Claude Code, OpenCode ([link](https://justin3go.com/en/posts/2026/04/09-context-compaction-in-codex-claude-code-and-opencode)) — three-vendor compaction comparison
- LangChain, Context Engineering for Agents ([link](https://www.langchain.com/blog/context-engineering-for-agents))
- [[Resources/Microsoft Agent Framework, Compaction|Microsoft Agent Framework, Compaction]] ([link](https://learn.microsoft.com/en-us/agent-framework/agents/conversations/compaction)) ·  also cited by 1 other lesson
- Mervin Praison, Managing Handoffs in Multi-Agent Coding Sessions: Fresh Context Without Losing Continuity ([link](https://mer.vin/2026/04/managing-handoffs-in-multi-agent-coding-sessions-fresh-context-without-losing-continuity/)) — distributed-systems framing
- [[Resources/OpenAI Agents SDK handoffs|OpenAI Agents SDK handoffs]] ([link](https://openai.github.io/openai-agents-python/handoffs/)) ·  also cited by 1 other lesson

## In learning paths

- [[Paths/Agent-Assisted Engineering|Agent-Assisted Engineering]] — step 13, required


%% ── my notes ── %%
