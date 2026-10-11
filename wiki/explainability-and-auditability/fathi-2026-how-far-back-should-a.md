---
title: "How Far Back Should a Transformer Look? Repetition and Copying in Music Sequence Models"
authors: "Amir Fathi"
year: 2026
doi: 10.48550/arXiv.2610.02837
category: explainability-and-auditability
source: fathi-2026-how-far-back-should-a.md
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/fathi-2026-how-far-back-should-a.pdf"
pdf_filename: fathi-2026-how-far-back-should-a.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
tags: []
---
## Summary

I inspected `/tmp/paper-digest/2610.02837v1.pdf`, the extracted text, all page breaks, Tables I–IX, Figures 1–8, Equations (1)–(4), and the reproducibility/audit appendix.

## Key Contributions

Evidence-grounded digest

### Bibliography and scope

**Amir Fathi**, “**How Far Back Should a Transformer Look? Repetition and Copying in Music Sequence Models**,” arXiv:**2610.02837v1** [cs.SD], **2 October 2026**, 17 pages. University of Alberta.

I inspected `/tmp/paper-digest/2610.02837v1.pdf`, the extracted text, all page breaks, Tables I–IX, Figures 1–8, Equations (1)–(4), and the reproducibility/audit appendix.

#### Page anchors

- **pp. 1–2:** Abstract, introduction, related work
- **pp. 2–4:** Corpora, splits, tokenization
- **pp. 4–5:** Autoencoder and exact-context predictors
- **pp. 5–6:** Evaluation protocol
- **p. 6:** Table II, Figure 1, context sweep
- **p. 7:** Table III, Table IV, repeat-lag and erasure analyses
- **pp. 8–9:** Figure 5, trained-model history restriction; O’Neill’s and MusicNet
- **pp. 9–11:** Seed dependence, averaging predictor, autoencoder-seed analysis
- **pp. 11–13:** Generation analysis, Table VII, Figure 7
- **pp. 13–15:** Audit of earlier result, limitations, discussion, Figure 8
- **pp. 15–17:** Conclusion, Tables VIII–IX, reproducibility appendix, references

---

### Core question and headline conclusion

The paper asks:

1. How does autoregressive symbolic-music prediction change as available history increases?
2. What information is actually being used by long-context models?

**Author’s main claim:** On the rendered Nottingham and O’Neill’s folk-score representations, most of the large long-context improvement is caused by **exact copying of earlier repeated passages**, rather than a general ability to model long-range musica

The complete evidence-grounded digest is in [`sources/fathi-2026-how-far-back-should-a.md`](../../sources/fathi-2026-how-far-back-should-a.md).

## Methodology and Architecture

Read the linked source digest for the paper's full method, equations, implementation details, and page/section anchors.

## Results

The linked source digest preserves the paper-reported results and their evidence boundaries; this page does not claim an independent reproduction.

## Related Papers

- [[overviews/2026-symbolic-music-literature-map]] — primary synthesis anchor for this batch; the overview places this paper beside related representation, generation, evaluation, and auditability work.
