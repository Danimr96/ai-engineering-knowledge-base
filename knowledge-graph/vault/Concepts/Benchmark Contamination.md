---
id: "concept:benchmark-contamination"
type: concept
name: Benchmark Contamination
canonical: true
category: "Evaluation & safety"
taught_in: 4
community: 24
tags:
  - concept/glossary
  - category/evaluation-and-safety
  - community/24
source: ai-engineering-from-scratch/glossary/terms.md
---

# Benchmark Contamination

**Community:** [[Communities/24 Eval Set · Regression Test · Test Oracle|24 Eval Set · Regression Test · Test Oracle]]

**What it actually means:** Overlap or information leakage between evaluation examples and data used to pretrain, tune, prompt, select, or otherwise improve the evaluated system.

**Why it matters:** Contamination can make a benchmark score reflect prior exposure rather than the ability to generalize to unseen tasks.

**In practice:** Track dataset provenance, search training sources for exact and near duplicates, hold back private test cases, and refresh public evals with newly authored examples.

**Common confusion:** Contamination is broader than exact copying. Paraphrases, answer keys, benchmark metadata, and repeated prompt tuning can also leak evaluation information.

**Category:** [[Categories/Evaluation & safety|Evaluation & safety]]

## Related concepts

- [[Concepts/Data Deduplication|Data Deduplication]]
- [[Concepts/Data Leakage|Data Leakage]]
- [[Concepts/Eval Set|Eval Set]]
- [[Concepts/Exact Match (EM)|Exact Match (EM)]]

## Taught in

- [[Lessons/02-16 Anomaly Detection|02/16 Anomaly Detection]] `alias` — A hyperparameter telling the detector what proportion of the data it should flag as anomalous
- [[Lessons/10-10 Evaluation- Benchmarks, Evals, LM Harness|10/10 Evaluation: Benchmarks, Evals, LM Harness]] `alias` — Training data includes benchmark questions, inflating scores without improving real capability
- [[Lessons/14-19 Benchmarks- SWE-bench, GAIA, AgentBench|14/19 Benchmarks: SWE-bench, GAIA, AgentBench]] `alias` — Benchmark tasks present in model training
- [[Lessons/16-24 Evaluation and Coordination Benchmarks|16/24 Evaluation and Coordination Benchmarks]] `alias` — Post-release, benchmarks drift into training corpora; scores inflate.

## Sources

- Investigating Data Contamination in Modern Benchmarks for Large Language Models ([link](https://arxiv.org/abs/2311.09783))


%% ── my notes ── %%
