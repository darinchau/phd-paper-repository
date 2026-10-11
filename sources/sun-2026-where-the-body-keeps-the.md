---
title: "Where the Body Keeps the Beat: Structured Motion Conditioning and Music Dynamics Supervision for Dance-to-Music Generation"
authors: "Changchang Sun, Lu Cheng, and Yan Yan"
year: 2026
doi: 10.48550/arXiv.2610.00726
category: generation-and-planning
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/sun-2026-where-the-body-keeps-the.pdf"
pdf_filename: sun-2026-where-the-body-keeps-the.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
---
## One-line Summary

I inspected the supplied extracted text and rendered pages, including all figures, tables, equations, and appendices.

## 1. Document Information

- **Canonical source:** arXiv `2610.00726v1`; official PDF preserved as `sun-2026-where-the-body-keeps-the.pdf`.
- **Full-paper evidence:** delegate digest `del_mv4099iy_wjxr.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### Evidence-grounded digest

### 1. Bibliography and version

- **Changchang Sun, Lu Cheng, Yan Yan**, “**Where the Body Keeps the Beat: Structured Motion Conditioning and Music Dynamics Supervision for Dance-to-Music Generation**” (**Dyna2Music**).
- **arXiv:2610.00726v1 [cs.SD], 30 September 2026**; supplied PDF contains **19 pages**.
- Affiliations: University of Illinois Chicago and Penn State University.
- Main paper: pp. 1–9; references: pp. 10–12; appendix: pp. 13–19.
- The paper is an audio-generation paper, not a symbolic-music paper.

I inspected the supplied extracted text and rendered pages, including all figures, tables, equations, and appendices.

---

### 2. Core contribution

#### Author claims

The paper proposes Dyna2Music, combining:

1. **Spatio-Spectral Motion Decomposition (SSMD)**  
   Separates dance motion by:
   - five body parts;
   - slow and fast temporal-frequency bands.

2. **Hierarchical Slow-Fast Conditioning Encoder (HSF-Encoder)**  
   Uses part-wise motion energy and frozen MotionBERT features to create 256-dimensional conditioning tokens.

3. **Latent Dynamics Consistency (LDC)**  
   Adds an auxiliary loss matching local adjacent-frame change magnitudes between:
   - a single-step estimate of the clean generated music latent;
   - the paired reference music latent.

4. **Latent flow-matching music generator**  
   A DiffRhythm-derived transformer generates continuous music latents, decoded by a frozen waveform VAE.

The authors report improved onset synchrony and FAD over 15 baselines on AIST++ and TikTok (abstract, pp. 1–3; Sections 3–4, pp. 4–9).

#### Interpretation

The technically important idea is not merely “more motion features.” It is the explicit separation of:

- **where** motion occurs;
- **at what temporal scale** it occurs;
- **how local output dynamics** should vary in latent space.

That design is potentially transferable to symbolic generation, but the paper does not demonstrate symbolic generation or repair.

---

### 3. Architecture

#### Input and latent representation

A dance sequence is represented as 3D joint positions \(J\) over \(N\) video frames. Paired audio \(y\) is encoded by a frozen waveform VAE:

\[
x_1 = E(y) \in \mathbb{R}^{T \times d_a}
\]

where \(T\) is the music-latent length (Section 3.1, Eq. 1, p. 4).

The VAE has:

- 64 latent channels;
- temporal downsampling factor 2048;
- stereo 44.1-kHz output (Section 4.2, p. 7; Appendix A.3, p. 14).

#### SSMD motion decomposition

The five body parts are (Appendix A.1, p. 13):

| Part | H36M-17 joint indices |
|---|---|
| Torso | `{0, 7, 8, 9, 10}` |
| Left arm | `{11, 12, 13}` |
| Right arm | `{14, 15, 16}` |
| Left leg | `{4, 5, 6}` |
| Right leg | `{1, 2, 3}` |

Velocities are frame differences multiplied by video frame rate. A fourth-order forward/backward Butterworth filter produces:

- slow component: low-pass cutoff **1.4 Hz**;
- fast component: high-pass cutoff **3.0 Hz**.

For body part \(p\) and band \(b\):

\[
K^{b}_{i,p}
=
\frac{1}{|J_p|}
\sum_{j\in J_p}
\|v^{b}_{i,j}\|_2^2
\]

(Section 3.2, Eq. 2, p. 5).

Important qualification: “slow” and “fast” mean the temporal frequency of velocity variation, **not velocity magnitude**.

Energy processing includes:

- 99.5th-percentile clipping per clip, part, and band;
- nonnegative clamping;
- Fourier resampling to latent length;
- no torso-centering for the energy branch (Appendix A.1, p. 13).

Frozen MotionBERT supplies 512-dimensional joint features. Features and energy are pooled/resampled into:

\[
S,F \in \mathbb{R}^{T\times 5},
\qquad
E \in \mathbb{R}^{T\times 5\times512}.
\]

#### HSF-Encoder

The encoder produces conditioning tokens:

\[
C\in\mathbb{R}^{T\times256}.
\]

Its stages are:

1. independently standardize slow and fast energy;
2. project energy and MotionBERT features to 256 dimensions;
3. add temporal, part, and band embeddings;
4. apply per-frame, part-wise multi-head attention;
5. aggregate parts with energy-dependent gating;
6. fuse slow and fast branches with a learned scalar gate.

For band \(b\):

\[
H_n^b = \operatorname{MHA}^b(B_n^b,E_n,E_n)
\]

where energy embeddings provide queries and MotionBERT features provide shared keys and values (Eq. 3, p. 5; Appendix A.2, pp. 13–14).

Part aggregation uses:

\[
g_{n,p}^{b}
=
\operatorname{softmax}_p
\left(
\operatorname{MLP}_{\mathrm{gate}}^b(B_{n,p}^{b})
\right),
\qquad
h_n^b=\sum_p g_{n,p}^{b}H_{n,p}^{b}.
\]

Slow-fast fusion is:

\[
u_n=\operatorname{LN}([h_n^s;h_n^f]),
\qquad
\alpha_n=\sigma(w^\top u_n),
\]

\[
m_n=\alpha_n h_n^s+(1-\alpha_n)h_n^f,
\]

\[
C_n=\operatorname{LN}(W_F[m_n;u_n])+e_{\mathrm{time}}
\]

(Eq. 5, p. 5).

Implementation details:

- four-head attention;
- energy MLP: hidden width 128, SiLU;
- part gate: \(256\rightarrow128\rightarrow1\);
- final projection: 768 dimensions to 256 (Appendix A.2, pp. 13–14).

#### Music generator

The music branch is a 16-block transformer adapted from DiffRhythm:

- hidden width: 2048;
- 32 attention heads;
- feed-forward expansion factor 4;
- noncausal self-attention;
- rotary positional embeddings;
- SiLU-gated feed-forward layers;
- cross-attention to HSF tokens;
- flow-time conditioning;
- final adaptive normalization and projection to 64 latent channels (Figure 2, p. 3; Appendix A.3, p. 14).

---

### 4. Latent Dynamics Consistency loss

Conditional flow matching uses:

\[
x_t=(1-t)x_0+tx_1,
\qquad
v^\ast=x_1-x_0
\]

(Eq. 6, p. 6).

The model predicts \(v_\theta(x_t,t,C)\). A one-step clean-latent estimate is:

\[
\hat{x}_1
=
x_t+(1-t)v_\theta(x_t,t,C)
\]

(Eq. 7, p. 6).

For a latent sequence \(z\), adjacent-frame change magnitude is:

\[
\delta_n(z)
=
\sqrt{
\frac{1}{d_a}
\sum_{k=1}^{d_a}
(z_{n,k}-z_{n-1,k})^2+\epsilon
},
\qquad \epsilon=10^{-6}.
\]

LDC is:

\[
\mathcal{L}_{\mathrm{LDC}}
=
\frac{1}{\max(1,|\mathcal I|)}
\sum_{(q,n)\in\mathcal I}
\left|
\delta_n(\hat{x}_{1,q})-\delta_n(x_{1,q})
\right|.
\]

The complete objective is:

\[
\mathcal{L}
=
\mathcal{L}_{\mathrm{FM}}
+
\lambda_{\mathrm{LDC}}\mathcal{L}_{\mathrm{LDC}}
\]

(Eqs. 8–9, p. 6).

#### What LDC does and does not supervise

The authors explicitly state that LDC:

- supervises **local latent variation magnitude**;
- adds no trainable parameters;
- adds no inference computation;
- requires neither beat annotations nor waveform decoding;
- does **not** constrain change direction;
- does **not** directly constrain beat locations (p. 6; Appendix A.4, p. 14).

This distinction is central. LDC is dynamics-shape supervision, not explicit rhythmic or semantic supervision.

---

### 5. Datasets and protocols

#### Data

| Dataset | Training | Test | Character |
|---|---:|---:|---|
| AIST++ | 8,819 | 180 | controlled studio dance |
| TikTok | 391 | 53 | in-the-wild social-media dance |

(Appendix A.3, p. 14; Section 4.1, p. 6.)

Five TikTok training pairs are excluded because they contain fewer than 100 latent frames, leaving **386 eligible training pairs**. The minimum is approximately 4.6 seconds. Sequence caps are:

- AIST++: 1,200 latent frames, approximately 55.7 seconds;
- TikTok: 700 latent frames, approximately 32.5 seconds.

#### Training

- AdamW;
- learning rate \(7.5\times10^{-5}\);
- linear warm-up then decay;
- FP16;
- gradient clipping at 1.0;
- up to 100 epochs;
- random seed 42;
- conditioning dropout 0.2;
- \(\lambda_{\mathrm{LDC}}=1\);
- EMA weights at inference (Section 4.2, p. 7).

Sampling uses 32 flow-time points and 31 Euler updates. The reported classifier-free guidance scale is zero, so inference uses the conditional velocity without guidance amplification (Appendix A.4, p. 15).

#### Onset synchrony

The protocol improves on one-second-bin evaluation used by LORIS:

- audio resampled to 44.1 kHz;
- SuperFlux-style spectral-flux onset detection;
- median aggregation;
- 256-sample hop, approximately 5.8 ms;
- one-to-one maximum-cardinality matching within \(\pm50\) ms;
- BCS interpreted as precision;
- BHS interpreted as recall;
- F1 is their harmonic mean;
- CSD/HSD are across-clip standard deviations.

The authors caution that event synchrony with a particular recording does not alone prove dance-specific rhythmic alignment (Appendix B.1, p. 15).

#### Additional analyses

- BAS with five motion-reference configurations (Sections 4.4, Appendix C, pp. 8, 16–17).
- Beat-relative onset profiles and periodicity:
  - 234 five-second windows;
  - 180 AIST++ test clips;
  - 10 tracks;
  - 20 mismatched beat grids per generated window;
  - 10,000 track-bootstrap resamples;
  - seed 20260921 (Appendix B.2, p. 15).
- Cross-dance similarity using LAION-CLAP embeddings (Section 4.6; Appendix B.3, pp. 8, 16).
- Subjective study with 10 participants and 10 trials each (Appendix E, pp. 18–19).

---

### 6. Exact main results

#### Table 1: onset-level synchrony

Values are `BCS / CSD / BHS / HSD / F1`, in percent.

| Method | AIST++ | TikTok |
|---|---|---|
| CMT | 32.77 / 23.43 / 10.51 / 8.74 / 14.80 | 20.20 / 18.43 / 12.01 / 11.54 / 13.64 |
| Diff-Foley | 31.02 / 23.10 / 12.85 / 9.51 / 16.80 | 23.21 / 20.73 / 7.86 / 9.22 / 9.72 |
| M2UGen | 32.10 / 20.81 / 43.19 / 25.70 / 33.24 | 19.38 / 11.91 / 40.64 / 25.83 / 24.71 |
| VidMuse | 33.41 / 18.41 / 49.72 / 17.41 / 38.06 | 19.33 / 10.12 / 42.64 / 15.79 / 25.37 |
| GVMGen | 28.18 / 27.77 / 12.10 / 16.35 / 12.49 | 18.54 / 21.56 / 10.60 / 11.78 / 10.82 |
| MTCV2M | 19.66 / 30.66 / 4.11 / 8.32 / 5.57 | 17.88 / 20.29 / 16.48 / 14.49 / 13.73 |
| SONIQUE | 37.36 / 34.44 / 8.55 / 12.60 / 11.16 | 22.69 / 25.51 / 19.40 / 17.95 / 16.16 |
| AudioX | 30.82 / 25.58 / 6.93 / 6.05 / 10.63 | 18.94 / 11.47 / 26.81 / 16.35 / 20.12 |
| D2M-GAN | 34.75 / 17.50 / 31.07 / 10.68 / 30.30 | 18.66 / 11.43 / 17.99 / 9.66 / 17.28 |
| CDCD | 37.27 / 24.84 / 36.88 / 22.09 / 30.79 | 22.01 / 14.82 / 25.42 / 12.37 / 18.06 |
| LORIS | 33.57 / 20.38 / 26.56 / 14.20 / 27.36 | 20.36 / 14.73 / 26.51 / 15.45 / 20.97 |
| Dance2MusicTI | 32.99 / 18.47 / 39.32 / 20.45 / 33.79 | 20.98 / 11.63 / 39.93 / 18.10 / 25.63 |
| PN-Diffusion | 34.01 / 18.75 / 32.44 / 22.01 / 29.46 | 14.42 / 25.55 / 5.82 / 10.08 / 6.99 |
| UniMuMo | 30.69 / 26.91 / 11.16 / 11.88 / 13.93 | 17.56 / 17.79 / 11.96 / 13.06 / 11.39 |
| AudioLDM-ControlNet | 36.39 / 24.74 / 15.67 / 11.81 / 20.11 | 20.30 / 12.84 / 19.05 / 10.67 / 18.23 |
| **Dyna2Music** | **60.44 / 26.57 / 63.54 / 25.70 / 55.76** | **24.06 / 11.44 / 44.19 / 15.08 / 29.99** |

(Table 1, p. 7.)

Author-reported F1 gains over the strongest baseline:

- AIST++: **55.76 vs. 38.06**, +17.70 points;
- TikTok: **29.99 vs. 25.63**, +4.36 points.

The authors also note that Dyna2Music’s CSD/HSD are not the lowest, so higher mean synchrony does not imply lower clip-to-clip variability.

#### Table 2: FAD

Values are `FAD-VGGish / FAD-PANNs / FAD-CLAP`; lower is better.

| Method | AIST++ | TikTok |
|---|---|---|
| CMT | 10.672 / 68.863 / 0.958 | 18.556 / 80.538 / 1.368 |
| Diff-Foley | 31.843 / 184.737 / 1.606 | 15.147 / 96.495 / 1.318 |
| M2UGen | 4.081 / 41.447 / 0.808 | 11.493 / 60.614 / 1.051 |
| VidMuse | 4.778 / 28.645 / 0.975 | 9.930 / 52.895 / 1.008 |
| GVMGen | 12.694 / 56.269 / 1.132 | 10.474 / 54.344 / 1.147 |
| MTCV2M | 15.695 / 62.076 / 1.130 | 9.230 / 61.119 / 0.952 |
| SONIQUE | 8.203 / 68.007 / 1.078 | 11.048 / 70.952 / 1.116 |
| AudioX | 23.151 / 96.082 / 1.748 | 8.539 / 52.205 / 0.919 |
| D2M-GAN | 11.719 / 71.355 / 1.673 | 12.885 / 99.451 / 1.863 |
| CDCD | 7.478 / 51.817 / 1.258 | 6.532 / 33.629 / 1.116 |
| LORIS | 10.733 / 30.998 / 1.047 | 15.872 / 59.243 / 1.214 |
| Dance2MusicTI | 8.968 / 49.539 / 1.171 | 10.146 / 66.981 / 1.346 |
| PN-Diffusion | 4.832 / 38.041 / 0.600 | 16.729 / 71.432 / 1.291 |
| UniMuMo | 10.307 / 56.046 / 1.157 | 11.505 / 66.003 / 1.233 |
| AudioLDM-ControlNet | 5.632 / 29.587 / 0.677 | 6.443 / 41.826 / 0.771 |
| **Dyna2Music** | **2.925 / 21.259 / 0.562** | **5.342 / 32.204 / 0.493** |

(Table 2, p. 7.)

Dyna2Music is lowest in all six FAD columns. This supports distributional audio similarity, but does not by itself establish conditional musical correctness.

---

### 7. Motion-reference and rhythm results

#### Motion reference analysis

Figure 1, p. 2, reports raw music-to-kinematic BAS:

| Motion reference | BAS | Kinematic-beat density |
|---|---:|---:|
| 1 part, 1 band | 0.307 | 2.1 beats/s |
| 2 parts, 1 band | 0.418 | 3.8 beats/s |
| 5 parts, 1 band | 0.569 | 5.4 beats/s |
| 2 parts, 2 bands | 0.472 | 7.9 beats/s |
| 5 parts, 2 bands | 0.661 | 11.6 beats/s |

The authors explicitly warn that raw BAS rises partly because finer references create denser candidate events.

For the five-part/two-band reference, Dyna2Music obtains:

- **0.684 BAS on AIST++**;
- **0.654 BAS on TikTok**;

beating the strongest generation baseline by 0.023 in both cases, but remaining below paired ground-truth music (Figure 3, p. 8).

#### Beat-relative rhythm

Dyna2Music’s matched-minus-mismatched contrasts on AIST++ are:

- on-beat onset strength: **0.379**, 95% CI `[0.256, 0.487]`;
- periodicity: **0.272**, 95% CI `[0.232, 0.315]`.

AudioLDM-ControlNet’s on-beat contrast is only 0.035; PN-Diffusion has negative contrasts on both measures (Appendix B.2, p. 15; Figure A1, p. 16).

However, shifting motion conditions by roughly a quarter or half beat leaves onset peaks near their original phase. The authors interpret this as evidence of a clip-onset phase prior and limited local motion-dependent phase tracking (Section 4.5, p. 8).

---

### 8. Ablations

#### Motion-conditioning ablation

Table A1, pp. 17–18:

Values are `BCS / CSD / BHS / HSD / F1`.

| Parts × bands | AIST++ | TikTok |
|---|---|---|
| 1×1 | 53.20 / 26.31 / 52.87 / 25.48 / 47.49 | 19.71 / 11.29 / 26.66 / 11.79 / 20.89 |
| 2×1 | 47.14 / 24.98 / 58.43 / 22.95 / 47.66 | 19.12 / 11.53 / 25.10 / 12.45 / 20.23 |
| 2×2 | 45.92 / 24.30 / 52.34 / 24.31 / 43.58 | 18.11 / 11.29 / 26.55 / 14.38 / 20.01 |
| 5×1 | 50.43 / 26.10 / 56.09 / 26.18 / 47.38 | 21.13 / 14.00 / 24.77 / 12.25 / 20.45 |
| **5×2** | **60.44 / 26.57 / 63.54 / 25.70 / 55.76** | **24.06 / 11.44 / 44.19 / 15.08 / 29.99** |

Author’s interpretation:

- merging bands at five-part resolution reduces F1 by:
  - **8.38 points** on AIST++;
  - **9.54 points** on TikTok.
- merging five parts into upper/lower body while retaining two bands reduces F1 by:
  - **12.18 points** on AIST++;
  - **9.98 points** on TikTok.

Important limitation: the variants are separately trained and have differing training budgets, so the paper says attribution to conditioning structure alone is limited (p. 18).

#### LDC-weight sensitivity

Evaluated weights:

- AIST++: `{0, 0.01, 0.05, 0.2, 1, 10}`;
- TikTok: `{0, 0.01, 0.2, 1, 10}`.

Results:

- F1 peaks at \(\lambda_{\mathrm{LDC}}=1\):
  - AIST++: **0.5576**, versus **0.502** at zero;
  - TikTok: **0.2999**, versus **0.233** at zero.
- At weight 10:
  - AIST++: 0.549;
  - TikTok: 0.285.
- Best FAD-CLAP is not at weight 1:
  - AIST++: 0.542 at zero;
  - TikTok: 0.471 at 0.01;
  - at weight 1: 0.562 and 0.493.

Thus, stronger LDC is not monotonically better, and the best synchrony/audio-distribution trade-off is metric-dependent (Appendix D, p. 18).

#### Subjective study

Ten participants each evaluated ten trials. Each trial presented the same dance with three concealed, randomized soundtrack versions. There were 100 ratings per method per dimension.

| Method | OVL | REL |
|---|---:|---:|
| AudioLDM-ControlNet | 3.3 | 3.0 |
| SONIQUE | 3.1 | 3.4 |
| **Dyna2Music** | **4.3** | **4.5** |

OVL = overall musical quality; REL = dance-music relevance. The paper reports no confidence intervals or significance tests (Appendix E, pp. 18–19).

---

### 9. Diversity

Dyna2Music’s mean pairwise CLAP similarity across different inputs is:

- AIST++: **0.58**, versus ground truth 0.62;
- TikTok: **0.47**, versus ground truth 0.66.

Lower similarity suggests more variation across dances than D2M-GAN and CMT (Section 4.6, p. 8; Figure 5, p. 9).

The authors correctly caution that this does not measure:

- repeated-sample diversity for one dance;
- novelty relative to training data;
- whether differences actually respond to the conditioning motion.

---

### 10. Limitations and artifact status

#### Explicitly supported limitations

1. **No direct beat-location supervision from LDC**  
   LDC matches magnitudes, not directions or beat positions (p. 6).

2. **Weak local phase control**  
   Quarter- and half-beat motion shifts do not substantially shift onset phase (p. 8).

3. **Mean synchrony hides variability**  
   CSD/HSD are not lowest (p. 7).

4. **Metrics are not sufficient alone**  
   Timestamp matching can reward agreement with a recording without proving dance-specific alignment (Appendix B.1, p. 15).

5. **BAS is density-sensitive**  
   Absolute BAS values across motion-reference configurations require care (Appendix C, pp. 16–17).

6. **Ablation attribution is imperfect**  
   Separate training and differing budgets limit causal attribution to the representation (p. 18).

7. **Long-range musical structure remains unresolved**  
   The conclusion identifies finer motion-dependent phase control and long-range musical structure as future work (p. 9).

#### Missing or unavailable artifact information

The paper says that supplementary material contains selected generation results from AIST++ and TikTok (p. 7). It does not provide, in the supplied PDF:

- a code repository URL;
- model checkpoints;
- dataset preprocessing scripts;
- a formal reproducibility statement;
- a license;
- a complete artifact description.

The paper’s opening appendix paragraph says that later appendices cover limitations and broader impact, but the supplied 19-page PDF ends after Appendix E/Table A2 and contains no separate limitations or broader-impact sections. This should be recorded as an incomplete or missing-paper component, not inferred as evidence that no limitations exist.

---

### 11. Relevance to controllable symbolic mashup and repair

#### Direct relevance: limited

**Author evidence:** Dyna2Music operates on continuous waveform latents and evaluates generated audio.

**Interpretation:** It does not address:

- MIDI or symbolic note generation;
- melody/harmony/voice-leading;
- source provenance;
- identity preservation;
- conflict diagnosis;
- minimal symbolic repair;
- inspectable note-level explanations.

Therefore, it is not a direct baseline for symbolic mashup or repair.

#### Transferable design ideas

##### A. Structured symbolic conditioning

The SSMD decomposition suggests separating symbolic controls by both **musical role** and **temporal scale**:

- slow branch:
  - phrase/form position;
  - harmonic rhythm;
  - cadence proximity;
  - long-range texture;
- fast branch:
  - onset density;
  - ornamentation;
  - syncopation;
  - articulation;
  - local voice-leading events.

Part-wise conditioning could become:

- melody;
- bass;
- harmony;
- inner voices;
- percussion;
- source-A and source-B provenance roles.

This is an interpretation, not a claim made by the authors.

##### B. Explicit symbolic latent-dynamics supervision

An analogous symbolic loss could compare adjacent-frame or adjacent-event changes in interpretable features:

\[
\Delta_t(z)=
[
\text{note-density change},
\text{velocity change},
\text{register change},
\text{pitch-class change},
\text{harmonic-rhythm change}
].
\]

Then supervise the generated sequence against a target or constraint-compatible sequence. Unlike Dyna2Music’s scalar magnitude, symbolic repair should likely preserve **direction and semantics**, not only magnitude.

##### C. Conflict-aware repair

For mashup repair, LDC-like supervision could identify locations where the generated recomposition changes too abruptly relative to the intended musical trajectory. Combine it with:

- protected-note/source-identity loss;
- chord/voice-leading validity constraints;
- minimum-edit regularization;
- explicit conflict labels;
- note/voice/phrase attribution;
- counterfactual alternatives.

##### D. Controllable gates

The HSF scalar gate is a useful mechanism for exposing controls such as:

- “more source-A melody”;
- “more source-B bass”;
- “preserve original rhythm”;
- “allow harmonic transformation”;
- “increase local ornamentation”;
- “prioritize phrase-level coherence.”

A symbolic system should make these gates inspectable and log their effects, rather than treating them only as hidden learned weights.

---

### 12. Concrete research ideas

1. **Symbolic Dynamics Consistency benchmark**  
   Compare flow/diffusion symbolic models with and without losses on local note-density, register, velocity, and harmonic-motion trajectories.

2. **Two-timescale mashup model**  
   Use separate slow and fast symbolic branches:
   - slow: phrase, cadence, harmonic rhythm;
   - fast: onset, ornament, articulation, voice-leading motion.

3. **Provenance-preserving latent supervision**  
   Add source-specific latent channels and supervise whether each generated event remains attributable to source A, source B, or a new recompositional operation.

4. **Motion-style intervention tests adapted to mashup control**  
   Shift or mask a control segment and test whether only the intended musical region changes. This directly addresses Dyna2Music’s phase-control weakness.

5. **Repair objective extending LDC**  
   Use:
   \[
   \mathcal L_{\text{repair}}
   =
   \mathcal L_{\text{dynamics}}
   +\mathcal L_{\text{identity}}
   +\mathcal L_{\text{validity}}
   +\lambda\mathcal L_{\text{edit-minimality}}.
   \]
   Evaluate conflict diagnosis, number of edits, identity retention, coherence, and explanation faithfulness separately.

6. **Fairer conditioning ablations**  
   Match parameter count, training steps, seeds, and data exposure across one-part/two-part/five-part variants. Dyna2Music’s own appendix identifies this as necessary.

7. **Avoid density-confounded alignment metrics**  
   Report event density, precision/recall, phase-shift robustness, and matched/mismatched controls alongside BAS. This is particularly important for symbolic mashup evaluation, where adding events can inflate proximity-based scores.

### Overall assessment

Dyna2Music provides a strong, clearly specified example of **structured conditioning plus explicit local latent-dynamics supervision**. Its best evidence is the consistent improvement in onset F1, FAD, and motion-reference BAS, supported by ablations and rhythm controls. Its main conceptual limitation is that the dynamics loss supervises only local magnitude, while phase, direction, musical structure, and provenance remain largely implicit. For the symbolic mashup/repair programme, the most valuable transfer is the architecture of **multi-axis, multi-timescale conditioning**, not the audio model itself.

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
