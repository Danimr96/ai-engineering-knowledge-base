---
id: "lesson:15/05"
type: lesson
ref: 15/05
phase: 15
num: 5
title: "AI Scientist v2 — Workshop-Level Autonomous Research"
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
  - 15/05
  - 15-05
tags:
  - phase/15
  - type/learn
  - community/25
  - stdlib-only
source: ai-engineering-from-scratch/phases/15-autonomous-systems/05-ai-scientist-v2/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/15-autonomous-systems/05-ai-scientist-v2"
---

# 15/05 AI Scientist v2 — Workshop-Level Autonomous Research

> Sakana's AI Scientist v2 (Yamada et al., arXiv:2504.08066) runs the full research loop: hypothesis, code, experiments, figures, writeup, submission. It is the first system to have a generated paper pass peer review at an ICLR 2025 workshop. Independent evaluation (Beel et al.) found 42% of experiments failed from coding errors and literature review frequently mislabeled established concepts as novel. Sakana's own docs warn that the codebase executes LLM-written code and recommend Docker isolation. Both halves of that picture are the point.

**Phase:** [[Phases/15 Autonomous Systems|Phase 15: Autonomous Systems]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/15-autonomous-systems/05-ai-scientist-v2/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/15-autonomous-systems/05-ai-scientist-v2) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/15-autonomous-systems/05-ai-scientist-v2) · code: main.py  
**Community:** [[Communities/25 Regression detection · AlphaEvolve · RSP|25 Regression detection · AlphaEvolve · RSP]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 15 · 03 (AlphaEvolve), Phase 15 · 04 (DGM)`

- [[Lessons/15-03 AlphaEvolve — Evolutionary Coding Agents|15/03 AlphaEvolve — Evolutionary Coding Agents]] — AlphaEvolve
- [[Lessons/15-04 Darwin Godel Machine — Open-Ended Self-Modifying Agents|15/04 Darwin Godel Machine — Open-Ended Self-Modifying Agents]] — DGM

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]], [[Lessons/15-01 The Shift from Chatbots to Long-Horizon Agents|15/01 The Shift from Chatbots to Long-Horizon Agents]], [[Lessons/15-02 STaR, V-STaR, Quiet-STaR — Self-Taught Reasoning|15/02 STaR, V-STaR, Quiet-STaR — Self-Taught Reasoning]]
- depth 3: [[Lessons/13-01 The Tool Interface — Why Agents Need Structured I-O|13/01 The Tool Interface — Why Agents Need Structured I/O]], [[Lessons/13-02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini|13/02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini]], [[Lessons/13-03 Parallel Tool Calls and Streaming with Tools|13/03 Parallel Tool Calls and Streaming with Tools]]

## Builds on this

- [[Lessons/15-06 Automated Alignment Research (Anthropic AAR)|15/06 Automated Alignment Research (Anthropic AAR)]]

## Concepts taught

- AI Scientist v1 `lesson term` — Filled experiments into a fixed scaffold
- AI Scientist v2 `lesson term` — Agentic tree search with VLM figure critique
- Agentic tree search `lesson term` — Expands multiple experiment plans in parallel; prunes by internal critic
- Vision-language critique `lesson term` — Multimodal model reads figures and rewrites them for clarity
- Literature retrieval `lesson term` — Searches prior work to confirm idea novelty — documented to mislabel
- Polish masking `lesson term` — Presentation quality exceeds experimental quality; hides weaknesses
- Sandbox escape `lesson term` — Agent-executed code does things the loop designer did not intend

## Ships

- [[Artifacts/15-05 ai-scientist-sandbox-review|ai-scientist-sandbox-review]] `skill` — Two-gate review checklist for research-loop agent outputs before anything leaves the sandbox.

## Further reading

- [[Resources/Anthropic — Measuring AI agent autonomy in practice|Anthropic — Measuring AI agent autonomy in practice]] ([link](https://www.anthropic.com/research/measuring-agent-autonomy)) — broader framing of open-ended research agents. ·  also cited by 16 other lessons
- [[Resources/Sakana AI Scientist v1 paper|Sakana AI Scientist v1 paper]] ([link](https://arxiv.org/abs/2408.06292)) — the templated predecessor. ·  also cited by 1 other lesson
- Beel et al. (2025). Independent evaluation of The AI Scientist ([link](https://arxiv.org/abs/2502.14297)) — external evaluation numbers.
- Yamada et al. (2025). The AI Scientist-v2 ([link](https://arxiv.org/abs/2504.08066)) — paper.
- Sakana blog on the Nature 2026 publication ([link](https://sakana.ai/ai-scientist-nature/)) — vendor summary with peer-review context.


%% ── my notes ── %%
