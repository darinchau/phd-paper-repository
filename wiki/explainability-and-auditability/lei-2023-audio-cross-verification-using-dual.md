---
title: "Audio Cross Verification Using Dual Alignment Likelihood Ratio Test"
authors: Heidi Lei, Arm Wonghirundacha, Irmak Bukey, TJ Tsai
year: 2023
doi: 10.48550/arXiv.2607.18190
category: explainability-and-auditability
source: lei-2023-audio-cross-verification-using-dual.md
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/lei-2023-audio-cross-verification-using-dual.pdf"
pdf_filename: lei-2023-audio-cross-verification-using-dual.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-31
tags:
  - audio-forensics
  - cross-verification
  - likelihood-ratio
  - alignment
  - explainable-decisions
---
## Summary

DA-LRT verifies a short audio clip against a trusted reference recording instead of hunting for editing artifacts. It builds two alignments of query to reference — a non-tampered hypothesis with a diagonal path only, and a tampered hypothesis that may insert, delete or replace material — then scores the clip by the likelihood ratio between the two hypotheses on the frames where the alignments disagree. On read speech it separates clean insertions and deletions down to a quarter second, while short replacements remain the hard case.

## Key Contributions

- Reframes tampering detection as **external consistency**: the claim becomes “this clip matches that source” rather than “I found no artifact”.
- Makes the decision an explicit comparison of two inspectable hypotheses whose alignment paths show *where* the clip diverges, an explanation surface a scalar classifier does not provide.
- Handles insertion, deletion and replacement in one framework via a two-state hidden-state time warping alignment.
- Reports a large reduction in equal error rate against an MFCC-Euclidean baseline across 15 bitrate × edit-length benchmarks.

## Methodology and Architecture

MFCCs (39 coefficients, 25 ms frames, 10 ms hop) are hashed into a 26-bit binary code to pre-select a candidate region in the reference. H1 then aligns query to reference with a diagonal-only path; H2 runs hidden-state time warping with insertion, deletion and plane-transition penalties. Frames where the paths agree model the “match” distribution as 39 scalar Gaussians fitted to feature differences; frames where they differ by two or more frames model the “non-match” distribution under an independence assumption. The log likelihood ratio over those disagreement frames is the tampering score. Evaluation uses DAPS read speech: 100 recordings, 20 speakers, three bitrates and five edit durations, 2,000 train and 2,000 test queries per benchmark, scored by equal error rate at recording level.

The complete evidence-grounded digest, with page anchors, the Table 1 values, and the paper's stated caveats, is in [`sources/lei-2023-audio-cross-verification-using-dual.md`](../../sources/lei-2023-audio-cross-verification-using-dual.md).

## Results

Aggregate equal error rate is 3.4% at 256 kbps, 3.7% at 128 kbps and 4.3% at 64 kbps, versus 9.2%, 9.0% and 8.8% for the MFCC-Euclidean baseline [PDF p. 4, Table 1]. Insertions and deletions are detected almost perfectly down to 0.25 s (0.00–0.20% error) because they desynchronise everything after the edit. Replacements keep the timeline aligned and are the failure mode: 3.1% error at 0.5 s and 33% at 0.25 s at 256 kbps [PDF p. 4, Table 1]. The authors stress that same-recording filler is a best case for the editor, and that the likelihood test's independence assumptions are known to be false but are applied to both hypotheses.

## Related Papers

- [[concepts/auditable-creative-editing-pipelines]] — the hierarchy this paper illustrates: a visible two-hypothesis comparison is decision auditability, not yet evidence that the stated reason is causally faithful.
- [[explainability-and-auditability/wei-2024-do-music-generation-models-encode]] — the probing counterpart: recoverability of a musical property is weaker evidence than an intervention, just as an alignment is weaker evidence than a controlled test.
- [[retrieval-and-recombination/davies-2014-automashupper-automatic-creation-of-multi]] — an earlier system that also exposes a beat-level alignment and its parameters, but does not use the alignment as the decision itself.
- [[explainability-and-auditability/al-2026-tracing-inputs-verifying-outputs-validating]] — provenance verification for generated music, the closest transfer target for a mashup or repair pipeline.
- [[overviews/2026-symbolic-music-literature-map]] — batch index for the October 2026 intake this reading belongs to.
