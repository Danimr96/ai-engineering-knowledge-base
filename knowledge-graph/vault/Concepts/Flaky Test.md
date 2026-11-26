---
id: "concept:flaky-test"
type: concept
name: Flaky Test
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

# Flaky Test

**Community:** [[Communities/24 Eval Set · Regression Test · Test Oracle|24 Eval Set · Regression Test · Test Oracle]]

**What it actually means:** A test that can pass and fail across equivalent runs without a relevant change to the code or intended test environment.

**Why it matters:** Flakiness weakens verification gates and can train people or agents to ignore real failures or retry until they obtain a false pass.

**In practice:** Preserve the failing seed and environment, quarantine only with an owner and deadline, then fix uncontrolled time, concurrency, network, order, or shared-state dependencies.

**Common confusion:** A test that consistently exposes an intermittent product bug is valuable evidence, not necessarily a flaky test.

**Category:** [[Categories/AI-native development|AI-native development]]

## Related concepts

- [[Concepts/Regression Test|Regression Test]]
- [[Concepts/Retry with Backoff|Retry with Backoff]]
- [[Concepts/Test Oracle|Test Oracle]]
- [[Concepts/Verification Gate|Verification Gate]]

## Sources

- De-Flake Your Tests ([link](https://conferences.computer.org/icsme/pdfs/ICSME2020-1oOutvkGTwF4GyVvNtr3Mm/561900a736/561900a736.pdf))


%% ── my notes ── %%
