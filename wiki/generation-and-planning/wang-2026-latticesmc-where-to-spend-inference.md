---
title: "LatticeSMC: Where to Spend Inference-Time Compute in Chunked Sequence Generators"
authors: "Xuanchen Wang, Heng Wang, and Weidong Cai"
year: 2026
doi: 10.48550/arXiv.2610.02774
category: generation-and-planning
source: wang-2026-latticesmc-where-to-spend-inference.md
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/wang-2026-latticesmc-where-to-spend-inference.pdf"
pdf_filename: wang-2026-latticesmc-where-to-spend-inference.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
tags: []
---
## Summary

The paper studies inference-time search for generators that produce long sequences **chunk by chunk**, with each chunk generated through iterative denoising or flow steps. Its central question is where to spend a fixed denoiser-evaluation budget: across particles, chunks, denoising steps, or terminal selection.

## Key Contributions

Core contribution and theoretical results

#### Problem formulation — §3.1, p.4

A sequence is divided into \(K\) chunks:

\[
x=(x^{(1)},\ldots,x^{(K)}), \qquad
p(x\mid c)=\prod_{k=1}^K p(x^{(k)}\mid x^{(<k)},c).
\]

Each chunk is generated using \(S\) denoising steps. Given reward \(r(x)\) and temperature \(\tau>0\), the intended target is

\[
\pi_\tau(x\mid c)\propto p(x\mid c)\exp(r(x)/\tau).
\]

The fixed budget is \(B=NKS\), counting one denoiser evaluation per particle and denoising step, multiplied by classifier-free-guidance cost where applicable.

The paper distinguishes:

- **Sampling:** return a particle according to its normalized importance weight.
- **Search:** return the highest-reward particle.

This distinction is important: many comparisons become unfair if a sampler returning a weighted draw is compared with a greedy method that always returns its best particle.

#### Lattice Feynman–Kac model — §3.2, p.4; Figure 1, p.2

The generation process is represented on a two-dimensional lattice:

\[
\mathcal L=\{(k,t):1\leq k\leq K,\;1\leq t\leq S\},
\]

where \(k\) is the chunk index and \(t\) the within-chunk denoising step. Potentials \(G_{k,t}\) are placed at lattice points. Existing approaches become different potential/resampling placements:

- **Best-of-\(N\):** terminal potential only.
- **Feynman–Kac steering:** potentials along the denoising axis.
- **Chunk pruning:** chunk-boundary potentials with deterministic top-\(M\) replication.
- **LatticeSMC:** exact chunk or prefix-score potentials, with ESS-gated systematic resampling.

The Feynman–Kac model is

The complete evidence-grounded digest is in [`sources/wang-2026-latticesmc-where-to-spend-inference.md`](../../sources/wang-2026-latticesmc-where-to-spend-inference.md).

## Methodology and Architecture

Read the linked source digest for the paper's full method, equations, implementation details, and page/section anchors.

## Results

The linked source digest preserves the paper-reported results and their evidence boundaries; this page does not claim an independent reproduction.

## Related Papers

- [[overviews/2026-symbolic-music-literature-map]] — primary synthesis anchor for this batch; the overview places this paper beside related representation, generation, evaluation, and auditability work.
