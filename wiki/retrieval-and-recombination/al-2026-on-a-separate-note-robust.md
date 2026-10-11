---
title: "On a Separate Note: Robust Score-Informed Note Separation with a Two-Stream TFC-TDF U-Net and Adaptive Set Ownership"
authors: "Benjamin Shiue-Hal Chou et al."
year: 2026
doi: 10.48550/arXiv.2609.29071
category: retrieval-and-recombination
source: al-2026-on-a-separate-note-robust.md
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/al-2026-on-a-separate-note-robust.pdf"
pdf_filename: al-2026-on-a-separate-note-robust.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
tags: []
---
## Summary

where \(x\) is a monaural mixture and \(s_i\) is the performed waveform of note \(i\). Each aligned score event is

## Key Contributions

Paper digest

### Identity

- **Title:** *On a Separate Note: Robust Score-Informed Note Separation with a Two-Stream TFC-TDF U-Net and Adaptive Set Ownership*
- **Authors:** Benjamin Shiue-Hal Chou, Purvish Jajal, Nicholas John Eliopoulos, James C. Davis, George K. Thiruvathukal, Kristen Yeon-Ji Yun, Hao-Wen Dong, and Yung-Hsiang Lu.
- **Venue/version:** arXiv:2609.29071v1, 24 September 2026; category cs.SD.
- **Scope:** 5-page paper; pages 1–4 contain the paper and page 5 contains references. **No appendix is present.**

### Page-by-page inspection

- **p. 1, Abstract, Introduction:** Defines score-informed note separation and motivates note-level editing, learning, and repairing wrong notes. Introduces NoteSep, NoteGrab, ASO, SCNS-Train, and SCNS-Eval.
- **p. 2, §§2.1–2.4:** Gives the task definition, selective harmonic gate, two-stream architecture, cross-attention, FiLM conditioning, and ASO design. Figure 1 shows NoteGrab; Figure 2 begins on this page.
- **p. 3, §2.4, §3.1–3.2:** Completes Figure 2, reports Table 1, dataset/training details, metrics, ablations, and computational cost.
- **p. 4, §§3.3–4:** Shows Figure 3 and Tables 2–3, evaluates editing and real-recording transfer, and gives the conclusion.
- **p. 5:** References only.

### Exact problem

**Author formulation (p. 2, §2.1):**

\[
x=\sum_i s_i
\]

where \(x\) is a monaural mixture and \(s_i\) is the performed waveform of note \(i\). Each aligned score event is

\[
q_i=(p_i,t_i^{on},t_i^{off}).
\]

Given a local mixture window and \(q_i\), the system estimates the performed waveform of that individual not

The complete evidence-grounded digest is in [`sources/al-2026-on-a-separate-note-robust.md`](../../sources/al-2026-on-a-separate-note-robust.md).

## Methodology and Architecture

Read the linked source digest for the paper's full method, equations, implementation details, and page/section anchors.

## Results

The linked source digest preserves the paper-reported results and their evidence boundaries; this page does not claim an independent reproduction.

## Related Papers

- [[overviews/2026-symbolic-music-literature-map]] — primary synthesis anchor for this batch; the overview places this paper beside related representation, generation, evaluation, and auditability work.
