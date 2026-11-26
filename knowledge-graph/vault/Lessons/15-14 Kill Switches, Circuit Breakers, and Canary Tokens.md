---
id: "lesson:15/14"
type: lesson
ref: 15/14
phase: 15
num: 14
title: "Kill Switches, Circuit Breakers, and Canary Tokens"
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
  - 15/14
  - 15-14
tags:
  - phase/15
  - type/learn
  - community/29
  - stdlib-only
source: ai-engineering-from-scratch/phases/15-autonomous-systems/14-kill-switches-canaries/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/15-autonomous-systems/14-kill-switches-canaries"
---

# 15/14 Kill Switches, Circuit Breakers, and Canary Tokens

> A kill switch is a boolean held outside the agent's edit surface — a Redis key, a feature flag, a signed config — that disables the agent entirely. A circuit breaker is finer-grained: it trips on a specific pattern (five identical tool calls in a row), pauses the offending path, and escalates to a human. A canary token inherits from classical deception: a fake credential or honeypot record an agent has no legitimate reason to touch, whose access triggers an alert. eBPF-based datapaths (e.g. Cilium) can rewrite a quarantined pod's egress to a forensic honeypot at the kernel layer; published Cilium benchmarks report sub-millisecond P99 datapath latency under load (your propagation budget depends on how a policy update reaches the node, not the datapath itself). Statistical detectors (EWMA, CUSUM) that adapt to a moving baseline will quietly accept drift — layer them with hard constitutional limits that do not bend.

**Phase:** [[Phases/15 Autonomous Systems|Phase 15: Autonomous Systems]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/15-autonomous-systems/14-kill-switches-canaries/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/15-autonomous-systems/14-kill-switches-canaries) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/15-autonomous-systems/14-kill-switches-canaries) · code: main.py  
**Community:** [[Communities/29 Eval-context gaming · Time horizon · thread_id|29 Eval-context gaming · Time horizon · thread_id]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 15 · 13 (Cost governors), Phase 15 · 10 (Permission modes)`

- [[Lessons/15-10 Permission Modes for Autonomous Agents|15/10 Permission Modes for Autonomous Agents]] — Permission modes
- [[Lessons/15-13 Action Budgets, Iteration Caps, and Cost Governors|15/13 Action Budgets, Iteration Caps, and Cost Governors]] — Cost governors

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/15-01 The Shift from Chatbots to Long-Horizon Agents|15/01 The Shift from Chatbots to Long-Horizon Agents]], [[Lessons/15-09 The Autonomous Coding Agent Landscape (2026)|15/09 The Autonomous Coding Agent Landscape (2026)]], [[Lessons/15-12 Long-Running Background Agents- Durable Execution|15/12 Long-Running Background Agents: Durable Execution]]
- depth 3: [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]], [[Lessons/14-07 Agent Memory — Virtual Context and Memory Paging|14/07 Agent Memory — Virtual Context and Memory Paging]]

## Builds on this

- [[Lessons/15-15 Human-in-the-Loop- Propose-Then-Commit|15/15 Human-in-the-Loop: Propose-Then-Commit]]

## Concepts taught

- [[Concepts/Kill switch|Kill switch]] `lesson term` — Boolean outside the agent's edit surface; checked on every consequential action
- [[Concepts/Circuit Breaker|Circuit Breaker]] `glossary` — Action-specific trip on repetition, failure rate, or rate-limit
- Canary token `lesson term` — Bait the agent has no legitimate reason to touch; access fires an alert
- Honeypot `lesson term` — Redirected traffic / workspace where a quarantined agent is observed
- EWMA `lesson term` — Exponentially weighted; adapts to drift (feature + bug)
- CUSUM `lesson term` — Detects sustained shift from baseline
- Hard limit `lesson term` — Does not adapt; constant regardless of history
- Constitutional limit `lesson term` — Tied to Lesson 17's constitution; cannot be edited by the agent

## Ships

- [[Artifacts/15-14 tripwire-design|tripwire-design]] `skill` — Review a proposed agent detector stack (kill switch, circuit breakers, canary tokens) and flag missing tripwires before the first autonomous run.

## Further reading

- [[Resources/Anthropic — Claude's Constitution (January 2026)|Anthropic — Claude's Constitution (January 2026)]] ([link](https://www.anthropic.com/news/claudes-constitution)) — hardcoded prohibitions as "constitutional limits". ·  also cited by 6 other lessons
- [[Resources/Anthropic — Measuring AI agent autonomy in practice|Anthropic — Measuring AI agent autonomy in practice]] ([link](https://www.anthropic.com/research/measuring-agent-autonomy)) — kill-switch and circuit-breaker framing for autonomous agents. ·  also cited by 16 other lessons
- Cilium — Network policy and eBPF ([link](https://docs.cilium.io/en/stable/security/network/)) — pod-level egress redirect and forensic honeypot patterns.
- [[Resources/Microsoft — Agent Framework- human-in-the-loop and checkpointing|Microsoft — Agent Framework: human-in-the-loop and checkpointing]] ([link](https://learn.microsoft.com/en-us/agent-framework/workflows/human-in-the-loop)) — production governance patterns. ·  also cited by 4 other lessons
- [[Resources/OWASP Top 10 for LLM Applications|OWASP Top 10 for LLM Applications]] ([link](https://owasp.org/www-project-top-10-for-large-language-model-applications/)) — detection-and-response requirements. ·  also cited by 1 other lesson


%% ── my notes ── %%
