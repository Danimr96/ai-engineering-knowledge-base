---
id: "concept:indirect-prompt-injection"
type: concept
name: Indirect Prompt Injection
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

# Indirect Prompt Injection

**Community:** [[Communities/14 Least Privilege · Prompt Injection · Sandbox|14 Least Privilege · Prompt Injection · Sandbox]]

**What it actually means:** A prompt-injection attack delivered through content the system retrieves or observes, such as a webpage, document, email, image text, or tool result, rather than directly through the user's instruction.

**Why it matters:** An agent can encounter attacker-controlled instructions while performing an authorized task and mistake that content for authority-bearing guidance.

**In practice:** Label external content as untrusted data, separate it from instructions, minimize tool permissions, require approval for consequential actions, and include malicious retrieved content in regression tests.

**Common confusion:** Indirect describes the delivery path, not a weaker attack. A hidden instruction in retrieved content can be as consequential as a direct user prompt.

**Category:** [[Categories/Security & governance|Security & governance]]

## Related concepts

- [[Concepts/Data Exfiltration|Data Exfiltration]]
- [[Concepts/Instruction Hierarchy|Instruction Hierarchy]]
- [[Concepts/Prompt Injection|Prompt Injection]]
- [[Concepts/Trust Boundary|Trust Boundary]]

## Taught in

- [[Lessons/14-27 Prompt Injection and the PVE Defense|14/27 Prompt Injection and the PVE Defense]] — Instructions embedded in data the agent retrieves
- [[Lessons/15-11 Browser Agents and Long-Horizon Web Tasks|15/11 Browser Agents and Long-Horizon Web Tasks]] — Untrusted content in a page the agent reads contains instructions the agent executes
- [[Lessons/18-15 Indirect Prompt Injection — Production Attack Surface|18/15 Indirect Prompt Injection — Production Attack Surface]]

## Sources

- [[Resources/Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection|Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection]] ([link](https://arxiv.org/abs/2302.12173))


%% ── my notes ── %%
