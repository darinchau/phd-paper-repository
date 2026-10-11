---
title: "MIRA: A Musical Intent Refinement Agent for Aligning Text-to-Music Generation with User Intent"
authors: "Zhilin Wang et al."
year: 2026
doi: 10.48550/arXiv.2610.10355
category: interaction-and-evaluation
source: al-2026-mira-a-musical-intent-refinement.md
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/al-2026-mira-a-musical-intent-refinement.pdf"
pdf_filename: al-2026-mira-a-musical-intent-refinement.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
tags: []
---
## Summary

Affiliations: Shandong University; University of Science and Technology of China; Central Conservatory of Music; Kunlun Tech Co. Ltd.; Shanghai Jiao Tong University.

## Key Contributions

central contribution is not a new music generator. It is an **external control-and-evaluation loop**:

> natural-language request → structured intent specification → generation → requirement-level verification → prompt revision/search → selected output.

This is potentially important for explainable systems because the optimization target is decomposed into auditable requirements rather than hidden inside one scalar reward.

---

### 3. MuRA-Bench

### 3.1 Dataset composition

**Anchor:** §3.1, Appendix A.1, PDF pp. 3 and 15; extracted text approximately lines 157–186 and 872–901.

MuRA-Bench contains:

- **100 controlled requests**;
- derived from anonymized intent seeds collected on the **Mureka** platform;
- **68 instrumental** and **32 vocal** requests;
- **1,566 rubric items**:
  - 996 base items;
  - 570 completion items;
- 6–31 items per request;
- mean: **15.66** items;
- median: **14.5** items.

The benchmark includes:

- partially specified requests;
- reference-based requests;
- hybrid requests;
- requests with multiple simultaneous constraints.

Raw user logs are not released. The paper states that the curated benchmark was released with platform permission, but the PDF does not provide the actual dataset contents or release mechanism beyond the project-page reference.

### 3.2 Rubric structure

For a request \(x\), the gold rubric is:

\[
R(x)=B(x)\cup C(x)
\]

where:

- \(B(x)\): requirements directly supported by the prompt;
- \(C(x)\): musical traits completed from references, use cases, and context.

The seven dimensions are:

| Dimension | Items |
|---|---:|
|

The complete evidence-grounded digest is in [`sources/al-2026-mira-a-musical-intent-refinement.md`](../../sources/al-2026-mira-a-musical-intent-refinement.md).

## Methodology and Architecture

Read the linked source digest for the paper's full method, equations, implementation details, and page/section anchors.

## Results

The linked source digest preserves the paper-reported results and their evidence boundaries; this page does not claim an independent reproduction.

## Related Papers

- [[overviews/2026-symbolic-music-literature-map]] — primary synthesis anchor for this batch; the overview places this paper beside related representation, generation, evaluation, and auditability work.
