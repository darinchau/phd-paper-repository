---
title: "Dialogue-Aware Video-to-Music Generation Using Public Domain Film Collections"
authors: "Haven Kim, Zachary Novack, Julian McAuley, and Hao-Wen Dong"
year: 2026
doi: 10.48550/arXiv.2608.11576
category: data-and-representation
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/kim-2026-dialogue-aware-video-to-music.pdf"
pdf_filename: kim-2026-dialogue-aware-video-to-music.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
---
## One-line Summary

The paper releases OSSL-v2 (1,886 films and 34,343 clips) and adds a frame-wise acoustic-dialogue FiLM adapter to video-to-music models. Gains are metric- and backbone-dependent, so the method is a low-level dialogue-conditioning precedent rather than demonstrated narrative understanding.

## 1. Document Information

- **Canonical source:** arXiv `2608.11576v1`; official PDF preserved as `kim-2026-dialogue-aware-video-to-music.pdf`.
- **Full-paper evidence:** delegate digest `del_mv40xsw4_sn45.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### Evidence-grounded digest

### Bibliography and scope

- **Haven Kim, Zachary Novack, Julian McAuley, and Hao-Wen Dong**, “**Dialogue-Aware Video-to-Music Generation Using Public Domain Film Collections**,” arXiv:**2608.11576v1**, cs.SD, **12 August 2026**. Affiliations: UC San Diego and University of Michigan.
- Seven-page paper; no appendix or supplementary experiments.
- Main contributions claimed by the authors:
  1. **OSSL-v2**, a durable, self-hosted film/video–music dataset.
  2. A lightweight, frame-aligned dialogue adapter for existing video-to-music models.
  3. Benchmarking of VidMuse, GVMGen, and Diff-V2M on common data.

Key cited systems:
- VidMuse [9], Tian et al., 2025.
- GVMGen [12], Zuo et al., arXiv:2501.09972, 2025.
- Diff-V2M [16], Ji et al., AAAI 2026.
- Prior OSSL [21], Kim et al., arXiv:2506.12573, 2025.

### Page and section anchors

| Location | Evidence |
|---|---|
| p.1, Abstract/§1 | Motivation, dataset scale, dialogue hypothesis, main claims |
| p.2, Fig. 1/Table 1/§2–§3 | Dialogue–music correlation, dataset comparison, OSSL-v2 construction |
| p.3, Fig. 2/§3–§5 | Filtering pipeline and dialogue adapter architecture |
| p.4, §5–§6 | Training protocol, splits, metrics, evaluation design |
| p.5, Table 2/§6–§9 | Complete results, conclusion, acknowledgements |
| pp.5–7, §9 | Bibliography |

### OSSL-v2 construction

#### Dataset facts

**Authors report** (p.1–3):

- **1,886 public-domain films**, downloaded from YouTube.
- **34,343 clips**, totaling **246.4 hours**.
- Mean clip duration: **28.6 seconds**.
- Dataset is hosted rather than distributed as URLs:
  - Hugging Face: `McAuley-Lab/OSSL-v2`
- Compared with prior OSSL: approximately **736 clips / 36.5 hours**, versus 34,343 clips / 246.4 hours here.

#### Processing pipeline

1. **Source separation**
   - An open-source cinematic source-separation model [37].
   - The authors use its high-quality option, reported as approximately **three times slower** than the default.
   - Music is extracted from the film audio.

2. **Event filtering**
   - PANNs [38] predicts probabilities over **527 event categories**.
   - Authors manually designate **157 categories as musical** and **370 as non-musical**.
   - Music probability = sum over the 157 musical labels.
   - Non-music probability = sum over the 370 non-musical labels.
   - A segment is retained when music probability exceeds non-music probability for at least **10 consecutive seconds**.
   - Additional rejection criterion: non-music probability greater than **0.05**.

The procedure is therefore not manual soundtrack annotation; it is source separation followed by heuristic audio-event filtering.

#### Rights and reproducibility

**Author claim:** OSSL-v2 is “public-domain,” “copyright-conscious,” self-hosted, and not subject to YouTube link rot (pp.1–2).

**What the paper establishes:**

- Films are described as public-domain.
- The resulting dataset is hosted independently of the original YouTube URLs.
- The dataset is intended to be downloadable without re-crawling YouTube.
- The authors explicitly motivate this by reporting that over **10% of a 300-video prior benchmark** had become unavailable within approximately two years.

**Important reproducibility/rights gaps in the paper:**

- No film-by-film public-domain evidence, jurisdiction, provenance manifest, or rights-verification procedure is described.
- No explicit dataset license or takedown policy is stated in the paper.
- YouTube is the acquisition source, but the paper does not explain whether the hosted files include original film material, derived clips only, or rights metadata.
- Self-hosting improves persistence, but does not by itself prove legal redistribution rights.
- The paper does not specify whether the 9:1 split is film-disjoint. If clips from the same film can cross train/test, visual and stylistic leakage is possible.
- The OSSL-v2 dataset link is provided, but exact split manifests, random seeds, and complete preprocessing configuration are not documented in the paper.

### Dialogue conditioning

#### Common adapter

**Authors’ formulation** (p.3):

- Video conditioning is a sequence  
  \(V=[v_1,\ldots,v_N]\), with \(v_i\in\mathbb{R}^d\).
- Dialogue is isolated using the same source-separation model.
- A small 1-D convolution produces a per-frame low-level dialogue representation \(u_i\in\mathbb{R}^c\), described as encoding properties such as loudness and energy.
- A two-layer MLP \(\phi\) produces FiLM parameters:
  \[
  (\gamma_i,\beta_i)=\phi(u_i)
  \]
- The video condition is modulated as:
  \[
  \tilde v_i=(1+\gamma_i)\odot v_i+\beta_i.
  \]
- The final layer of \(\phi\) is zero-initialized, so the adapter begins as an identity mapping.

This is **acoustic dialogue conditioning**, not transcript, semantic speech, speaker-identity, or explicit emotion conditioning.

#### Backbone-specific implementation

- **VidMuse:** MusicGen-based autoregressive model. It already retains frame order through CLIP frame embeddings and learned positional embeddings; FiLM is applied directly.
- **GVMGen:** MusicGen-based autoregressive Transformer. Its Q-Former outputs are mean-pooled per frame but originally lack positional embeddings. The authors:
  - add learned per-frame positional embeddings before FiLM;
  - add fixed sinusoidal positional embeddings to cross-attention keys and values.
- **Diff-V2M:** Stable Audio Open latent-diffusion model with visual semantic features on a temporal grid. FiLM is applied to the per-frame features.

Figure 2 (p.3) depicts the GVMGen modification; grayscale components are original GVMGen, colored components are additions.

#### Training protocol

- Models: VidMuse, GVMGen, Diff-V2M, each with and without `+Dialogue`.
- Sonique is excluded because it uses unpaired data and is considered incompatible with the paired-data protocol.
- Authors state they use repository-recommended hyperparameters, supplementing missing details from papers.
- Original models use 30-second segments, but experiments train on **10-second crops**, because OSSL-v2’s shortest clips are 10 seconds.
- Inference generates music for the **full input-video duration**.
- The paper does not give complete optimizer, seed, hardware, training-step, or exact configuration tables.

### Dataset splits and evaluation

- OSSL-v2 is split **9:1** into training and test sets.
- Table 2 reports **3,332 OSSL-v2 test clips**.
- External evaluation set: **OES-Com**, **100 30-second clips** from commercial films.
- Low-residual-music subsets:
  - OSSL-v2: **878 / 3,332**
  - OES-Com: **20 / 100**
- LRM criterion: separated dialogue stem has summed probability below **0.05** over the 157 musical PANNs labels, corresponding to average probability below approximately **0.0003**.

Metrics:

- **CLAP similarity (`Sim`, higher is better):** paired semantic fidelity.
- **PaSST event-distribution KL (`KL`, lower is better):** paired audio-event similarity.
- **Precision (`P`, higher is better):** distributional fidelity.
- **FAD (`FAD`, lower is better):** distributional fidelity.
- **Recall (`R`, higher is better):** diversity.

FAD, Precision, and Recall use a reference distribution from **5,000 privately crawled commercial film soundtracks**. The authors release precomputed reference embedding mean/covariance at:

`https://github.com/havenpersona/ossl-v2`

This partially supports reproducibility, but the underlying 5,000-track reference corpus is not public.

### Dialogue–music correlation

Figure 1 (p.2) reports:

- Per-frame dialogue loudness versus music loudness, both in LUFS.
- Pearson correlation: **\(r=-0.11\)**.

**Author interpretation:** dialogue and music loudness are weakly negatively related, consistent with speech-aware musical ducking and local temporal coupling.

**Caution:** the paper does not report sample count, confidence interval, significance test, aggregation procedure beyond the binned plot, or whether the correlation is computed per clip or after pooling all frames. The correlation is weak and does not by itself establish that dialogue improves music generation.

### Exact objective results

Columns are `Sim↑ / KL↓ / P↑ / FAD↓ / R↑`.

#### OES-Com, all 100 clips

| Model | Sim | KL | P | FAD | R |
|---|---:|---:|---:|---:|---:|
| VidMuse | 0.19 | 1.47 | 0.17 | 93.64 | 0.00 |
| VidMuse + Dialogue | **0.23** | **0.85** | 0.04 | 97.70 | 0.03 |
| GVMGen | 0.23 | 0.97 | 0.53 | 73.40 | 0.17 |
| GVMGen + Dialogue | 0.22 | **0.87** | **0.57** | 77.29 | 0.01 |
| Diff-V2M | 0.23 | **0.62** | 0.00 | 129.30 | 0.00 |
| Diff-V2M + Dialogue | **0.25** | 0.63 | 0.00 | 130.72 | 0.00 |

#### OES-Com, LRM, 20 clips

| Model | Sim | KL | P | FAD | R |
|---|---:|---:|---:|---:|---:|
| VidMuse | 0.19 | 1.58 | 0.10 | 109.04 | 0.09 |
| VidMuse + Dialogue | **0.22** | **0.89** | 0.10 | 113.24 | 0.00 |
| GVMGen | 0.23 | 0.94 | **0.55** | 89.81 | 0.03 |
| GVMGen + Dialogue | **0.24** | **0.77** | 0.50 | 90.17 | 0.04 |
| Diff-V2M | 0.21 | 0.64 | 0.00 | 137.38 | 0.00 |
| Diff-V2M + Dialogue | **0.23** | 0.68 | 0.00 | 137.45 | 0.00 |

#### OSSL-v2, all 3,332 clips

| Model | Sim | KL | P | FAD | R |
|---|---:|---:|---:|---:|---:|
| VidMuse | 0.35 | 0.94 | 0.38 | 65.57 | 0.00 |
| VidMuse + Dialogue | **0.36** | **0.82** | 0.32 | 66.12 | 0.00 |
| GVMGen | **0.43** | **0.72** | **0.56** | **49.05** | **0.22** |
| GVMGen + Dialogue | 0.39 | 0.73 | 0.42 | 56.16 | 0.11 |
| Diff-V2M | 0.26 | 0.75 | 0.00 | 119.68 | 0.00 |
| Diff-V2M + Dialogue | **0.27** | **0.68** | 0.00 | **118.87** | 0.00 |

#### OSSL-v2, LRM, 878 clips

| Model | Sim | KL | P | FAD | R |
|---|---:|---:|---:|---:|---:|
| VidMuse | 0.34 | 0.89 | 0.43 | 64.04 | 0.00 |
| VidMuse + Dialogue | **0.35** | **0.80** | **0.45** | 66.89 | 0.00 |
| GVMGen | **0.43** | 0.72 | **0.56** | **48.98** | **0.25** |
| GVMGen + Dialogue | 0.39 | 0.73 | 0.44 | 55.98 | 0.13 |
| Diff-V2M | 0.27 | 0.73 | 0.00 | 120.22 | 0.00 |
| Diff-V2M + Dialogue | **0.28** | **0.64** | 0.00 | **119.41** | 0.00 |

#### Authors’ conclusions from Table 2

- **GVMGen** is called the strongest overall baseline under this protocol because it has the best distributional results on OSSL-v2.
- **VidMuse + Dialogue** shows the clearest paired-fidelity improvement:
  - OES-Com KL: 1.47 → 0.85
  - OSSL-v2 KL: 0.94 → 0.82
  - OES-Com CLAP: 0.19 → 0.23
  - OSSL-v2 CLAP: 0.35 → 0.36
- Dialogue improves Diff-V2M’s CLAP on both sets and KL on OSSL-v2, but Diff-V2M has **Precision = 0.00** everywhere.
- GVMGen improves on OES-Com but regresses on OSSL-v2:
  - OES-Com KL: 0.97 → 0.87
  - OSSL-v2 CLAP: 0.43 → 0.39
- Similar patterns on LRM subsets are used to argue that gains are not primarily caused by residual music leaking into the dialogue stem.
- The authors interpret stronger OES-Com gains as evidence that dialogue acts as a cross-domain regularizer.

**Interpretation:** these are metric-specific gains, not uniformly better generations. Dialogue frequently improves paired KL/CLAP while worsening FAD, Precision, or Recall. There is no human evaluation or direct temporal-alignment metric.

### Limitations

The paper has no dedicated limitations section. Evidence-based limitations include:

1. **Acoustic rather than linguistic dialogue:** the adapter receives low-level dialogue energy/loudness, so it cannot explicitly reason about words, characters, intent, narrative events, or semantic emotion.
2. **Weak causal evidence:** dialogue and music are correlated at \(r=-0.11\), but the adapter may learn ducking or production conventions rather than narrative understanding.
3. **Source-separation artifacts:** the need for LRM analysis demonstrates possible residual leakage; the separation quality itself is not quantitatively reported.
4. **Heuristic labels:** the 157 musical PANNs categories are manually selected, and the 0.05 threshold is empirically chosen without an ablation.
5. **Potential split leakage:** the paper does not state that train/test splits are film-disjoint.
6. **Evaluation limitations:** no listening study, emotion-consistency annotation, narrative appropriateness score, or explicit temporal synchronization measure.
7. **Private reference data:** the 5,000-track commercial reference set is unavailable; only precomputed statistics are released.
8. **Small external LRM sample:** OES-Com LRM contains only 20 clips.
9. **Length mismatch:** training uses random 10-second crops while inference uses full video duration.
10. **Metric conflict:** Diff-V2M has low KL but zero Precision and very high FAD, illustrating that no single metric adequately captures useful soundtrack quality.

### Relevance to emotion, narrative conditioning, and explainable control

**Author-supported relevance:**

- The paper explicitly motivates dialogue through character interaction, narrative emphasis, and emotional intensity (p.3).
- It frames film music as conveying emotion and shaping scene interpretation (p.1).
- Dialogue is temporally localized, making it a plausible conditioning signal for scene-level musical timing.

**Interpretation:**

- The method is better characterized as **time-aligned prosodic/acoustic conditioning** than emotion- or narrative-conditioned generation.
- It offers a useful low-level control interface: dialogue activity can modulate frame-wise visual conditioning through interpretable FiLM parameters \((\gamma_i,\beta_i)\).
- However, the paper does not expose those parameters as user controls, visualize their effect, or demonstrate causal attribution from dialogue events to musical changes.

### Concrete research directions

1. **Separate dialogue factors**
   - Add ASR text, speaker turns, prosody, speech rate, intensity, and speech emotion as separate streams.
   - Compare acoustic-only, transcript-only, semantic-only, and fused conditioning.

2. **Narrative-to-score planning**
   - Predict interpretable scene controls such as valence, arousal, tension, pacing, instrumentation, mode, tempo, density, and dynamics.
   - Generate a symbolic score or structured music plan before rendering audio.

3. **Explainable FiLM control**
   - Expose dialogue-strength and dialogue-emotion gates as user-adjustable controls.
   - Log temporal FiLM activations and cross-attention weights.
   - Perform interventions: mute dialogue, shift dialogue timing, swap dialogue between scenes, or alter prosody while holding video fixed.

4. **Causal evaluation**
   - Use counterfactual dialogue edits and measure changes in musical onset density, loudness ducking, tempo, harmonic tension, and instrumentation.
   - Add human judgments for emotional congruence, narrative fit, temporal alignment, and musical quality.

5. **Stronger dataset protocol**
   - Release film-level split manifests, source hashes, preprocessing code, separator versions, threshold decisions, and rights evidence.
   - Ensure all clips from a film remain in one split.
   - Version source and derived artifacts separately.

6. **Symbolic-music extension**
   - Convert the dialogue adapter into a controllable symbolic composition model whose outputs are inspectable as note density, register, harmony, rhythm, and orchestration decisions.
   - Use the generated audio model only as a renderer, preserving an explanation trail from film/dialogue → narrative attributes → symbolic musical decisions.

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
