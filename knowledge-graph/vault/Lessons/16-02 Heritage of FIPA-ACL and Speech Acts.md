---
id: "lesson:16/02"
type: lesson
ref: 16/02
phase: 16
num: 2
title: Heritage of FIPA-ACL and Speech Acts
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 0
code_files: 1
concepts: 9
prereqs: 1
community: 6
aliases:
  - 16/02
  - 16-02
tags:
  - phase/16
  - type/learn
  - community/06
  - stdlib-only
source: ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/02-fipa-acl-heritage/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/02-fipa-acl-heritage"
---

# 16/02 Heritage of FIPA-ACL and Speech Acts

> Before MCP, before A2A, there was FIPA-ACL. In 2000 the IEEE Foundation for Intelligent Physical Agents ratified an agent communication language with twenty performatives, two content languages, and a set of interaction protocols — contract net, subscribe/notify, request-when. It faded from industry because the ontology overhead was too heavy for the web, but the LLM revival of multi-agent systems is quietly reimplementing the same ideas without the formal semantics: JSON contracts stand in for performatives, natural language stands in for ontologies. This lesson reads FIPA-ACL seriously so you can see which 2026 protocol decisions are reinvention, which are novelty, and where the current wave is going to rediscover problems the 2000s already solved.

**Phase:** [[Phases/16 Multi-Agent & Swarms|Phase 16: Multi-Agent & Swarms]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/16-multi-agent-and-swarms/02-fipa-acl-heritage/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/02-fipa-acl-heritage) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/02-fipa-acl-heritage) · code: main.py  
**Community:** [[Communities/06 Communicative dehallucination · Consensus · Contract Net|06 Communicative dehallucination · Consensus · Contract Net]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 16 · 01 (Why Multi-Agent)`

- [[Lessons/16-01 Why Multi-Agent|16/01 Why Multi-Agent?]] — Why Multi-Agent

## Builds on this

- [[Lessons/16-16 Negotiation and Bargaining|16/16 Negotiation and Bargaining]]
- [[Lessons/16-25 Case Studies and the 2026 State of the Art|16/25 Case Studies and the 2026 State of the Art]]

## Concepts taught

- Speech act `lesson term` — Austin/Searle: utterances as actions. The theoretical parent of ACL.
- FIPA `lesson term` — IEEE Foundation for Intelligent Physical Agents. Standardized ACL in 2000.
- ACL `lesson term` — FIPA's envelope format: performative + content + metadata.
- Performative `lesson term` — The intent class of a message: inform, request, propose, cfp, etc.
- KQML `lesson term` — Knowledge Query and Manipulation Language (1993). Simpler, narrower.
- Ontology `lesson term` — A formal definition of the concepts the content language talks about.
- SL0 / SL1 `lesson term` — Semantic Language levels 0 and 1 — the formal content language family.
- [[Concepts/Contract Net|Contract Net]] `lesson term` — Manager issues cfp; bidders propose; manager accepts. The canonical interaction protocol.
- Interaction protocol `lesson term` — A sequence of performatives with known correctness: request-when, subscribe-notify, etc.

## Ships

- [[Artifacts/16-02 fipa-mapper|fipa-mapper]] `skill` — Map any 2026 agent-protocol spec (MCP, A2A, ACP, ANP, CA-MCP, NLIP, or a new one) onto FIPA-ACL performatives and interaction protocols to decide what is genuine novelty and what is reinvention.

## Further reading

- [[Resources/A2A specification|A2A specification]] ([link](https://a2a-protocol.org/latest/specification/)) — the modern agent-peer equivalent of contract-net and subscribe-notify ·  also cited by 1 other lesson
- [[Resources/Liu et al. — A Survey of Agent Interoperability Protocols- MCP, ACP, A2A, ANP|Liu et al. — A Survey of Agent Interoperability Protocols: MCP, ACP, A2A, ANP]] ([link](https://arxiv.org/html/2505.02279v1)) — the canonical 2025 survey connecting modern specs to FIPA heritage ·  also cited by 1 other lesson
- FIPA ACL Message Structure Specification (fipa00037) ([link](http://www.fipa.org/specs/fipa00037/)) — the ratified 2000 envelope format
- [[Resources/Model Context Protocol — Specification 2026-07-28|Model Context Protocol — Specification 2026-07-28]] ([link](https://modelcontextprotocol.io/specification/2026-07-28)) — the current stateless tool-use equivalent of `request`/`query-ref` ·  also cited by 5 other lessons


%% ── my notes ── %%
