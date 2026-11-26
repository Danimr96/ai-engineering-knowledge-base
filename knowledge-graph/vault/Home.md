---
type: home
tags:
  - home
built: "2026-09-25T18:28:59+00:00"
upstream_commit: f6721a01
---

# AI Engineering from Scratch — knowledge graph

Generated from `build/graph.json`. Rebuild with `uv run python -m kg.cli all`. Everything above the *my notes* marker in a generated note is overwritten; everything below it, and everything in `My Notes/`, is yours.

## Tables

- [[Bases/Lessons.base|All lessons]] · [[Bases/My Route.base|My route]] · [[Bases/Concepts.base|Concepts]] · [[Bases/Resources.base|Resources]] · [[Bases/Artifacts.base|Artifacts]] · [[Bases/Libraries.base|Libraries]] · [[Bases/Communities.base|Communities]]

## My route

| Step | Lesson | Status | Bridges |
|---|---|---|---|
| 1 | [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]] | done |  |
| 2 | [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]] | planned |  |
| 3 | [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]] | planned |  |
| 4 | [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]] | planned | [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05]], [[Lessons/01-09 Information Theory|01/09]], [[Lessons/03-03 Backpropagation from Scratch|03/03]], [[Lessons/03-06 Optimizers|03/06]], [[Lessons/07-02 Self-Attention from Scratch|07/02]], [[Lessons/07-03 Multi-Head Attention|07/03]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05]] |
| 5 | [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]] | planned | [[Lessons/19-76 Collective Ops From Scratch|19/76]] |
| 6 | [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]] | planned |  |
| 7 | [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]] | planned | [[Lessons/09-01 MDPs, States, Actions & Rewards|09/01]], [[Lessons/09-06 Policy Gradient — REINFORCE from Scratch|09/06]], [[Lessons/09-08 Proximal Policy Optimization (PPO)|09/08]] |
| 8 | [[Lessons/10-08 DPO- Direct Preference Optimization|10/08 DPO: Direct Preference Optimization]] | planned | [[Lessons/01-06 Probability and Distributions|01/06]] |
| 9 | [[Lessons/10-09 Constitutional AI and Self-Improvement|10/09 Constitutional AI and Self-Improvement]] | planned |  |
| 10 | [[Lessons/10-10 Evaluation- Benchmarks, Evals, LM Harness|10/10 Evaluation: Benchmarks, Evals, LM Harness]] | planned |  |
| 11 | [[Lessons/10-11 Quantization- Making Models Fit|10/11 Quantization: Making Models Fit]] | planned | [[Lessons/01-13 Numerical Stability|01/13]] |
| 12 | [[Lessons/10-12 Inference Optimization|10/12 Inference Optimization]] | planned | [[Lessons/07-12 KV Cache, Flash Attention & Inference Optimization|07/12]] |
| 13 | [[Lessons/10-13 Building a Complete LLM Pipeline|10/13 Building a Complete LLM Pipeline]] | planned |  |
| 14 | [[Lessons/10-14 Open Models- Architecture Walkthroughs|10/14 Open Models: Architecture Walkthroughs]] | planned | [[Lessons/07-11 Mixture of Experts (MoE)|07/11]] |
| 15 | [[Lessons/10-25 Speculative Decoding and EAGLE|10/25 Speculative Decoding and EAGLE]] | planned | [[Lessons/07-16 Speculative Decoding — Draft, Verify, Repeat|07/16]] |
| 16 | [[Lessons/10-15 Speculative Decoding and EAGLE-3|10/15 Speculative Decoding and EAGLE-3]] | planned |  |
| 17 | [[Lessons/10-16 Differential Attention (V2)|10/16 Differential Attention (V2)]] | planned | [[Lessons/07-15 Attention Variants — Sliding Window, Sparse, Differential|07/15]] |
| 18 | [[Lessons/10-17 Native Sparse Attention (DeepSeek NSA)|10/17 Native Sparse Attention (DeepSeek NSA)]] | planned |  |
| 19 | [[Lessons/10-18 Multi-Token Prediction (MTP)|10/18 Multi-Token Prediction (MTP)]] | planned |  |
| 20 | [[Lessons/10-19 DualPipe Parallelism|10/19 DualPipe Parallelism]] | planned |  |
| 21 | [[Lessons/10-20 DeepSeek-V3 Architecture Walkthrough|10/20 DeepSeek-V3 Architecture Walkthrough]] | planned |  |
| 22 | [[Lessons/10-21 Jamba — Hybrid SSM-Transformer|10/21 Jamba — Hybrid SSM-Transformer]] | planned |  |
| 23 | [[Lessons/10-22 Async and Hogwild! Inference|10/22 Async and Hogwild! Inference]] | planned |  |
| 24 | [[Lessons/10-34 Gradient Checkpointing and Activation Recomputation|10/34 Gradient Checkpointing and Activation Recomputation]] | planned |  |

## Phases

| # | Phase | Lessons | Done | Hours | Requires |
|---|---|---|---|---|---|
| 0 | [[Phases/00 Setup & Tooling|Setup & Tooling]] | 12 | 0 | 14.0 |  |
| 1 | [[Phases/01 Math Foundations|Math Foundations]] | 22 | 0 | 23.0 | [[Phases/00 Setup & Tooling|P0]] |
| 2 | [[Phases/02 ML Fundamentals|ML Fundamentals]] | 18 | 0 | 21.0 | [[Phases/01 Math Foundations|P1]] |
| 3 | [[Phases/03 Deep Learning Core|Deep Learning Core]] | 13 | 0 | 15.0 | [[Phases/02 ML Fundamentals|P2]] |
| 4 | [[Phases/04 Computer Vision|Computer Vision]] | 28 | 0 | 27.0 | [[Phases/03 Deep Learning Core|P3]] |
| 5 | [[Phases/05 NLP, Foundations to Advanced|NLP, Foundations to Advanced]] | 29 | 0 | 30.0 | [[Phases/03 Deep Learning Core|P3]] |
| 6 | [[Phases/06 Speech & Audio|Speech & Audio]] | 17 | 0 | 18.0 | [[Phases/03 Deep Learning Core|P3]] |
| 7 | [[Phases/07 Transformers Deep Dive|Transformers Deep Dive]] | 16 | 0 | 14.0 | [[Phases/05 NLP, Foundations to Advanced|P5]] |
| 8 | [[Phases/08 Generative AI|Generative AI]] | 15 | 0 | 14.0 | [[Phases/07 Transformers Deep Dive|P7]] |
| 9 | [[Phases/09 Reinforcement Learning|Reinforcement Learning]] | 12 | 0 | 13.0 | [[Phases/03 Deep Learning Core|P3]] |
| 10 | [[Phases/10 LLMs from Scratch|LLMs from Scratch]] | 24 | 1 | 26.0 | [[Phases/07 Transformers Deep Dive|P7]] |
| 11 | [[Phases/11 LLM Engineering|LLM Engineering]] | 17 | 0 | 19.0 | [[Phases/10 LLMs from Scratch|P10]] |
| 12 | [[Phases/12 Multimodal AI|Multimodal AI]] | 25 | 0 | 65.0 | [[Phases/10 LLMs from Scratch|P10]] |
| 13 | [[Phases/13 Tools & Protocols|Tools & Protocols]] | 31 | 0 | 43.0 | [[Phases/11 LLM Engineering|P11]] |
| 14 | [[Phases/14 Agent Engineering|Agent Engineering]] | 54 | 0 | 55.0 | [[Phases/13 Tools & Protocols|P13]] |
| 15 | [[Phases/15 Autonomous Systems|Autonomous Systems]] | 22 | 0 | 20.0 | [[Phases/14 Agent Engineering|P14]] |
| 16 | [[Phases/16 Multi-Agent & Swarms|Multi-Agent & Swarms]] | 25 | 0 | 28.0 | [[Phases/15 Autonomous Systems|P15]] |
| 17 | [[Phases/17 Infrastructure & Production|Infrastructure & Production]] | 28 | 0 | 32.0 | [[Phases/14 Agent Engineering|P14]] |
| 18 | [[Phases/18 Ethics, Safety & Alignment|Ethics, Safety & Alignment]] | 30 | 0 | 31.0 | [[Phases/15 Autonomous Systems|P15]] |
| 19 | [[Phases/19 Capstone Projects|Capstone Projects]] | 85 | 0 | 620.0 | [[Phases/16 Multi-Agent & Swarms|P16]], [[Phases/17 Infrastructure & Production|P17]], [[Phases/18 Ethics, Safety & Alignment|P18]] |

## Communities (what the data clusters, across phases)

| # | Cluster | Lessons | Concepts | Phases |
|---|---|---|---|---|
| 1 | [[Communities/01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism|Expert Parallelism · Pipeline Parallelism · Tensor Parallelism]] | 22 | 35 | 5, 7, 10, 11, 17 |
| 2 | [[Communities/02 Bucket · Causal mask · Manifest|Bucket · Causal mask · Manifest]] | 38 | 10 | 19 |
| 3 | [[Communities/03 Parallel tool calls · Strict mode · Refusal|Parallel tool calls · Strict mode · Refusal]] | 40 | 8 | 11, 13, 15, 19 |
| 4 | [[Communities/04 Overfitting · Underfitting · Data Leakage|Overfitting · Underfitting · Data Leakage]] | 16 | 28 | 2 |
| 5 | [[Communities/05 Temperature · Autoregressive · Logits|Temperature · Autoregressive · Logits]] | 12 | 27 | 1, 7, 8 |
| 6 | [[Communities/06 Communicative dehallucination · Consensus · Contract Net|Communicative dehallucination · Consensus · Contract Net]] | 23 | 15 | 16 |
| 7 | [[Communities/07 Swarm · Evaluator-Optimizer · Debate|Swarm · Evaluator-Optimizer · Debate]] | 19 | 10 | 14 |
| 8 | [[Communities/08 Backpropagation · Gradient · Activation Function|Backpropagation · Gradient · Activation Function]] | 12 | 16 | 1 |
| 9 | [[Communities/09 VAD · Barge-in · Full duplex|VAD · Barge-in · Full duplex]] | 11 | 15 | 6, 19 |
| 10 | [[Communities/10 Trace · Shadow Traffic · requestState|Trace · Shadow Traffic · requestState]] | 14 | 11 | 13, 19 |
| 11 | [[Communities/11 Learning Rate · Optimizer · Batch Size|Learning Rate · Optimizer · Batch Size]] | 4 | 20 | 1, 2, 3 |
| 12 | [[Communities/12 Attention · Cross-Attention · Self-Attention|Attention · Cross-Attention · Self-Attention]] | 12 | 12 | 4, 5, 7 |
| 13 | [[Communities/13 Object Multiplex · Clip · Divided attention|Object Multiplex · Clip · Divided attention]] | 14 | 8 | 4 |
| 14 | [[Communities/14 Least Privilege · Prompt Injection · Sandbox|Least Privilege · Prompt Injection · Sandbox]] | 4 | 16 | 11, 13, 14, 19 |
| 15 | [[Communities/15 System of record · Block severity · Definition of done|System of record · Block severity · Definition of done]] | 14 | 4 | 14 |
| 16 | [[Communities/16 Backpressure · Rate Limit · Admission Control|Backpressure · Rate Limit · Admission Control]] | 0 | 17 |  |
| 17 | [[Communities/17 Tool Contract · Agent · Function Calling|Tool Contract · Agent · Function Calling]] | 3 | 13 | 11, 14 |
| 18 | [[Communities/18 Embedding · Cosine Similarity · HNSW|Embedding · Cosine Similarity · HNSW]] | 2 | 12 | 1, 11 |
| 19 | [[Communities/19 CIMD · DCR · Resource indicator|CIMD · DCR · Resource indicator]] | 6 | 8 | 13 |
| 20 | [[Communities/20 Acceptance rate · Draft model · EAGLE-3|Acceptance rate · Draft model · EAGLE-3]] | 5 | 8 | 7, 10, 19 |
| 21 | [[Communities/21 Time to First Token (TTFT) · Time per Output Token (TPOT) · Prefill|Time to First Token (TTFT) · Time per Output Token (TPOT) · Prefill]] | 2 | 11 | 17 |
| 22 | [[Communities/22 Backward pass · Forward pass · Vanishing gradient|Backward pass · Forward pass · Vanishing gradient]] | 7 | 5 | 3 |
| 23 | [[Communities/23 Automatic Speech Recognition (ASR) · Llama Guard · Homoglyph|Automatic Speech Recognition (ASR) · Llama Guard · Homoglyph]] | 6 | 5 | 15, 18 |
| 24 | [[Communities/24 Eval Set · Regression Test · Test Oracle|Eval Set · Regression Test · Test Oracle]] | 0 | 11 |  |
| 25 | [[Communities/25 Regression detection · AlphaEvolve · RSP|Regression detection · AlphaEvolve · RSP]] | 7 | 3 | 15 |
| 26 | [[Communities/26 BM25 · Reciprocal Rank Fusion (RRF) · Bi-encoder|BM25 · Reciprocal Rank Fusion (RRF) · Bi-encoder]] | 3 | 7 | 5, 11 |
| 27 | [[Communities/27 Decision boundary · Bias · ELBO|Decision boundary · Bias · ELBO]] | 5 | 5 | 3, 8 |
| 28 | [[Communities/28 Production-stack · RadixAttention · cache_control|Production-stack · RadixAttention · cache_control]] | 7 | 3 | 17 |
| 29 | [[Communities/29 Eval-context gaming · Time horizon · thread_id|Eval-context gaming · Time horizon · thread_id]] | 7 | 3 | 15 |
| 30 | [[Communities/30 Evaluation (Eval) · Kill switch · Non-determinism|Evaluation (Eval) · Kill switch · Non-determinism]] | 6 | 4 | 17 |
| … | 65 smaller clusters in `Communities/` | | | |

## Libraries

- [[Libraries/numpy (python)|numpy (python)]] — 75 lessons
- [[Libraries/torch (python)|torch (python)]] — 62 lessons
- [[Libraries/hono (typescript)|hono (typescript)]] — 10 lessons
- [[Libraries/scikit-learn (python)|scikit-learn (python)]] — 8 lessons
- [[Libraries/zod (typescript)|zod (typescript)]] — 5 lessons
- [[Libraries/torchvision (python)|torchvision (python)]] — 4 lessons
- [[Libraries/matplotlib (python)|matplotlib (python)]] — 3 lessons
- [[Libraries/pandas (python)|pandas (python)]] — 2 lessons
- [[Libraries/tiktoken (python)|tiktoken (python)]] — 2 lessons
- [[Libraries/@hono-node-server (typescript)|@hono/node-server (typescript)]] — 2 lessons
- [[Libraries/anthropic (python)|anthropic (python)]] — 1 lessons
- [[Libraries/build_catalog (python)|build_catalog (python)]] — 1 lessons
- [[Libraries/datasets (python)|datasets (python)]] — 1 lessons
- [[Libraries/diffusers (python)|diffusers (python)]] — 1 lessons
- [[Libraries/h5py (python)|h5py (python)]] — 1 lessons

## Learning paths

- [[Paths/AI Data Systems|AI Data Systems]]
- [[Paths/AI Evaluation and Reliability|AI Evaluation and Reliability]]
- [[Paths/Agent Skills Engineering|Agent Skills Engineering]]
- [[Paths/Agent Systems Engineering|Agent Systems Engineering]]
- [[Paths/Agent-Assisted Engineering|Agent-Assisted Engineering]]
- [[Paths/Building and Deploying AI Applications|Building and Deploying AI Applications]]
- [[Paths/Customer AI Deployment|Customer AI Deployment]]
- [[Paths/Developer Experience and Education|Developer Experience and Education]]
- [[Paths/LLM Product Engineering|LLM Product Engineering]]
- [[Paths/Model Context Protocol (MCP)|Model Context Protocol (MCP)]]
- [[Paths/Product Judgment and Delivery|Product Judgment and Delivery]]
- [[Paths/Software Engineering Fundamentals|Software Engineering Fundamentals]]

## Glossary categories

- [[Categories/AI-native development|AI-native development]] (23)
- [[Categories/Agents & tools|Agents & tools]] (27)
- [[Categories/Data & representations|Data & representations]] (13)
- [[Categories/Evaluation & safety|Evaluation & safety]] (17)
- [[Categories/Infrastructure & serving|Infrastructure & serving]] (18)
- [[Categories/Math & training|Math & training]] (42)
- [[Categories/Models & inference|Models & inference]] (29)
- [[Categories/Multimodal systems|Multimodal systems]] (15)
- [[Categories/Prompting & context|Prompting & context]] (15)
- [[Categories/Reliability & operations|Reliability & operations]] (17)
- [[Categories/Retrieval & generation|Retrieval & generation]] (14)
- [[Categories/Security & governance|Security & governance]] (20)

## Myths

- [[Myths/01 AI understands language|Myth: AI understands language]]
- [[Myths/02 More parameters = smarter model|Myth: More parameters = smarter model]]
- [[Myths/03 Neural networks are black boxes|Myth: Neural networks are black boxes]]
- [[Myths/04 AI will replace programmers|Myth: AI will replace programmers]]
- [[Myths/05 You need a PhD in math to do AI|Myth: You need a PhD in math to do AI]]
- [[Myths/06 GPT stands for General Purpose Technology|Myth: GPT stands for General Purpose Technology]]
- [[Myths/07 Temperature makes the AI more creative|Myth: Temperature makes the AI more creative]]
- [[Myths/08 Fine-tuning teaches the model new knowledge|Myth: Fine-tuning teaches the model new knowledge]]
- [[Myths/09 Bigger context window = better|Myth: Bigger context window = better]]
- [[Myths/10 AI agents are autonomous|Myth: AI agents are autonomous]]
- [[Myths/11 Transformers understand order because of positional encoding|Myth: Transformers understand order because of positional encoding]]
- [[Myths/12 Pre-training is just reading the internet|Myth: Pre-training is just reading the internet]]
- [[Myths/13 RLHF aligns AI with human values|Myth: RLHF aligns AI with human values]]
- [[Myths/14 Embeddings capture meaning|Myth: Embeddings capture meaning]]
- [[Myths/15 Zero-shot means no training|Myth: Zero-shot means no training]]
- [[Myths/16 AI models learn like humans|Myth: AI models learn like humans]]
- [[Myths/17 Scaling laws mean bigger is always better|Myth: Scaling laws mean bigger is always better]]
- [[Myths/18 Open source AI is the same as open weights|Myth: Open source AI is the same as open weights]]
- [[Myths/19 Prompt engineering is not real engineering|Myth: Prompt engineering is not real engineering]]
- [[Myths/20 CNNs are outdated, everything is transformers now|Myth: CNNs are outdated, everything is transformers now]]
- [[Myths/21 You need massive compute to train useful models|Myth: You need massive compute to train useful models]]

## What is in this vault

| Folder | Notes |
|---|---|
| Artifacts | 495 |
| Categories | 12 |
| Communities | 95 |
| Concepts | 647 |
| Lessons | 523 |
| Libraries | 35 |
| Myths | 21 |
| Paths | 12 |
| Phases | 20 |
| Resources | 359 |
| Tracks | 5 |

Graph counts (all of them, including nodes without a note): artifact 495, category 12, community 95, concept 3171, learning_path 12, lesson 523, library 35, myth 21, phase 20, resource 1670, track 5
