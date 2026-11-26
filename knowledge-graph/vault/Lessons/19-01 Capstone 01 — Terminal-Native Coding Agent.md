---
id: "lesson:19/01"
type: lesson
ref: 19/01
phase: 19
num: 1
title: "Capstone 01 — Terminal-Native Coding Agent"
lesson_type: capstone
languages:
  - TypeScript
  - Bun
  - Python
time_min: 2100
on_route: false
quiz_count: 7
code_files: 12
concepts: 7
prereqs: 0
libraries:
  - zod
aliases:
  - 19/01
  - 19-01
tags:
  - phase/19
  - type/capstone
  - stdlib-only
source: ai-engineering-from-scratch/phases/19-capstone-projects/01-terminal-native-coding-agent/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/01-terminal-native-coding-agent"
---

# 19/01 Capstone 01 — Terminal-Native Coding Agent

> By 2026 the shape of a coding agent is settled. A TUI harness, a stateful plan, a sandboxed tool surface, a loop that plans, acts, observes, recovers. Claude Code, Cursor 3, and OpenCode all look the same from 50 feet. This capstone asks you to build one end to end — CLI in, pull request out — and measure it against mini-swe-agent and Live-SWE-agent on SWE-bench Pro. You will learn why the hard part is not the model call but the tool loop, the sandbox, and the cost ceiling on a 50-turn run.

**Phase:** [[Phases/19 Capstone Projects|Phase 19: Capstone Projects]] · **Type:** Capstone · **Time:** 2100 min · **Languages:** TypeScript, Bun, Python · **Status:** —  
**Open:** [[Upstream/19-capstone-projects/01-terminal-native-coding-agent/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/01-terminal-native-coding-agent) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/19-capstone-projects/01-terminal-native-coding-agent) · code: main.py, ts/src/eval.ts, ts/src/harness.ts, ts/src/hooks.ts, ts/src/index.ts, ts/src/model.ts … · quiz: 7 questions  
**Libraries:** [[Libraries/zod (typescript)|zod]]  

## Prerequisites

Stated upstream: `Phase 11 (LLM engineering), Phase 13 (tools and protocols), Phase 14 (agents), Phase 15 (autonomous systems), Phase 17 (infrastructure)`

- Whole phase: [[Phases/11 LLM Engineering|Phase 11: LLM Engineering]] — LLM engineering ·  medium confidence
- Whole phase: [[Phases/13 Tools & Protocols|Phase 13: Tools & Protocols]] — tools and protocols ·  medium confidence
- Whole phase: [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] — agents ·  medium confidence
- Whole phase: [[Phases/15 Autonomous Systems|Phase 15: Autonomous Systems]] — autonomous systems ·  medium confidence
- Whole phase: [[Phases/17 Infrastructure & Production|Phase 17: Infrastructure & Production]] — infrastructure ·  medium confidence

## Concepts taught

- Harness `lesson term` — The code surrounding the model that dispatches tools, maintains plan state, and enforces budgets
- [[Concepts/Hook|Hook]] `lesson term` — A user-authored script run on one of eight lifecycle events by the harness
- [[Concepts/Worktree|Worktree]] `glossary` — A linked git checkout at a separate path; disposable without touching the main clone
- TodoWrite `lesson term` — A typed list of pending/in-progress/done items the model rewrites each turn
- StreamableHTTP `lesson term` — 2026 MCP revision: long-lived HTTP connection with bidirectional streaming; replaces SSE
- Token ceiling `lesson term` — Per-turn or per-session cap on input+output tokens; triggers compaction or termination
- pass@1 `lesson term` — Fraction of SWE-bench tasks solved on the first run without retry or test-set peeking

## Ships

- [[Artifacts/19-01 terminal-coding-agent|terminal-coding-agent]] `skill` — Build and evaluate a terminal-native coding agent against SWE-bench Pro with bounded cost, sandboxed tools, and full 2026 hook surface.

## Further reading

- Model Context Protocol 2026 roadmap ([link](https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/)) — StreamableHTTP, capability metadata
- Cursor 3 changelog ([link](https://cursor.com/changelog)) — Agent Tabs and Composer 2 product notes
- [[Resources/Claude Code subagents documentation|Claude Code subagents documentation]] ([link](https://docs.anthropic.com/en/docs/claude-code)) — reference harness from Anthropic ·  also cited by 2 other lessons
- Live-SWE-agent ([link](https://github.com/OpenAutoCoder/live-swe-agent)) — 79.2% SWE-bench Verified with Opus 4.5
- mini-swe-agent ([link](https://github.com/SWE-agent/mini-swe-agent)) — minimal baseline for SWE-bench harness comparison
- OpenCode ([link](https://opencode.ai)) — open harness, 112k stars
- [[Resources/OpenTelemetry — GenAI semconv|OpenTelemetry — GenAI semconv]] ([link](https://opentelemetry.io/docs/specs/semconv/gen-ai/)) — span schema for tool calls and token usage ·  also cited by 9 other lessons
- [[Resources/Jimenez et al. SWE-bench leaderboard|Jimenez et al. SWE-bench leaderboard]] ([link](https://www.swebench.com/)) — the evaluation this capstone targets ·  also cited by 4 other lessons


%% ── my notes ── %%
