---
id: "concept:tool-poisoning"
type: concept
name: Tool poisoning
canonical: false
taught_in: 2
community: 3
tags:
  - concept/lesson-term
  - community/03
source: ai-engineering-from-scratch/phases/11-llm-engineering/09-function-calling/docs/en.md
---

# Tool poisoning

**Community:** [[Communities/03 Parallel tool calls · Strict mode · Refusal|03 Parallel tool calls · Strict mode · Refusal]]

> *What people say:* "Prompt injection via tools"

**What it actually means:** An attack where tool results contain instructions that manipulate the model's behavior -- sanitize all tool outputs

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/11-09 Function Calling & Tool Use|11/09 Function Calling & Tool Use]]
- [[Lessons/13-05 Tool Schema Design — Naming, Descriptions, Parameter Constraints|13/05 Tool Schema Design — Naming, Descriptions, Parameter Constraints]] — Hidden instructions in a tool description that hijack the agent


%% ── my notes ── %%
