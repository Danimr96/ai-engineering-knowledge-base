---
id: "lesson:16/21"
type: lesson
ref: 16/21
phase: 16
num: 21
title: "Agent Economies, Token Incentives, Reputation"
lesson_type: learn
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
  - 16/21
  - 16-21
tags:
  - phase/16
  - type/learn
  - community/06
  - stdlib-only
source: ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/21-agent-economies/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/21-agent-economies"
---

# 16/21 Agent Economies, Token Incentives, Reputation

> Long-horizon autonomous agents (METR's 1-hour to 8-hour work-curve) need economic agency. The emerging **5-layer stack** is: **DePIN** (physical compute) → **Identity** (W3C DIDs + reputation capital) → **Cognition** (RAG + MCP) → **Settlement** (account abstraction) → **Governance** (Agentic DAOs). Production agent-incentive networks include **Bittensor** (TAO subnets reward task-specific models), **Fetch.ai / ASI Alliance** (ASI-1 Mini LLM + FET token), and **Gonka** (transformer-based PoW that reallocates compute to productive AI tasks). Academic work: AAMAS 2025's decentralized LaMAS uses **Shapley-value credit attribution** to fairly reward contributing agents; Google Research "Mechanism design for large language models" proposes **token auctions** with second-price payment under monotone aggregation. This lesson builds a minimal agent marketplace, applies Shapley-value credit attribution to a multi-agent pipeline, and runs a second-price token auction so the game-theory machinery lands concretely.

**Phase:** [[Phases/16 Multi-Agent & Swarms|Phase 16: Multi-Agent & Swarms]] · **Type:** Learn · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/16-multi-agent-and-swarms/21-agent-economies/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/21-agent-economies) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/21-agent-economies) · code: main.py  
**Community:** [[Communities/06 Communicative dehallucination · Consensus · Contract Net|06 Communicative dehallucination · Consensus · Contract Net]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 16 · 16 (Negotiation and Bargaining), Phase 16 · 09 (Parallel Swarm Networks)`

- [[Lessons/16-09 Parallel - Swarm - Networked Architectures|16/09 Parallel / Swarm / Networked Architectures]] — Parallel Swarm Networks
- [[Lessons/16-16 Negotiation and Bargaining|16/16 Negotiation and Bargaining]] — Negotiation and Bargaining

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/16-02 Heritage of FIPA-ACL and Speech Acts|16/02 Heritage of FIPA-ACL and Speech Acts]], [[Lessons/16-04 The Multi-Agent Primitive Model|16/04 The Multi-Agent Primitive Model]], [[Lessons/16-05 Supervisor - Orchestrator-Worker Pattern|16/05 Supervisor / Orchestrator-Worker Pattern]]
- depth 3: [[Lessons/16-01 Why Multi-Agent|16/01 Why Multi-Agent?]]

## Builds on this

- [[Lessons/16-25 Case Studies and the 2026 State of the Art|16/25 Case Studies and the 2026 State of the Art]]

## Concepts taught

- DePIN `lesson term` — Token-incentivized compute/storage/bandwidth. Bittensor, Akash, Render.
- [[Concepts/DID|DID]] `lesson term` — W3C spec for portable IDs. Agent reputation binds to DID, not to a platform.
- ERC-4337 `lesson term` — Contract accounts that can sponsor gas, enabling agent payments.
- Shapley value `lesson term` — Unique allocation satisfying efficiency, symmetry, linearity, null.
- Second-price auction `lesson term` — Truthful mechanism: winner pays second-highest bid. Monotone aggregation compatible.
- Reputation capital `lesson term` — DID-bound score from confirmed contributions; decays over time.
- Agentic DAO `lesson term` — DAO with agent voters as first-class, voting power tied to reputation.
- TAO / FET / GPU credits `lesson term` — Bittensor TAO, Fetch.ai FET, various DePIN tokens.

## Ships

- [[Artifacts/16-21 economy-designer|economy-designer]] `skill` — Design a minimal agent economy — identity, credit attribution, payment mechanism, reputation. Picks the smallest stack that solves the user's multi-agent incentive problem.

## Further reading

- The Agent Economy ([link](https://arxiv.org/abs/2602.14219)) — 2026 survey of the 5-layer agent-economy stack
- Bittensor TAO documentation ([link](https://docs.bittensor.com/)) — subnet structure and reward distribution
- Fetch.ai / ASI Alliance ([link](https://fetch.ai/)) — ASI-1 Mini LLM and FET token
- AAMAS 2025 — decentralized LaMAS ([link](https://www.ifaamas.org/Proceedings/aamas2025/pdfs/p2896.pdf)) — Shapley-value credit attribution
- Google Research — Mechanism design for large language models ([link](https://research.google/blog/mechanism-design-for-large-language-models/)) — token auctions with monotone aggregation
- [[Resources/W3C Decentralized Identifiers|W3C Decentralized Identifiers]] ([link](https://www.w3.org/TR/did-core/)) — identity foundation ·  also cited by 1 other lesson


%% ── my notes ── %%
