---
title: "StepAudio 3 Music Technical Report"
authors: "Chengli Feng et al."
year: 2026
doi: 10.48550/arXiv.2609.16034
category: generation-and-planning
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/al-2026-stepaudio-3-music-technical-report.pdf"
pdf_filename: al-2026-stepaudio-3-music-technical-report.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
---
## One-line Summary

1. A discrete music tokenizer, 2. A Mixture-of-Experts autoregressive model, 3. An explicit ABC notation planning pass, 4. A continuous flow-matching DiT renderer.

## 1. Document Information

- **Canonical source:** arXiv `2609.16034v1`; official PDF preserved as `al-2026-stepaudio-3-music-technical-report.pdf`.
- **Full-paper evidence:** delegate digest `del_mv41492s_n4j6.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### StepAudio 3 Music — evidence-grounded digest

**Sources inspected**

- Full PDF: `/tmp/paper-digest/2609.16034v1.pdf` — 18 pages.
- Extracted text: `/tmp/paper-digest/2609.16034v1.txt`.
- All pages, Figures 1–6, and Tables 1–6 were inspected; evaluation pages were also visually checked.
- Official showcase/API pages:
  - https://stepaudiollm.github.io/step-audio-3-music/
  - https://stepaudiollm.github.io/step-audio-3-music/api.html

### Bottom line

**Author claim:** StepAudio 3 Music is a long-form, text- and reference-conditioned music generator combining:

1. A discrete music tokenizer,
2. A Mixture-of-Experts autoregressive model,
3. An explicit ABC notation planning pass,
4. A continuous flow-matching DiT renderer.

**Assessment:** The most research-relevant contribution is not the audio quality alone, but the **ABC-CoT intermediate arrangement plan and LLM-based plan editing**. This is a promising precedent for explainable musical control. However, the system remains primarily an audio-generation system: it does not demonstrate exact note-, chord-, bar-, source-provenance-, or repair-level guarantees. It is therefore highly relevant as an architectural inspiration for symbolic mashup/repair, but not a directly usable symbolic repair system.

---

### 1. System architecture

#### 1.1 Two-stage autoregressive generation

The paper defines lyrics, text prompts, and optional references as conditioning \(c\), an ABC arrangement plan as \(a\), and music tokens as \(m_{1:T}\).

The explicit-planning mode factorizes generation as:

\[
p(a,m_{1:T}\mid c)
=
p(a\mid c)
\prod_t p(m_t\mid m_{<t},a,c)
\]

Without explicit planning, the model directly predicts:

\[
\prod_t p(m_t\mid m_{<t},c)
\]

The ABC-CoT plan contains:

- Chords,
- Tempo,
- Time signature,
- Number of bars,
- Key,
- ABC melody notation.

The paper describes this plan as readable and editable before acoustic synthesis (Sections 2.2–2.3, pp. 2–4).

#### 1.2 Tokenizer and acoustic renderer

The final representation is:

- 50 tokens/second,
- One codebook with 65,536 entries,
- One discrete token stream rather than multiple residual streams.

The tokenizer uses:

- 24-layer bidirectional Conformer,
- Hidden dimension 1,024,
- Approximately 0.6B parameters,
- Lower 12 layers → 32-dimensional quantization space,
- Upper 12 layers after quantization,
- 24-kHz audio frontend,
- 48-kHz waveform output from the final VAE decoder.

The tokenizer is trained in three stages:

1. **Self-supervised BEST-RQ-style pretraining** with contiguous waveform spans replaced by Gaussian noise.
2. **Multi-task representation learning** using CTC lyric supervision, Mel reconstruction, and Chroma reconstruction.
3. **Discrete tokenization** by inserting a 65,536-entry VQ bottleneck between Conformer layers 12 and 13.

The renderer is a separately trained flow-matching DiT. It predicts continuous StepAudio VAE latents conditioned on the discrete music tokens, which are then decoded into waveform audio (Sections 2.4–2.6 and 4.1, pp. 4–9).

#### 1.3 Chunked rendering

For DiT training, each example uses:

- Two seconds of latent context,
- A 30-second target segment.

At inference, previously generated latents replace the ground-truth context. This is intended to support long-form generation, but it introduces possible error accumulation across chunks.

---

### 2. Data and training scale

#### 2.1 Data pipeline

The paper reports a corpus of:

- More than **100 million songs**,
- More than **5 million hours of audio**,
- Approximately **one trillion tokens**.

The automated preprocessing pipeline includes:

- Frequency-band analysis,
- Audio-event detection using FireRedVAD,
- Vocal/accompaniment separation using Demucs,
- Language identification using MMS-LID,
- Chinese/English transcription using FireRed ASR,
- Other supported languages using WhisperX,
- Timestamped lyrics and confidence scores,
- Song section analysis using SongFormer.

The final records contain language, lyrics timestamps, section boundaries, spectral measurements, and ASR confidence (Section 3, pp. 7–8).

The authors also construct an ABC corpus for music-to-ABC understanding and ABC-to-music generation.

#### 2.2 LLM pretraining curriculum

The LLM is initialized from a text MoE model. Reported consumption is:

| Stage | Tokens | Context | Batch |
|---|---:|---:|---:|
| Large-scale pretraining | 600B | 16,384 | 768 |
| Multi-task mid-pretraining | 500B | 32,768 | 512 |
| High-quality annealing | 80B | 32,768 | 512 |

The stages are consumed-token counts and are not necessarily disjoint.

**Stage 1:**

- Approximately 500B lyrics-to-music tokens,
- Approximately 100B music-to-lyrics tokens,
- Constant learning rate \(2.45\times10^{-5}\).

**Stage 2:**

- 32% standard music generation,
- 16% ABC-CoT generation,
- 20% music understanding,
- 32% other reference-conditioned tasks,
- Learning rate decays from \(2.45\times10^{-5}\) to \(2.0\times10^{-5}\).

**Stage 3:**

- Approximately 80B high-quality tokens,
- Song generation, cover generation, and vocal-to-mix generation,
- Learning rate warms to \(2.0\times10^{-5}\), then decays to \(2.0\times10^{-6}\),
- Checkpoints evaluated at 20B, 40B, 60B, and 80B tokens.

#### 2.3 SFT and DPO

The SFT corpus contains approximately **20B tokens**, including direct generation and ABC-CoT generation.

The listed task allocation is approximately:

- Lyrics-to-music/instrumental generation: 6B,
- Lyrics-to-music with ABC-CoT: 2B,
- Cover-song generation: 4B,
- Vocal-to-mix generation: 2B,
- Additional conditioning variants involving references and dry vocals.

DPO uses:

- Approximately 500 prompts,
- Four caption–lyrics instances per prompt,
- Four audio candidates per instance,
- Approximately 2,000 expert preference pairs.

Experts rank musicality, melodic/harmonic coherence, condition adherence, vocal performance, and perceptual quality.

The paper does **not** report the MoE’s total or active parameter count, number of experts, training hardware, wall-clock training time, or total compute. These omissions materially limit reproducibility.

---

### 3. Evaluation results

#### 3.1 Objective comparison — Table 3, p. 13

The main comparison uses:

- 339 lyrics-to-song conditions for AudioBox-Aesthetics and MuQ-MuLan,
- 316 vocal conditions for SongBench,
- One generated sample per condition,
- Suno V5.5, Suno V5, Mureka V9, and MiniMax Music 3 as commercial baselines.

##### Caption alignment and AudioBox-Aesthetics

| Metric | StepAudio 3 | Best baseline |
|---|---:|---:|
| MuQ-MuLan | **0.4465** | 0.4437 |
| Content Enjoyment | **7.7086** | 7.6823 |
| Content Usefulness | **8.0052** | 7.9584 |
| Production Quality | **8.3868** | 8.2988 |
| Production Complexity | 6.5595 | descriptive, not ranked |

The authors claim the best MuQ-MuLan, Content Enjoyment, Content Usefulness, and Production Quality scores.

##### SongBench

StepAudio 3 scores:

| Dimension | Score |
|---|---:|
| Melody | 6.5394 |
| Arrangement | 6.9122 |
| Vocal | 7.0172 |
| Instrumental | 7.0086 |
| Mixing | 6.7284 |
| Structure | 6.5544 |
| Musicality | 5.7465 |

Mureka V9 leads every SongBench dimension in this comparison. Thus, StepAudio’s superiority is **metric-dependent**, not universal.

#### 3.2 Artificial Analysis Music Arena

The supplied leaderboard snapshot reports:

- Quality Elo: **1105**
- Rank: **4th among the systems shown**
- 95% confidence interval: approximately **−14/+14**
- Samples: **2,119**

The paper explicitly calls the figure a supplied preliminary result and notes that this evaluation uses different prompts and task conditions from the internal benchmark.

#### 3.3 Detokenizer ablation — Table 4, p. 14

Direct VAE reconstruction improves substantially from 25 Hz to 50 Hz:

- MCD: 4.79 → **3.59**
- SI-SNR: 4.21 → **7.68**
- SDR: 5.54 → **8.57**

For token-conditioned rendering, the 0.9B DiT is generally best:

| DiT | MCD | MS-Mel-L1 | SI-SNR | SDR | UTMOS |
|---|---:|---:|---:|---:|---:|
| 0.9B | **5.48** | **1.32** | −19.49 | −2.97 | **3.45** |
| 4B | 6.72 | 1.63 | −23.27 | **−2.47** | 3.07 |
| 8B | 7.42 | 1.89 | −21.38 | −3.05 | 3.20 |

The 4B model is better only on SDR. The authors interpret this as evidence of a tokenizer-imposed information ceiling: increasing renderer size does not reliably improve output.

#### 3.4 DPO ablation — Table 5, p. 15

| Configuration | SB Musicality | SB Mean | CE | PQ | MuQ-MuLan |
|---|---:|---:|---:|---:|---:|
| SFT | 5.6395 | 6.5445 | 7.6259 | 8.2700 | 0.4157 |
| SFT + DPO | **5.7465** | **6.6438** | **7.7086** | **8.3868** | **0.4465** |

DPO improves all reported metrics, although the evaluation uses SongBench for both filtering SFT data and evaluation, reducing independence.

#### 3.5 Planning and plan editing — Table 6, p. 15

Mean SongBench score:

- Direct: **6.6438**
- ABC-CoT: **6.6713** (+0.0275)
- ABC-CoT + LLM editing: **6.7220** (+0.0781 versus Direct)

LLM-edited ABC-CoT improves every reported dimension:

- Melody: 6.6454
- Arrangement: 7.0211
- Vocal: 7.0282
- Instrumental: 7.0396
- Mixing: 6.8483
- Structure: 6.6411
- Musicality: 5.8300

Largest gains over Direct are reported for Mixing (+0.1199), Arrangement (+0.1089), and Melody (+0.1060).

**Interpretation:** This is the strongest evidence in the paper for explainable controllability, but it measures evaluator scores—not whether the rendered audio exactly follows the ABC plan.

---

### 4. Audio examples and release status

#### Official showcase

The official website advertises:

- Song generation,
- Instrumental generation,
- Cover generation,
- Dry-vocal-to-mix generation,
- 48-kHz stereo full-song output.

The showcase contains curated static audio assets organized into four sections of five examples. Examples include:

- `audio/tracks/t-03.mp3` — listed duration 3:12,
- `audio/tracks/t-18.mp3` — listed duration 3:10,
- Reference-song assets such as `audio/refs/ref-song-03.mp3`.

These are demonstration assets, not the benchmark samples used for Tables 3–6.

The API page describes a preview model identifier, `stepaudio-3-music-preview`, with natural-language lyrics/prompts and reference-audio inputs. It advertises limited-time free access and indicates that a paid service is planned.

#### What is not released

As of inspection, I found no public:

- Model weights,
- MoE checkpoint,
- Tokenizer checkpoint,
- DiT/VAE checkpoint,
- Training code,
- Training dataset,
- Evaluation generation files,
- Reproducible local inference package,
- Public symbolic ABC-CoT intermediate outputs.

The website’s ABC/notation material is promotional or planned-interface material; it does not amount to an open symbolic planning implementation. The page also indicates that a fuller Voice Studio experience is forthcoming.

---

### 5. Limitations

The paper explicitly acknowledges:

1. **No note-, chord-, or bar-level adherence evaluation.** Caption similarity is not symbolic adherence.
2. SongBench is used to filter SFT data, so evaluation is not fully independent.
3. The main benchmark uses one sample per condition and does not measure sampling variance.
4. Invalid outputs were removed when constructing common subsets.
5. Commercial baselines were accessed through hosted services, whose inference settings cannot be reproduced locally.
6. The objective benchmark is dominated by vocal and lyrics-conditioned generation.
7. Instrumental, cover, and vocal-to-mix capabilities are not equally established by the reported common-subset evaluation.
8. The Artificial Analysis arena uses different prompts, generated lyrics, voters, and task conditions.
9. The authors’ interpretation that music-theoretic knowledge explains improvements is not separately isolated by a controlled listening study.
10. The conclusion identifies complex arrangements, very long temporal dependencies, vocal naturalness, and high-frequency reconstruction as remaining challenges.

---

### 6. Feasibility for a small PhD research group

#### Not realistically feasible

Reproducing the complete system from scratch is frontier-scale because it requires:

- More than 100M songs,
- Approximately 1T corpus tokens,
- Approximately 1.18T consumed pretraining tokens,
- A large MoE language model,
- A 0.6B tokenizer,
- A 0.9B DiT renderer,
- Large-scale multilingual annotation and source separation,
- Expert preference data,
- Significant undisclosed compute.

The API is usable for qualitative black-box experiments, but not for reproducible architecture or training research.

#### Feasible

A small group can reproduce the **research idea** at a much smaller scale:

1. Use ABC, MIDI, or another symbolic representation as an explicit intermediate plan.
2. Train or adapt a small language model for plan generation and editing.
3. Use an existing symbolic or audio renderer rather than training the full codec/DiT stack.
4. Construct exact symbolic evaluation:
   - Note adherence,
   - Chord adherence,
   - Bar/beat alignment,
   - Tempo/key consistency,
   - Minimal-edit distance,
   - Source attribution,
   - Constraint satisfaction.
5. Compare direct generation, plan-first generation, and plan editing.
6. Use the public API only as an audio-quality reference, not as a reproducible baseline.

---

### 7. Relevance to controllable/explainable symbolic mashup and repair

#### Strong relevance

StepAudio provides a useful architecture pattern:

> condition → explicit symbolic arrangement plan → token/audio realization

Its ABC-CoT plan is:

- Human-readable,
- Temporally organized,
- Potentially editable,
- A natural location for explaining harmony, rhythm, melody, and form decisions.

The Table 6 results support the hypothesis that editing an intermediate symbolic plan can improve downstream musical quality.

#### Important gaps for mashup and repair

The paper does not demonstrate:

- Combining two or more source songs with explicit source roles,
- Provenance tracking for copied or transformed material,
- Conflict detection between source melodies/chords/rhythms,
- Minimal repair,
- Exact preservation of a requested vocal or melody,
- Note-level or bar-level guarantees,
- User-visible explanations of why a repair was made,
- Round-trip symbolic extraction and verification.

Cover generation is related to reference-conditioned transformation, and vocal-to-mix is relevant to accompaniment, but neither is equivalent to symbolic mashup or repair.

#### Recommended research direction

A PhD-scale adaptation would retain the plan-first idea but make the plan explicitly symbolic and verifiable:

- Represent each musical event with source provenance.
- Add constraint and conflict annotations.
- Let an LLM propose edits to ABC/MIDI rather than directly edit audio.
- Render the repaired plan.
- Re-extract symbolic structure from the result.
- Verify exact constraints automatically.
- Report both musical-quality metrics and repair correctness.

**Overall assessment:** StepAudio 3 Music is a strong frontier-scale demonstration that explicit musical planning can improve controllability and perceived quality. For explainable symbolic mashup/repair, its most transferable component is the intermediate-plan interface—not its opaque end-to-end audio model.

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
