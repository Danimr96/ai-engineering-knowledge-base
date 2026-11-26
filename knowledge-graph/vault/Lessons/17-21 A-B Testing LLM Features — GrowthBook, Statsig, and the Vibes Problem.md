---
id: "lesson:17/21"
type: lesson
ref: 17/21
phase: 17
num: 21
title: "A/B Testing LLM Features — GrowthBook, Statsig, and the Vibes Problem"
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 6
code_files: 1
concepts: 11
prereqs: 2
community: 30
aliases:
  - 17/21
  - 17-21
tags:
  - phase/17
  - type/learn
  - community/30
  - stdlib-only
source: ai-engineering-from-scratch/phases/17-infrastructure-and-production/21-ab-testing-llm-features/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/21-ab-testing-llm-features"
---

# 17/21 A/B Testing LLM Features — GrowthBook, Statsig, and the Vibes Problem

> Traditional A/B testing was not built for non-deterministic LLMs. The critical distinction: evals answer "can the model do the job?" A/B tests answer "do users care?" Both are required; shipping on vibe checks is over. What to test in 2026: prompt engineering (wording), model selection (GPT-4 vs GPT-3.5 vs OSS; accuracy vs cost vs latency), generation parameters (temperature, top-p). Real cases: a chatbot reward-model variant delivered +70% conversation length and +30% retention; Nextdoor AI subject-line experiments delivered +1% CTR after reward-function refinement; Khan Academy Khanmigo iterated on a latency-vs-math-accuracy axis. Platform split: **Statsig** (acquired by OpenAI for $1.1B in September 2025) — sequential testing, CUPED, all-in-one. **GrowthBook** — open-source, warehouse-native, Bayesian + Frequentist + Sequential engines, CUPED, SRM checks, Benjamini-Hochberg + Bonferroni corrections. You pick based on warehouse-SQL preference and whether "acquired by OpenAI" matters to your organization.

**Phase:** [[Phases/17 Infrastructure & Production|Phase 17: Infrastructure & Production]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/17-infrastructure-and-production/21-ab-testing-llm-features/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/21-ab-testing-llm-features) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/17-infrastructure-and-production/21-ab-testing-llm-features) · code: main.py · quiz: 6 questions  
**Community:** [[Communities/30 Evaluation (Eval) · Kill switch · Non-determinism|30 Evaluation (Eval) · Kill switch · Non-determinism]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 17 · 13 (Observability), Phase 17 · 20 (Progressive Deployment)`

- [[Lessons/17-13 LLM Observability Stack Selection|17/13 LLM Observability Stack Selection]] — Observability
- [[Lessons/17-20 Shadow Traffic, Canary Rollout, and Progressive Deployment for LLMs|17/20 Shadow Traffic, Canary Rollout, and Progressive Deployment for LLMs]] — Progressive Deployment

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/17-08 Inference Metrics — TTFT, TPOT, ITL, Goodput, P99|17/08 Inference Metrics — TTFT, TPOT, ITL, Goodput, P99]]
- depth 3: [[Lessons/17-04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill|17/04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill]]

## Builds on this

- [[Lessons/17-20 Shadow Traffic, Canary Rollout, and Progressive Deployment for LLMs|17/20 Shadow Traffic, Canary Rollout, and Progressive Deployment for LLMs]]

## Concepts taught

- [[Concepts/Evaluation (Eval)|Evaluation (Eval)]] (as *Eval*) `glossary` — Labeled-set evaluation of model capability
- A/B test `lesson term` — Live randomized comparison on users
- CUPED `lesson term` — Pre-period regression to reduce variance
- Sequential test `lesson term` — Always-valid procedure allowing early stop
- Multiple comparison `lesson term` — Running many tests inflates false positives
- Bonferroni `lesson term` — Divide α by number of tests
- Benjamini-Hochberg `lesson term` — False-discovery-rate control, less conservative
- SRM `lesson term` — Sample ratio mismatch; assignment bug
- Statsig `lesson term` — Commercial all-in-one, acquired 2025
- GrowthBook `lesson term` — MIT warehouse-native platform
- mSPRT `lesson term` — Classical sequential procedure

## Ships

- [[Artifacts/17-21 ab-plan|ab-plan]] `skill` — Design an LLM A/B test — pick platform (Statsig or GrowthBook), primary metric, guardrails, sample size with LLM-noise buffer, CUPED, sequential stopping, and multiple-comparison correction.

## Further reading

- Howard — Confidence Sequences ([link](https://arxiv.org/abs/1810.08240))
- GrowthBook — How to A/B Test AI ([link](https://blog.growthbook.io/how-to-a-b-test-ai-a-practical-guide/))
- Deng et al. — CUPED ([link](https://www.exp-platform.com/Documents/2013-02-CUPED-ImprovingSensitivityOfControlledExperiments.pdf))
- Statsig — Beyond Prompts: Data-Driven LLM Optimization ([link](https://www.statsig.com/blog/llm-optimization-online-experimentation))
- Statsig vs GrowthBook comparison ([link](https://www.statsig.com/perspectives/ab-testing-feature-flags-comparison-tools))

## In learning paths

- [[Paths/AI Evaluation and Reliability|AI Evaluation and Reliability]] — step 8, required


%% ── my notes ── %%
