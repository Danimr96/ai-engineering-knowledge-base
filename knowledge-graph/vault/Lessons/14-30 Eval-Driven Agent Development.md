---
id: "lesson:14/30"
type: lesson
ref: 14/30
phase: 14
num: 30
title: Eval-Driven Agent Development
lesson_type: learn+build
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 7
code_files: 1
concepts: 10
prereqs: 29
community: 7
aliases:
  - 14/30
  - 14-30
tags:
  - phase/14
  - type/learn+build
  - community/07
  - stdlib-only
source: ai-engineering-from-scratch/phases/14-agent-engineering/30-eval-driven-agent-development/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/30-eval-driven-agent-development"
---

# 14/30 Eval-Driven Agent Development

> Anthropic's guidance: "start with simple prompts, optimize them with comprehensive evaluation, and add multi-step agentic systems only when needed." Evaluation is not the last step. It's the outer loop that drives every other choice in Phase 14.

**Phase:** [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] · **Type:** Learn + Build · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/14-agent-engineering/30-eval-driven-agent-development/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/30-eval-driven-agent-development) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/14-agent-engineering/30-eval-driven-agent-development) · code: main.py · quiz: 7 questions  
**Community:** [[Communities/07 Swarm · Evaluator-Optimizer · Debate|07 Swarm · Evaluator-Optimizer · Debate]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `All of Phase 14.`

- **14/01-29** — earlier lessons of this phase ·  medium confidence:
    - [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]]
    - [[Lessons/14-02 ReWOO and Plan-and-Execute- Decoupled Planning|14/02 ReWOO and Plan-and-Execute: Decoupled Planning]]
    - [[Lessons/14-03 Reflexion- Verbal Reinforcement Learning|14/03 Reflexion: Verbal Reinforcement Learning]]
    - [[Lessons/14-04 Tree of Thoughts and LATS- Deliberate Search|14/04 Tree of Thoughts and LATS: Deliberate Search]]
    - [[Lessons/14-05 Self-Refine and CRITIC- Iterative Output Improvement|14/05 Self-Refine and CRITIC: Iterative Output Improvement]]
    - [[Lessons/14-06 Tool Use and Function Calling|14/06 Tool Use and Function Calling]]
    - [[Lessons/14-07 Agent Memory — Virtual Context and Memory Paging|14/07 Agent Memory — Virtual Context and Memory Paging]]
    - [[Lessons/14-08 Memory Blocks and Sleep-Time Compute|14/08 Memory Blocks and Sleep-Time Compute]]
    - [[Lessons/14-09 Hybrid Memory- Vector + Graph + KV|14/09 Hybrid Memory: Vector + Graph + KV]]
    - [[Lessons/14-10 Skill Libraries and Lifelong Learning (Voyager)|14/10 Skill Libraries and Lifelong Learning (Voyager)]]
    - [[Lessons/14-11 Planning with HTN and Evolutionary Search|14/11 Planning with HTN and Evolutionary Search]]
    - [[Lessons/14-12 Anthropic's Workflow Patterns- Simple Over Complex|14/12 Anthropic's Workflow Patterns: Simple Over Complex]]
    - [[Lessons/14-13 Stateful Graph Orchestration — Durable Execution and Checkpoints|14/13 Stateful Graph Orchestration — Durable Execution and Checkpoints]]
    - [[Lessons/14-14 The Actor Model for Agents — Async Messages and Typed Runtimes|14/14 The Actor Model for Agents — Async Messages and Typed Runtimes]]
    - [[Lessons/14-15 Role-Based Agent Teams — Roles, Tasks, Processes|14/15 Role-Based Agent Teams — Roles, Tasks, Processes]]
    - [[Lessons/14-16 OpenAI Agents SDK- Handoffs, Guardrails, Tracing|14/16 OpenAI Agents SDK: Handoffs, Guardrails, Tracing]]
    - [[Lessons/14-17 The Harness as a Library — Subagents and Session Store|14/17 The Harness as a Library — Subagents and Session Store]]
    - [[Lessons/14-18 Production Agent Runtimes — Fast Instantiation and Typed Workflows|14/18 Production Agent Runtimes — Fast Instantiation and Typed Workflows]]
    - [[Lessons/14-19 Benchmarks- SWE-bench, GAIA, AgentBench|14/19 Benchmarks: SWE-bench, GAIA, AgentBench]]
    - [[Lessons/14-20 Benchmarks- WebArena and OSWorld|14/20 Benchmarks: WebArena and OSWorld]]
    - [[Lessons/14-21 Computer Use- Claude, OpenAI CUA, Gemini|14/21 Computer Use: Claude, OpenAI CUA, Gemini]]
    - [[Lessons/14-22 Voice Agents- Pipecat and LiveKit|14/22 Voice Agents: Pipecat and LiveKit]]
    - [[Lessons/14-23 OpenTelemetry GenAI Semantic Conventions|14/23 OpenTelemetry GenAI Semantic Conventions]]
    - [[Lessons/14-24 Agent Observability- Langfuse, Phoenix, Opik|14/24 Agent Observability: Langfuse, Phoenix, Opik]]
    - [[Lessons/14-25 Multi-Agent Debate and Collaboration|14/25 Multi-Agent Debate and Collaboration]]
    - [[Lessons/14-26 Failure Modes- Why Agents Break|14/26 Failure Modes: Why Agents Break]]
    - [[Lessons/14-27 Prompt Injection and the PVE Defense|14/27 Prompt Injection and the PVE Defense]]
    - [[Lessons/14-28 Orchestration Patterns- Supervisor, Swarm, Hierarchical|14/28 Orchestration Patterns: Supervisor, Swarm, Hierarchical]]
    - [[Lessons/14-29 Production Runtimes- Queue, Event, Cron|14/29 Production Runtimes: Queue, Event, Cron]]

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/13-01 The Tool Interface — Why Agents Need Structured I-O|13/01 The Tool Interface — Why Agents Need Structured I/O]]

## Builds on this

- [[Lessons/19-27 Capstone Lesson 27- Eval Harness with Fixture Tasks|19/27 Capstone Lesson 27: Eval Harness with Fixture Tasks]]

## Concepts taught

- Static benchmark `lesson term` — SWE-bench, GAIA, AgentBench, WebArena, OSWorld
- Custom offline eval `lesson term` — LLM-as-judge / exec / trajectory on your product shape
- Online eval `lesson term` — Session replay, guardrail alerts, cost/latency tracking
- [[Concepts/Evaluator-Optimizer|Evaluator-Optimizer]] `lesson term` — Iterate until judge passes
- CI gate `lesson term` — Fail the build on eval regression
- [[Concepts/Baseline|Baseline]] `lesson term` — Reference score to detect regression
- [[Concepts/Trajectory efficiency|Trajectory efficiency]] `lesson term` — Agent step count divided by human expert minimum
- [[Concepts/Eval Set|Eval Set]] `glossary` — A versioned collection of inputs, expected properties, scoring rules, and metadata used to measure an AI system against a defined capability or risk.
- [[Concepts/LLM-as-a-Judge|LLM-as-a-Judge]] `glossary` — Using a language model to score, compare, classify, or critique another system's output against a rubric.
- [[Concepts/Regression Test|Regression Test]] `glossary` — A repeatable check that protects behavior known to work, especially after code, prompt, model, retrieval, or tool changes.

## Ships

- [[Artifacts/14-30 eval-suite|eval-suite]] `skill` — Build a three-layer eval suite (static benchmarks, custom offline, online production) with evaluator-optimizer loop and CI gates.

## Further reading

- [[Resources/Building Effective Agents|Building Effective Agents]] ([link](https://www.anthropic.com/research/building-effective-agents)) — "start simple, optimize with evals" ·  also cited by 16 other lessons
- [[Resources/Berkeley Function Calling Leaderboard|Berkeley Function Calling Leaderboard]] ([link](https://gorilla.cs.berkeley.edu/leaderboard.html)) — tool-use benchmark ·  also cited by 2 other lessons
- [[Resources/Langfuse docs|Langfuse docs]] ([link](https://langfuse.com/)) — evals + session replay in practice ·  also cited by 1 other lesson
- [[Resources/OpenAI, SWE-bench Verified|OpenAI, SWE-bench Verified]] ([link](https://openai.com/index/introducing-swe-bench-verified/)) — the curated benchmark ·  also cited by 3 other lessons

## In learning paths

- [[Paths/Agent Systems Engineering|Agent Systems Engineering]] — step 12, required
- [[Paths/AI Evaluation and Reliability|AI Evaluation and Reliability]] — step 3, required


%% ── my notes ── %%
