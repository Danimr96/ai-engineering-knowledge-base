---
id: "lesson:17/16"
type: lesson
ref: 17/16
phase: 17
num: 16
title: Model Routing as a Cost-Reduction Primitive
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 6
code_files: 2
concepts: 9
prereqs: 2
aliases:
  - 17/16
  - 17-16
tags:
  - phase/17
  - type/learn
  - stdlib-only
source: ai-engineering-from-scratch/phases/17-infrastructure-and-production/16-model-routing/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/16-model-routing"
---

# 17/16 Model Routing as a Cost-Reduction Primitive

> A dynamic broker evaluates every request (task type, token length, embedding similarity, confidence) and sends simple queries to a cheap model, escalating complex ones to a frontier model. Also called model cascading. Production case studies show 20-60% cost reduction at iso-quality across US/UK/EU deployments; a 30% routing efficiency improvement on high-volume SaaS turns into six-figure annual savings. The 2026 context is that LLM inference prices dropped ~10x per year — a GPT-4-class token went from $20/M to ~$0.40/M from late 2022 to 2026. Most of the drop is better serving stacks (Phase 17 · 04-09), not hardware. Routing is how you convert that price drop into margin without product regression. The failure mode is cheap-model drift: the route pushes 40% to a weaker model, quality drops 3-5% on reasoning tasks, no one notices for a quarter. Gate routes by online quality metrics, not just offline eval sets.

**Phase:** [[Phases/17 Infrastructure & Production|Phase 17: Infrastructure & Production]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/17-infrastructure-and-production/16-model-routing/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/16-model-routing) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/17-infrastructure-and-production/16-model-routing) · code: main.py, main.ts · quiz: 6 questions  
**Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 17 · 01 (Managed LLM Platforms), Phase 17 · 19 (AI Gateways)`

- [[Lessons/17-01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI|17/01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI]] — Managed LLM Platforms
- [[Lessons/17-19 AI Gateways — LiteLLM, Portkey, Kong AI Gateway, Bifrost|17/19 AI Gateways — LiteLLM, Portkey, Kong AI Gateway, Bifrost]] — AI Gateways

## Builds on this

- [[Lessons/17-19 AI Gateways — LiteLLM, Portkey, Kong AI Gateway, Bifrost|17/19 AI Gateways — LiteLLM, Portkey, Kong AI Gateway, Bifrost]]

## Concepts taught

- [[Concepts/Model routing|Model routing]] `lesson term` — Dynamic choice of model per request
- Model cascade `lesson term` — Run cheap, fall through to frontier on low confidence
- Pre-route `lesson term` — Classifier up front; no re-run
- Ensemble route `lesson term` — Run multiple, reward-model picks best
- Escalation rate `lesson term` — Fraction of cascade requests that escalated
- RouteLLM `lesson term` — OSS router library
- Not Diamond `lesson term` — SaaS model-routing product
- [[Concepts/Drift|Drift]] `lesson term` — Distribution shift without router noticing
- Online quality gate `lesson term` — Automated LLM-judge sampling live traffic

## Ships

- [[Artifacts/17-16 router-plan|router-plan]] `skill` — Design an LLM model-routing plan — pick pattern (pre-route, cascade, ensemble), signals (task, length, embedding, confidence), and online quality gates.

## Further reading

- AbhyashSuchi — Model Routing LLM 2026 Best Practices ([link](https://abhyashsuchi.in/model-routing-llm-2026-best-practices/))
- Lukas Brunner — Rise of Inference Optimization 2026 ([link](https://dev.to/lukas_brunner/the-rise-of-inference-optimization-the-real-llm-infra-trend-shaping-2026-4e4o))
- RouteLLM paper / code ([link](https://github.com/lm-sys/RouteLLM))
- [[Resources/Not Diamond|Not Diamond]] ([link](https://www.notdiamond.ai)) ·  also cited by 1 other lesson
- OpenRouter ([link](https://openrouter.ai/)) — multi-model gateway with routing primitives.


%% ── my notes ── %%
