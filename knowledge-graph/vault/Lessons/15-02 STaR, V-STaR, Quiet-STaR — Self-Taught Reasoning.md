---
id: "lesson:15/02"
type: lesson
ref: 15/02
phase: 15
num: 2
title: "STaR, V-STaR, Quiet-STaR — Self-Taught Reasoning"
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 0
code_files: 1
concepts: 7
prereqs: 4
community: 3
aliases:
  - 15/02
  - 15-02
tags:
  - phase/15
  - type/learn
  - community/03
  - stdlib-only
source: ai-engineering-from-scratch/phases/15-autonomous-systems/02-star-family-reasoning/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/15-autonomous-systems/02-star-family-reasoning"
---

# 15/02 STaR, V-STaR, Quiet-STaR — Self-Taught Reasoning

> The smallest possible self-improvement loop sits inside the rationale. A model generates a chain of thought, keeps the ones that land on correct answers, and fine-tunes on those. That is STaR. V-STaR adds a verifier so inference-time selection is better. Quiet-STaR pushes the rationale down to every token. All three work. None of them are magic — the loop preserves any shortcut that happened to reach the right answer.

**Phase:** [[Phases/15 Autonomous Systems|Phase 15: Autonomous Systems]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/15-autonomous-systems/02-star-family-reasoning/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/15-autonomous-systems/02-star-family-reasoning) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/15-autonomous-systems/02-star-family-reasoning) · code: main.py  
**Community:** [[Communities/03 Parallel tool calls · Strict mode · Refusal|03 Parallel tool calls · Strict mode · Refusal]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 13 · 01-03 (Reasoning and CoT), Phase 15 · 01 (long-horizon framing)`

- [[Lessons/15-01 The Shift from Chatbots to Long-Horizon Agents|15/01 The Shift from Chatbots to Long-Horizon Agents]] — long-horizon framing
- **13/01-03** — Reasoning and CoT:
    - [[Lessons/13-01 The Tool Interface — Why Agents Need Structured I-O|13/01 The Tool Interface — Why Agents Need Structured I/O]]
    - [[Lessons/13-02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini|13/02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini]]
    - [[Lessons/13-03 Parallel Tool Calls and Streaming with Tools|13/03 Parallel Tool Calls and Streaming with Tools]]

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]]

## Builds on this

- [[Lessons/15-03 AlphaEvolve — Evolutionary Coding Agents|15/03 AlphaEvolve — Evolutionary Coding Agents]]

## Concepts taught

- STaR `lesson term` — Fine-tune on model-generated rationales that land correct answers; repeat
- Rationalization `lesson term` — Inject the correct answer and re-prompt for a rationale on problems the base model fails
- V-STaR `lesson term` — DPO-train a verifier on both correct and incorrect rationales, use it for inference-time selection
- Quiet-STaR `lesson term` — Generate hidden thoughts at every token position; mix with baseline prediction
- Answer-conditioned gradient `lesson term` — The training loop rewards final answers, not reasoning steps
- Process reward model `lesson term` — Reward model trained on per-step correctness, not outcome — contrasts with STaR
- Shortcut rationale `lesson term` — A rationale that reaches the label via a non-generalizing pattern; STaR keeps these

## Ships

- [[Artifacts/15-02 star-loop-reviewer|star-loop-reviewer]] `skill` — Audit a proposed self-taught reasoning pipeline (STaR-family) before you commit training compute to it.

## Further reading

- Zelikman et al. (2022). STaR: Bootstrapping Reasoning With Reasoning ([link](https://arxiv.org/abs/2203.14465)) — the original paper.
- [[Resources/Lightman et al., 2023 - -Let's Verify Step by Step|Lightman et al., 2023 -- "Let's Verify Step by Step]] ([link](https://arxiv.org/abs/2305.20050)) — process reward models, the alternative gradient signal. ·  also cited by 2 other lessons
- Hosseini et al. (2024). V-STaR: Training Verifiers for Self-Taught Reasoners ([link](https://arxiv.org/abs/2402.06457)) — adds a DPO verifier for inference-time selection.
- Zelikman et al. (2024). Quiet-STaR: Language Models Can Teach Themselves to Think Before Speaking ([link](https://arxiv.org/abs/2403.09629)) — per-token internal rationales.
- [[Resources/DeepSeek-AI (2025). DeepSeek-R1- Incentivizing Reasoning Capability in LLMs via Reinforcement Learning|DeepSeek-AI (2025). DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning]] ([link](https://arxiv.org/abs/2501.12948)) — RL on verifiable tasks, STaR scaled to frontier training. ·  also cited by 4 other lessons


%% ── my notes ── %%
