---
title: "Rethinking Music Tokenization: A Semantic Codec toward High-Fidelity LLM Music Generation"
authors: "Huakang Chen et al."
year: 2026
doi: 10.48550/arXiv.2609.21240
category: data-and-representation
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/al-2026-rethinking-music-tokenization-a-semantic.pdf"
pdf_filename: al-2026-rethinking-music-tokenization-a-semantic.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
---
## One-line Summary

1. waveform reconstruction fidelity; 2. semantic/content preservation; and 3. autoregressive language-model predictability.

## 1. Document Information

- **Canonical source:** arXiv `2609.21240v1`; official PDF preserved as `al-2026-rethinking-music-tokenization-a-semantic.pdf`.
- **Full-paper evidence:** delegate digest `del_mv41492r_152t.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### Evidence-grounded digest

**Paper:** Huakang Chen et al., “Rethinking Music Tokenization: A Semantic Codec toward High-Fidelity LLM Music Generation,” arXiv:2609.21240v1, 18 September 2026.  
**Pages inspected:** 7 PDF pages, including figures, tables, equations, and references. There is no dedicated limitations section or appendix.

### 1. Core contribution

The paper introduces **MuSeC**, a music codec intended to improve the trade-off between:

1. waveform reconstruction fidelity;
2. semantic/content preservation; and
3. autoregressive language-model predictability.

The authors argue that ordinary reconstruction codecs encode fine acoustic detail into high-entropy tokens, while speech-derived semantic codecs impose an inadequate notion of semantics on music. MuSeC instead factorizes a mixed music signal into:

- a **semantic stream**, derived from intermediate layers of a music SSL model; and
- an **acoustic stream**, learned with residual vector quantization to recover information missing from the semantic stream.

**Author claim:** The factorization improves reconstruction and token predictability without source separation (pp. 1–2, Sec. I–II).  
**Interpretation:** MuSeC is a learned audio-latent decomposition, not an interpretable symbolic representation. Its “semantic” tokens are still frame-level cluster IDs rather than notes, chords, voices, phrases, or source-labelled musical events.

---

### 2. Definition of music semantics

#### Layer-wise probing

The authors evaluate frozen SSL representations from:

- MERT;
- MuQ;
- LeVo BEST-RQ MuEncoder; and
- WavLM as a speech-SSL reference.

They probe MARBLE/MIR tasks:

- MTT music tagging;
- GTZAN genre;
- EMO/R2A emotion;
- GS key detection;
- GTZAN beat tracking;
- GuitarSet chord estimation; and
- lyrics transcription.

They omit performance-level and acoustic-level MARBLE tasks because their goal is music generation tokenization rather than general music understanding (p. 3, Sec. III-A).

#### Their operational definition

The paper observes mostly unimodal layer-wise performance curves:

- **Earlier-peaking attributes:** key, beat, and chord.
- **Middle/deeper-peaking attributes:** tagging, genre, emotion.
- **Deep-layer-biased attribute:** lyrics.

The authors therefore define:

- **music acoustic content:** key, beat, and chord—the “structural scaffold”;
- **music semantic content:** tagging, genre, emotion, and lyrics.

They select **LeVo BEST-RQ** because it performs best on tagging-related tasks and lyrics transcription (p. 3, Sec. III-A).

**Author claim:** Music has a hierarchy analogous to speech, but the appropriate semantic content must be grounded in music-specific MIR tasks rather than speech objectives.  
**Interpretation/caveat:** This is an operational probe-based definition, not a proof that the representation contains causally independent semantic and acoustic factors. The category “semantic” also mixes global descriptors with linguistic content, while harmony and meter are classified as acoustic.

---

### 3. MuSeC architecture

#### Semantic encoder

The semantic path is:

```text
frozen LeVo BEST-RQ SSL model
        → selected intermediate layer
        → k-means quantizer
        → semantic tokens
```

The selected configuration is:

- SSL layer: **layer 6**;
- k-means codebook: **2,048 clusters**;
- frame rate: **25 Hz**;
- output: **one semantic token per frame**.

The candidate layers were only `{3, 6, 9}` and candidate cluster sizes `{1024, 2048, 4096}`. Selection was based on reconstruction from quantized features alone (p. 3, Sec. III-B).

#### Acoustic encoder/decoder

The acoustic path consists of:

- causal convolutional front-end;
- sliding-window Transformer;
- RVQ;
- mirrored Transformer/convolutional decoder.

At 24 kHz, the causal convolution downsamples by **960**, yielding 25-Hz frame-level latents. The input is stereo. Semantic and acoustic representations are frame-synchronous and are concatenated channel-wise without resampling or alignment (p. 3, Sec. III-B).

#### RVQ

Acoustic RVQ configuration:

- codebook size: **1,024**;
- total codebooks: **32**;
- embedding dimension: **1,024**;
- inference: retain the first **16 acoustic codebooks**;
- training: sample a truncation depth \(m \sim U\{9,\ldots,32\}\), dropping later codebooks.

This stochastic codebook dropout is intended to make earlier codebooks carry more information and make degradation graceful under truncation.

Thus, the full MuSeC representation is:

```text
1 semantic token + 16 acoustic tokens per 25-Hz frame
```

#### Discriminators

The codec uses:

- a DAC-style discriminator: MPD + MRD;
- a multi-scale subband CQT discriminator: MSS-CQT.

These operate with adversarial and feature-matching losses (p. 3, Sec. III-B).

---

### 4. Training procedure

MuSeC is trained in three stages (p. 4, Sec. III-C).

#### Stage 1: semantic codebook

- 5,000 hours of music;
- 10-second clips;
- frozen SSL features;
- offline k-means;
- CPU training for 6 epochs.

#### Stage 2: codec training

- 120,000 hours;
- 24-kHz music;
- random 6-second crops;
- frozen semantic encoder/tokenizer;
- train acoustic encoder, RVQ, and decoder.

The authors’ factorization mechanism is implicit: because the semantic stream is frozen, the acoustic RVQ is pressured to encode information absent from the semantic representation. There is **no explicit disentanglement objective**.

#### Stage 3: decoder super-resolution

- 20,000 hours of 48-kHz music;
- high-quality audio filtered using AudioBox and SongEval;
- encoders and codebooks frozen;
- decoder retrained only;
- fixed 25-Hz tokens rendered at 48 kHz.

#### Loss

The generator loss is:

\[
L_G =
\lambda_{\mathrm{stft}}L_{\mathrm{MR-STFT}}
+\lambda_{\mathrm{stereo}}L_{\mathrm{SD-STFT}}
+\lambda_cL_{\mathrm{commit}}
+\lambda_{\mathrm{adv}}L_{\mathrm{adv}}
+\lambda_{\mathrm{fm}}L_{\mathrm{fm}}.
\]

The stereo sum/difference STFT loss is intended to preserve the stereo image, not merely mono content (p. 4, Sec. III-D).

All loss weights are set to 1 and reportedly were not tuned.

#### Training configuration

- AdamW, \(\beta_1=0.5,\beta_2=0.9\);
- initial learning rate \(2\times10^{-4}\);
- cosine decay with linear warmup;
- weight decay \(5\times10^{-2}\) on Transformer parameters;
- frozen semantic encoder: **330M parameters**;
- trainable acoustic encoder-decoder: **45M ConvNet + 135M Transformer**;
- 8 NVIDIA A100 80-GB GPUs;
- batch size 2/GPU, total 16;
- Stage 2: 800k steps;
- Stage 3: 1M steps.

The paper does not identify the large public training corpora in sufficient detail to reproduce their composition, licensing, or stylistic balance.

---

### 5. Evaluation design

The paper evaluates three axes (p. 5, Sec. IV-B).

#### Content preservation

- MTT tagging: AP and AUC;
- GuitarSet chords: accuracy;
- lyrics: normalized score from a lightweight CTC probe over frozen tokens.

#### LM friendliness

A 500M-parameter autoregressive LM predicts the first codebook. An MTP module predicts later codebooks. Metrics:

- first-codebook PPL;
- Top-1, Top-5, and Top-10 token accuracy.

#### Reconstruction

- PESQ;
- STOI;
- Mel-spectrogram \(L_1\).

PESQ and STOI are speech-oriented metrics. The authors compute them per stereo channel and average them, while Mel-\(L_1\) is intended to provide a broader spectral measure.

---

### 6. Main results

**Table I, p. 4.** Higher is better except PPL and Mel-\(L_1\).

| Codec | Rate | MTT AP/AUC | Chords | Lyrics | LM Top-1/5/10 | PPL | PESQ | STOI | Mel-\(L_1\) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| XCodec-YuE | 50 Hz | .347/.884 | .348 | .352 | .498/.783/.882 | 6.884 | 1.642 | .617 | 1.905 |
| MuCodec-LeVo | 25 Hz | .294/.865 | .264 | .387 | .391/.577/.662 | **1.575** | 1.167 | .375 | 1.419 |
| MuSeC, 8 acoustic | 25 Hz | .344/.892 | .298 | .425 | .628/.889/.932 | 1.613 | 1.714 | .621 | .984 |
| MuSeC, 16 acoustic | 25 Hz | **.346/.894** | **.365** | **.490** | **.651/.905/.955** | 1.694 | **2.201** | **.683** | **.883** |

#### Authors’ interpretation

The full MuSeC configuration gives the strongest overall trade-off:

- similar MTT AP to XCodec-YuE;
- better MTT AUC;
- better chord and lyric preservation;
- much higher LM Top-k accuracy;
- better reconstruction scores;
- half the frame rate of XCodec-YuE.

The authors emphasize that MuCodec-LeVo’s lower PPL is misleading: its single semantic codebook is easier to predict but reconstruction and content preservation are poor.

**Important interpretation:** MuSeC’s improved LM metrics are measured with a separate 500M LM and token probes, not with a demonstrated end-to-end generative music model or human evaluation.

---

### 7. Ablations

**Table II, p. 5.**

| Variant | MTT AP/AUC | Chords | Lyrics | Top-1/5/10 | PPL | PESQ | STOI | Mel-\(L_1\) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| LeVo BEST-RQ k-means | .345/.891 | .171 | .499 | — | — | — | — | — |
| MuSeC-S1A16 | **.346/.894** | .365 | .490 | **.651/.905/.955** | 1.694 | 2.201 | .683 | .883 |
| MuSeC-S0A16 | .292/.854 | .358 | .443 | .532/.807/.882 | 5.771 | 1.540 | .616 | 1.178 |
| MuSeC-A16 | .286/.850 | **.360** | .317 | .582/.811/.902 | 6.543 | **2.246** | **.689** | **.831** |

Definitions:

- **S1A16:** one semantic codebook plus 16 acoustic codebooks;
- **S0A16:** semantic branch retained but semantic tokens disabled;
- **A16:** semantic branch removed.

The acoustic-only model has the best reconstruction metrics but substantially worse semantic preservation and LM predictability. This supports the authors’ claim that semantic tokens help modeling while acoustic RVQ improves local musical/acoustic structure.

The most informative reported double dissociation is:

- continuous LeVo layer-6 representation: chord accuracy **.542**;
- k-means semantic tokens alone: chord accuracy **.171**;
- full MuSeC: chord accuracy **.365**;
- MTT AUC: **.891 → .894**;
- lyrics: **.499 → .490**.

The paper also reports that adding the acoustic stream restores key/beat/chord-related information while largely preserving semantic scores; adding the semantic stream restores lyrics and emotion with limited change to acoustic scores (pp. 6, Fig. 3 and Sec. V).

**Caveat:** The double dissociation is evidence of task-selective information distribution, but it does not establish causal disentanglement or source independence.

---

### 8. Limitations and gaps

The paper does not provide a formal limitations section. The following are evidence-grounded limitations and interpretations.

1. **Not symbolic.** MuSeC operates on 24/48-kHz waveform audio and produces 25-Hz frame tokens. It does not explicitly represent notes, durations, voices, bars, motifs, harmony functions, phrase boundaries, or provenance.

2. **No source identity factorization.** The authors avoid source separation, which avoids separation losses, but the resulting tokens are not assigned to vocals, accompaniment, source A, or source B. This is a major limitation for provenance-preserving mashups.

3. **Semantic labels are indirect.** The semantic stream is selected through frozen SSL probes and k-means reconstruction. No token-level semantic labels or interventions demonstrate that a particular token means a particular musical concept.

4. **Implicit rather than guaranteed disentanglement.** Freezing the semantic tokenizer forces the acoustic stream to encode residual information, but there is no explicit independence, mutual-information, causal, or adversarial disentanglement loss.

5. **Evaluation is proxy-based.** The paper evaluates probes, LM token prediction, and reconstruction metrics. It does not evaluate actual generated songs, controlled editing, listener judgments, musician judgments, phrase coherence, source identity, novelty, playability, or explanation faithfulness.

6. **Speech metrics are imperfect for music.** PESQ and STOI are acknowledged as speech-oriented proxies, even though the paper uses them for stereo music.

7. **Training data are underspecified.** The paper gives total hours and sampling rates but not a complete dataset inventory, genre distribution, duplicate control, licensing details, or train/test separation beyond the additional bilingual lyric test set.

8. **Semantic layer search is narrow.** Only layers 3, 6, and 9 and three cluster sizes are considered. The semantic backbone is selected partly for tags and lyrics, which may bias the representation toward global descriptors and vocals.

9. **No controllability demonstration.** The paper claims usefulness for future high-fidelity LLM music generation, but does not show controllable semantic-token editing or user-facing controls.

---

### Relevance to explicit intermediate/latent spaces

### Directly useful ideas

MuSeC provides a useful template for a **multi-level latent space**:

1. **Global semantic layer:** genre, emotion, lyrics, broad style.
2. **Structural musical layer:** key, beat, chords.
3. **Residual acoustic layer:** timbre, stereo image, fine detail.

For symbolic mashup and repair, however, the paper’s own classification suggests that key, beat, and chords should not be hidden inside an acoustic residual. They should become explicit, inspectable controls.

A more suitable symbolic adaptation would be:

```text
source audio/MIDI
  → phrase/bar-level semantic representation
  → explicit beat/meter/key/chord scaffold
  → note/voice/event representation
  → residual rendering representation
```

MuSeC’s frame synchronization could help align representations, but symbolic music requires bar/beat/phrase synchronization rather than only 25-Hz synchronization.

### Relevance to controllable mashup

**Author result:** semantic and acoustic streams can preserve different information types from a mixed signal.  
**Research interpretation:** This suggests a route to separating mashup controls by function, but not by source.

For a mashup system, add:

- source-specific semantic streams \(S_A,S_B\);
- explicit provenance labels on notes and phrases;
- beat/bar alignment variables;
- chord/key/voice-leading constraints;
- residual rendering tokens only after symbolic decisions are fixed.

The codec could remain a synthesis backend, while symbolic decisions occur in an explicit intermediate space.

### Relevance to symbolic repair

MuSeC’s probe behavior suggests a diagnostic hierarchy:

- chord/key/beat probes identify structural incompatibility;
- lyric/tag/emotion probes identify higher-level identity or expressive content;
- acoustic residuals identify timbral and rendering artifacts.

A repair model could therefore search over structured edits such as:

- transposition;
- onset displacement;
- chord substitution;
- voice reassignment;
- register change;
- rhythmic quantization;
- phrase-level bridge insertion.

Each edit should be evaluated through:

1. structural compatibility;
2. source-identity preservation;
3. minimal edit cost;
4. playability;
5. explanation faithfulness.

MuSeC alone cannot provide note-level explanations, but its multi-stream design could supply an audio-level diagnostic layer.

---

### Concrete research ideas

### 1. Symbolic MuSeC

Train parallel encoders for:

- MIDI/event tokens;
- chord/key/beat annotations;
- audio SSL features;
- residual acoustic features.

Test whether explicit symbolic tokens improve LM predictability and controllability over MuSeC’s unconstrained k-means semantic tokens.

### 2. Provenance-preserving dual-source codec

Encode sources A and B separately, then expose:

- \(z_A^{semantic}, z_B^{semantic}\);
- \(z_A^{structural}, z_B^{structural}\);
- shared rendering/residual tokens.

Evaluate whether source identity survives recomposition using source-retrieval and attribution probes.

### 3. Token intervention tests

For each token stream, intervene and measure targeted changes:

- change semantic token sequence while holding acoustic tokens fixed;
- change chord/key/beat tokens while holding semantic tokens fixed;
- change residual tokens while holding symbolic structure fixed.

This would test whether the streams are actually controllable rather than merely correlated with probe tasks.

### 4. Conflict-aware repair benchmark

Construct paired symbolic excerpts with controlled conflicts:

- incompatible key;
- chord–melody clash;
- meter/groove mismatch;
- voice crossing;
- cadence conflict;
- register collision.

Require the system to output:

- conflict type;
- responsible notes/voices/phrases;
- minimal repair;
- preserved source material;
- counterfactual alternatives;
- rationale graph.

### 5. Replace proxy evaluation with mashup evaluation

Retain the paper’s token metrics, but add separate evaluation for:

- compatibility;
- source identity;
- structural coherence;
- novelty;
- playability;
- explanation faithfulness.

Use musician and listener evaluation separately, rather than reducing all outcomes to one score.

### Bottom line

MuSeC is relevant as a strong **audio codec design pattern**: freeze a high-level representation, let a residual RVQ recover missing fidelity, and evaluate content and predictability separately. Its central limitation for this research programme is that its latent factors remain learned audio features, not explicit symbolic causes. The most promising direction is therefore not to use MuSeC tokens as explanations directly, but to combine its hierarchical factorization with an explicit provenance-aware symbolic layer for alignment, mashup search, conflict diagnosis, and minimal repair.

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
