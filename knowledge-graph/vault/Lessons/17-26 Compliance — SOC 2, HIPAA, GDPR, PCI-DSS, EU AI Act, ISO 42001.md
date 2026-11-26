---
id: "lesson:17/26"
type: lesson
ref: 17/26
phase: 17
num: 26
title: "Compliance — SOC 2, HIPAA, GDPR, PCI-DSS, EU AI Act, ISO 42001"
lesson_type: learn
time_min: 60
on_route: false
quiz_count: 6
code_files: 1
concepts: 9
prereqs: 2
community: 30
aliases:
  - 17/26
  - 17-26
tags:
  - phase/17
  - type/learn
  - community/30
  - stdlib-only
source: ai-engineering-from-scratch/phases/17-infrastructure-and-production/26-compliance-frameworks/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/26-compliance-frameworks"
---

# 17/26 Compliance — SOC 2, HIPAA, GDPR, PCI-DSS, EU AI Act, ISO 42001

> Multi-framework coverage is table stakes for 2026 enterprise deals. **EU AI Act**: in force since August 1, 2024. Most high-risk requirements enforce August 2, 2026. Fines up to €15M or 3% global annual turnover for high-risk-system obligations (Art. 99(4)); up to €35M or 7% for prohibited AI practices (Art. 99(3)). Applies globally if serving EU users. **Colorado AI Act**: effective June 30, 2026 (delayed from February 2026 by SB25B-004) — impact assessments for high-risk systems, right to appeal AI decisions. Virginia similar for credit/employment/housing/education. **SOC 2 Type II**: de facto B2B AI requirement (Type II, not Type I, for fintech). **GDPR**: largest documented AI-specific fine is €30.5M against Clearview AI (Dutch DPA, Sept 2024); Italy's Garante issued €15M against OpenAI in Dec 2024 (later overturned on appeal in March 2026). Real-time PII redaction at inference is the defensible standard; post-processing cleanup is not enough. **HIPAA**: healthcare bound — cannot send PHI to external AI services without BAA. **PCI-DSS**: AI-interaction-layer coverage requires configuration + contractual agreements, not automatic. **ISO 42001**: emerging AI governance standard, growing procurement requirement alongside ISO 27001. Reference profile: OpenAI maintains SOC 2 Type 2, ISO/IEC 27001:2022, ISO/IEC 27701:2019, GDPR/CCPA/HIPAA (BAA)/FERPA, PCI-DSS for ChatGPT payment components. Cross-framework mapping reduces audit fatigue: access controls map across ISO 27001 A.5.15-5.18, GDPR Art. 32, HIPAA §164.312(a).

**Phase:** [[Phases/17 Infrastructure & Production|Phase 17: Infrastructure & Production]] · **Type:** Learn · **Time:** 60 min · **Status:** —  
**Open:** [[Upstream/17-infrastructure-and-production/26-compliance-frameworks/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/26-compliance-frameworks) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/17-infrastructure-and-production/26-compliance-frameworks) · code: main.py · quiz: 6 questions  
**Community:** [[Communities/30 Evaluation (Eval) · Kill switch · Non-determinism|30 Evaluation (Eval) · Kill switch · Non-determinism]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 17 · 25 (Security), Phase 17 · 13 (Observability)`

- [[Lessons/17-13 LLM Observability Stack Selection|17/13 LLM Observability Stack Selection]] — Observability
- [[Lessons/17-25 Security — Secrets, API Key Rotation, Audit Logs, Guardrails|17/25 Security — Secrets, API Key Rotation, Audit Logs, Guardrails]] — Security

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/17-08 Inference Metrics — TTFT, TPOT, ITL, Goodput, P99|17/08 Inference Metrics — TTFT, TPOT, ITL, Goodput, P99]], [[Lessons/17-19 AI Gateways — LiteLLM, Portkey, Kong AI Gateway, Bifrost|17/19 AI Gateways — LiteLLM, Portkey, Kong AI Gateway, Bifrost]]
- depth 3: [[Lessons/17-01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI|17/01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI]], [[Lessons/17-04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill|17/04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill]], [[Lessons/17-16 Model Routing as a Cost-Reduction Primitive|17/16 Model Routing as a Cost-Reduction Primitive]]

## Concepts taught

- SOC 2 Type II `lesson term` — Controls operating over 6-12 months, independently attested
- HIPAA BAA `lesson term` — Business Associate Agreement; required for PHI
- GDPR `lesson term` — Real-time PII redaction is the defensible 2026 standard
- [[Concepts/EU AI Act|EU AI Act]] `lesson term` — High-risk enforcement August 2026; €15M / 3% (high-risk obligations) — €35M / 7% (prohibited practices)
- Colorado AI Act `lesson term` — June 30, 2026 effective (delayed by SB25B-004); impact assessments
- ISO 42001 `lesson term` — Emerging framework for AI risk + transparency
- ISO 27001 `lesson term` — Information Security Management System baseline
- Conformity assessment `lesson term` — High-risk requirement: docs, testing, logging
- Cross-framework mapping `lesson term` — Single policy satisfies multiple framework controls

## Ships

- [[Artifacts/17-26 compliance-matrix|compliance-matrix]] `skill` — Produce the required-framework matrix for an LLM SaaS given customer geography, segment, and contract scope. Map controls across SOC 2, HIPAA, GDPR, PCI-DSS, EU AI Act, Colorado AI Act, ISO 42001.

## Further reading

- Dsalta — SOC 2 Type 2 Audit Guide 2026: 10 AI Controls ([link](https://www.dsalta.com/resources/ai-compliance/soc-2-type-2-audit-guide-2026-10-ai-powered-controls-every-saas-team-needs))
- EU AI Act official text ([link](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)) — primary source.
- GuardionAI — LLM Compliance 2026: ISO 42001, EU AI Act, SOC 2, GDPR ([link](https://guardion.ai/blog/llm-compliance-guide-iso-42001-eu-ai-act-soc2-gdpr-2026))
- ISO/IEC 42001:2023 ([link](https://www.iso.org/standard/81230.html)) — AI management system standard.
- Colorado AI Act ([link](https://leg.colorado.gov/bills/sb24-205)) — primary source.
- OpenAI Security and Privacy ([link](https://openai.com/security-and-privacy/)) — reference compliance profile.


%% ── my notes ── %%
