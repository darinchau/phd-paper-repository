---
title: "On a Separate Note: Robust Score-Informed Note Separation with a Two-Stream TFC-TDF U-Net and Adaptive Set Ownership"
authors: "Benjamin Shiue-Hal Chou et al."
year: 2026
doi: 10.48550/arXiv.2609.29071
category: retrieval-and-recombination
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/al-2026-on-a-separate-note-robust.pdf"
pdf_filename: al-2026-on-a-separate-note-robust.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
---
## One-line Summary

where \(x\) is a monaural mixture and \(s_i\) is the performed waveform of note \(i\). Each aligned score event is

## 1. Document Information

- **Canonical source:** arXiv `2609.29071v1`; official PDF preserved as `al-2026-on-a-separate-note-robust.pdf`.
- **Full-paper evidence:** delegate digest `del_mv41ns1t_0wsb.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### Paper digest

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

Given a local mixture window and \(q_i\), the system estimates the performed waveform of that individual note. For \(K\) concurrent events, it extracts all \(K\) notes and jointly reallocates mixture energy.

The paper’s claimed novelty is the “first deep learning-based” score-informed **note-level** separator; this is an author claim, not independently verified here (pp. 1, 4).

### Method

#### NoteGrab — p. 2, §§2.2–2.3

1. Apply HPSS to the mixture window.
2. Process harmonic and percussive components in separate TFC-TDF v3 U-Nets.
3. The selective variant detects a competing note one or two octaves lower and zeros harmonic energy below:

\[
\max(30, f_0-60)\ \text{Hz}.
\]

The percussive input remains ungated to retain attacks and inharmonic detail.

4. Exchange information through bidirectional cross-attention at three middle stages.
5. Condition pitch, onset, and offset through piano-roll-like feature maps and FiLM layers.
6. Sum harmonic and percussive predictions in the waveform domain.

Each stream is a 27.4M-parameter TFC-TDF U-Net (p. 2, §2.3).

#### Adaptive Set Ownership (ASO) — pp. 2–3, §2.4

ASO operates on a 6-second window containing all notes. It uses nine per-note feature maps:

1. mixture magnitude;
2. estimate/mixture magnitude ratio;
3. estimate’s share of summed estimates;
4. phase similarity;
5. distance to nearest scored harmonic;
6. normalized harmonic index;
7–8. onset and acoustic-offset distances;
9. a learned energy gate.

The network predicts relative log-gains. The paper gives:

\[
w_i=|R_i|G_i e^{d_i},\qquad
A_i=\frac{w_i}{\sum_k w_k},\qquad
S_i=A_iX.
\]

Thus ASO reallocates the observed mixture STFT among competing note estimates. It uses magnitude reallocation rather than complex masks because the authors found this easier to train and superior in the final system.

**Interpretation:** ASO is an explicit, inspectable ownership mechanism: its output says which note receives each time-frequency region. However, the paper does not evaluate whether users can understand or trust these ownership maps.

#### Compute — p. 3, §2.4

For a 2-second, 16-query input on an NVIDIA A10:

- NoteGrab: 1323.8 GMACs, 454.7 ms, 840.1 MiB peak allocation.
- ASO: 14.0 GMACs, 32.7 ms, 828.5 MiB.
- Inference budget: \(K+1\) passes.

For single-note extraction, ASO requires labels for overlapping notes and substantially more than the single NoteGrab pass.

### Data and training

**SCNS-Train (p. 3, §3.1):**

- 25,729 source-complete mixtures.
- 743,920 isolated-note targets.
- Six symbolic datasets plus NSynth and TinySOL recorded-note libraries.

**SCNS-Eval (p. 3, §3.1):**

- 144 disjoint PDMX scores.
- 3,473 scored notes.
- 16 held-out instruments.
- Held-out note libraries.
- No score or audio library shared with training.

Training uses gain, detuning, pitch-shift, echo, room-impulse-response, and colored-noise augmentation. NoteGrab uses 16-kHz audio, 1024-sample STFTs, 128-sample hops, 30,000 steps, batch size 8, AdamW, learning rate \(5\times10^{-5}\), and cosine decay (p. 3, §3.1).

### Results

#### Table 1: SCNS-Eval note separation — p. 3, §3.2

Median SI-SDR, with means in parentheses:

| System | SI-SDR | Off-E | Gain | Oct-Conf |
|---|---:|---:|---:|---:|
| Melodyne 5.4.2 | −3.88 (−4.86) | 0.62 | 0.34 | — |
| Score-Informed NMF | 2.49 (2.27) | 0.25 | 0.82 | — |
| Independent Ungated | 3.94 (3.59) | 0.09 | 0.62 | 8.15% |
| Independent Selective | 4.46 (4.24) | 0.09 | 0.62 | 7.79% |
| NoteGrab Ungated | 4.54 (4.28) | 0.11 | 0.71 | 8.29% |
| NoteGrab Selective | 5.09 (4.87) | 0.12 | 0.72 | 5.19% |
| **NoteSep** | **7.39 (7.35)** | **0.11** | **0.83** | **2.96%** |

The authors report that selective gating improves octave robustness and that ASO provides the largest improvement.

Melodyne is not directly comparable: it does not use the score, matched only 1,890/3,473 notes (54.42%), and obtained −3.88 dB median SI-SDR. On that matched subset, the paper reports 9.24 dB for NoteSep, distinct from the 7.39-dB full-evaluation result.

#### Figure 3 octave-overlap example — p. 4

The A4/A5 piano example shows:

- A4’s second harmonic and A5’s fundamental colliding near 831 Hz.
- A4’s fourth harmonic and A5’s second harmonic colliding near 1.66 kHz.
- ASO reducing both estimates where their raw claims exceed mixture energy.
- Energy moved from A4 toward A5 near 1.66 kHz.
- The paper reports a 5.16-dB SI-SDR improvement for A4.

#### Table 2: editing — p. 4, §3.3

The evaluation contains 13,892 rebalancing, retiming, retuning, and repitching edits.

| System | Pre-edit SI-SDR | Target 2f | Unedited 2f | Final 2f |
|---|---:|---:|---:|---:|
| Score-Informed NMF | 2.49 | 25.73 | 41.77 | 43.40 |
| NoteGrab | 5.09 | 31.70 | 32.87 | 32.38 |
| **NoteSep** | **7.39** | **40.09** | **71.23** | **71.08** |

The authors explicitly note that independently extracted NoteGrab notes degrade when summed because mixture consistency is not enforced. ASO substantially improves both preservation of the unedited material and the final remixed result.

Important evaluation caveat: edits are applied to stored note estimates, and the system does **not** subtract an estimate from the original input mixture (p. 4, §3.3).

#### Table 3: real-recording transfer — p. 4, §3.4

**PHENICX-Anechoic:**

- NoteGrab: SI-SDRi 6.09 dB, SDR −1.32 dB.
- NoteSep: SI-SDRi 8.45 dB, SDR 1.53 dB.

**Bach10:**

- NoteGrab: SI-SDRi 8.75 dB, SDR 5.73 dB.
- NoteSep: SI-SDRi 10.10 dB, SDR 6.83 dB.

NoteSep remains below the task-specific Miron CNN on Bach10 SI-SDRi but exceeds the Miron NMF baseline. The evaluation covers four PHENICX pieces, 38 stems/11,410 note queries, and ten Bach10 quartets.

### Limitations

#### Explicit or directly implied by the paper

- **Requires aligned score events:** pitch, onset, and offset are assumed known (p. 2, §2.1).
- **Monaural formulation:** no multichannel separation is evaluated (p. 2, §2.1).
- **ASO is expensive for one-note extraction:** it needs concurrent-note labels and all-note processing (p. 3, §2.4).
- **Mixture consistency trade-off:** ASO improves joint allocation but deliberately does not guarantee perfect consistency (p. 3, §2.4).
- **Synthetic-to-real gap remains:** SCNS training is synthetic/curated, while real transfer is tested only on PHENICX-Anechoic and Bach10 (p. 4, §3.4).
- **Editing benchmark construction:** edits are applied to ground-truth notes and stored estimates rather than a complete subtract–replace pipeline (p. 4, §3.3).
- **No human listening study:** reported results are SI-SDR, projection/off-target measures, 2f, and SDR.
- **No formal explanation evaluation:** although harmonic gates and ownership maps are inspectable, the paper does not measure explanation fidelity, user comprehension, or causal attribution.

### Artifact status

**Author claim:**

- Code and model weights are stated to be released at `github.com/ben2002chou/notesep` (p. 1 footnote).
- The conclusion says the accompanying artifact provides code, datasets, checkpoints, audio examples, and an interactive note-level visualization (p. 4).
- Demo: `benschou.com/notesep` (pp. 1, 4).

**Evidence boundary:** The PDF establishes that these artifacts are claimed/provided by the authors; it does not give a version, commit, checksum, download instructions, or reproducibility report. I have not treated availability or completeness as independently verified.

### Relevance to the research program

#### Explainable generative music

**Direct contribution:** limited. NoteSep is a discriminative audio separator, not a generative composition model.

**Useful infrastructure:**

- Score events provide an interpretable control interface.
- Harmonic gating gives a transparent rationale for octave disambiguation.
- ASO produces per-note time-frequency ownership, potentially usable as an explanation trace.
- Note-level outputs support localized correction rather than whole-stem regeneration.

**Interpretation:** A generative model could use NoteSep as a source-preserving analysis layer: identify the affected note, preserve all other note estimates, generate only a replacement, and remix through ownership-aware allocation.

#### Source-preserving mashups

The paper is strongly relevant as an audio decomposition component:

1. Obtain aligned note events from each source.
2. Extract individual performed notes with NoteSep.
3. Retime, repitch, rebalance, or transplant selected notes.
4. Recombine through an ownership-aware remixer.

However, the paper does **not** demonstrate cross-song mashups, source identity preservation, beat/key alignment, or perceptual evaluation of transferred material.

#### Repair

The motivation explicitly includes correcting a wrong note (p. 1, Introduction). The method can isolate a suspect note and preserve surrounding notes while replacing or editing it.

The missing component is a complete repair model: NoteSep does not decide what the corrected note should be. That requires score inference, a symbolic repair model, or an instrument-conditioned note synthesizer.

### Concrete research ideas

1. **Explainable score-guided repair loop:** NoteSep → detect/edit one score event → generate a replacement note → ASO remix. Report target-note quality, untouched-material preservation, and explanation faithfulness.
2. **ASO explanations for mashups:** expose ownership masks, competing-note identities, harmonic indices, and onset distances as user-facing evidence for why energy was assigned to a source.
3. **Uncertainty-aware note repair:** propagate uncertainty in transcription, onset, offset, and pitch; compare deterministic NoteSep against multi-hypothesis extraction.
4. **Cross-song source-preserving mashup benchmark:** evaluate note transplantation across instruments, rooms, recording styles, and expressive timing, including human judgments of source identity and edit transparency.
5. **Joint symbolic/audio model:** learn to infer missing or incorrect score events while using NoteSep’s extracted audio as the preservation constraint.
6. **Efficient single-note ASO:** develop a local ownership model that does not require extracting every concurrent note, reducing the paper’s stated single-note compute burden.
7. **Beyond octave collisions:** extend explicit ownership reasoning to fifths, unison notes, sustain-pedal resonance, vibrato, and dense orchestral mixtures.

**Overall assessment:** This paper offers a valuable, technically interpretable separation primitive for note-level editing and repair. Its strongest relevance is as a source-preservation front end for explainable music transformation—not as a generative model itself.

## 3. Methodology and Architecture

The methodology and architecture are preserved in the embedded full-paper digest above, including its original page/section anchors.

## 4. Key Results and Benchmarks

Reported results and benchmark denominators are preserved in the embedded digest above; no unverified reproduction is implied by this record.

## 5. Limitations and Future Work

The evidence limitations, artifact status, and future-work claims are preserved in the embedded digest above. See the batch report for relevance to the explainable symbolic music AI programme.

## 6. Related Work

- [[overviews/2026-symbolic-music-literature-map]] — batch literature map and bidirectional synthesis anchor.

## 7. Glossary

- **Primary category:** `retrieval-and-recombination`. Domain-specific terms are defined in the embedded digest and cross-paper synthesis.
