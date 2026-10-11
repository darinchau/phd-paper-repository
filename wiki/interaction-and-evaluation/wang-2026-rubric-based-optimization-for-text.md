---
title: "Rubric-Based Optimization for Text-to-Music Generation"
authors: "Ping Wang, Guang Yang, Shao-Rong Su, Junkai Wu, Pang Wei Koh, and Noah A. Smith"
year: 2026
doi: 10.48550/arXiv.2610.03589
category: interaction-and-evaluation
source: wang-2026-rubric-based-optimization-for-text.md
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/wang-2026-rubric-based-optimization-for-text.pdf"
pdf_filename: wang-2026-rubric-based-optimization-for-text.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
tags: []
---
## Summary

> Use broad rubric rewards for qualities difficult to formalize, but use exact symbolic objectives wherever reliable measurements exist.

## Key Contributions

Bottom line

**Yes, the method is adaptable to our research, but the exact setup is not Qwen-lab-scale.** The generators are only **300M MusicGen-small** and **3.5B ACE-Step**, both frozen and adapted with LoRA. The largest component is the **30B Qwen3-Omni evaluator**, used only for inference; a **7B Qwen2-Audio** evaluator also works. The main cost is rating generated audio, not pretraining.

For our symbolic mashup/repair work, the most transferable idea is:

> Use broad rubric rewards for qualities difficult to formalize, but use exact symbolic objectives wherever reliable measurements exist.

That maps naturally to perceptual coherence versus explicit harmony, voice-leading, provenance, source identity, and repair constraints.

---

### 1. Bibliography and version status

- **Title:** *Rubric-Based Optimization for Text-to-Music Generation*
- **Authors:** Ping Wang, Guang Yang, Shao-Rong Su, Junkai Wu, Pang Wei Koh, Noah A. Smith
- **Affiliations:** University of Washington and Allen Institute for AI
- **Identifier shown in PDF:** `arXiv:2610.03589v1 [cs.SD]`
- **PDF date:** 2 October 2026
- **Status:** “Preprint. Under review.”
- **DOI:** `10.48550/arXiv.2610.03589`
- **Length:** 27 PDF pages, including references and appendices.

Evidence: PDF page 1; extracted text `/tmp/paper-digest/2610.03589v1.txt:1-15`.

#### Version ambiguity

The supplied PDF consistently identifies itself as **v1**. You reported that the API now returns a later **v2** from October 2026. I have **not treated v2 as equivalent**: all findings below refer specifically to the downloaded v1. The PDF

The complete evidence-grounded digest is in [`sources/wang-2026-rubric-based-optimization-for-text.md`](../../sources/wang-2026-rubric-based-optimization-for-text.md).

## Methodology and Architecture

Read the linked source digest for the paper's full method, equations, implementation details, and page/section anchors.

## Results

The linked source digest preserves the paper-reported results and their evidence boundaries; this page does not claim an independent reproduction.

## Related Papers

- [[overviews/2026-symbolic-music-literature-map]] — primary synthesis anchor for this batch; the overview places this paper beside related representation, generation, evaluation, and auditability work.
