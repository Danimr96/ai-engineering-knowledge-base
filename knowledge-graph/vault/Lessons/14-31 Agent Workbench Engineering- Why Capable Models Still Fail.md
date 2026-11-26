---
id: "lesson:14/31"
type: lesson
ref: 14/31
phase: 14
num: 31
title: "Agent Workbench Engineering: Why Capable Models Still Fail"
lesson_type: learn+build
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 7
code_files: 1
concepts: 5
prereqs: 2
community: 15
aliases:
  - 14/31
  - 14-31
tags:
  - phase/14
  - type/learn+build
  - community/15
  - stdlib-only
source: ai-engineering-from-scratch/phases/14-agent-engineering/31-agent-workbench-why-models-fail/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/31-agent-workbench-why-models-fail"
---

# 14/31 Agent Workbench Engineering: Why Capable Models Still Fail

> A capable model is not enough. Reliable agents need a workbench: instructions, state, scope, feedback, verification, review, and handoff. Strip those away and even a frontier model produces work that is unsafe to ship.

**Phase:** [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] · **Type:** Learn + Build · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/14-agent-engineering/31-agent-workbench-why-models-fail/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/31-agent-workbench-why-models-fail) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/14-agent-engineering/31-agent-workbench-why-models-fail) · code: main.py · quiz: 7 questions  
**Community:** [[Communities/15 System of record · Block severity · Definition of done|15 System of record · Block severity · Definition of done]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 14 · 01 (Agent Loop), Phase 14 · 26 (Failure Modes)`

- [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]] — Agent Loop
- [[Lessons/14-26 Failure Modes- Why Agents Break|14/26 Failure Modes: Why Agents Break]] — Failure Modes

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/14-05 Self-Refine and CRITIC- Iterative Output Improvement|14/05 Self-Refine and CRITIC: Iterative Output Improvement]], [[Lessons/14-24 Agent Observability- Langfuse, Phoenix, Opik|14/24 Agent Observability: Langfuse, Phoenix, Opik]]
- depth 3: [[Lessons/14-03 Reflexion- Verbal Reinforcement Learning|14/03 Reflexion: Verbal Reinforcement Learning]], [[Lessons/14-23 OpenTelemetry GenAI Semantic Conventions|14/23 OpenTelemetry GenAI Semantic Conventions]]

## Builds on this

- [[Lessons/14-32 The Minimal Agent Workbench|14/32 The Minimal Agent Workbench]]
- [[Lessons/14-42 Capstone- Ship a Reusable Agent Workbench Pack|14/42 Capstone: Ship a Reusable Agent Workbench Pack]]
- [[Lessons/14-43 Frame the Task Before the Agent Writes Code|14/43 Frame the Task Before the Agent Writes Code]]

## Concepts taught

- Workbench `lesson term` — Engineered surfaces around the model that make work reliable
- Surface `lesson term` — A named, machine-readable input the agent reads or writes every turn
- [[Concepts/System of record|System of record]] `lesson term` — The file the agent treats as truth when chat history is gone
- [[Concepts/Definition of done|Definition of done]] `lesson term` — An objective, file-backed checklist the agent cannot fake
- Workbench audit `lesson term` — A pass over the seven surfaces that flags missing pieces before work begins

## Ships

- [[Artifacts/14-31 workbench-audit|workbench-audit]] `skill` — Audit a repo for the seven agent workbench surfaces and report which are missing, partial, or healthy before any agent work begins.

## Further reading

- Addy Osmani, Agent Harness Engineering ([link](https://addyosmani.com/blog/agent-harness-engineering/)) — `Agent = Model + Harness` and the ratchet pattern; thin on infrastructure
- [[Resources/Anthropic, Effective harnesses for long-running agents|Anthropic, Effective harnesses for long-running agents]] ([link](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)) — long-horizon surfaces inside a specific runtime ·  also cited by 4 other lessons
- [[Resources/Anthropic, Harness design for long-running application development|Anthropic, Harness design for long-running application development]] ([link](https://www.anthropic.com/engineering/harness-design-long-running-apps)) — applied design notes ·  also cited by 2 other lessons
- Augment Code, Harness Engineering for AI Coding Agents ([link](https://www.augmentcode.com/guides/harness-engineering-ai-coding-agents)) — constraint-first walkthrough
- [[Resources/LangChain, The Anatomy of an Agent Harness|LangChain, The Anatomy of an Agent Harness]] ([link](https://blog.langchain.com/the-anatomy-of-an-agent-harness/)) — eleven components: prompts, tools, hooks, orchestration, sandboxes, memory, skills, subagents, runtime; omits queues, deployment, authz ·  also cited by 1 other lesson
- LangChain Deep Agents harness capabilities ([link](https://docs.langchain.com/oss/python/deepagents/harness)) — runtime config surface
- [[Resources/HKUDS-OpenHarness|HKUDS/OpenHarness]] ([link](https://github.com/HKUDS/OpenHarness)) — open agent harness with built-in personal agent ·  also cited by 1 other lesson
- ai-boost/awesome-harness-engineering ([link](https://github.com/ai-boost/awesome-harness-engineering)) — alternate curated list (tools, evals, memory, MCP, permissions)
- [[Resources/andrewgarst-agentic_harness|andrewgarst/agentic_harness]] ([link](https://github.com/andrewgarst/agentic_harness)) — production-ready reference implementation with Redis-backed memory and eval suite ·  also cited by 1 other lesson
- walkinglabs/awesome-harness-engineering ([link](https://github.com/walkinglabs/awesome-harness-engineering)) — curated reading list across context, evaluation, observability, orchestration
- HumanLayer, Skill Issue: Harness Engineering for Coding Agents ([link](https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents)) — "it's not a model problem, it's a configuration problem"
- Jaymin West, Agentic Engineering — Chapter 6: Harnesses ([link](https://www.jayminwest.com/agentic-engineering-book/6-harnesses)) — book-length treatment, treats harness as the primary security boundary
- Martin Fowler / Birgitta Böckeler, Harness engineering for coding agent users ([link](https://martinfowler.com/articles/harness-engineering.html)) — guides (feedforward) + sensors (feedback); the cleanest control-theory framing
- [[Resources/MongoDB, The Agent Harness- Why the LLM Is the Smallest Part of Your Agent System|MongoDB, The Agent Harness: Why the LLM Is the Smallest Part of Your Agent System]] ([link](https://www.mongodb.com/company/blog/technical/agent-harness-why-llm-is-smallest-part-of-your-agent-system)) — receipts: Vercel 80% to 100%, Harvey 2x accuracy, Terminal Bench Top 30 to Top 5 ·  also cited by 1 other lesson
- HN: Effective harnesses for long-running agents ([link](https://news.ycombinator.com/item?id=46081704))
- [[Resources/HN- Improving 15 LLMs at Coding in One Afternoon. Only the Harness Changed|HN: Improving 15 LLMs at Coding in One Afternoon. Only the Harness Changed]] ([link](https://news.ycombinator.com/item?id=46988596)) ·  also cited by 1 other lesson
- HN: The agent harness belongs outside the sandbox ([link](https://news.ycombinator.com/item?id=47990675)) — argues for authorization as a separate plane
- OpenAI, Harness engineering: leveraging Codex in an agent-first world ([link](https://openai.com/index/harness-engineering/)) — Codex team's view of the surfaces around their runtime
- OpenAI, Unrolling the Codex agent loop ([link](https://openai.com/index/unrolling-the-codex-agent-loop/)) — the agent loop reduced to a `while` over function calls
- [[Resources/preprints.org, Harness Engineering for Language Agents (March 2026)|preprints.org, Harness Engineering for Language Agents (March 2026)]] ([link](https://www.preprints.org/manuscript/202603.1756)) — academic framing as control / agency / runtime ·  also cited by 1 other lesson
- Sequoia podcast, Harrison Chase on Context Engineering Long-Horizon Agents ([link](https://sequoiacap.com/podcast/context-engineering-our-way-to-long-horizon-agents-langchains-harrison-chase/)) — runtime concerns over model concerns

## In learning paths

- [[Paths/Agent-Assisted Engineering|Agent-Assisted Engineering]] — step 1, required


%% ── my notes ── %%
