---
id: "lesson:19/09"
type: lesson
ref: 19/09
phase: 19
num: 9
title: "Capstone 09 — Code Migration Agent (Repo-Level Language / Runtime Upgrade)"
lesson_type: capstone
languages:
  - Python
  - Java
  - Python
  - TypeScript
time_min: 1800
on_route: false
quiz_count: 7
code_files: 8
concepts: 7
prereqs: 0
community: 83
libraries:
  - "@hono/node-server"
  - hono
aliases:
  - 19/09
  - 19-09
tags:
  - phase/19
  - type/capstone
  - community/83
  - stdlib-only
source: ai-engineering-from-scratch/phases/19-capstone-projects/09-code-migration-agent/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/09-code-migration-agent"
---

# 19/09 Capstone 09 — Code Migration Agent (Repo-Level Language / Runtime Upgrade)

> Amazon's MigrationBench (Java 8 to 17) and Google's App Engine Py2-to-Py3 migrator set the 2026 bar. Moderne's OpenRewrite does deterministic AST rewrites at scale. Grit targets the same problem with codemod-style DSL. The production pattern combines both: a deterministic substrate for safe rewrites plus an agent layer for the ambiguous cases, a sandbox for per-branch builds, and a test harness that flips green before the PR opens. The capstone is to migrate 50 real repos and publish a pass rate with a failure taxonomy.

**Phase:** [[Phases/19 Capstone Projects|Phase 19: Capstone Projects]] · **Type:** Capstone · **Time:** 1800 min · **Languages:** Python, Java, Python, TypeScript · **Status:** —  
**Open:** [[Upstream/19-capstone-projects/09-code-migration-agent/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/09-code-migration-agent) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/19-capstone-projects/09-code-migration-agent) · code: main.py, ts/src/cost.ts, ts/src/index.ts, ts/src/migrations.ts, ts/src/server.ts, ts/src/types.ts … · quiz: 7 questions  
**Community:** [[Communities/83 Coverage delta · Verification|83 Coverage delta · Verification]] · **Libraries:** [[Libraries/@hono-node-server (typescript)|@hono/node-server]], [[Libraries/hono (typescript)|hono]]  

## Prerequisites

Stated upstream: `Phase 5 (NLP), Phase 7 (transformers), Phase 11 (LLM engineering), Phase 13 (tools), Phase 14 (agents), Phase 15 (autonomous), Phase 17 (infrastructure)`

- Whole phase: [[Phases/11 LLM Engineering|Phase 11: LLM Engineering]] — LLM engineering ·  medium confidence
- Whole phase: [[Phases/13 Tools & Protocols|Phase 13: Tools & Protocols]] — tools ·  medium confidence
- Whole phase: [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] — agents ·  medium confidence
- Whole phase: [[Phases/15 Autonomous Systems|Phase 15: Autonomous Systems]] — autonomous ·  medium confidence
- Whole phase: [[Phases/17 Infrastructure & Production|Phase 17: Infrastructure & Production]] — infrastructure ·  medium confidence
- Whole phase: [[Phases/05 NLP, Foundations to Advanced|Phase 5: NLP, Foundations to Advanced]] — NLP ·  medium confidence
- Whole phase: [[Phases/07 Transformers Deep Dive|Phase 7: Transformers Deep Dive]] — transformers ·  medium confidence

## Concepts taught

- Deterministic substrate `lesson term` — OpenRewrite / libcst: declarative AST rewrites with safety guarantees
- Codemod `lesson term` — A rewrite rule that changes source code mechanically
- Build drift `lesson term` — Subtle Maven / Gradle / uv behavior changes between major versions
- Failure class `lesson term` — A labeled reason a repo did not migrate: dep, syntax, test, build-tool, budget
- [[Concepts/Coverage delta|Coverage delta]] `lesson term` — Change in test coverage % from base to migrated branch
- Agent turn `lesson term` — One plan -> act -> observe cycle in the agent loop
- Budget exhaustion `lesson term` — The repo consumed its 30-min / $8 / 20-turn limit without passing

## Ships

- [[Artifacts/19-09 migration-agent|migration-agent]] `skill` — Build a repo-level code migration agent that combines deterministic recipes with an agent fallback loop, passes MigrationBench, and publishes a failure taxonomy.

## Further reading

- Amazon MigrationBench ([link](https://aws.amazon.com/blogs/devops/amazon-introduces-two-benchmark-datasets-for-evaluating-ai-agents-ability-on-code-migration/)) — the canonical 2026 benchmark
- Google App Engine Py2 to Py3 migrator ([link](https://cloud.google.com/appengine)) — alternate migration benchmark
- [[Resources/Daytona sandboxes|Daytona sandboxes]] ([link](https://daytona.io)) — reference per-branch sandbox ·  also cited by 1 other lesson
- OpenAI sandboxed migration cookbook ([link](https://developers.openai.com/cookbook/examples/agents_sdk/sandboxed-code-migration/sandboxed_code_migration_agent)) — the Agents SDK reference
- OpenRewrite documentation ([link](https://docs.openrewrite.org)) — recipe authoring
- libcst ([link](https://github.com/Instagram/LibCST)) — Python deterministic substrate
- Grit.io ([link](https://www.grit.io)) — alternate codemod DSL
- Moderne.io OpenRewrite platform ([link](https://www.moderne.io)) — the deterministic substrate reference


%% ── my notes ── %%
