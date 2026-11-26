---
id: "lesson:15/15"
type: lesson
ref: 15/15
phase: 15
num: 15
title: "Human-in-the-Loop: Propose-Then-Commit"
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
  - 15/15
  - 15-15
tags:
  - phase/15
  - type/learn
  - community/35
  - stdlib-only
source: ai-engineering-from-scratch/phases/15-autonomous-systems/15-propose-then-commit/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/15-autonomous-systems/15-propose-then-commit"
---

# 15/15 Human-in-the-Loop: Propose-Then-Commit

> The 2026 consensus on HITL is specific. It is not "the agent asks, the user clicks Approve." It is propose-then-commit: the proposed action is persisted to a durable store with an idempotency key; surfaced to a reviewer with intent, data lineage, permissions touched, blast radius, and a rollback plan; committed only after positive acknowledgement; verified after execution to confirm the side effect actually happened. LangGraph's `interrupt()` plus PostgreSQL checkpointing, Microsoft Agent Framework's `RequestInfoEvent`, and Cloudflare's `waitForApproval()` all implement the same shape. The canonical failure mode is the rubber-stamp approval: "Approve?" is clicked without review. The documented mitigation is challenge-and-response with an explicit checklist.

**Phase:** [[Phases/15 Autonomous Systems|Phase 15: Autonomous Systems]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/15-autonomous-systems/15-propose-then-commit/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/15-autonomous-systems/15-propose-then-commit) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/15-autonomous-systems/15-propose-then-commit) · code: main.py  
**Community:** [[Communities/35 Checkpoint · Durable Execution · Idempotency|35 Checkpoint · Durable Execution · Idempotency]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 15 · 12 (Durable execution), Phase 15 · 14 (Tripwires)`

- [[Lessons/15-12 Long-Running Background Agents- Durable Execution|15/12 Long-Running Background Agents: Durable Execution]] — Durable execution
- [[Lessons/15-14 Kill Switches, Circuit Breakers, and Canary Tokens|15/14 Kill Switches, Circuit Breakers, and Canary Tokens]] — Tripwires

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/15-01 The Shift from Chatbots to Long-Horizon Agents|15/01 The Shift from Chatbots to Long-Horizon Agents]], [[Lessons/15-10 Permission Modes for Autonomous Agents|15/10 Permission Modes for Autonomous Agents]], [[Lessons/15-13 Action Budgets, Iteration Caps, and Cost Governors|15/13 Action Budgets, Iteration Caps, and Cost Governors]]
- depth 3: [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]], [[Lessons/15-09 The Autonomous Coding Agent Landscape (2026)|15/09 The Autonomous Coding Agent Landscape (2026)]]

## Builds on this

- [[Lessons/15-16 Checkpoints and Rollback|15/16 Checkpoints and Rollback]]

## Concepts taught

- Propose-then-commit `lesson term` — Persisted proposal + positive commit + verify
- [[Concepts/Idempotency|Idempotency]] (as *Idempotency key*) `glossary` — Unique per proposal; second execution no-ops
- [[Concepts/Data Lineage|Data Lineage]] `glossary` — The specific source content that led to the proposal
- [[Concepts/Blast radius|Blast radius]] `lesson term` — Scope of effect if the action goes wrong
- Rubber-stamp `lesson term` — "Approve" clicked without genuine review
- Challenge-and-response `lesson term` — Reviewer must positively acknowledge specific questions
- RequestInfoEvent `lesson term` — Durable HITL request with structured metadata
- interrupt / waitForApproval() (as *interrupt() / waitForApproval()*) `lesson term` — LangGraph / Cloudflare equivalents of the same shape

## Ships

- [[Artifacts/15-15 hitl-design|hitl-design]] `skill` — Review a proposed Human-in-the-Loop workflow for propose-then-commit shape and flag missing metadata, idempotency, verification, or challenge-and-response layers.

## Further reading

- [[Resources/Anthropic — Claude's Constitution (January 2026)|Anthropic — Claude's Constitution (January 2026)]] ([link](https://www.anthropic.com/news/claudes-constitution)) — constitutional framing around oversight. ·  also cited by 6 other lessons
- [[Resources/Anthropic — Measuring AI agent autonomy in practice|Anthropic — Measuring AI agent autonomy in practice]] ([link](https://www.anthropic.com/research/measuring-agent-autonomy)) — HITL as a mitigation for long-horizon risk. ·  also cited by 16 other lessons
- [[Resources/EU AI Act — Article 14- Human oversight|EU AI Act — Article 14: Human oversight]] ([link](https://artificialintelligenceact.eu/article/14/)) — regulatory baseline for high-risk systems. ·  also cited by 1 other lesson
- [[Resources/Cloudflare Agents — Human in the loop|Cloudflare Agents — Human in the loop]] ([link](https://developers.cloudflare.com/agents/concepts/human-in-the-loop/)) — `waitForApproval()` and Durable Objects. ·  also cited by 1 other lesson
- [[Resources/Microsoft — Agent Framework- human-in-the-loop and checkpointing|Microsoft — Agent Framework: human-in-the-loop and checkpointing]] ([link](https://learn.microsoft.com/en-us/agent-framework/workflows/human-in-the-loop)) — `RequestInfoEvent`, durable approvals. ·  also cited by 4 other lessons


%% ── my notes ── %%
