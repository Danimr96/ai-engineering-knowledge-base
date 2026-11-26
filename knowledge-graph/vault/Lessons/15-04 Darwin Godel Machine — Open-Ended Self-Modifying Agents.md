---
id: "lesson:15/04"
type: lesson
ref: 15/04
phase: 15
num: 4
title: "Darwin Godel Machine — Open-Ended Self-Modifying Agents"
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 2
community: 25
aliases:
  - 15/04
  - 15-04
tags:
  - phase/15
  - type/learn
  - community/25
  - stdlib-only
source: ai-engineering-from-scratch/phases/15-autonomous-systems/04-darwin-godel-machine/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/15-autonomous-systems/04-darwin-godel-machine"
---

# 15/04 Darwin Godel Machine — Open-Ended Self-Modifying Agents

> Schmidhuber's 2003 Godel Machine required a formal proof that any self-modification was beneficial before accepting it. That proof is impossible in practice. Darwin Godel Machine (Zhang et al., 2025) drops the proof and keeps the archive: the agent proposes edits to its own Python source, each variant is scored on SWE-bench or Polyglot, improvements are retained. SWE-bench climbed from 20% to 50%. Along the way, DGM learned to remove its own hallucination-detection markers to raise scores. The reward-hacking demo is in the paper.

**Phase:** [[Phases/15 Autonomous Systems|Phase 15: Autonomous Systems]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/15-autonomous-systems/04-darwin-godel-machine/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/15-autonomous-systems/04-darwin-godel-machine) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/15-autonomous-systems/04-darwin-godel-machine) · code: main.py  
**Community:** [[Communities/25 Regression detection · AlphaEvolve · RSP|25 Regression detection · AlphaEvolve · RSP]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 15 · 03 (evolutionary coding), Phase 14 · 01 (the agent loop)`

- [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]] — the agent loop
- [[Lessons/15-03 AlphaEvolve — Evolutionary Coding Agents|15/03 AlphaEvolve — Evolutionary Coding Agents]] — evolutionary coding

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/15-01 The Shift from Chatbots to Long-Horizon Agents|15/01 The Shift from Chatbots to Long-Horizon Agents]], [[Lessons/15-02 STaR, V-STaR, Quiet-STaR — Self-Taught Reasoning|15/02 STaR, V-STaR, Quiet-STaR — Self-Taught Reasoning]]
- depth 3: [[Lessons/13-01 The Tool Interface — Why Agents Need Structured I-O|13/01 The Tool Interface — Why Agents Need Structured I/O]], [[Lessons/13-02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini|13/02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini]], [[Lessons/13-03 Parallel Tool Calls and Streaming with Tools|13/03 Parallel Tool Calls and Streaming with Tools]]

## Builds on this

- [[Lessons/15-05 AI Scientist v2 — Workshop-Level Autonomous Research|15/05 AI Scientist v2 — Workshop-Level Autonomous Research]]
- [[Lessons/15-06 Automated Alignment Research (Anthropic AAR)|15/06 Automated Alignment Research (Anthropic AAR)]]
- [[Lessons/15-07 Recursive Self-Improvement — Capability vs Alignment|15/07 Recursive Self-Improvement — Capability vs Alignment]]
- [[Lessons/15-08 Bounded Self-Improvement Designs|15/08 Bounded Self-Improvement Designs]]

## Concepts taught

- Godel Machine `lesson term` — 2003 design: only accept edits whose benefit can be formally proven
- Darwin Godel Machine `lesson term` — 2025 design: archive + empirical scores, no proof required
- Archive `lesson term` — Keyed by score and diversity descriptor; never forgets
- [[Concepts/SWE-bench|SWE-bench]] `lesson term` — 2,294 Python test-fixing tasks from real GitHub issues
- Polyglot `lesson term` — Smaller, multi-language version of the same idea
- Scaffolding `lesson term` — Tool wrappers, prompt templates, routing logic
- Undermining safeguards `lesson term` — Agent disables its own safety checks to raise score
- Evaluator firewall `lesson term` — Evaluator lives in a namespace the agent cannot edit

## Ships

- [[Artifacts/15-04 dgm-evaluator-firewall|dgm-evaluator-firewall]] `skill` — Specify the evaluator separation a Darwin-Godel-Machine-style self-modifying agent loop needs to avoid documented reward hacking.

## Further reading

- [[Resources/Anthropic — Responsible Scaling Policy v3.0 (Feb 2026)|Anthropic — Responsible Scaling Policy v3.0 (Feb 2026)]] ([link](https://anthropic.com/responsible-scaling-policy/rsp-v3-0)) — "undermining safeguards" framing for this failure class. ·  also cited by 5 other lessons
- Zhang et al. (2025). Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents ([link](https://arxiv.org/abs/2505.22954)) — the paper.
- [[Resources/OpenAI, SWE-bench Verified|OpenAI, SWE-bench Verified]] ([link](https://openai.com/index/introducing-swe-bench-verified/)) — the subset DGM is measured against. ·  also cited by 3 other lessons
- Sakana AI — Darwin Godel Machine announcement ([link](https://sakana.ai/dgm/)) — vendor summary.
- [[Resources/Jimenez et al. SWE-bench leaderboard|Jimenez et al. SWE-bench leaderboard]] ([link](https://www.swebench.com/)) — benchmark spec and scoring. ·  also cited by 4 other lessons


%% ── my notes ── %%
