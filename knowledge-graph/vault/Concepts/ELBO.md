---
id: "concept:elbo"
type: concept
name: ELBO
canonical: false
taught_in: 2
community: 27
tags:
  - concept/lesson-term
  - community/27
source: ai-engineering-from-scratch/phases/08-generative-ai/01-generative-models-taxonomy-history/docs/en.md
---

# ELBO

**Community:** [[Communities/27 Decision boundary · Bias · ELBO|27 Decision boundary · Bias · ELBO]]

> *What people say:* "Evidence lower bound"

**What it actually means:** A tractable lower bound on log p(x); VAEs and diffusion optimize it.

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/08-01 Generative Models — Taxonomy & History|08/01 Generative Models — Taxonomy & History]]
- [[Lessons/08-02 Autoencoders & Variational Autoencoders (VAE)|08/02 Autoencoders & Variational Autoencoders (VAE)]] — log p(x) ≥ recon - KL[q(z|x) || p(z)]; tight when q = p(z|x).


%% ── my notes ── %%
