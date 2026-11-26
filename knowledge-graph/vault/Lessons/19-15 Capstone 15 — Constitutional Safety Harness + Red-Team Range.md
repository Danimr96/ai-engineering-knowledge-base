---
id: "lesson:19/15"
type: lesson
ref: 19/15
phase: 19
num: 15
title: "Capstone 15 — Constitutional Safety Harness + Red-Team Range"
lesson_type: capstone
languages:
  - Python
  - YAML
time_min: 1500
on_route: false
quiz_count: 7
code_files: 1
concepts: 8
prereqs: 0
community: 89
aliases:
  - 19/15
  - 19-15
tags:
  - phase/19
  - type/capstone
  - community/89
  - stdlib-only
source: ai-engineering-from-scratch/phases/19-capstone-projects/15-constitutional-safety-harness/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/15-constitutional-safety-harness"
---

# 19/15 Capstone 15 — Constitutional Safety Harness + Red-Team Range

> Anthropic's Constitutional Classifiers, Meta's Llama Guard 4, Google's ShieldGemma-2, NVIDIA's Nemotron 3 Content Safety, and X-Guard for multilingual coverage defined the 2026 safety-classifier stack. garak, PyRIT, NVIDIA Aegis, and promptfoo became the standard adversarial evaluation tools. NeMo Guardrails v0.12 ties them into a production pipeline. This capstone wires all of it together: a layered safety harness around a target app, an autonomous red-team agent running 6+ attack families, and a constitutional self-critique run that produces a measurable harmlessness delta.

**Phase:** [[Phases/19 Capstone Projects|Phase 19: Capstone Projects]] · **Type:** Capstone · **Time:** 1500 min · **Languages:** Python, YAML · **Status:** —  
**Open:** [[Upstream/19-capstone-projects/15-constitutional-safety-harness/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/15-constitutional-safety-harness) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/19-capstone-projects/15-constitutional-safety-harness) · code: main.py · quiz: 7 questions  
**Community:** [[Communities/89 GCG · PAIR · TAP|89 GCG · PAIR · TAP]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 10 (LLMs from scratch), Phase 11 (LLM engineering), Phase 13 (tools), Phase 14 (agents), Phase 18 (ethics, safety, alignment)`

- Whole phase: [[Phases/10 LLMs from Scratch|Phase 10: LLMs from Scratch]] — LLMs from scratch ·  medium confidence
- Whole phase: [[Phases/11 LLM Engineering|Phase 11: LLM Engineering]] — LLM engineering ·  medium confidence
- Whole phase: [[Phases/13 Tools & Protocols|Phase 13: Tools & Protocols]] — tools ·  medium confidence
- Whole phase: [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] — agents ·  medium confidence
- Whole phase: [[Phases/18 Ethics, Safety & Alignment|Phase 18: Ethics, Safety & Alignment]] — ethics, safety, alignment ·  medium confidence

## Concepts taught

- Layered safety `lesson term` — Multiple guardrails at input, gate, output, HITL
- Llama Guard 4 `lesson term` — The 2026 reference input/output content classifier
- [[Concepts/PAIR|PAIR]] `lesson term` — Paper (Chao et al.) on LLM-driven jailbreak discovery
- [[Concepts/TAP|TAP]] `lesson term` — Tree-search variant of PAIR
- [[Concepts/GCG|GCG]] `lesson term` — Gradient-based adversarial suffix attack
- Constitutional self-critique `lesson term` — Target drafts -> critic scores -> rewrite -> retrain
- XSTest `lesson term` — Benchmark for over-refusal regression
- CVSS 4.0 `lesson term` — Standard vulnerability scoring for safety findings

## Ships

- [[Artifacts/19-15 safety-harness|safety-harness]] `skill` — Wire a layered safety pipeline around a target LLM app, run a six-family red-team range, and run a constitutional self-critique for a measurable harmlessness delta.

## Further reading

- [[Resources/Anthropic — Constitutional Classifiers (2024-2026)|Anthropic — Constitutional Classifiers (2024-2026)]] ([link](https://www.anthropic.com/research/constitutional-classifiers)) — training-time reference ·  also cited by 1 other lesson
- [[Resources/Chao et al. — Jailbreaking Black Box LLMs in Twenty Queries (arXiv-2310.08419)|Chao et al. — Jailbreaking Black Box LLMs in Twenty Queries (arXiv:2310.08419)]] ([link](https://arxiv.org/abs/2310.08419)) — jailbreak agent paper ·  also cited by 3 other lessons
- X-Guard (arXiv:2504.08848) ([link](https://arxiv.org/abs/2504.08848)) — 132-language multilingual safety
- NVIDIA Nemotron 3 Content Safety ([link](https://developer.nvidia.com/blog/building-nvidia-nemotron-3-agents-for-reasoning-multimodal-rag-voice-and-safety/)) — enterprise reference
- [[Resources/NeMo Guardrails v0.12|NeMo Guardrails v0.12]] ([link](https://docs.nvidia.com/nemo-guardrails/)) — rail framework ·  also cited by 1 other lesson
- [[Resources/Microsoft PyRIT — GitHub|Microsoft PyRIT — GitHub]] ([link](https://github.com/Azure/PyRIT)) — Microsoft red-team framework ·  also cited by 1 other lesson
- [[Resources/NVIDIA Garak — GitHub|NVIDIA Garak — GitHub]] ([link](https://github.com/NVIDIA/garak)) — NVIDIA red-team toolkit ·  also cited by 1 other lesson
- Google ShieldGemma-2 ([link](https://huggingface.co/google/shieldgemma-2b)) — image + multimodal safety
- [[Resources/Meta — Llama Guard 4 model card|Meta — Llama Guard 4 model card]] ([link](https://www.llama.com/docs/model-cards-and-prompt-formats/llama-guard-4/)) — the 2026 input/output classifier ·  also cited by 2 other lessons


%% ── my notes ── %%
