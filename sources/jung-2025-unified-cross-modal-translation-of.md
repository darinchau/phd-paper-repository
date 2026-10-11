---
title: "Unified Cross-modal Translation of Score Images, Symbolic Music, and Performance Audio"
authors: "Jongmin Jung, Dongmin Kim, Sihun Lee, Seola Cho, Hyungjoon So, Irmak Bukey, Chris Donahue, and Dasaem Jeong"
year: 2025
doi: 10.48550/arXiv.2505.12863
category: data-and-representation
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/jung-2025-unified-cross-modal-translation-of.pdf"
pdf_filename: jung-2025-unified-cross-modal-translation-of.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
---
## One-line Summary

“**Unified Cross-modal Translation of Score Images, Symbolic Music, and Performance Audio**.” arXiv:**2505.12863v1** [cs.SD], **19 May 2025**.

## 1. Document Information

- **Canonical source:** arXiv `2505.12863v1`; official PDF preserved as `jung-2025-unified-cross-modal-translation-of.pdf`.
- **Full-paper evidence:** delegate digest `del_mv40xsw4_v7pn.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### Evidence-grounded digest

### 1. Bibliography and version

**Jongmin Jung, Dongmin Kim, Sihun Lee, Seola Cho, Hyungjoon So, Irmak Bukey, Chris Donahue, and Dasaem Jeong.**  
“**Unified Cross-modal Translation of Score Images, Symbolic Music, and Performance Audio**.” arXiv:**2505.12863v1** [cs.SD], **19 May 2025**.

I inspected the supplied **17-page PDF** and extracted text. The PDF uses an IEEE journal template, but the supplied artifact identifies itself as an arXiv preprint; no accepted-publication metadata is given.

---

### 2. Core contribution

#### Authors’ claim

The paper proposes a unified token-level encoder–decoder Transformer for four modalities:

1. score images,
2. symbolic notation / MusicXML,
3. performance MIDI,
4. performance audio.

The claimed contributions are:

- a single multitask framework for cross-modal music translation;
- the first successful direct score-image-to-performance-audio system;
- the YouTube Score Video (YTSV) dataset;
- multitask improvements to OMR, AMT, MIDI-to-audio, image-to-audio, and audio-to-image tasks.

Anchors: **Abstract, pp. 1–2; Fig. 2, p. 2; Sections III–VIII, pp. 3–10.**

#### Important qualification

Despite the “unified” framing, the experiments train **two separate checkpoints**:

- Image-to-Audio direction (I2A)
- Audio-to-Image direction (A2I)

They do not share weights. The authors explicitly identify training one model for both directions as future work (**Conclusion, p. 10**).

---

### 3. Modalities and token design

#### Modality roles

The paper treats the modalities as a spectrum:

- **Score image:** scanned or rendered notation.
- **Symbolic notation:** Linearized MusicXML (LMX), including pitch, duration, voicing, articulation, slurs, tempo, and dynamics.
- **MIDI:** performance-oriented event representation with onset/offset timing, pitch, velocity, instruments, and timing markers.
- **Audio:** recorded or synthesized performance.

Anchors: **Section II, pp. 2–3; Fig. 3, p. 3.**

#### Image tokens

The authors train a modified **Residual Quantized VAE (RQVAE)**:

- 16× spatial compression;
- four unshared codebooks;
- 1,024 codes per codebook;
- model dimension 256;
- grayscale score images;
- no attention blocks, to emphasize local notation details;
- vertical flattening: top-to-bottom within a column, then left-to-right across columns;
- each token corresponds to approximately a **16×16-pixel** image region.

Preprocessing:

- threshold pixels above median − 20 to white;
- 32 image variants using 8 horizontal and 4 vertical shifts.

Anchors: **Section III-B1, p. 4; Appendix D, pp. 16–17; Fig. 11.**

#### Audio tokens

They retrain **DAC** rather than use the standard nine-codebook model:

- audio resampled to 44.1 kHz and converted to mono;
- hop size 512 samples;
- approximately 86.13 RVQ token sets per second;
- four unshared codebooks;
- 1,024 codes per codebook;
- embedding size 1,024;
- nine temporal-shift variants for augmentation.

Anchor: **Section III-B1, p. 4.**

#### Symbolic tokens

- MusicXML is converted to **Linearized MusicXML (LMX)** using the prior LMX implementation.
- MIDI uses a MIDI-like event representation derived from MT3/YourMT3+:
  - instrument identifiers;
  - pitch;
  - note-on and note-off events;
  - velocity;
  - quantized time markers at 10 ms intervals.

Anchors: **Section III-B2–B3, pp. 3–4.**

#### Unified token space

Each modality has its own vocabulary:

\[
X \in \{I,A,N,M\}
\]

for image, audio, notation, and MIDI.

The global vocabulary includes:

- modality-specific tokens;
- modality-specific `[SOS]` and `[EOS]`;
- `[SEP]` for image boundaries, such as musical systems.

The source embedding is:

\[
e_i =
\mathrm{TokEmb}(z_i^{(X)})
+\mathrm{PosEmb}_X(i)
+\mathrm{TgtEmb}_Y
\]

Thus target modality is explicitly supplied as an embedding.

For image/audio targets, the main decoder emits one timestep representation and a one-layer causal sub-decoder predicts the parallel codebook tokens. Symbolic targets use one token stream. Training uses teacher forcing and cross-entropy.

Anchors: **Section III-C, p. 4; Appendix A, pp. 12–13.**

---

### 4. Architecture and training

#### Main architecture

Final multitask models use:

- 12 encoder layers;
- 12 decoder layers;
- model dimension 1,024;
- feed-forward dimension 4,096;
- GELU activation;
- 16 main attention heads;
- 8 sub-decoder heads.

Image/audio codebook embeddings initialize the corresponding Transformer token embeddings; other parameters are randomly initialized.

#### Optimization

- AdamW;
- initial learning rate \(10^{-4}\);
- cosine decay to \(10^{-5}\);
- 2,000-step linear warm-up;
- 600,000 updates;
- batch size: 24 sequence pairs;
- two NVIDIA H100 SXM GPUs.

For OMR, AMT, and MIDI-to-audio multitask fine-tuning:

- 50,000 steps;
- learning rate \(10^{-5}\).

#### Curriculum

For I2A:

1. OMR from the beginning;
2. MIDI-to-audio after 15,000 steps;
3. direct image-to-audio after 50,000 steps.

For A2I:

1. AMT from the beginning;
2. LMX-to-image after 40,000 steps;
3. audio-to-image after 70,000 steps.

Weighted task sampling prevents the largest dataset from dominating.

Anchors: **Section VI-B, pp. 6–7; Table III, p. 7.**

---

### 5. Dataset and scale

### YouTube Score Video dataset

YTSV contains weakly aligned score-video slides and performance audio.

After filtering:

| Category | Videos | Segments | Hours |
|---|---:|---:|---:|
| Solo piano | 9,052 | 232,029 | 762.34 |
| Accompanied solo | 912 | 47,373 | 141.83 |
| String quartet | 594 | 48,470 | 138.48 |
| Other chamber | 1,659 | 106,048 | 298.65 |
| **Total** | **12,217** | **433,920** | **1,341** |

The collection covers approximately **10,000 pieces** by more than **2,000 composers**.

The alignment is primarily at slide-transition level, not note level. Videos contain page cuts, crossfades, or wipes. The authors use rule-based transition detection, system cropping, and audio slicing.

Filtering excludes or reduces:

- orchestral compositions;
- vocal music;
- larger chamber works;
- works after 2000;
- handwritten or annotated scores;
- poor-quality scans;
- segments outside approximately 3–20 seconds;
- images exceeding 256,000 pixels.

Anchors: **Section IV, pp. 4–6; Table I, p. 5; Fig. 4; Fig. 5.**

The authors use Claude 3.5 Sonnet to extract metadata from video titles, including composer, instrumentation, year, category, and staff count. They fine-tune two YOLOv8-medium models:

- system bounding-box detection: 1,306 labels;
- staff-region detection: 1,254 labels;
- staff height normalized to 18 pixels.

Anchors: **Appendix C, pp. 14–16.**

### Other datasets

| Dataset | Modalities | Entries | Hours |
|---|---|---:|---:|
| YTSV | image/audio | 433,920 | 1,341 |
| GrandStaff | image/LMX | 7,661 | estimated 23 |
| OLiMPiC | image/LMX | 17,945 | estimated 47 |
| MusicNet | MIDI/audio | 330 | 33 |
| MAESTRO | MIDI/audio | 1,276 | 199 |
| SLakh | MIDI/audio | 2,100 | 145 |
| BPSD | image/LMX/MIDI/audio | 32 | 14 |

GrandStaff is augmented to 53,882 notation samples and 107,764 distorted score images. OLiMPiC training uses synthetic images. SLakh is used only as mixed audio.

Anchor: **Section V, pp. 6–7; Table II, p. 6.**

### Directions and subsets

I2A uses:

- piano-only YTSV subset, **YTSV-P**: 252,000 segments, 815 hours;
- MAESTRO for MIDI-to-audio.

A2I uses the full YTSV dataset.

The BPSD test subset contains nine sonatas also present in the MAESTRO test set. These are removed from GrandStaff training. YTSV versions of the same piece are assigned to the same split, and pieces overlapping MAESTRO/MusicNet test sets are assigned to test.

YTSV-T11 is a manually selected test set of **11 pieces by seven composers**.

Anchor: **Section VI-A/C, pp. 6–7; Appendix C-F, p. 16.**

---

### 6. Exact results

### Image-to-audio: Table IV, p. 8

Onset F1 is higher-is-better; FAD is lower-is-better.

| Method | BPSD F1 50/100/200 ms | YTSV-T11 F1 50/100/200 ms | BPSD FAD | YTSV FAD |
|---|---|---|---:|---:|
| Direct I2A, I2A-only | 23.49 / 34.51 / 44.15 | 27.05 / 43.32 / 53.02 | 0.422 | 0.317 |
| Direct I2A, OMR + I2A | 48.67 / 64.30 / 74.01 | 51.60 / 67.92 / 75.98 | 0.098 | 0.056 |
| Direct I2A, OMR + I2A + M2A | 48.36 / 64.63 / 74.92 | 52.66 / 68.45 / 76.24 | 0.081 | 0.055 |
| Multi-stage, same unified model | 50.91 / 70.40 / 79.96 | not reported | 0.137 | not reported |
| Zeus → VirtuosoNet → MSD | 45.52 / 59.35 / 69.36 | not reported | 0.330 | not reported |
| DAC reconstruction upper bound | 68.83 / 82.39 / 87.47 | 82.28 / 86.43 / 88.76 | 0.050 | 0.035 |

#### Interpretation

The multitask model substantially outperforms the image-to-audio-only model. The authors interpret this as evidence that OMR teaches the model to read score content and MIDI-to-audio teaches more natural performance modeling.

The multi-stage explicit-symbolic route gives better note-level F1 than direct I2A but worse FAD. This is directly relevant to intermediate MIDI designs: symbolic intermediates improve measurable note accuracy, but OMR errors—especially accidentals—can cause audible dissonance.

The paper also reports attention maps showing correspondence between image RVQ regions and generated audio tokens (**Fig. 6, p. 9**). This is evidence of learned cross-modal alignment, but not a faithful explanation or causal attribution test.

### Audio-to-image: Table V, p. 9

| Method | Pitch EMD | Duration EMD |
|---|---:|---:|
| Audio-to-image only | 4.6436 | 0.4873 |
| + AMT | 2.8880 | 0.4377 |
| + LMX-to-image | 2.6350 | 0.4317 |
| Ground-truth random-pair baseline | 3.4921 | 0.9936 |
| RQVAE reconstruction | 0.8990 | 0.1301 |
| Ground-truth image | 0.4865 | 0.1113 |

The authors state that A2I outputs are not yet human-readable or performable. Generated pages often have overcrowded staves, misplaced clefs, and other artifacts.

### MIDI-to-audio: Table VI, p. 9

| Method | F1 50 ms | F1 100 ms | F1 200 ms | FAD |
|---|---:|---:|---:|---:|
| MIDI-to-audio only | 26.61 | 64.86 | 88.20 | 0.201 |
| + OMR + I2A | 39.37 | 66.63 | 84.66 | 0.143 |

#### Internal inconsistency

The prose immediately below Table VI reports a different result for the augmented model:

- 45.91 at 50 ms;
- 69.54 at 100 ms;
- 84.55 at 200 ms;
- FAD 0.116.

Those values do not match Table VI’s displayed row. This should be treated as an unresolved reporting inconsistency, not silently reconciled.

### OMR: Table VII, p. 10

SER is lower-is-better.

| Method | OLiMPiC synthetic | OLiMPiC scanned | BPSD scanned |
|---|---:|---:|---:|
| OMR-only | 15.90 | 24.58 | 45.39 |
| + Image-to-audio | 10.57 | 15.45 | 23.85 |
| + MIDI-to-audio | **9.72** | **13.67** | **23.36** |
| Zeus | 10.10 | 14.45 | 31.24 |

The authors claim state-of-the-art OMR performance relative to their comparison, with BPSD SER improving from 45.39 to 23.36.

### AMT: Table VIII, p. 10

| Method | MusicNet strings | MusicNet woodwind | MAESTRO |
|---|---:|---:|---:|
| AMT-only | 87.21 | 72.04 | 89.40 |
| + Audio-to-image | 87.28 | 72.61 | 89.38 |
| + LMX-to-image | 87.25 | 75.52 | 89.45 |
| Maman et al. | 81.8 | **84.2** | 89.7 |

The gains are modest. The authors attribute weaker woodwind performance to the absence of orchestral training data compared with Maman et al.

---

### 7. Evaluation methodology and caveats

- I2A audio is transcribed with Onsets and Frames.
- Reference and generated audio are aligned with dynamic time warping.
- F1 is computed at 50, 100, and 200 ms onset tolerances.
- FAD uses LAION-CLAP embeddings.
- A2I is evaluated indirectly by running Zeus OMR on generated images and comparing pitch/duration-token histograms with EMD.
- OMR uses LMX symbol error rate.
- AMT uses mir_eval note-onset F1.

Important caveats:

1. I2A quality is evaluated through automatic transcription rather than direct human musical judgment.
2. DTW can make timing comparisons more forgiving.
3. A2I EMD evaluates token distributions, not readable engraving, voice correctness, or playability.
4. The DAC reconstruction is an upper bound that exposes codec limitations.
5. There is no listening study, musician evaluation, or systematic human assessment of expressivity.

---

### 8. Limitations, artifacts, and reproducibility

### Explicit author-reported limitations

- AMT improvement is modest.
- A2I images are not practically usable.
- The framework has separate I2A and A2I checkpoints.
- The image and audio codecs limit output quality.
- Sparse slide-level alignment does not provide note-level supervision.
- The current I2A focus is largely piano because multi-timbre audio modeling is difficult.
- OMR errors can create severe musical errors despite small visual differences.

Anchor: **Section VIII, p. 10.**

### Reproducibility

The paper says YTSV metadata, video links, and preprocessing code **will be released upon acceptance** (**footnote 1, p. 5**). In the supplied paper:

- no code repository is identified;
- no trained checkpoint URL is supplied;
- no dataset license is specified;
- no explicit license for the YTSV collection is specified;
- the source material is derived from YouTube videos, so redistribution and copyright status require independent verification;
- the demo page is given as `https://sakem.in/u-must/`.

These are artifact/reproducibility limitations, not necessarily evidence that the authors never released anything later.

---

### 9. Relevance to explicit MIDI intermediates and explainable symbolic mashups/repair

### Strong relevance

This paper provides a useful empirical comparison between:

1. **direct image → audio**, and
2. **image → MusicXML → MIDI → audio**.

The explicit intermediate route achieves higher note-level F1 but worse perceptual FAD. This suggests a real design trade-off:

- explicit symbolic representations improve inspectability and pitch/timing control;
- symbolic errors can propagate catastrophically into audio;
- direct generation may conceal errors and produce better perceptual smoothing;
- neither route alone guarantees musical correctness.

For an explainable system, MIDI should not merely be an internal token stream. It should be exposed as:

- editable notes and voices;
- aligned provenance to source score regions;
- uncertainty or alternative hypotheses;
- constraints and repair operations;
- auditable transformations before rendering audio.

### What the paper does not address

It does not perform symbolic mashups or repair. There is:

- one source rather than two;
- no alignment between source A and source B;
- no conflict diagnosis;
- no minimal repair;
- no protected source material;
- no provenance graph;
- no explanation-faithfulness evaluation;
- no musician control interface.

Therefore, the paper is best viewed as **cross-modal infrastructure**, not a mashup or repair method.

---

### 10. Concrete research ideas

1. **MIDI-centered unified model**  
   Make MIDI/LMX an explicit hub rather than only one task among many. Compare direct image→audio against image→MIDI→performance and retain n-best symbolic hypotheses.

2. **Conflict-aware symbolic mashup benchmark**  
   Pair two MIDI sources and annotate:
   - incompatible pitches;
   - rhythmic conflicts;
   - voice-crossing;
   - register collisions;
   - cadence/form conflicts;
   - repair severity.

3. **Provenance-preserving repair**  
   Attach every generated or modified note to:
   - source A;
   - source B;
   - inferred bridge material;
   - repair operation;
   - musical rationale.

4. **Counterfactual repair evaluation**  
   For each conflict, compare:
   - unmodified overlay;
   - minimal repair;
   - aggressive transformation;
   - human reference repair.

   Evaluate source identity, compatibility, coherence, novelty, playability, and explanation faithfulness separately.

5. **Audio-aware symbolic repair**  
   Use the paper’s observation that visually small OMR errors can sound catastrophic. Train a repair objective that combines:
   - symbolic legality;
   - harmonic/voice-leading constraints;
   - rendered-audio perceptual loss;
   - source-identity preservation.

6. **Uncertainty-aware cascades**  
   Propagate OMR uncertainty into MIDI and audio. Avoid committing to one accidental, duration, or voice when several symbolic hypotheses remain plausible.

7. **Note-level YTSV alignment**  
   Use self-supervised audio–score alignment to refine YTSV’s slide-level supervision into measure- or note-level alignments, as proposed by the authors.

8. **Explanation faithfulness tests**  
   Replace attention visualization alone with interventions:
   - mask the claimed explanatory score region;
   - alter the claimed source note;
   - test whether generated audio changes accordingly;
   - compare against non-attended regions.

9. **One shared bidirectional model**  
   Test the authors’ proposed decoder-only or fully shared model, but preserve modality-specific output heads and explicit symbolic checkpoints for auditability.

10. **Human evaluation focused on musicianship**  
    Add musician ratings for:
    - recognizable source contributions;
    - musical coherence;
    - repair necessity;
    - playability;
    - usefulness of explanations;
    - control over protected material.

**Overall assessment:** the paper demonstrates that shared training across image, symbolic, MIDI, and audio representations can materially improve cross-modal music tasks. Its most important implication for your research is not direct score-to-audio generation itself, but the empirical evidence that an explicit symbolic path improves inspectability and note accuracy while introducing error propagation. That trade-off is an excellent foundation for provenance-preserving, conflict-aware symbolic mashup and repair systems.

## 3. Methodology and Architecture

The methodology and architecture are preserved in the embedded full-paper digest above, including its original page/section anchors.

## 4. Key Results and Benchmarks

Reported results and benchmark denominators are preserved in the embedded digest above; no unverified reproduction is implied by this record.

## 5. Limitations and Future Work

The evidence limitations, artifact status, and future-work claims are preserved in the embedded digest above. See the batch report for relevance to the explainable symbolic music AI programme.

## 6. Related Work

- [[overviews/2026-symbolic-music-literature-map]] — batch literature map and bidirectional synthesis anchor.

## 7. Glossary

- **Primary category:** `data-and-representation`. Domain-specific terms are defined in the embedded digest and cross-paper synthesis.
