---
id: "lesson:19/16"
type: lesson
ref: 19/16
phase: 19
num: 16
title: "Capstone 16 — GitHub Issue-to-PR Autonomous Agent"
lesson_type: capstone
languages:
  - Python
  - TypeScript
  - YAML
time_min: 1800
on_route: false
quiz_count: 7
code_files: 8
concepts: 7
prereqs: 0
community: 83
libraries:
  - hono
aliases:
  - 19/16
  - 19-16
tags:
  - phase/19
  - type/capstone
  - community/83
  - stdlib-only
source: ai-engineering-from-scratch/phases/19-capstone-projects/16-github-issue-to-pr-agent/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/16-github-issue-to-pr-agent"
---

# 19/16 Capstone 16 — GitHub Issue-to-PR Autonomous Agent

> Label an issue, get a PR — the 2026 product shape for autonomous coding agents: run an agent in a cloud sandbox, verify tests pass, and post a review-ready PR with rationale. AWS Remote SWE Agents, Cursor Background Agents, OpenAI Codex cloud, and Google Jules all ship it. The hard parts are reproducing the repo's build environment automatically, preventing credential leakage, enforcing per-repo budgets, and making sure the agent cannot force-push. This capstone builds the self-hosted version and compares it on cost and pass rate to the hosted alternatives.

**Phase:** [[Phases/19 Capstone Projects|Phase 19: Capstone Projects]] · **Type:** Capstone · **Time:** 1800 min · **Languages:** Python, TypeScript, YAML · **Status:** —  
**Open:** [[Upstream/19-capstone-projects/16-github-issue-to-pr-agent/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/16-github-issue-to-pr-agent) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/19-capstone-projects/16-github-issue-to-pr-agent) · code: main.py, ts/src/agent.ts, ts/src/index.ts, ts/src/router.ts, ts/src/server.ts, ts/src/types.ts … · quiz: 7 questions  
**Community:** [[Communities/83 Coverage delta · Verification|83 Coverage delta · Verification]] · **Libraries:** [[Libraries/hono (typescript)|hono]]  

## Prerequisites

Stated upstream: `Phase 11 (LLM engineering), Phase 13 (tools), Phase 14 (agents), Phase 15 (autonomous), Phase 17 (infrastructure)`

- Whole phase: [[Phases/11 LLM Engineering|Phase 11: LLM Engineering]] — LLM engineering ·  medium confidence
- Whole phase: [[Phases/13 Tools & Protocols|Phase 13: Tools & Protocols]] — tools ·  medium confidence
- Whole phase: [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] — agents ·  medium confidence
- Whole phase: [[Phases/15 Autonomous Systems|Phase 15: Autonomous Systems]] — autonomous ·  medium confidence
- Whole phase: [[Phases/17 Infrastructure & Production|Phase 17: Infrastructure & Production]] — infrastructure ·  medium confidence

## Concepts taught

- GitHub App `lesson term` — App with fine-grained permissions + short-lived installation token
- Async cloud agent `lesson term` — Non-interactive worker that runs in a cloud sandbox, not a terminal
- Environment inference `lesson term` — Detect language + package manager, generate a Dockerfile if absent
- [[Concepts/Verification|Verification]] `lesson term` — Run the full test suite inside the worker before opening a PR
- [[Concepts/Coverage delta|Coverage delta]] `lesson term` — Change in test coverage % from base to agent branch
- Per-repo budget `lesson term` — Dollar and PR-count cap enforced at the dispatcher
- Rationale `lesson term` — Agent's summary of what changed and why; required in the PR body

## Ships

- [[Artifacts/19-16 issue-to-pr|issue-to-pr]] `skill` — Build an async GitHub issue-to-PR agent that runs in a cloud sandbox, reproduces the build, verifies tests, and opens review-ready PRs within strict per-repo budgets.

## Further reading

- [[Resources/Daytona sandboxes|Daytona sandboxes]] ([link](https://daytona.io)) — reference sandbox ·  also cited by 1 other lesson
- Cursor Background Agents ([link](https://docs.cursor.com/background-agent)) — commercial alternative
- GitHub App documentation ([link](https://docs.github.com/en/apps)) — scoped bot identity
- [[Resources/Factory Droids|Factory Droids]] ([link](https://www.factory.ai)) — alternate commercial reference ·  also cited by 1 other lesson
- SWE-agent ([link](https://github.com/SWE-agent/SWE-agent)) — CLI reference
- AWS Remote SWE Agents ([link](https://github.com/aws-samples/remote-swe-agents)) — the canonical async cloud agent reference
- Google Jules ([link](https://jules.google)) — Google's hosted version
- OpenAI Codex (cloud) ([link](https://openai.com/codex)) — hosted competitor


%% ── my notes ── %%
