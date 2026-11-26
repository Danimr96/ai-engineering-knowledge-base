---
id: "lesson:18/23"
type: lesson
ref: 18/23
phase: 18
num: 23
title: "Watermarking — SynthID, Stable Signature, C2PA"
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 6
code_files: 1
concepts: 8
prereqs: 2
community: 32
aliases:
  - 18/23
  - 18-23
tags:
  - phase/18
  - type/build
  - community/32
  - stdlib-only
source: ai-engineering-from-scratch/phases/18-ethics-safety-alignment/23-watermarking-synthid-stable-signature-c2pa/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/23-watermarking-synthid-stable-signature-c2pa"
---

# 18/23 Watermarking — SynthID, Stable Signature, C2PA

> Three technologies structure 2026 AI-generated-content provenance. SynthID (Google DeepMind) — image watermarking launched August 2023, text+video May 2024 (Gemini + Veo), text open-sourced October 2024 via Responsible GenAI Toolkit, unified multi-media detector November 2025 alongside Gemini 3 Pro. Text watermarking adjusts next-token sampling probabilities imperceptibly; image/video watermarks survive compression, cropping, filters, frame-rate changes. Stable Signature (Fernandez et al., ICCV 2023, arXiv:2303.15435) — fine-tunes the latent diffusion decoder so every output contains a fixed message; cropped (10% of content) generated images detected >90% at FPR<1e-6. Follow-up "Stable Signature is Unstable" (arXiv:2405.07145, May 2024) — fine-tuning removes the watermark while preserving quality. C2PA — cryptographically signed, tamper-evident metadata standard (C2PA 2.2 Explainer 2025). Watermarking and C2PA are complementary: metadata can be stripped but carries richer provenance; watermarks persist through transcoding but carry less information.

**Phase:** [[Phases/18 Ethics, Safety & Alignment|Phase 18: Ethics, Safety & Alignment]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/18-ethics-safety-alignment/23-watermarking-synthid-stable-signature-c2pa/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/23-watermarking-synthid-stable-signature-c2pa) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/18-ethics-safety-alignment/23-watermarking-synthid-stable-signature-c2pa) · code: main.py · quiz: 6 questions  
**Community:** [[Communities/32 Instruction-Following as Alignment Signal · Reward Hacking and Goodhart's Law · Sycophancy as RLHF Amplific|32 Instruction-Following as Alignment Signal · Reward Hacking and Goodhart's Law · Sycophancy as RLHF Amplification]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 10 · 04 (sampling), Phase 01 · 09 (information theory)`

- [[Lessons/01-09 Information Theory|01/09 Information Theory]] — information theory
- [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]] — sampling

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]], [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]], [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]], [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]]
- depth 3: [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]], [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]], [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]], [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]], [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]], [[Lessons/03-05 Loss Functions|03/05 Loss Functions]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]]

## Builds on this

- [[Lessons/18-28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR|18/28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR]]

## Concepts taught

- SynthID `lesson term` — Cross-modal provenance signal; text, image, audio, video
- Token watermark `lesson term` — Biased-sampling text watermark detectable via green-token z-score
- Stable Signature `lesson term` — Fine-tuned-decoder watermark; ICCV 2023
- [[Concepts/C2PA|C2PA]] `lesson term` — Cryptographically signed tamper-evident provenance metadata
- Paraphrase robustness `lesson term` — Text watermark property; currently limited
- Fine-tune removal `lesson term` — Attack that removes image watermark via decoder fine-tuning
- Cross-modal detector `lesson term` — November 2025 unified API across modalities
- [[Concepts/Content Provenance|Content Provenance]] `glossary` — Verifiable information about the origin and editing history of a piece of media or other digital content, including the actors, tools, transformations, and assertions attached to it.

## Ships

- [[Artifacts/18-23 provenance-audit|provenance-audit]] `skill` — Audit a content deployment's provenance chain across watermarking and C2PA metadata.

## Further reading

- Kirchenbauer et al. — A Watermark for Large Language Models (ICML 2023, arXiv:2301.10226) ([link](https://arxiv.org/abs/2301.10226)) — the token-watermark mechanism
- Fernandez et al. — Stable Signature (ICCV 2023, arXiv:2303.15435) ([link](https://arxiv.org/abs/2303.15435)) — image watermark paper
- Stable Signature is Unstable" (arXiv:2405.07145) ([link](https://arxiv.org/abs/2405.07145)) — the removal attack
- C2PA 2.2 Explainer (2025) ([link](https://c2pa.org/specifications/specifications/2.2/explainer/Explainer.html)) — metadata standard
- Google DeepMind — SynthID ([link](https://deepmind.google/models/synthid/)) — the cross-modal watermark


%% ── my notes ── %%
