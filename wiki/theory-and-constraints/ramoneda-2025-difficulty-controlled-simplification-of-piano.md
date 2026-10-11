---
title: "Difficulty-Controlled Simplification of Piano Scores with Synthetic Data for Inclusive Music Education"
authors: "Pedro Ramoneda, Emilia Parada-Cabaleiro, Dasaem Jeong, and Xavier Serra"
year: 2025
doi: 10.48550/arXiv.2511.16228
category: theory-and-constraints
source: ramoneda-2025-difficulty-controlled-simplification-of-piano.md
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/ramoneda-2025-difficulty-controlled-simplification-of-piano.pdf"
pdf_filename: ramoneda-2025-difficulty-controlled-simplification-of-piano.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
tags: []
---
## Summary

“**Difficulty-Controlled Simplification of Piano Scores with Synthetic Data for Inclusive Music Education**.” **arXiv:2511.16228v2 [cs.SD], 22 November 2025**, 9 pages. No journal or conference venue is specified in the paper. The version/date appear on p. 1. The complete reference list is on pp. 8–9.

## Key Contributions

Evidence-grounded digest

### Bibliographic record

**Ramoneda, Pedro; Parada-Cabaleiro, Emilia; Jeong, Dasaem; Serra, Xavier.**  
“**Difficulty-Controlled Simplification of Piano Scores with Synthetic Data for Inclusive Music Education**.” **arXiv:2511.16228v2 [cs.SD], 22 November 2025**, 9 pages. No journal or conference venue is specified in the paper. The version/date appear on p. 1. The complete reference list is on pp. 8–9.

Important cited resources include:

- Mayer et al. (2024), “Practical End-to-End Optical Music Recognition for Pianoform Music” — source of the LMX representation.
- Ramoneda et al. (2024), “Combining piano performance dimensions for score difficulty classification” — source of the difficulty-labeling framework.
- Wu et al. (2025), “CLaMP 3: Universal Music Information Retrieval Across Unaligned Modalities and Unseen Languages” — style/content similarity model.
- XMander (2023), unofficial MuseScore dataset — source of the initial corpus.

### Research question and contribution

The paper asks whether piano-score simplification can be treated as **conditional symbolic-score translation**: given a difficult piano score, generate an easier version while preserving its musical identity, especially melody, harmony, style, readability, and playability.

The authors’ claimed contributions are:

1. A decoder-only transformer for difficulty-aware MusicXML score generation.
2. **PianoPairs**, a synthetic paired dataset of versions of the same piece at different estimated difficulty levels.
3. A mining strategy combining:
   - difficulty estimation with a c

The complete evidence-grounded digest is in [`sources/ramoneda-2025-difficulty-controlled-simplification-of-piano.md`](../../sources/ramoneda-2025-difficulty-controlled-simplification-of-piano.md).

## Methodology and Architecture

Read the linked source digest for the paper's full method, equations, implementation details, and page/section anchors.

## Results

The linked source digest preserves the paper-reported results and their evidence boundaries; this page does not claim an independent reproduction.

## Related Papers

- [[overviews/2026-symbolic-music-literature-map]] — primary synthesis anchor for this batch; the overview places this paper beside related representation, generation, evaluation, and auditability work.
