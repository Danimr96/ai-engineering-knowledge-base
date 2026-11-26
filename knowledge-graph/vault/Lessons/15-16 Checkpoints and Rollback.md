---
id: "lesson:15/16"
type: lesson
ref: 15/16
phase: 15
num: 16
title: Checkpoints and Rollback
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 2
community: 35
aliases:
  - 15/16
  - 15-16
tags:
  - phase/15
  - type/learn
  - community/35
  - stdlib-only
source: ai-engineering-from-scratch/phases/15-autonomous-systems/16-checkpoints-rollback/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/15-autonomous-systems/16-checkpoints-rollback"
---

# 15/16 Checkpoints and Rollback

> Every graph-state transition persists. When a worker crashes, its lease expires and another worker picks up at the latest checkpoint. Cloudflare Durable Objects hold state across hours or weeks. Propose-then-commit (Lesson 15) defines a rollback plan per action. Post-action verification closes the loop. EU AI Act Article 14 makes effective human oversight mandatory for high-risk systems — in practice this means checkpoints must be queryable, rollbacks must be rehearsed, and the audit trail must survive a deploy. The sharp failure mode: without idempotency keys and precondition checks, a retry after a transient failure can double-execute an already-approved action. Post-action verification is what catches it.

**Phase:** [[Phases/15 Autonomous Systems|Phase 15: Autonomous Systems]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/15-autonomous-systems/16-checkpoints-rollback/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/15-autonomous-systems/16-checkpoints-rollback) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/15-autonomous-systems/16-checkpoints-rollback) · code: main.py  
**Community:** [[Communities/35 Checkpoint · Durable Execution · Idempotency|35 Checkpoint · Durable Execution · Idempotency]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 15 · 12 (Durable execution), Phase 15 · 15 (Propose-then-commit)`

- [[Lessons/15-12 Long-Running Background Agents- Durable Execution|15/12 Long-Running Background Agents: Durable Execution]] — Durable execution
- [[Lessons/15-15 Human-in-the-Loop- Propose-Then-Commit|15/15 Human-in-the-Loop: Propose-Then-Commit]] — Propose-then-commit

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/15-01 The Shift from Chatbots to Long-Horizon Agents|15/01 The Shift from Chatbots to Long-Horizon Agents]], [[Lessons/15-10 Permission Modes for Autonomous Agents|15/10 Permission Modes for Autonomous Agents]], [[Lessons/15-14 Kill Switches, Circuit Breakers, and Canary Tokens|15/14 Kill Switches, Circuit Breakers, and Canary Tokens]]
- depth 3: [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]], [[Lessons/15-09 The Autonomous Coding Agent Landscape (2026)|15/09 The Autonomous Coding Agent Landscape (2026)]], [[Lessons/15-13 Action Budgets, Iteration Caps, and Cost Governors|15/13 Action Budgets, Iteration Caps, and Cost Governors]]

## Concepts taught

- [[Concepts/Checkpoint|Checkpoint]] `glossary` — Every graph-state transition persists to a durable store
- Lease `lesson term` — Short-lived claim that a worker is executing a run; expires on crash
- Precondition `lesson term` — Assertion that the state is still consistent with the approved action
- Post-action verify `lesson term` — Confirm the side effect actually happened in the target system
- In-band rollback `lesson term` — Reverse the side effect with the inverse operation
- Compensating transaction `lesson term` — A new action that neutralizes the original
- Mark-as-done-first `lesson term` — Persist the committed status before returning from commit
- Article 14 `lesson term` — Operational: queryable checkpoints, rehearsed rollbacks, auditable trail

## Ships

- [[Artifacts/15-16 rollback-rehearsal|rollback-rehearsal]] `skill` — Design a rollback-rehearsal test for a proposed autonomous workflow and audit the checkpoint backend for audit-trail persistence.

## Further reading

- [[Resources/Anthropic — Measuring AI agent autonomy in practice|Anthropic — Measuring AI agent autonomy in practice]] ([link](https://www.anthropic.com/research/measuring-agent-autonomy)) — reliability framing for long-horizon workflows. ·  also cited by 16 other lessons
- [[Resources/EU AI Act — Article 14- Human oversight|EU AI Act — Article 14: Human oversight]] ([link](https://artificialintelligenceact.eu/article/14/)) — regulatory baseline. ·  also cited by 1 other lesson
- [[Resources/Anthropic — How the agent loop works|Anthropic — How the agent loop works]] ([link](https://code.claude.com/docs/en/agent-sdk/agent-loop)) — workflow shape for Claude Code Routines. ·  also cited by 3 other lessons
- [[Resources/Cloudflare Agents — Human in the loop|Cloudflare Agents — Human in the loop]] ([link](https://developers.cloudflare.com/agents/concepts/human-in-the-loop/)) — Durable Objects as a state substrate. ·  also cited by 1 other lesson
- [[Resources/Microsoft — Agent Framework- human-in-the-loop and checkpointing|Microsoft — Agent Framework: human-in-the-loop and checkpointing]] ([link](https://learn.microsoft.com/en-us/agent-framework/workflows/human-in-the-loop)) — checkpoint primitives and lease recovery. ·  also cited by 4 other lessons


%% ── my notes ── %%
