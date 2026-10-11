---
title: "A Decomposed Retrieval-Edit-Rerank Framework for Chord Generation"
authors: "Qiqi He, Dichucheng Li, Xiaoheng Sun, and Anqi Huang"
year: 2026
doi: 10.48550/arXiv.2605.07489
category: retrieval-and-recombination
source: he-2026-a-decomposed-retrieval-edit-rerank.md
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/he-2026-a-decomposed-retrieval-edit-rerank.pdf"
pdf_filename: he-2026-a-decomposed-retrieval-edit-rerank.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
tags: []
---
## Summary

1. **Retrieval**: find stylistically plausible melody–chord examples. 2. **Editing**: project each retrieved chord progression into a music-theoretically feasible space. 3. **Reranking**: select among feasible candidates using a soft trade-off between retrieval similarity and editing cost.

## Key Contributions

Evidence-grounded digest

### 1. Bibliography and version

**Qiqi He, Dichucheng Li, Xiaoheng Sun, and Anqi Huang.** “A Decomposed Retrieval-Edit-Rerank Framework for Chord Generation.” *International Conference on Multimedia Retrieval (ICMR ’26)*, Amsterdam, June 16–19, 2026, 5 pages. DOI: `10.1145/3805622.3810672`; ACM ISBN `979-8-4007-2617-0/2026/06`.

- arXiv version: **2605.07489v1 [cs.SD]**, submitted **8 May 2026**.
- Authors: NetEase Cloud Music except Dichucheng Li, listed as Individual Researcher.
- Inspected the complete supplied PDF and extracted text: pages 1–5, Figures 1–5, Tables 1–2, all equations, conclusion, and references.

### 2. Paper’s central claim

The paper decomposes symbolic melody harmonization into:

1. **Retrieval**: find stylistically plausible melody–chord examples.
2. **Editing**: project each retrieved chord progression into a music-theoretically feasible space.
3. **Reranking**: select among feasible candidates using a soft trade-off between retrieval similarity and editing cost.

**Author claim:** This separation improves the diversity–feasibility trade-off, interpretability, and controllability relative to monolithic chord-generation systems (Abstract; pp. 1–2, §2).

**Interpretation:** The main contribution is architectural and procedural rather than a new generative model. The system turns chord generation into candidate-conditioned symbolic decision-making.

---

### 3. Method and algorithms

#### 3.1 Retrieval

**Memory construction** (p. 2, §2.1; Fig. 2, p. 3):

- Training melodies are clipped into structurally meaningful segments.
-

The complete evidence-grounded digest is in [`sources/he-2026-a-decomposed-retrieval-edit-rerank.md`](../../sources/he-2026-a-decomposed-retrieval-edit-rerank.md).

## Methodology and Architecture

Read the linked source digest for the paper's full method, equations, implementation details, and page/section anchors.

## Results

The linked source digest preserves the paper-reported results and their evidence boundaries; this page does not claim an independent reproduction.

## Related Papers

- [[overviews/2026-symbolic-music-literature-map]] — primary synthesis anchor for this batch; the overview places this paper beside related representation, generation, evaluation, and auditability work.
