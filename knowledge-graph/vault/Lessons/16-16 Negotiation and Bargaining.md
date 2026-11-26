---
id: "lesson:16/16"
type: lesson
ref: 16/16
phase: 16
num: 16
title: Negotiation and Bargaining
lesson_type: learn+build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 2
community: 6
aliases:
  - 16/16
  - 16-16
tags:
  - phase/16
  - type/learn+build
  - community/06
  - stdlib-only
source: ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/16-negotiation-bargaining/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/16-negotiation-bargaining"
---

# 16/16 Negotiation and Bargaining

> Agents negotiate resources, prices, task allocations, and terms. The 2026 benchmark set is clear: NegotiationArena (arXiv:2402.05863) shows LLMs can improve payoffs ~20% via persona manipulation ("desperation"); "Measuring Bargaining Abilities" (arXiv:2402.15813) shows buyer is harder than seller and scale does not help — their **OG-Narrator** (deterministic offer generator + LLM narrator) pushed deal rate from 26.67% to 88.88%; the Large-Scale Autonomous Negotiation Competition (arXiv:2503.06416) ran ~180k negotiations and found that **chain-of-thought-concealing** agents win by hiding reasoning from counterparts; Bhattacharya et al. 2025 on Harvard Negotiation Project metrics ranked Llama-3 most-effective, Claude-3 aggressive, GPT-4 fairest. This lesson implements Contract Net Protocol (the FIPA ancestor, Lesson 02), wires an LLM-style buyer/seller, runs an OG-Narrator-style decomposition, and measures how deal rate changes with each structural choice.

**Phase:** [[Phases/16 Multi-Agent & Swarms|Phase 16: Multi-Agent & Swarms]] · **Type:** Learn + Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/16-multi-agent-and-swarms/16-negotiation-bargaining/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/16-negotiation-bargaining) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/16-negotiation-bargaining) · code: main.py  
**Community:** [[Communities/06 Communicative dehallucination · Consensus · Contract Net|06 Communicative dehallucination · Consensus · Contract Net]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 16 · 02 (FIPA-ACL Heritage), Phase 16 · 09 (Parallel Swarm Networks)`

- [[Lessons/16-02 Heritage of FIPA-ACL and Speech Acts|16/02 Heritage of FIPA-ACL and Speech Acts]] — FIPA-ACL Heritage
- [[Lessons/16-09 Parallel - Swarm - Networked Architectures|16/09 Parallel / Swarm / Networked Architectures]] — Parallel Swarm Networks

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/16-01 Why Multi-Agent|16/01 Why Multi-Agent?]], [[Lessons/16-04 The Multi-Agent Primitive Model|16/04 The Multi-Agent Primitive Model]], [[Lessons/16-05 Supervisor - Orchestrator-Worker Pattern|16/05 Supervisor / Orchestrator-Worker Pattern]]

## Builds on this

- [[Lessons/16-21 Agent Economies, Token Incentives, Reputation|16/21 Agent Economies, Token Incentives, Reputation]]
- [[Lessons/16-25 Case Studies and the 2026 State of the Art|16/25 Case Studies and the 2026 State of the Art]]

## Concepts taught

- [[Concepts/Contract Net|Contract Net]] `lesson term` — Smith 1980, FIPA 1996. cfp + propose + accept/reject. The canonical task-market.
- ZOPA `lesson term` — Overlap between buyer's max and seller's min. Offers outside it cannot close.
- BATNA `lesson term` — Your fallback if this deal fails. Sets your reservation price.
- OG-Narrator `lesson term` — Decomposition: deterministic offer, LLM narration.
- Zeuthen strategy `lesson term` — Classical offer-generator that concedes based on risk limits.
- Rubinstein bargaining `lesson term` — Game-theoretic model for infinite-horizon bargaining with discounting.
- CoT concealment `lesson term` — Winners in arXiv:2503.06416 kept private scratchpads; public channel shows offer only.
- Persona manipulation `lesson term` — arXiv:2402.05863: ~20% payoff gain from desperation/urgency personas.

## Ships

- [[Artifacts/16-16 bargainer-designer|bargainer-designer]] `skill` — Design a negotiation protocol: which agent narrates, which component generates offers, how private scratchpads separate from public messages, what the round bound is, and how deal rate is monitored.

## Further reading

- NegotiationArena ([link](https://arxiv.org/abs/2402.05863)) — the benchmark; persona manipulation and exploitation findings
- Measuring Bargaining Abilities of Language Models ([link](https://arxiv.org/abs/2402.15813)) — OG-Narrator and the buyer-harder-than-seller result
- Large-Scale Autonomous Negotiation Competition ([link](https://arxiv.org/abs/2503.06416)) — ~180k negotiations; chain-of-thought concealment wins
- Smith 1980 — The Contract Net Protocol ([link](https://ieeexplore.ieee.org/document/1675516)) — the classical mechanism, IEEE Transactions on Computers
- LLM-Stakeholders Interactive Negotiation (NeurIPS 2024) ([link](https://proceedings.neurips.cc/paper_files/paper/2024/file/984dd3db213db2d1454a163b65b84d08-Paper-Datasets_and_Benchmarks_Track.pdf)) — multi-party scorable games with secret utilities


%% ── my notes ── %%
