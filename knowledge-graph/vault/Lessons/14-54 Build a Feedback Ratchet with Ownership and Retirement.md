---
id: "lesson:14/54"
type: lesson
ref: 14/54
phase: 14
num: 54
title: Build a Feedback Ratchet with Ownership and Retirement
lesson_type: learn+build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 6
code_files: 2
concepts: 0
prereqs: 2
community: 44
aliases:
  - 14/54
  - 14-54
tags:
  - phase/14
  - type/learn+build
  - community/44
  - stdlib-only
source: ai-engineering-from-scratch/phases/14-agent-engineering/54-build-the-feedback-ratchet/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/54-build-the-feedback-ratchet"
---

# 14/54 Build a Feedback Ratchet with Ownership and Retirement

> Shipping closes one build loop and opens the learning loop. Evidence must change the system or it becomes telemetry nobody owns.

**Phase:** [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] · **Type:** Learn + Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/14-agent-engineering/54-build-the-feedback-ratchet/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/54-build-the-feedback-ratchet) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/14-agent-engineering/54-build-the-feedback-ratchet) · code: main.py, tests/test_main.py · quiz: 6 questions  
**Community:** [[Communities/44 Define the Outcome Before You Choose the Output · Discover the Workflow People Actually Perform · Map Assum|44 Define the Outcome Before You Choose the Output · Discover the Workflow People Actually Perform · Map Assumptions and Resolve the Riskiest One First]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 14 lessons 46 and 53`

- [[Lessons/14-46 Turn Every Agent Correction into a System Improvement|14/46 Turn Every Agent Correction into a System Improvement]]
- [[Lessons/14-53 Choose Prototype, Pilot, or Production Deliberately|14/53 Choose Prototype, Pilot, or Production Deliberately]]

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/14-37 Runtime Feedback Loops|14/37 Runtime Feedback Loops]], [[Lessons/14-38 Verification Gates|14/38 Verification Gates]], [[Lessons/14-39 Reviewer Agent- Separate Builder from Marker|14/39 Reviewer Agent: Separate Builder from Marker]], [[Lessons/14-40 Multi-Session Handoff|14/40 Multi-Session Handoff]], [[Lessons/14-41 The Workbench on a Real Repo|14/41 The Workbench on a Real Repo]], [[Lessons/14-50 Choose the Smallest Slice That Can Change the Decision|14/50 Choose the Smallest Slice That Can Change the Decision]], [[Lessons/14-51 Write Specifications That Preserve Judgment|14/51 Write Specifications That Preserve Judgment]], [[Lessons/14-52 Design Success Metrics Before the Result Exists|14/52 Design Success Metrics Before the Result Exists]]
- depth 3: [[Lessons/14-32 The Minimal Agent Workbench|14/32 The Minimal Agent Workbench]], [[Lessons/14-33 Agent Instructions as Executable Constraints|14/33 Agent Instructions as Executable Constraints]], [[Lessons/14-34 Repo Memory and Durable State|14/34 Repo Memory and Durable State]], [[Lessons/14-35 Initialization Scripts for Agents|14/35 Initialization Scripts for Agents]], [[Lessons/14-36 Scope Contracts and Task Boundaries|14/36 Scope Contracts and Task Boundaries]], [[Lessons/14-47 Define the Outcome Before You Choose the Output|14/47 Define the Outcome Before You Choose the Output]], [[Lessons/14-49 Map Assumptions and Resolve the Riskiest One First|14/49 Map Assumptions and Resolve the Riskiest One First]]

## Further reading

- [[Resources/Basili, Caldiera, and Rombach, The Goal Question Metric Approach|Basili, Caldiera, and Rombach, The Goal Question Metric Approach]] ([link](https://www.cs.toronto.edu/~sme/CSC444F/handouts/GQM-paper.pdf)) — for organizational learning through goal-oriented measurement. ·  also cited by 2 other lessons
- [[Resources/Nuseibeh and Easterbrook, Requirements Engineering- A Roadmap|Nuseibeh and Easterbrook, Requirements Engineering: A Roadmap]] ([link](https://www.cs.toronto.edu/~sme/papers/2000/ICSE2000.pdf)) — for treating requirements as evolving through the system lifecycle. ·  also cited by 5 other lessons
- [[Resources/Fagerholm et al., Building Blocks for Continuous Experimentation|Fagerholm et al., Building Blocks for Continuous Experimentation]] ([link](https://doi.org/10.1145/2601248.2601276)) — for the technical and organizational loop that connects evidence to continued product development. ·  also cited by 1 other lesson

## In learning paths

- [[Paths/Developer Experience and Education|Developer Experience and Education]] — step 11, required
- [[Paths/Customer AI Deployment|Customer AI Deployment]] — step 12, required
- [[Paths/Product Judgment and Delivery|Product Judgment and Delivery]] — step 8, required


%% ── my notes ── %%
