---
id: "concept:prompt-cache"
type: concept
name: Prompt Cache
canonical: true
category: "Prompting & context"
taught_in: 5
community: 41
tags:
  - concept/glossary
  - category/prompting-and-context
  - community/41
source: ai-engineering-from-scratch/glossary/terms.md
---

# Prompt Cache

**Community:** [[Communities/41 Prompt Cache · Cache hit rate · Model routing|41 Prompt Cache · Cache hit rate · Model routing]]

**What it actually means:** Reuse of provider-side or application-side computation for an identical or eligible prompt prefix so repeated inference avoids some preprocessing work.

**Why it matters:** Stable instructions and large shared documents can become cheaper or faster across repeated calls when the provider's cache contract is satisfied.

**In practice:** Place stable policy text before request-specific content, monitor cache-hit metadata, and treat misses as normal because eligibility and lifetime vary by provider.

**Common confusion:** A prompt cache is a provider or application reuse contract and may use prefix caching internally. Prefix caching specifically reuses eligible exact-token KV state, while semantic caching reuses a prior result for a sufficiently similar request.

**Category:** [[Categories/Prompting & context|Prompting & context]]

## Related concepts

- [[Concepts/Context Window|Context Window]]
- [[Concepts/KV Cache|KV Cache]]
- [[Concepts/Prefix Caching|Prefix Caching]]
- [[Concepts/Semantic Cache|Semantic Cache]]
- [[Concepts/Time to First Token (TTFT)|Time to First Token (TTFT)]]

## Taught in

- [[Lessons/11-11 Caching, Rate Limiting & Cost Optimization|11/11 Caching, Rate Limiting & Cost Optimization]] `alias` — Provider-level caching where repeated prompt prefixes get a discount (90% Anthropic, 50% OpenAI) -- no code changes for OpenAI, explicit markers for Anthropic
- [[Lessons/11-15 Prompt Caching and Context Caching|11/15 Prompt Caching and Context Caching]] — Reusing a provider-side KV-cache for matching prefixes; 50-90% discount on repeated input tokens.
- [[Lessons/15-13 Action Budgets, Iteration Caps, and Cost Governors|15/13 Action Budgets, Iteration Caps, and Cost Governors]] `alias` — Provider-side cache reduces re-send token cost to near zero
- [[Lessons/19-02 Capstone 02 — RAG over Codebase (Cross-Repo Semantic Search)|19/02 Capstone 02 — RAG over Codebase (Cross-Repo Semantic Search)]] `alias` — 2026 Claude / OpenAI feature that discounts repeat prefix tokens up to 90%
- [[Lessons/19-08 Capstone 08 — Production RAG Chatbot for a Regulated Vertical|19/08 Capstone 08 — Production RAG Chatbot for a Regulated Vertical]] `alias` — Claude/OpenAI feature: cached prefix tokens discounted 60-90% on hit


%% ── my notes ── %%
