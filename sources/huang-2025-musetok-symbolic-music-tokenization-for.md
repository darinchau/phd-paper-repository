---
title: "MuseTok: Symbolic Music Tokenization for Generation and Semantic Understanding"
authors: "Jingyue Huang, Zachary Novack, Phillip Long, Yupeng Hou, Ke Chen, Taylor Berg-Kirkpatrick, and Julian McAuley"
year: 2025
doi: 10.48550/arXiv.2510.16273
category: data-and-representation
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/huang-2025-musetok-symbolic-music-tokenization-for.pdf"
pdf_filename: huang-2025-musetok-symbolic-music-tokenization-for.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-20
---

# MuseTok: Symbolic Music Tokenization for Generation and Semantic Understanding

## One-line Summary

MuseTok learns a bar-wise residual vector-quantized code stack (RQ-VAE) over REMI+ piano scores, reconstructs near-losslessly at 16 levels, drives a two-stage code-then-events generator that beats REMI+ and AMT on objective continuation similarity but loses on rated Pitch and Harmony, and offers qualitative evidence that early codebooks carry transposition-invariant information while deeper ones carry absolute pitch.

## 1. Document Information

- **Authors and affiliation:** Jingyue Huang, Zachary Novack, Phillip Long, Yupeng Hou, Ke Chen, Taylor Berg-Kirkpatrick, Julian McAuley (University of California San Diego).
- **Version:** arXiv 2510.16273v1, submitted 18 October 2025; 5 pages (four of content plus references). The arXiv comment is not recorded here; the publisher DOI found in search results (10.1109/icassp55912.2026.11463020, ICASSP 2026) was not opened, so venue acceptance is recorded as reported by the code repository README ("official code for ICASSP 2026 paper"), not verified from the proceedings.
- **Extraction denominator and method:** all **5/5 pages** read. Text taken from the bundled LaTeX source (`MuseTok.tex`, 555 lines), treated as source of truth for numbers; pages 2–4 rendered to PNG at 120 DPI and checked visually for Figure 1 (architecture), Table 1 (tokenization), Table 2 (generation), Table 3 (understanding), Figure 2 (code usage) and Figure 3 (pitch-shift similarity). The LaTeX source archive is stored as `papers/huang-2025-musetok-symbolic-music-tokenization-for.tar.gz`.
- **Released artefacts (checked 2026-10-20):** GitHub `Yuer867/MuseTok` (commit `7b71d16`, last push 2026-01-19, no licence file declared via the GitHub API). It contains training scripts for tokenizer and generator (`train_tokenizer.py`, `train_generator.py`), reconstruction/generation/evaluation scripts, configs, the REMI+ vocabulary pickle and data-processing code. The README links a Google Drive `ckpt.zip` (988,813,361 bytes; SHA-256 `4d910671…94f8db31`) containing `ckpt/best_tokenizer/model.pt` (376 MB) and `ckpt/best_generator/model.pt` (693 MB). The tokenizer state dict has 16 SimVQ codebooks of shape 2048 × 128 and 94.1M parameters, i.e. the paper's **MuseTok-Large**. **MuseTok-Small (D=8), on which the Section 4.5 analyses were run, is not released.** Processed datasets are marked "to be released".
- **Local check:** with torch 2.5.1+cpu the released tokenizer loads, encodes the repo's bundled test MIDI, and the sum of the 16 per-level code vectors equals the returned latent to 3×10⁻⁷. On a quantised synthetic 16-bar piano pattern, greedy decoding of the first four bars reproduced the event sequence exactly at depth 16 (112/112 events). The bundled `test/Classic_358.mid` is unquantised performance timing and decodes at only 0.37 event accuracy because the encoder snaps onsets to the score grid; this is a pre-processing mismatch, not a model failure. The repo pins `miditoolkit==4`, which does not exist on PyPI; with miditoolkit 1.0.1 the pre-processing needs a shim because `Note.duration` became read-only.

## 2. Key Contributions

1. **Bar-wise RQ-VAE tokenizer for symbolic music** (Sec. 3.1, Fig. 1). A Transformer encoder maps each bar's REMI+ events to a latent `z_b`; `D` non-shared codebooks quantize the residual stepwise; a Transformer decoder reconstructs the event sequence autoregressively conditioned on the summed code embedding of the current bar.
2. **Two-stage generation** (Sec. 3.2). A separate 152M-parameter Transformer predicts the flattened code stream (16 codes per bar, 256 for a 16-bar sequence) by next-token prediction; the frozen tokenizer decoder then renders events. Codes are predicted serially, not level-parallel.
3. **Understanding probes** at note level (melody extraction), bar level (133-class chord recognition) and song level (4-class emotion) using the code embeddings as classifier input (Sec. 3.3, Table 3).
4. **Qualitative analysis of what codebooks learn** on MuseTok-Small (Sec. 4.5): texture-specific code usage, time-signature differentiation that grows with depth, and pitch-shift invariance decreasing with depth.

## 3. Methodology and Architecture

- **Representation:** REMI+ events (Bar, Beat/position, Note_Pitch, Note_Duration, Time_Signature, EOS; velocity and tempo removed except for the emotion task), onsets and durations aligned to sheet-music positions. Vocabulary 140 events (Sec. 4.1); the released dictionary has `n_token=168` in the model constructor.
- **Quantization (Eqs. 1–3):** `c_b^1 = argmin_k ||z_b − e_k^1||`, `c_b^d = argmin_k ||z_b − e_k^d − Σ_{i<d} r_b^i||`; the decoder conditions on `r_b = Σ_{d=1}^{D} r_b^d`.
- **Training objective (Eqs. 4–5):** `L = L_recon + L_commit`; reconstruction is autoregressive event cross-entropy; the commitment loss is applied cumulatively at every depth (`Σ_d Σ_b ||z_b − sg[Σ_{d'≤d} r_b^{d'} W^d]||²`) with SimVQ linear transforms `W^d` and the rotation trick; codebooks updated by EMA.
- **Configurations:** 12-layer, 8-head, 512-dim encoder and decoder; 16-bar training sequences; random transposition within ±6 semitones; chorale and polyphonic pieces upsampled. MuseTok-Small: D=8, K=1024, 128-dim latent. MuseTok-Large: D=16, K=2048. Adam, lr 1e−4, 200-step warm-up, ~45k steps on one RTX A6000 (Sec. 4.2).
- **Data:** PDMX plus POP909, EMOPIA, Pop1k7, Hymnal, Multipianomide (Classical Piano Midi Page) and Ragtime; time-signature-change pieces split into constant-meter clips of ≥ 8 bars; 195,187 sequences (83.7% monophonic, 13.1% chorale, 3.2% polyphonic), random 8:1:1 split (Sec. 4.1). The split is random at sequence level; the paper does not state whether clips of one piece can fall on both sides.
- **Generator:** 12-layer, 16-head, 1024-dim, 152M parameters, sequence length 256, ~200k steps (~4 days), offline key transposition ±6, nucleus sampling τ = 1.1, p = 0.9, then top-k = 30 (Sec. 4.3).

## 4. Key Results and Benchmarks

### Tokenization (Table 1; PPL lower is better, Acc = 1 − edit/|X|)

| Model | PPL mono. | PPL chora. | PPL poly. | Acc mono. | Acc chora. | Acc poly. | Util |
|---|---|---|---|---|---|---|---|
| VAE (128-dim, upper bound) | 1.123 | 1.086 | **1.159** | 96.70 | 83.59 | 82.21 | – |
| MuseTok-Small (D=8, K=1024) | 1.093 | 1.169 | 1.498 | 97.76 | 80.85 | 62.92 | **99.58%** |
| − w/o SimVQ + rotation | 1.151 | 1.268 | 1.667 | 80.55 | 64.04 | 54.59 | 87.77% |
| − w/o SimVQ | 1.129 | 1.242 | 1.620 | 85.87 | 66.19 | 56.15 | 90.50% |
| − PDMX only | 1.106 | 1.174 | – | 97.91 | 78.11 | – | 99.29% |
| MuseTok-Large (D=16, K=2048) | **1.091** | **1.081** | 1.217 | **99.58** | **93.71** | **82.68** | 98.96% |

Polyphonic material is hardest at every setting; Small loses ~20 accuracy points on polyphony relative to Large. Standard deviations are reported for PPL only; seeds and number of runs are not stated.

### Continuation (Table 2; 4-bar primers)

| Model | sim_chr | sim_grv | Pitch | Structure | Harmony | Development |
|---|---|---|---|---|---|---|
| REMI (same data and size) | 94.61 | 87.41 | **4.099** | **3.927** | **3.927** | **3.646** |
| AMT (`music-small-100k`) | 94.72 | 84.08 | 3.839 | 3.328 | 3.516 | 3.156 |
| MuseTok | **95.19** | **88.77** | 3.698 | 3.839 | 3.604 | 3.635 |

Subjective scores: 5-point Likert, 24 participants × 8 groups = 192 ratings per model per aspect. No confidence intervals or significance tests are reported. The authors attribute the Pitch deficit to more out-of-key notes and note that a fixed 16 codes per bar may add noise for simple (monophonic) bars, which reconstruct well with 8 codes.

### Understanding (Table 3; accuracy %)

| Model | Melody (POP909) | Chord (POP909, 133 classes) | Emotion (EMOPIA, 4 classes) |
|---|---|---|---|
| RNN | 89.98 | 38.03 | 53.46 |
| MIDI-BERT | **90.97** | – | 67.74 |
| MusicBERT | – | – | 77.78 |
| MuseTok | 81.92 | **49.87** | **78.95** |

The emotion model is a MuseTok variant retrained with velocity. Baselines are copied or run with differing classifier heads; the comparison is not head-matched.

### What codebooks learn (Sec. 4.5, MuseTok-Small only, Figs. 2–3)

- **Texture:** top-50 code sets for 1,000 random monophonic, chorale and polyphonic samples are "largely distinct" at both d=1 and d=8.
- **Time signature:** at d=1 the code distribution barely separates six time signatures; at d=8 it diverges. The authors read the first codebook as encoding information shared across metres.
- **Transposition:** cosine similarity between code embeddings of original and pitch-shifted samples stays above 0.7 at d=1 for every shift in ±6 and drops sharply with depth (≈0.0–0.4 by d=2–8 for most shifts; read from Fig. 3). Peaks at ±4, then ±5, ±3 and minima at ±6 are read as interval knowledge. The authors conclude that rhythm and relative contour sit in early codebooks and absolute pitch in deeper ones, while stating that the attributes "are not fully disentangled".

## 5. Limitations and Future Work

- **The level analysis is correlational and on the unreleased Small model.** Code frequency and embedding cosine similarity show what correlates with each depth; no intervention (swap, ablate or resample a level and decode) tests whether the decoder actually uses that information at that depth. Similarity of code *embeddings* under transposition is not the same as invariance of the *decoded music*.
- **Prefix decodability is not evaluated.** The decoder is trained only on the full 16-level sum; Table 1 reports only full-depth reconstruction. Our local check on one synthetic 4-bar pattern gave event accuracy 0.19 / 0.31 / 0.51 / 0.80 / 1.00 at depth 1 / 2 / 4 / 8 / 12, so truncated prefixes decode, but off the training distribution. In that single example the depth-1 decode produced 163 events against 112 in the reference, so even rhythm/density is not intact at depth 1. Any level-wise claim must handle the off-distribution prefix problem.
- **Generation is not coarse-to-fine.** Codes are flattened and predicted serially; there is no level-parallel or level-schedule experiment.
- **Pitch quality:** rated lowest on Pitch among the three systems and below REMI on Harmony; melody extraction is the weakest understanding task.
- **Fixed depth:** the authors list adaptive per-bar depth as future work.
- **Evaluation thinness:** single-run numbers, no seeds, no intervals for listening scores, random sequence-level split.
- **Scope:** single-track piano only; tempo and velocity removed; supported metres 2/4, 3/4, 4/4, 2/2, 3/8, 6/8 (notebook).

## 6. Related Work

- **Discrete music representations:** RQ-VAE (Lee et al., image generation), SimVQ, rotation trick; audio-side discrete tokens (JukeMIR, Sheet Sage) as motivation.
- **Symbolic encodings and pretraining:** REMI, REMI+ (FIGARO), Compound Word, MMT, MIDI-BERT, MusicBERT, PianoTree-VAE, MuseMorphose.
- **Within this knowledge base:** [[data-and-representation/fradet-2023-miditok-a-python-package-for]] (event tokenization tooling), [[data-and-representation/kumar-2023-from-words-to-music-a]] (subword tokenization), [[other/kumbong-2026-ncm-next-concept-modeling-fast]] (multiscale residual VQ code ladder generated coarse-to-fine, with coarse-code intervention probes; text and Sudoku only).

## 7. Glossary

- **RQ-VAE / RVQ:** residual-quantized variational autoencoder / residual vector quantization; each level quantizes the residual left by previous levels.
- **REMI+:** extended REvamped MIDI-derived event encoding with bar, position, pitch, duration and time-signature tokens.
- **SimVQ:** codebook reparameterisation with a learned linear transform over a frozen codebook, used to avoid code collapse.
- **Rotation trick:** gradient estimator for VQ that rotates the encoder output onto the code vector instead of a straight-through copy.
- **EMA:** exponential moving average codebook update.
- **Util:** fraction of codes used at least once on the test set, averaged over levels.
- **sim_chr / sim_grv:** bar-wise chroma and grooving similarity between generated bars and primer bars.
- **AMT:** Anticipatory Music Transformer.
- **PDMX:** Public Domain MusicXML dataset.
- **ICASSP:** IEEE International Conference on Acoustics, Speech and Signal Processing.
