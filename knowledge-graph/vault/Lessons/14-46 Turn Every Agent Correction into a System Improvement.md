---
id: "lesson:14/46"
type: lesson
ref: 14/46
phase: 14
num: 46
title: Turn Every Agent Correction into a System Improvement
lesson_type: learn+build
languages:
  - Python
time_min: 65
on_route: false
quiz_count: 6
code_files: 2
concepts: 0
prereqs: 5
community: 15
aliases:
  - 14/46
  - 14-46
tags:
  - phase/14
  - type/learn+build
  - community/15
  - stdlib-only
source: ai-engineering-from-scratch/phases/14-agent-engineering/46-turn-feedback-into-system/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/46-turn-feedback-into-system"
---

# 14/46 Turn Every Agent Correction into a System Improvement

> A correction that lives only in chat fixes one run. A correction promoted into a test, boundary, example, or tool improves every later run.

**Phase:** [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] · **Type:** Learn + Build · **Time:** 65 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/14-agent-engineering/46-turn-feedback-into-system/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/46-turn-feedback-into-system) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/14-agent-engineering/46-turn-feedback-into-system) · code: main.py, tests/test_main.py · quiz: 6 questions  
**Community:** [[Communities/15 System of record · Block severity · Definition of done|15 System of record · Block severity · Definition of done]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 14 lessons 37 to 41`

- **14/37-41**:
    - [[Lessons/14-37 Runtime Feedback Loops|14/37 Runtime Feedback Loops]]
    - [[Lessons/14-38 Verification Gates|14/38 Verification Gates]]
    - [[Lessons/14-39 Reviewer Agent- Separate Builder from Marker|14/39 Reviewer Agent: Separate Builder from Marker]]
    - [[Lessons/14-40 Multi-Session Handoff|14/40 Multi-Session Handoff]]
    - [[Lessons/14-41 The Workbench on a Real Repo|14/41 The Workbench on a Real Repo]]

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/14-32 The Minimal Agent Workbench|14/32 The Minimal Agent Workbench]], [[Lessons/14-33 Agent Instructions as Executable Constraints|14/33 Agent Instructions as Executable Constraints]], [[Lessons/14-34 Repo Memory and Durable State|14/34 Repo Memory and Durable State]], [[Lessons/14-35 Initialization Scripts for Agents|14/35 Initialization Scripts for Agents]], [[Lessons/14-36 Scope Contracts and Task Boundaries|14/36 Scope Contracts and Task Boundaries]]
- depth 3: [[Lessons/14-31 Agent Workbench Engineering- Why Capable Models Still Fail|14/31 Agent Workbench Engineering: Why Capable Models Still Fail]]

## Builds on this

- [[Lessons/14-54 Build a Feedback Ratchet with Ownership and Retirement|14/54 Build a Feedback Ratchet with Ownership and Retirement]]

## Further reading

- [[Resources/Shinn et al., Reflexion- Language Agents with Verbal Reinforcement Learning (arXiv-2303.11366)|Shinn et al., Reflexion: Language Agents with Verbal Reinforcement Learning (arXiv:2303.11366)]] ([link](https://arxiv.org/abs/2303.11366)) — for using feedback traces to improve later decisions without changing model weights. ·  also cited by 1 other lesson
- [[Resources/Madaan et al., Self-Refine (arXiv-2303.17651)|Madaan et al., Self-Refine (arXiv:2303.17651)]] ([link](https://arxiv.org/abs/2303.17651)) — for iterative feedback and revision inside a task loop. ·  also cited by 3 other lessons
- [[Resources/Basili, Caldiera, and Rombach, The Goal Question Metric Approach|Basili, Caldiera, and Rombach, The Goal Question Metric Approach]] ([link](https://www.cs.toronto.edu/~sme/CSC444F/handouts/GQM-paper.pdf)) — for turning goals into questions and operational measurements. ·  also cited by 2 other lessons

## In learning paths

- [[Paths/Agent-Assisted Engineering|Agent-Assisted Engineering]] — step 15, required


%% ── my notes ── %%
