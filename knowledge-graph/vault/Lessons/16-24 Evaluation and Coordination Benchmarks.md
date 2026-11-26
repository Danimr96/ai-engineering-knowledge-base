---
id: "lesson:16/24"
type: lesson
ref: 16/24
phase: 16
num: 24
title: Evaluation and Coordination Benchmarks
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
  - 16/24
  - 16-24
tags:
  - phase/16
  - type/learn
  - community/06
  - stdlib-only
source: ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/24-evaluation-coordination-benchmarks/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/24-evaluation-coordination-benchmarks"
---

# 16/24 Evaluation and Coordination Benchmarks

> Five 2025-2026 benchmarks cover the multi-agent evaluation space. **MultiAgentBench / MARBLE** (ACL 2025, arXiv:2503.01935) evaluates star/chain/tree/graph topologies with milestone KPIs; **graph is best for research**, cognitive planning adds ~3% milestone achievement. **COMMA** evaluates multimodal asymmetric-information coordination; state-of-the-art models including GPT-4o struggle to beat a random baseline. **MedAgentBoard** (arXiv:2505.12371) covers four medical task categories and often finds multi-agent does not dominate single-LLM. **AgentArch** (arXiv:2509.10769) benchmarks enterprise agent architectures combining tool-use + memory + orchestration. **SWE-bench Pro** ([arXiv:2509.16941](https://arxiv.org/abs/2509.16941)) has 1865 problems across 41 repos spanning business apps, B2B services, and developer tools; frontier models score ~23% on Pro vs 70%+ on Verified — a reality check on contamination. Claude Opus 4.7 (April 2026) is reported at **64.3%** on Pro with explicit agent-teams coordination (no Anthropic primary source published yet — treat as preliminary); Verdent (agent scaffold) hits **76.1% pass@1** on Verified ([Verdent technical report](https://www.verdent.ai/blog/swe-bench-verified-technical-report)). **AAAI 2026 Bridge Program WMAC** (https://multiagents.org/2026/) is the 2026 community focal point. This lesson builds on MARBLE's metrics, runs a topology-vs-metric sweep, and pins the "just passing SWE-bench Verified is not evidence of generalization" rule.

**Phase:** [[Phases/16 Multi-Agent & Swarms|Phase 16: Multi-Agent & Swarms]] · **Type:** Learn · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/16-multi-agent-and-swarms/24-evaluation-coordination-benchmarks/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/24-evaluation-coordination-benchmarks) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/24-evaluation-coordination-benchmarks) · code: main.py  
**Community:** [[Communities/06 Communicative dehallucination · Consensus · Contract Net|06 Communicative dehallucination · Consensus · Contract Net]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 16 · 15 (Voting and Debate Topology), Phase 16 · 23 (Failure Modes)`

- [[Lessons/16-15 Voting, Self-Consistency, and Debate Topology|16/15 Voting, Self-Consistency, and Debate Topology]] — Voting and Debate Topology
- [[Lessons/16-23 Failure Modes — MAST, Groupthink, Monoculture, Cascading Errors|16/23 Failure Modes — MAST, Groupthink, Monoculture, Cascading Errors]] — Failure Modes

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/16-07 Society of Mind and Multi-Agent Debate|16/07 Society of Mind and Multi-Agent Debate]], [[Lessons/16-13 Shared Memory and Blackboard Patterns|16/13 Shared Memory and Blackboard Patterns]], [[Lessons/16-14 Consensus and Byzantine Fault Tolerance for Agents|16/14 Consensus and Byzantine Fault Tolerance for Agents]]
- depth 3: [[Lessons/16-04 The Multi-Agent Primitive Model|16/04 The Multi-Agent Primitive Model]], [[Lessons/16-09 Parallel - Swarm - Networked Architectures|16/09 Parallel / Swarm / Networked Architectures]]

## Builds on this

- [[Lessons/16-25 Case Studies and the 2026 State of the Art|16/25 Case Studies and the 2026 State of the Art]]

## Concepts taught

- MARBLE `lesson term` — ACL 2025; star/chain/tree/graph topologies with milestone KPIs.
- COMMA `lesson term` — Multimodal asymmetric-info coordination; frontier models struggle vs random.
- MedAgentBoard `lesson term` — Four medical categories; often finds multi-agent does not dominate single-LLM.
- AgentArch `lesson term` — Tools + memory + orchestration layered.
- [[Concepts/SWE-bench Pro|SWE-bench Pro]] `lesson term` — 1865 problems, 41 repos; ~23% vs 70%+ on Verified (the contamination signal).
- Milestone achievement `lesson term` — Benchmarks that reward progress, not only final success.
- [[Concepts/Benchmark Contamination|Benchmark Contamination]] (as *Contamination*) `glossary` — Post-release, benchmarks drift into training corpora; scores inflate.
- WMAC `lesson term` — Workshop on Multi-Agent Coordination; community focal point.

## Ships

- [[Artifacts/16-24 benchmark-reader|benchmark-reader]] `skill` — Read a multi-agent benchmark claim skeptically. Grades the claim on benchmark selection, contamination, baselines, statistical significance, task diversity, and cost disclosure.

## Further reading

- [[Resources/MultiAgentBench - MARBLE|MultiAgentBench / MARBLE]] ([link](https://arxiv.org/abs/2503.01935)) — topology benchmark with milestone KPIs ·  also cited by 1 other lesson
- MedAgentBoard ([link](https://arxiv.org/abs/2505.12371)) — domain stress test; multi-agent often does not dominate
- AgentArch ([link](https://arxiv.org/abs/2509.10769)) — enterprise agent architectures
- [[Resources/MARBLE repo|MARBLE repo]] ([link](https://github.com/ulab-uiuc/MARBLE)) — reference implementation ·  also cited by 1 other lesson
- [[Resources/AAAI 2026 WMAC|AAAI 2026 WMAC]] ([link](https://multiagents.org/2026/)) — the 2026 community focal point ·  also cited by 1 other lesson
- [[Resources/Jimenez et al. SWE-bench leaderboard|Jimenez et al. SWE-bench leaderboard]] ([link](https://www.swebench.com/)) — Verified and Pro scores for frontier models ·  also cited by 4 other lessons


%% ── my notes ── %%
