---
title: "Towards AI-Generated Music Plagiarism Detection as a Version Identification Problem"
authors: "Fotis Koutsikos et al."
year: 2026
doi: 10.48550/arXiv.2610.09075
category: explainability-and-auditability
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/al-2026-towards-ai-generated-music-plagiarism.pdf"
pdf_filename: al-2026-towards-ai-generated-music-plagiarism.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
---
## One-line Summary

“**Towards AI-Generated Music Plagiarism Detection as a Version Identification Problem**.” arXiv:2610.09075v1 [cs.SD], **6 October 2026**, 5 pages.

## 1. Document Information

- **Canonical source:** arXiv `2610.09075v1`; official PDF preserved as `al-2026-towards-ai-generated-music-plagiarism.pdf`.
- **Full-paper evidence:** delegate digest `del_mv3zfqmn_1nsp.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### Paper digest

### Bibliographic record

**Koutsikos, Fotis; Prokopiou, Ioannis; Kantarelis, Spyridon; Lyberatos, Vassilis; Vikatos, Pantelis; Aidinis, Athanasios; Stafylakis, Themos; Voulodimos, Athanasios; Stamou, Giorgos.**  
“**Towards AI-Generated Music Plagiarism Detection as a Version Identification Problem**.” arXiv:2610.09075v1 [cs.SD], **6 October 2026**, 5 pages.

Affiliations: National Technical University of Athens, Athens University of Economics and Business, Orfium, and Archimedes/Athena R.C.

The paper has no stated journal/conference publication in v1. It contains Figures 1–3, Table 1, and 25 references.

---

### 1. Research question and thesis

#### Authors’ formulation

The paper asks whether pretrained **music version identification (MVI)** systems, originally designed to recognize human covers and alternate recordings, can detect plagiarism when the candidate track is produced through generative re-synthesis.

The central reframing is:

> Is the candidate a musical version or derivative of the reference, rather than merely whether the candidate is AI-generated?

The formal task is pairwise classification. Given embeddings

\[
z_{\text{ori}}=f_\theta(x_{\text{ori}}), \qquad
z_{\text{cand}}=f_\theta(x_{\text{cand}})
\]

a threshold system predicts plagiarism when

\[
d(z_{\text{ori}},z_{\text{cand}})\leq\tau.
\]

The paper explicitly says this is a **technical similarity judgment**, not a legal determination of substantial similarity. See **§2.1, PDF p. 2**.

#### Main thesis

Scalar embedding distances fail especially badly after generative re-synthesis. However, plagiarism-related information is not necessarily destroyed; it becomes distributed across embedding coordinates. A classifier over coordinate-wise embedding shifts can recover some of this information.

The abstract reports an overall **F0.5 improvement from 0.612 to 0.803**. See **Abstract, PDF p. 1**.

---

### 2. COPYCAT benchmark construction

COPYCAT means **Corpus Of Plagiarized Yet Camouflaged Artificial Tracks**.

#### Source material

The benchmark starts from the SMP dataset [4], described as containing:

- 70 real-world plagiarism allegations;
- segment-level timestamps;
- broad stylistic coverage;
- 1,219 alleged-similarity anchor segments.

Each anchor is:

- 20 seconds long;
- mono;
- sampled at 22,050 Hz;
- extracted around the alleged similarity region.

The authors argue that segment-level comparison is preferable to whole-track comparison because unrelated material would dilute the evidence. See **§2.2 and §3.1, PDF pp. 2–3**.

#### Stem processing

Each anchor is separated with **Hybrid Transformer Demucs v4** into:

- vocals;
- bass;
- drums;
- other/melodic-harmonic material.

This enables controlled vocal reintegration and stem-conditioned generation.

#### Positive transformation categories

Each transformed excerpt is paired with its original anchor as a positive pair.

##### 1. Human Plagiarism

The original SMP human-plagiarism relationships.

##### 2. Human Plagiarism + DSP

Human-plagiarism pairs with deterministic signal processing applied.

##### 3. Original + DSP

DSP transformations applied to an unmodified original.

##### 4. AI Generation

Full or stem-conditioned generative re-synthesis.

##### 5. AI + DSP

Generative re-synthesis followed by DSP obfuscation.

The five categories are reported in **Table 1, PDF p. 4**.

---

### 3. Generative models and transformations

#### MusicGen

- Melody variant.
- 32 kHz generation.
- Conditions on chromagram features extracted from the anchor.
- Produces a full re-synthesis.

#### AudioLDM 2

- `audioldm_48k` variant.
- 48 kHz generation.
- Uses audio-guided diffusion with the anchor as an acoustic reference.
- Produces a full re-synthesis.

#### MGE-LDM

- Preserves one source stem.
- Inpaints the surrounding accompaniment.
- Three stem-specific variants per anchor:
  - bass;
  - drums;
  - melodic/harmonic instruments.

This design attempts to isolate which musical components carry the plagiarism signal.

Together, the three architectures produce **5,472 AI-derivative positive pairs**.

#### Prompt and vocal controls

The generation process uses randomized text prompts that are deliberately unrelated to the source style. The authors therefore intend retained similarity to originate from audio conditioning rather than textual style prompting.

Human vocals are re-integrated into derivatives, with pitch and tempo augmentation.

Vocal validity is determined using an energy-based VAD filter on the Demucs-separated vocals. Because vocals are re-integrated into every derivative, vocal presence is inherited from the anchor.

#### DSP transformations

The paper reports ten deterministic transformations combining:

- pitch shifts of **±2 and ±4 semitones**;
- tempo modifications from **0.90× to 1.10×**.

These transformations are applied over the source, human-cover, and AI-derived material. The resulting collection contains **73,590 audio variants**.

---

### 4. Negative-pair construction

Random negatives would be too easy, so COPYCAT mines negatives at three difficulty levels in the CLEWS embedding space:

1. random negatives;
2. intra-category nearest negatives, where categories are defined by source × DSP combinations;
3. global nearest negatives.

Each level contributes approximately **79,000 pairs**, producing:

- **350,654 total comparisons**;
- **113,690 positive pairs**;
- **236,964 negative pairs**.

The source audio is commercially licensed. The authors release manifests, prompts, scripts, and source code, but **not the raw audio**. See **§3.1, PDF p. 3**.

---

### 5. Representations and models

### Acoustic branch: CLEWS

The paper uses a frozen pretrained **CLEWS Discogs-VI checkpoint**:

- 1,024-dimensional embeddings;
- CQT-based representation;
- selected over the SHS100k configuration because its set-size distribution was considered more realistic;
- chosen based on reported state-of-the-art MVI performance.

CLEWS is intended to capture timbral and structural similarity.

### Semantic branch: WEALY

The paper uses frozen **WEALY** embeddings:

- 512-dimensional embeddings;
- extracted from a Whisper-Turbo backbone;
- used only when both segments pass vocal-validity gating.

WEALY is intended to capture lyrical/semantic similarity.

### Threshold baselines

For each branch, the authors search over:

- Euclidean distance;
- Manhattan distance;
- cosine distance;
- Pearson distance.

The distance and threshold are calibrated to maximize **F0.5**, which weights precision twice as heavily as recall.

The best distances are:

- **Manhattan** for CLEWS;
- **cosine** for WEALY.

### Score-level fusion

Normalized acoustic and semantic distances are fused as:

\[
d_{\mathrm{fusion}}
=
\alpha \hat d_{\mathrm{ac}}
+
(1-\alpha)\hat d_{\mathrm{sem}}
\]

when both excerpts are vocal-valid. Otherwise, only the acoustic score is used.

The learned value is:

\[
\alpha=1.0.
\]

Thus, scalar fusion effectively discards WEALY.

### Coordinate-wise shift representation

The key representation is the absolute embedding shift:

\[
\Delta z =
\left(
|z^{\mathrm{cand}}_1-z^{\mathrm{ori}}_1|,
\dots,
|z^{\mathrm{cand}}_\ell-z^{\mathrm{ori}}_\ell|
\right).
\]

Absolute rather than signed shifts are used because the authors treat plagiarism as direction-agnostic.

Three feature configurations are tested:

1. **Engineered features**
   - CLEWS and WEALY distances;
   - mean, standard deviation, percentiles, and L2 norm of \(\Delta z\);
   - statistics over stable and volatile dimensions;
   - vocal-validity flags.

2. **Full shift vector**
   - all 1,024 CLEWS shift coordinates.

3. **Hybrid representation**
   - engineered features;
   - the most volatile CLEWS dimensions.

The classifier is global **XGBoost**.

---

### 6. Splits and evaluation protocol

The paper uses:

- stratified 5-fold cross-validation for threshold models;
- stratified, grouped 5-fold cross-validation for XGBoost;
- grouping by original-track filename to reduce source leakage;
- ten random seeds for XGBoost;
- mean results with 95% confidence intervals.

For hybrid models, volatile dimensions are ranked independently inside each training fold to avoid feature-selection leakage.

The paper does **not** report an independent held-out external test set. Results are cross-validation results over COPYCAT.

This is important for provenance research: the benchmark tests interpolation across controlled transformations, but it does not establish generalization to unseen commercial generators, unseen source catalogs, or real legal disputes.

---

### 7. Exact results

### Table 1: category-level performance

Percentages are precision, recall, and F0.5.

| Category | Pairs | WEALY P/R/F0.5 | CLEWS P/R/F0.5 | XGBoost Hybrid Top-512 P/R/F0.5 |
|---|---:|---|---|---|
| Human Plagiarism | 3,757 | 74.2 / 25.9 / 54.0 | 98.0 / 30.6 / 68.0 | **97.3 ± 0.1 / 86.5 ± 0.5 / 94.9 ± 0.2** |
| Human Plagiarism + DSP | 37,570 | 72.3 / 24.8 / 52.3 | 97.7 / 27.4 / 64.5 | **97.2 ± 0.1 / 83.1 ± 0.4 / 94.0 ± 0.2** |
| Original + DSP | 12,190 | 51.8 / 80.1 / 55.7 | **96.9 / 95.2 / 96.5** | 87.2 ± 0.4 / 99.3 ± 0.0 / 89.4 ± 0.3 |
| AI Generation | 5,472 | 42.4 / 51.5 / 43.9 | 84.3 / 15.0 / 43.8 | **75.1 ± 0.4 / 56.5 ± 0.3 / 70.5 ± 0.3** |
| AI + DSP | 54,701 | 36.4 / 34.3 / 36.0 | 79.0 / 10.3 / 33.9 | **72.0 ± 0.5 / 50.0 ± 0.3 / 66.2 ± 0.4** |
| **Overall** | **113,690** | 45.6 / 36.6 / 43.5 | **92.8 / 26.0 / 61.2** | **84.2 ± 0.4 / 67.7 ± 0.3 / 80.3 ± 0.3** |

**Source:** Table 1, PDF p. 4.

#### Main numerical conclusions

- CLEWS has strong precision but poor recall on AI derivatives.
- CLEWS overall F0.5 is **0.612**.
- Hybrid Top-512 reaches **0.803**.
- On AI + DSP:
  - CLEWS recall: **10.3%**;
  - Hybrid recall: **50.0%**.
- On human plagiarism:
  - CLEWS recall: **30.6%**;
  - Hybrid recall: **86.5%**.
- The threshold baseline is better for Original + DSP:
  - CLEWS F0.5: **96.5%**;
  - Hybrid F0.5: **89.4%**.

The authors interpret this as evidence that conservative scalar thresholds work well for simple acoustic perturbations but not for generative re-synthesis.

---

### Ablations

Reported in **§3.2, PDF p. 3**:

| Configuration | Overall F0.5 |
|---|---:|
| CLEWS scalar threshold | **0.612** |
| 24 engineered features | **0.617** |
| Vocal-validity flags alone | **0.836** |
| Flags + engineered features | **0.853** |
| Full 1,024-dimensional CLEWS \(\Delta z\) | **0.811** |
| Top-256 volatile dimensions | **0.749** |
| Top-512 volatile dimensions | **0.792** |
| Top-1,024 dimensions | **0.811** |
| Hybrid Top-512 | **0.803** |

The vocal flags are excluded from the final model because they act as a transformation-category shortcut: vocal-validity profiles correlate with the construction category rather than necessarily with musical similarity.

The final hybrid model uses 24 engineered features plus the 512 most volatile CLEWS coordinates.

Training-cost figures:

- Top-512: **54 seconds per fold**;
- Top-1,024: **119 seconds per fold**.

---

### Feature importance

The authors report that:

- WEALY distance features are the highest-ranked family among engineered features;
- they rank above CLEWS distance summaries;
- no individual raw dimension is as important as these summaries;
- collectively, the semantic features contribute to the improvement.

This suggests that WEALY is not useless, but scalar score fusion cannot exploit its information.

---

### 8. Figures and visual interpretation

### Figure 1: framework overview

**PDF p. 1**

The diagram shows:

1. segment extraction;
2. reference/candidate pair construction;
3. acoustic CLEWS encoding;
4. semantic WEALY encoding;
5. vocal-aware score fusion;
6. supervised classification using distances and \(\Delta z\);
7. binary detection, robustness, and latent-space evaluation.

The architecture separates pair construction from representation extraction and downstream decision-making.

### Figure 2: origin-centered UMAP

**PDF p. 4**

Four example projections are shown:

- Pair 27, segment 40 s;
- Pair 35, segment 154 s;
- Pair 56, segment 282 s;
- Pair 16, segment 225 s.

Each anchor is centered at the origin. The figure displays source-specific displacement geometry:

- human covers are generally closest to the anchor;
- MGE-LDM variants occupy intermediate regions;
- MusicGen and AudioLDM 2 are farther away;
- DSP variants form peripheral/radial shells around their base derivatives;
- displacement directions vary by source and transformation.

#### Authors’ interpretation

Plagiarism information remains geometrically organized even when scalar distances exceed the threshold.

#### My interpretation

The figure supports using **directional or structured latent evidence**, but it does not prove that the directions correspond to interpretable musical factors such as melody, harmony, or rhythm. Those factors are not separately annotated.

### Figure 3: CLEWS distance versus pitch shift

**PDF p. 4**

The graph plots Manhattan distance against pitch shift from −4 to +4 semitones. The dashed reference threshold is:

\[
\tau = 986.4
\]

The qualitative strata are:

- pitch-shifted originals remain below the threshold;
- human covers and MGE-LDM remain near the threshold;
- MusicGen and AudioLDM 2 remain far above it;
- generative re-synthesis distances are nearly flat as pitch shift changes.

#### Authors’ interpretation

Generative re-synthesis already moves embeddings close to maximal acoustic distance, so additional DSP intensity does not provide useful magnitude information. Coordinate-wise structure, rather than distance magnitude, is the useful signal.

WEALY shows an analogous but complementary behavior, with greater sensitivity to pitch than tempo.

---

### 9. Limitations and artifact status

### Explicitly acknowledged by the authors

The conclusions state that the system should be treated as a **triage mechanism for expert review**, not a replacement for legal judgment.

Future work listed by the authors includes:

- more generative architectures;
- broader DSP perturbations;
- lyric-preserving datasets;
- newer MVI systems;
- fine-tuning the MVI encoders;
- source attribution beyond binary detection.

The authors also note that commercial systems such as Suno and Udio do not provide the audio-conditioning interfaces needed for this experimental construction.

### Dataset and experimental limitations

#### Synthetic AI derivatives

The benchmark’s AI cases are controlled re-syntheses from MusicGen, AudioLDM 2, and MGE-LDM. They are not necessarily representative of:

- Suno;
- Udio;
- proprietary systems;
- prompt-only generation;
- iterative human editing;
- real-world infringement workflows.

#### Artificial prompt design

Randomized prompts unrelated to source style isolate audio conditioning, but this also removes an important real-world pathway: a user may supply lyrics, genre, artist style, or detailed textual descriptions related to the source.

#### Vocal shortcut

The vocal-validity flags achieve F0.5 **0.836 alone**, almost matching the **0.853** result with flags plus engineered features. This is a substantial benchmark-construction shortcut. The final model excludes the flags, but other category-correlated artifacts may remain.

#### Lack of symbolic or legal labels

A positive AI pair is positive because it was generated from an anchor. This does not establish that human listeners, musicologists, or courts would judge it derivative or substantially similar.

#### Audio-only evidence

The system does not directly expose:

- copied melodic intervals;
- harmonic progressions;
- rhythmic patterns;
- lyric correspondences;
- arrangement structure;
- instrument-level provenance.

#### Source and generator generalization

Grouping by original filename reduces track leakage, but the paper does not report:

- leave-one-source-case-out results;
- leave-one-generator-out results;
- temporal generalization;
- external validation;
- performance on genuinely novel generators.

#### Negative mining bias

Negatives are mined using CLEWS space, while CLEWS is also one of the principal evaluation representations. This may make the benchmark difficult in a CLEWS-specific way while not necessarily reflecting all plausible non-derivatives.

#### Artifact availability

Released:

- manifests;
- prompts;
- scripts;
- source code.

Not released:

- raw SMP audio, because it is commercially licensed.

Repository stated in footnote 3:

`https://github.com/fotiskoutsikos/Plagiarism-Detection-System.git`

The paper does not specify a software release version, commit hash, artifact DOI, raw-audio access procedure, or exact pretrained-checkpoint packaging.

---

### 10. Relevance to explainable symbolic music AI

### Provenance

The paper is highly relevant as a **candidate retrieval and triage layer** for provenance systems:

1. retrieve likely source recordings with an MVI encoder;
2. locate similar segments;
3. map those segments into symbolic representations;
4. explain similarity in terms of melody, harmony, rhythm, lyrics, instrumentation, and form.

However, the current method’s \(\Delta z\) coordinates are not musically interpretable. They indicate that something in the embedding changed in a characteristic way, not what musical content was retained.

### Explainable mashup

For mashup construction, a provenance-aware pipeline could use COPYCAT-style detection to:

- identify source candidates before combining stems;
- distinguish ordinary DSP edits from stronger generative transformations;
- flag source-derived material for attribution;
- provide segment-level evidence rather than whole-track similarity;
- attach confidence and abstention states to source matches.

The category structure is especially relevant to mashups because MGE-LDM explicitly tests stem-level preservation.

### Symbolic repair

The paper’s segment-centered formulation could support repair:

- detect a damaged or suspicious segment;
- retrieve a likely source/version;
- align corresponding symbolic events;
- propose repairs for missing notes, chords, timing, or instrumentation;
- explain the repair through aligned source events and transformation history.

The paper itself does not perform symbolic transcription, alignment, repair, or explanation; this is an extension rather than an author claim.

---

### 11. Concrete research ideas

1. **Musicologically factorized shift modeling**  
   Replace opaque \(\Delta z\) coordinates with groups tied to melody contour, interval sequence, harmony, rhythm, lyrics, timbre, and arrangement. Test whether coordinate groups provide better explanations than raw feature importance.

2. **Audio-to-symbolic provenance alignment**  
   Use CLEWS/WEALY-style retrieval to find candidate sources, then align both tracks to notes, chords, beats, lyrics, and stems. Report evidence as matched bars and musical attributes.

3. **Transformation-aware provenance graphs**  
   Represent provenance as a graph: source recording → stem extraction → pitch/tempo edits → generative re-synthesis → mashup/repair. Store model, prompt, conditioning signal, and confidence at each edge.

4. **Counterfactual explanations**  
   Evaluate how changing only pitch, tempo, harmony, melody, or lyrics changes the detector score. This would reveal whether a match is driven by musically meaningful structure or an acoustic artifact.

5. **Leakage-resistant COPYCAT extension**  
   Remove vocal/category shortcuts; use source-disjoint and generator-disjoint splits; mine negatives with multiple unrelated embedding spaces; add human similarity judgments.

6. **Explainable mashup safety gate**  
   Before mashup assembly, retrieve possible sources and display:
   - matched segments;
   - melodic/harmonic/rhythmic evidence;
   - transformation severity;
   - confidence;
   - nearest non-match alternatives.

7. **Provenance-assisted symbolic repair**  
   When a symbolic track contains missing or corrupted events, retrieve source versions and propose repair candidates, with explanations such as “melodic contour restored from source bars 17–20.”

8. **Beyond binary detection**  
   Extend the model to:
   - top-\(k\) source attribution;
   - partial-source localization;
   - transformation classification;
   - uncertainty calibration;
   - abstention when evidence is insufficient.

9. **Interpretable stem-level evaluation**  
   Create cases where only melody, bass, drums, harmony, or lyrics are preserved. Measure which components each model detects and whether the explanation matches the known construction.

10. **Open-audio reproducibility set**  
    Build an openly distributable analogue using public-domain or Creative Commons recordings, preserving the same 20-second anchors, transformations, and hard-negative protocol.

---

### Bottom line

**Author claim:** pretrained scalar MVI distances are inadequate for AI-generated derivatives, but coordinate-wise embedding shifts substantially improve detection, reaching **80.3% overall F0.5** and **66.2% on AI + DSP**.

**My assessment:** the paper provides a useful retrieval/triage architecture and a strong argument against relying on one similarity score. For explainable symbolic music research, its most valuable contribution is the controlled transformation framework—not yet a symbolic explanation method. The next step is to connect latent-space evidence to aligned musical structures and provenance graphs, while eliminating vocal/category shortcuts and testing source- and generator-disjoint generalization.

## 3. Methodology and Architecture

The methodology and architecture are preserved in the embedded full-paper digest above, including its original page/section anchors.

## 4. Key Results and Benchmarks

Reported results and benchmark denominators are preserved in the embedded digest above; no unverified reproduction is implied by this record.

## 5. Limitations and Future Work

The evidence limitations, artifact status, and future-work claims are preserved in the embedded digest above. See the batch report for relevance to the explainable symbolic music AI programme.

## 6. Related Work

- [[overviews/2026-symbolic-music-literature-map]] — batch literature map and bidirectional synthesis anchor.

## 7. Glossary

- **Primary category:** `explainability-and-auditability`. Domain-specific terms are defined in the embedded digest and cross-paper synthesis.
