---
id: "lesson:08/12"
type: lesson
ref: 08/12
phase: 8
num: 12
title: 3D Generation
lesson_type: learn
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 0
code_files: 1
concepts: 7
prereqs: 1
community: 78
aliases:
  - 08/12
  - 08-12
tags:
  - phase/08
  - type/learn
  - community/78
  - stdlib-only
source: ai-engineering-from-scratch/phases/08-generative-ai/12-3d-generation/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/12-3d-generation"
---

# 08/12 3D Generation

> 3D is the modality where 2D-to-3D leverage is strongest. The 2023 breakthrough was 3D Gaussian Splatting. The 2024-2026 generative push layers multi-view diffusion + 3D reconstruction on top to produce objects and scenes from a single prompt or photo.

**Phase:** [[Phases/08 Generative AI|Phase 8: Generative AI]] · **Type:** Learn · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/08-generative-ai/12-3d-generation/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/12-3d-generation) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/08-generative-ai/12-3d-generation) · code: main.py  
**Community:** [[Communities/78 3D Gaussian splatting · NeRF|78 3D Gaussian splatting · NeRF]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 4 (Vision), Phase 8 · 07 (Latent Diffusion)`

- [[Lessons/08-07 Latent Diffusion & Stable Diffusion|08/07 Latent Diffusion & Stable Diffusion]] — Latent Diffusion
- Whole phase: [[Phases/04 Computer Vision|Phase 4: Computer Vision]] — Vision ·  medium confidence

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/07-09 Vision Transformers (ViT)|07/09 Vision Transformers (ViT)]], [[Lessons/08-02 Autoencoders & Variational Autoencoders (VAE)|08/02 Autoencoders & Variational Autoencoders (VAE)]], [[Lessons/08-06 Diffusion Models — DDPM from Scratch|08/06 Diffusion Models — DDPM from Scratch]]
- depth 3: [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]], [[Lessons/03-07 Regularization|03/07 Regularization]], [[Lessons/04-03 CNNs — LeNet to ResNet|04/03 CNNs — LeNet to ResNet]], [[Lessons/04-14 Vision Transformers (ViT)|04/14 Vision Transformers (ViT)]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/08-01 Generative Models — Taxonomy & History|08/01 Generative Models — Taxonomy & History]]

## Concepts taught

- [[Concepts/3D Gaussian splatting|3D Gaussian splatting]] `lesson term` — Scene as a cloud of 3D Gaussians; differentiable alpha-composite render.
- [[Concepts/NeRF|NeRF]] `lesson term` — MLP that outputs color + density at a 3D point; render by ray integration.
- Triplane `lesson term` — Factor 3D into three 2-D axis-aligned feature grids; cheaper than volumetric.
- SDS `lesson term` — Train 3D model by using 2D-diffusion score as pseudo-gradient.
- Multi-view diffusion `lesson term` — Diffusion model that outputs a batch of consistent camera views.
- PBR `lesson term` — Material with albedo, roughness, metallic, normal channels.
- [[Concepts/Densification|Densification]] `lesson term` — 3DGS training heuristic: split / clone splats in high-gradient regions.

## Ships

- [[Artifacts/08-12 3d-pipeline|3d-pipeline]] `skill` — Choose a 3D generation or reconstruction pipeline given input type, output format, and use case.

## Further reading

- [[Resources/NeRF (Mildenhall et al., 2020)|NeRF (Mildenhall et al., 2020)]] ([link](https://arxiv.org/abs/2003.08934)) — NeRF. ·  also cited by 1 other lesson
- Poole et al. (2022). DreamFusion: Text-to-3D using 2D Diffusion ([link](https://arxiv.org/abs/2209.14988)) — SDS.
- Liu et al. (2023). Zero-1-to-3: Zero-shot One Image to 3D Object ([link](https://arxiv.org/abs/2303.11328)) — Zero123.
- [[Resources/3D Gaussian Splatting (Kerbl et al., 2023)|3D Gaussian Splatting (Kerbl et al., 2023)]] ([link](https://arxiv.org/abs/2308.04079)) — 3DGS. ·  also cited by 1 other lesson
- Shi et al. (2023). MVDream ([link](https://arxiv.org/abs/2308.16512)) — multi-view diffusion.
- Hong et al. (2023). LRM: Large Reconstruction Model for Single Image to 3D ([link](https://arxiv.org/abs/2311.04400)) — LRM.
- Gao et al. (2024). CAT3D: Create Anything in 3D with Multi-View Diffusion Models ([link](https://arxiv.org/abs/2405.10314)) — CAT3D.
- Stability AI (2024). Stable Video 3D (SV3D) ([link](https://stability.ai/research/sv3d)) — SV3D.


%% ── my notes ── %%
