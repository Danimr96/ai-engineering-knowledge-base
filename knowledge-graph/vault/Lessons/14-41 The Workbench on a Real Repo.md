---
id: "lesson:14/41"
type: lesson
ref: 14/41
phase: 14
num: 41
title: The Workbench on a Real Repo
lesson_type: build
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 7
code_files: 1
concepts: 8
prereqs: 9
community: 15
aliases:
  - 14/41
  - 14-41
tags:
  - phase/14
  - type/build
  - community/15
  - stdlib-only
source: ai-engineering-from-scratch/phases/14-agent-engineering/41-workbench-for-real-repos/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/41-workbench-for-real-repos"
---

# 14/41 The Workbench on a Real Repo

> Eleven lessons of surfaces are worth nothing if they do not survive contact with a real codebase. This lesson runs the same task twice on a small sample app: prompt-only versus workbench-guided. The numbers do the arguing.

**Phase:** [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] · **Type:** Build · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/14-agent-engineering/41-workbench-for-real-repos/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/41-workbench-for-real-repos) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/14-agent-engineering/41-workbench-for-real-repos) · code: main.py · quiz: 7 questions  
**Community:** [[Communities/15 System of record · Block severity · Definition of done|15 System of record · Block severity · Definition of done]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phases 14 · 32 to 14 · 40`

- **14/32-40**:
    - [[Lessons/14-32 The Minimal Agent Workbench|14/32 The Minimal Agent Workbench]]
    - [[Lessons/14-33 Agent Instructions as Executable Constraints|14/33 Agent Instructions as Executable Constraints]]
    - [[Lessons/14-34 Repo Memory and Durable State|14/34 Repo Memory and Durable State]]
    - [[Lessons/14-35 Initialization Scripts for Agents|14/35 Initialization Scripts for Agents]]
    - [[Lessons/14-36 Scope Contracts and Task Boundaries|14/36 Scope Contracts and Task Boundaries]]
    - [[Lessons/14-37 Runtime Feedback Loops|14/37 Runtime Feedback Loops]]
    - [[Lessons/14-38 Verification Gates|14/38 Verification Gates]]
    - [[Lessons/14-39 Reviewer Agent- Separate Builder from Marker|14/39 Reviewer Agent: Separate Builder from Marker]]
    - [[Lessons/14-40 Multi-Session Handoff|14/40 Multi-Session Handoff]]

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/14-31 Agent Workbench Engineering- Why Capable Models Still Fail|14/31 Agent Workbench Engineering: Why Capable Models Still Fail]]
- depth 3: [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]], [[Lessons/14-26 Failure Modes- Why Agents Break|14/26 Failure Modes: Why Agents Break]]

## Builds on this

- [[Lessons/14-42 Capstone- Ship a Reusable Agent Workbench Pack|14/42 Capstone: Ship a Reusable Agent Workbench Pack]]
- [[Lessons/14-46 Turn Every Agent Correction into a System Improvement|14/46 Turn Every Agent Correction into a System Improvement]]
- [[Lessons/19-29 Capstone Lesson 29- End-to-End Coding Agent on the Harness|19/29 Capstone Lesson 29: End-to-End Coding Agent on the Harness]]

## Concepts taught

- Sample app `lesson term` — Small but realistic enough to exercise all seven surfaces
- [[Concepts/Pipeline|Pipeline]] `lesson term` — Ordered sequence of surface reads/writes the agent follows
- Before/after report `lesson term` — The artifact you hand to a skeptic
- False negative `lesson term` — Tasks where prompt-only is faster; useful to enumerate honestly
- Workbench benchmark `lesson term` — Portable harness that runs the comparison on your codebase
- [[Concepts/Patch|Patch]] `glossary` — A reviewable representation of changes to one or more files, usually expressed as additions and deletions against a known base revision.
- [[Concepts/Progressive Disclosure|Progressive Disclosure]] `glossary` — Supplying a person or model with the minimum useful context first, then revealing deeper detail when the task or evidence requires it.
- [[Concepts/Worktree|Worktree]] `glossary` — In Git, a working directory attached to a repository and branch or commit, with shared object storage but its own checked-out files and index.

## Ships

- [[Artifacts/14-41 workbench-benchmark|workbench-benchmark]] `skill` — Run the same task through prompt-only and workbench-guided pipelines on a project's own sample app and emit a five-outcome before/after report.

## Further reading

- [[Resources/Building Effective Agents|Building Effective Agents]] ([link](https://www.anthropic.com/research/building-effective-agents)) ·  also cited by 16 other lessons
- [[Resources/Cloudflare, Orchestrating AI Code Review at Scale|Cloudflare, Orchestrating AI Code Review at Scale]] ([link](https://blog.cloudflare.com/ai-code-review/)) — 131k review runs / 30 days in production ·  also cited by 2 other lessons
- [[Resources/LangChain, The Anatomy of an Agent Harness|LangChain, The Anatomy of an Agent Harness]] ([link](https://blog.langchain.com/the-anatomy-of-an-agent-harness/)) — Terminal Bench Top-30 to Top-5 receipt ·  also cited by 1 other lesson
- [[Resources/MongoDB, The Agent Harness- Why the LLM Is the Smallest Part of Your Agent System|MongoDB, The Agent Harness: Why the LLM Is the Smallest Part of Your Agent System]] ([link](https://www.mongodb.com/company/blog/technical/agent-harness-why-llm-is-smallest-part-of-your-agent-system)) — Vercel + Harvey numbers ·  also cited by 1 other lesson
- [[Resources/HN- Improving 15 LLMs at Coding in One Afternoon. Only the Harness Changed|HN: Improving 15 LLMs at Coding in One Afternoon. Only the Harness Changed]] ([link](https://news.ycombinator.com/item?id=46988596)) — replicated across 15 models ·  also cited by 1 other lesson
- [[Resources/preprints.org, Harness Engineering for Language Agents (March 2026)|preprints.org, Harness Engineering for Language Agents (March 2026)]] ([link](https://www.preprints.org/manuscript/202603.1756)) — 88% enterprise failure rate, runtime root causes ·  also cited by 1 other lesson

## In learning paths

- [[Paths/Agent-Assisted Engineering|Agent-Assisted Engineering]] — step 14, required


%% ── my notes ── %%
