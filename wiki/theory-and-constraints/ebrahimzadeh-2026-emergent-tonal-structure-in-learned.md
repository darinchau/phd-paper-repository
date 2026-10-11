---
title: "Emergent Tonal Structure in Learned Chord Embeddings and Its Relation to Tonal Tension"
authors: "Maral Ebrahimzadeh, Gilberto Bernardes, and Sebastian Stober"
year: 2026
doi: 10.48550/arXiv.2609.36460
category: theory-and-constraints
source: ebrahimzadeh-2026-emergent-tonal-structure-in-learned.md
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/ebrahimzadeh-2026-emergent-tonal-structure-in-learned.pdf"
pdf_filename: ebrahimzadeh-2026-emergent-tonal-structure-in-learned.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
tags: []
---
## Summary

The paper tests whether simple skip-gram chord embeddings can learn interpretable tonal geometry from symbolic chord co-occurrences. Twelve-fold transposition augmentation strengthens circle-of-fifths organization, transposition equivariance, key-centered structure, tonal steering, and tension stability, while the study remains a small, theory-guided triad-level probing baseline.

## Key Contributions

Central contribution

#### Authors’ claim

The paper tests whether simple skip-gram chord embeddings, trained only from symbolic chord co-occurrences, develop:

1. Circle-of-fifths geometry.
2. Transposition-equivariant structure.
3. Key-centered regions.
4. Interpretable movement between tonal regions.
5. Tension-related quantities corresponding to TIV-based measures and human tension profiles.

The authors report that **12-fold transposition augmentation generally improves stability, tonal coherence, and interpretability**.

#### Interpretation

This is primarily a **post-hoc interpretability and probing study**, not a model with an explicitly designed tonal latent space. The embeddings are ordinary 64-dimensional skip-gram vectors; tonal structure is demonstrated through external geometric tests, key templates, and tension probes.

---

### 1. Data and representation

### Corpora

**BPS-FH**  
- Expert Roman-numeral annotations for the first movements of Beethoven’s 32 piano sonatas.
- Chord roots and qualities derived using an adapted released chord-symbol translation implementation.
- Primary dataset.

**Isophonics**  
- Beatles catalogue chord annotations.
- Only the chord-label layer is used.
- Secondary dataset.

PDF p. 2, §3.1.

### Tokenization and preprocessing

The supported labels are reduced to a vocabulary of **24 root–quality tokens**:

```text
root_quality
C_M
A_m
```

The vocabulary contains all 12 pitch-class roots in major and minor quality.

Processing:

- Major, minor, and dominant-family labels—including sevenths and selected extensions—are mapped to their

The complete evidence-grounded digest is in [`sources/ebrahimzadeh-2026-emergent-tonal-structure-in-learned.md`](../../sources/ebrahimzadeh-2026-emergent-tonal-structure-in-learned.md).

## Methodology and Architecture

Read the linked source digest for the paper's full method, equations, implementation details, and page/section anchors.

## Results

The linked source digest preserves the paper-reported results and their evidence boundaries; this page does not claim an independent reproduction.

## Related Papers

- [[overviews/2026-symbolic-music-literature-map]] — primary synthesis anchor for this batch; the overview places this paper beside related representation, generation, evaluation, and auditability work.
