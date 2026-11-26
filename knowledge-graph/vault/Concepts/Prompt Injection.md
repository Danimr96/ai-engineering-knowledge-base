---
id: "concept:prompt-injection"
type: concept
name: Prompt Injection
canonical: true
category: "Evaluation & safety"
taught_in: 4
community: 14
tags:
  - concept/glossary
  - category/evaluation-and-safety
  - community/14
source: ai-engineering-from-scratch/glossary/terms.md
---

# Prompt Injection

**Community:** [[Communities/14 Least Privilege · Prompt Injection · Sandbox|14 Least Privilege · Prompt Injection · Sandbox]]

> *What people say:* An adversarial instruction that redirects a model.

**What it actually means:** An attack or failure mode in which untrusted content influences a model to disregard intended instructions, expose data, misuse tools, or take actions outside the user's goal. The content can arrive directly from a user or indirectly through retrieved pages, files, messages, or tool output.

**Why it matters:** Models process instructions and data through the same language channel, so input filtering alone cannot reliably separate every malicious instruction from legitimate content.

**In practice:** Treat external content as untrusted, isolate it from authority-bearing instructions, minimize tool permissions, require approval for consequential writes, and verify outputs and actions.

**Common confusion:** Prompt injection is not technically the same mechanism as SQL injection, and a stronger system prompt is not a complete defense.

**Category:** [[Categories/Evaluation & safety|Evaluation & safety]]

## Related concepts

- [[Concepts/Approval Gate|Approval Gate]]
- [[Concepts/Indirect Prompt Injection|Indirect Prompt Injection]]
- [[Concepts/Instruction Hierarchy|Instruction Hierarchy]]
- [[Concepts/Jailbreak|Jailbreak]]
- [[Concepts/Least Privilege|Least Privilege]]
- [[Concepts/Red Teaming|Red Teaming]]
- [[Concepts/Sandbox|Sandbox]]
- [[Concepts/System Prompt|System Prompt]]
- [[Concepts/Threat Model|Threat Model]]
- [[Concepts/Tool Contract|Tool Contract]]

## Taught in

- [[Lessons/05-17 Chatbots — Rule-Based to Neural to LLM Agents|05/17 Chatbots — Rule-Based to Neural to LLM Agents]] — Malicious input that tries to override the system prompt.
- [[Lessons/11-01 Prompt Engineering- Techniques & Patterns|11/01 Prompt Engineering: Techniques & Patterns]] — An attack where user input contains instructions that override the system prompt, causing the model to ignore its rules
- [[Lessons/11-12 Guardrails, Safety & Content Filtering|11/12 Guardrails, Safety & Content Filtering]] — Crafting input that overrides the system prompt, causing the model to follow attacker instructions instead of developer instructions
- [[Lessons/14-27 Prompt Injection and the PVE Defense|14/27 Prompt Injection and the PVE Defense]]

## Sources

- OWASP prompt injection guidance ([link](https://genai.owasp.org/llmrisk/llm01-prompt-injection/))


%% ── my notes ── %%
