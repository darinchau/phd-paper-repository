---
title: "Scaling Self-Supervised Representation Learning for Symbolic Piano Performance"
authors: "Louis Bradshaw, Honglu Fan, Alexander Spangher, Stella Biderman, and Simon Colton"
year: 2025
doi: 10.48550/arXiv.2506.23869
category: data-and-representation
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/bradshaw-2025-scaling-self-supervised-representation.pdf"
pdf_filename: bradshaw-2025-scaling-self-supervised-representation.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-21
---

# Scaling Self-Supervised Representation Learning for Symbolic Piano Performance

## One-line Summary

Pretraining a 650M autoregressive transformer on 60,473 hours of Aria-MIDI transcriptions, then adding a SimCLR-style contrastive finetuning stage, produces symbolic piano embeddings that beat MERT, M3, and CLaMP 3 on linear probes, and a generator that beats Anticipatory Music Transformer and MusicGen in listening tests while tying Suno 3.5 and human continuations.

## 1. Document Information

- **Authors and affiliations:** Louis Bradshaw (Queen Mary University of London; EleutherAI), Honglu Fan (University of Geneva; EleutherAI), Alexander Spangher (University of Southern California; EleutherAI), Stella Biderman (EleutherAI), Simon Colton (Queen Mary University of London).
- **Venue and version:** ISMIR 2025; arXiv 2506.23869v1, 30 June 2025. 9 PDF pages: content pp. 1–4, references pp. 5–9.
- **Extraction:** full text via `pdftotext -layout`; Tables 1–2, Figures 1–2, tokenizer description, and training recipe inspected.
- **Artifacts:** Aria model and MIDI processing/tokenization library at `https://github.com/eleutherai/aria`; Aria-MIDI at `https://github.com/loubbrad/aria-midi`.
- **Anchors:** tokenizer §3.1 pp. 2–3; model and pretraining §3.2 pp. 3–4; contrastive objective §3.3 p. 4 (Eq. 2); listening test Table 1 p. 3; probe results Table 2 p. 4.

## 2. Key Contributions

1. **Aria**, a 650M-parameter decoder-only transformer pretrained by next-token prediction on 820,944 files / 60,473 hours of solo-piano MIDI, then finetuned for continuation.
2. **A SimCLR adaptation for symbolic music.** Two non-overlapping 100–650-note slices of the same file are positive views; augmented and tokenized; the final hidden state at an appended end-of-sequence token is projected to 512 dimensions; NT-Xent with temperature 0.1. Crucially, contrastive training only works as a second stage on top of next-token pretraining.
3. **State-of-the-art linear probes** on genre, form, musical period, composer, Pianist8, and VG-MIDI, against MERT, M3, and CLaMP 3.
4. **A human listening test** of 45-second continuations from 15-second prompts with 46 musically trained participants, against Anticipatory Music Transformer, MusicGen, Suno 3.5, and ground-truth human continuations.

## 3. Methodology and Architecture

- **Tokenizer (§3.1).** 10 ms onset/duration resolution; 12 velocity bins; 13 instrument classes (12 GM groups plus percussion). A note is `[instrument, pitch, velocity]`, `[onset]`, `[duration]`; onsets are absolute within 5,000 ms segments, marked by `<T>`. The authors argue absolute segment-relative onsets avoid the temporal drift of relative time-shift tokens for transcribed performance timing, and the tokenizer natively accepts multi-track MIDI even though training is piano-only. Metadata (key, tempo, metre) is discarded; sustain pedal is folded into durations.
- **Model (§3.2).** LLaMA 3.2 1B configuration reduced to hidden size 1,536, 24 heads, standard multi-head attention and LayerNorm, about 650M parameters. Sequence length 8,192 tokens; online transposition ±5 semitones, tempo ±20%, velocity ±10%.
- **Data.** 60,473 hours after filtering: deduplication of over-represented works (at most 10 performances per opus/piece for prolific composers), removal of files without compositional identifiers for those composers, note-density/pitch/duration-entropy/silence/repetition heuristics, and removal of Black MIDI. 75 epochs, AdamW, lr 3e-4, 1,000 warmup steps, 9 days on 8×H100.
- **Generative finetuning.** One epoch on a higher-quality, deduplicated subset with a `<D>` token about 100 tokens before the end, enabling controllable endings.
- **Contrastive finetuning.** 25 epochs, lr 1e-5, one positive pair per file per epoch, 512-dimensional projection. Ablations vary epochs (1/25), temperature (0.05/0.1), and training from scratch without the pretrained initialization.

## 4. Key Results and Benchmarks

**Listening test (Table 1, p. 3).** Aria wins 38–6 against Anticipatory Music Transformer (p = 9.4e-7), 49–0 against MusicGen (p = 3.6e-15), ties Suno 3.5 (18 wins / 9 ties / 21 losses, p = 0.75), and ties human ground truth (15/9/17, p = 0.86). This is evidence for local 45-second coherence under a specific prompt set and participant pool, not for full-piece composition.

**Linear probes (Table 2, p. 4).**

| Model | Genre | Form | Period | Composer | Pianist8 | VG-MIDI |
|---|---:|---:|---:|---:|---:|---:|
| MERT | 83.0 | 63.9 | 69.5 | 69.6 | 65.1 | 45.5 |
| M3 | 85.1 | 69.9 | 71.2 | 71.9 | 81.9 | 54.6 |
| CLaMP 3 | 89.1 | 77.8 | 80.6 | 84.5 | 80.7 | 45.5 |
| AriaEmb (frozen) | 92.4 | 82.5 | 84.7 | 90.5 | 91.6 | 63.6 |
| AriaFt (supervised) | 93.2 | 87.5 | 86.5 | 96.3 | 91.6 | 68.2 |

Scores are accuracy; macro-F1 is within about one point. The contrastive-from-scratch ablation (25 epochs, no pretraining) collapses to 65.5 composer accuracy versus 90.5, which is the paper's strongest evidence that the generative pretraining, not the contrastive objective alone, supplies the transferable structure.

**Few-shot finetuning.** With 100/200/500/1,000 labelled files, composer accuracy is 78.1/85.2/90.1 and genre 91.1/90.8/91.4 (the table's 1,000-file column is partly empty). The claim is that a few hundred labels suffice, not that the model is label-free.

**Limits of the comparison.** All probes are solo piano, while MERT, M3, and CLaMP 3 were trained for broader material; the authors acknowledge this. The listening test excludes closed models (AudioLM) and MuPT because ABC bar-level timing is incompatible with millisecond MIDI.

## 5. Limitations and Future Work

- **Piano only.** The tokenizer is multi-track-capable, but no multi-instrument training or evaluation is reported.
- **Transcription-defined corpus.** All training data comes from Aria-MIDI; errors and style biases of Aria-AMT are inherited and not separately measured.
- **Probe scope.** Genre/form/period/composer labels come from LLM-extracted metadata, so label noise and taxonomic inconsistency are unquantified. Pianist8 and VG-MIDI are small.
- **Listening scope.** 46 participants, five prompts, 45-second continuations; no full-piece, structural, or long-horizon evaluation, and no musician control task.
- **No explanation.** Embedding dimensions and attention are not interpreted; the paper demonstrates transfer, not mechanism.

## 6. Related Work

- Aria-MIDI (the corpus), Aria-AMT (the transcriber), MAESTRO and Music Transformer (the data-scaling precedent).
- MusicBERT and MidiBERT-Piano: masked symbolic pretraining; CLaMP/CLaMP 2/CLaMP 3 and M3: contrastive symbolic-text retrieval; MERT: self-supervised audio.
- SimCLR, SimCSE, and NT-Xent: the contrastive recipe adapted here.
- Anticipatory Music Transformer, MusicGen, Suno 3.5: generation baselines.

## 7. Glossary

- **SSL:** Self-Supervised Learning.
- **NT-Xent:** Normalized Temperature-scaled Cross-Entropy loss.
- **SimCLR:** A Simple Framework for Contrastive Learning of Visual Representations.
- **Linear probe:** training a linear classifier on frozen embeddings.
- **AriaEmb / AriaFt:** the frozen contrastive embedding model / the supervised-finetuned classifier in Table 2.
- **AMT:** Automatic Music Transcription.
- **MIR:** Music Information Retrieval.
