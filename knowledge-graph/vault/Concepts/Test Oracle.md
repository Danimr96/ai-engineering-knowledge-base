---
id: "concept:test-oracle"
type: concept
name: Test Oracle
canonical: true
category: AI-native development
taught_in: 0
community: 24
tags:
  - concept/glossary
  - category/ai-native-development
  - community/24
source: ai-engineering-from-scratch/glossary/terms.md
---

# Test Oracle

**Community:** [[Communities/24 Eval Set · Regression Test · Test Oracle|24 Eval Set · Regression Test · Test Oracle]]

**What it actually means:** The mechanism, specification, reference, invariant, or human judgment used to decide whether observed program behavior is correct.

**Why it matters:** Generating test inputs is not enough; automated verification requires an independent basis for classifying each result.

**In practice:** Prefer executable invariants, reference implementations, schemas, and deterministic expected outputs, then document where human judgment remains necessary.

**Common confusion:** The model that wrote the code should not be treated as an independent oracle merely because you ask it whether its own output is correct.

**Category:** [[Categories/AI-native development|AI-native development]]

## Related concepts

- [[Concepts/Eval Set|Eval Set]]
- [[Concepts/Flaky Test|Flaky Test]]
- [[Concepts/Human-in-the-Loop (HITL)|Human-in-the-Loop (HITL)]]
- [[Concepts/Pass@k|Pass@k]]
- [[Concepts/Regression Test|Regression Test]]
- [[Concepts/Verification Gate|Verification Gate]]

## Sources

- The Oracle Problem in Software Testing ([link](https://www.computer.org/csdl/journal/ts/2015/05/06963470/13rRUx0geBw))


%% ── my notes ── %%
