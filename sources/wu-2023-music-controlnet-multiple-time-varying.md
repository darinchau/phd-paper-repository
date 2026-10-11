---
title: "Music ControlNet: Multiple Time-varying Controls for Music Generation"
authors: "Shih-Lun Wu, Chris Donahue, Shinji Watanabe, Nicholas J. Bryan, and Dasaem Jeong"
year: 2023
doi: 10.48550/arXiv.2311.07069
category: generation-and-planning
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/wu-2023-music-controlnet-multiple-time-varying.pdf"
pdf_filename: wu-2023-music-controlnet-multiple-time-varying.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
---
## One-line Summary

The model generates Mel spectrograms with diffusion and renders them through a DiffWave vocoder. It uses global genre/mood conditioning plus any subset of the time-varying controls.

## 1. Document Information

- **Canonical source:** arXiv `2311.07069v1`; official PDF preserved as `wu-2023-music-controlnet-multiple-time-varying.pdf`.
- **Full-paper evidence:** delegate digest `del_mv415ez7_dm5h.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### Evidence-grounded digest

**Paper:** Shih-Lun Wu, Chris Donahue, Shinji Watanabe, Nicholas J. Bryan, *Music ControlNet: Multiple Time-varying Controls for Music Generation*, arXiv:2311.07069v1, 13 Nov 2023.

### 1. Core contribution

**Author claim:** Music ControlNet adds composable, time-varying controls to text-conditioned music generation: melody, dynamics, and rhythm. Each control may be omitted, fully specified, or specified only over selected time spans, with the model improvising elsewhere ([p.1, Abstract; §I; Fig.1]).

The model generates Mel spectrograms with diffusion and renders them through a DiffWave vocoder. It uses global genre/mood conditioning plus any subset of the time-varying controls.

**Interpretation:** This is a useful control interface, but it is not a source-preserving or provenance-aware mashup system. It preserves selected musical attributes statistically; it does not preserve exact notes, tracks, timbres, or source identity.

---

### 2. Problem formulation and architecture

#### Conditional audio generation

The authors factorize generation as:

\[
p(w,s\mid c_{\text{text}},C)
=
p(w\mid s)\,p(s\mid c_{\text{text}},C)
\]

where \(w\) is waveform, \(s\) is a spectrogram, \(c_{\text{text}}\) is global style, and \(C\) is the set of time-varying controls ([p.3, §III-A, Eqs. 8–9]).

They assume waveform and controls are conditionally independent given the spectrogram. The model therefore learns \(p(s\mid c_{\text{text}},C)\), while a separately trained DiffWave model learns \(p(w\mid s)\).

#### Control representation

Unlike image ControlNet, where controls share image spatial dimensions, Music ControlNet defines:

\[
C=\{c^{(n)}\in\mathbb{R}^{T f_k\times B_n\times D_n}\}_{n=1}^{N}
\]

where \(B_n\) is control-specific and need not equal the spectrogram’s frequency-bin count \(B\) ([p.4, §III-A, Eq. 10]).

This matters because:

- time is shared between controls and output;
- control dimensions need not correspond directly to frequencies;
- a dynamics value, for example, describes a frame-wide musical intensity rather than a frequency-specific amplitude.

#### ControlNet adaptation

The pretrained text-conditioned U-Net is frozen while an adaptor/control branch is fine-tuned, following ControlNet. Zero-initialized convolution layers inject control information into the frozen decoder ([p.3–4, §II-D; §III-B, Eqs. 11–12]).

For each control, a one-hidden-layer MLP \(M^{(n)}\):

1. maps the control’s class dimension to the spectrogram frequency dimension;
2. learns the relationship between control classes and frequency bins;
3. produces representations that are concatenated across controls before entering a shared zero convolution.

**Interpretation:** The MLP gives the network flexibility to learn that, for example, a 12-class chroma control does not directly equal 12 spectrogram bins.

---

### 3. Partial-control design

#### Full control dropout

For each training example, a subset of controls is randomly dropped by replacing it with an all-zero tensor:

\[
c^{(n)} =
\begin{cases}
0 & n\in I'\\
c^{(n)} & n\notin I'
\end{cases}
\]

This teaches the model to respond to arbitrary subsets of melody, dynamics, and rhythm ([p.4, §III-C, Eq. 13]).

The authors additionally assign higher probability to keeping or dropping all controls, because they found this perceptually preferable.

#### Partial temporal masking

For every active control, the authors randomly sample a temporal interval \([t_{n,a},t_{n,b}]\) and replace the control with zeros within that interval:

\[
c_t^{(n)} =
\begin{cases}
0 & t\in[t_{n,a},t_{n,b}]\\
c_t^{(n)} & \text{otherwise}
\end{cases}
\]

At training time, the model uniformly chooses between:

1. full masking of selected controls;
2. full plus partial temporal masking ([p.4–5, §III-C; Fig.2]).

**Author claim:** This allows creators to provide only a local control span and instruct the model to improvise in the remaining spans.

**Important limitation for symbolic use:** Zero means “unprovided/improvise,” not necessarily musical silence. A symbolic system should represent *unknown*, *silence*, and *hard absence* separately.

---

### 4. Control extraction and creator interfaces

All three controls can be extracted directly from audio/spectrograms, avoiding manual annotation during training ([p.5, §III-D]).

| Control | Extracted representation | Creator-facing construction |
|---|---|---|
| **Melody** | Librosa chromagram; energy rearranged into 12 pitch classes; frame-wise argmax creates a one-hot pitch-class sequence; high-pass filtering at Middle C, 261.2 Hz, suppresses bass dominance | Record a simple melody or draw a pitch contour |
| **Dynamics** | Sum linear-spectrogram energy across frequency, convert to dB, apply a Savitzky–Golay smoothing filter with a one-second context window | Draw a time-varying intensity curve |
| **Rhythm** | In-house RNN beat detector produces frame-wise beat and downbeat probabilities, giving two control channels | Time-stretch existing rhythm curves, shift beat timestamps, or draw rhythmic patterns |

The authors argue that dynamics also correlates with instrumentation, harmonic texture, and rhythmic density, while beat/downbeat curves provide more useful timing control than a single global BPM value ([p.5, §III-D]).

#### Creator-control dataset

Created controls were intentionally simpler than extracted controls:

- **Melody:** 20 six-second controls from recordings of 10 public-domain classical melodies.
- **Dynamics:** 24 curves from linear, tanh, and cosine functions, flipped or unflipped, with ±6, ±9, ±12, and ±15 dB ranges.
- **Rhythm:** 20 presets from four in-domain songs, time-stretched by factors 0.8, 0.9, 1.0, 1.1, and 1.2.
- Each control set was crossed with 10 genres × 10 moods, producing 2.0K, 2.4K, and 2.0K examples respectively ([p.6, §IV-B]).

**Interpretation:** The creator controls test generalization from realistic audio-derived controls to low-dimensional, hand-designed controls. They do not test arbitrary symbolic scores or multi-track MIDI.

---

### 5. Data, model, and training

#### Data

- Approximately **1,800 hours** of licensed instrumental music.
- Genre and mood tags only; no free-form captions.
- Evaluation:
  - 2K held-out in-domain songs;
  - approximately 5K ten-second MusicCaps clips;
  - MusicCaps descriptions converted to genre/mood tags using ChatGPT;
  - created-control datasets ([p.5, §IV-A]).

#### Spectrogram model

- Convolutional U-Net.
- Five 2-D convolutional ResNet blocks with channels `[64, 64, 128, 128, 256]`.
- Stride-2 downsampling.
- 22.05 kHz audio.
- Hop size 256, approximately 86 frames/second.
- Window size 2048.
- 160 Mel bins.
- 160 dB dynamic range, scaled to \([-1,1]\).
- 1,000-step cosine diffusion schedule.
- 256-dimensional learnable genre/mood embeddings injected by cross-attention into the inner two ResNet blocks.
- Six-second training output: \(512\times160\times1\).
- L1 noise-prediction objective.
- 41M parameters ([p.6, §IV-C]).

#### Training and inference

- Pretraining: 5 days on 32 A100 GPUs.
- Control fine-tuning: 3 days on 8 A100 GPUs.
- Adam, learning rate \(10^{-5}\).
- Inference: 100-step DDIM; classifier-free guidance scale 4 applied to global style.
- DiffWave vocoder: 50-step training schedule, six-step inference, 22.05 kHz ([p.6, §IV-C]).

---

### 6. Evaluation metrics

- **Melody accuracy:** frame-wise agreement of 12 pitch classes between input control and extracted output.
- **Dynamics correlation:** Pearson correlation:
  - *micro*: calculated independently per generation;
  - *macro*: pooled over all generations.
- **Rhythm F1:** beat/downbeat timestamp alignment after HMM post-filtering; timestamps count as aligned if within 70 ms.
- **CLAP:** cosine similarity between audio and text embeddings using prompts such as “An audio of happy jazz music.”
- **FAD:** VGGish-based Fréchet Audio Distance; lower is better ([p.6–7, §IV-D]).

---

### 7. Quantitative results

### Table I — extracted controls, single versus multiple controls

**Rows are ordered as global-only, single melody, single dynamics, single rhythm, then four multi-control combinations. Values are melody accuracy; dynamics micro/macro; beat/downbeat F1; CLAP; FAD.**

| Controls | Melody | Dyn. micro/macro | Rhythm beat/downbeat | CLAP | FAD |
|---|---:|---:|---:|---:|---:|
| Global style only | 8.5 | −0.7 / 0.7 | 27.8 / 7.8 | .28 | 1.51 |
| Melody | **58.3** | 4.4 / 3.1 | 40.2 / 12.1 | .28 | 1.34 |
| Dynamics | 8.6 | **88.8 / 63.6** | 36.7 / 16.1 | .26 | 1.50 |
| Rhythm | 8.6 | 25.8 / 34.6 | **69.2 / 35.4** | .27 | 1.17 |
| Melody + dynamics | **57.7** | **89.7 / 64.8** | 47.4 / 21.8 | .26 | 1.38 |
| Melody + rhythm | **59.1** | 31.6 / 36.3 | **70.0 / 38.7** | .26 | 1.16 |
| Dynamics + rhythm | 8.7 | **89.6 / 60.9** | **72.1 / 39.9** | .26 | 1.12 |
| Melody + dynamics + rhythm | **58.7** | **90.8 / 64.0** | **70.8 / 40.8** | .25 | 1.14 |

**Author interpretation:** The relevant control substantially improves its metric. Multiple controls retain approximately the same controllability as single controls. CLAP decreases mildly as more controls are enforced, while FAD does not worsen ([p.6–7, Table I; §V-A]).

**Caveat:** Dynamics and rhythm scores are already elevated when those controls are omitted, which the authors attribute to natural correlation between dynamics and rhythm.

---

### Table II — extracted versus created controls

| Control | Source | Main controllability result | CLAP | FAD |
|---|---|---:|---:|---:|
| Melody | Extracted | 58.3% | .28 | 1.34 |
| Melody | Created | **78.2%** | .27 | 1.81 |
| Dynamics | Extracted | 88.8 / 63.6 micro/macro | .26 | 1.50 |
| Dynamics | Created | **98.5 / 93.2** | .26 | 2.18 |
| Rhythm | Extracted | 69.2 / 35.4 beat/downbeat | .26 | 1.17 |
| Rhythm | Created | **88.6 / 45.2** | .26 | 2.93 |

**Author claim:** Created controls improve controllability, demonstrating generalization to out-of-domain inputs ([p.8, Table II; §V-B]).

**Author limitation:** FAD degrades for created controls. The outputs may be less musically interesting—for example, a melody may be rendered by one instrument over a constant chord, or dynamics may be expressed using monotonous bass or sound effects. The authors suggest generating batches and selecting the best sample.

---

### Table III — fully versus partially specified created controls

| Control | Full | Partial |
|---|---:|---:|
| Melody accuracy | 78.2 | 74.3 |
| Dynamics micro/macro | 98.5 / 93.2 | 88.6 / 89.0 |
| Rhythm beat/downbeat | 88.6 / 45.2 | 80.1 / 34.8 |
| CLAP | .27 | .27 melody; .27/.26 for other rows |
| FAD | 1.81 | 1.66 melody; 1.52 dynamics; 2.60 rhythm |

For partial controls, only a random **1.0–4.5 seconds** of the six-second sequence was specified; controllability metrics were evaluated only in the specified span ([p.7–8, §V-C; Table III]).

**Author claim:** Partial control causes only mild degradation and does not produce pronounced incoherence at controlled/uncontrolled boundaries.

---

### Table IV — duration extrapolation

| Generation length | Melody accuracy | CLAP | FAD |
|---:|---:|---:|---:|
| 6 sec | 78.2 | .27 | 1.81 |
| 12 sec | 81.0 | .32 | 2.11 |
| 24 sec | 82.8 | .33 | 2.54 |

**Author claim:** Fully convolutional generation retains control and text adherence at 2× and 4× training duration.

**Observed limitation:** FAD worsens, and listening reveals noticeably increasing background noise as duration increases ([p.8, §V-D; Table IV]).

---

### Table V — MusicGen comparison

Music ControlNet has **41M parameters**, versus MusicGen’s **1.5B**. For created melodies:

| Condition | Music ControlNet | MusicGen |
|---|---:|---:|
| Full melody control | 82.6% | 55.2% |
| Half-length melody prompt | 80.8% | 56.8% |

For extracted melodies:

| Condition | Music ControlNet | MusicGen |
|---|---:|---:|
| Full control | 47.1% | 41.3% |
| Half prompt | 46.7% | 42.1% |

The authors’ headline **49% relative improvement** corresponds approximately to \(82.6/55.2-1\).

CLAPtag is comparable:

- Music ControlNet: approximately .33.
- MusicGen: approximately .34.

MusicGen has better FAD against MusicCaps, but the authors note that MusicCaps contains vocals and low-quality recordings absent from their licensed instrumental training data. Against their in-domain reference set, Music ControlNet is competitive or somewhat better ([p.8–9, §V-E; Table V]).

**Important comparison caveat:** MusicGen receives free-form text, while Music ControlNet receives only genre/mood tags in this experiment. The authors therefore report both CLAPtext and CLAPtag.

---

### 8. Figures

#### Figure 1 — system overview ([p.2])

Shows:

1. creator supplies mood/genre text;
2. creator supplies any subset of melody, dynamics, and rhythm;
3. controls may be partial, with “improvise” spans;
4. pretrained U-Net plus control branch denoises a Mel spectrogram;
5. vocoder produces audio;
6. controls are extracted from output for post-hoc analysis.

#### Figure 2 — masking schemes ([p.4–5])

Compares:

- **Full masking**, inherited from Uni-ControlNet;
- **Full + partial masking**, proposed here.

Gray regions represent omitted controls or uncontrolled temporal spans. The figure illustrates multiple combinations of dropped controls and interval-level omissions.

#### Figure 3 — single-control examples ([p.9])

Left: controls extracted from songs, with styles such as “Inspiring, Electronic,” “Dynamic, R&B,” and “Inspiring, Pop.”

Right: creator controls such as “Sad, Jazz,” “Happy, Country,” and “Nostalgic, World.”

The displayed outputs visually follow:

- one-hot melody contours;
- drawn dynamics curves;
- beat/downbeat rhythm curves.

**Author claim:** The model follows controls even when their relationship to spectrogram structure is indirect and produces richer music than simply copying the low-dimensional control.

#### Figure 4 — multiple and partial controls ([p.10])

- **4a:** simultaneous full melody and dynamics controls, with rhythm omitted.
- **4b:** all three controls, each specified only over part of the six-second span. The creator scenario is: begin with a signature melody, intensify later, and synchronize beats to video cuts.

The uncontrolled spans are labelled “improvise.” The authors report visually cohesive transitions without visible spectrogram borders.

---

### 9. Human evaluation

There is **no formal human-subject evaluation** in the paper:

- no listening-test protocol;
- no blinded pairwise preference study;
- no participant count;
- no MOS, ratings, or inter-rater statistics.

The authors do report informal listening:

- they listened to longer generations and observed increased background noise ([p.8, §V-D]);
- they make perceptual claims about created controls being less musically interesting ([p.7, §V-B]);
- they show qualitative spectrogram/control examples in Figures 3–4.

These are author observations, not controlled human-evaluation evidence.

---

### 10. Limitations and scope

### Explicit or strongly implied by the authors

1. **Global text control is limited.** The training data lacks free-form captions, so the model uses genre/mood tags rather than unrestricted text ([p.5, §IV-A]).
2. **Training duration is only six seconds.** Longer generation increases noise and FAD ([p.8, §V-D]).
3. **Created controls can produce less interesting music.** FAD increases and outputs may become monotonous ([p.7, §V-B]).
4. **Domain is restricted.** Training uses licensed instrumental music; no singing voice. MusicCaps FAD comparisons may be biased by vocals and low-quality recordings ([p.8, §V-E; p.10, §VIII]).
5. **The controls are proxies.** Melody is a single pitch class per frame; dynamics is one smoothed energy value; rhythm is beat/downbeat probability.
6. **The paper itself proposes additional future controls**, including chords, multi-track pitch, instruments, emotion, and tension ([p.10, §VII]).

### Source-preservation and provenance limitations

These are not presented as author claims; they follow from the method:

- The model generates new audio rather than preserving source tracks or exact symbolic events.
- Melody extraction discards octave, voicing, duration semantics, instrument, and simultaneous pitches.
- Dynamics is not a source performance envelope; it is a smoothed scalar loudness proxy.
- Rhythm contains beat/downbeat probabilities, not exact note onsets or drum events.
- No source identifiers, hashes, timestamps, licenses, transformation logs, or provenance metadata are modeled.
- The paper mentions “remixing” by combining controls from existing music ([p.5, §III-D]), but does not provide a dedicated cross-source experiment showing melody from source A, rhythm from source B, and style from source C.
- There is no guarantee that generated material is attributable to, or reconstructively faithful to, the source from which a control was extracted.

---

### 11. Relevance to source-preserving symbolic mashup research

### Directly reusable ideas

1. **Control dropout for composability.** Train with arbitrary subsets of controls so a mashup system can independently activate melody, rhythm, harmony, dynamics, or instrumentation.
2. **Temporal partial masking.** Let creators specify only selected bars or phrases and allow controlled improvisation elsewhere.
3. **Self-supervised control extraction.** Derive training controls automatically from recordings, reducing manual annotation.
4. **Creator/extracted domain gap.** Evaluate separately on:
   - source-derived controls;
   - clean symbolic controls;
   - hand-edited controls;
   - noisy or incomplete controls.
5. **Separate controllability from realism.** Their melody/dynamics/rhythm metrics are useful precedents, but a symbolic mashup system should add note-level and source-level metrics.

### Concrete research design

#### A. Provenance-aware symbolic controls

Represent every event as:

```text
(source_id, track_id, instrument, pitch, onset, duration, velocity, confidence)
```

Maintain a manifest containing:

- source URI or content hash;
- license and ownership metadata;
- extractor/version;
- time-warp and transposition operations;
- which output events were copied, transformed, or newly generated.

This would address the provenance information entirely absent from Music ControlNet.

#### B. Replace proxies with symbolic constraints

Use multi-track controls containing:

- exact pitch and octave;
- onset and duration;
- velocity/articulation;
- chord/harmony;
- beat and downbeat;
- instrument/track identity.

A differentiable or constrained renderer could preserve selected events exactly while allowing the model to generate accompaniment.

#### C. Explicit source mixing

Train and test combinations such as:

- melody from source A;
- rhythm from source B;
- harmony from source C;
- dynamics from source D;
- target style from text or a reference recording.

Report both:

- **source fidelity:** note/onset/beat recall and precision;
- **novelty:** proportion of generated events not copied from sources;
- **provenance accuracy:** whether each output event is correctly attributed;
- **musicality:** controlled human evaluation.

#### D. Better partial-control semantics

Do not encode every omitted region as zero. Use separate states:

1. hard rest/silence;
2. unknown—model may improvise;
3. soft suggestion;
4. hard constraint.

This avoids conflating “no note” with “no instruction.”

#### E. Human evaluation designed for agency

A follow-up should test:

- control adherence;
- musical quality;
- source recognizability;
- perceived originality;
- creator preference;
- provenance clarity;
- boundary quality between controlled and improvised regions.

### Overall assessment

Music ControlNet is strong evidence that low-dimensional, time-varying controls can be composed, partially specified, and generalized from extracted audio features to creator-designed inputs. Its most valuable contribution for symbolic mashup research is the **training strategy for composable and temporally incomplete controls**.

However, it should not be treated as evidence of source preservation. The method controls perceptual proxies in generated audio; it does not retain symbolic event identity, source attribution, exact performance detail, or an auditable provenance chain.

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
