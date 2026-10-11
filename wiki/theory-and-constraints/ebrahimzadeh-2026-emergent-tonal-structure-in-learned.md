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

The paper tests whether a very simple **skip-gram embedding of chord tokens** can learn interpretable tonal geometry without explicit music-theoretic supervision. It compares:

## Key Contributions

Central contribution

The paper tests whether a very simple **skip-gram embedding of chord tokens** can learn interpretable tonal geometry without explicit music-theoretic supervision. It compares:

- **AUG:** all 12 pitch-class transpositions of each corpus sequence.
- **ORIG:** the original, non-augmented sequences.

The augmented embeddings generally recover stronger circle-of-fifths structure, transposition equivariance, key-centered organization, interpretable key-to-key steering, and more stable tension-related quantities.

Code: **https://github.com/MaraalE/chord-tonality** (p. 1, footnote 1).

---

### Page-by-page evidence map

- **p. 1:** Abstract, motivation, introduction, related work, code link.
- **p. 2:** Related work; datasets; corpus preprocessing; Table 1; skip-gram setup.
- **p. 3:** Circle-of-fifths analysis; Figure 1; Tables 2–3; transposition equivariance; start of key analysis.
- **p. 4:** Table 4 key structure; controls; tonal-region steering; Table 5; start of tension analysis.
- **p. 5:** Tension definitions, Eqs. 1–3; Table 6; TIV comparison setup.
- **p. 6:** Table 7 TIV correspondence; human-tension experiment setup.
- **p. 7:** Figure 2, Figure 3, Table 8; limitations; conclusion and future work.
- **p. 8:** AI usage statement and references.

---

### Data and preprocessing

### Corpora (§3.1, p. 2)

1. **BPS-FH**
   - Expert Roman-numeral annotations for the first movements of Beethoven’s 32 piano sonatas.
   - Chord roots and qualities derived using an adapted released chord-symbol translation implementation.

2. **Isophonics**
   - Beatles chor

The complete evidence-grounded digest is in [`sources/ebrahimzadeh-2026-emergent-tonal-structure-in-learned.md`](../../sources/ebrahimzadeh-2026-emergent-tonal-structure-in-learned.md).

## Methodology and Architecture

Read the linked source digest for the paper's full method, equations, implementation details, and page/section anchors.

## Results

The linked source digest preserves the paper-reported results and their evidence boundaries; this page does not claim an independent reproduction.

## Related Papers

- [[overviews/2026-symbolic-music-literature-map]] — primary synthesis anchor for this batch; the overview places this paper beside related representation, generation, evaluation, and auditability work.
