---
id: "lesson:15/03"
type: lesson
ref: 15/03
phase: 15
num: 3
title: "AlphaEvolve — Evolutionary Coding Agents"
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 0
code_files: 1
concepts: 7
prereqs: 2
community: 25
aliases:
  - 15/03
  - 15-03
tags:
  - phase/15
  - type/learn
  - community/25
  - stdlib-only
source: ai-engineering-from-scratch/phases/15-autonomous-systems/03-alphaevolve-evolutionary-coding/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/15-autonomous-systems/03-alphaevolve-evolutionary-coding"
---

# 15/03 AlphaEvolve — Evolutionary Coding Agents

> Pair a frontier coding model with an evolutionary loop and a machine-checkable evaluator. Let the loop run long enough. It discovers a 4x4 complex-matrix multiplication procedure that uses 48 scalar multiplications — the first improvement over Strassen in 56 years. It also finds a Google-wide Borg scheduling heuristic that recovers ~0.7% of cluster compute in production. The architecture is boring on purpose. The wins come from the evaluator's rigor.

**Phase:** [[Phases/15 Autonomous Systems|Phase 15: Autonomous Systems]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/15-autonomous-systems/03-alphaevolve-evolutionary-coding/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/15-autonomous-systems/03-alphaevolve-evolutionary-coding) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/15-autonomous-systems/03-alphaevolve-evolutionary-coding) · code: main.py  
**Community:** [[Communities/25 Regression detection · AlphaEvolve · RSP|25 Regression detection · AlphaEvolve · RSP]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 15 · 01 (long-horizon framing), Phase 15 · 02 (self-taught reasoning)`

- [[Lessons/15-01 The Shift from Chatbots to Long-Horizon Agents|15/01 The Shift from Chatbots to Long-Horizon Agents]] — long-horizon framing
- [[Lessons/15-02 STaR, V-STaR, Quiet-STaR — Self-Taught Reasoning|15/02 STaR, V-STaR, Quiet-STaR — Self-Taught Reasoning]] — self-taught reasoning

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/13-01 The Tool Interface — Why Agents Need Structured I-O|13/01 The Tool Interface — Why Agents Need Structured I/O]], [[Lessons/13-02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini|13/02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini]], [[Lessons/13-03 Parallel Tool Calls and Streaming with Tools|13/03 Parallel Tool Calls and Streaming with Tools]], [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]]

## Builds on this

- [[Lessons/15-04 Darwin Godel Machine — Open-Ended Self-Modifying Agents|15/04 Darwin Godel Machine — Open-Ended Self-Modifying Agents]]
- [[Lessons/15-05 AI Scientist v2 — Workshop-Level Autonomous Research|15/05 AI Scientist v2 — Workshop-Level Autonomous Research]]

## Concepts taught

- [[Concepts/AlphaEvolve|AlphaEvolve]] `lesson term` — Gemini + program database + machine-checkable evaluator
- MAP-elites `lesson term` — Grid keyed by feature vectors; each cell holds the best variant with that descriptor
- Island model `lesson term` — Independent populations that migrate periodically; prevents premature convergence
- Machine-checkable evaluator `lesson term` — A unit test, simulator, or benchmark the LLM cannot fake — a prerequisite for this loop
- [[Concepts/Reward hacking|Reward hacking]] `lesson term` — Loop finds a way to maximize score without doing the intended task
- Seed program `lesson term` — An initial correct-but-suboptimal program the loop evolves from
- Held-out evaluator `lesson term` — Inputs generated at evaluation time to prevent memorization

## Ships

- [[Artifacts/15-03 evaluator-rigor-audit|evaluator-rigor-audit]] `skill` — Audit a proposed AlphaEvolve-style evolutionary coding loop's evaluator before committing any compute to the search.

## Further reading

- [[Resources/Anthropic — Responsible Scaling Policy v3.0 (Feb 2026)|Anthropic — Responsible Scaling Policy v3.0 (Feb 2026)]] ([link](https://anthropic.com/responsible-scaling-policy/rsp-v3-0)) — frames evaluator-bound autonomy as a key research direction. ·  also cited by 5 other lessons
- [[Resources/AlphaEvolve (arXiv-2506.13131)|AlphaEvolve (arXiv:2506.13131)]] ([link](https://arxiv.org/abs/2506.13131)) — the full paper. ·  also cited by 2 other lessons
- DeepMind blog on AlphaEvolve ([link](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/)) — vendor writeup with results.
- AlphaEvolve results repository ([link](https://github.com/google-deepmind/alphaevolve_results)) — discovered algorithms, including the 48-mul 4x4 matmul.
- Romera-Paredes et al. (2023). Mathematical discoveries from program search with LLMs (FunSearch) ([link](https://www.nature.com/articles/s41586-023-06924-6)) — the predecessor system.


%% ── my notes ── %%
