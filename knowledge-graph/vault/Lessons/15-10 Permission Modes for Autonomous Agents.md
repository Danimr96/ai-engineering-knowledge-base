---
id: "lesson:15/10"
type: lesson
ref: 15/10
phase: 15
num: 10
title: Permission Modes for Autonomous Agents
lesson_type: learn
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 2
community: 29
aliases:
  - 15/10
  - 15-10
tags:
  - phase/15
  - type/learn
  - community/29
  - stdlib-only
source: ai-engineering-from-scratch/phases/15-autonomous-systems/10-claude-code-permission-modes/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/15-autonomous-systems/10-claude-code-permission-modes"
---

# 15/10 Permission Modes for Autonomous Agents

> A permission ladder — graduated levels of autonomy from review-every-action to approve-everything — is how a harness governs what an autonomous agent may do without asking. Claude Code, this lesson's worked example, exposes six such modes: "plan" asks before every action, "default" (labeled "Manual" in the UI) asks only for risky ones, "acceptEdits" auto-approves file writes but still confirms shell execution, and "bypassPermissions" approves everything. Auto Mode — the `auto` permission mode — replaces per-action approval with a separate classifier model that reviews each action before it runs and blocks anything that escalates beyond what the request asked for. Action budgets are enforced via `max_turns` and `max_budget_usd`. Availability of `auto` depends on plan, org enablement, model, and provider — and Anthropic is explicit that the classifier is not sufficient alone.

**Phase:** [[Phases/15 Autonomous Systems|Phase 15: Autonomous Systems]] · **Type:** Learn · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/15-autonomous-systems/10-claude-code-permission-modes/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/15-autonomous-systems/10-claude-code-permission-modes) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/15-autonomous-systems/10-claude-code-permission-modes) · code: main.py  
**Community:** [[Communities/29 Eval-context gaming · Time horizon · thread_id|29 Eval-context gaming · Time horizon · thread_id]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 15 · 01 (Long-horizon agents), Phase 15 · 09 (Coding-agent landscape)`

- [[Lessons/15-01 The Shift from Chatbots to Long-Horizon Agents|15/01 The Shift from Chatbots to Long-Horizon Agents]] — Long-horizon agents
- [[Lessons/15-09 The Autonomous Coding Agent Landscape (2026)|15/09 The Autonomous Coding Agent Landscape (2026)]] — Coding-agent landscape

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]], [[Lessons/14-07 Agent Memory — Virtual Context and Memory Paging|14/07 Agent Memory — Virtual Context and Memory Paging]]
- depth 3: [[Lessons/14-06 Tool Use and Function Calling|14/06 Tool Use and Function Calling]]

## Builds on this

- [[Lessons/15-11 Browser Agents and Long-Horizon Web Tasks|15/11 Browser Agents and Long-Horizon Web Tasks]]
- [[Lessons/15-12 Long-Running Background Agents- Durable Execution|15/12 Long-Running Background Agents: Durable Execution]]
- [[Lessons/15-13 Action Budgets, Iteration Caps, and Cost Governors|15/13 Action Budgets, Iteration Caps, and Cost Governors]]
- [[Lessons/15-14 Kill Switches, Circuit Breakers, and Canary Tokens|15/14 Kill Switches, Circuit Breakers, and Canary Tokens]]
- [[Lessons/15-17 Constitutional AI and Rule Overrides|15/17 Constitutional AI and Rule Overrides]]
- [[Lessons/15-18 Llama Guard and Input-Output Classification|15/18 Llama Guard and Input/Output Classification]]

## Concepts taught

- Permission mode `lesson term` — One of six named policies controlling per-action approval
- plan mode `lesson term` — Agent writes a plan; user approves before execution
- acceptEdits `lesson term` — File writes auto-approve; shell exec still prompts
- auto `lesson term` — Separate classifier model reviews each action; blocks escalation beyond the request
- bypassPermissions `lesson term` — Approves everything; intended for ephemeral containers
- Stage 1 (simulator) `lesson term` — Cheap rule over proposed actions in code/main.py
- Stage 2 (simulator) `lesson term` — Slower multi-rule reviewer for flagged actions in code/main.py
- Research preview `lesson term` — Anthropic framing for features whose failure mode is still being mapped

## Ships

- [[Artifacts/15-10 permission-mode-picker|permission-mode-picker]] `skill` — Match a Claude Code task to the correct permission mode, budget caps, and required isolation before starting a run.

## Further reading

- [[Resources/Anthropic — Claude's Constitution (January 2026)|Anthropic — Claude's Constitution (January 2026)]] ([link](https://www.anthropic.com/news/claudes-constitution)) — the reason-based layer that shapes classifier judgments. ·  also cited by 6 other lessons
- Anthropic — Claude Code product page ([link](https://www.anthropic.com/product/claude-code)) — feature surface and Auto Mode announcement.
- [[Resources/Anthropic — Measuring AI agent autonomy in practice|Anthropic — Measuring AI agent autonomy in practice]] ([link](https://www.anthropic.com/research/measuring-agent-autonomy)) — internal perspective on long-horizon permission design. ·  also cited by 16 other lessons
- [[Resources/Anthropic — How the agent loop works|Anthropic — How the agent loop works]] ([link](https://code.claude.com/docs/en/agent-sdk/agent-loop)) — permission modes, budgets, action format. ·  also cited by 3 other lessons
- [[Resources/Claude Managed Agents overview|Claude Managed Agents overview]] ([link](https://platform.claude.com/docs/en/managed-agents/overview)) — managed-service execution model. ·  also cited by 3 other lessons


%% ── my notes ── %%
