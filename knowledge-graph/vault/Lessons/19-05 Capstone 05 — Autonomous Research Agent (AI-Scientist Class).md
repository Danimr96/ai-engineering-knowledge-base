---
id: "lesson:19/05"
type: lesson
ref: 19/05
phase: 19
num: 5
title: "Capstone 05 — Autonomous Research Agent (AI-Scientist Class)"
lesson_type: capstone
languages:
  - Python
  - LaTeX
time_min: 2400
on_route: false
quiz_count: 7
code_files: 1
concepts: 7
prereqs: 0
community: 14
aliases:
  - 19/05
  - 19-05
tags:
  - phase/19
  - type/capstone
  - community/14
  - stdlib-only
source: ai-engineering-from-scratch/phases/19-capstone-projects/05-autonomous-research-agent/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/05-autonomous-research-agent"
---

# 19/05 Capstone 05 — Autonomous Research Agent (AI-Scientist Class)

> Sakana's AI-Scientist-v2 published full papers. Agent Laboratory ran the experiments. Allen AI shared traces. The 2026 shape is plan-execute-verify tree search over experiments, budgeted cost, sandboxed code execution, a vision-feedback LaTeX writer, and an automated NeurIPS-style reviewer ensemble. The capstone is to build one, run it end to end within $30 per paper, and survive the sandbox-escape red team that Sakana documented.

**Phase:** [[Phases/19 Capstone Projects|Phase 19: Capstone Projects]] · **Type:** Capstone · **Time:** 2400 min · **Languages:** Python, LaTeX · **Status:** —  
**Open:** [[Upstream/19-capstone-projects/05-autonomous-research-agent/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/05-autonomous-research-agent) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/19-capstone-projects/05-autonomous-research-agent) · code: main.py · quiz: 7 questions  
**Community:** [[Communities/14 Least Privilege · Prompt Injection · Sandbox|14 Least Privilege · Prompt Injection · Sandbox]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 2 (ML), Phase 3 (deep learning), Phase 7 (transformers), Phase 10 (LLMs from scratch), Phase 14 (agents), Phase 15 (autonomous), Phase 16 (multi-agent), Phase 18 (safety)`

- Whole phase: [[Phases/10 LLMs from Scratch|Phase 10: LLMs from Scratch]] — LLMs from scratch ·  medium confidence
- Whole phase: [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] — agents ·  medium confidence
- Whole phase: [[Phases/15 Autonomous Systems|Phase 15: Autonomous Systems]] — autonomous ·  medium confidence
- Whole phase: [[Phases/16 Multi-Agent & Swarms|Phase 16: Multi-Agent & Swarms]] — multi-agent ·  medium confidence
- Whole phase: [[Phases/18 Ethics, Safety & Alignment|Phase 18: Ethics, Safety & Alignment]] — safety ·  medium confidence
- Whole phase: [[Phases/02 ML Fundamentals|Phase 2: ML Fundamentals]] — ML ·  medium confidence
- Whole phase: [[Phases/03 Deep Learning Core|Phase 3: Deep Learning Core]] — deep learning ·  medium confidence
- Whole phase: [[Phases/07 Transformers Deep Dive|Phase 7: Transformers Deep Dive]] — transformers ·  medium confidence

## Concepts taught

- Tree search `lesson term` — Best-first exploration over experiment nodes with a novelty×quality×budget score
- [[Concepts/Sandbox|Sandbox]] `glossary` — Container with no network, bounded CPU/memory, pinned seeds, read-only inputs
- Vision critique `lesson term` — Compile the paper to PDF, feed the PDF back to a VLM for layout and claim-evidence critique
- Reviewer ensemble `lesson term` — Multiple LLM judges scoring the paper with a NeurIPS rubric; weighted aggregate gates the pipeline
- Novelty score `lesson term` — Heuristic that penalizes proximity to the 50-paper literature cache
- Cost ceiling `lesson term` — Hard cap on total spend per paper; Langfuse counters + pre-run estimates
- [[Concepts/Red Teaming|Red Teaming]] (as *Red team*) `glossary` — Adversarial tasks that would escape the sandbox if the policy is wrong

## Ships

- [[Artifacts/19-05 ai-scientist|ai-scientist]] `skill` — Build an autonomous research agent that runs experiment tree search, writes LaTeX papers with vision critique, and passes a sandbox-escape red team.

## Further reading

- Semantic Scholar Graph API ([link](https://api.semanticscholar.org/)) — literature search
- [[Resources/Sakana AI Scientist v1 paper|Sakana AI Scientist v1 paper]] ([link](https://arxiv.org/abs/2408.06292)) — the original methodology ·  also cited by 1 other lesson
- E2B sandboxes ([link](https://e2b.dev)) — reference experiment isolation
- Sakana AI-Scientist-v2 repository ([link](https://github.com/SakanaAI/AI-Scientist-v2)) — the reference production research agent
- Agent Laboratory (AMD) ([link](https://github.com/SamuelSchmidgall/AgentLaboratory)) — multi-role research-lab framework
- [[Resources/LangGraph documentation|LangGraph documentation]] ([link](https://langchain-ai.github.io/langgraph/)) — reference orchestration layer ·  also cited by 3 other lessons
- NeurIPS reviewer guidelines ([link](https://neurips.cc/Conferences/2026/Reviewer-Guidelines)) — the rubric the reviewer ensemble encodes
- ShinkaEvolve (Sakana ICLR 2026) ([link](https://sakana.ai)) — evolutionary extension


%% ── my notes ── %%
