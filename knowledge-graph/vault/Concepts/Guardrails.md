---
id: "concept:guardrails"
type: concept
name: Guardrails
canonical: true
category: "Evaluation & safety"
taught_in: 3
community: 14
tags:
  - concept/glossary
  - category/evaluation-and-safety
  - community/14
source: ai-engineering-from-scratch/glossary/terms.md
---

# Guardrails

**Community:** [[Communities/14 Least Privilege · Prompt Injection · Sandbox|14 Least Privilege · Prompt Injection · Sandbox]]

> *What people say:* Safety filters around a model.

**What it actually means:** System controls that constrain inputs, tool use, outputs, permissions, and escalation. They can include schemas, policy checks, classifiers, allowlists, sandboxing, approvals, and post-action verification.

**Why it matters:** No single filter covers all failure modes, so controls should be layered according to risk.

**Common confusion:** Guardrails reduce risk; they do not prove that an AI system is safe.

**Category:** [[Categories/Evaluation & safety|Evaluation & safety]]

## Related concepts

- [[Concepts/AI Risk Assessment|AI Risk Assessment]]
- [[Concepts/Alignment|Alignment]]
- [[Concepts/Approval Gate|Approval Gate]]
- [[Concepts/Defense in Depth|Defense in Depth]]
- [[Concepts/Evaluation (Eval)|Evaluation (Eval)]]
- [[Concepts/Human-in-the-Loop (HITL)|Human-in-the-Loop (HITL)]]
- [[Concepts/Jailbreak|Jailbreak]]
- [[Concepts/Least Privilege|Least Privilege]]
- [[Concepts/Precision & Recall|Precision & Recall]]
- [[Concepts/Red Teaming|Red Teaming]]
- [[Concepts/Sandbox|Sandbox]]
- [[Concepts/System Prompt|System Prompt]]

## Taught in

- [[Lessons/11-12 Guardrails, Safety & Content Filtering|11/12 Guardrails, Safety & Content Filtering]] — Any validation layer that checks input or output of an LLM application for safety, relevance, or policy compliance
- [[Lessons/13-21 LLM Routing Layer — LiteLLM, OpenRouter, Portkey|13/21 LLM Routing Layer — LiteLLM, OpenRouter, Portkey]] — Redact PII, reject policy violations
- [[Lessons/14-16 OpenAI Agents SDK- Handoffs, Guardrails, Tracing|14/16 OpenAI Agents SDK: Handoffs, Guardrails, Tracing]] `alias` — Validation on input / output / tool invocation


%% ── my notes ── %%
