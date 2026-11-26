---
id: "lesson:19/06"
type: lesson
ref: 19/06
phase: 19
num: 6
title: "Capstone 06 — DevOps Troubleshooting Agent for Kubernetes"
lesson_type: capstone
languages:
  - Python
  - TypeScript
time_min: 1800
on_route: false
quiz_count: 7
code_files: 10
concepts: 7
prereqs: 0
community: 46
libraries:
  - hono
  - zod
aliases:
  - 19/06
  - 19-06
tags:
  - phase/19
  - type/capstone
  - community/46
  - stdlib-only
source: ai-engineering-from-scratch/phases/19-capstone-projects/06-devops-troubleshooting-agent/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/06-devops-troubleshooting-agent"
---

# 19/06 Capstone 06 — DevOps Troubleshooting Agent for Kubernetes

> AWS's DevOps Agent went GA, Resolve AI published its K8s playbooks, NeuBird demoed semantic monitoring, and Metoro tied AI SRE to per-service SLOs. The production shape is settled: an alert webhook fires, an agent reads telemetry, walks a graph of K8s objects, ranks root-cause hypotheses, and posts a Slack brief with approval buttons. Read-only by default. Every remediation gated by a human. This capstone is that agent, evaluated on 20 synthetic incidents and compared against AWS's Agent on three shared cases.

**Phase:** [[Phases/19 Capstone Projects|Phase 19: Capstone Projects]] · **Type:** Capstone · **Time:** 1800 min · **Languages:** Python, TypeScript · **Status:** —  
**Open:** [[Upstream/19-capstone-projects/06-devops-troubleshooting-agent/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/06-devops-troubleshooting-agent) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/19-capstone-projects/06-devops-troubleshooting-agent) · code: main.py, ts/src/agent.ts, ts/src/blocks.ts, ts/src/index.ts, ts/src/server.ts, ts/src/slack_verify.ts … · quiz: 7 questions  
**Community:** [[Communities/46 Audit Log · Observability · Incident Response|46 Audit Log · Observability · Incident Response]] · **Libraries:** [[Libraries/hono (typescript)|hono]], [[Libraries/zod (typescript)|zod]]  

## Prerequisites

Stated upstream: `Phase 11 (LLM engineering), Phase 13 (tools and MCP), Phase 14 (agents), Phase 15 (autonomous), Phase 17 (infrastructure), Phase 18 (safety)`

- Whole phase: [[Phases/11 LLM Engineering|Phase 11: LLM Engineering]] — LLM engineering ·  medium confidence
- Whole phase: [[Phases/13 Tools & Protocols|Phase 13: Tools & Protocols]] — tools and MCP ·  medium confidence
- Whole phase: [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] — agents ·  medium confidence
- Whole phase: [[Phases/15 Autonomous Systems|Phase 15: Autonomous Systems]] — autonomous ·  medium confidence
- Whole phase: [[Phases/17 Infrastructure & Production|Phase 17: Infrastructure & Production]] — infrastructure ·  medium confidence
- Whole phase: [[Phases/18 Ethics, Safety & Alignment|Phase 18: Ethics, Safety & Alignment]] — safety ·  medium confidence

## Concepts taught

- K8s knowledge graph `lesson term` — Nodes = K8s objects + telemetry series; edges = ownership, scheduling, observation
- Read-only-by-default `lesson term` — Agent's service account has only get/list/describe verbs; destructive verbs live in a separate server behind approval
- [[Concepts/Audit Log|Audit Log]] `glossary` — Append-only record of every candidate command, whether it ran, who approved
- Hypothesis ranking `lesson term` — Recency × specificity × graph-path length inverse × citation count
- Slack approval card `lesson term` — Interactive Slack message with remediation buttons; agent cannot proceed until a human clicks
- Telemetry citation `lesson term` — A Prometheus query, Loki selector, or Tempo trace URL that supports a claim
- MTTR `lesson term` — Wall-clock from alert fire to SLO recovery

## Ships

- [[Artifacts/19-06 devops-agent|devops-agent]] `skill` — Build a Kubernetes troubleshooting agent that walks a cluster knowledge graph, ranks root causes, and gates every remediation through Slack.

## Further reading

- ArgoCD rollback ([link](https://argo-cd.readthedocs.io/en/stable/user-guide/commands/argocd_app_rollback/)) — the gated remediation target
- AWS DevOps Agent GA ([link](https://aws.amazon.com/blogs/aws/aws-devops-agent-helps-you-accelerate-incident-response-and-improve-system-reliability-preview/)) — the canonical 2026 reference
- FastMCP ([link](https://github.com/jlowin/fastmcp)) — Python MCP server framework
- kube-state-metrics ([link](https://github.com/kubernetes/kube-state-metrics)) — the cluster-state source
- [[Resources/LangGraph documentation|LangGraph documentation]] ([link](https://langchain-ai.github.io/langgraph/)) — reference agent orchestrator ·  also cited by 3 other lessons
- Metoro AI SRE ([link](https://metoro.io)) — SLO-first production framing
- [[Resources/NeuBird Hawkeye|NeuBird Hawkeye]] ([link](https://www.neubird.ai/)) — semantic-graph approach ·  also cited by 1 other lesson
- Resolve AI K8s troubleshooting ([link](https://resolve.ai/blog/kubernetes-troubleshooting-in-resolve-ai)) — the competitor reference


%% ── my notes ── %%
