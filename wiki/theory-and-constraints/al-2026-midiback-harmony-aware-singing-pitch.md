---
title: "MIDIBACK: Harmony-Aware Singing Pitch Correction via Joint Vocal-Accompaniment Symbolic Modeling"
authors: "Joaquim Cavalcante et al."
year: 2026
doi: 10.48550/arXiv.2609.28008
category: theory-and-constraints
source: al-2026-midiback-harmony-aware-singing-pitch.md
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/al-2026-midiback-harmony-aware-singing-pitch.pdf"
pdf_filename: al-2026-midiback-harmony-aware-singing-pitch.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
tags: []
---
## Summary

Thus, the digest below is grounded in the supplied MIDIBACK text extraction, with anchors such as “text p. 2, §2.3.” The PDF itself should be replaced before treating visual figures or PDF page numbers as authoritative.

## Key Contributions

Source-integrity warning

The supplied artifacts are inconsistent:

- `/tmp/paper-digest/2609.28008v2.txt` contains a **four-page MIDIBACK paper**, with logical anchors from the Abstract/§1 on text page 1 through References on text page 4.
- The visible `/tmp/paper-digest/2609.28008v2.pdf` has **22 rendered pages**, whose page 1 title is *Channel-Preserving Representation Alignment for EEG-to-Music Reconstruction*, marked `arXiv:2606.04040v2`; page 22 is its EEG supplementary appendix.
- The PDF’s hidden text layer contains MIDIBACK text on only the early logical pages, while the visible pages are unrelated.

Thus, the digest below is grounded in the supplied MIDIBACK text extraction, with anchors such as “text p. 2, §2.3.” The PDF itself should be replaced before treating visual figures or PDF page numbers as authoritative.

### Bibliographic and research question

**Cavalcante et al., “MIDIBACK: Harmony-Aware Singing Pitch Correction via Joint Vocal-Accompaniment Symbolic Modeling,” arXiv:2609.28008v2, 24 September 2026.**

The paper asks whether pitch correction can infer intended vocal notes from both vocal context and the note-level harmonic/polyphonic context of an accompaniment, rather than applying nearest-semitone or vocal-only correction.

The claimed contribution is a symbolic, note-level automatic pitch-correction model that serializes vocal and accompaniment events into one chronological OctupleMIDI sequence.

---

### Method

#### 1. Audio-to-symbolic preprocessing  
**Text p. 2, §2.1; p. 3, §3.1**

The pipeline uses:

1. `audio-slicer` for segmentation.
2. GAM

The complete evidence-grounded digest is in [`sources/al-2026-midiback-harmony-aware-singing-pitch.md`](../../sources/al-2026-midiback-harmony-aware-singing-pitch.md).

## Methodology and Architecture

Read the linked source digest for the paper's full method, equations, implementation details, and page/section anchors.

## Results

The linked source digest preserves the paper-reported results and their evidence boundaries; this page does not claim an independent reproduction.

## Related Papers

- [[overviews/2026-symbolic-music-literature-map]] — primary synthesis anchor for this batch; the overview places this paper beside related representation, generation, evaluation, and auditability work.
