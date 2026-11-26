---
id: "lesson:15/13"
type: lesson
ref: 15/13
phase: 15
num: 13
title: "Action Budgets, Iteration Caps, and Cost Governors"
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 2
community: 29
aliases:
  - 15/13
  - 15-13
tags:
  - phase/15
  - type/learn
  - community/29
  - stdlib-only
source: ai-engineering-from-scratch/phases/15-autonomous-systems/13-cost-governors/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/15-autonomous-systems/13-cost-governors"
---

# 15/13 Action Budgets, Iteration Caps, and Cost Governors

> A mid-sized e-commerce agent's monthly LLM cost jumped from $1,200 to $4,800 after its team enabled the "order-tracking" skill. That is not a pricing bug. That is an agent that found a new loop and kept spending inside it. Microsoft's Agent Governance Toolkit (April 2, 2026) codifies the defense against this class: per-request `max_tokens`, per-task token and dollar budgets, per-day/month caps, iteration caps, tiered model routing, prompt caching, context windowing, HITL checkpoints on expensive actions, kill switches on budget breach. Anthropic's Claude Code Agent SDK ships the same primitives under different names. Financial velocity limits — e.g. cut access on >$50 in 10 minutes — catch loops faster than monthly caps.

**Phase:** [[Phases/15 Autonomous Systems|Phase 15: Autonomous Systems]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/15-autonomous-systems/13-cost-governors/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/15-autonomous-systems/13-cost-governors) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/15-autonomous-systems/13-cost-governors) · code: main.py  
**Community:** [[Communities/29 Eval-context gaming · Time horizon · thread_id|29 Eval-context gaming · Time horizon · thread_id]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 15 · 10 (Permission modes), Phase 15 · 12 (Durable execution)`

- [[Lessons/15-10 Permission Modes for Autonomous Agents|15/10 Permission Modes for Autonomous Agents]] — Permission modes
- [[Lessons/15-12 Long-Running Background Agents- Durable Execution|15/12 Long-Running Background Agents: Durable Execution]] — Durable execution

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/15-01 The Shift from Chatbots to Long-Horizon Agents|15/01 The Shift from Chatbots to Long-Horizon Agents]], [[Lessons/15-09 The Autonomous Coding Agent Landscape (2026)|15/09 The Autonomous Coding Agent Landscape (2026)]]
- depth 3: [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]], [[Lessons/14-07 Agent Memory — Virtual Context and Memory Paging|14/07 Agent Memory — Virtual Context and Memory Paging]]

## Builds on this

- [[Lessons/15-14 Kill Switches, Circuit Breakers, and Canary Tokens|15/14 Kill Switches, Circuit Breakers, and Canary Tokens]]

## Concepts taught

- Denial of Wallet `lesson term` — Agent loop generating spend with no cap to stop it
- max_tokens `lesson term` — Ceiling on a single completion's size
- max_turns `lesson term` — Ceiling on agent loop iterations in a session
- max_budget_usd `lesson term` — Session cost cap; aborts on breach
- Velocity limit `lesson term` — Limit on spend per short window (e.g., $50 / 10 min)
- Tiered routing `lesson term` — Cheap model default; escalate only when classifier warrants
- [[Concepts/Prompt Cache|Prompt Cache]] (as *Prompt caching*) `glossary` — Provider-side cache reduces re-send token cost to near zero
- HITL checkpoint `lesson term` — Human tap required before expensive action

## Ships

- [[Artifacts/15-13 agent-budget-audit|agent-budget-audit]] `skill` — Audit an agent deployment's cost-governor stack and flag missing layers before enabling unattended runs.

## Further reading

- [[Resources/Anthropic — Measuring AI agent autonomy in practice|Anthropic — Measuring AI agent autonomy in practice]] ([link](https://www.anthropic.com/research/measuring-agent-autonomy)) — cost profile for long-horizon agents. ·  also cited by 16 other lessons
- [[Resources/Anthropic — How the agent loop works|Anthropic — How the agent loop works]] ([link](https://code.claude.com/docs/en/agent-sdk/agent-loop)) — `max_turns`, `max_budget_usd`, tool allowlists. ·  also cited by 3 other lessons
- [[Resources/Microsoft — Agent Framework- human-in-the-loop and checkpointing|Microsoft — Agent Framework: human-in-the-loop and checkpointing]] ([link](https://learn.microsoft.com/en-us/agent-framework/workflows/human-in-the-loop)) — cost-governor checkpoints. ·  also cited by 4 other lessons
- Anthropic — Prompt caching (Claude API docs) ([link](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)) — caching mechanics.
- [[Resources/Claude Managed Agents overview|Claude Managed Agents overview]] ([link](https://platform.claude.com/docs/en/managed-agents/overview)) — provider-side cost controls. ·  also cited by 3 other lessons


%% ── my notes ── %%
