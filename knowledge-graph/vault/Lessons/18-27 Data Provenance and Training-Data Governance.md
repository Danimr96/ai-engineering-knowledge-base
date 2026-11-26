---
id: "lesson:18/27"
type: lesson
ref: 18/27
phase: 18
num: 27
title: Data Provenance and Training-Data Governance
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 6
code_files: 1
concepts: 7
prereqs: 2
community: 87
aliases:
  - 18/27
  - 18-27
tags:
  - phase/18
  - type/learn
  - community/87
  - stdlib-only
source: ai-engineering-from-scratch/phases/18-ethics-safety-alignment/27-data-provenance-training-governance/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/27-data-provenance-training-governance"
---

# 18/27 Data Provenance and Training-Data Governance

> EU AI Act requires machine-readable opt-out standards for GPAI by August 2025 (via EU Copyright Directive TDM exception). California AB 2013 (signed 2024) — Generative AI training-data transparency requires developers to publish a summary of datasets with 12 mandated fields. 2025 DPA alignment on legitimate interest: Irish DPC (21 May 2025) accepts Meta's LLM training on first-party public EU/EEA adult content with safeguards after EDPB opinion; Cologne Higher Regional Court (23 May 2025) dismisses injunction; Hamburg DPA drops urgency; UK ICO (23 September 2025) issues a positive regulatory response to LinkedIn's AI-training safeguards (transparency, simplified opt-out, extended objection windows) and continues monitoring — not a formal clearance. Brazilian ANPD (2 July 2024) suspended Meta's processing over insufficient information transparency; the preventive measure was lifted on 30 August 2024 after Meta submitted a compliance plan. Key irreversibility problem: cookie-consent frameworks are designed for real-time, reversible tracking; once data is in model weights, surgical erasure is impossible — no practical GDPR right-to-erasure for trained neural networks. Compliance window is at collection time. Data Provenance Initiative (dataprovenance.org, Longpre, Mahari, Lee et al., "Consent in Crisis", July 2024): large-scale audit shows rapid decline of the AI data commons as publishers add robots.txt restrictions.

**Phase:** [[Phases/18 Ethics, Safety & Alignment|Phase 18: Ethics, Safety & Alignment]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/18-ethics-safety-alignment/27-data-provenance-training-governance/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/27-data-provenance-training-governance) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/18-ethics-safety-alignment/27-data-provenance-training-governance) · code: main.py · quiz: 6 questions  
**Community:** [[Communities/87 EU AI Act|87 EU AI Act]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 18 · 24 (regulatory), Phase 18 · 26 (cards)`

- [[Lessons/18-24 Regulatory Frameworks — EU, US, UK, Korea|18/24 Regulatory Frameworks — EU, US, UK, Korea]] — regulatory
- [[Lessons/18-26 Model, System, and Dataset Cards|18/26 Model, System, and Dataset Cards]] — cards

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/18-18 Frontier Safety Frameworks — RSP, PF, FSF|18/18 Frontier Safety Frameworks — RSP, PF, FSF]]
- depth 3: [[Lessons/18-07 Sleeper Agents — Persistent Deception|18/07 Sleeper Agents — Persistent Deception]], [[Lessons/18-08 In-Context Scheming in Frontier Models|18/08 In-Context Scheming in Frontier Models]], [[Lessons/18-09 Alignment Faking|18/09 Alignment Faking]], [[Lessons/18-17 WMDP and Dual-Use Capability Evaluation|18/17 WMDP and Dual-Use Capability Evaluation]]

## Builds on this

- [[Lessons/18-24 Regulatory Frameworks — EU, US, UK, Korea|18/24 Regulatory Frameworks — EU, US, UK, Korea]]
- [[Lessons/18-28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR|18/28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR]]

## Concepts taught

- AB 2013 `lesson term` — Generative AI training-data transparency; 12 mandated fields
- TDM exception `lesson term` — EU Copyright Directive training-data exception with opt-out
- Legitimate interest `lesson term` — GDPR Article 6 basis that may justify training on public content
- Opt-out signal `lesson term` — robots.txt, C2PA "No AI Training," TDM.Reservation
- Irreversibility `lesson term` — Data in model weights is not surgically removable
- Unlearning `lesson term` — Post-training interventions to reduce model dependence on specific data
- Consent in Crisis `lesson term` — July 2024 finding of accelerating robots.txt restrictions

## Ships

- [[Artifacts/18-27 provenance-check|provenance-check]] `skill` — Check a training dataset against California AB 2013 and EU TDM opt-out obligations.

## Further reading

- Longpre, Mahari, Lee et al. — Consent in Crisis (dataprovenance.org, July 2024) ([link](https://www.dataprovenance.org/consent-in-crisis-paper)) — DPI audit
- [[Resources/EU AI Act text (Regulation 2024-1689)|EU AI Act text (Regulation 2024/1689)]] ([link](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)) — Copyright chapter ·  also cited by 1 other lesson
- IAPP — EU Digital Omnibus GDPR amendments (2025) ([link](https://iapp.org/news/a/eu-digital-omnibus-amendments-to-gdpr-to-facilitate-ai-training-miss-the-mark)) — regulatory context
- California AB 2013 ([link](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240AB2013)) — Generative AI training-data transparency law


%% ── my notes ── %%
