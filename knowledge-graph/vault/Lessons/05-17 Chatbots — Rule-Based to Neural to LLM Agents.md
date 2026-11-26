---
id: "lesson:05/17"
type: lesson
ref: 05/17
phase: 5
num: 17
title: "Chatbots — Rule-Based to Neural to LLM Agents"
lesson_type: learn
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 8
code_files: 1
concepts: 6
prereqs: 2
community: 74
aliases:
  - 05/17
  - 05-17
tags:
  - phase/05
  - type/learn
  - community/74
  - stdlib-only
source: ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/17-chatbots-rule-to-neural/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/17-chatbots-rule-to-neural"
---

# 05/17 Chatbots — Rule-Based to Neural to LLM Agents

> ELIZA replied with pattern matches. DialogFlow mapped intents. GPT answered from weights. Claude runs tools and verifies. Each era solved the previous one's worst failure.

**Phase:** [[Phases/05 NLP, Foundations to Advanced|Phase 5: NLP, Foundations to Advanced]] · **Type:** Learn · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/05-nlp-foundations-to-advanced/17-chatbots-rule-to-neural/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/17-chatbots-rule-to-neural) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/17-chatbots-rule-to-neural) · code: main.py · quiz: 8 questions  
**Community:** [[Communities/74 Slot · JSON mode|74 Slot · JSON mode]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 5 · 13 (Question Answering), Phase 5 · 14 (Information Retrieval)`

- [[Lessons/05-13 Question Answering Systems|05/13 Question Answering Systems]] — Question Answering
- [[Lessons/05-14 Information Retrieval and Search|05/14 Information Retrieval and Search]] — Information Retrieval

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/05-02 Bag of Words, TF-IDF, and Text Representation|05/02 Bag of Words, TF-IDF, and Text Representation]], [[Lessons/05-04 GloVe, FastText, and Subword Embeddings|05/04 GloVe, FastText, and Subword Embeddings]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]], [[Lessons/05-11 Machine Translation|05/11 Machine Translation]]
- depth 3: [[Lessons/02-02 Linear Regression|02/02 Linear Regression]], [[Lessons/05-01 Text Processing — Tokenization, Stemming, Lemmatization|05/01 Text Processing — Tokenization, Stemming, Lemmatization]], [[Lessons/05-03 Word Embeddings — Word2Vec from Scratch|05/03 Word Embeddings — Word2Vec from Scratch]], [[Lessons/05-09 Sequence-to-Sequence Models|05/09 Sequence-to-Sequence Models]]

## Builds on this

- [[Lessons/05-20 Structured Outputs & Constrained Decoding|05/20 Structured Outputs & Constrained Decoding]]
- [[Lessons/05-29 Dialogue State Tracking|05/29 Dialogue State Tracking]]

## Concepts taught

- Intent `lesson term` — Categorical label (book_flight, reset_password). Routed to a handler.
- [[Concepts/Slot|Slot]] `lesson term` — Parameter the bot needs (date, destination). Slot filling is the sequence of asks.
- [[Concepts/RAG (Retrieval-Augmented Generation)|RAG (Retrieval-Augmented Generation)]] (as *RAG*) `glossary` — Retrieve relevant docs, then ground the LLM's response.
- [[Concepts/Tool call|Tool call]] `lesson term` — LLM emits a structured call with name + args. Runtime executes, returns result.
- [[Concepts/Agent loop|Agent loop]] `lesson term` — Controller that runs LLM calls interleaved with tool calls until task complete.
- [[Concepts/Prompt Injection|Prompt Injection]] `glossary` — Malicious input that tries to override the system prompt.

## Ships

- [[Artifacts/05-17 chatbot-architect|chatbot-architect]] `skill` — Design a chatbot stack for a given use case.

## Further reading

- Turing (1950). Computing Machinery and Intelligence ([link](https://academic.oup.com/mind/article/LIX/236/433/986238)) — the paper that made conversation the field's benchmark.
- [[Resources/Building Effective Agents|Building Effective Agents]] ([link](https://www.anthropic.com/research/building-effective-agents)) — 2024 production guidance that still holds in 2026. ·  also cited by 16 other lessons
- Thoppilan et al. (2022). LaMDA: Language Models for Dialog Applications ([link](https://arxiv.org/abs/2201.08239)) — Google's late neural-chatbot paper, just before LLM agents took over.
- [[Resources/ReAct|ReAct]] ([link](https://arxiv.org/abs/2210.03629)) — the paper that named the agent loop pattern. ·  also cited by 5 other lessons
- [[Resources/Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection|Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection]] ([link](https://arxiv.org/abs/2302.12173)) — the prompt-injection paper. ·  also cited by 4 other lessons
- AWS — Securing Amazon Bedrock Agents against Indirect Prompt Injections ([link](https://aws.amazon.com/blogs/machine-learning/securing-amazon-bedrock-agents-a-guide-to-safeguarding-against-indirect-prompt-injections/)) — practical orchestration-layer defenses including Plan-Verify-Execute and user-confirmation flows.
- Colby, Weber, Hilf (1971). Artificial Paranoia ([link](https://doi.org/10.1016/0004-3702(71)) — 90002-6) — PARRY's affect-variable architecture, the first stateful chatbot.
- OWASP prompt injection guidance ([link](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)) — the ranking that made prompt injection the top security concern.
- EchoLeak (CVE-2025-32711) ([link](https://www.vectra.ai/topics/prompt-injection)) — the canonical zero-click data-exfiltration CVE from indirect prompt injection. Reference case for why write-access agents need runtime defenses.
- Weizenbaum (1966). ELIZA — A Computer Program For the Study of Natural Language Communication ([link](https://web.stanford.edu/class/cs124/p36-weizenabaum.pdf)) — the original rule-based chatbot paper.


%% ── my notes ── %%
