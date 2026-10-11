---
title: "POP909: A Pop-song Dataset for Music Arrangement Generation"
authors: "Ziyu Wang, Ke Chen, Junyan Jiang, Yiyi Zhang, Maoran Xu, Shuqi Dai, Xianbin Gu, and Gus Xia"
year: 2020
doi: 10.48550/arXiv.2008.07142
category: data-and-representation
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/wang-2020-pop909-a-pop-song-dataset.pdf"
pdf_filename: wang-2020-pop909-a-pop-song-dataset.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
---
## One-line Summary

1. A style-consistent piano arrangement rather than arbitrary extracted tracks. 2. Precise alignment to a source representation: lead melody, audio, or full score. 3. External annotations such as beat, downbeat, key, and chord labels.

## 1. Document Information

- **Canonical source:** arXiv `2008.07142v1`; official PDF preserved as `wang-2020-pop909-a-pop-song-dataset.pdf`.
- **Full-paper evidence:** delegate digest `del_mv40f079_a1nd.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### POP909 digest

### 1. Bibliography and version

**Ziyu Wang, Ke Chen, Junyan Jiang, Yiyi Zhang, Maoran Xu, Shuqi Dai, Xianbin Gu, and Gus Xia.** “POP909: A Pop-song Dataset for Music Arrangement Generation.” *Proceedings of the 21st International Society for Music Information Retrieval Conference*, Montréal, Canada, 2020.

- arXiv: **2008.07142v1 [cs.SD]**, 17 August 2020.
- Wang and Chen are marked as equal contributors.
- The paper itself carries a **Creative Commons Attribution 4.0 International License (CC BY 4.0)** attribution notice (PDF p. 1, footer).
- Dataset URL given by the authors: `https://github.com/music-x-lab/POP909-Dataset` (PDF p. 2, footnote 1).
- The paper does **not clearly specify a separate license for the dataset files or source audio**. The CC BY notice should not automatically be interpreted as licensing copyrighted song audio.

I inspected all **8 PDF pages**. Pages 7–8 contain references only.

---

### 2. Core contribution

#### Author claims

POP909 is intended to address three dataset requirements (PDF pp. 1–3, §§1, 2.3):

1. A style-consistent piano arrangement rather than arbitrary extracted tracks.
2. Precise alignment to a source representation: lead melody, audio, or full score.
3. External annotations such as beat, downbeat, key, and chord labels.

The dataset contains:

- **909 popular songs**
- Approximately **60 hours** of arrangements
- Songs by **462 artists**
- Release dates spanning approximately the **1950s–2010**
- Multiple piano-arrangement revisions per song
- MIDI tracks aligned to corresponding audio using manually labelled tempo curves

The authors frame two primary tasks (PDF p. 2, §1):

- **Task 1:** piano accompaniment generation conditioned on melody and auxiliary annotations.
- **Task 2:** audio-to-piano re-orchestration from a full orchestral recording.

They also mention unconditional symbolic generation and expressive performance rendering.

#### Interpretation

POP909 is primarily a **source-conditioned piano accompaniment dataset**, not a general-purpose multitrack pop-production dataset. Its strongest contribution is the combination of:

- separated musical roles,
- human-created arrangement targets,
- revisions,
- performance timing,
- beat/chord/key metadata.

---

### 3. Dataset structure and musical representation

#### MIDI content

Each qualified arrangement contains three tracks (PDF p. 3, §3.2; Fig. 2):

- **MELODY:** lead/vocal melody transcription.
- **BRIDGE:** secondary melodies or lead instruments.
- **PIANO:** accompaniment textures such as broken chords and arpeggios.

The authors define **BRIDGE + PIANO** as the complete piano accompaniment arrangement.

The MIDI includes expressive velocities based on the original audio. This makes the data performance-oriented rather than purely quantized score data.

#### Folder layout

The paper’s Figure 3 gives this structure (PDF p. 4, §3.3):

```text
POP909/
  Song 001/
    001.mid
    beat_audio.txt
    beat_midi.txt
    chord_midi.txt
    chord_audio.txt
    key_audio.txt
    versions/
      001-v1.mid
      001-v2.mid
      001-v3.mid
  ...
  Song 909/
  Index File
```

The root index contains song name, artist, number of modifications, and other metadata.

The paper says the collection began with 1,000 songs and retained 909 songs judged to have high arrangement quality. Both the final qualified version and unqualified intermediate versions are released.

#### Dataset-table evidence

Table 1 (PDF p. 2) compares datasets using:

- polyphony,
- lead melody,
- audio,
- time alignment,
- beat/key/chord annotation,
- score/performance modality.

POP909 is the only listed dataset marked as having all of:

- polyphony,
- lead melody,
- audio pairing,
- time alignment,
- beat, key, and chord annotations,
- score and performance modalities.

The table rounds POP909’s size to **“1k”**, while the paper’s main text consistently states **909 songs**. Likewise, the table lists Lakh MIDI as 170k while the prose gives 176,581.

---

### 4. Alignment and annotation methods

### Beat and downbeat

PDF p. 4, §4.1:

#### MIDI-derived beat annotation

The method uses:

1. The manually labelled tempo curve.
2. MIDI onset and velocity patterns from the accompaniment.
3. Initial beat estimation.
4. Beat propagation using the tempo curve.
5. Autocorrelation to estimate beats per measure.
6. Search over phase shifts to maximize correlation with MIDI attacks.

The method assumes time signatures are generally stable within a song, with occasional phase changes.

#### Audio-derived annotation

Audio beats/downbeats use the joint beat/downbeat tracker of Böck et al. [32].

The authors report:

- More than **90% beat-position consistency** between MIDI and audio methods under a **100 ms tolerance**.
- **80% downbeat agreement**.

Both results are supplied.

#### Table 2

Table 2 (PDF p. 4) illustrates song 003:

- `beat_midi` includes beat time and two downbeat hypotheses:
  - `downbeat_1`: simple-meter assumption
  - `downbeat_2`: compound-meter assumption
- `beat_audio` includes beat time and beat order.
- `chord_midi` and `chord_audio` contain start time, end time, and chord.
- `key_audio` contains start time, end time, and key.

For MIDI-derived annotations, the paper states that the **qualified final arrangement** is used.

### Chord annotation

PDF pp. 4–5, §4.2:

- Audio chords use a large-vocabulary chord transcription system [33].
- Audio chord boundaries are post-processed and aligned to beat positions.
- MIDI chords use a method based on [34].
- MIDI segmentation is performed at beat level.
- Templates include:
  - major, minor, diminished, augmented triads and inversions;
  - major/minor/dominant/diminished/half-diminished sevenths and inversions;
  - suspended chords;
  - major/minor sixth chords.

Crucially, the authors explicitly state that audio and arrangement chord progressions **may differ intentionally**. For example, an original `C:maj` may become `C:sus2` in the arrangement.

Reported root-note matching:

- More than **800 songs** have matching degrees above **75%**.
- Some songs are below **40%**.
- Authors attribute low matching to out-of-tune recordings, sound effects, and deliberate chord re-arrangement.

This makes the chord labels useful as parallel source/target information, but not necessarily as a single ground-truth progression.

### Key annotation

PDF p. 5, §4.3:

- Key is extracted from audio using a method related to [35].
- The authors modify whole-song key classification to allow mid-song key changes.
- A median filter post-processes frame-level labels.

There is no corresponding MIDI key annotation described.

---

### 5. Baseline experiments

### Token representation

PDF pp. 5–6, §5.1 and Table 3:

The authors use a MIDI-like event sequence containing note-on, note-off, time-shift, and velocity events.

Time shifts are quantized to **1/4 beat**, with 16 possible values from **1/4 beat to 4 beats**. Longer notes and rests use multiple time-shift tokens.

Table 3 gives:

| Event | Token range |
|---|---|
| Note-On | 0–127: MELODY/BRIDGE; 256–383: PIANO |
| Note-Off | 128–255: MELODY/BRIDGE; 384–511: PIANO |
| Time-Shift | 512–527 |
| Velocity | 528–560 |

### Experiment 1: unconditional polyphonic generation

PDF pp. 5–6, §5.1:

- Relative-position transformer encoder.
- Joint modelling of the event sequence.
- Dataset split: **90% train / 5% validation / 5% test**.
- Maximum sequence length: **2048**.
- Hidden size: **512**.
- Attention heads: **6**.
- Attention layers: **6**.
- Cross-entropy loss.
- Adam with β₁ = 0.9 and β₂ = 0.998.
- Warm-up steps: **4,000**.
- Early stopping.

Table 4 reports:

| Metric | Train | Test |
|---|---:|---:|
| Loss | 2.08978 | 2.38122 |
| Token accuracy | 0.62021 | 0.54529 |

These are token prediction metrics, not musical-quality metrics.

### Experiment 2: melody-conditioned accompaniment

PDF p. 5, §5.2:

- MELODY and BRIDGE are merged into a single **main melody** input.
- PIANO is treated as the accompaniment target.
- The same trained joint model is reused.
- During inference, the melody tokens are forced to match the supplied melody, while accompaniment is generated conditionally.

This is therefore not a separately trained conditional architecture; it is constrained generation from the joint model.

### Reported results

PDF p. 6, §5.3 and Fig. 4:

- The examples use the first **500 MIDI-event tokens** as context.
- The authors claim basic harmonic relationships and consistent rhythmic patterns.
- They explicitly acknowledge that quality is “far from” state-of-the-art systems.
- Results are qualitative piano-roll examples only.

There are no arrangement-specific metrics such as:

- melody preservation,
- chord accuracy,
- accompaniment diversity,
- source similarity,
- human preference,
- timing accuracy,
- repair success,
- audio perceptual quality.

---

### 6. Limitations and leakage risks

#### Explicit limitations

1. **No detailed genre, demographic, or cultural breakdown.**  
   Selection is based on popular songs and judged arrangement quality, creating likely popularity and style bias (PDF p. 3, §3.1).

2. **Annotation accuracy is incompletely validated.**  
   Beat agreement is cross-method consistency, not ground-truth accuracy. Chord root matching is also not true correctness, especially because the arrangement may intentionally reharmonize the source.

3. **Audio distribution is unclear.**  
   The paper claims alignment to original audio, but Figure 3 lists MIDI and text files only; it does not show audio files. The paper does not explain the copyright status or redistribution terms of the source recordings.

4. **No explicit arrangement-quality evaluation.**  
   Professional musicians and iterative review are described, but the paper gives no evaluator counts, inter-rater agreement, review rubric, or quantitative quality annotation.

5. **Task 2 is proposed but not experimentally demonstrated.**  
   The baselines use symbolic MIDI and melody conditioning, not audio-to-arrangement generation.

6. **Auxiliary annotations are not used in the baseline.**  
   Beat, chord, and key are released but not incorporated into the reported generator.

#### Data leakage risks

These are interpretations based on omissions in the paper:

- The split protocol does not state whether it is grouped by **song, artist, or arrangement lineage**.
- Multiple revisions of the same song could leak across train/validation/test if versions are independently split.
- The 462 artists may appear in multiple partitions, enabling artist/style memorization.
- Near-duplicate revisions could make test performance look better than generalization to unseen songs.
- Popular-song repetitions, covers, or artist-specific motifs are not discussed.
- A leakage-safe benchmark should split by **song first**, keep all revisions together, and ideally report artist-disjoint results separately.

---

### 7. Relevance to source-preserving arrangement, mashup, and repair

#### Strong relevance

POP909 supports source-preserving research through:

- aligned MELODY/BRIDGE/PIANO roles;
- beat and downbeat grids;
- tempo curves and expressive timing;
- parallel audio- and MIDI-derived chord labels;
- key-change annotations;
- multiple human revisions;
- explicit alignment between source material and arrangement target.

The source/target distinction is especially valuable because the paper acknowledges that arrangement can preserve melody while changing harmony.

#### Important mismatch

POP909 does **not** directly provide:

- full multitrack source stems;
- explicit source-preservation constraints;
- edit masks;
- corruption/repair pairs;
- reviewer comments;
- mashup pairs between different songs;
- section/phrase labels;
- provenance labels for copied versus newly created material;
- a demonstrated audio-to-piano baseline.

Thus, it is better viewed as a foundation for **structured accompaniment and arrangement repair**, not as a ready-made mashup or source-separation benchmark.

#### Research ideas

1. **Version-aware arrangement repair**  
   Treat `v1 → v2 → ... → final` as an edit trajectory. Extract note-level and phrase-level edits, then train a model to predict reviewer-accepted corrections. Keep all versions of one song in one split.

2. **Constrained source-preserving generation**  
   Condition on melody, bridge, beat, key, and chord labels while enforcing hard or soft constraints on melody identity, timing, and harmonic deviation.

3. **Dual-source chord modelling**  
   Represent `chord_audio` and `chord_midi` separately. Learn when reharmonization is intentional instead of treating disagreement as annotation error.

4. **Mashup alignment benchmark**  
   Pair songs by compatible key, tempo, beat structure, and chord regions. Use POP909 annotations to create controlled cross-song accompaniment tasks, while measuring melody preservation and structural compatibility.

5. **Leakage-safe evaluation protocol**  
   Report song-disjoint, artist-disjoint, and revision-disjoint results. Include nearest-neighbour similarity and memorization tests.

6. **Explainable arrangement controls**  
   Expose interpretable controls for accompaniment density, arpeggiation, chord substitution, bridge activity, register, and expressive velocity. Evaluate whether generated changes are attributable to those controls.

7. **Annotation uncertainty modelling**  
   Preserve both beat/downbeat alternatives and confidence estimates rather than collapsing them into a single deterministic grid.

8. **Audio-conditioned extension**  
   If legally distributable audio is available, build an audio-to-arrangement model using the alignment and evaluate whether it preserves source melody, tempo, key, and phrase structure. Otherwise, use legally cleared substitute audio or symbolic proxies.

### Bottom line

POP909 is a highly useful **aligned, role-separated, revision-rich piano-arrangement corpus**. Its strongest research value for explicit source-preserving systems lies in the human arrangement targets, expressive timing, and parallel structural annotations. Its principal weaknesses are unclear audio licensing/distribution, limited validation of annotation correctness, absent arrangement-quality metrics, and unspecified split handling for multiple revisions and artists.

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
