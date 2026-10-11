---
title: "MidiTok: A Python Package for MIDI File Tokenization"
authors: "Nathan Fradet, Jean-Pierre Briot, Fabien Chhel, Amal El Fallah Seghrouchni, and Nicolas Gutowski"
year: 2023
doi: 10.48550/arXiv.2310.17202
category: data-and-representation
source: fradet-2023-miditok-a-python-package-for.md
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/fradet-2023-miditok-a-python-package-for.pdf"
pdf_filename: fradet-2023-miditok-a-python-package-for.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
tags: []
---
## Summary

MidiTok is an open-source Python library that converts MIDI into token sequences suitable for Transformer-style symbolic-music models. Its central contribution is not a new model, dataset, or tokenization algorithm; it is a **unified, configurable implementation of many existing tokenization schemes**, plus preprocessing, BPE, augmentation, dataset utilities, and model-hub integration.

## Key Contributions

central contribution is not a new model, dataset, or tokenization algorithm; it is a **unified, configurable implementation of many existing tokenization schemes**, plus preprocessing, BPE, augmentation, dataset utilities, and model-hub integration.

The paper addresses a genuine reproducibility problem: many symbolic-music papers introduce token formats without releasing convenient implementations. MidiTok aims to make tokenization interchangeable and reproducible across generation, transcription, modeling, and MIR tasks (§1, p.1).

The paper reports that MidiTok had already been used in research and production-oriented tooling, including Qosmo’s Neutone DAW plugin (§6, p.7).

---

### 2. Package architecture and workflow

#### Configuration-driven design

A tokenizer is created from a `TokenizerConfig` containing:

- pitch range;
- beat/time resolution;
- number of velocity bins;
- enabled optional information such as tempo, rests, chords, programs, sustain pedal, pitch bend, and time signatures;
- special tokens;
- single-stream versus per-track operation.

The tokenizer derives its vocabulary from this configuration and can save/load the configuration as JSON (§3, p.3).

The implementation is organized around shared abstractions:

- `Event`: token type, value, time, and optional description;
- `TokSequence`: tokens, integer IDs, events, or BPE bytes;
- a common `MusicTokenizer` base class;
- tokenizer-specific subclasses for REMI, TSD, CPWord, MIDILike, MuMIDI, Octuple, MMM, Structured, and related schemes.

The v2-era source exposes these through `miditok/classes.py` and

The complete evidence-grounded digest is in [`sources/fradet-2023-miditok-a-python-package-for.md`](../../sources/fradet-2023-miditok-a-python-package-for.md).

## Methodology and Architecture

Read the linked source digest for the paper's full method, equations, implementation details, and page/section anchors.

## Results

The linked source digest preserves the paper-reported results and their evidence boundaries; this page does not claim an independent reproduction.

## Related Papers

- [[overviews/2026-symbolic-music-literature-map]] — primary synthesis anchor for this batch; the overview places this paper beside related representation, generation, evaluation, and auditability work.
