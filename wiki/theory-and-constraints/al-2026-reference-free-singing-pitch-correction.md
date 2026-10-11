---
title: "Reference-Free Singing Pitch Correction via Music-Constrained Sequence Editing"
authors: "Biao Dong et al."
year: 2026
doi: 10.48550/arXiv.2610.11524
category: theory-and-constraints
source: al-2026-reference-free-singing-pitch-correction.md
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/al-2026-reference-free-singing-pitch-correction.pdf"
pdf_filename: al-2026-reference-free-singing-pitch-correction.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
tags: []
---
## Summary

I read the supplied extracted text and rendered pages 1–5. The tables, equations, architecture diagram, and Figure 2 were visually checked against the extraction.

## Key Contributions

Problem and claimed contribution

#### Problem

The paper addresses pitch correction when only an unaccompanied vocal recording is available. Existing systems often require a target melody, accompaniment, professional performance, MIDI, or predefined scale. The proposed task is to infer:

1. **Whether each detected note needs correction**, and
2. **The signed pitch modification**, using only the input performance.

The authors formulate this as **music-constrained sequence editing**, rather than direct pitch-sequence generation (Abstract; §§1, 2.1, pp. 1–2).

#### Author claims

The paper claims that the method:

- improves note-level pitch accuracy from **73.25% to 83.43%**;
- outperforms BERT-APC by **3.99 percentage points**;
- increases error repair rate from **26.18% to 46.81%**;
- preserves naturalness better than aggressive key snapping;
- uses tonal information without requiring a target melody or ground-truth key annotation (Abstract; §§4.1–4.3, pp. 1, 4).

#### Interpretation

The central methodological idea is conservative symbolic editing: preserve the input sequence and make sparse pitch edits. This is closer to a repair operator than to unconstrained generation.

---

### 3. Representation and processing pipeline

#### Audio-to-symbolic front end

The system uses:

- **SOME** for note-level pitch, onset, and duration;
- **RMVPE** for frame-level \(F_0\), used during reconstruction;
- quantized semitone pitches;
- a fixed vocal instrument code;
- estimated bar positions, time signature, and tempo.

The note representation is:

\[
x_i=(p_i,d_i,s_i,e_i)
\]

where \(p_

The complete evidence-grounded digest is in [`sources/al-2026-reference-free-singing-pitch-correction.md`](../../sources/al-2026-reference-free-singing-pitch-correction.md).

## Methodology and Architecture

Read the linked source digest for the paper's full method, equations, implementation details, and page/section anchors.

## Results

The linked source digest preserves the paper-reported results and their evidence boundaries; this page does not claim an independent reproduction.

## Related Papers

- [[overviews/2026-symbolic-music-literature-map]] — primary synthesis anchor for this batch; the overview places this paper beside related representation, generation, evaluation, and auditability work.
