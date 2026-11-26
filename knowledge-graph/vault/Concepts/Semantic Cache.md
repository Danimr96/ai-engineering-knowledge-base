---
id: "concept:semantic-cache"
type: concept
name: Semantic Cache
canonical: true
category: AI-native development
taught_in: 1
tags:
  - concept/glossary
  - category/ai-native-development
source: ai-engineering-from-scratch/glossary/terms.md
---

# Semantic Cache

**What it actually means:** A cache that reuses a previous result when a new request is judged sufficiently similar under a chosen representation and threshold.

**Why it matters:** It can reduce latency and cost for repeated intents, but an incorrect match can return stale or user-inappropriate output.

**In practice:** Cache low-risk FAQ answers by normalized intent, include tenant and policy version in the key, and bypass the cache for personalized or time-sensitive requests.

**Common confusion:** Semantic similarity does not guarantee that two requests have the same correct answer. A semantic cache reuses a prior result, while prefix caching reuses exact-token KV state and prompt caching follows provider or application eligibility rules.

**Category:** [[Categories/AI-native development|AI-native development]]

## Related concepts

- [[Concepts/Agent Memory|Agent Memory]]
- [[Concepts/Cost per Successful Task|Cost per Successful Task]]
- [[Concepts/Embedding|Embedding]]
- [[Concepts/Grounding|Grounding]]
- [[Concepts/Prefix Caching|Prefix Caching]]
- [[Concepts/Prompt Cache|Prompt Cache]]

## Taught in

- [[Lessons/11-13 Building a Production LLM Application|11/13 Building a Production LLM Application]] — A cache keyed by embedding similarity rather than exact string match -- two differently-phrased identical questions return the same cached response


%% ── my notes ── %%
