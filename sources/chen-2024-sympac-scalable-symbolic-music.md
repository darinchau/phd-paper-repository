---
title: "SymPAC: Scalable Symbolic Music Generation With Prompts And Constraints"
authors: "Haonan Chen, Jordan B. L. Smith, Janne Spijkervet, Ju-Chiang Wang, Pei Zou, Bochen Li, Qiuqiang Kong, and Xingjian Du"
year: 2024
doi: 10.48550/arXiv.2409.03055
category: generation-and-planning
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/chen-2024-sympac-scalable-symbolic-music.pdf"
pdf_filename: chen-2024-sympac-scalable-symbolic-music.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-21
---

# SymPAC: Scalable Symbolic Music Generation With Prompts And Constraints

## One-line Summary

SymPAC trains an 86M decoder-only symbolic generator solely on symbolic events extracted from ~1M in-house audio tracks by a stack of MIR models (transcription, beat tracking, chords, sections, tagging), encodes control signals in prompt bars, and enforces user constraints at sampling with finite-state machines; it beats FIGARO and MMT in a 12-participant MOS study and scales with transcribed data.

## 1. Document Information

- **Authors and affiliations:** Haonan Chen, Jordan B. L. Smith, Janne Spijkervet, Ju-Chiang Wang, Pei Zou, Bochen Li, Qiuqiang Kong, Xingjian Du; ByteDance Inc., Queen Mary University of London, and The Chinese University of Hong Kong.
- **Venue and version:** ISMIR 2024; arXiv 2409.03055v2, 9 September 2024. 12 PDF pages: content pp. 1–5, references pp. 6–12.
- **Extraction:** full text via `pdftotext -layout`; Tables 1–5, Figures 1–2, and §5 inspected. The supplement is referenced but not part of this PDF.
- **Artifacts:** no public dataset or model release is stated; the 1M-track corpus is in-house and licensed.
- **Anchors:** motivation §1 p. 1; encoding §3.1 pp. 2–3; FSM §3.2 p. 3 (Algorithm 1); datasets §4.1 p. 3; scaling Table 2 p. 4; control Tables 4–5 p. 5; MOS Table 3 p. 5; conclusion §5 p. 5.

## 2. Key Contributions

1. **A purely transcribed-data training demonstration.** A high-quality multi-track symbolic generator is trained only on MIR outputs from audio, with no manually annotated symbolic corpus. The authors claim this is the first such demonstration.
2. **Prompt bars.** Control signals (genre, section, tempo, chords, active tracks) are encoded as a separate bar sequence before the musical bars, so the decoder sees the full control context before generating notes; missing controls can be inferred by the model.
3. **Constrained generation via finite-state machines.** At each sampling step an FSM restricts the vocabulary to tokens consistent with the encoding grammar and the user's inputs, guaranteeing chord and structure adherence rather than merely encouraging it.
4. **Scale and control evidence.** KLD to a held-out set improves monotonically from 1% to 100% of the in-house data for six of seven metric classes; chord-input accuracy is 87.2%, and structure control is substantially better than unguided generation.

## 3. Methodology and Architecture

- **Data.** Three corpora used separately, never mixed: Lakh MIDI (170K songs, symbolic), Million Song Dataset (1M 30–60 s audio previews), and an in-house licensed corpus (IHD, ~1M full songs, 3,688M notes after transcription). The public MSD route is the reproducible one; IHD is not.
- **MIR extraction.** Pretrained models for beat tracking, chord detection, section detection, multi-track transcription (Time-Frequency Perceiver), and music tagging. Their outputs become tokens. The pipeline is the paper's real dependency: errors in beat tracking or transcription become training targets.
- **Encoding.** REMI+ with bar as the unit. A song bar has meta (bar, genre, section, bpm level), chord (position, chord), instrument tracks (track token, then position/duration/pitch groups), and drum track (position/drum). Prompt bars keep only the control fields. A full piece is all prompt bars, `end_of_prompt`, all song bars, `end_of_song`.
- **Model.** Llama-style decoder, 12 layers, 12 heads, 768 dimensions, ~86M parameters; 10,240-token training windows. No augmentation and no data filtering, on the argument that scale covers the diversity and transposition would distort instrument ranges.
- **Constrained decoding.** The FSM state tracks the grammar and the user's requested values; at each step it returns the allowed sub-vocabulary, and the model samples only from it. This is analogous to regular-expression matching over token sequences.

## 4. Key Results and Benchmarks

**Scaling (Table 2, p. 4).** Average KLD to a 3,000-sample held-out set, lower is better. IHD-100% is best in 6 of 7 classes; IHD-1% is worst in 6 of 7. Examples: chord 0.112 / 0.119 / 0.347; structure 0.348 / 0.220 / 0.786; vocal note 0.416 / 0.892 / 1.086; piano note 0.178 / 0.403 / 0.686. The structure metric is non-monotone (10% beats 100%), which the authors call a possible lucky alignment and leave unresolved.

**Control adherence (Tables 4–5, p. 5).** Chord input: 87.2% (IHD-100), 86.9% (IHD-10), 74.0% (IHD-1), 87.6% (MSD). Structure: HR3F/PWF/Sf = 0.60/0.50/0.50 with the full model, versus 0.54/0.47/0.47 for IHD-1%; with oracle segmentation 0.72/0.80. These metrics measure whether the generated structure matches the requested one, not whether the music is good.

**Subjective evaluation (Table 3, p. 5).** Twelve MIR researchers/producers rated 10 samples per model on five 5-point scales. Overall MOS: SymPAC-IHD 3.60, SymPAC-LMD 3.25, SymPAC-MSD 3.07, FIGARO 2.74, MMT 2.16. SymPAC-IHD beats FIGARO on richness (3.58 vs 2.73), arrangement (3.45 vs 2.85), structure (3.73 vs 2.62), and overall (3.60 vs 2.74); coherence is 3.55 vs 3.12. The sample is small and the raters are not a general listener population.

**What the comparison does not isolate.** The IHD model has more data and a different distribution than LMD; the LMD model is the same-size-data comparison and still beats FIGARO overall (3.25 vs 2.74), but the paper does not control for training compute or encoding differences.

## 5. Limitations and Future Work

- **In-house corpus.** The headline scale result depends on 1M licensed tracks that cannot be inspected or reproduced; the public MSD arm is weaker.
- **Coarse musical resolution.** Position/duration are quantized to 1/16 bar, which handles 4/4 poorly for 3/4 and 6/8; chords are limited to 12 major/minor triads. This rules out much classical repertoire and fine harmonic control.
- **Sequence length.** Average IHD sequence is ~8,000 tokens; the model needs BPE or compound tokens to scale further.
- **Transcription and beat-tracking errors are inherited.** The paper measures output quality, not label quality; a wrong downbeat becomes a wrong bar line in training.
- **Control ≠ quality.** The FSM guarantees grammar and requested tokens, not musical coherence; the structure metric can be satisfied by repetitive output.
- **Evaluation size.** 12 raters, 10 samples each, no confidence intervals or significance tests reported beyond the text.

## 6. Related Work

- Music Transformer, REMI, Pop Music Transformer, FIGARO, MMT: symbolic generation and control-token precedents.
- MT3 and Time-Frequency Perceiver: multi-track transcription used in the pipeline.
- Music Structure Analysis (Foote, 2D-Fourier) and mir_eval: the structure evaluation stack.
- VAE-based control (MusicVAE, MuseMorphose) and encoder-decoder control (FIGARO): the alternatives SymPAC argues against.
- MSD, Lakh, MAESTRO, GiantMIDI: the dataset landscape in Table 1.

## 7. Glossary

- **MIR:** Music Information Retrieval.
- **FSM:** Finite State Machine.
- **REMI+:** multi-track Revamped MIDI encoding.
- **IHD:** In-House Dataset (licensed, unreleased).
- **MSD:** Million Song Dataset.
- **LMD:** Lakh MIDI Dataset.
- **KLD:** Kullback–Leibler Divergence.
- **MOS:** Mean Opinion Score.
- **HR3F / PWF / Sf:** structure boundary F-measure / pairwise clustering F-measure / entropy F-measure.
