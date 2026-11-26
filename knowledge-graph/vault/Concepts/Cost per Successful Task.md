---
id: "concept:cost-per-successful-task"
type: concept
name: Cost per Successful Task
canonical: true
category: AI-native development
taught_in: 0
community: 16
tags:
  - concept/glossary
  - category/ai-native-development
  - community/16
source: ai-engineering-from-scratch/glossary/terms.md
---

# Cost per Successful Task

**Community:** [[Communities/16 Backpressure · Rate Limit · Admission Control|16 Backpressure · Rate Limit · Admission Control]]

**What it actually means:** Total system cost divided by the number of tasks that satisfy a defined success criterion, including retries, failed runs, tool use, and evaluation overhead.

**Why it matters:** A cheap model call can produce an expensive workflow if it fails often or requires repeated human correction.

**In practice:** Measure provider charges and infrastructure cost across 100 repository tasks, then divide by the number whose patches pass tests and review.

**Common confusion:** Cost per token measures usage. Cost per successful task measures useful outcomes.

**Category:** [[Categories/AI-native development|AI-native development]]

## Related concepts

- [[Concepts/Evaluation (Eval)|Evaluation (Eval)]]
- [[Concepts/Goodput|Goodput]]
- [[Concepts/Model Router|Model Router]]
- [[Concepts/Retry with Backoff|Retry with Backoff]]
- [[Concepts/Semantic Cache|Semantic Cache]]
- [[Concepts/Token Budget|Token Budget]]
- [[Concepts/Verification Gate|Verification Gate]]


%% ── my notes ── %%
