---
id: "concept:streaming"
type: concept
name: Streaming
canonical: true
category: "Models & inference"
taught_in: 4
community: 21
tags:
  - concept/glossary
  - category/models-and-inference
  - community/21
source: ai-engineering-from-scratch/glossary/terms.md
---

# Streaming

**Community:** [[Communities/21 Time to First Token (TTFT) · Time per Output Token (TPOT) · Prefill|21 Time to First Token (TTFT) · Time per Output Token (TPOT) · Prefill]]

> *What people say:* Showing output as it is generated.

**What it actually means:** Delivering incremental response events before the complete result is ready. A stream may contain token text, structured deltas, tool-call arguments, usage metadata, or status events depending on the API.

**Why it matters:** It improves perceived responsiveness, but it does not reduce the model's actual time to produce a complete answer.

**Common confusion:** Network transport, event shape, and chunk boundaries are provider-specific and are not guaranteed to align with words or tokens.

**Category:** [[Categories/Models & inference|Models & inference]]

## Related concepts

- [[Concepts/Autoregressive|Autoregressive]]
- [[Concepts/Inference|Inference]]
- [[Concepts/Observability|Observability]]
- [[Concepts/Time per Output Token (TPOT)|Time per Output Token (TPOT)]]
- [[Concepts/Time to First Token (TTFT)|Time to First Token (TTFT)]]
- [[Concepts/Tokens per Second (TPS)|Tokens per Second (TPS)]]

## Taught in

- [[Lessons/00-04 APIs & Keys|00/04 APIs & Keys]] — Getting the response word by word instead of waiting for the full response
- [[Lessons/00-09 Data Management|00/09 Data Management]] — Processing data row by row from a remote source without downloading the full dataset
- [[Lessons/11-13 Building a Production LLM Application|11/13 Building a Production LLM Application]]
- [[Lessons/14-29 Production Runtimes- Queue, Event, Cron|14/29 Production Runtimes: Queue, Event, Cron]] — Progressive output; better UX; latency observable per chunk


%% ── my notes ── %%
