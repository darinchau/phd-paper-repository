---
title: "Reimagining Dance: Real-time Music Co-creation between Dancers and AI"
authors: "Olga Vechtomova and Jeff Bos"
year: 2025
doi: 10.48550/arXiv.2506.12008
category: interaction-and-evaluation
source: vechtomova-2025-reimagining-dance-real-time-music.md
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/vechtomova-2025-reimagining-dance-real-time-music.pdf"
pdf_filename: vechtomova-2025-reimagining-dance-real-time-music.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
tags: []
---
## Summary

I reviewed all five PDF pages, the extracted text, Figures 1–3, and the linked supplementary plots referenced in the paper’s footnote.

## Key Contributions

Core contribution

#### Author claim

The authors invert the usual dance–music relationship. Instead of music driving choreography, the dancer’s movement conditions the next musical clip. The dancer is therefore both performer and musical co-creator.

The system does not synthesize waveform audio directly. It predicts an audio latent representation and retrieves an existing clip from a library, producing a real-time collage through cross-fading.

#### Interpretation

This is best understood as **stateful, retrieval-based mixed-initiative co-creation**, not autonomous music generation. The AI contributes selection and sequencing; the dancer contributes embodied control; the original recordings provide the musical material.

---

### Architecture and interaction loop

**Figure 1, p. 1; “System Architecture,” p. 2; “Real-time Inference,” p. 3**

1. **Movement capture**
   - Webcam input.
   - TensorFlow **MoveNet Thunder** extracts five landmarks:
     - head
     - left wrist
     - right wrist
     - left ankle
     - right ankle

2. **Movement encoding**
   - Each 3.5-second motion sequence becomes a color-coded trajectory image.
   - Input size: **256 × 256 × 3**.
   - A movement VAE maps it to a **128-dimensional latent vector**.

3. **Audio encoding**
   - Audio is represented as spectrograms of 3.5-second clips.
   - Audio VAE input: **224 × 224 × 1**.
   - Five convolutional encoder layers with ReLU; decoder uses transposed convolutions.
   - Audio latent dimension: **128**.

4. **Cross-modal generation**
   - Inputs:
     - current movement latent
     - previous audio c

The complete evidence-grounded digest is in [`sources/vechtomova-2025-reimagining-dance-real-time-music.md`](../../sources/vechtomova-2025-reimagining-dance-real-time-music.md).

## Methodology and Architecture

Read the linked source digest for the paper's full method, equations, implementation details, and page/section anchors.

## Results

The linked source digest preserves the paper-reported results and their evidence boundaries; this page does not claim an independent reproduction.

## Related Papers

- [[overviews/2026-symbolic-music-literature-map]] — primary synthesis anchor for this batch; the overview places this paper beside related representation, generation, evaluation, and auditability work.
