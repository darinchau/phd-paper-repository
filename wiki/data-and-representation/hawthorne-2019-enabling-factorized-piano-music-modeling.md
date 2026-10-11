---
title: "Enabling Factorized Piano Music Modeling and Generation with the MAESTRO Dataset"
authors: "Curtis Hawthorne, Andriy Stasyuk, Adam Roberts, Ian Simon, Cheng-Zhi Anna Huang, Sander Dieleman, Erich Elsen, Jesse Engel, and Douglas Eck"
year: 2019
doi: 10.48550/arXiv.1810.12247
category: data-and-representation
source: hawthorne-2019-enabling-factorized-piano-music-modeling.md
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/hawthorne-2019-enabling-factorized-piano-music-modeling.pdf"
pdf_filename: hawthorne-2019-enabling-factorized-piano-music-modeling.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
tags: []
---
## Summary

\[ P(\text{audio}) = \mathbb{E}_{\text{notes}} \left[P(\text{audio}\mid\text{notes})\right] \tag{1} \]

## Key Contributions

Paper digest

### 1. Bibliographic identity

**Curtis Hawthorne, Andriy Stasyuk, Adam Roberts, Ian Simon, Cheng-Zhi Anna Huang, Sander Dieleman, Erich Elsen, Jesse Engel, and Douglas Eck.**  
**“Enabling Factorized Piano Music Modeling and Generation with the MAESTRO Dataset.”**  
arXiv:**1810.12247v5** [cs.SD], submitted **17 January 2019**; published as an **ICLR 2019 conference paper**.

- arXiv record: https://arxiv.org/abs/1810.12247v5
- Initial submission: 29 October 2018.
- v5 is the version represented by `/tmp/paper-digest/1810.12247v5.pdf`.
- Dataset results use **MAESTRO v1.0.0**.
- Dataset: CC BY-NC-SA 4.0.

I inspected all 12 PDF pages, including Figure 1, Figure 2, Tables 1–7, and the alignment appendix.

---

### 2. Direct answer: is MIDI an explicit latent space?

### Short answer

**MIDI is an explicit, discrete intermediate representation and can be called a discrete latent code in the paper’s probabilistic factorization. However, it is not a learned latent space in the usual VAE/embedding sense.**

The authors write:

\[
P(\text{audio}) =
\mathbb{E}_{\text{notes}}
\left[P(\text{audio}\mid\text{notes})\right]
\tag{1}
\]

**p. 2, §1, Equation (1).**

They explicitly say this “can be thought of as a generative model with a discrete latent code of musical notes.”

But the implementation is not a jointly trained latent-variable model:

| Common interpretation | Wave2Midi2Wave |
|---|---|
| Continuous latent vector \(z\) | Discrete note-event sequence |
| Encoder learns \(q(z\mid x)\) | Onsets and Frames transcribes audio into notes |
| Decoder reconstructs audio

The complete evidence-grounded digest is in [`sources/hawthorne-2019-enabling-factorized-piano-music-modeling.md`](../../sources/hawthorne-2019-enabling-factorized-piano-music-modeling.md).

## Methodology and Architecture

Read the linked source digest for the paper's full method, equations, implementation details, and page/section anchors.

## Results

The linked source digest preserves the paper-reported results and their evidence boundaries; this page does not claim an independent reproduction.

## Related Papers

- [[overviews/2026-symbolic-music-literature-map]] — primary synthesis anchor for this batch; the overview places this paper beside related representation, generation, evaluation, and auditability work.
