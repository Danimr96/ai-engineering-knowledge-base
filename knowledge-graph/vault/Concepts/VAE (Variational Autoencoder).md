---
id: "concept:vae-variational-autoencoder"
type: concept
name: VAE (Variational Autoencoder)
canonical: true
category: "Models & inference"
taught_in: 1
tags:
  - concept/glossary
  - category/models-and-inference
source: ai-engineering-from-scratch/glossary/terms.md
---

# VAE (Variational Autoencoder)

> *What people say:* A probabilistic generative autoencoder.

**What it actually means:** A latent-variable model trained with a reconstruction objective and a regularization term that keeps an approximate posterior close to a chosen prior. The reparameterization estimator allows gradients through stochastic latent sampling.

**Common confusion:** A VAE does not force every latent distribution to one fixed Gaussian; the exact prior and approximate posterior are modeling choices.

**Category:** [[Categories/Models & inference|Models & inference]]

## Related concepts

- [[Concepts/Decoder|Decoder]]
- [[Concepts/Diffusion Model|Diffusion Model]]
- [[Concepts/Encoder|Encoder]]
- [[Concepts/Image Token|Image Token]]
- [[Concepts/Latent Space|Latent Space]]

## Taught in

- [[Lessons/08-02 Autoencoders & Variational Autoencoders (VAE)|08/02 Autoencoders & Variational Autoencoders (VAE)]] `alias` — Encoder outputs a distribution, KL penalty shapes code space.

## Sources

- [[Resources/Auto-Encoding Variational Bayes|Auto-Encoding Variational Bayes]] ([link](https://arxiv.org/abs/1312.6114))


%% ── my notes ── %%
