---
title: "Audio Cross Verification Using Dual Alignment Likelihood Ratio Test"
authors: Heidi Lei, Arm Wonghirundacha, Irmak Bukey, TJ Tsai
year: 2023
doi: 10.48550/arXiv.2607.18190
category: explainability-and-auditability
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/lei-2023-audio-cross-verification-using-dual.pdf"
pdf_filename: lei-2023-audio-cross-verification-using-dual.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-31
---

## One-line Summary

Instead of looking for tampering artifacts, DA-LRT verifies a short clip against a trusted reference by computing two alignments — one assuming no tampering, one allowing insertions, deletions or replacements — and turning the difference into a likelihood ratio, so the decision is an explicit comparison of two inspectable hypotheses rather than a black-box score.

## 1. Document Information

- **Canonical citation:** Heidi Lei, Arm Wonghirundacha, Irmak Bukey, and TJ Tsai, “Audio Cross Verification Using Dual Alignment Likelihood Ratio Test,” arXiv:2607.18190v1 [cs.SD], 20 July 2026, 6 PDF pages. The arXiv comment states “Published at ICASSP 2023”; the PDF itself carries no proceedings header, so the venue line rests on that arXiv metadata, not on the read text.
- **Affiliations:** Massachusetts Institute of Technology; Pomona College; Harvey Mudd College. [PDF p. 1]
- **DOI:** `10.48550/arXiv.2607.18190` (arXiv DOI; no publisher DOI appears in the PDF).
- **Code:** `https://github.com/HMC-MIR/AudioCrossVerification` (URL printed in the repository digest of this batch, not verified here).
- **Canonical integrity:** SHA-256 `658d8d317ad16ba92f80eb8f743a42dac8fbab827002639250c0757d4f269e3e`; byte-identical to the PDF supplied for the October 2026 arXiv batch.
- **Rights boundary:** arXiv preprint; redistribution terms follow the arXiv licence on the abs page, which this record does not restate. Retained locally as research evidence only.
- **Primary category:** `explainability-and-auditability`. The contribution is a verification/forensic decision procedure whose main selling point is that its output is a hypothesis comparison with visible alignments, not a new generative or representation model.
- **Evidence levels:** “reported” values come from the paper's tables and text; “repository interpretation” marks what this repository infers for its own programme. Numerical results were re-read from the rendered table, and one figure in the batch digest was corrected during this ingest (see §4).

## 2. Key Contributions

### Cross verification instead of artifact detection

The paper separates *internal* consistency (does the signal contain traces of editing?) from *external* consistency (does this clip match a trusted source?). Artifact detectors can be defeated by anti-forensics and can only say “no evidence of tampering”; cross verification asks a stronger question and needs a reference recording, which the authors assume is available through fingerprinting or metadata. [PDF p. 1]

### Two hypotheses, two alignments, one likelihood ratio

H1 allows only a diagonal path (no tampering). H2 uses Hidden State Time Warping (HSTW) with a “matching” state and a “tampering” state that may take insertion/deletion steps, so the optimal path can leave and re-enter the diagonal. Query frames where the two paths disagree become the observations for a log-likelihood-ratio test, and that ratio is the tampering score. [PDF pp. 2–3]

### A localisable explanation

Because both paths are returned, the method shows *where* the query and the reference diverge, not just whether they do. The authors present this as the explainability argument: the user sees the two competing accounts of the same clip. [PDF p. 4]

## 3. Methodology and Architecture

- **Features.** MFCCs, 25 ms frames, 10 ms hop, 39 coefficients including deltas. [PDF p. 2]
- **Stage 1 — pre-selection.** A 26-bit binary hash (thresholded delta and delta-delta coefficients) finds the offset with minimum Hamming distance against the reference, and a buffered window around it is kept as the search region. [PDF p. 2]
- **Stage 2 — dual alignment.** H1 re-estimates the offset with an MFCC Euclidean cost under a diagonal-only constraint. H2 runs HSTW with insertion penalty α, deletion penalty γ, and plane-transition penalty β, using the dynamic-programming recurrences printed on p. 3; backpointers recover the optimal path. [PDF pp. 2–3]
- **Stage 3 — likelihood ratio.** Frames whose alignments agree (partition A) model the “match” distribution: 39 scalar Gaussians fitted to feature differences. Frames whose alignments differ by two or more frames (partition B), plus frames that sit entirely in the tampering plane, model the “non-match” distribution under an independence assumption. Partition B is scored under both hypotheses and the log ratio is the tampering score. [PDF p. 3, eq. 1–2]
- **Data.** DAPS: 100 high-quality low-noise read-speech recordings, 20 speakers, 5 scripts. Each recording is re-encoded at R kbps, 10 ten-second segments are sampled, and each segment is tampered by insertion, deletion, or replacement of an L-second filler taken from *the same recording* (same speaker, style, room). This yields 4,000 queries per (R, L) condition; half the speakers are held out. Three bitrates (256, 128, 64 kbps) × five durations (4, 2, 1, 0.5, 0.25 s) give 15 benchmarks of 2,000 train and 2,000 test queries each. [PDF pp. 3–4]
- **Metric.** Equal error rate (EER) at recording level, the level closest to a user's experience of the tool. [PDF p. 4]

## 4. Key Results and Benchmarks

Table 1 reports EER in percent. Aggregate rows (“all” tampering types) are [PDF p. 4, Table 1]:

| Query bitrate | DA-LRT | MFCC-Euclidean baseline |
|---|---|---|
| 256 kbps | 3.4 | 9.2 |
| 128 kbps | 3.7 | 9.0 |
| 64 kbps | 4.3 | 8.8 |

At 256 kbps by tampering type and duration, EER is [PDF p. 4, Table 1]: insertion 0.00 / 0.00 / 0.00 / 0.20 / 0.20 for L = 4 / 2 / 1 / 0.5 / 0.25 s; deletion 0.00 / 0.00 / 0.00 / 0.20 / 0.00; replacement 0.00 / 0.00 / 0.00 / 3.1 / 33. The same replacement cells read 3.1 / 34 at 128 kbps and 4.0 / 38 at 64 kbps, so bitrate matters only for short replacements. [PDF p. 4, Table 1]

- **Why insertions and deletions are easy.** They desynchronise every later frame, creating a global shift; replacements keep the timeline aligned and must be found from local feature differences alone. [PDF p. 4]
- **Runtime.** Mean 433 ms for query MFCCs, 5.82 s for reference MFCCs, and 123 ms for offset estimation, both alignments and the likelihood test. [PDF p. 4]
- **Correction to the batch digest.** The local batch digest reported the aggregate EERs correctly but compressed the replacement trend and omitted that EER values are percentages. It also implied a separate limitations section; the paper's caveats sit inside the results and method text instead. This record follows Table 1 directly.

## 5. Limitations and Future Work

- **Read speech, not news video.** DAPS is clean studio speech; there is no background noise, music, applause, or channel effect beyond bitrate, although DAPS contains other acoustic conditions the authors leave for future work. [PDF p. 3]
- **Best-case filler.** Inserted and replacement material comes from the same recording, so speaker, style and room match perfectly; real edits may be easier or harder to catch. [PDF pp. 3–4]
- **Silence-on-silence replacements.** For the shortest edits the random interval choice can replace silence with silence, which the authors say may make those cells overly pessimistic. [PDF p. 4]
- **Faulty modelling assumptions, applied symmetrically.** Features are assumed independent across time and across coefficients; the paper calls the assumptions “clearly … faulty” and argues that applying them to both hypotheses avoids systematic bias. [PDF p. 3]
- **Only EER is reported** in the main table (no ROC/DET curves or confidence intervals), although the score is described as supporting an ROC characterisation. [PDF pp. 3–4]
- **A trusted reference is required.** The method cannot verify a wholly synthetic recording with no matching source. [PDF p. 1]

## 6. Related Work

- **Two-hypothesis evidence for explanations.** The likelihood-ratio construction is the same move this repository wants for “graded faithfulness”: score a claim by how much better one explicit hypothesis explains the observations than a stated alternative. See [[concepts/auditable-creative-editing-pipelines]] for the workflow-transparency versus decision-auditability versus faithful-explanation ladder, and [[explainability-and-auditability/wei-2024-do-music-generation-models-encode]] for the probing-side version.
- **Alignment as a localisation device.** AutoMashUpper ([[retrieval-and-recombination/davies-2014-automashupper-automatic-creation-of-multi]]) also exposes a beat-level alignment whose parameters can be inspected; DA-LRT goes further by making the alignment itself the evidence.
- **Adjacent verification work in this repository.** [[explainability-and-auditability/al-2026-tracing-inputs-verifying-outputs-validating]] and [[explainability-and-auditability/al-2026-towards-ai-generated-music-plagiarism]] treat provenance verification for music rather than speech tampering, which is the transfer target for a mashup or repair pipeline.

## 7. Glossary

- **DA-LRT:** Dual Alignment Likelihood Ratio Test.
- **DAPS:** Device and Produced Speech corpus used here for read-speech recordings.
- **EER:** Equal Error Rate, the threshold at which false-accept and false-reject rates are equal.
- **HSTW:** Hidden State Time Warping, a two-state alignment that permits off-diagonal edit steps.
- **LRT:** Likelihood Ratio Test.
- **MFCC:** Mel-Frequency Cepstral Coefficients.
