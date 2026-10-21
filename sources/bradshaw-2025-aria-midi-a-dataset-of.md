---
title: "Aria-MIDI: A Dataset of Piano MIDI Files for Symbolic Music Modeling"
authors: "Louis Bradshaw and Simon Colton"
year: 2025
doi: 10.48550/arXiv.2504.15071
category: data-and-representation
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/bradshaw-2025-aria-midi-a-dataset-of.pdf"
pdf_filename: bradshaw-2025-aria-midi-a-dataset-of.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-21
---

# Aria-MIDI: A Dataset of Piano MIDI Files for Symbolic Music Modeling

## One-line Summary

Aria-MIDI builds 1,186,253 solo-piano MIDI files (about 100,000 hours) by crawling YouTube with a language model, filtering and segmenting audio with a distilled source-separation classifier, transcribing with Aria-AMT, and attaching LLM-extracted composer/work metadata; compositional deduplication leaves 800,973 files.

## 1. Document Information

- **Authors and affiliation:** Louis Bradshaw and Simon Colton, Queen Mary University of London.
- **Venue and version:** ICLR 2025 conference paper; arXiv 2504.15071v1, 21 April 2025. 17 PDF pages: main paper pp. 1–10, references pp. 11–14, appendices pp. 15–17.
- **Extraction:** `pdftotext -layout` over the full PDF; main text, Tables 1–6, and Figures 1–5 inspected. The appendices (LLM prompts) were skimmed for the metadata schema, not reproduced.
- **Artifact:** dataset and piano classifier advertised at `https://github.com/loubbrad/aria-midi` and `https://github.com/loubbrad/aria-cl`; licence CC-BY-NC-SA; audio and raw metadata are not released.
- **Anchors:** dataset scale Table 1 p. 2; pipeline §2.1–2.4 pp. 3–6; validation Tables 3–6 pp. 7–9; deduplication and statistics §4 pp. 9–10.

## 2. Key Contributions

1. **A scalable crawl-and-score pipeline.** Llama 3.1 70B scores YouTube titles/descriptions for solo-piano likelihood; the YouTube related-video endpoint supplies new candidates. The 70B model reaches F1 81.9 at score threshold 4 against human labels, versus 77.3 for 8B and 85.1 for 405B (Table 3, p. 7).
2. **A distilled piano/non-piano classifier and segmenter.** MVSep piano source separation pseudo-labels unlabelled audio; the distilled CNN classifies five-second clips and segments long recordings. The authors report an 8-fold absolute reduction in non-piano audio misclassified as piano relative to the ablation, and 98.83% removal of non-piano audio at threshold 0.5 (Table 4, p. 7).
3. **A large transcribed corpus with metadata.** 3,290,453 videos crawled, 1,713,650 processed by the classifier, >1M segments transcribed. Files carry composer, performer, opus, piece, key, genre, and period tags with reported presence/accuracy (Table 6, p. 9).
4. **Compositional deduplication.** Removing duplicate composer–opus–piece triples, and all unlabelled works by prolific composers, reduces the corpus to 800,973 files / 66,650 hours (p. 10).

## 3. Methodology and Architecture

- **Crawl (§2.1).** Fifty manually chosen seed videos; for each unscored video an LLM assigns a 1–5 solo-piano score from title and description; high-scoring videos seed the next related-video expansion. Classical repertoire dominates early, then diversifies.
- **Audio classification (§2.2).** MVSep separates piano from "other". For each five-second clip, per-frame RMS energy is computed on both stems. A clip is non-piano if the "other" stem has a contiguous region longer than `l_min` above `dB_min`, or if the piano stem is silent for more than four seconds. A five-layer CNN over 256-bin mel spectrograms is trained on 2,405 hours of mixed real, pseudo-labelled, and synthetic audio (Table 2, p. 5), with noise, pitch-shift, and band-pass augmentation.
- **Segmentation (§2.2.2).** Five-second windows with a one-second stride; a region is non-piano when all windows in it score below 0.5 and the region exceeds three seconds; retained piano segments must exceed 45 seconds and average score 0.7.
- **Transcription (§2.3).** Aria-AMT, a Whisper-style piano transcription model, at 10 ms resolution. 100,629 hours took 765 H100-hours, about 131× real time and 2,327 notes/s.
- **Metadata (§2.4).** Llama 3.1 70B extracts entities from titles/descriptions; entity resolution is used to control over-representation (e.g., 6,819 "Moonlight" titles).

## 4. Key Results and Benchmarks

- **Scale (Table 1, p. 2).** 1,186,253 files / 100,629 hours before deduplication; 800,973 files / 66,650 hours after. This is roughly two orders of magnitude more hours than MAESTRO (199 h), ATEPP (1,009 h), or GiantMIDI (1,237 h), and about 10× Lakh's hours, but solo piano only.
- **Classifier quality (Tables 4–5, pp. 7–8).** Segmentation F1 73.86 at threshold 0.5, with 94.22% piano and 98.83% non-piano overlap. Per-file classification at T=0.7 reaches 100% precision / 89.86% recall for any solo piano and 90.98% / 95.28% for high-quality solo piano, with 0 false positives on the 250-file human-labelled sample.
- **Metadata quality (Table 6, p. 9).** Composer present in 71.0% of files with 99.3% accuracy; performer 62.0%/99.2%; opus 32.0%/100%; genre 86.5%/94.2%; period 63.0%/92.9%. Missing-label rates are low except period (12.5%).
- **What the validation does not measure.** Transcription note accuracy is not re-measured here; the paper delegates it to Aria-AMT. No listening test, no downstream model ablation, and no comparison of models trained on Aria-MIDI versus human MIDI is reported.

## 5. Limitations and Future Work

- **Piano only, and overwhelmingly classical.** The corpus cannot support multi-instrument or band-music modelling without a different transcription stack. The authors name guitar and multi-instrument extension as future work.
- **Transcription is the ceiling.** Every downstream claim inherits Aria-AMT's errors: missed notes, octave errors, smeared timing, pedal/velocity approximations. The paper does not estimate how those errors propagate into generation or representation learning.
- **Metadata is inferred, not authoritative.** Presence is incomplete (only 32% opus, 22% piece number), and deduplication can only work on the tags that exist.
- **Legal and distribution constraints.** Only MIDI and derived labels are released, under CC-BY-NC-SA; audio and raw metadata are withheld.
- **Quality is a classifier score, not a musical judgement.** A high classifier score means "sounds like clean solo piano", not "correctly transcribed".

## 6. Related Work

- GiantMIDI-Piano, ATEPP, and PiJAMA: earlier piano transcription corpora built with Kong et al.'s high-resolution transcription model and human-in-the-loop pruning (pp. 2–3).
- MAESTRO: aligned Disklavier audio/MIDI, the quality reference but two orders of magnitude smaller.
- Lakh MIDI: large but web-scraped, heterogeneous, and not performance-derived.
- Aria-AMT and Aria: the transcription model and the downstream scaling study that use this corpus.
- MT3 / YourMT3+: the multi-instrument transcription route the paper does not take.

## 7. Glossary

- **AMT:** Automatic Music Transcription.
- **MIDI:** Musical Instrument Digital Interface; here a note-event representation.
- **MVSep:** a music source-separation service/model used to isolate piano.
- **Pseudo-labelling:** training labels produced by a model rather than a human.
- **Entity resolution:** mapping different surface strings to one composer/work identity.
- **dBFS:** decibels relative to full scale.
- **CC-BY-NC-SA:** Creative Commons Attribution–NonCommercial–ShareAlike licence.
