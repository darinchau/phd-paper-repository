---
title: "Synthesis and Editing of Multi-Instrument Audio Mixtures Using Scalar-Quantised Latents with MIDI Span Conditioning"
authors: "Sungkyun Chang, Keshav Bhandari, Simon Dixon, and Emmanouil Benetos"
year: 2026
doi: 10.48550/arXiv.2609.25546
category: retrieval-and-recombination
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/chang-2026-synthesis-and-editing-of-multi.pdf"
pdf_filename: chang-2026-synthesis-and-editing-of-multi.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
---
## One-line Summary

The authors introduce **SpanSynth-Edit**, a flow-matching model that synthesises or edits a selected region of a mono multi-instrument mixture from revised MIDI.

## 1. Document Information

- **Canonical source:** arXiv `2609.25546v1`; official PDF preserved as `chang-2026-synthesis-and-editing-of-multi.pdf`.
- **Full-paper evidence:** delegate digest `del_mv41492q_d4if.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### Evidence-grounded digest

**Paper reviewed:** arXiv:2609.25546v1, *Synthesis and Editing of Multi-Instrument Audio Mixtures Using Scalar-Quantised Latents with MIDI Span Conditioning*. I reviewed the extracted text and all 13 PDF pages, including appendices and references.

### 1. Core contribution

The authors introduce **SpanSynth-Edit**, a flow-matching model that synthesises or edits a selected region of a mono multi-instrument mixture from revised MIDI.

The central design is:

1. Encode observed audio into low-rate scalar-quantised latents.
2. Keep contextual audio latents fixed.
3. Represent MIDI notes as frame-aligned lifecycle events with continuous timing attributes.
4. Generate only the target region with a large diffusion transformer.
5. Decode the edited latent sequence back to audio.

The authors claim this supports adding, deleting, or changing notes while retaining surrounding audio and timbres. This is an author claim; the experiments measure preservation indirectly through audio similarity and transcription-derived metrics rather than source-level separation or attribution.  
**Anchor:** PDF pp. 1–2, Abstract, §1–§2.

---

### 2. Audio representation and SQ model

#### Frozen scalar-quantised codec

This is not a newly trained SQ-VAE in the paper. The model uses a **frozen HeartCodec encoder and decoder**:

- Input: 48-kHz mono audio.
- Latent dimension: 128 channels.
- Frame rate: 25 Hz.
- Hop: 40 ms.
- Encoder output bounded by `tanh`.
- Coordinate-wise quantisation:

\[
Q(x)=\operatorname{round}(9x)/9
\]

This produces **19 values in \([-1,1]\)**. The generated latent sequence is clipped and requantised before decoding:

\[
\hat y=D_{\mathrm{SQ}}\left(Q(\operatorname{clip}(Z,-1,1))\right).
\]

For a 20.48-second crop, the stored representation is **512 × 128 signed 8-bit SQ codes**, after discarding the codec’s first 50 latent frames.  
**Anchors:** PDF p. 2, §2.1; Appendix A, PDF p. 6.

#### Context masking

Two masks identify:

- observed versus target audio frames;
- availability of contextual MIDI.

The clean observed audio condition is:

\[
A=b_{\mathrm{obs}}\odot Z.
\]

Observed audio enters the model without additional noise and is held fixed during inference.  
**Anchor:** PDF p. 2, §2.1, Eq. (1), Fig. 1(a).

#### Generator

The generator is:

- **480.8 million parameters**, codec excluded;
- a **25-block DiT**;
- transformer width: **1,024**;
- conditional flow matching;
- 32 Euler steps in the principal experiments;
- classifier-free guidance scale 2.

The transformer predicts the vector field from noisy latents conditioned on clean audio context, MIDI Span features, and masks. Training minimizes MSE on target frames.  
**Anchor:** PDF p. 2, §2.3; PDF p. 3, §3.1.

The model is therefore a **flow-matching transformer over scalar-quantised continuous latents**, not a discrete codec-token autoregressive transformer.

---

### 3. MIDI Span conditioning

#### Event representation

Each non-drum MIDI note is represented in every audio frame that it overlaps:

- `ONSET` in the onset frame;
- `SUSTAIN` between boundaries;
- `OFFSET` in the offset frame.

If onset and offset occur inside the same frame, only `ONSET` is retained. Drum hits are represented as a single onset event.

Each event contains:

- categorical state;
- instrument class;
- pitch;
- velocity;
- within-frame boundary position;
- remaining duration.

The within-frame boundary is:

\[
x_{\mathrm{boundary}} =
2(t_{\mathrm{event}}-t_k)/H-1.
\]

Thus MIDI timing is not restricted to the 40-ms audio-latent grid. Onsets at shared frame boundaries are assigned to the later frame; offsets to the earlier frame.  
**Anchor:** PDF p. 2, §2.2, Eq. (2), Fig. 1(b).

#### Permutation-invariant pooling

Events in each frame form an unordered set, padded to **128 slots**. A shared encoder maps events to 128-dimensional vectors. Deep-Sets-style pooling concatenates:

- one ordinary sum;
- five learned sigmoid-gated sums;
- RMS normalisation;
- projected log-count features for melodic and drum events.

The resulting per-frame MIDI condition is:

\[
m_k\in\mathbb{R}^{768}.
\]

Slot-index embeddings are omitted, so note ordering should not affect the representation. Empty sets become zero vectors.  
**Anchor:** PDF p. 2, §2.2.

#### Editing mechanism

Editing resynthesises both changed and unchanged notes in the target region from the revised MIDI. It does **not** copy unchanged target notes directly from the source audio.

The optional FlowEdit variant compares:

- the before-edit latent sequence and MIDI;
- the revised MIDI and current edited sequence.

It updates only target frames while preserving observed SQ codes.  
**Anchor:** PDF p. 3, §2.3.

---

### 4. Datasets and experimental design

#### Training

The authors report:

- **660 hours** of performance MIDI paired with 48-kHz mono audio;
- 17 public instrumental dataset families;
- 15 datasets containing real recordings;
- Adam;
- 125k training steps;
- effective batch size 80;
- peak learning rate \(10^{-4}\), with linear warmup and decay.

Training data include Slakh, AAM, MAESTRO, PianoVAM, MusicNetEM, BSD/BSED, GOAT, GuitarSet, URMP, IDMT-SMT-Bass, KRAISLER, ChoraleBricks, FiloBass, MDB Drums, EGSet12, ENST-Drums, and STAR Drums.  
**Anchors:** PDF p. 3, §3.1; Appendix A, PDF p. 6.

Augmentation combines a base arrangement with up to two additional recordings. Requested additions occur with probabilities 50%, 35%, and 15% for zero, one, and two additions. Drum-free material receives ±1 or ±2 semitone pitch shifts with corresponding MIDI transposition.  
**Anchor:** Appendix A, PDF p. 6.

#### Editing benchmarks

- **Slakh:** 668 original/revised pairs.
  - New-instrument additions.
  - Note insertion/deletion.
  - Track deletion.
  - With- and without-drums conditions.
- **POP909:** 147 songs × 3 edit durations × 2 rendering conditions = **882 pairs**.
  - MIDI revisions come from the external Modulator system.
  - Audio is rendered using the Salamander piano SoundFont.
  - Half dry and half matched-reverberation.

**Anchors:** PDF p. 3, §3.1; Appendix C, PDF pp. 10–11.

#### Metrics

Audio quality:

- MuQ-Eval;
- Audiobox Production Quality;
- MERT-based FAD.

Audio similarity:

- MuQ cosine similarity;
- CLAP cosine similarity;
- Smooth MSS spectral error.

MIDI adherence is measured by running **YourMT3+** on generated audio:

- `FOn`: instrument-agnostic onset F1;
- `FP37` and `FP13`: fine/coarse instrument-labelled onset F1;
- `Radd`: requested additions detected;
- `Rdel`: deleted notes still detected;
- `Fkeep`: unchanged notes retained;
- `FOpenMIC`: instrument-presence F1.

This is an important methodological limitation: most note-adherence numbers are properties of **audio → transcription → comparison**, not direct measurements of the generated waveform’s symbolic correctness.  
**Anchor:** PDF p. 3, §3.1.

---

### 5. Principal synthesis results

The authors report that SpanSynth-Edit matches or exceeds baselines on most audio-quality and similarity metrics, except for MAESTRO PQ and FAD, where MIDI-VALLE and U-MusT respectively lead.

Selected Table 1 results:

| Dataset | MuQ-Eval | PQ | FAD | MuQ cosine | CLAP cosine | FOn | FP37 | FP13 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Slakh | 4.67 | 8.02 | 1.41 | .89 | .86 | 50.88 | 29.57 | 37.61 |
| Slakh + drums | 4.65 | 8.08 | 1.33 | .89 | .90 | 54.06 | 37.78 | 44.84 |
| MusicNetEM | 4.75 | 7.60 | 3.15 | .92 | .87 | 76.56 | 71.94 | 74.69 |
| URMP | 4.82 | 7.90 | 4.95 | .91 | .83 | 54.24 | 37.85 | 47.90 |
| GuitarSet | 4.14 | 8.40 | 4.05 | .92 | .91 | 88.01 | — | — |
| MAESTRO Piano V3 | 4.61 | 7.50 | 2.89 | .96 | .86 | 76.49 | — | — |

The paper states that FOn exceeds the strongest reported baseline in each Table 1 group by **2.22–9.86 percentage points**, although instrument-labelled gains are less consistent. On Slakh with drums, SpanSynth-Edit beats SpecDiff on FP13 but trails it on FP37.  
**Anchors:** PDF p. 3, Table 1, §3.2; Appendix B, PDF pp. 7–9.

---

### 6. Editing results

The model generally provides strong audio similarity and `Fkeep`, but deletion adherence is weaker.

Selected results:

#### Slakh, no drums: note insertion/deletion

| Model | Radd | Rdel | Fkeep |
|---|---:|---:|---:|
| CTD | 43.20 | 3.82 | 28.91 |
| Ours | 42.51 | 6.08 | 33.24 |
| Ours + FlowEdit | 43.49 | 8.01 | 35.75 |

#### Slakh with drums: note insertion/deletion

| Model | Radd | Rdel | Fkeep |
|---|---:|---:|---:|
| SpecDiff | 52.64 | 2.62 | 39.19 |
| U-MusT | 20.50 | 3.72 | 9.56 |
| Ours | 56.44 | 4.56 | 41.90 |
| Ours + FlowEdit | 50.54 | 7.78 | 41.55 |

#### POP909 AI edits

| Model | Radd | Rdel | Fkeep |
|---|---:|---:|---:|
| MIDI-VALLE | 72.74 | 4.86 | 10.41 |
| Ours | 89.86 | 3.40 | 13.84 |
| Ours + FlowEdit | 86.81 | 5.06 | 12.46 |

The authors’ interpretation is:

- ordinary SpanSynth-Edit often gives the best MuQ-Eval and PQ;
- FlowEdit gives the best FAD and MSS;
- the model or FlowEdit variant gives the best `Radd`/`Fkeep` in each editing group;
- deletion retention (`Rdel`) remains worse than selected baselines;
- FlowEdit improves deletion behavior but often reduces addition recall.

**Anchors:** PDF p. 4, Table 2, §3.2; Appendix C, PDF pp. 10–11.

---

### 7. Error analysis and ablations

#### Transcription and codec error

On Slakh with drums, synthesis adherence degrades substantially before generation:

- perfect AMT control: FP37/FOn = 100/100;
- ground truth audio transcribed by YourMT3+: 78.40/82.79;
- continuous codec reconstruction: 44.43/55.94;
- SQ reconstruction: 43.98/55.79;
- generated audio: 37.78/54.06.

For new-instrument editing, perfect control is 100/100, while ground-truth audio transcribed by YourMT3+ falls to 71.40/72.80.

The authors attribute the largest losses to transcription and reconstruction, not scalar quantisation:

- YourMT3+ causes a 21.60-point FP37 loss in synthesis;
- reconstruction without SQ causes a further 33.97-point loss;
- scalar quantisation adds only 0.45 points in the synthesis analysis;
- generation adds a smaller residual loss.

They suggest the codec’s pretraining distribution may mismatch the training audio and motivate decoder fine-tuning.  
**Anchor:** PDF p. 4, Table 3, §3.3; Appendix D, PDF p. 12.

#### Timing sensitivity

The authors delay MIDI onsets by 1–40 ms and compare harmonic-energy or drum-onset cross-correlations.

Findings:

- weak sensitivity to 1–5 ms shifts, possibly because of annotation error;
- clearer response from 10–40 ms;
- weak measured response for strings and pipe instruments.

This demonstrates that MIDI Span carries sub-frame timing information, but it does not establish uniformly reliable sample-accurate onset control.  
**Anchor:** PDF p. 4, Fig. 2, §3.3.

#### Inference-time ablations

On 56 target intervals:

| Setting | MuQ-Eval | FAD | FOn |
|---|---:|---:|---:|
| 4 steps | 4.48 | 3.65 | 74.60 |
| 8 steps | 4.46 | 3.29 | 76.14 |
| 16 steps | 4.43 | 3.09 | 75.90 |
| 32 steps | 4.41 | 2.99 | 73.34 |
| 64 steps | 4.40 | 2.95 | 73.03 |
| − contextual MIDI | 4.44 | 3.36 | 76.01 |
| − clean audio context | 3.48 | 9.95 | 76.01 |
| − CFG | 4.29 | 2.98 | 45.66 |

Interpretation:

- more than eight Euler steps improves FAD but slightly reduces MuQ-Eval and FOn;
- contextual MIDI has no consistent benefit in this small ablation;
- removing clean audio context severely harms quality and FAD;
- removing CFG strongly reduces onset F1.

The authors caution that the ablation uses only seven recordings and should not be treated as dataset-specific evidence.  
**Anchors:** PDF p. 4, Table 4; Appendix E, PDF p. 12.

---

### 8. Listening evaluation and limitations

There is **no formal listening test** in v1. The paper explicitly states that listening tests with music experts are future work. The website provides audio demos, but these are demonstrations, not a controlled perceptual evaluation.

Other limitations:

1. **Transcription-mediated adherence metrics.** YourMT3+ errors dominate some reported losses.
2. **Codec reconstruction loss.** HeartCodec reconstruction is a major bottleneck.
3. **Mono audio.** Stereo image and spatial attribution are discarded.
4. **Target-region resynthesis.** Unchanged notes inside the edited region are regenerated, not copied.
5. **Instrument classes are coarse.** The representation does not provide robust performer, source-recording, or stem identity.
6. **Deletion is weak.** `Rdel` is low across systems and tasks.
7. **Limited source-disjointness.** Appendix A notes that BSD/BSED share symphonies and score passages, so that split is not composition-disjoint.
8. **No explicit provenance or attribution evaluation.**
9. **Synthetic/rendered evaluation components.** Slakh is synthesised, and POP909 editing uses SoundFont renders; these do not fully represent commercial recordings or complex studio mixes.
10. **Model-selection uncertainty.** Confidence intervals are source-recording bootstrap intervals, not training-run uncertainty or paired significance tests.

**Anchors:** PDF p. 4, §3.3–§4; Appendix A, PDF p. 6; Appendix B, PDF p. 7.

---

### 9. Artifact status

The paper says that demos, checkpoints, data, and benchmark samples are available through `mimbres.github.io/spansynth-edit`.

The live artifacts currently show a mixed status:

- Public GitHub repository: `https://github.com/mimbres/spansynth-edit`
- Public checkpoint: `https://huggingface.co/mimbres/spansynth-edit`
- Running Hugging Face Space: `https://huggingface.co/spaces/mimbres/spansynth-edit`
- Audio demonstration page: `https://mimbres.github.io/spansynth-edit/`
- The project page labels **Data: “Coming soon”**.
- The Hugging Face checkpoint contains transformer, codec, HeartCodec SQ, pipeline, and `v3-sq-v8-127750step` weights.
- The repository README documents local CLI, Diffusers, CPU/MPS/CUDA, and ComfyUI usage.
- README-reported inference memory is about 3.9 GiB; the paper reports 3.37 GiB for a GH200, batch 1, MIDI-only generation.
- The live demo states that early selections use the Base SQ checkpoint at step 127,750, CFG 2, and 64 steps.
- Code and model weights are Apache-2.0, but dataset licenses remain applicable.

Thus, **code, weights, demos, and an interactive interface are available; the full training/evaluation data release is not yet clearly available**.

---

### Relevance to source-preserving audio and symbolic mashups

### Directly useful

SpanSynth-Edit provides several strong building blocks:

- MIDI-controlled regional editing rather than unconstrained generation.
- Multi-instrument joint modelling.
- Explicit contextual audio conditioning for timbre continuity.
- Instrument-labelled note events.
- Within-frame timing via continuous boundary positions.
- Addition of instruments absent from the context.
- Paired original/revised editing benchmarks.
- A practical low-rate latent representation.

These properties are highly relevant to symbolic mashups where a symbolic arrangement must be rendered while retaining characteristics of a source recording.

### Important mismatch

For **source-preserving** mashups, the method is not yet sufficient:

- It models a mono mixture, not independently attributable sources.
- It has no source-recording or performer identity channel.
- It does not guarantee that unchanged notes retain their original waveform, phase, articulation, or spatial position.
- It regenerates all target-region content, including nominally unchanged notes.
- `Fkeep` is based on transcription, not source isolation.
- The model can preserve context outside the target, but preservation inside the edited span is only statistical.

Therefore, the appropriate interpretation is:

> SpanSynth-Edit is a strong **context-preserving MIDI-guided resynthesis** model, but not a provenance-preserving or source-isolating mashup system.

The paper’s `Fkeep`, MuQ/CLAP similarity, and fixed-context design are useful starting points, but they do not establish attribution or non-interference at the source level.

---

### Concrete research ideas

1. **Locked-source editing:** represent each stem/source with an explicit source ID and lock unchanged source latents. Generate only the residual associated with changed MIDI events.

2. **Stem-aware MIDI Span:** extend each event with recording ID, performer ID, stem ID, microphone/channel, and edit status: `locked`, `modified`, `added`, or `deleted`.

3. **Mixture-plus-residual architecture:** preserve the original mixture outside and inside the edit region through a copied baseline path, then generate a residual for additions or replacements. Penalise changes to locked stems.

4. **Attribution metrics:** supplement transcription metrics with:
   - source-conditioned SI-SDR;
   - unchanged-stem spectral deviation;
   - source leakage into newly added instruments;
   - boundary discontinuity;
   - performer/timbre embedding drift;
   - stereo/spatial preservation;
   - note-level source attribution accuracy.

5. **Ground-truth paired mashup benchmark:** create source-separated mixtures with known MIDI, then evaluate insertion, deletion, replacement, and cross-source orchestration under controlled overlap.

6. **Codec study:** compare frozen HeartCodec, fine-tuned decoder, higher-rate SQ latents, and unquantised latents. The paper’s Table 3 suggests codec reconstruction—not scalar quantisation alone—is a major bottleneck.

7. **Human evaluation:** test experts on:
   - whether unchanged material sounds preserved;
   - whether additions belong to the requested source/timbre;
   - whether edits create artifacts;
   - whether the result is musically playable;
   - whether provenance remains audibly identifiable.

8. **Attribution-aware loss:** use contrastive losses that preserve embeddings of locked source stems while separating the identity of newly added material.

9. **Symbolic edit provenance:** retain a machine-readable edit ledger linking each generated audio region to original MIDI events, revised MIDI events, and source recordings. This would make the system useful for explainable mashups rather than merely controllable synthesis.

10. **Robust timing evaluation:** use synthetic sub-frame perturbations with exact ground truth instead of relying only on transcription and annotation-sensitive onset detection.

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
