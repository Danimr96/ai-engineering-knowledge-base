---
id: "lesson:14/39"
type: lesson
ref: 14/39
phase: 14
num: 39
title: "Reviewer Agent: Separate Builder from Marker"
lesson_type: build
languages:
  - Python
time_min: 55
on_route: false
quiz_count: 7
code_files: 1
concepts: 6
prereqs: 1
community: 15
aliases:
  - 14/39
  - 14-39
tags:
  - phase/14
  - type/build
  - community/15
  - stdlib-only
source: ai-engineering-from-scratch/phases/14-agent-engineering/39-reviewer-agent/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/39-reviewer-agent"
---

# 14/39 Reviewer Agent: Separate Builder from Marker

> The agent that wrote the code cannot grade it. A reviewer is a second loop with a different system prompt, a different goal, and read-only access to everything the builder produced. The gap between builder and reviewer is where most reliability lives.

**Phase:** [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] · **Type:** Build · **Time:** 55 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/14-agent-engineering/39-reviewer-agent/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/39-reviewer-agent) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/14-agent-engineering/39-reviewer-agent) · code: main.py · quiz: 7 questions  
**Community:** [[Communities/15 System of record · Block severity · Definition of done|15 System of record · Block severity · Definition of done]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 14 · 38 (Verification Gate)`

- [[Lessons/14-38 Verification Gates|14/38 Verification Gates]] — Verification Gate

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/14-33 Agent Instructions as Executable Constraints|14/33 Agent Instructions as Executable Constraints]], [[Lessons/14-36 Scope Contracts and Task Boundaries|14/36 Scope Contracts and Task Boundaries]], [[Lessons/14-37 Runtime Feedback Loops|14/37 Runtime Feedback Loops]]
- depth 3: [[Lessons/14-32 The Minimal Agent Workbench|14/32 The Minimal Agent Workbench]], [[Lessons/14-35 Initialization Scripts for Agents|14/35 Initialization Scripts for Agents]]

## Builds on this

- [[Lessons/14-40 Multi-Session Handoff|14/40 Multi-Session Handoff]]
- [[Lessons/14-41 The Workbench on a Real Repo|14/41 The Workbench on a Real Repo]]
- [[Lessons/14-42 Capstone- Ship a Reusable Agent Workbench Pack|14/42 Capstone: Ship a Reusable Agent Workbench Pack]]
- [[Lessons/14-45 Delegate Agent Work with Isolation and Merge Contracts|14/45 Delegate Agent Work with Isolation and Merge Contracts]]
- [[Lessons/14-46 Turn Every Agent Correction into a System Improvement|14/46 Turn Every Agent Correction into a System Improvement]]

## Concepts taught

- Reviewer rubric `lesson term` — Five-dimension 0-2 scoring with a written question per dimension
- Soft fail `lesson term` — Total below 7; builder gets findings to address
- Hard fail `lesson term` — Total below 5 or any dimension at 0; halt and surface to human
- Role separation `lesson term` — Same model can be both roles; the discipline is inputs and posture
- Confidence floor `lesson term` — Refuse to emit a verdict when the rubric is uncertain
- [[Concepts/Reviewer Agent|Reviewer Agent]] `glossary` — An agent assigned to inspect another agent's artifact or decision against explicit criteria and return findings or a verdict.

## Ships

- [[Artifacts/14-39 reviewer-agent|reviewer-agent]] `skill` — Stand up a reviewer agent role with a five-dimension rubric that reads builder artifacts, produces a structured review report, and starts human review from a written page instead of a blank one.

## Further reading

- Arize, LLM as a Judge — Primer and Pre-Built Evaluators ([link](https://arize.com/llm-as-a-judge/))
- [[Resources/Cloudflare, Orchestrating AI Code Review at Scale|Cloudflare, Orchestrating AI Code Review at Scale]] ([link](https://blog.cloudflare.com/ai-code-review/)) — 7-specialist + coordinator architecture, 131k runs / 30 days ·  also cited by 2 other lessons
- [[Resources/Anthropic, Claude Code subagents|Anthropic, Claude Code subagents]] ([link](https://code.claude.com/docs/en/sub-agents)) ·  also cited by 1 other lesson
- Evidently AI, LLM-as-a-judge: a complete guide ([link](https://www.evidentlyai.com/llm-guide/llm-as-a-judge))
- LangChain, How to Calibrate LLM-as-a-Judge with Human Corrections ([link](https://www.langchain.com/articles/llm-as-a-judge)) — calibration-set workflow
- Adnan Masood, Rubric-Based Evaluations and LLM-as-a-Judge: Methodologies, Biases, Empirical Validation ([link](https://medium.com/@adnanmasood/rubric-based-evals-llm-as-a-judge-methodologies-and-empirical-validation-in-domain-context-71936b989e80)) — the 4 biases and mitigations
- MLflow, LLM-as-a-Judge Evaluation ([link](https://mlflow.org/llm-as-a-judge)) — production tooling for separated builder/evaluator
- [[Resources/OpenAI Agents SDK handoffs|OpenAI Agents SDK handoffs]] ([link](https://openai.github.io/openai-agents-python/handoffs/)) ·  also cited by 1 other lesson
- Agent-as-a-Judge: Evaluating Agents with Agents (OpenReview / ICLR) ([link](https://openreview.net/forum?id=DeVm3YUnpj)) — DevAI benchmark, 366 hierarchical solution requirements

## In learning paths

- [[Paths/Agent-Assisted Engineering|Agent-Assisted Engineering]] — step 11, required


%% ── my notes ── %%
