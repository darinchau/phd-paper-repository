---
title: "MuseGAN: Multi-track Sequential Generative Adversarial Networks for Symbolic Music Generation and Accompaniment"
authors: "Hao-Wen Dong, Wen-Yi Hsiao, Li-Chia Yang, and Yi-Hsuan Yang"
year: 2017
doi: 10.48550/arXiv.1709.06298
category: generation-and-planning
source: dong-2017-musegan-multi-track-sequential-generative.md
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/dong-2017-musegan-multi-track-sequential-generative.pdf"
pdf_filename: dong-2017-musegan-multi-track-sequential-generative.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
tags: []
---
## Summary

They report that the systems can generate coherent four-bar phrases from scratch and can generate four additional tracks conditioned on one human-provided track.

## Key Contributions

Core contribution

**Author claim — Abstract, Introduction, PDF pp. 1–2:** MuseGAN is a WGAN-GP-based framework for generating short, multi-track, polyphonic symbolic music. It models:

- five tracks: bass, drums, guitar, piano, strings;
- local musical structure at the bar level;
- temporal structure across four-bar phrases;
- inter-track dependencies;
- track-conditional generation for accompaniment.

The authors present three alternative models for inter-track dependency:

1. **Jamming model**
2. **Composer model**
3. **Hybrid model**

They report that the systems can generate coherent four-bar phrases from scratch and can generate four additional tracks conditioned on one human-provided track.

**Interpretation:** The major conceptual contribution is not long-form composition, but factorizing multi-track generation into:

```text
time-independent track/style variables
+ time-dependent shared/private variables
+ bar-level convolutional generators
```

This factorization remains relevant to structured symbolic generation, although the representation and evaluation are now substantially outdated.

---

### 2. Data and representation

#### Piano-roll representation

**Proposed Model → Data Representation, PDF p. 2**

An `M`-track bar is represented as:

```text
x ∈ {0,1}^{R × S × M}
```

where:

- `R = 96` time steps per bar;
- `S = 84` retained pitches after filtering;
- `M = 5` tracks.

A four-bar phrase therefore has shape:

```text
4 × 96 × 84 × 5
```

The representation is binary. For non-drum tracks, a one-step rest is inserted between notes to distinguish successive no

The complete evidence-grounded digest is in [`sources/dong-2017-musegan-multi-track-sequential-generative.md`](../../sources/dong-2017-musegan-multi-track-sequential-generative.md).

## Methodology and Architecture

Read the linked source digest for the paper's full method, equations, implementation details, and page/section anchors.

## Results

The linked source digest preserves the paper-reported results and their evidence boundaries; this page does not claim an independent reproduction.

## Related Papers

- [[overviews/2026-symbolic-music-literature-map]] — primary synthesis anchor for this batch; the overview places this paper beside related representation, generation, evaluation, and auditability work.
