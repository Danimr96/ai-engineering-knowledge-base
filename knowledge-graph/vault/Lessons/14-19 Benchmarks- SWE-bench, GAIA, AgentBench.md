---
id: "lesson:14/19"
type: lesson
ref: 14/19
phase: 14
num: 19
title: "Benchmarks: SWE-bench, GAIA, AgentBench"
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 7
code_files: 1
concepts: 8
prereqs: 1
community: 31
aliases:
  - 14/19
  - 14-19
tags:
  - phase/14
  - type/learn
  - community/31
  - stdlib-only
source: ai-engineering-from-scratch/phases/14-agent-engineering/19-benchmarks-swebench-gaia/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/19-benchmarks-swebench-gaia"
---

# 14/19 Benchmarks: SWE-bench, GAIA, AgentBench

> Three benchmarks anchor agent evaluation in 2026. SWE-bench tests code patching. GAIA tests generalist tool use. AgentBench tests multi-environment reasoning. Know their composition, their contamination story, and what they do not measure.

**Phase:** [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/14-agent-engineering/19-benchmarks-swebench-gaia/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/19-benchmarks-swebench-gaia) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/14-agent-engineering/19-benchmarks-swebench-gaia) · code: main.py · quiz: 7 questions  
**Community:** [[Communities/31 GUI grounding · VisualWebArena · OSWorld|31 GUI grounding · VisualWebArena · OSWorld]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 14 · 06 (Tool Use)`

- [[Lessons/14-06 Tool Use and Function Calling|14/06 Tool Use and Function Calling]] — Tool Use

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/13-01 The Tool Interface — Why Agents Need Structured I-O|13/01 The Tool Interface — Why Agents Need Structured I/O]], [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]]

## Builds on this

- [[Lessons/14-20 Benchmarks- WebArena and OSWorld|14/20 Benchmarks: WebArena and OSWorld]]
- [[Lessons/14-30 Eval-Driven Agent Development|14/30 Eval-Driven Agent Development]]
- [[Lessons/19-27 Capstone Lesson 27- Eval Harness with Fixture Tasks|19/27 Capstone Lesson 27: Eval Harness with Fixture Tasks]]

## Concepts taught

- [[Concepts/SWE-bench|SWE-bench]] `lesson term` — 2,294 GitHub issues; patch must flip FAIL_TO_PASS tests
- [[Concepts/SWE-bench Verified|SWE-bench Verified]] `lesson term` — 500 human-curated tasks, OpenAI
- FAIL_TO_PASS `lesson term` — Tests previously failing that must pass after the patch
- PASS_TO_PASS `lesson term` — Tests that were passing and must still pass
- GAIA `lesson term` — 466 human-easy / AI-hard multi-tool questions
- AgentBench `lesson term` — 8 environments; long-horizon multi-turn
- [[Concepts/Benchmark Contamination|Benchmark Contamination]] (as *Contamination*) `glossary` — Benchmark tasks present in model training
- SWE-bench+ `lesson term` — 32.67% solution leakage found in successful SWE-bench patches

## Ships

- [[Artifacts/14-19 benchmark-harness|benchmark-harness]] `skill` — Build a SWE-bench-style harness for a codebase with FAIL_TO_PASS / PASS_TO_PASS gating, contamination checks, and step-count metrics.

## Further reading

- Liu et al., AgentBench (arXiv:2308.03688) ([link](https://arxiv.org/abs/2308.03688)) — multi-environment suite
- Jimenez et al., SWE-bench (arXiv:2310.06770) ([link](https://arxiv.org/abs/2310.06770)) — the original benchmark
- Mialon et al., GAIA (arXiv:2311.12983) ([link](https://arxiv.org/abs/2311.12983)) — generalist benchmark
- [[Resources/OpenAI, SWE-bench Verified|OpenAI, SWE-bench Verified]] ([link](https://openai.com/index/introducing-swe-bench-verified/)) — the curated subset ·  also cited by 3 other lessons


%% ── my notes ── %%
