---
title: "Enabling Factorized Piano Music Modeling and Generation with the MAESTRO Dataset"
authors: "Curtis Hawthorne, Andriy Stasyuk, Adam Roberts, Ian Simon, Cheng-Zhi Anna Huang, Sander Dieleman, Erich Elsen, Jesse Engel, and Douglas Eck"
year: 2019
doi: 10.48550/arXiv.1810.12247
category: data-and-representation
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/hawthorne-2019-enabling-factorized-piano-music-modeling.pdf"
pdf_filename: hawthorne-2019-enabling-factorized-piano-music-modeling.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
---
## One-line Summary

\[ P(\text{audio}) = \mathbb{E}_{\text{notes}} \left[P(\text{audio}\mid\text{notes})\right] \tag{1} \]

## 1. Document Information

- **Canonical source:** arXiv `1810.12247v5`; official PDF preserved as `hawthorne-2019-enabling-factorized-piano-music-modeling.pdf`.
- **Full-paper evidence:** delegate digest `del_mv3zjm7q_kf19.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### Paper digest

### 1. Bibliographic identity

**Curtis Hawthorne, Andriy Stasyuk, Adam Roberts, Ian Simon, Cheng-Zhi Anna Huang, Sander Dieleman, Erich Elsen, Jesse Engel, and Douglas Eck.**  
**“Enabling Factorized Piano Music Modeling and Generation with the MAESTRO Dataset.”**  
arXiv:**1810.12247v5** [cs.SD], submitted **17 January 2019**; published as an **ICLR 2019 conference paper**.

- arXiv record: https://arxiv.org/abs/1810.12247v5
- Initial submission: 29 October 2018.
- v5 is the version represented by `/tmp/paper-digest/1810.12247v5.pdf`.
- Dataset results use **MAESTRO v1.0.0**.
- Dataset: CC BY-NC-SA 4.0.

I inspected all 12 PDF pages, including Figure 1, Figure 2, Tables 1–7, and the alignment appendix.

---

### 2. Direct answer: is MIDI an explicit latent space?

### Short answer

**MIDI is an explicit, discrete intermediate representation and can be called a discrete latent code in the paper’s probabilistic factorization. However, it is not a learned latent space in the usual VAE/embedding sense.**

The authors write:

\[
P(\text{audio}) =
\mathbb{E}_{\text{notes}}
\left[P(\text{audio}\mid\text{notes})\right]
\tag{1}
\]

**p. 2, §1, Equation (1).**

They explicitly say this “can be thought of as a generative model with a discrete latent code of musical notes.”

But the implementation is not a jointly trained latent-variable model:

| Common interpretation | Wave2Midi2Wave |
|---|---|
| Continuous latent vector \(z\) | Discrete note-event sequence |
| Encoder learns \(q(z\mid x)\) | Onsets and Frames transcribes audio into notes |
| Decoder reconstructs audio | Conditional WaveNet synthesizes waveform |
| Prior and decoder trained jointly | Three separately trained models |
| KL/ELBO or latent regularization | No VAE objective or latent-space geometry |
| Latent is usually hidden | MIDI is observable, editable, and human-readable |

The authors define three modules on **p. 2, §1**:

1. **Encoder:** \(P(\text{notes}\mid\text{audio})\)  
   Onsets and Frames transcription model.

2. **Prior:** \(P(\text{notes})\)  
   Music Transformer generating performance MIDI autoregressively.

3. **Decoder:** \(P(\text{audio}\mid\text{notes})\)  
   MIDI-conditioned WaveNet synthesizer.

Therefore:

> **MIDI is “latent” in the probabilistic sense that it mediates between audio and the audio-generating process, but “explicit symbolic bottleneck” or “intermediate representation” is more precise than “latent space.”**

The Figure 1 caption itself uses quotation marks around the transcription model “encodes” audio as MIDI (**p. 2, Fig. 1**), reinforcing that this is a conceptual factorization rather than a conventional learned latent encoder.

---

### What the MIDI representation means here

This is **performance MIDI**, not merely a symbolic score.

The dataset MIDI includes:

- note pitches and timings,
- key-strike velocities,
- sustain-pedal positions,
- performance timing.

The paper states this on **p. 3, §3**.

The MIDI therefore represents much of **what was played and how it was performed**, but not the complete waveform realization. It does not directly represent:

- room acoustics,
- microphone placement,
- pedal and string noise beyond MIDI events,
- breathing and audience sounds,
- detailed instrument timbre,
- all expressive waveform-level behavior.

The authors explicitly report that WaveNet reproduces “the response of the room, breathing of the player, and shuffling of listeners” (**p. 7, §6**). These details are learned by the audio decoder, not stored explicitly in MIDI.

A further implementation nuance is important:

> The WaveNet does not consume the entire event-level MIDI file directly. Its input is an 88-dimensional onset piano roll at 4-ms resolution, with onset velocity in \([0,1]\) (**p. 7, §6**).

Thus, the symbolic prior and the audio decoder do not necessarily expose exactly the same representation. The Transformer models event-based MIDI; WaveNet receives an onset/velocity conditioning signal.

---

### 3. Wave2Midi2Wave architecture

### Figure 1: system structure

**p. 2, Figure 1** depicts three paths:

```text
audio
  │
  ▼
Onsets & Frames transcription
  │
  ▼
piano-roll / MIDI representation
  │
  ▼
Music Transformer event prediction
  │
  ▼
conditional WaveNet
  │
  ▼
synthesized audio
```

The three functions are factorized according to the proposed musician/instrument division:

- **Transcription:** audio → symbolic performance
- **Symbolic modeling:** symbolic performance → new symbolic performance
- **Synthesis:** symbolic performance → waveform

The intended timescale division is:

- audio waveform: sub-millisecond/local detail,
- note events: musical events and performance timing,
- Transformer sequence: phrases and approximately one-minute structure.

The authors claim that the system models coherent structure over approximately six orders of magnitude, from roughly **0.1 ms to 100 seconds** (**abstract, p. 1**).

### Why factorize?

The authors’ stated advantages are (**p. 3, §1**):

- greater human interpretability and manipulation,
- modularity,
- independent replacement of performance and instrument models,
- longer symbolic modeling horizons,
- reuse of prior symbolic-generation and conditional-audio techniques,
- ability to transcribe otherwise unlabeled piano audio and use it for training.

This is best understood as a **structured, editable bottleneck**, not as an explanation mechanism by itself.

---

### 4. MAESTRO dataset

### Dataset composition

**Table 1, p. 3:**

| Split | Performances | Compositions | Hours | Size | Notes |
|---|---:|---:|---:|---:|---:|
| Train | 954 | 295 | 140.1 | 83.6 GB | 5.06M |
| Validation | 105 | 60 | 15.3 | 9.1 GB | 0.54M |
| Test | 125 | 75 | 16.9 | 10.1 GB | 0.57M |
| **Total** | **1,184** | **430** | **172.3** | **102.8 GB** | **6.18M** |

The data came from nine years of the International Piano-e-Competition:

- Yamaha Disklavier performances,
- virtuoso pianists,
- acoustic piano audio,
- high-resolution captured MIDI,
- 44.1–48 kHz, 16-bit stereo audio,
- approximately 3-ms audio/MIDI alignment.

The repertoire is mostly classical, broadly covering composers from the seventeenth through early twentieth centuries.

The split prevents the **same composition** from appearing in multiple subsets (**p. 4, §3.2**), although popular compositions performed by many contestants were preferentially assigned to training.

### Comparison with earlier datasets

**Table 2, p. 4:**

| Dataset | Performances | Compositions | Hours | Notes |
|---|---:|---:|---:|---:|
| SMD | 50 | 50 | 4.7 | 0.15M |
| MusicNet | 156 | 60 | 15.3 | 0.58M |
| MAPS | 270 | 208 | 17.9 | 0.62M |
| MAESTRO | 1,184 | ~430 | 172.3 | 6.18M |

The authors’ main argument is scale plus natural human performance. MAPS contains a substantial amount of synthesized or sequencer-created audio; MusicNet uses separately sourced scores with less reliable alignment; SMD is much smaller.

### Alignment pipeline

The appendix gives a substantial alignment procedure:

- synthesize MIDI using FluidSynth;
- compare real and synthesized audio using CQT features;
- coarse alignment with a 4096-sample hop, approximately 90 ms;
- 48 CQT bins corresponding to MIDI notes C2–B5;
- dB normalization and an −80 dB cutoff;
- MSE-based alignment;
- manual repair of several MIDI clock failures;
- segmentation at long MIDI silences;
- one-second padding at segment boundaries;
- fine alignment with DTW;
- 22,050-Hz mono audio;
- hop length 64, approximately 3 ms;
- cosine distances inside a 2.5-second Sakoe–Chiba band.

These details are in **pp. 11–12, Appendix**.

---

### 5. Training and models

### Piano transcription

**§4, pp. 5–6.**

The transcription model extends **Onsets and Frames** with:

- an offset-detection head;
- offset labels covering 32 ms after note end;
- bidirectional LSTM layers increased from 128 to 256 units;
- convolutional filters changed from 32/32/64 to 48/48/96;
- fully connected layer increased from 512 to 768 units;
- no gradient propagation from frame detection into the onset network;
- unweighted frame loss;
- HTK mel-frequency spacing;
- optional SoX audio augmentation.

Training lasted **670,000 steps**.

#### MAPS result

With audio augmentation, Table 4 reports:

- frame F1: **84.91**
- note F1: **86.44**
- note-with-offset F1: **67.43**
- note-with-offset-and-velocity F1: **51.77**

#### MAESTRO test result

Without augmentation, Table 5 reports:

- frame: P/R/F1 = **92.11 / 88.41 / 90.15**
- note: **98.27 / 92.61 / 95.32**
- note with offset: **82.95 / 78.24 / 80.50**
- note with offset and velocity: **79.89 / 75.37 / 77.54**

Audio augmentation improved MAPS generalization but slightly worsened MAESTRO test performance (**Table 6, p. 6**).

### Music Transformer

**§5, p. 6.**

The symbolic model uses the decoder of the Music Transformer with relative self-attention. The paper refers to the earlier Music Transformer paper for architecture details.

Training:

- random crops of **2,048 events**;
- pitch transposition between a minor third below and above;
- time-stretch factors:

\[
\{0.95, 0.975, 1.0, 1.025, 1.05\}.
\]

Two models were trained:

- on ground-truth MAESTRO MIDI;
- on transcribed **MAESTRO-T** MIDI.

Validation NLL (**Table 7, p. 6**):

| Model | Validation NLL |
|---|---:|
| Ground-truth MAESTRO MIDI | 1.84 |
| MAESTRO-T transcribed MIDI | 1.72 |

MAESTRO-T is generated by transcribing MAESTRO training audio. The authors acknowledge that this audio was also used to train the transcription model, although they argue that train/validation/test transcription scores are similar (**p. 6**).

### WaveNet synthesis

**§6, pp. 6–7.**

The WaveNet:

- is autoregressive;
- uses a larger receptive field than the earlier baseline;
- was tested with six stacks of ten residual layers;
- ultimately used two sequential stacks of six layers;
- produces 16-bit output with a mixture-of-logistics output distribution;
- receives an 88-key onset piano roll at 250 Hz / 4-ms resolution.

Three models were trained:

1. **Unconditioned:** audio only.
2. **Ground:** audio conditioned on ground-truth MIDI.
3. **Transcribed:** audio conditioned on inferred MIDI.

After one million training steps, losses were:

- unconditioned: **3.72**
- ground: **3.70**
- transcribed: **3.84**

The paper explicitly warns that teacher forcing makes these losses poor indicators of conditioning quality.

Two practical limitations are candidly reported:

- long samples can exhibit **timbral shifts** due to heterogeneous recording conditions;
- arbitrary windows can produce a sonic crash at the beginning, so the authors trim the first **two seconds** from reported outputs.

---

### 6. Listening evaluation

**§7, pp. 7–8; Figure 2, p. 8.**

The study used 20-second clips from:

- real recordings;
- unconditioned WaveNet;
- ground-truth MIDI-conditioned WaveNet;
- transcribed-MIDI WaveNet;
- transcribed-MIDI plus Transformer-generated MIDI.

There were **640 ratings**, with each source involved in 128 pairwise comparisons.

Figure 2’s visual ranking is approximately:

1. ground-truth recordings;
2. ground-truth MIDI-conditioned WaveNet;
3. transcribed-MIDI WaveNet;
4. transcribed-MIDI plus Transformer;
5. unconditioned WaveNet.

The paper reports:

\[
\chi^2(2)=67.63,\quad p<0.001.
\]

Post-hoc Wilcoxon tests with Bonferroni correction found no statistically significant difference between real recordings and the Ground/Test or Transcribed/Test samples at the stated threshold (**p. 8**).

Important qualification: this is a **20-second realism test**, not a test of long-form composition quality, symbolic correctness, source identity, or explanation faithfulness.

---

### 7. What the paper does and does not establish

### It does establish

- A practical factorization of piano modeling into transcription, symbolic generation, and waveform synthesis.
- A high-quality paired audio/MIDI dataset.
- A human-editable symbolic interface.
- Better long-range structure than unconditional sample-level audio generation.
- Strong piano transcription performance.
- Realistic short audio synthesis conditioned on symbolic events.
- Modular replacement of the symbolic and synthesis components.

### It does not establish

- A learned continuous MIDI latent manifold.
- Joint end-to-end optimization of all three modules.
- A faithful posterior \(P(\text{notes}\mid\text{audio})\) coupled to the prior and decoder.
- That MIDI fully explains the waveform.
- That generated symbolic decisions are accompanied by reasons or provenance.
- That generated music preserves source identity.
- That the approach supports multi-instrument or multi-track mashups.
- That it solves composition-level evaluation.
- That the audio model can independently manipulate all MIDI dimensions.

The paper’s use of “interpretable” means primarily **human-readable and manipulable intermediate events**. It does not mean mechanistic interpretability, causal explanations, rationale graphs, or verified explanation faithfulness.

---

### 8. Limitations relevant to symbolic mashups

1. **Single instrument:** piano only.
2. **Narrow repertoire:** mostly classical competition performances.
3. **No multi-source provenance:** MIDI events do not identify whether a note came from source A, source B, or the model.
4. **No mashup task:** no alignment, conflict diagnosis, source preservation, or recomposition benchmark.
5. **No explicit musical roles:** melody, bass, harmony, voice, texture, and phrase function are not represented as separate explanatory objects.
6. **Decoder mismatch:** the Transformer operates on event-based MIDI, while WaveNet conditions on onset/velocity piano rolls.
7. **Transcription errors:** symbolic generation inherits errors from audio transcription.
8. **Potential data leakage in MAESTRO-T:** the transcribed training audio was also used in transcription training.
9. **Short listening test:** only 20-second excerpts were evaluated.
10. **Generation artifacts:** first-two-second crashes and long-sample timbral shifts required engineering workarounds.
11. **No causal explanation:** editing a note provides an intervention, but the model does not explain why the note was selected.

For your research, the most useful interpretation is:

> Wave2Midi2Wave provides an editable symbolic control layer, but not yet a provenance-preserving or explanation-faithful recomposition system.

---

### 9. Modern spins

The following are verified from primary arXiv records. They represent several distinct directions rather than one unified successor.

### A. Better symbolic representations

#### Music Transformer — Huang et al., arXiv:1809.04281

Uses efficient relative self-attention for longer musical sequences, motif continuation, and melody-conditioned accompaniment.

**Relevance:** establishes the immediate symbolic-generation foundation used by Wave2Midi2Wave.

#### Pop Music Transformer — Huang & Yang, arXiv:2002.00212

Introduces a beat-aware representation with explicit beat/bar/phrase structure and flexible tempo changes.

**Relevance:** makes metrical structure more explicit than generic event serialization. Useful for phrase-aware mashup alignment.

#### Compound Word Transformer — Hsiao et al., arXiv:2101.02402

Groups related attributes such as pitch, duration, velocity, and placement into compound tokens, with type-specific Transformer heads.

**Relevance:** reduces sequence length and preserves attribute structure. A useful alternative to treating every MIDI attribute as an independent language token.

#### MusicBERT — Zeng et al., arXiv:2106.05630

Uses OctupleMIDI encoding and bar-level masking for large-scale symbolic music understanding.

**Relevance:** useful as a symbolic encoder for matching, style classification, melody completion, or source-identity analysis. It is primarily an understanding model, not an explanation-generating model.

#### MidiTok — Fradet et al., arXiv:2310.17202

An extensible tokenizer library supporting multiple MIDI serialization schemes.

**Relevance:** practical infrastructure for comparing event, beat-based, compound, and attribute-aware representations without conflating tokenization with latent learning.

---

### B. Multi-track generation and inpainting

#### MMM — Ens & Pasquier, arXiv:2008.06048

The Multi-Track Music Machine serializes each track separately and concatenates tracks, supporting:

- track-level inpainting;
- bar-level inpainting;
- instrumentation control;
- note-density control.

**Relevance:** probably the most directly useful symbolic precedent for mashup recomposition. It treats tracks as explicit editable units rather than merely interleaved events.

#### PopMAG — Ren et al., arXiv:2008.07703

Introduces MuMIDI for simultaneous multi-track generation, models multiple note attributes together, and adds long-context memory.

**Relevance:** addresses cross-track harmony and long-range accompaniment, both central to mashups.

#### SongDriver — Wang et al., arXiv:2209.06054

Separates real-time accompaniment into chord arrangement and playable multi-track prediction, with cached future chords and low-latency generation.

**Relevance:** useful for interactive or musician-in-the-loop mashup systems, though it is accompaniment rather than general recomposition.

---

### C. More controllable symbolic interfaces

#### MuseCoco — Lu et al., arXiv:2306.00110

Uses a two-stage design:

```text
text → musical attributes → symbolic music
```

The attributes act as an intermediate control layer. The paper reports control over musical properties and a 1.2-billion-parameter model.

**Relevance:** attributes could become explicit mashup controls such as tempo, density, instrumentation, register, harmony, or texture.

**Important limitation:** attribute conditioning is not automatically an explanation. The system still needs provenance and counterfactual tests to establish explanation faithfulness.

#### ChatMusician — Yuan et al., arXiv:2402.16153

Continually pretrains and fine-tunes LLaMA2 using ABC notation as a text-compatible musical representation. It supports conditioning on chords, melodies, motifs, and musical forms.

**Relevance:** demonstrates an LLM-style symbolic interface.

**Limitation:** ABC text is human-readable, but the LLM’s internal reasoning remains opaque, and textual fluency does not guarantee valid musical constraints or faithful rationales.

---

### D. More interpretable audio synthesis

#### MIDI-DDSP — Wu et al., arXiv:2112.09312

A hierarchical model with three levels:

```text
notes → performance attributes → DDSP synthesis parameters → audio
```

It explicitly models properties such as:

- timbre,
- vibrato,
- dynamics,
- articulation.

Users can intervene at each hierarchy level or rely on learned priors.

**Relevance:** this is a strong modern successor to the WaveNet decoder for explainable control. It separates:

- what notes are played,
- how they are performed,
- how the instrument produces sound.

That hierarchy is more suitable for explanation than a single opaque waveform decoder.

---

### E. True learned latent alternatives

These should not be confused with Wave2Midi2Wave’s explicit MIDI bottleneck.

#### MusicVAE — Roberts et al., arXiv:1803.05428

A hierarchical VAE for musical note sequences with a learned latent vector. It explicitly targets sampling, interpolation, reconstruction, and long-term structure.

**This is a genuine learned latent space** in the usual VAE sense.

#### Jukebox — Dhariwal et al., arXiv:2005.00341

Uses multiscale VQ-VAE codes for raw audio and autoregressive Transformers.

**This is a learned discrete audio latent representation, not MIDI.** It is powerful for audio generation but much less directly editable at the note/provenance level.

#### MusicGen — Copet et al., arXiv:2306.05284

Uses compressed discrete audio tokens with a single-stage Transformer and supports text or melodic conditioning.

Again, these are **audio codec tokens**, not symbolic note representations. They offer controllability but not the same inspectability as MIDI.

---

### 10. Implications for your symbolic-mashup research

A promising modern architecture would retain the paper’s central idea but extend the representation:

```text
audio source A/B
    ↓
transcription and score/performance extraction
    ↓
provenance-preserving symbolic graph
    ├── source identity
    ├── voice/track role
    ├── phrase and motif identity
    ├── harmony and meter
    ├── protected notes
    └── detected conflicts
    ↓
alignment / transformation / repair / inpainting
    ↓
multi-track symbolic generator
    ↓
hierarchical expressive renderer
```

The key distinction is:

- **Wave2Midi2Wave:** MIDI is an explicit, editable performance bottleneck.
- **Your target system:** the symbolic layer should additionally encode provenance, musical roles, conflicts, repair operations, and reasons.

For explainable mashups, MIDI should therefore be treated as the **กลาง control and evidence layer**, not as a complete explanation. A defensible explanation would need to state:

1. which source contributed each event;
2. which conflict was detected;
3. which notes were protected or changed;
4. what transformation was applied;
5. why that operation improved compatibility;
6. what counterfactual alternatives were rejected.

That capability is absent from the 2019 paper but can be built on its factorized architecture.

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
