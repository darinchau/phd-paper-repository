---
title: "MuseTimbre: Zero-Shot Timbre Transfer by Controlling a Frozen Music Generator"
authors: "Yuan-Chiao Cheng and Zhiyao Duan"
year: 2026
doi: 10.48550/arXiv.2609.30548
category: generation-and-planning
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/cheng-2026-musetimbre-zero-shot-timbre-transfer.pdf"
pdf_filename: cheng-2026-musetimbre-zero-shot-timbre-transfer.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
---
## One-line Summary

Code: `https://github.com/barry-mir/muse-timbre` Audio/demo: `https://barry-mir.github.io/muse-timbre-demo/`

## 1. Document Information

- **Canonical source:** arXiv `2609.30548v1`; official PDF preserved as `cheng-2026-musetimbre-zero-shot-timbre-transfer.pdf`.
- **Full-paper evidence:** delegate digest `del_mv40f07a_51l9.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### Evidence-grounded digest: MuseTimbre

### 1. Bibliography and version

- **Title:** *MuseTimbre: Zero-Shot Timbre Transfer by Controlling a Frozen Music Generator*
- **Authors:** Yuan-Chiao Cheng, Zhiyao Duan
- **Version:** arXiv:2609.30548v1, [cs.SD], **24 September 2026**
- **Affiliations:** Georgia Institute of Technology; University of Rochester
- **Paper length:** 5 pages, including references.
- **Artifact links stated by the authors:**  
  Code: `https://github.com/barry-mir/muse-timbre`  
  Audio/demo: `https://barry-mir.github.io/muse-timbre-demo/`
- **Artifact claim:** The paper says it releases code, model weights, and audio examples (p. 2, footnote and §1). This digest does not independently verify repository contents, licensing, reproducibility, or link availability.

The paper contains 30 references. The central dependencies are Stable Audio 3 [12], LAION-CLAP [15], Basic Pitch [14], Control-Transfer Diffusion [4], TokenSynth [5], and the MuScriptor transcription model [16].

---

### 2. Problem and claimed contribution

#### Author’s framing

Instrument timbre transfer re-voices a source performance with the timbre of a reference instrument while preserving its notes. The authors identify two problems:

1. **Pitch/timbre disentanglement:** The source recording contains both musical content and source-instrument timbre.
2. **Precise target-timbre specification:** A text label such as “violin” cannot capture the nuances of a particular recording.

MuseTimbre is claimed to be, “to our best knowledge,” the first system to transfer timbre from an audio reference to a polyphonic source by conditioning a pretrained music generator rather than training a dedicated generator from scratch (abstract, §1, p. 1).

#### Interpretation

The key design is not waveform-preserving editing. It is **regeneration from an explicit symbolic-like pitch representation plus an audio-derived timbre embedding**. This distinction matters for mashup and repair: source notes can be preserved or edited, but the original waveform’s timing, articulation, and performance detail are not directly retained.

---

### 3. Architecture

#### Frozen generator

MuseTimbre adds two control pathways to **Stable Audio 3 Medium**, described as a pretrained rectified-flow diffusion transformer:

- Frozen audio autoencoder/VAE
- Frozen DiT backbone
- Frozen original text-conditioning pathway
- Trainable pitch-conditioning pathway
- Trainable timbre-conditioning pathway

This is shown in **Figure 1, p. 2**, and described in §2.2.

#### Pitch pathway

The source clip is converted to a binary piano roll:

- **176 channels:** 88 note channels + 88 onset channels
- Resampled to approximately **10.8 frames/second**, matching the latent frame rate
- Note channels indicate frames during which a note is active.
- Onset channels indicate the first frame of a note.
- Basic Pitch salience thresholds:
  - Notes: **0.35**
  - Onsets: **0.50**
- A trainable **1-D CNN** encodes the roll into per-frame features.
- Features enter every DiT layer through decoupled cross-attention.
- Rotary embeddings are applied to queries, keys, and values.
- The added pathway is controlled by a **zero-initialized gate**.

The authors argue that removing harmonic structure from the source makes the pitch representation carry little source-timbre information (§2.3, p. 2).

#### Timbre pathway

The reference waveform is processed by the audio branch of **LAION-CLAP**:

- Input sampling rate: **48 kHz**
- Output: a single time-invariant **512-dimensional embedding**
- CLAP is **fine-tuned end-to-end** on the transfer task.
- A linear projection maps the embedding to AdaLN scale and shift parameters.
- Modulation is expressed as:

\[
x \leftarrow x(1+\gamma)+\beta
\]

- Timbre AdaLN occurs after pitch cross-attention in every DiT layer.
- It also uses a zero-initialized AdaLN-Zero-style gate.

Figure 1 places the modules in the following approximate layer order:

1. Self-attention  
2. Frozen text cross-attention  
3. Pitch cross-attention  
4. Timbre AdaLN  
5. Feed-forward network  

#### Important control property

The authors state that the original Stable Audio text control remains usable alongside pitch and reference timbre. A MIDI/piano-roll score can also replace the source-audio transcription input (§2.6, p. 3).

---

### 4. Training objective and data

#### Objective

The whole trainable system is optimized with a rectified-flow objective:

\[
x_t=(1-t)z_0+t\epsilon
\]

and predicts the velocity \(\epsilon-z_0\):

\[
\mathcal{L}
=
\mathbb{E}_{z_0,\epsilon,t}
\left\|
v_\theta(x_t,t,c_{\text{pitch}},c_{\text{timbre}})
-
(\epsilon-z_0)
\right\|_2^2
\]

(§2.5, p. 3).

For a training clip:

- Pitch is either ground-truth pitch or Basic Pitch output.
- Timbre is extracted from a **different segment of the same clip**.
- Training uses a 50/50 mixture of synthesized and real audio.

#### Synthesized data

- Rendered Slakh MIDI stems
- **Seven General MIDI soundfonts**
- Approximately **1.1 million stem recordings**
- At least 10 seconds each
- **13 instrument classes**

#### Real data

- **18,869 clips**
- From **1,208 single-instrument stems**
- Sources: MoisesDB and URMP
- Drums, percussion, vocals, and untagged stems removed
- Includes binarized Basic Pitch rolls
- Training clips: **5 seconds at 44.1 kHz**

#### Optimization and compute

- AdamW
- **250,000 steps**
- **Two GPUs**
- Effective batch size: **16**
- Weight decay: **0.01**
- **1,000 warmup steps**, then cosine decay
- Learning rate:
  - Fine-tuned timbre encoder: **10⁻⁵**
  - Control modules: **10⁻⁴**
- Multi-condition classifier-free-guidance dropout

The paper does **not** report model parameter counts, trainable parameter counts, GPU models for training, training wall-clock time, CFG dropout probabilities, or exact soundfont identities.

#### Inference

- Starts from noise
- **25 Euler steps**
- Approximately **one second** on a single RTX 5090 for five seconds of audio
- Pitch CFG = **2**
- Timbre CFG = **2**

---

### 5. Evaluation setup

#### Held-out datasets

Evaluation uses **304 cross-instrument pairs** from four datasets held out during training:

- PHENICX-Anechoic
- MAESTRO v3 test split
- GOAT
- Bach10

There are **13 instruments** in total. The authors select isolated single-instrument clips and use the loudest five seconds. Each source/reference pair uses different instruments and comes from different datasets, so the pair shares neither instrument identity nor recording condition (§3.1, p. 3).

#### Metrics

##### Timbre match

- Uses PaSST, an AudioSet-trained audio tagger.
- A prediction counts as a match if its top-1 AudioSet class lies within the reference instrument’s family.
- The paper reports family mappings in **Table 2, p. 3**.

Examples:

- Violin/viola → violin, bowed string, string section
- Cello/double bass → cello/double bass, bowed string, string section
- Flute/clarinet/saxophone → own label or woodwind
- Trumpet/horn → trumpet/French horn or brass
- Piano → piano or keyboard
- Electric guitar → electric guitar, guitar, or plucked string

The reference clips themselves achieve only **88.5% PaSST accuracy**, establishing an approximate metric ceiling.

##### Pitch preservation

- Output is transcribed with MuScriptor conditioned on the target instrument.
- Compared against ground-truth source MIDI.
- Frame-F1 at **10 ms hop** and **50-cent tolerance**.
- Source-audio transcription achieves an average frame-F1 of **0.540**, another practical upper bound.

---

### 6. Main results

#### Exact values reported in the text

| System | Timbre match | Melody/pitch frame-F1 |
|---|---:|---:|
| **MuseTimbre** | **57.6%** | **0.316** |
| CTD | 48.7% | lower than MuseTimbre; exact value not tabulated |
| SS-VQ-VAE | 45.4% | lower than MuseTimbre; exact value not tabulated |
| TokenSynth-A, audio reference | 34.6% | **0.380** |
| TokenSynth-T, text prompt | 30.4% | **0.367** |

These results are stated in §3.2 and visualized in **Figure 2, p. 3**.

The paper’s main claim is therefore asymmetric:

- MuseTimbre has the best reported timbre match.
- TokenSynth-A and TokenSynth-T have higher pitch frame-F1.
- The baselines exhibit a pitch–timbre trade-off.
- MuseTimbre occupies a better timbre position while remaining competitive in pitch.

Figure 2 also plots DDIM-inv, DDPM-inv, and MuseControlLite, but their exact coordinates are not numerically tabulated; they must be read approximately from the graph.

#### Subjective evaluation

The authors conduct a MUSHRA-like listening test without anchors:

- 20 musically trained listeners
- 10 source/reference/system tuples
- Scores from 0 to 5
- Systems: MuseTimbre, CTD, SS-VQ-VAE, TokenSynth-A
- Attributes: timbre, pitch, fidelity

Reported values (§3.4, **Figure 4, p. 4**):

| System | Timbre | Pitch | Fidelity |
|---|---:|---:|---:|
| MuseTimbre | **2.6** | not stated numerically in text | **2.5** |
| TokenSynth-A | 2.4 | **3.4** | **2.6** |
| CTD | 1.4 | figure only | figure only |
| SS-VQ-VAE | 1.1 | figure only | figure only |

MuseTimbre wins subjective timbre and is within 0.1 of TokenSynth-A on fidelity. TokenSynth-A wins subjective pitch.

---

### 7. Timbre-encoder retrieval experiment

#### Design

The authors construct a controlled grid:

- 13 instruments
- 40 melodic segments from the four evaluation datasets
- Every combination of content and instrument timbre is rendered.
- Retrieval pools have sizes \(N=2,4,8,16,32,64,128,256\).
- Each pool contains:
  - One target with the query instrument but different note content
  - Distractors
  - At least one distractor with the query’s exact notes but a different timbre

This specifically tests whether the embedding recognizes instrument identity rather than matching pitch content (§3.3, p. 4; Figure 3).

#### Results

At pool size \(N=256\):

- Fine-tuned CLAP: **0.88 top-1 accuracy**
- Frozen CLAP: **0.53**
- Absolute gain: **0.35**
- Fine-tuned CLAP ranks first at every displayed pool size.
- It also outperforms AST, MERT, and Music2Latent embeddings.

#### Author’s interpretation

Fine-tuning reshapes CLAP into a pitch-robust timbre-similarity space.

#### Qualification

This test uses synthetic controlled renders because real recordings rarely provide identical content in different timbres. The authors explicitly leave broader real-recording timbre-similarity evaluation to future work.

---

### 8. Module ablation and disentanglement

**Table 1, p. 4** evaluates the same 304 pairs with either conditioning module removed. CFG remains pitch = timbre = 2.

| Conditioning | Timbre match | Frame-F1 |
|---|---:|---:|
| Pitch + timbre | **57.6%** | **0.316** |
| Pitch only; null timbre | **16.1%** | **0.267** |
| Timbre only; null pitch | **74.7%** | **0.041** |

The authors call this a “double dissociation”:

- Removing timbre collapses timbre match while preserving much of the melody.
- Removing pitch collapses melody while retaining high timbre match.

The 16.1% result is near the stated **11.8% random-guess rate**. The authors suggest residual performance may come from pitch-range information weakly indicating instrument category.

#### Interpretation

This is useful causal evidence that the two added pathways carry different information. It is not a complete disentanglement proof: the experiment does not test leakage under adversarial pitch/register changes, temporal timbre changes, or unseen source identities.

---

### 9. Limitations and artifact status

#### Explicitly stated or directly evident

1. **Real timbre retrieval is not fully evaluated.** The retrieval experiment relies on synthetic controlled renders; real-recording evaluation is left for future work (§3.3).
2. **Timbre is represented globally.** The reference produces one time-invariant 512-D embedding, so time-varying instrument effects, articulation, room changes, and evolving distortion are not separately controlled.
3. **Pitch depends on Basic Pitch.** The model uses fixed note/onset thresholds and does not use the newer MuScriptor model internally.
4. **The evaluation metric is family-level.** PaSST AudioSet matches may accept broad labels such as “bowed string” or “woodwind”; this is not exact performer or recording-identity verification.
5. **No dedicated artifact analysis is reported.** The paper gives no objective distortion, noise, transient, phase, or spectral-fidelity metric and no systematic artifact/failure-case table.
6. **No uncertainty or significance analysis is reported.** There are no confidence intervals, per-dataset breakdowns, per-instrument breakdowns, or statistical tests.
7. **The paper does not report full model/compute reproducibility details.** Parameter counts, exact Stable Audio 3 configuration, training GPU types, elapsed training time, and CFG-dropout probabilities are absent.

The paper describes the evaluation clips as real polyphonic recordings, but §3.1 says it selects **isolated single-instrument clips**. Thus the evaluation tests polyphony within an instrument—particularly relevant for piano—but not arbitrary multi-instrument mixtures or stem-level identity assignment.

---

### 10. Relevance to symbolic mashup, repair, source identity, and explainability

#### Symbolic mashup

**Direct opportunity:** the system accepts a piano roll or MIDI score and combines it with an audio reference timbre (§2.6). This gives a practical route from symbolic content to reference-specific rendering.

**Current limitation:** the 176-channel roll represents one undifferentiated 88-note instrument stream. It does not natively represent:

- Multiple independently controlled stems
- Per-stem timbre references
- Velocity
- Pedal
- Detailed articulation
- Performer-specific timing
- Instrument-specific pitch ranges beyond the roll itself

A mashup system would need a hierarchical or multi-track pitch representation and separate identity embeddings per stem.

#### Symbolic repair

The explicit roll is useful as an editable intermediate:

1. Transcribe a damaged performance.
2. Detect missing, duplicated, or implausible notes.
3. Repair the roll symbolically.
4. Render the repaired score through a reference timbre.

This is an interpretation rather than an experiment in the paper. MuseTimbre does not train a repair objective, confidence model, masked-note inpainting objective, or preservation loss.

#### Source-identity controls

The model provides a relatively clear separation between:

- **What is played:** piano-roll pitch/onset control.
- **What plays it:** reference-audio timbre embedding.

However, “timbre identity” should not be equated with complete source identity. The reported metrics primarily measure instrument-family similarity. Performer identity, microphone, room, production style, dynamics, and temporal articulation are not separately identified.

#### Explainability

The architecture is more inspectable than an unconditioned generator:

- The pitch control is an interpretable note/onset roll.
- The timbre control is an explicit reference embedding.
- Module ablations provide causal evidence of distinct control roles.
- The frozen backbone reduces the number of learned pathways that must be explained.

But the paper does **not** provide human-readable explanations, note-level attribution, embedding visualization, uncertainty, or counterfactual explanation tools. The learned CLAP embedding remains difficult to interpret semantically beyond retrieval behavior.

---

### 11. Concrete research directions

1. **Multi-stem symbolic control:** Use separate roll streams and separate timbre embeddings for each mashup stem, with explicit routing and stem-level cross-attention.
2. **Repair-aware training:** Mask note/onset regions during training and optimize reconstruction, edit locality, and confidence-calibrated correction rather than only generation quality.
3. **Hierarchical identity embeddings:** Factor reference representations into instrument, performer, articulation, room, microphone, and production-style components.
4. **Temporal timbre conditioning:** Replace the single global CLAP vector with chunk-level or note-aligned embeddings for changing articulations and recording environments.
5. **Pitch-leakage tests:** Train with hard positives—same instrument, different register/content—and hard negatives—same notes, different instruments—to test whether timbre embeddings truly ignore pitch.
6. **Better disentanglement objectives:** Add adversarial or contrastive losses that explicitly suppress pitch, tempo, and melodic-content information in the timbre representation.
7. **Explainability probes:** Perform counterfactual interventions on individual roll notes and embedding dimensions, then measure output changes with note-level and instrument-level attribution.
8. **Stronger evaluation:** Add per-instrument/per-dataset results, onset/duration/velocity preservation, artifact metrics, source-identity verification, confidence intervals, and real paired recordings.
9. **Controlled generation studies:** Sweep pitch/timbre CFG independently to quantify the quality–preservation trade-off and identify failure regions.
10. **Symbolic-native integration:** Compare audio transcription with direct MIDI input and quantify how transcription errors affect timbre transfer and repair quality.

**Overall assessment:** MuseTimbre’s strongest contribution is the explicit, modular separation of symbolic pitch control from audio-reference timbre control while retaining a frozen general-purpose generator. Its results support instrument-family transfer and pitch-robust timbre retrieval, but the evidence does not yet establish fine-grained performer identity, temporal timbre control, multi-stem mashup capability, or artifact-free source-preserving editing.

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
