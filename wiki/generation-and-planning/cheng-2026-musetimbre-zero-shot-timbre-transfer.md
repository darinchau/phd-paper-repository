---
title: "MuseTimbre: Zero-Shot Timbre Transfer by Controlling a Frozen Music Generator"
authors: "Yuan-Chiao Cheng and Zhiyao Duan"
year: 2026
doi: 10.48550/arXiv.2609.30548
category: generation-and-planning
source: cheng-2026-musetimbre-zero-shot-timbre-transfer.md
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/cheng-2026-musetimbre-zero-shot-timbre-transfer.pdf"
pdf_filename: cheng-2026-musetimbre-zero-shot-timbre-transfer.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
tags: []
---
## Summary

Code: `https://github.com/barry-mir/muse-timbre` Audio/demo: `https://barry-mir.github.io/muse-timbre-demo/`

## Key Contributions

Problem and claimed contribution

#### Author’s framing

Instrument timbre transfer re-voices a source performance with the timbre of a reference instrument while preserving its notes. The authors identify two problems:

1. **Pitch/timbre disentanglement:** The source recording contains both musical content and source-instrument timbre.
2. **Precise target-timbre specification:** A text label such as “violin” cannot capture the nuances of a particular recording.

MuseTimbre is claimed to be, “to our best knowledge,” the first system to transfer timbre from an audio reference to a polyphonic source by conditioning a pretrained music generator rather than training a dedicated generator from scratch (abstract, §1, p. 1).

#### Interpretation

The key design is not waveform-preserving editing. It is **regeneration from an explicit symbolic-like pitch representation plus an audio-derived timbre embedding**. This distinction matters for mashup and repair: source notes can be preserved or edited, but the original waveform’s timing, articulation, and performance detail are not directly retained.

---

### 3. Architecture

#### Frozen generator

MuseTimbre adds two control pathways to **Stable Audio 3 Medium**, described as a pretrained rectified-flow diffusion transformer:

- Frozen audio autoencoder/VAE
- Frozen DiT backbone
- Frozen original text-conditioning pathway
- Trainable pitch-conditioning pathway
- Trainable timbre-conditioning pathway

This is shown in **Figure 1, p. 2**, and described in §2.2.

#### Pitch pathway

The source clip is converted to a binary piano roll:

- **17

The complete evidence-grounded digest is in [`sources/cheng-2026-musetimbre-zero-shot-timbre-transfer.md`](../../sources/cheng-2026-musetimbre-zero-shot-timbre-transfer.md).

## Methodology and Architecture

Read the linked source digest for the paper's full method, equations, implementation details, and page/section anchors.

## Results

The linked source digest preserves the paper-reported results and their evidence boundaries; this page does not claim an independent reproduction.

## Related Papers

- [[overviews/2026-symbolic-music-literature-map]] — primary synthesis anchor for this batch; the overview places this paper beside related representation, generation, evaluation, and auditability work.
