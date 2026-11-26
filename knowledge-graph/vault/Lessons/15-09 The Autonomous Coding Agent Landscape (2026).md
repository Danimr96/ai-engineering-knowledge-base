---
id: "lesson:15/09"
type: lesson
ref: 15/09
phase: 15
num: 9
title: The Autonomous Coding Agent Landscape (2026)
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
  - 15/09
  - 15-09
tags:
  - phase/15
  - type/learn
  - community/29
  - stdlib-only
source: ai-engineering-from-scratch/phases/15-autonomous-systems/09-coding-agent-landscape/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/15-autonomous-systems/09-coding-agent-landscape"
---

# 15/09 The Autonomous Coding Agent Landscape (2026)

> SWE-bench Verified went from 4% to 80.9% in under three years. Same Claude Sonnet 4.5 scored 43.2% on SWE-agent v1 and 59.8% on Cline autonomous — the scaffolding around the model now matters as much as the model itself. OpenHands (formerly OpenDevin) is the most active MIT-licensed platform and its CodeAct loop executes Python actions directly in a sandbox instead of JSON tool calls. The headline numbers hide a methodological issue: 161 of 500 SWE-bench Verified tasks require only a 1–2 line change, and SWE-bench Pro (10+ line tasks) sits at 23–59% for the same frontier models.

**Phase:** [[Phases/15 Autonomous Systems|Phase 15: Autonomous Systems]] · **Type:** Learn · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/15-autonomous-systems/09-coding-agent-landscape/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/15-autonomous-systems/09-coding-agent-landscape) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/15-autonomous-systems/09-coding-agent-landscape) · code: main.py  
**Community:** [[Communities/29 Eval-context gaming · Time horizon · thread_id|29 Eval-context gaming · Time horizon · thread_id]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 14 · 07 (Tool use), Phase 15 · 01 (Long-horizon agents)`

- [[Lessons/14-07 Agent Memory — Virtual Context and Memory Paging|14/07 Agent Memory — Virtual Context and Memory Paging]] — Tool use
- [[Lessons/15-01 The Shift from Chatbots to Long-Horizon Agents|15/01 The Shift from Chatbots to Long-Horizon Agents]] — Long-horizon agents

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]], [[Lessons/14-06 Tool Use and Function Calling|14/06 Tool Use and Function Calling]]
- depth 3: [[Lessons/13-01 The Tool Interface — Why Agents Need Structured I-O|13/01 The Tool Interface — Why Agents Need Structured I/O]]

## Builds on this

- [[Lessons/15-10 Permission Modes for Autonomous Agents|15/10 Permission Modes for Autonomous Agents]]

## Concepts taught

- [[Concepts/SWE-bench|SWE-bench]] `lesson term` — Real GitHub issues with ground-truth patches and test suites
- [[Concepts/SWE-bench Verified|SWE-bench Verified]] `lesson term` — 500 human-curated tasks, easier-tail present
- [[Concepts/SWE-bench Pro|SWE-bench Pro]] `lesson term` — 10+ line changes; frontier sits at 23–59%
- CodeAct `lesson term` — Agent emits Python; Jupyter-style kernel executes in sandbox
- JSON tool call `lesson term` — Each action is a structured JSON payload validated before execution
- Scaffold `lesson term` — Retrieval + planner + executor + verifier loop around the base model
- ACI (Agent-Computer Interface) `lesson term` — Command set designed for LLM ergonomics, not human shells
- Verifier loop `lesson term` — Run tests, read output, revise patch; biggest non-model reliability gain

## Ships

- [[Artifacts/15-09 coding-scaffold-audit|coding-scaffold-audit]] `skill` — Audit a proposed coding-agent scaffold (retrieval, verifier loop, sandbox, benchmark fit) before adopting it for production code changes.

## Further reading

- [[Resources/Anthropic — Measuring AI agent autonomy in practice|Anthropic — Measuring AI agent autonomy in practice]] ([link](https://www.anthropic.com/research/measuring-agent-autonomy)) — long-horizon coding-agent reliability framing. ·  also cited by 16 other lessons
- Wang et al. — OpenHands: An Open Platform for AI Software Developers ([link](https://arxiv.org/abs/2407.16741)) — CodeAct architecture and event-stream design.
- Epoch AI — SWE-bench leaderboard ([link](https://epoch.ai/benchmarks)) — live-tracked scores.
- [[Resources/OpenAI, SWE-bench Verified|OpenAI, SWE-bench Verified]] ([link](https://openai.com/index/introducing-swe-bench-verified/)) — how the curated subset was built. ·  also cited by 3 other lessons
- [[Resources/Jimenez et al. SWE-bench leaderboard|Jimenez et al. SWE-bench leaderboard]] ([link](https://www.swebench.com/)) — the original benchmark and methodology. ·  also cited by 4 other lessons


%% ── my notes ── %%
