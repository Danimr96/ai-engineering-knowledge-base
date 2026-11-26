---
id: "lesson:11/02"
type: lesson
ref: 11/02
phase: 11
num: 2
title: "Few-Shot, Chain-of-Thought, Tree-of-Thought"
lesson_type: build
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 1
community: 42
libraries:
  - openai
aliases:
  - 11/02
  - 11-02
tags:
  - phase/11
  - type/build
  - community/42
source: ai-engineering-from-scratch/phases/11-llm-engineering/02-few-shot-cot/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/11-llm-engineering/02-few-shot-cot"
---

# 11/02 Few-Shot, Chain-of-Thought, Tree-of-Thought

> Telling a model what to do is prompting. Showing it how to think is engineering. The gap between 78% and 91% accuracy on the same model, same task, same data is not a better model. It is a better reasoning strategy.

**Phase:** [[Phases/11 LLM Engineering|Phase 11: LLM Engineering]] · **Type:** Build · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/11-llm-engineering/02-few-shot-cot/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/11-llm-engineering/02-few-shot-cot) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/11-llm-engineering/02-few-shot-cot) · code: advanced_prompting.py  
**Community:** [[Communities/42 Few-Shot · Prompt Engineering · In-Context Learning|42 Few-Shot · Prompt Engineering · In-Context Learning]] · **Libraries:** [[Libraries/openai (python)|openai]]  

## Prerequisites

Stated upstream: `Lesson 11.01 (Prompt Engineering)`

- [[Lessons/11-01 Prompt Engineering- Techniques & Patterns|11/01 Prompt Engineering: Techniques & Patterns]] — Prompt Engineering

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]], [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]], [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]], [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]], [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]]
- depth 3: [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/19-76 Collective Ops From Scratch|19/76 Collective Ops From Scratch]]

## Builds on this

- [[Lessons/11-05 Context Engineering- Windows, Budgets, Memory, and Retrieval|11/05 Context Engineering: Windows, Budgets, Memory, and Retrieval]]
- [[Lessons/11-06 RAG (Retrieval-Augmented Generation)|11/06 RAG (Retrieval-Augmented Generation)]]
- [[Lessons/11-13 Building a Production LLM Application|11/13 Building a Production LLM Application]]

## Concepts taught

- [[Concepts/Few-Shot|Few-Shot]] (as *Few-shot prompting*) `glossary` — Including input-output demonstrations in the prompt to anchor the model's output format and behavior
- [[Concepts/Chain of Thought (CoT)|Chain of Thought (CoT)]] (as *Chain-of-Thought*) `glossary` — Eliciting intermediate reasoning tokens that extend the model's effective computation before producing a final answer
- [[Concepts/Self-Consistency|Self-Consistency]] `lesson term` — Sampling N diverse reasoning paths at temperature > 0 and selecting the most common final answer by majority vote
- [[Concepts/Tree of thought|Tree of thought]] (as *Tree-of-Thought*) `lesson term` — Structured search over reasoning branches where each partial solution is evaluated and only promising paths are expanded
- [[Concepts/ReAct|ReAct]] `glossary` — Interleaving reasoning traces with external actions (search, compute, API calls) in a Thought-Action-Observation loop
- [[Concepts/Prompt chaining|Prompt chaining]] `lesson term` — Decomposing a complex task into sequential prompts where each output feeds the next input
- Zero-shot CoT `lesson term` — Appending a reasoning trigger phrase to a prompt without any examples, relying on the model's latent reasoning capability

## Ships

- [[Artifacts/11-02 prompt-reasoning-chain|prompt-reasoning-chain]] `prompt` — Production-ready few-shot CoT prompt with self-consistency support for multi-step reasoning tasks
- [[Artifacts/11-02 skill-cot-patterns|skill-cot-patterns]] `skill` — Decision framework for choosing the right reasoning technique based on task complexity, accuracy requirements, and cost constraints

## Further reading

- [[Resources/Wei et al., 2022 - -Chain-of-Thought Prompting Elicits Reasoning in Large Language Models|Wei et al., 2022 -- "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models]] ([link](https://arxiv.org/abs/2201.11903)) — Wei et al. 2022. The original CoT paper from Google Brain. Read sections 2-3 for the core results. ·  also cited by 1 other lesson
- [[Resources/Self-Consistency Improves Chain of Thought Reasoning in Language Models|Self-Consistency Improves Chain of Thought Reasoning in Language Models]] ([link](https://arxiv.org/abs/2203.11171)) — Wang et al. 2023. The self-consistency paper. Table 1 has all the numbers you need. ·  also cited by 1 other lesson
- Large Language Models are Zero-Shot Reasoners ([link](https://arxiv.org/abs/2205.11916)) — Kojima et al. 2022. The "Let's think step by step" paper. Surprisingly effective for how simple it is.
- [[Resources/ReAct|ReAct]] ([link](https://arxiv.org/abs/2210.03629)) — Yao et al. 2022. The foundation of modern AI agents. Section 3 explains the Thought-Action-Observation loop. ·  also cited by 5 other lessons
- [[Resources/Yao et al. — Tree of Thoughts- Deliberate Problem Solving with Large Language Models (arXiv-2305.10601)|Yao et al. — Tree of Thoughts: Deliberate Problem Solving with Large Language Models (arXiv:2305.10601)]] ([link](https://arxiv.org/abs/2305.10601)) — Yao et al. 2023. ToT paper. The Game of 24 results in section 4 are the highlight. ·  also cited by 2 other lessons
- [[Resources/Lightman et al., 2023 - -Let's Verify Step by Step|Lightman et al., 2023 -- "Let's Verify Step by Step]] ([link](https://arxiv.org/abs/2305.20050)) — process reward models (PRM) that grade each step of a chain; the reasoning supervision signal that succeeds outcome-only rewards. ·  also cited by 2 other lessons
- [[Resources/DSPy- Compiling Declarative Language Model Calls into Self-Improving Pipelines|DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines]] ([link](https://arxiv.org/abs/2310.03714)) — Khattab et al. 2023. Treats prompting as a compilation problem. Read if you want to move beyond manual prompt engineering. ·  also cited by 1 other lesson
- Snell et al., "Scaling LLM Test-Time Compute Optimally" (2024) ([link](https://arxiv.org/abs/2408.03314)) — systematic study of CoT length, self-consistency sampling, and MCTS; where "think step by step" goes when accuracy matters more than latency.
- OpenAI — Reasoning models guide ([link](https://platform.openai.com/docs/guides/reasoning)) — vendor guidance on when chain-of-thought becomes an internal, priced-per-token "reasoning" mode versus a prompt-level trick.


%% ── my notes ── %%
