---
title: "Pop Music Transformer: Beat-based Modeling and Generation of Expressive Pop Piano Compositions"
authors: "Yu-Siang Huang and Yi-Hsuan Yang"
year: 2020
doi: 10.48550/arXiv.2002.00212
category: generation-and-planning
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/huang-2020-pop-music-transformer-beat-based.pdf"
pdf_filename: huang-2020-pop-music-transformer-beat-based.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
---
## One-line Summary

The authors argue that Transformer music generation benefits substantially from a better **symbolic event representation**, not only from architectural innovation.

## 1. Document Information

- **Canonical source:** arXiv `2002.00212v3`; official PDF preserved as `huang-2020-pop-music-transformer-beat-based.pdf`.
- **Full-paper evidence:** delegate digest `del_mv40l1x9_ahrt.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### Evidence-grounded digest

### Bibliography and scope

- **Yu-Siang Huang and Yi-Hsuan Yang**, “**Pop Music Transformer: Beat-based Modeling and Generation of Expressive Pop Piano Compositions**.”
- arXiv:**2002.00212v3**, category **[cs.SD]**, dated **10 August 2020**.
- Published in **28th ACM International Conference on Multimedia (MM ’20)**, October 12–16, 2020, Seattle; ACM, 9 pages.
- DOI: **10.1145/3394171.3413671**.
- Evidence: `/tmp/paper-digest/2002.00212v3.pdf`, p. 1; extracted text `/tmp/paper-digest/2002.00212v3.txt:1-48`.
- I inspected all nine PDF pages, including every figure and table. **There is no appendix in v3**; pp. 8–9 contain the conclusion, acknowledgement, and references.

### Central contribution

The authors argue that Transformer music generation benefits substantially from a better **symbolic event representation**, not only from architectural innovation.

Their representation, **REMI** (“revamped MIDI-derived events”), makes the following explicit:

1. bar boundaries;
2. quantized positions within each bar;
3. note duration;
4. local tempo;
5. chord labels.

The claimed result is better rhythmic regularity and subjective preference over a Transformer-XL adaptation of Music Transformer.

This is an author claim; the empirical evidence is specifically for **expressive solo Pop piano**, not general music generation.

---

### Representation and timing

#### Conventional MIDI-like representation

The baseline follows the event representation of Oore et al. [30] and Music Transformer [23]:

| Musical property | Event |
|---|---|
| Pitch onset | `Note-On`, pitch 0–127 |
| Pitch offset | `Note-Off`, pitch 0–127 |
| Relative timing | `Time-Shift`, 10–1000 ms |
| Dynamics | `Note Velocity`, quantized to 32 levels |

`Time-Shift` expresses the relative time gap between successive events. The authors argue that timing mistakes accumulate during autoregressive inference, even though teacher forcing can hide such problems during training.

Evidence: PDF pp. 1, 3–4; `.txt:56-93, 182-216`.

#### REMI representation

REMI replaces or augments these events as follows:

| REMI event | Specification |
|---|---|
| `Bar` | Starts a new bar |
| `Position` | One of 16 positions within a bar |
| `Note Velocity` | 32 quantized levels |
| `Note-On` | MIDI pitch 0–127 |
| `Note Duration` | 1–64 multiples of a 32nd note |
| `Tempo Class` / `Tempo Value` | Local tempo, 30–209 BPM |
| `Chord` | 60 root/quality symbols |

The data use **4/4 music**, so each bar has four beats and the bar is quantized into **Q = 16 sixteenth-note positions**.

A note is serialized as:

```text
Note Velocity → Note-On → Note Duration
```

This makes note length explicit instead of requiring the model to learn the pairing between distant `Note-On` and `Note-Off` events.

A representative sequence in Figure 3 is:

```text
Bar,
Position(1/16),
Chord(C:maj),
Position(1/16),
Tempo Class(mid),
Tempo Value(10),
Position(1/16),
Note Velocity(16),
Note On(60),
Note Duration(4),
Position(5/16),
Tempo Value(12),
Position(9/16),
Note Velocity(14),
Note On(67),
Note Duration(8),
Bar
```

Evidence: PDF pp. 1, 3; Figure 3, p. 3; `.txt:96-148`.

#### Relative timing versus metrical timing

REMI does **not** primarily represent time as a sequence of relative delays. Instead:

- `Bar` resets the larger metrical context.
- `Position` provides an absolute quantized location within the bar.
- `Tempo` changes the conversion from metrical time to physical seconds.
- `Note Duration` represents rhythmic length explicitly.

Tempo events are inserted once per beat, allowing local tempo variation and expressive rubato while preserving the metrical grid.

This is a useful separation between:

```text
metrical location = Bar + Position
physical time = metrical location + local Tempo
note length = Note Duration
```

The paper’s preliminary tests found that 32nd- or 64th-note grids produced fragmented, unpleasant generations with the adopted Transformer-XL. The authors therefore retained Q = 16.

Evidence: PDF pp. 3–5; `.txt:182-228, 331-344`.

---

### Chord representation and preprocessing

#### Chord recognition

The 60 chord types are:

- 12 chromatic roots;
- five qualities: major, minor, diminished, augmented, dominant.

The authors use a heuristic symbolic chord-recognition procedure:

1. compute binary chroma features for each tick;
2. use 2-beat and 4-beat sliding windows;
3. treat active notes as candidate roots;
4. score pitch intervals against the rule table in Table 2;
5. recursively assign the highest-scoring chord label.

The chord token is explicitly described as a **symbol**: the model still generates the actual notes separately through `Note-On` events.

Evidence: PDF pp. 4–5, Table 2; `.txt:229-245, 329-343`.

#### Beat, downbeat, and transcription pipeline

The training pipeline is:

```text
audio
→ automatic piano transcription
→ beat/downbeat tracking
→ chord recognition
→ REMI event sequence
→ Transformer-XL
```

Specifically:

- `Onsets and Frames` estimates pitch, onset, offset, and velocity.
- A recurrent beat/downbeat tracker supplies beat and downbeat positions.
- Tick positions between beats are linearly interpolated.
- Onsets and offsets are aligned to the nearest tick and then quantized to the sixteenth-note grid.

This is important: REMI is not simply a hand-designed encoding of clean symbolic scores. Its labels depend on automatic transcription, beat tracking, and heuristic chord recognition.

Evidence: Figure 2, PDF pp. 2 and 5; `.txt:315-343`.

---

### Model and training

The model is a single autoregressive **Transformer-XL**, not separate networks for notes, rhythm, tempo, and harmony.

Configuration:

- 12 self-attention layers;
- 8 attention heads;
- approximately 41 million parameters;
- input segment length: 512 events;
- recurrence/cache length: 512 events;
- mini-batch size: 16;
- NVIDIA V100;
- cross-entropy training objective.

The authors state that Transformer-XL gave better perceived temporal coherence than their non-XL Transformer implementation, but they omit a direct XL-versus-non-XL comparison because Transformer-XL music generation had already been reported elsewhere.

All event types are modeled jointly. Figure 4 shows that:

- Baseline 1 struggles particularly with `Time-Shift`;
- `Note-Off` has higher loss than `Note-On`;
- REMI `Position` events are learned relatively easily.

Evidence: PDF pp. 4 and 6; Figure 4; `.txt:246-305, 378-410`.

#### Dataset

- **775** Pop piano performances;
- approximately **48 hours**;
- covers of Japanese anime, Korean popular, and Western popular songs;
- performed by different pianists;
- piano only;
- all selected pieces are in **4/4**.

The authors planned to release transcribed MIDI and REMI event sequences rather than audio because of copyright restrictions.

Evidence: PDF p. 5, §5.1; `.txt:316-344`.

---

### Baselines

The comparison uses three Transformer-XL variants:

1. **Baseline 1**  
   `Note-Off` + `Time-Shift` in 10–1000 ms units.

2. **Baseline 2**  
   Replaces `Note-Off` with `Note Duration`, but retains millisecond `Time-Shift`.

3. **Baseline 3**  
   Uses `Note Duration` and a sixteenth-note-multiple `Time-Shift`, making its grid closer to REMI.

This is a reasonably informative ablation: it separates the effect of explicit duration from the effect of explicit bar/position structure.

Evidence: PDF p. 6, §5.2; `.txt:378-397`.

---

### Objective evaluation

Each model generates:

- 1,000 sequences;
- 4,096 events per sequence;
- temperature-controlled top-k sampling;
- conversion to MIDI;
- piano-synthesized audio;
- re-analysis using a joint beat/downbeat tracker.

Metrics:

- **Beat STD**: standard deviation of inter-beat intervals;
- **Downbeat STD**: standard deviation of inter-downbeat intervals;
- **Downbeat salience**: average tracker confidence for downbeats.

The authors compare generated values to the training-data values. They explicitly note that small STD can mean excessive rigidity, while large STD can mean instability.

#### Table 3 results

Values are:

| Method | Beat STD | Downbeat STD | Downbeat salience |
|---|---:|---:|---:|
| Baseline 1 | 0.0968 | 0.3561 | 0.1033 |
| Baseline 2 | 0.0394 | 0.1372 | 0.1651 |
| Baseline 3 | 0.0396 | 0.1383 | 0.1702 |
| REMI + Tempo + Chord | 0.0386 | 0.1376 | 0.2279 |
| REMI + Tempo | 0.0363 | 0.1265 | 0.1936 |
| REMI + Chord | 0.0292 | 0.0932 | 0.1742 |
| REMI without Tempo/Chord | 0.0199 | 0.0595 | 0.1880 |
| Training data | 0.0607 | 0.2163 | 0.2055 |

Evidence: PDF p. 6, Table 3; `.txt:355-373`.

#### Author interpretation

The paper claims:

- Baseline 1 has notably unstable rhythm.
- Explicit `Note Duration` improves rhythmic stability.
- REMI models have stronger downbeat salience.
- Models without tempo have lower STD than the training data, suggesting that tempo events are needed for expressive rhythmic freedom.
- `Position` and `Bar` improve metrical regularity.

A careful qualification: the objective metric does not directly measure musical quality. It measures how a beat/downbeat tracker responds to synthesized audio, and “closer to training data” is treated as better. The full REMI configuration does not uniformly minimize distance to the training statistics.

---

### Subjective listening study

The listening study uses:

- 100 additional Pop piano performances;
- no overlap with training data;
- first four bars as prompts;
- 16 generated continuation bars;
- three systems:
  - Baseline 1;
  - Baseline 3;
  - REMI **without Chord**.

The chord token was omitted so that rhythmic differences would dominate the comparison.

Participants:

- 76 total;
- 51 classified as “pros” because they understood basic music theory and had amateur-musician experience;
- each participant evaluated two randomly selected sample sets;
- each set contained outputs from all three systems;
- participants selected the most-liked and least-liked sample using any criterion.

#### Mean preference scores

Scale: 1 = least liked, 3 = most liked.

| Group | Baseline 1 | Baseline 3 | REMI |
|---|---:|---:|---:|
| Pros | 1.77 | 2.03 | 2.20 |
| Non-pros | 1.66 | 1.90 | 2.44 |
| All participants | 1.73 | 1.98 | 2.28 |

#### Pairwise results

| Pair | REMI/system wins | Losses | p-value |
|---|---:|---:|---:|
| REMI vs Baseline 1 | 103 | 49 | 5.623e-5 |
| REMI vs Baseline 3 | 92 | 60 | 0.0187 |
| Baseline 3 vs Baseline 1 | 90 | 62 | 0.0440 |

The authors report REMI as preferred by both pros and non-pros, with the REMI-versus-Baseline-1 difference significant at p < 0.01.

Evidence: PDF pp. 7–8, Tables 4–5; `.txt:452-500`.

Qualification: this is a small online social-network study with a free-form evaluation criterion, not a blinded laboratory study with standardized musicality dimensions.

---

### Controllable generation

The authors demonstrate control by masking the output probabilities of selected events.

- Prohibiting `F minor` causes the model to choose harmonically related alternatives.
- Forcing a high `Tempo Class` changes both tempo values and generated note events.
- Figure 6 shows these effects over continuations after a four-bar prompt.

This is conditional decoding over explicit event types, not a learned disentangled latent space.

Evidence: PDF p. 8, Figure 6, §5.5; `.txt:483-501`.

---

### Limitations

#### Explicitly acknowledged by the authors

- Q = 16 cannot represent fine timing, triplets, swing, or microtiming well.
- Finer 32nd/64th-note grids caused fragmented generations with the adopted Transformer-XL.
- The dataset is restricted to 4/4.
- The work covers Pop piano rather than multiple instruments.
- Future work is needed for longer-term structure and longer-context architectures.
- The authors propose adding groove, emotion, guitar, bass, drums, lyrics, and video conditioning.

Evidence: PDF pp. 5 and 8; §6; `.txt:331-344, 542-558`.

#### Additional methodological limitations

These are interpretations based on the design:

- Automatic transcription and beat/downbeat/chord recognition introduce label noise.
- Chord labels are restricted to 60 heuristic categories.
- The subjective evaluation does not test repair, infilling, multi-track arrangement, or long-form composition.
- The objective metrics are tracker-derived proxies rather than direct measures of musical coherence.
- The paper does not report a modern held-out likelihood comparison, calibration analysis, or systematic error analysis.
- The “latent” structure is imposed as observable tokens; the model does not learn a continuous, disentangled latent representation.

---

### Relevance to explicit symbolic latent spaces

#### What transfers directly

REMI is a strong design precedent for **structured symbolic spaces**:

- rhythm is represented by `Bar` and `Position`;
- note articulation is represented by `Note Duration`;
- performance timing is separated into local tempo;
- harmony is represented by explicit chord symbols;
- all variables remain editable and inspectable.

For an explainable music system, this is valuable because a generated event can be attributed to a recognizable musical factor rather than an opaque embedding dimension.

#### Important distinction

REMI is not an explicit latent-space model in the representation-learning sense. It is:

```text
hand-designed symbolic vocabulary
+ autoregressive Transformer-XL
```

There is no encoder, continuous latent variable, disentanglement objective, or learned bar-level latent code. A modern system could therefore use REMI as the **observable symbolic interface** while learning higher-level latent variables over bars, phrases, harmony, groove, or arrangement roles.

---

### Relevance to mashups

#### Interpretation and concrete direction

REMI’s shared `Bar`/`Position` coordinate is naturally suited to mashup alignment:

1. beat-track and downbeat-track each source;
2. map all sources into a common bar-position grid;
3. represent tempo separately from metrical position;
4. encode source-specific harmony, melody, bass, and groove;
5. condition generation on selected tracks while masking others.

Potential experiment:

- preserve vocal/melody events from source A;
- preserve groove or drum-like rhythmic descriptors from source B;
- generate piano accompaniment under a selected chord progression;
- evaluate bar-boundary alignment, harmonic clash rate, beat consistency, and human preference.

A missing capability is explicit multi-instrument identity. REMI’s paper only models solo piano, so a mashup extension needs track/instrument tokens and cross-track attention.

---

### Relevance to symbolic repair

REMI offers several repair advantages:

- `Note Duration` avoids dangling `Note-On`/`Note-Off` pairs.
- `Bar` and `Position` provide stable repair boundaries.
- chord and tempo events can be held fixed while repairing notes.
- explicit event masks can impose constraints during decoding.

Concrete repair model:

```text
corrupted REMI span
→ bar-aware masked-span Transformer
→ constrained reconstruction
→ preserve fixed events and boundary context
```

Suggested evaluations:

- exact recovery of held-out events;
- edit distance from the original;
- onset/offset boundary continuity;
- chord consistency;
- beat/downbeat stability;
- human ratings of “seamlessness” and “intent preservation.”

This would extend the paper beyond left-to-right continuation, which is the only generation task actually evaluated.

---

### Concrete research ideas

1. **Hierarchical REMI latent space**  
   Learn phrase/bar embeddings above event tokens, with separate latent factors for harmony, rhythm, tempo, and performance expression. Test whether interventions in one factor preserve the others.

2. **Uncertainty-aware REMI preprocessing**  
   Preserve beat-tracker, transcription, and chord-recognition confidence instead of converting each MIR output into a hard label.

3. **Microtiming residuals**  
   Keep `Bar + Position` as the stable grid, then model continuous onset residuals for swing, triplets, and expressive timing.

4. **Bar-aware masked repair**  
   Train with randomly masked bars and constrained reconstruction, including cases where only harmony, rhythm, or dynamics are corrupted.

5. **Cross-source mashup conditioning**  
   Use shared metrical coordinates but separate source/style streams. Control which source supplies melody, harmony, groove, or accompaniment.

6. **Modern long-context comparison**  
   Compare Transformer-XL with hierarchical attention, bar-level memory, state-space models, and diffusion/insertion models while keeping the REMI vocabulary fixed.

7. **Better evaluation**  
   Combine tracker metrics with event-level validity, repetition/novelty, harmonic consistency, boundary continuity, edit locality, and controlled listening studies.

**Bottom line:** the paper’s lasting contribution is not merely “use Transformer-XL for Pop piano.” It demonstrates that explicit, musically meaningful symbolic coordinates—especially bar position, duration, tempo, and chord—can make generation more controllable, rhythmically coherent, and easier to inspect.

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
