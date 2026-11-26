---
id: "lesson:18/25"
type: lesson
ref: 18/25
phase: 18
num: 25
title: EchoLeak and the Emergence of CVEs for AI
lesson_type: learn
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 6
code_files: 1
concepts: 8
prereqs: 1
aliases:
  - 18/25
  - 18-25
tags:
  - phase/18
  - type/learn
  - stdlib-only
source: ai-engineering-from-scratch/phases/18-ethics-safety-alignment/25-echoleak-cves-for-ai/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/25-echoleak-cves-for-ai"
---

# 18/25 EchoLeak and the Emergence of CVEs for AI

> CVE-2025-32711 "EchoLeak" (CVSS 9.3) was the first publicly documented zero-click prompt injection in a production LLM system (Microsoft 365 Copilot). Discovered by Aim Labs (Aim Security), disclosed to MSRC, patched via server-side update June 2025. Attack: attacker sends a crafted email to any employee; the victim's Copilot retrieves the email as RAG context during a routine query; hidden instructions execute; Copilot exfiltrates sensitive organizational data via a CSP-approved Microsoft domain. Bypassed XPIA prompt-injection filters and Copilot's link-redaction mechanisms. Aim Labs's term: "LLM Scope Violation" — external untrusted input manipulates the model to access and leak confidential data. Related: CamoLeak (CVSS 9.6, GitHub Copilot Chat) exploited the Camo image proxy; fixed by disabling image rendering entirely. GitHub Copilot RCE CVE-2025-53773. NIST has called indirect prompt injection "generative AI's greatest security flaw"; OWASP 2025 ranks it #1 threat to LLM applications.

**Phase:** [[Phases/18 Ethics, Safety & Alignment|Phase 18: Ethics, Safety & Alignment]] · **Type:** Learn · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/18-ethics-safety-alignment/25-echoleak-cves-for-ai/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/25-echoleak-cves-for-ai) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/18-ethics-safety-alignment/25-echoleak-cves-for-ai) · code: main.py · quiz: 6 questions  
**Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 18 · 15 (indirect prompt injection)`

- [[Lessons/18-15 Indirect Prompt Injection — Production Attack Surface|18/15 Indirect Prompt Injection — Production Attack Surface]] — indirect prompt injection

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/18-12 Red-Teaming- PAIR and Automated Attacks|18/12 Red-Teaming: PAIR and Automated Attacks]]
- depth 3: [[Lessons/18-01 Instruction-Following as Alignment Signal|18/01 Instruction-Following as Alignment Signal]]

## Builds on this

- [[Lessons/18-28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR|18/28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR]]

## Concepts taught

- EchoLeak `lesson term` — CVE-2025-32711, CVSS 9.3, zero-click prompt injection
- LLM Scope Violation `lesson term` — Untrusted input triggers privileged-scope access + exfiltration
- CamoLeak `lesson term` — CVSS 9.6 via Camo image proxy; image rendering disabled in fix
- [[Concepts/Zero-click|Zero-click]] `lesson term` — Attack fires during routine agent operation
- XPIA `lesson term` — Cross-Prompt Injection Attack filter; bypassed by EchoLeak
- OWASP LLM01 `lesson term` — Prompt injection; OWASP's 2025 ranking
- Three-boundary model `lesson term` — Retrieval, scope, output — each must be independently controlled
- [[Concepts/Data Exfiltration|Data Exfiltration]] `glossary` — Unauthorized transfer of protected data from a system or trust zone to a person, tool, service, or storage location that is not permitted to receive it.

## Ships

- [[Artifacts/18-25 cve-review|cve-review]] `skill` — Review a production AI deployment for LLM Scope Violation exposure.

## Further reading

- Aim Labs — EchoLeak writeup (June 2025) ([link](https://www.aim.security/lp/aim-labs-echoleak-blogpost)) — the CVE disclosure
- Aim Labs — LLM Scope Violation framework ([link](https://arxiv.org/html/2509.10540v1)) — the threat-model framework
- [[Resources/OWASP — LLM Top 10 (2025)|OWASP — LLM Top 10 (2025)]] ([link](https://genai.owasp.org/llm-top-10/)) — LLM01 prompt injection ·  also cited by 1 other lesson
- Microsoft MSRC CVE-2025-32711 ([link](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32711)) — CVE record


%% ── my notes ── %%
