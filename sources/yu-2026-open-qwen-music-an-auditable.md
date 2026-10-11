---
title: "Open-Qwen-Music: An Auditable Framework for LLM-Based Music Composition and Diffusion Rendering"
authors: "Yangbin Yu and Mingyu Yang"
year: 2026
doi: 10.48550/arXiv.2609.31652
category: explainability-and-auditability
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/yu-2026-open-qwen-music-an-auditable.pdf"
pdf_filename: yu-2026-open-qwen-music-an-auditable.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
---
## One-line Summary

1. **How can a modular semantic-composition/acoustic-rendering system be trained under explicit, independently reproducible interfaces?** 2. **How can component-level diagnostics and artifact provenance make a modular text-to-music system reproducible and inspectable?**

## 1. Document Information

- **Canonical source:** arXiv `2609.31652v1`; official PDF preserved as `yu-2026-open-qwen-music-an-auditable.pdf`.
- **Full-paper evidence:** delegate digest `del_mv3zdkce_us2w.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### Evidence-grounded digest

### 1. Bibliographic identity

**Yu, Yangbin, and Mingyu Yang.** “**Open-Qwen-Music: An Auditable Framework for LLM-Based Music Composition and Diffusion Rendering**.” *arXiv preprint* **arXiv:2609.31652v1 [cs.SD]**, 14 September 2026, **version 1**, 18 pages. The paper states that the work was done at Tencent.

- Paper URL: <https://arxiv.org/abs/2609.31652>
- Code/artifacts: <https://github.com/biang15343100-source/Open-Qwen-Music>
- Dataset release: <https://huggingface.co/datasets/david-miller-45678/open-qwen-music-dataset-c-minimax-music3>

This is an arXiv preprint, not a peer-reviewed conference publication in the paper’s bibliography.

---

### 2. Research question and intended contribution

The paper asks two explicit questions (§1, p. 2):

1. **How can a modular semantic-composition/acoustic-rendering system be trained under explicit, independently reproducible interfaces?**
2. **How can component-level diagnostics and artifact provenance make a modular text-to-music system reproducible and inspectable?**

The authors present Open-Qwen-Music as an **open reconstruction of Qwen-Music**, not as a quality-equivalent replacement. Their principal claim is that it makes the entire LLM-composition-plus-diffusion-rendering workflow inspectable:

> “We present the system as a transparent, executable research baseline … not as evidence of quality parity with Qwen-Music.” (Abstract, p. 1)

The paper’s “first fully open” claim is explicitly qualified as “to our knowledge” (§5, p. 10); it is not established by a systematic comparison of all prior open systems.

---

### 3. Architecture

The system has four major learned stages with explicit interfaces (Table 2, p. 4):

| Representation | Rate/interface | Function |
|---|---:|---|
| Semantic Tokens | 25 Hz, one 32,768-entry codebook | Music LLM and renderer conditioning |
| Melody Tokens | 6.25 Hz; 255 = unvoiced | Optional Melody-CoT planning |
| Spectral latent | 25 Hz, 128 dimensions | Acoustic renderer output |
| Waveform | 48 kHz stereo | Playback/evaluation |

#### 3.1 Semantic tokenizer

The tokenizer maps **24-kHz mono audio** to a **25-Hz single-codebook stream** (§3.1, pp. 4–5).

Important specifications:

- Nominal bitrate: **375 bit/s**
- 128-bin log-Mel frontend
- `nfft = 2048`, hop = `240`, `fmax = 12 kHz`
- Causal ConvNeXt frontend with kernel 7 and expansion 4
- 24-layer Conformer
- Hidden width 1,024; 16 attention heads; 4,096-dimensional feed-forward layer; RoPE
- A **16-dimensional cosine vector quantizer** after layer 13
- Codebook size: **32,768**
- Auxiliary heads for:
  - 4,096-unit multilingual CTC subwords
  - log-Mel prediction
  - soft Chroma prediction

Training consists of masked BestRQ pretraining, domain adaptation, causal adaptation, semantic supervision, and discrete quantization. Appendix Table 12 (p. 17) reports six optimization phases:

- 100,000 masked-pretraining updates
- 20,000 domain-adaptation updates
- 20,000 causal-adaptation updates
- 2,000 supervised-head-warmup updates
- 40,000 joint semantic-supervision updates
- 25,000 codebook-training updates

The codebook is initialized using **1,048,576 projected frames**, PCA whitening, and five iterations of minibatch spherical k-means. The commitment weight is **0.25**, EMA decay **0.99**, and the transition includes 5,000-step gate warmup and a 5,000-step frozen-lower-encoder interval (pp. 5, 17).

#### 3.2 Music LLM

The planner is nominally a **3B-parameter autoregressive Music LLM**, but it does **not** reproduce the unavailable Qwen-Music initialization exactly.

- Qwen-Music reportedly uses Qwen3.5-Omni 3B.
- Open-Qwen-Music uses the public **Qwen2.5-Omni thinker** (§3.2, p. 5).
- A deterministic serializer replaces the unavailable Prompt Rewriter.
- Training uses only English, section-based windows of at most **30 seconds / 750 Semantic frames**.
- No supervised fine-tuning, offline DPO, or online GSPO is performed.

The paper implements three sequence layouts:

\[
s_{\text{plain}}=[x,z],\quad
s_{\text{section}}=[x,m_{\text{section}},z],\quad
s_{\text{unique}}=[x,m_{\text{unique}},z]
\]

where `x` is the textual condition, `m` is Melody-CoT, and `z` is the Semantic Token sequence. Final training and inference use **direct text-to-semantic mode**; Melody-CoT remains an available alternative interface.

Training details:

- **291,569 English section-window records**
- 64 H20 GPUs
- BF16, DDP
- AdamW, constant learning rate `1 × 10⁻⁴`
- Gradient clipping at 2
- Two-step gradient accumulation
- 4,096-token per-GPU budget
- Two stages of 5,000 updates each, 10,000 cumulative updates (Appendix Table 13, p. 17)
- Sampling-stratum weights: **0.31479, 0.12719, 0.55802**

Decoding uses temperature **0.7**, top-p **0.98**, Semantic Token repetition penalty **0.1** over a 64-token window (p. 6; Appendix Table 15, p. 18).

#### 3.3 Acoustic renderer

The renderer follows the published Qwen-Music decomposition:

1. Conditional flow/diffusion transformer predicts 128-dimensional acoustic latents.
2. A spectral VAE decodes them into a coarse 48-kHz stereo complex spectrogram.
3. A Band-Mode Refiner corrects residual spectral errors before inverse STFT.

The paper distinguishes published Qwen-Music design from reconstruction choices. The reported reconstruction uses:

- Conditional DiT:
  - 24 blocks
  - width 1,536
  - 24 attention heads of dimension 64
  - feed-forward multiplier 4
  - QK RMS normalization
  - differential attention
  - 64 learned memory tokens
- 25-Hz, 128-dimensional latent output
- Conditional rectified flow with Gaussian source, uniformly sampled timesteps, velocity prediction
- AdamW learning rate `5 × 10⁻⁵`
- EMA decay **0.999**
- Semantic-token corruption adaptation:
  - 25% of examples corrupted
  - codebook-neighbor sampling with `K = 384`
  - clean-token phase for first 25,000 updates, followed by a 1,000-update corruption ramp (Appendix §B.3, p. 18)

The Spec-VAE uses:

- 48-kHz stereo
- STFT `nfft = 960`
- Hann window, hop 480
- No centering
- 240-sample left pad
- DC retained, Nyquist removed
- `[2, 480, T]` complex-spectrogram representation

The Refiner is a 12-layer ConvNeXt-1D network, width 256, kernel 7, with hard frequency boundaries at **1.5 kHz and 4 kHz**:

- Low band: phase only
- Mid band: magnitude and phase
- High band: magnitude only

Inference uses an **8-step Euler solver**, CFG **1.0**, and loudness target **−15.4335 LUFS** (p. 7; Appendix Table 15, p. 18).

---

### 4. Data and annotation

#### Corpus scale

Table 1 (p. 2) reports:

| Corpus | Records | Hours |
|---|---:|---:|
| Dataset-Inventory | 1,481,301 | 63,170.407 |
| Dataset-Annotated | 240,325 | 9,506.162 |
| Dataset-Annotation-Filtered | 44,355 | 2,155.176 |
| MiniMax generated set | 25,606 | 1,103.057 |
| Research package | 62,417 | 2,958.571 |

Dataset-Inventory combines **26 heterogeneous sources**. Dataset-Annotated caps each source at 20,000 records. Dataset-Annotation-Filtered applies quality and balancing constraints, including a **4:1 vocal-to-instrumental ratio**. The LLM corpus contains 291,569 English windows.

The MiniMax set contains synthetic audio generated with MiniMax Music 3 using deterministic seeds, five target durations, and up to five retries. The paper reports quality checks for duration, loudness, clipping, silence, DC offset, bandwidth, and spectral flatness (§2.1, p. 3).

#### Annotation pipeline

The 12-stage pipeline includes:

1. Indexing
2. Vocal/accompaniment separation with Hybrid Demucs
3. SongFormer structure analysis
4. Vocal-stem transcription
5. Mixture transcription
6. Lyric fusion
7. Forced alignment
8. Section assembly
9. Voice acoustics
10. Generative tagging
11. Tag fusion
12. Validation/export

The transcription stack uses **Qwen3-ASR-1.7B** and **Qwen3-ForcedAligner-0.6B**. Pitch analysis uses pYIN for annotation and RMVPE for Melody Tokens. Tags are generated with Qwen3-Omni-30B-A3B-Instruct (pp. 3, 16).

The authors explicitly warn that lyrics, sections, tags, and descriptions are **automatic estimates, not human ground truth**.

---

### 5. Evaluation and exact results

#### 5.1 Automatic annotation audit

Table 6 (p. 8):

| Signal | Result |
|---|---:|
| Lyric LCS recall | **0.889** |
| Lyric precision | **0.879** |
| Lyric LCS-recall CI | **[0.877, 0.902]** |
| Vocal-gender accuracy | **88.3%**; CI **[85.9, 90.3]** |
| Genre accuracy | **75.2%** |
| Mood accuracy | **76.9%** |
| Confidence-error correlation | Spearman **−0.764** |

The denominators and reference sets differ by task; the authors correctly state that these values must not be averaged into a single annotation score.

#### 5.2 Semantic quantization loss

Table 7 (p. 8) compares projected continuous features `P` with nearest-code quantized features `Q`. Values are the increase `Q − P`; lower is better.

| Evaluation panel | Examples | PER increase | Mel increase | Chroma increase |
|---|---:|---:|---:|---:|
| Common music holdout | 2,372 | **2.352 pp** | — | **0.00124** |
| Exposure panel | 256 | **2.153 pp** | **0.0306** | **0.00159** |
| Real-recording panel | 101 | **2.879 pp** | **0.0267** | **0.00143** |

Approximately **98.2%** of the 32,768-entry codebook is active on the evaluated panels. The paper compares this only contextually with Qwen-Music’s reported “more than 99%” utilization; it is not a controlled comparison.

#### 5.3 End-to-end generation

There is **no quantitative system-level generation benchmark**.

The paper reports qualitative listening observations (§4.3, p. 9):

- With Semantic Tokens extracted from reference audio:
  - Most lyrics remain intelligible.
  - Vocal timbre has electronic coloration.
  - Stereo width and depth are limited.
- With Music-LLM-generated Semantic Tokens:
  - Some words and phrases are omitted.
  - Vocals are often indistinct or missing.
  - Output is less stable than reference-token reconstruction.

The authors interpret this contrast as evidence that Music-LLM-generated Semantic Tokens contribute substantially to vocal degradation. However, they do not provide an independent held-out LLM evaluation, matched baselines, listener preference scores, MOS, FAD, CLAP, lyric-coverage benchmark, or statistical significance tests.

The **50.3% preference rate against Suno V5.5** mentioned on p. 2 belongs to the Qwen-Music paper, not to Open-Qwen-Music.

---

### 6. What is established versus not established

#### Author-supported claims

The paper provides evidence that:

- The modular pipeline can be implemented with explicit representation contracts.
- The tokenizer’s discrete bottleneck introduces measurable prediction-error increases of **2.153–2.879 percentage points PER** on its panels.
- Annotation quality is imperfect and heterogeneous.
- The renderer can preserve much lyric content when given reliable reference Semantic Tokens.
- The released system can generate complete 48-kHz stereo outputs.
- Provenance manifests and artifact hashes are supplied for the released workflow.

#### Claims not established by the paper

The study does **not** establish that:

- Open-Qwen-Music matches Qwen-Music’s quality.
- The architecture is superior to other open music-generation architectures.
- Semantic-token errors are causally responsible for all end-to-end vocal failures.
- The reconstructed tokenizer is optimal.
- Automatic annotation is sufficiently accurate for reliable semantic supervision.
- The system performs well on long-form generation, multilingual generation, instrumental composition, mashups, or repair.
- The model produces interpretable musical plans in a human-meaningful symbolic sense.
- The released dataset is a complete redistribution of the 63,170-hour inventory.
- The system is independently reproducible by a third party; the paper reports release and specification, but no independent reproduction study.

Important limitations acknowledged by the authors include:

- Training exposure is approximately **10,100 hours**, versus more than **five million hours** reported for Qwen-Music (p. 9).
- Annotation is automatically generated.
- The LLM is trained only on English windows of at most 30 seconds.
- No post-training alignment is performed.
- Quantization discards information.
- Rendering has electronic coloration and weak spatial fidelity.
- Evaluation coverage is narrow and largely qualitative.

---

### 7. Artifact and reproducibility status

The paper claims to release:

- Training datasets
- Provenance manifests
- Data-processing and annotation code
- Training and inference implementations
- Evaluation code
- Configurations
- Pretrained weights for every learned module
- SHA-256 artifact bindings across the workflow

The public research package contains:

- **36,811 access-screened** Dataset-Annotation-Filtered audio records
- All **25,606 MiniMax** records
- **631 metadata-only** Cambridge-MT records are not counted as audio

The authors exclude **6,912 records** from Jamendo-QA, MoisesDB, MuChin-v2, and Music4All because of access or redistribution restrictions. One JamendoMaxCaps record is quarantined by the privacy scanner (§2.3, p. 4).

Thus, “fully open” means a fully specified and substantially released research implementation—not unrestricted redistribution of every source item used in the broad inventory. The paper’s provenance model is a genuine strength, but exact end-to-end reproducibility still depends on external models, hardware, source permissions, and the authors’ implementation.

---

### 8. Relevance to explainable symbolic music AI

#### Strong relevance

The work is relevant to explainability at the **system-audit and representation-contract level**:

- Discrete Semantic Tokens create inspectable intermediate sequences.
- The tokenizer, planner, renderer, and refiner can be independently replaced.
- Artifact manifests connect data, checkpoints, configurations, and generated outputs.
- The `Q − P` quantization experiment explicitly measures information loss at a module boundary.
- Reference-token reconstruction versus generated-token rendering offers a useful decomposition of failure sources.
- Section-aligned lyrics and Melody Tokens provide temporal structure for downstream analysis.

#### Important mismatch

This is not a conventional symbolic-music system:

- Semantic Tokens are learned audio codes, not notes, chords, beats, or MIDI events.
- Melody Tokens encode reduced pitch information but not a full symbolic score.
- There is no explicit harmonic graph, voice-leading representation, instrument event representation, or editable symbolic provenance.
- The paper provides auditability, not human-interpretable explanations of why a particular musical event was generated.

#### Mashup relevance

Potentially useful components:

- Shared semantic token space
- Section boundaries and aligned lyrics
- Vocal/accompaniment separation
- Frame-aligned conditioning
- Provenance-aware source records

But mashup capability is **not evaluated**. There is no experiment on stem recombination, key/tempo alignment, cross-song structural matching, source attribution, or musical coherence after token transplantation.

#### Repair relevance

The reference-audio reconstruction path suggests a possible repair system:

- Extract Semantic Tokens from corrupted audio.
- Edit or replace local token spans.
- Re-render through the acoustic stack.
- Compare reconstructed content with the original.

However, the paper reports no repair benchmark, corruption protocol, inpainting task, edit-locality measure, or restoration metric.

---

### 9. Concrete research opportunities

1. **Symbolic-semantic dual bottleneck**  
   Add beat, chord, note, section, and instrument-event tokens alongside Semantic Tokens. Measure whether symbolic supervision improves controllability and explanation without harming audio fidelity.

2. **Causal information-loss study**  
   Compare continuous features, cosine-quantized features, alternative codebook sizes, product quantization, and residual quantization. Report downstream Music-LLM NLL, lyric coverage, termination rate, and rendered-audio metrics—not only tokenizer-head errors.

3. **Auditable mashup benchmark**  
   Create controlled cross-song tests for vocal/instrumental recombination, tempo/key changes, section replacement, and source attribution. Preserve token-level provenance so each rendered region can be traced to source audio and transformation operations.

4. **Token-level repair benchmark**  
   Define corruptions such as lyric deletion, pitch drift, missing sections, clipped stems, and wrong instrumentation. Evaluate semantic recovery, lyric intelligibility, musical continuity, spectral distortion, and edit locality.

5. **Counterfactual explanations**  
   Replace a token span, tag, lyric section, or Melody-CoT segment while holding all other variables fixed. Measure which changes affect lyric identity, instrumentation, rhythm, or timbre.

6. **Uncertainty-aware annotation and generation**  
   Propagate ASR, alignment, pitch, and tag confidence into training weights and generation. Compare confidence-aware supervision with hard filtering.

7. **Human-verified calibration sets**  
   Build small multilingual expert-annotated subsets for lyrics, sections, gender, genre, mood, and instrument labels. Estimate calibration rather than treating confidence thresholds as accuracy.

8. **Renderer robustness to planner errors**  
   Train and evaluate against realistic token errors measured from the Music LLM, rather than only codebook-neighbor corruption. Report degradation as a function of token error rate and error type.

9. **Explainable long-context composition**  
   Extend beyond 30-second windows and expose section-level planning traces, with metrics for recurrence, thematic development, transition quality, and constraint adherence.

### Bottom line

Open-Qwen-Music’s main contribution is **reproducible modularization and provenance**, not demonstrated generation quality. Its strongest evidence concerns annotation audits and semantic quantization loss. For explainable symbolic music research, it offers a valuable auditable audio-token baseline and a clear experimental scaffold, but substantial work remains to make the representation musically symbolic, causally interpretable, and useful for mashup or repair tasks.

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
