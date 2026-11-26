---
id: "concept:jailbreak"
type: concept
name: Jailbreak
canonical: true
category: "Security & governance"
taught_in: 2
community: 14
tags:
  - concept/glossary
  - category/security-and-governance
  - community/14
source: ai-engineering-from-scratch/glossary/terms.md
---

# Jailbreak

**Community:** [[Communities/14 Least Privilege · Prompt Injection · Sandbox|14 Least Privilege · Prompt Injection · Sandbox]]

**What it actually means:** An adversarial input or interaction strategy intended to make a model produce behavior that its training or application controls are designed to prevent.

**Why it matters:** Successful jailbreaks expose gaps between stated policy and actual behavior, and they can become more consequential when the model controls tools or protected data.

**In practice:** Derive test families from prohibited behaviors, vary format and interaction length, measure both refusal and harmful completion, and convert confirmed failures into versioned adversarial evals.

**Common confusion:** A jailbreak targets model or system behavioral restrictions. Prompt injection redirects instruction following, often toward an attacker's goal; one interaction can involve both.

**Category:** [[Categories/Security & governance|Security & governance]]

## Related concepts

- [[Concepts/Eval Set|Eval Set]]
- [[Concepts/Guardrails|Guardrails]]
- [[Concepts/Prompt Injection|Prompt Injection]]
- [[Concepts/Red Teaming|Red Teaming]]

## Taught in

- [[Lessons/11-12 Guardrails, Safety & Content Filtering|11/12 Guardrails, Safety & Content Filtering]] — Techniques that override the model's safety training (not your system prompt) to produce content the model would normally refuse
- [[Lessons/19-82 Capstone 82 — Jailbreak Taxonomy|19/82 Capstone 82 — Jailbreak Taxonomy]] — a prompt that produces output violating a stated policy

## Sources

- [[Resources/Universal and Transferable Adversarial Attacks on Aligned Language Models|Universal and Transferable Adversarial Attacks on Aligned Language Models]] ([link](https://arxiv.org/abs/2307.15043))


%% ── my notes ── %%
