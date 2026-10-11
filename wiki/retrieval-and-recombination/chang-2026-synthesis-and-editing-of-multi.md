---
title: "Synthesis and Editing of Multi-Instrument Audio Mixtures Using Scalar-Quantised Latents with MIDI Span Conditioning"
authors: "Sungkyun Chang, Keshav Bhandari, Simon Dixon, and Emmanouil Benetos"
year: 2026
doi: 10.48550/arXiv.2609.25546
category: retrieval-and-recombination
source: chang-2026-synthesis-and-editing-of-multi.md
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/chang-2026-synthesis-and-editing-of-multi.pdf"
pdf_filename: chang-2026-synthesis-and-editing-of-multi.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
tags: []
---
## Summary

The authors introduce **SpanSynth-Edit**, a flow-matching model that synthesises or edits a selected region of a mono multi-instrument mixture from revised MIDI.

## Key Contributions

Core contribution

The authors introduce **SpanSynth-Edit**, a flow-matching model that synthesises or edits a selected region of a mono multi-instrument mixture from revised MIDI.

The central design is:

1. Encode observed audio into low-rate scalar-quantised latents.
2. Keep contextual audio latents fixed.
3. Represent MIDI notes as frame-aligned lifecycle events with continuous timing attributes.
4. Generate only the target region with a large diffusion transformer.
5. Decode the edited latent sequence back to audio.

The authors claim this supports adding, deleting, or changing notes while retaining surrounding audio and timbres. This is an author claim; the experiments measure preservation indirectly through audio similarity and transcription-derived metrics rather than source-level separation or attribution.  
**Anchor:** PDF pp. 1–2, Abstract, §1–§2.

---

### 2. Audio representation and SQ model

#### Frozen scalar-quantised codec

This is not a newly trained SQ-VAE in the paper. The model uses a **frozen HeartCodec encoder and decoder**:

- Input: 48-kHz mono audio.
- Latent dimension: 128 channels.
- Frame rate: 25 Hz.
- Hop: 40 ms.
- Encoder output bounded by `tanh`.
- Coordinate-wise quantisation:

\[
Q(x)=\operatorname{round}(9x)/9
\]

This produces **19 values in \([-1,1]\)**. The generated latent sequence is clipped and requantised before decoding:

\[
\hat y=D_{\mathrm{SQ}}\left(Q(\operatorname{clip}(Z,-1,1))\right).
\]

For a 20.48-second crop, the stored representation is **512 × 128 signed 8-bit SQ codes**, after discarding the codec’s first 50 latent fram

The complete evidence-grounded digest is in [`sources/chang-2026-synthesis-and-editing-of-multi.md`](../../sources/chang-2026-synthesis-and-editing-of-multi.md).

## Methodology and Architecture

Read the linked source digest for the paper's full method, equations, implementation details, and page/section anchors.

## Results

The linked source digest preserves the paper-reported results and their evidence boundaries; this page does not claim an independent reproduction.

## Related Papers

- [[overviews/2026-symbolic-music-literature-map]] — primary synthesis anchor for this batch; the overview places this paper beside related representation, generation, evaluation, and auditability work.
