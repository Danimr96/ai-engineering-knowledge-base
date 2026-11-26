---
id: "lesson:15/11"
type: lesson
ref: 15/11
phase: 15
num: 11
title: Browser Agents and Long-Horizon Web Tasks
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
  - 15/11
  - 15-11
tags:
  - phase/15
  - type/learn
  - community/29
  - stdlib-only
source: ai-engineering-from-scratch/phases/15-autonomous-systems/11-browser-agents/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/15-autonomous-systems/11-browser-agents"
---

# 15/11 Browser Agents and Long-Horizon Web Tasks

> ChatGPT agent (July 2025) merged Operator and deep research into one browser/terminal agent and set BrowseComp SOTA at 68.9%. OpenAI shut Operator down August 31, 2025 — consolidation at the product layer. Anthropic's Vercept acquisition moved Claude Sonnet on OSWorld from under 15% to 72.5%. WebArena-Verified (ServiceNow, ICLR 2026) fixed 11.3 percentage points of false-negative rate in the original WebArena and shipped the 258-task Hard subset. The numbers are real. So is the attack surface: OpenAI's head of preparedness stated publicly that indirect prompt injection into browser agents "is not a bug that can be fully patched." Documented 2025–2026 attacks: Tainted Memories (Atlas CSRF), HashJack (Cato Networks), and one-click hijacks in Perplexity Comet.

**Phase:** [[Phases/15 Autonomous Systems|Phase 15: Autonomous Systems]] · **Type:** Learn · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/15-autonomous-systems/11-browser-agents/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/15-autonomous-systems/11-browser-agents) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/15-autonomous-systems/11-browser-agents) · code: main.py  
**Community:** [[Communities/29 Eval-context gaming · Time horizon · thread_id|29 Eval-context gaming · Time horizon · thread_id]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 15 · 10 (Permission modes), Phase 15 · 01 (Long-horizon agents)`

- [[Lessons/15-01 The Shift from Chatbots to Long-Horizon Agents|15/01 The Shift from Chatbots to Long-Horizon Agents]] — Long-horizon agents
- [[Lessons/15-10 Permission Modes for Autonomous Agents|15/10 Permission Modes for Autonomous Agents]] — Permission modes

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]], [[Lessons/15-09 The Autonomous Coding Agent Landscape (2026)|15/09 The Autonomous Coding Agent Landscape (2026)]]
- depth 3: [[Lessons/14-07 Agent Memory — Virtual Context and Memory Paging|14/07 Agent Memory — Virtual Context and Memory Paging]]

## Concepts taught

- [[Concepts/Indirect Prompt Injection|Indirect Prompt Injection]] `glossary` — Untrusted content in a page the agent reads contains instructions the agent executes
- Tainted Memories `lesson term` — Agent writes an attacker-supplied instruction to durable memory; triggered next session
- HashJack `lesson term` — Payload hidden in URL fragment / query string is in the agent's context but not visibly rendered
- One-click hijack `lesson term` — Visible affordance rides a follow-on payload the agent executes
- BrowseComp `lesson term` — Finding specific facts on the open web; minute-scale horizon
- [[Concepts/OSWorld|OSWorld]] `lesson term` — Full OS control; multi-step GUI tasks
- WebArena-Verified `lesson term` — ServiceNow's regraded WebArena with Hard subset
- Read/write boundary `lesson term` — Reading never consequential; writing requires fresh approval if content is out-of-trust

## Ships

- [[Artifacts/15-11 browser-agent-trust-boundary|browser-agent-trust-boundary]] `skill` — Scope a proposed browser-agent deployment — trust zones, authorized writes, required defenses — before the agent touches a real site.

## Further reading

- [[Resources/Anthropic — Measuring AI agent autonomy in practice|Anthropic — Measuring AI agent autonomy in practice]] ([link](https://www.anthropic.com/research/measuring-agent-autonomy)) — includes attack-surface discussion for computer-use agents. ·  also cited by 16 other lessons
- [[Resources/OpenAI, Computer-Using Agent|OpenAI, Computer-Using Agent]] ([link](https://openai.com/index/computer-using-agent/)) — the Operator lineage and the architecture that became ChatGPT agent. ·  also cited by 3 other lessons
- OpenAI — Introducing ChatGPT agent ([link](https://openai.com/index/introducing-chatgpt-agent/)) — merge of Operator and deep research; BrowseComp SOTA.
- WebArena-Verified (OpenReview) ([link](https://openreview.net/forum?id=94tlGxmqkN)) — ICLR 2026 fixed-subset paper.
- Zhou et al. — WebArena ([link](https://webarena.dev/)) — the original benchmark.


%% ── my notes ── %%
