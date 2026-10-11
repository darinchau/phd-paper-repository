---
title: "Where the Body Keeps the Beat: Structured Motion Conditioning and Music Dynamics Supervision for Dance-to-Music Generation"
authors: "Changchang Sun, Lu Cheng, and Yan Yan"
year: 2026
doi: 10.48550/arXiv.2610.00726
category: generation-and-planning
source: sun-2026-where-the-body-keeps-the.md
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/sun-2026-where-the-body-keeps-the.pdf"
pdf_filename: sun-2026-where-the-body-keeps-the.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
tags: []
---
## Summary

I inspected the supplied extracted text and rendered pages, including all figures, tables, equations, and appendices.

## Key Contributions

Core contribution

#### Author claims

The paper proposes Dyna2Music, combining:

1. **Spatio-Spectral Motion Decomposition (SSMD)**  
   Separates dance motion by:
   - five body parts;
   - slow and fast temporal-frequency bands.

2. **Hierarchical Slow-Fast Conditioning Encoder (HSF-Encoder)**  
   Uses part-wise motion energy and frozen MotionBERT features to create 256-dimensional conditioning tokens.

3. **Latent Dynamics Consistency (LDC)**  
   Adds an auxiliary loss matching local adjacent-frame change magnitudes between:
   - a single-step estimate of the clean generated music latent;
   - the paired reference music latent.

4. **Latent flow-matching music generator**  
   A DiffRhythm-derived transformer generates continuous music latents, decoded by a frozen waveform VAE.

The authors report improved onset synchrony and FAD over 15 baselines on AIST++ and TikTok (abstract, pp. 1–3; Sections 3–4, pp. 4–9).

#### Interpretation

The technically important idea is not merely “more motion features.” It is the explicit separation of:

- **where** motion occurs;
- **at what temporal scale** it occurs;
- **how local output dynamics** should vary in latent space.

That design is potentially transferable to symbolic generation, but the paper does not demonstrate symbolic generation or repair.

---

### 3. Architecture

#### Input and latent representation

A dance sequence is represented as 3D joint positions \(J\) over \(N\) video frames. Paired audio \(y\) is encoded by a frozen waveform VAE:

\[
x_1 = E(y) \in \mathbb{R}^{T \times d_a}
\]

where \(T\) is the music-latent l

The complete evidence-grounded digest is in [`sources/sun-2026-where-the-body-keeps-the.md`](../../sources/sun-2026-where-the-body-keeps-the.md).

## Methodology and Architecture

Read the linked source digest for the paper's full method, equations, implementation details, and page/section anchors.

## Results

The linked source digest preserves the paper-reported results and their evidence boundaries; this page does not claim an independent reproduction.

## Related Papers

- [[overviews/2026-symbolic-music-literature-map]] — primary synthesis anchor for this batch; the overview places this paper beside related representation, generation, evaluation, and auditability work.
