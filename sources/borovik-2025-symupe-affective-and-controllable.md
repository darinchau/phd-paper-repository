---
title: "SyMuPe: Affective and Controllable Symbolic Music Performance"
authors: Ilya Borovik, Dmitrii Gavrilev, Vladimir Viro
year: 2025
doi: 10.1145/3746027.3755871
category: generation-and-planning
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/borovik-2025-symupe-affective-and-controllable.pdf"
pdf_filename: borovik-2025-symupe-affective-and-controllable.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-16
---

## One-line Summary

Borovik et al. train PianoFlow, a 24M-parameter conditional flow-matching transformer for expressive piano performance rendering, on a curated 2,968-hour score–performance corpus (PERiScoPe), and add emotion/text control through a 33-emotion classifier whose soft labels weight Flan-T5 template embeddings; the model wins 67.1% of blind pairwise listening comparisons and 57.1% against real dataset performances, but the training corpus and emotion-labeled recordings are partly proprietary and unreleased, and the human-comparison win is qualified by transcribed-MIDI sources and non-musician listeners.

## 1. Document Information

- **Exact title:** *SyMuPe: Affective and Controllable Symbolic Music Performance*. [PDF p. 1]
- **Authors:** Ilya Borovik (Skoltech), Dmitrii Gavrilev (Skoltech), Vladimir Viro (Peachnote GmbH). [PDF p. 1]
- **Source record:** arXiv `2511.03425v1` (cs.SD, 5 Nov 2025); published in *Proceedings of the 33rd ACM International Conference on Multimedia (MM '25)*, Dublin, DOI `10.1145/3746027.3755871`. The ingested PDF is the author's ACM camera-ready version ("posted here for your personal use"), not the ACM Version of Record. The ACM MM 2025 Outstanding Paper Award is claimed on the authors' GitHub repository, not in the PDF itself. [PDF p. 1; repository inference from external project page]
- **Length and denominator:** 16 physical PDF pages (main body pp. 1–9, references pp. 9–12, appendices A–F pp. 12–16). This digest checked **16/16 pages**. The paper prints no page numbers; anchors use physical PDF pages.
- **Extraction method:** full PDF extracted with PyMuPDF (UTF-8). All main tables (1–2) and figures (1–5) checked against extracted text; no corruption detected in the main body. Appendix E per-piece win rates and the emotion co-occurrence description were read from the extraction.
- **Canonical integrity:** SHA-256 `22abe3b66849efcd592234fb7c7bc413c8eb1aae5b20618d9e94655dd9d3deb6`. The canonical `papers/` copy was downloaded directly from `arxiv.org/pdf/2511.03425`.
- **Availability boundary:** demo page and GitHub code repository are referenced; the 2,215-hour proprietary performance data and the internal 33-emotion recording dataset are explicitly not distributable (raw audio is never stored, per the ethical statement). This bounds independent reproduction of the headline results.

This digest distinguishes author-reported claims (default), values verified against the extraction (marked), and repository interpretation.

## 2. Key Contributions

1. **SyMuPe framework** — a MidiTok-based tokenizer plus configurable transformer models (encoder MLM, encoder–decoder CLM, and flow matching) for score→performance rendering. [PDF pp. 1, 4]
2. **PianoFlow** — a conditional flow-matching (OT-CFM) performance-inpainting model with multi-mask training; claims state-of-the-art rendering quality at near-real-time inference (355 notes/s on a V100). [PDF pp. 1, 4–5]
3. **PERiScoPe dataset** — 2,968 hours / 36,977 performances / 1,176 pieces / 67 composers of note-aligned score–performance pairs (partly proprietary). [PDF p. 5, Table 1]
4. **Emotion/text conditioning** — a 33-emotion classifier (top-1/3/5 accuracy 32%/57%/73%) whose bar-level soft labels weight Flan-T5 template embeddings, enabling arbitrary text prompts to steer expression. [PDF pp. 1, 5–6, 8]

## 3. Methodology and Architecture

- **Representation:** four real-valued score features per note (pitch, position, position shift, duration; positions resolved to 1/96th notes, bars up to 2 whole notes) and four real-valued performance features (velocity, time shift, time duration, sustained duration). Real values avoid quantization loss; pedal is approximated by the factorized pressed/sustained duration pair. Sequences sorted by score time then pitch. [PDF pp. 4–5]
- **Objective:** masked conditional flow matching — `L = E||m ⊙ (u(x_t|x) − v_t(x_t, x_ctx, y; θ))||²` over OT linear-interpolation paths; only masked positions are supervised. [PDF p. 4, eqs. 5–7]
- **Multi-mask training:** five mask families (random notes, beats, bars, contiguous segments, end-of-sequence continuation) sampled uniformly for half the batch; the other half is fully masked (unconditional rendering). This yields one model supporting inpainting, continuation, and full rendering. [PDF p. 5]
- **Architecture:** 8-layer transformer encoder, d=512, 8 heads, single key-value attention, RoPE, SwiGLU; sinusoidal flow-time embedding injected via adaptive layer norm; 24M parameters. Inference uses a 10-step ODE solver with adaptive step size (γ=0.75). [PDF pp. 5, 6]
- **Conditioning:** score tempo/velocity tokens from MusicXML direction markings and local beat-tempo tokens; emotion-weighted Flan-T5-base text embeddings (16 templates × 33 emotions, probability-weighted per bar). All control embeddings are added before the middle (5th) layer; classifier-free guidance with per-input dropout 0.2 and inference-time interpolation strength α (eqs. 8–9). [PDF pp. 5–6]
- **Data pipeline:** (n)ASAP + ATEPP (metadata-fixed) + proprietary web audio (IMSLP title search, Transkun V2 transcription) + PDMX scores; Parangonar alignment with deviating-onset cleanup and interpolation of unperformed notes (7.5% of notes interpolated); composition-level train/val/test splits to prevent leakage. [PDF pp. 4–5]
- **Baselines:** internal MLM encoder and EncDec (ScorePerformer-style, both 24M) plus VirtuosoNet/ISGN (5M, official checkpoint) and DExter (62M, official checkpoint, score-only conditioning). External models may have seen ASAP/ATEPP test material during their training. [PDF pp. 6–7]

## 4. Key Results and Benchmarks

- **Objective (Table 2):** PianoFlow has the best correlations with human performances for IOI (0.86 vs dataset ceiling 0.90), OD (0.09), and Art (0.35); VirtuosoNet is best on velocity correlation (0.48 vs 0.43). On KL divergence the internal MLM encoder is closest overall, but the listening test shows KL does not track perceptual quality (MLM win rate 25.7% internally). Score conditioning tokens improve PianoFlow on all features (ablation row). [PDF pp. 7, Table 2]
- **Listening test:** 32 recruited, 26 retained participants (≥10 non-click-through evaluations), 708 paired ratings over 20 pieces spanning Baroque–Impressionist; synthesized with Pianoteq; Telegram-bot side-by-side protocol. Overall win rates: PianoFlow 67.1% > Dataset 59.6% > VirtuosoNet 51.0% > Deadpan 41.8% > DExter 27.7%. PianoFlow beats real dataset performances 57.1% head-to-head. [PDF pp. 7, Fig. 2; App. E]
- **Human-comparison caveat (authors' own):** two-thirds of "real" samples are audio-transcribed MIDI, and non-musician listeners may prefer the model's smoother predictions; the authors' fair statement is that PianoFlow "outperforms the average combination of human MIDI performances in ASAP and ATEPP", not human performance per se. DExter's low score is partly attributed to its slow 1000-step batched inference and abnormal timing changes on some scores. [PDF pp. 7–8]
- **Emotion control (Fig. 4, qualitative):** on Mozart K.331/III "Alla Turca", "anger" raises loudness and sustain; "dreamy"/"sad" slow the performance; the out-of-scope prompt "thunderstorms and lightning" yields louder but not faster playing; combined "sad and angry" interpolates between the two single-emotion renderings. [PDF p. 8]
- **Inpainting (Fig. 5, qualitative):** a two-style transition (passionate → lento) inpainted over a 64-note span changes gradually and aligns with bar boundaries (not perfectly smooth, authors' note); masking the left hand of Beethoven Op.79/III yields a full-sounding complement of the right hand. [PDF p. 8]
- **Efficiency:** notes per second on V100 — MLM 3450 (temporally incoherent), VirtuosoNet 1700, PianoFlow 355, EncDec 80, DExter 30. [PDF p. 7, Table 2]

## 5. Limitations and Future Work

- Proprietary data (74.6% of the corpus hours) and the emotion-recording dataset cannot be released; reproduction of PERiScoPe-scale training is not possible from the paper alone. [PDF pp. 5, 16]
- External baselines run with official checkpoints on possibly-seen repertoire, and retraining them on PERiScoPe was deemed non-trivial — an asymmetry the authors acknowledge. [PDF pp. 6–7]
- The listening-test population is not screened for musical expertise, per-piece win rates vary widely (e.g., PianoFlow 33.3% on Elgar vs 92.9% on Chopin Ballade No. 1), and participant feedback says some choices were tempo-driven; the authors themselves advise reading per-piece results and warn that survey composition alters ratings. [PDF pp. 7, 15–16, App. E]
- Emotion classification accuracy (32% top-1 over 33 classes) is low; control was only demonstrated qualitatively on a single piece, with no controlled evaluation of how strongly text changes audible expression. [PDF pp. 7–8]
- Repository inference: the claim of "interpretability" in the conclusion refers to intuitive text control of a black-box renderer, not to any explanation or trace of how performance decisions are made.

## 6. Related Work

Positions itself against ScorePerformer (Borovik & Viro 2023, the EncDec baseline's ancestor), VirtuosoNet/ISGN, DExter (diffusion), and audio-domain renderers; first application of flow matching to symbolic performance rendering per the authors. Emotion coverage (33 labels) exceeds the usual 4–6 label setups. [PDF pp. 2–3]

## 7. Glossary

- **EPR (expressive performance rendering):** generating an expressive performance (timing, dynamics, articulation) from a symbolic score.
- **OT-CFM (optimal-transport conditional flow matching):** regression of a vector field on linear-interpolation probability paths between noise and data; enables few-step ODE sampling.
- **Multi-mask training:** randomly choosing which performance features to inpaint during training (notes/beats/bars/segments/end).
- **PERiScoPe:** Piano Expression Refined Score and Performance, the authors' combined 2,968-hour aligned corpus.
- **Flan-T5:** Google's instruction-tuned T5 text encoder used to embed emotion templates.
- **Classifier-free guidance (CFG):** training-time control dropout plus inference-time interpolation between conditional and unconditional vector fields (strength α).
