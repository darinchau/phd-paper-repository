---
title: "Scaling Self-Supervised Representation Learning for Symbolic Piano Performance"
authors: "Louis Bradshaw, Honglu Fan, Alexander Spangher, Stella Biderman, and Simon Colton"
year: 2025
doi: 10.48550/arXiv.2506.23869
source: bradshaw-2025-scaling-self-supervised-representation.md
category: data-and-representation
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/bradshaw-2025-scaling-self-supervised-representation.pdf"
pdf_filename: bradshaw-2025-scaling-self-supervised-representation.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-21
tags: [symbolic-piano, self-supervised-learning, contrastive-learning, simclr, embeddings, listening-test, aria]
---

# Scaling Self-Supervised Representation Learning for Symbolic Piano Performance

## Summary

This paper is the strongest existing answer to "does audio-derived symbolic data actually help?" It pretrains a 650M autoregressive transformer on 60,473 hours of Aria-MIDI transcriptions, then adds a SimCLR-style contrastive stage over two slices of the same MIDI file. The frozen embeddings beat MERT, M3, and CLaMP 3 on six linear-probe benchmarks, including composer (90.5% vs 84.5%) and Pianist8 (91.6% vs 81.9%). The generative model beats Anticipatory Music Transformer and MusicGen in a 46-participant listening test and statistically ties Suno 3.5 and human continuations. The critical ablation: contrastive training without the generative pretraining collapses (composer 65.5% vs 90.5%), so the scale and the next-token objective carry the transfer, not SimCLR alone.

## Key Contributions

- **Aria**, a 650M decoder-only symbolic model trained on ~60k hours, with a segment-relative absolute-onset tokenizer designed for performance timing.
- **A two-stage recipe**: next-token pretraining → contrastive finetuning; the paper shows the order is necessary, not cosmetic.
- **SOTA frozen symbolic embeddings** on genre, form, period, composer, Pianist8, and VG-MIDI, with few-shot finetuning needing only a few hundred labels.
- **Human evidence** that large-scale symbolic pretraining yields locally coherent piano continuations competitive with a proprietary audio generator.

## Methodology and Architecture

Tokenizer: 10 ms resolution, 12 velocity bins, 13 instrument classes, `[instrument, pitch, velocity] [onset] [duration]`, absolute onsets within five-second `<T>` segments, pedal folded into duration, metadata discarded. Model: LLaMA-3.2-1B backbone reduced to 1,536 hidden size and ~650M parameters, 8,192-token context, 9 days on 8 H100s. Pretraining corpus: 820,944 files after work-level deduplication and heuristic quality filters. Generative finetuning: one epoch on cleaner data with an end-control token. Contrastive stage: two non-overlapping 100–650-note slices, independent augmentation, EOS-token embedding projected to 512 dimensions, NT-Xent (τ = 0.1), 25 epochs, lr 1e-5. Probes are linear classifiers on averaged slice embeddings; supervised finetuning replaces the LM head with a classification head.

## Results

| Claim | Measurement | Anchor |
|---|---|---|
| Beats AMT on coherence | 38 wins / 0 ties / 6 losses | Table 1, p. 3 |
| Beats MusicGen | 49 / 1 / 0 | Table 1, p. 3 |
| Ties Suno 3.5 | 18 / 9 / 21, p = 0.75 | Table 1, p. 3 |
| Ties human continuations | 15 / 9 / 17, p = 0.86 | Table 1, p. 3 |
| Composer probe | 90.5% (AriaEmb) vs 84.5% (CLaMP 3) | Table 2, p. 4 |
| Pianist8 probe | 91.6% vs 81.9% (M3) | Table 2, p. 4 |
| Contrastive from scratch | 65.5% composer vs 90.5% | Table 2, p. 4 |

The listening test covers 45-second continuations of five 15-second prompts, not full pieces. Probe benchmarks are piano-only, while the baselines are general models; the authors state this asymmetry. Few-shot results use 100–1,000 labelled files and are strongest for composer and genre.

## Related Papers

- [[overviews/audio-symbolic-transfer]] — the central evidence that transcribed audio can substitute for scarce symbolic data at piano scale.
- [[concepts/transcription-as-supervision]] — the corpus is a learned label function; this paper measures its downstream benefit but not its error structure.
- [[data-and-representation/bradshaw-2025-aria-midi-a-dataset-of]] — the corpus and transcription pipeline.
- [[data-and-representation/huang-2025-musetok-symbolic-music-tokenization-for]] — a different symbolic representation with contrastive/understanding probes.
- [[generation-and-planning/wang-2025-notagen-advancing-musicality-in-symbolic]] — symbolic generation at scale from score text, with a different evaluation philosophy.
- [[generation-and-planning/guo-2025-moonbeam-a-midi-foundation-model]] — MIDI foundation model with relative-attention inductive bias.
- [[retrieval-and-recombination/wu-2025-clamp-3-universal-music]] — the cross-modal retrieval baseline that Aria's probes outperform on piano.
