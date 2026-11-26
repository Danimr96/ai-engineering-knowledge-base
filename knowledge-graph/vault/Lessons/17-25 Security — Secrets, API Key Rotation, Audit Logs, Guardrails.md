---
id: "lesson:17/25"
type: lesson
ref: 17/25
phase: 17
num: 25
title: "Security — Secrets, API Key Rotation, Audit Logs, Guardrails"
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 6
code_files: 1
concepts: 11
prereqs: 2
community: 30
aliases:
  - 17/25
  - 17-25
tags:
  - phase/17
  - type/learn
  - community/30
  - stdlib-only
source: ai-engineering-from-scratch/phases/17-infrastructure-and-production/25-security-secrets-audit/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/25-security-secrets-audit"
---

# 17/25 Security — Secrets, API Key Rotation, Audit Logs, Guardrails

> Eliminate secret sprawl via centralized vaults (HashiCorp Vault, AWS Secrets Manager, Azure Key Vault). Never store credentials in config files, env files in VCS, spreadsheets. Use IAM roles over static keys; OIDC for CI/CD. The AI-gateway pattern is the 2026 solution: apps → gateway → model provider, with gateway pulling credentials from vault at runtime. Rotate in vault and all apps pick up in minutes — no redeploys, no Slack "who has the new key" messages. Rotation policy ≤90 days; scan with TruffleHog / GitGuardian / Gitleaks on every commit. Zero-trust: MFA, SSO, RBAC/ABAC, short-lived tokens, device posture. PII scrubbing uses entity recognition to mask PHI/PII before forwarding; consistent tokenization (Mesh approach) maps sensitive values to stable placeholders so the LLM preserves code/relationship semantics. Network egress: LLM services in dedicated VPC/VNet subnet whitelisting only `api.openai.com`, `api.anthropic.com` etc; block all other outbound. The 2026 incident driver: Vercel supply-chain attack via compromised CI/CD credentials exfiltrated env vars across thousands of customer deployments.

**Phase:** [[Phases/17 Infrastructure & Production|Phase 17: Infrastructure & Production]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/17-infrastructure-and-production/25-security-secrets-audit/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/25-security-secrets-audit) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/17-infrastructure-and-production/25-security-secrets-audit) · code: main.py · quiz: 6 questions  
**Community:** [[Communities/30 Evaluation (Eval) · Kill switch · Non-determinism|30 Evaluation (Eval) · Kill switch · Non-determinism]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 17 · 19 (AI Gateways), Phase 17 · 13 (Observability)`

- [[Lessons/17-13 LLM Observability Stack Selection|17/13 LLM Observability Stack Selection]] — Observability
- [[Lessons/17-19 AI Gateways — LiteLLM, Portkey, Kong AI Gateway, Bifrost|17/19 AI Gateways — LiteLLM, Portkey, Kong AI Gateway, Bifrost]] — AI Gateways

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/17-01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI|17/01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI]], [[Lessons/17-08 Inference Metrics — TTFT, TPOT, ITL, Goodput, P99|17/08 Inference Metrics — TTFT, TPOT, ITL, Goodput, P99]], [[Lessons/17-16 Model Routing as a Cost-Reduction Primitive|17/16 Model Routing as a Cost-Reduction Primitive]]
- depth 3: [[Lessons/17-04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill|17/04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill]]

## Builds on this

- [[Lessons/17-26 Compliance — SOC 2, HIPAA, GDPR, PCI-DSS, EU AI Act, ISO 42001|17/26 Compliance — SOC 2, HIPAA, GDPR, PCI-DSS, EU AI Act, ISO 42001]]

## Concepts taught

- Vault `lesson term` — Centralized credential management service
- IAM role `lesson term` — Role assumed by app; returns short-lived creds
- OIDC for CI/CD `lesson term` — No static keys in CI — identity via OIDC
- TruffleHog / GitGuardian / Gitleaks `lesson term` — Commit-time secret detection
- RBAC / ABAC `lesson term` — Role-based vs attribute-based
- PII scrubbing `lesson term` — Remove or tokenize sensitive entities
- Consistent tokenization `lesson term` — Same value → same token each time
- Mesh approach `lesson term` — Semantic-preserving tokenization pattern
- Egress whitelist `lesson term` — Only permitted domains reachable
- [[Concepts/Audit Log|Audit Log]] `glossary` — Append-only record for compliance
- [[Concepts/Zero Trust|Zero Trust]] `glossary` — A security model that grants no implicit trust from network location or asset ownership and instead evaluates each access request against identity, device, resource, policy, and current context.

## Ships

- [[Artifacts/17-25 llm-security-plan|llm-security-plan]] `skill` — Produce an LLM security plan covering secrets vault, PII scrubbing with consistent tokenization, network egress allowlist, audit log retention, and zero-trust posture.

## Further reading

- Datadog — LLM Guardrails Best Practices ([link](https://www.datadoghq.com/blog/llm-guardrails-best-practices/))
- HashiCorp Vault docs ([link](https://developer.hashicorp.com/vault/docs))
- Doppler — Advanced LLM Security ([link](https://www.doppler.com/blog/advanced-llm-security))
- Microsoft Presidio ([link](https://github.com/microsoft/presidio)) — PII detection and anonymization.
- JumpServer — Secrets Management Best Practices 2026 ([link](https://www.jumpserver.com/blog/secret-management-best-practices-2026))
- Portkey — Manage LLM API keys with secret references ([link](https://portkey.ai/blog/secret-references-ai-api-key-management/))

## In learning paths

- [[Paths/Software Engineering Fundamentals|Software Engineering Fundamentals]] — step 12, required


%% ── my notes ── %%
