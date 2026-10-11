---
title: "VMAS: Video-to-Music Generation via Semantic Alignment in Web Music Videos"
authors: "Yan-Bo Lin, Yu Tian, Linjie Yang, Gedas Bertasius, and Heng Wang"
year: 2024
doi: 10.48550/arXiv.2409.07450
category: generation-and-planning
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/lin-2024-vmas-video-to-music-generation.pdf"
pdf_filename: lin-2024-vmas-video-to-music-generation.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
---
## One-line Summary

The supplied PDF is the v1 manuscript. The project page identifies the work as a **WACV 2025 Oral** paper and provides qualitative demo videos.

## 1. Document Information

- **Canonical source:** arXiv `2409.07450v1`; official PDF preserved as `lin-2024-vmas-video-to-music-generation.pdf`.
- **Full-paper evidence:** delegate digest `del_mv40xsw4_ltcj.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### VMAS digest

### 1. Bibliography and version

**Paper:** Yan-Bo Lin, Yu Tian, Linjie Yang, Gedas Bertasius, Heng Wang, “VMAS: Video-to-Music Generation via Semantic Alignment in Web Music Videos,” arXiv:2409.07450v1 [cs.MM], 11 September 2024.

The supplied PDF is the v1 manuscript. The project page identifies the work as a **WACV 2025 Oral** paper and provides qualitative demo videos.

**Primary sources inspected:** all pages of `/tmp/paper-digest/2409.07450v1.pdf` and the extracted text `/tmp/paper-digest/2409.07450v1.txt`, including Tables 1–7, Figures 1–8, appendices, and references.

---

### 2. Core contribution

**Author claim:** VMAS generates instrumental background music directly from video, avoiding the small, narrow MIDI datasets used by earlier video-to-music systems.

The system combines:

1. A temporally efficient video encoder.
2. An autoregressive EnCodec-token music decoder.
3. A global video–music contrastive objective.
4. A local video-beat alignment objective based on optical flow and onset detection.

The stated goal is simultaneous alignment with:

- **High-level semantics:** genre, style, and overall content.
- **Low-level dynamics:** scene changes, human motion, and other visually salient moments.

**Interpretation:** VMAS is not merely video-conditioned music generation. It explicitly introduces intermediate alignment signals that could be exposed as controls or explanations.

---

### 3. Dataset: DISCO-MV

#### Dataset statistics

**PDF p. 1, Table 1; p. 3, §3**

| Dataset | Videos | Mean within-video frame similarity |
|---|---:|---:|
| SymMV | 1.1K | 0.64 |
| YouTube-8M subset | 110K | 0.66 |
| DISCO-10M | 15.3M | 0.91 |
| **DISCO-MV** | **2.2M** | **0.61** |

The paper describes DISCO-MV as **2.28M video–music samples spanning approximately 47,000 hours**. It also combines 81K video–music samples from YouTube-8M.

Evaluation splits were manually selected for strong video–music correspondence:

- Validation: **1,120 videos**
- Test: **1,086 videos**

#### Construction

**PDF p. 3, §3**

1. Start from DISCO-10M, built from YouTube videos matched to Spotify artist metadata.
2. Remove visually static or repetitive videos using pairwise frame similarity.
3. Retain videos with intra-video similarity below **0.7**.
4. Apply Demucs vocal separation; the authors report successful vocal removal for approximately **95%** of soundtracks.
5. Add YouTube-8M samples.

**Author claim:** filtering is essential because unfiltered DISCO-10M contains long clips with a single repeated frame or very little visual variation.

#### Genre analysis

**PDF p. 10, Appendix D, Figure 5**

Genres are assigned using zero-shot CLAP embeddings and GTZAN genre prompts. Jazz and disco are predominant; blues is underrepresented because it is scarce in the source DISCO-10M data.

**Interpretation:** DISCO-MV is much larger than prior datasets, but its distribution is not neutral. Genre imbalance and source-derived biases matter for symbolic generation and repair.

---

### 4. Model and training details

#### Audio representation

**PDF p. 4, §4.1; p. 10, Appendix B**

- Audio length: **10 seconds**
- Sampling rate: **32 kHz**
- Codec: pretrained **EnCodec**
- EnCodec stride: **640**
- Token frame rate: **50 Hz**
- Four residual-vector-quantization codebooks
- Codebook size: **2,048**
- Delay-interleaving pattern
- Approximately **500 autoregressive audio-token steps** per 10-second clip

The model predicts EnCodec tokens rather than symbolic notes or MIDI.

#### Video representation

**PDF p. 4, Table 2 and §4.2; p. 10, Appendix B**

- **96 frames**
- **9.6 FPS**
- Input resolution: **224 × 224**
- 3D convolution:
  - Kernel: `[3 × 7 × 7]`
  - Stride: `[2 × 4 × 4]`
  - Padding: `[1 × 3 × 3]`
- Backbone: Hiera-Base, 24 layers
- Modified Q-Pooling:
  - Layer 2: spatial stride increased from 2 to 4
  - Layer 5: spatial stride increased from 2 to 7
  - Layer 21: standard spatial downsampling
- Final representation: approximately `48 × 1 × 1 × 768`

**Author claim:** the modified encoder processes many densely sampled frames more efficiently than standard encoders while retaining fine temporal information.

#### Autoregressive decoder

**PDF p. 4, §4.3; p. 10, Appendix B**

The decoder uses alternating causal self-attention and video-conditioned multi-head attention. Video features are supplied as keys and values to every decoder layer.

Appendix details:

- MusicGen-medium autoregressive decoder
- **48 transformer layers**
- Feature dimension: **1,536**
- Decoder predicts EnCodec-token categories

#### Global semantic alignment

**PDF p. 5, §4.4**

Predicted audio-token logits are mapped through the EnCodec embedding matrix:

`M = ŶE`

The model mean-pools video features and music embeddings, then applies a batchwise cosine-similarity contrastive loss:

`Lc = -1/B Σi log exp(g(vᵢ,mᵢ)) / Σj exp(g(vᵢ,mⱼ))`

This encourages the generated music to match the video globally.

#### Local video-beat alignment

**PDF p. 5, Figure 2 and §4.4**

1. Detect music onsets using an off-the-shelf onset detector.
2. Compute optical flow between consecutive video frames.
3. Spatially average flow magnitude.
4. Mark local maxima as “video beats.”
5. Mark a timestep as an overlapping video–music beat if a detected music beat occurs within a local temporal window.
6. Use the resulting mask as an importance weight for token-level cross-entropy.

The weighted autoregressive loss is:

`Lg = -Σᵢ P_av[i] Σc Yᵢ,c log(Ŷᵢ,c)`

The overall loss is:

`L = Lc + λLg`

Appendix B reports:

- Local alignment parameter in Eq. (3): **0.05**
- Main loss-balancing parameter λ: **0.25**

**Interpretation:** the beat mechanism is a weakly supervised pseudo-labeling system. It does not know musical structure directly; it assumes that optical-flow peaks and detected onsets should coincide.

#### Optimization

**PDF p. 10, Appendix B**

- Optimizer: AdamW
- Batch size: **8 per GPU**
- Hardware: **32 NVIDIA GPUs across four nodes**
- Approximately **four days** of training
- D-Adaptation for automatic learning-rate selection
- Cosine learning-rate schedule
- Warmup: **4,000 steps**
- EMA decay: **0.99**
- Training clips: 10 seconds

---

### 5. Evaluation and baselines

#### Datasets and metrics

**PDF p. 6, §5.1–§5.2**

MusicCaps test set:

- **2,858** ten-second video–music samples
- Captions written by professional musicians

Metrics:

- **FAD:** VGGish feature-distribution distance
- **KL:** genre-distribution divergence using a Million Song Dataset classifier
- **MV Align:** synchronization between music beats and visual dynamics

Baselines:

- CMT
- Video2Music
- VidMusicGen
- Vid2MLDM
- V2Meow

The authors note that V2Meow code and checkpoints were unavailable.

#### Main quantitative results

**PDF p. 6, Table 3**

| Method | MusicCaps FAD | KL | MV Align | DISCO-MV FAD | KL | MV Align |
|---|---:|---:|---:|---:|---:|---:|
| CMT | 16.20 | 1.42 | 0.18 | 3.70 | 1.82 | 0.34 |
| Video2Music | 24.70 | 1.35 | 0.19 | 4.36 | 1.93 | 0.29 |
| VidMusicGen | 6.91 | 1.26 | 0.17 | 2.93 | 1.60 | 0.25 |
| Vid2MLDM | 8.99 | 1.15 | 0.20 | 3.21 | 1.41 | 0.32 |
| V2Meow | 4.62 | — | — | — | — | — |
| **VMAS** | **4.07** | **1.09** | **0.22** | **2.38** | **1.34** | **0.35** |

The authors claim VMAS outperforms prior methods on all reported metrics. V2Meow is only directly comparable on MusicCaps FAD because its other artifacts were unavailable.

#### Same-data comparison with V2Meow

**PDF p. 7, Table 4**

Using the 100K-video MV100K training set:

| Method | Training data | FAD | KL |
|---|---|---:|---:|
| V2Meow | MV100K | 4.62 | 1.22 |
| VMAS | MV100K | 4.51 | 1.15 |
| VMAS | DISCO-MV, 2.2M | 4.07 | 1.10 |

**Author claim:** both the architecture/alignment design and scaling to DISCO-MV contribute materially.

#### Alignment ablation

**PDF p. 8, Table 5**

| Configuration | FAD | KL | MV Align |
|---|---:|---:|---:|
| Autoregressive baseline | 2.75 | 1.40 | 0.243 |
| + video–music contrastive loss | 2.40 | 1.34 | 0.251 |
| + video-beat alignment | 2.38 | 1.34 | 0.352 |

The contrastive objective mainly improves FAD/KL. The beat objective produces the largest MV Align improvement.

#### Encoder comparison

**PDF p. 8, Table 6**

| Encoder | Frames | FAD | KL | MV Align | GFLOPS |
|---|---:|---:|---:|---:|---:|
| CLIP | 16 | 2.61 | 1.41 | 0.274 | 281.6 |
| Hiera | 16 | 2.58 | 1.41 | 0.316 | 140.2 |
| **VMAS encoder** | **96** | **2.38** | **1.34** | **0.342** | **130.7** |

#### Data-cleaning ablation

**PDF p. 8, §6.2**

Unfiltered DISCO-10M:

- FAD: 4.52
- KL: 2.11
- MV Align: 0.18

Filtered DISCO-MV:

- FAD: 2.38
- KL: 1.34
- MV Align: 0.35

#### Retrieval evaluation

**PDF p. 11, Appendix E, Table 7**

Using 2,000 DISCO-MV test videos:

| Model/encoder | Frames | R@1 | R@10 |
|---|---:|---:|---:|
| MVPt + CLIP | 16 | 4.2 | 17.3 |
| MVPt + Hiera | 16 | 4.8 | 18.1 |
| VMAS | 96 | 6.3 | 26.7 |

---

### 6. Human evaluation

**PDF p. 7, Figure 3; p. 9, Figure 4; p. 11, Appendix C**

Approximately **200 Amazon Mechanical Turk subjects** compared VMAS against CMT, Video2Music, VidMusicGen, and Vid2MLDM.

Prompts:

1. Which sample has better overall music quality?
2. Which sample has better synchronization between music beats and visual dynamics?

Responses:

- Method A better
- Cannot tell
- Method B better

The paper reports:

- VMAS preferred **over 70%** of the time for overall music quality.
- VMAS preferred **67%** of the time for music–video alignment.

The comparisons were pairwise, randomized, and methods were hidden from raters. The paper does not provide a numerical table of every bar in Figure 3, confidence intervals, inter-rater reliability, or raw responses.

**Interpretation:** this supports perceptual superiority, but not necessarily causal alignment correctness. Pairwise preference is also vulnerable to presentation effects and does not establish note-level or beat-level accuracy.

---

### 7. Appendix findings

- **Appendix B:** detailed EnCodec, Hiera, decoder, and optimization settings.
- **Appendix C:** human-evaluation interface and protocol.
- **Appendix D:** CLAP/GTZAN genre analysis; jazz and disco dominate, blues is sparse.
- **Appendix E:** performance improves as training data increases from 10%, 25%, 50%, to 100%.
- **Appendix F, Figure 8:** qualitative spectrogram comparison. The authors highlight a surfer’s sharp turn where VMAS produces a stronger beat; competing systems often produce more uniform beat intensity.
- **Appendix A:** summarizes the supplementary material.
- The paper states that future work includes video–music style transfer, editing, and retrieval.

---

### 8. Limitations and reproducibility

#### Explicit or directly evidenced limitations

1. **Web-data quality:** source videos contain static frames, weak correspondence, genre imbalance, and possible metadata noise.
2. **Vocal-removal imperfection:** Demucs succeeds for approximately 95%, not all, soundtracks.
3. **Baseline incomparability:** V2Meow code/checkpoints were unavailable; some comparisons rely on reported numbers.
4. **Human evaluation limitations:** approximately 200 MTurk raters, pairwise preferences, no published raw responses or uncertainty estimates.
5. **Metric limitations:** FAD, KL, and MV Align do not measure musical form, harmonic correctness, symbolic editability, or long-range structure.
6. **Data-selection bias:** validation/test videos were manually selected for high correspondence and may not represent deployment data.

#### Artifact status

The project page contains:

- Paper link.
- Qualitative MP4 demonstrations for CMT, Vid2MLDM, Video2Music, VidMusicGen, and VMAS.
- WACV 2025 Oral designation.

The page has **no active code, checkpoint, or dataset-download link**. Its code button is commented out; the commented URL points to `GenjiB/LAVISH`, not an evident VMAS release.

#### Rights and licensing

**Author claim:** DISCO-MV is built from publicly available YouTube-8M and DISCO-10M data and “will be available” under **CC-BY-4.0**, matching the source datasets as described in Table 1.

Reproducibility caveat: the paper does not provide a manifest, hashes, precise video identifiers, filtering logs, or a working dataset release. A CC-BY statement does not by itself resolve all platform terms, third-party music rights, derivative-work issues, or redistribution rights for downloaded media.

---

### 9. Relevance to symbolic mashup and repair

#### Useful condition signals

VMAS supplies a useful hierarchy of multimodal signals:

- **Global semantic embedding:** video genre/style/content compatibility.
- **Dense temporal representation:** 96-frame, high-FPS visual context.
- **Optical-flow peaks:** visually salient motion events.
- **Onset detections:** musical rhythmic events.
- **Overlap mask:** explicit candidate alignment points.
- **Cross-attention:** temporal conditioning of music generation on video features.

These are more actionable for explainable symbolic systems than a single opaque video embedding.

#### Important mismatch

VMAS generates EnCodec audio tokens, not MIDI or event tokens. It therefore does not directly support:

- Note-level editing.
- Chord repair.
- Instrument-aware mashup.
- Exact bar/beat quantization.
- Symbolic provenance.
- Guaranteed preservation of musical constraints.

#### Explainability assessment

**Author-supported:** the model has interpretable alignment components and visualizations.

**Interpretation:** the system is not fully explainable in the causal sense. Optical-flow maxima are only proxies for musical importance; global mean pooling can hide local semantics; and the learned decoder may use cues not represented by the reported masks.

---

### 10. Concrete research ideas

1. **Symbolic VMAS decoder:** retain the global contrastive and local beat objectives, but decode MIDI/event tokens with explicit bar, beat, chord, and instrument channels.

2. **Explainable repair masks:** convert optical-flow peaks and detected audio onsets into beat-grid constraints. Output each repair with provenance such as “scene transition at 3.2 s increased beat probability.”

3. **Video-conditioned mashup retrieval:** use the global embedding to retrieve compatible MIDI/stem candidates, then use local beat masks for segment-level alignment.

4. **Differentiable beat alignment:** replace the binary `P_av` mask with soft alignment via differentiable dynamic time warping or optimal transport between visual events and symbolic beats.

5. **Counterfactual controls:** allow users to suppress or emphasize specific visual events and test whether generated symbolic changes are localized and predictable.

6. **Structure-aware objectives:** add downbeat, phrase-boundary, chord-transition, and repetition losses so that visual alignment does not damage musical form.

7. **Rights-safe benchmark:** create a reproducible dataset with stable identifiers, license metadata, source splits, genre balancing, and train/test separation by artist or video source.

8. **Better evaluation:** supplement FAD/KL/MV Align with beat F1, downbeat accuracy, note-edit distance, chord consistency, instrument preservation, repair success rate, and explanation faithfulness.

Overall, VMAS is highly relevant as a blueprint for **hierarchical multimodal conditioning**, but symbolic mashup/repair would need to replace its waveform-token output with structured music representations and make its alignment signals explicit user controls.

## 3. Methodology and Architecture

The methodology and architecture are preserved in the embedded full-paper digest above, including its original page/section anchors.

## 4. Key Results and Benchmarks

Reported results and benchmark denominators are preserved in the embedded digest above; no unverified reproduction is implied by this record.

## 5. Limitations and Future Work

The evidence limitations, artifact status, and future-work claims are preserved in the embedded digest above. See the batch report for relevance to the explainable symbolic music AI programme.

## 6. Related Work

- [[overviews/2026-symbolic-music-literature-map]] — batch literature map and bidirectional synthesis anchor.

## 7. Glossary

- **Primary category:** `generation-and-planning`. Domain-specific terms are defined in the embedded digest and cross-paper synthesis.
