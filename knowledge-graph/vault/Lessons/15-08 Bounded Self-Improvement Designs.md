---
id: "lesson:15/08"
type: lesson
ref: 15/08
phase: 15
num: 8
title: Bounded Self-Improvement Designs
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
  - 15/08
  - 15-08
tags:
  - phase/15
  - type/learn
  - community/25
  - stdlib-only
source: ai-engineering-from-scratch/phases/15-autonomous-systems/08-bounded-self-improvement/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/15-autonomous-systems/08-bounded-self-improvement"
---

# 15/08 Bounded Self-Improvement Designs

> Research has converged on four primitives for bounding a self-improvement loop. Formal invariants that must hold across every edit. Alignment anchors that cannot be modified. Multi-objective constraints where every dimension (safety, fairness, robustness) must hold, not just performance. Regression detection that pauses the loop when historical metrics suggest capability loss. None of them is a proof of safety — information-theoretic results (Kolmogorov complexity, Lob's theorem) bound what any system can prove about its own successors. They are mitigations that raise the cost of silent failure.

**Phase:** [[Phases/15 Autonomous Systems|Phase 15: Autonomous Systems]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/15-autonomous-systems/08-bounded-self-improvement/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/15-autonomous-systems/08-bounded-self-improvement) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/15-autonomous-systems/08-bounded-self-improvement) · code: main.py  
**Community:** [[Communities/25 Regression detection · AlphaEvolve · RSP|25 Regression detection · AlphaEvolve · RSP]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 15 · 07 (RSI), Phase 15 · 04 (DGM)`

- [[Lessons/15-04 Darwin Godel Machine — Open-Ended Self-Modifying Agents|15/04 Darwin Godel Machine — Open-Ended Self-Modifying Agents]] — DGM
- [[Lessons/15-07 Recursive Self-Improvement — Capability vs Alignment|15/07 Recursive Self-Improvement — Capability vs Alignment]] — RSI

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]], [[Lessons/15-03 AlphaEvolve — Evolutionary Coding Agents|15/03 AlphaEvolve — Evolutionary Coding Agents]], [[Lessons/15-06 Automated Alignment Research (Anthropic AAR)|15/06 Automated Alignment Research (Anthropic AAR)]]
- depth 3: [[Lessons/15-01 The Shift from Chatbots to Long-Horizon Agents|15/01 The Shift from Chatbots to Long-Horizon Agents]], [[Lessons/15-02 STaR, V-STaR, Quiet-STaR — Self-Taught Reasoning|15/02 STaR, V-STaR, Quiet-STaR — Self-Taught Reasoning]], [[Lessons/15-05 AI Scientist v2 — Workshop-Level Autonomous Research|15/05 AI Scientist v2 — Workshop-Level Autonomous Research]]

## Concepts taught

- Invariant `lesson term` — A property checked by external code before and after every edit
- Alignment anchor `lesson term` — Immutable core-goal representation outside the loop's edit surface
- Multi-objective constraint `lesson term` — Performance, safety, fairness, robustness — all required
- [[Concepts/Regression detection|Regression detection]] `lesson term` — Pause the loop when historical metric deltas suggest capability loss
- Kolmogorov bound `lesson term` — Limits what a system can prove about its own successor
- Lob's theorem `lesson term` — System can act on "I should" without proving it should
- Gate stack `lesson term` — Multiple primitives combined; any failure rejects the edit
- Bounded improvement `lesson term` — Raises silent-failure cost; does not close the safety problem

## Ships

- [[Artifacts/15-08 bounded-loop-review|bounded-loop-review]] `skill` — Audit a proposed bounded self-improvement loop against the four-primitive stack (invariants, anchor, multi-objective, regression detection).

## Further reading

- [[Resources/Anthropic — Claude's Constitution (January 2026)|Anthropic — Claude's Constitution (January 2026)]] ([link](https://www.anthropic.com/news/claudes-constitution)) — the reason-based alignment anchor. ·  also cited by 6 other lessons
- [[Resources/Anthropic — Responsible Scaling Policy v3.0 (Feb 2026)|Anthropic — Responsible Scaling Policy v3.0 (Feb 2026)]] ([link](https://anthropic.com/responsible-scaling-policy/rsp-v3-0)) — multi-objective capability thresholds. ·  also cited by 5 other lessons
- [[Resources/DeepMind Frontier Safety Framework v3|DeepMind Frontier Safety Framework v3]] ([link](https://deepmind.google/blog/strengthening-our-frontier-safety-framework/)) — deceptive-alignment monitoring as an invariant primitive. ·  also cited by 5 other lessons
- [[Resources/ICLR 2026 RSI Workshop summary (OpenReview)|ICLR 2026 RSI Workshop summary (OpenReview)]] ([link](https://openreview.net/pdf?id=OsPQ6zTQXV)) — the four-primitive convergence. ·  also cited by 1 other lesson
- Schmidhuber (2003). Godel Machines ([link](https://people.idsia.ch/~juergen/goedelmachine.html)) — the formal-proof ancestor of these primitives.


%% ── my notes ── %%
