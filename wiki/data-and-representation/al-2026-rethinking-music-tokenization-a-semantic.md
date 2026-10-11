---
title: "Rethinking Music Tokenization: A Semantic Codec toward High-Fidelity LLM Music Generation"
authors: "Huakang Chen et al."
year: 2026
doi: 10.48550/arXiv.2609.21240
category: data-and-representation
source: al-2026-rethinking-music-tokenization-a-semantic.md
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/al-2026-rethinking-music-tokenization-a-semantic.pdf"
pdf_filename: al-2026-rethinking-music-tokenization-a-semantic.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
tags: []
---
## Summary

MuSeC separates a frozen music-SSL semantic stream from residual acoustic RVQ tokens to improve reconstruction, content probes, and LM predictability. Its learned audio tokens are not symbolic notes or provenance explanations, so an explicit event layer remains necessary for mashups and repair.

## Key Contributions

Core contribution

The paper introduces **MuSeC**, a music codec intended to improve the trade-off between:

1. waveform reconstruction fidelity;
2. semantic/content preservation; and
3. autoregressive language-model predictability.

The authors argue that ordinary reconstruction codecs encode fine acoustic detail into high-entropy tokens, while speech-derived semantic codecs impose an inadequate notion of semantics on music. MuSeC instead factorizes a mixed music signal into:

- a **semantic stream**, derived from intermediate layers of a music SSL model; and
- an **acoustic stream**, learned with residual vector quantization to recover information missing from the semantic stream.

**Author claim:** The factorization improves reconstruction and token predictability without source separation (pp. 1–2, Sec. I–II).  
**Interpretation:** MuSeC is a learned audio-latent decomposition, not an interpretable symbolic representation. Its “semantic” tokens are still frame-level cluster IDs rather than notes, chords, voices, phrases, or source-labelled musical events.

---

### 2. Definition of music semantics

#### Layer-wise probing

The authors evaluate frozen SSL representations from:

- MERT;
- MuQ;
- LeVo BEST-RQ MuEncoder; and
- WavLM as a speech-SSL reference.

They probe MARBLE/MIR tasks:

- MTT music tagging;
- GTZAN genre;
- EMO/R2A emotion;
- GS key detection;
- GTZAN beat tracking;
- GuitarSet chord estimation; and
- lyrics transcription.

They omit performance-level and acoustic-level MARBLE tasks because their goal is music generation tokenization rather than general mu

The complete evidence-grounded digest is in [`sources/al-2026-rethinking-music-tokenization-a-semantic.md`](../../sources/al-2026-rethinking-music-tokenization-a-semantic.md).

## Methodology and Architecture

Read the linked source digest for the paper's full method, equations, implementation details, and page/section anchors.

## Results

The linked source digest preserves the paper-reported results and their evidence boundaries; this page does not claim an independent reproduction.

## Related Papers

- [[overviews/2026-symbolic-music-literature-map]] — primary synthesis anchor for this batch; the overview places this paper beside related representation, generation, evaluation, and auditability work.
