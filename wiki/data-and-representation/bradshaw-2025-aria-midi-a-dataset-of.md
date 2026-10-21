---
title: "Aria-MIDI: A Dataset of Piano MIDI Files for Symbolic Music Modeling"
authors: "Louis Bradshaw and Simon Colton"
year: 2025
doi: 10.48550/arXiv.2504.15071
source: bradshaw-2025-aria-midi-a-dataset-of.md
category: data-and-representation
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/bradshaw-2025-aria-midi-a-dataset-of.pdf"
pdf_filename: bradshaw-2025-aria-midi-a-dataset-of.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-21
tags: [dataset, piano, automatic-music-transcription, youtube, metadata, deduplication, aria]
---

# Aria-MIDI: A Dataset of Piano MIDI Files for Symbolic Music Modeling

## Summary

Aria-MIDI is the largest public solo-piano symbolic corpus: 1,186,253 transcriptions (about 100,000 hours), reduced to 800,973 files (66,650 hours) after compositional deduplication. It is built from YouTube audio, not from scores: an LLM crawls and scores candidate videos, a distilled source-separation classifier prunes and segments them, Aria-AMT transcribes them, and an LLM attaches composer/work metadata. The paper's contribution is the pipeline and its validation, not a new transcription model. Its evidence supports "audio can supply symbolic data at scale for piano"; it does not establish transcription fidelity, multi-instrument coverage, or downstream musical quality.

## Key Contributions

- A language-model-guided crawl that reaches diverse piano recordings without a fixed repertoire list; Llama 3.1 70B reaches 81.9 F1 at the chosen threshold, close to human labels (83.2–85.3) and better than the 8B model.
- A distilled classifier that turns expensive source separation into cheap five-second classification and segmentation; the full pipeline removes 98.83% of non-piano audio while retaining 94.22% of piano audio in the segmentation evaluation.
- A corpus roughly two orders of magnitude larger than MAESTRO/ATEPP/GiantMIDI in hours, with per-file composer (71% present, 99.3% accurate), performer, genre, and period tags.
- A documented deduplication rule (composer–opus–piece triples, plus removal of unlabelled works by prolific composers) that yields a compositionally cleaner subset.

## Methodology and Architecture

The pipeline has four stages. (1) Crawl: seed videos plus YouTube related-video expansion, prioritised by an LLM score of solo-piano likelihood from title/description. (2) Audio curation: MVSep splits each track into piano and "other"; energy rules on the separated stems produce pseudo-labels; a five-layer mel-spectrogram CNN is trained on 2,405 hours; inference uses overlapping five-second windows, an "all windows below 0.5 for at least three seconds" rule for non-piano regions, and a 45-second minimum for retained segments. (3) Transcription: Aria-AMT at 10 ms resolution, 131× real time. (4) Metadata: Llama 3.1 70B extracts composer, opus, piece, performer, key, genre, and period; these tags drive entity resolution and deduplication. The dataset is released as MIDI plus labels under CC-BY-NC-SA; audio is not released.

## Results

| Quantity | Value | Anchor |
|---|---:|---|
| Files before / after dedup | 1,186,253 / 800,973 | Table 1, p. 2 |
| Hours before / after dedup | 100,629 / 66,650 | Table 1, p. 2 |
| Videos crawled / classifier-processed | 3,290,453 / 1,713,650 | §4, p. 9 |
| Segmentation F1 (τ=0.5) | 73.86 | Table 4, p. 7 |
| Piano / non-piano overlap | 94.22% / 98.83% | Table 4, p. 7 |
| Per-file precision / recall (T=0.7, any piano) | 100% / 89.86% | Table 5, p. 8 |
| Composer present / accurate | 71.0% / 99.3% | Table 6, p. 9 |

The evaluation sample is 250 human-labelled videos, so the confidence intervals around these rates are wide and are not reported. Transcription accuracy is not measured in this paper. There is no experiment in which a model trained on Aria-MIDI is compared with the same model trained on human-authored MIDI, so the dataset's downstream value is asserted rather than demonstrated here; the companion scaling paper supplies that evidence.

## Related Papers

- [[overviews/audio-symbolic-transfer]] — places Aria-MIDI as the hard-transcription route from audio to symbolic data, and the corpus behind Aria's scaling result.
- [[concepts/transcription-as-supervision]] — the general mechanism: a transcription model defines the effective label function and its errors become the training distribution.
- [[data-and-representation/bradshaw-2025-scaling-self-supervised-representation]] — pretrains a 650M symbolic model and contrastive embeddings on this corpus.
- [[data-and-representation/hawthorne-2019-enabling-factorized-piano-music-modeling]] — the aligned-audio/MIDI quality reference that Aria-MIDI trades fidelity for scale.
- [[data-and-representation/chang-2024-yourmt3-multi-instrument-music-transcription]] — the multi-instrument transcription route that Aria-MIDI does not cover.
- [[generation-and-planning/chen-2024-sympac-scalable-symbolic-music]] — a multi-track corpus built the same way from in-house audio, with beat and structure labels added.
