---
id: "lesson:08/09"
type: lesson
ref: 08/09
phase: 8
num: 9
title: "Inpainting, Outpainting & Image Editing"
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 2
community: 68
aliases:
  - 08/09
  - 08-09
tags:
  - phase/08
  - type/build
  - community/68
  - stdlib-only
source: ai-engineering-from-scratch/phases/08-generative-ai/09-inpainting-outpainting-editing/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/09-inpainting-outpainting-editing"
---

# 08/09 Inpainting, Outpainting & Image Editing

> Text-to-image makes new things. Inpainting fixes old ones. In production, 70% of billable image work is editing — swap a background, remove a logo, extend the canvas, regenerate a hand. Inpainting is where diffusion earns its keep.

**Phase:** [[Phases/08 Generative AI|Phase 8: Generative AI]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/08-generative-ai/09-inpainting-outpainting-editing/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/09-inpainting-outpainting-editing) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/08-generative-ai/09-inpainting-outpainting-editing) · code: main.py  
**Community:** [[Communities/68 CFG · ControlNet|68 CFG · ControlNet]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 8 · 07 (Latent Diffusion), Phase 8 · 08 (ControlNet & LoRA)`

- [[Lessons/08-07 Latent Diffusion & Stable Diffusion|08/07 Latent Diffusion & Stable Diffusion]] — Latent Diffusion
- [[Lessons/08-08 ControlNet, LoRA & Conditioning|08/08 ControlNet, LoRA & Conditioning]] — ControlNet & LoRA

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/07-09 Vision Transformers (ViT)|07/09 Vision Transformers (ViT)]], [[Lessons/08-02 Autoencoders & Variational Autoencoders (VAE)|08/02 Autoencoders & Variational Autoencoders (VAE)]], [[Lessons/08-06 Diffusion Models — DDPM from Scratch|08/06 Diffusion Models — DDPM from Scratch]]
- depth 3: [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]], [[Lessons/03-07 Regularization|03/07 Regularization]], [[Lessons/04-03 CNNs — LeNet to ResNet|04/03 CNNs — LeNet to ResNet]], [[Lessons/04-14 Vision Transformers (ViT)|04/14 Vision Transformers (ViT)]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/08-01 Generative Models — Taxonomy & History|08/01 Generative Models — Taxonomy & History]]

## Concepts taught

- [[Concepts/Inpainting|Inpainting]] `lesson term` — Regenerate inside a mask; keep outside pixels.
- Outpainting `lesson term` — Regenerate outside the canvas; keep inside.
- 9-channel U-Net `lesson term` — U-Net with noisy | encoded-source | mask as input.
- SDEdit `lesson term` — Noise to time t, denoise with new prompt.
- InstructPix2Pix `lesson term` — Fine-tuned diffusion on (image, instruction, output) triples.
- RePaint `lesson term` — Re-noise periodically during reverse to reduce seams.
- SAM `lesson term` — Mask generator by clicks or boxes; pairs with inpaint.
- Flux-Kontext `lesson term` — Flux variant that accepts a reference image + instruction for edits.

## Ships

- [[Artifacts/08-09 editing-pipeline|editing-pipeline]] `skill` — Plan an image-editing pipeline from source + edit description to a ready-to-ship output.

## Further reading

- Meng et al. (2022). SDEdit: Guided Image Synthesis and Editing with Stochastic Differential Equations ([link](https://arxiv.org/abs/2108.01073)) — SDEdit.
- Lugmayr et al. (2022). RePaint: Inpainting using Denoising Diffusion Probabilistic Models ([link](https://arxiv.org/abs/2201.09865)) — training-free inpainting.
- Hertz et al. (2022). Prompt-to-Prompt Image Editing with Cross-Attention Control ([link](https://arxiv.org/abs/2208.01626)) — attention-level editing.
- Brooks, Holynski, Efros (2023). InstructPix2Pix ([link](https://arxiv.org/abs/2211.09800)) — text-instruction editing.
- Kirillov et al. (2023). Segment Anything ([link](https://arxiv.org/abs/2304.02643)) — SAM, the mask source.
- Ravi et al. (2024). SAM 2: Segment Anything in Images and Videos ([link](https://arxiv.org/abs/2408.00714)) — video SAM.
- Black Forest Labs (2024). Flux.1-Fill and Flux.1-Kontext ([link](https://blackforestlabs.ai/flux-1-tools/)) — 2024 tooling.


%% ── my notes ── %%
