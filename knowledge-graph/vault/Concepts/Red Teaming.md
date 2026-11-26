---
id: "concept:red-teaming"
type: concept
name: Red Teaming
canonical: true
category: "Security & governance"
taught_in: 3
community: 14
tags:
  - concept/glossary
  - category/security-and-governance
  - community/14
source: ai-engineering-from-scratch/glossary/terms.md
---

# Red Teaming

**Community:** [[Communities/14 Least Privilege · Prompt Injection · Sandbox|14 Least Privilege · Prompt Injection · Sandbox]]

**What it actually means:** A structured adversarial testing process in which authorized testers seek failures using documented objectives, threat assumptions, cases, and evidence.

**Why it matters:** Ordinary quality tests rarely explore how a system behaves under manipulation, misuse, conflicting goals, or determined attempts to bypass controls.

**In practice:** Derive attacks from a threat model, run them in an isolated environment, record reproducible cases, remediate by layer, and convert confirmed failures into regression evals.

**Common confusion:** A list of jailbreak prompts is not a complete red-team program, and red teaming cannot prove the absence of unknown failures.

**Category:** [[Categories/Security & governance|Security & governance]]

## Related concepts

- [[Concepts/Eval Set|Eval Set]]
- [[Concepts/Guardrails|Guardrails]]
- [[Concepts/Jailbreak|Jailbreak]]
- [[Concepts/Prompt Injection|Prompt Injection]]
- [[Concepts/Threat Model|Threat Model]]

## Taught in

- [[Lessons/11-12 Guardrails, Safety & Content Filtering|11/12 Guardrails, Safety & Content Filtering]] — Systematically trying to break your LLM application with adversarial prompts to find vulnerabilities before attackers do
- [[Lessons/19-05 Capstone 05 — Autonomous Research Agent (AI-Scientist Class)|19/05 Capstone 05 — Autonomous Research Agent (AI-Scientist Class)]] `alias` — Adversarial tasks that would escape the sandbox if the policy is wrong
- [[Lessons/19-08 Capstone 08 — Production RAG Chatbot for a Regulated Vertical|19/08 Capstone 08 — Production RAG Chatbot for a Regulated Vertical]] `alias` — Pre-release jailbreak, PII extraction, off-domain probes

## Sources

- Red Teaming Language Models with Language Models ([link](https://arxiv.org/abs/2202.03286))


%% ── my notes ── %%
