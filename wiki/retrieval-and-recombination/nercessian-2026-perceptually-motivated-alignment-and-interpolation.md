---
title: "Perceptually Motivated Alignment and Interpolation of Pitch-Aligned Time-Frequency Representations"
authors: "Shahan Nercessian, Jeff Sontag, and Alejandro Koretzky"
year: 2026
doi: 10.48550/arXiv.2609.31971
category: retrieval-and-recombination
source: nercessian-2026-perceptually-motivated-alignment-and-interpolation.md
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/nercessian-2026-perceptually-motivated-alignment-and-interpolation.pdf"
pdf_filename: nercessian-2026-perceptually-motivated-alignment-and-interpolation.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
tags: []
---
## Summary

The paper provides an interpretable harmonic alignment/interpolation layer using invertible perceptual TIV transforms, pitch-axis assignment, and Circle-of-Fifths optimal transport; it is useful for mashup harmonic control but does not solve temporal, timbral, or source-separation alignment.

## Key Contributions

Core contribution

The authors propose a signal-processing toolkit for manipulating pitch-aligned time-frequency representations (PTFRs), including:

1. An invertible extension of the tonal interval vector (TIV).
2. Perceptually weighted alignment through pitch-axis permutations.
3. Optimal-transport interpolation on the Circle of Fourths/Fifths.
4. A low-dimensional geometric representation intended to separate:
   - root,
   - scale density,
   - scale color.

Their stated goal is structured manipulation of both audio-derived and symbolic pitch representations without requiring explicit key detection (Abstract; DAFx.1, §1).

**Interpretation:** This is best understood as a harmonic/pitch-structure layer, not a complete mashup-alignment system. It does not solve beat synchronization, phrase alignment, source separation, timbral matching, or expressive timing.

---

### 2. TIV and the perceptual representation

#### Original TIV

For chroma \(c\in\mathbb{R}^{N}\), normally \(N=12\), the paper defines:

\[
T(c)[k]
=
w_\ast[k]\sum_{n=0}^{N-1}\bar c[n]
\exp\left(-j\frac{2\pi kn}{N}\right),
\qquad 1\leq k\leq 6,
\]

with

\[
\bar c[n]=
\frac{c[n]}{\sum_{n=0}^{N-1}c[n]}.
\]

This normalization makes the representation amplitude-invariant (DAFx.2, §2, Eqs. 1–2).

The weights are:

- **Symbolic:**  
  \[
  w_{\text{symbolic}}=[2,11,17,16,19,7].
  \]
- **Audio:**  
  \[
  w_{\text{audio}}=[3,8,11.5,15,14.5,7.5].
  \]

The authors state that these weights derive from empirical dyad-consonance ratings. They claim that Euclidean distance in TIV space better corresponds to perceived cons

The complete evidence-grounded digest is in [`sources/nercessian-2026-perceptually-motivated-alignment-and-interpolation.md`](../../sources/nercessian-2026-perceptually-motivated-alignment-and-interpolation.md).

## Methodology and Architecture

Read the linked source digest for the paper's full method, equations, implementation details, and page/section anchors.

## Results

The linked source digest preserves the paper-reported results and their evidence boundaries; this page does not claim an independent reproduction.

## Related Papers

- [[overviews/2026-symbolic-music-literature-map]] — primary synthesis anchor for this batch; the overview places this paper beside related representation, generation, evaluation, and auditability work.
