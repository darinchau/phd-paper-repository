---
title: "Sori: Streamable and Controllable Model for Non-musical Audio to Symbolic Music Transformation"
authors: Kyungsu Kim, Yejin Kim, Kyogu Lee
year: 2026
doi: 10.48550/arXiv.2610.15474
category: generation-and-planning
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/kim-2026-sori-streamable-and-controllable.pdf"
pdf_filename: kim-2026-sori-streamable-and-controllable.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-31
---

## One-line Summary

Sori names and attacks a new task — turning non-musical audio such as rain, a cough, or speech into symbolic music — by training an encoder–decoder Transformer on musical data only with a domain-adversarial encoder, so that one classifier-free-guidance dial continuously trades how closely the output follows the input against how musical it sounds, in real time on a laptop CPU.

## 1. Document Information

- **Canonical citation:** Kyungsu Kim, Yejin Kim, and Kyogu Lee, “Sori: Streamable and Controllable Model for Non-musical Audio to Symbolic Music Transformation,” arXiv:2610.15474v1 [cs.SD], 11 October 2026, 5 PDF pages. The arXiv record has no venue or acceptance comment; treat it as a preprint.
- **Affiliation:** Music and Audio Research Group (MARG), Seoul National University. [PDF p. 1]
- **DOI:** `10.48550/arXiv.2610.15474` (arXiv DOI).
- **Demo:** `https://soridemo0320.github.io/sori-demo/` (from the batch metadata).
- **Canonical integrity:** SHA-256 `6542e6ec6b3bb735e5fd91167463a224b0de132c21b14814ee73f405f12c305c`.
- **Rights boundary:** arXiv preprint; terms follow the arXiv licence, not restated here. Local research evidence only.
- **Primary category:** `generation-and-planning`. The paper's contribution is a generation interface (audio-conditioned symbolic generation with an inference-time control), not a representation analysis or a benchmark.
- **Evidence levels:** Table 1 and the streaming numbers were re-read from the PDF. The listening protocol is reported as IRB-approved (IRB No. 2512/003-007) with 21 retained participants after an attention check.

## 2. Key Contributions

### A new task and its evaluation axes

Automatic music transcription assumes musical input and one correct score. Non-musical Audio to Symbolic Music Transformation (NASMT) is one-to-many: many scores are defensible for a cough. The paper therefore evaluates two axes in tension — *input correspondence* (does the output track the source's timing and spectrum?) and *musicality* (is the output coherent music?) — rather than a single reconstruction score. [PDF pp. 1–2]

### Learning the mapping without paired data

No paired non-musical-audio/MIDI corpus exists, so the decoder is trained only on musical data and a domain-adversarial objective aligns encoder features between musical and non-musical audio. The adversarial loss is weighted 0.01 and alternates five discriminator updates per encoder–decoder update after a 50k-iteration warm-up on transcription alone. [PDF p. 3]

### One dial for the trade-off

Classifier-free guidance gives a single γ: 0 ignores the input, 1 is standard conditioning, and above 1 amplifies it. This is the paper's interface contribution — an interpretable, continuous control over correspondence versus musicality that a performer could turn in real time. [PDF p. 3, eq. 4]

### Streaming on a consumer CPU

A nested decoder allows at most four events per 50 ms frame with a spillover flag for the rare frame that needs more (99.52% of training timesteps need none), and ALiBi positions plus an attention-sink KV cache keep computation bounded. [PDF p. 3]

## 3. Methodology and Architecture

- **Input.** 16 kHz log-mel spectrogram, 512 bins, 50 ms hop. [PDF p. 2]
- **Encoder.** Eight pre-norm Transformer layers, d = 768, 8 heads, with a CLS representation used by the domain discriminator. [PDF pp. 2–3]
- **Temporal decoder.** Eight layers of causal cross-attention over encoder output, producing per-timestep context. [PDF p. 2]
- **Event decoder.** Four layers, d = 512, generating the note events within a timestep autoregressively; vocabulary of 530 tokens (88 note-off, 88 pitches × 5 velocity bins of note-on, end-of-sequence, padding). Frame-aligned sparse piano-roll targets carry onset, offset, velocity and activity channels. [PDF pp. 2–3]
- **Training data.** Nlakh-style rendering with NSynth sample-based instruments: 9.53M five-second segments over 953 instruments, and 530k held-out test segments over 53 disjoint instruments. The adversarial side uses the downloadable unbalanced AudioSet training split (1.65M five-second clips) and its 17k-clip evaluation split. 300k iterations, AdamW, encoder/decoder learning rate 3 × 10⁻⁵ and discriminator 3 × 10⁻⁶. [PDF p. 3]
- **Metrics.** Onset F1 averaged over 11 DSP-based onset detectors with ±100 ms tolerance (neural detectors are avoided to prevent bias toward musical audio); Multi-Scale Spectrogram distance after FluidSynth rendering; Fréchet Music Distance with CLaMP 2 embeddings against the held-out Nlakh set; and a Prolific listening study on 5-point Likert scales for correspondence and musicality. [PDF p. 3]

## 4. Key Results and Benchmarks

Table 1, AudioSet evaluation set [PDF p. 4]:

| Condition | OnF1 ↑ | MSS ↓ | FMD ↓ | Subj. corr. ↑ | Subj. mus. ↑ |
|---|---|---|---|---|---|
| Sori γ = 0.0 | 0.087 | 57.2 | 143.6 | 1.20 | 2.19 |
| Sori γ = 0.5 | 0.236 | 32.7 | **33.6** | 1.64 | **3.34** |
| Sori γ = 1.0 | 0.327 | 18.3 | 51.3 | 2.61 | 3.27 |
| Sori γ = 2.0 | 0.363 | 13.1 | 161.8 | **2.97** | 2.59 |
| Sori γ = 3.0 | **0.368** | **11.8** | 248.0 | 2.52 | 2.20 |
| Sori without DAT, γ = 3.0 | 0.386 | 10.2 | 324.0 | 2.54 | 1.98 |
| Basic Pitch | 0.210 | 32.8 | 181.8 | 2.35 | 2.15 |
| Deep Salience | 0.300 | 21.7 | 195.2 | 2.63 | 2.37 |
| TimbreTrap | 0.167 | 33.1 | 472.7 | 2.51 | 1.51 |

- **The trade-off is monotone in γ:** onset F1 rises and spectral distance falls as γ grows, while FMD bottoms out at moderate guidance and listening-rated musicality peaks at γ = 0.5. [PDF p. 4]
- **Moderate guidance is the useful operating point:** at γ = 1.0 Sori beats all three transcription references on OnF1, MSS and FMD, with comparable rated correspondence and higher rated musicality. [PDF p. 4]
- **DAT shifts the trade-off rather than dominating it:** the no-DAT ablation has better objective correspondence at every strong-guidance point but worse FMD and rated musicality. [PDF p. 4]
- **Streaming:** mean real-time factor 0.82 (max 0.90) on an Apple M3 CPU at 50 ms frames, with 64 ms algorithmic latency dominated by the centred STFT lookahead. [PDF p. 4]

## 5. Limitations and Future Work

- **The evaluation set is not purely non-musical.** AudioSet splits are used without filtering music clips, so part of the input distribution is already music. [PDF p. 4]
- **No ablation of the nested decoder** or of the spillover mechanism; their contribution to control quality is untested. [PDF p. 4]
- **Musicality is measured inside the training distribution.** FMD is computed against Nlakh, which derives from the same Lakh corpus used for training, so it may not reflect musicality beyond that distribution. [PDF pp. 3–4]
- **Correspondence is DSP-based.** Onset detection and spectral distance do not establish perceptual correspondence; the listening study is the only perceptual evidence.
- **Small listening panel.** 33 participants took part and 12 were excluded by the attention check, leaving 21. [PDF p. 3]
- **Weak musicality baselines.** The reference systems are transcription models, none of which was built for musicality, so the comparison is a floor rather than a strong alternative.
- **Monophonic-ish output.** The score is a single-track piano roll, not an arrangement. [PDF pp. 2–3]

## 6. Related Work

- **Correspondence versus musicality is the repository's own tension.** In mashup and repair the same question appears as *preserve the source* versus *make it musical*; Sori's single interpretable knob is a candidate interface pattern. See [[concepts/audio-symbolic-modality-gap]] and [[overviews/audio-symbolic-transfer]].
- **Audio-to-symbolic generation with explicit control.** [[generation-and-planning/wang-2022-audio-to-symbolic-arrangement-via-cross-modal]] arranges audio into symbolic form with cross-modal representation learning rather than adversarial domain alignment.
- **Cross-modal conditioning without paired data.** [[retrieval-and-recombination/fernandez-mendez-2026-descriptor-injected-cross-modal-learning]] and [[retrieval-and-recombination/wu-2025-clamp-3-universal-music]] also bridge audio and symbolic spaces without paired scores, through descriptor injection and contrastive pretraining respectively.
- **Explanation gap.** [[concepts/auditable-creative-editing-pipelines]] notes that a visible control is workflow transparency; Sori exposes γ but not which input frames caused which events, although its cross-attention could.

## 7. Glossary

- **ALiBi:** Attention with Linear Biases, a positional-encoding scheme.
- **AMT:** Automatic Music Transcription.
- **CFG:** Classifier-Free Guidance.
- **DAT:** Domain-Adversarial Training.
- **FMD:** Fréchet Music Distance, here computed with CLaMP 2 embeddings.
- **IRB:** Institutional Review Board.
- **MSS:** Multi-Scale Spectrogram similarity/distance.
- **NASMT:** Non-musical Audio to Symbolic Music Transformation.
- **OnF1:** Onset F1.
- **RTF:** Real-Time Factor, processing time divided by audio duration.
- **STFT:** Short-Time Fourier Transform.
- **γ:** the classifier-free-guidance strength.
