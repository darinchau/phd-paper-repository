---
title: "From Words to Music: A Study of Subword Tokenization Techniques in Symbolic Music Generation"
authors: "Adarsh Kumar and Pedro Sarmento"
year: 2023
doi: 10.48550/arXiv.2304.08953
category: data-and-representation
source: kumar-2023-from-words-to-music-a.md
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/kumar-2023-from-words-to-music-a.pdf"
pdf_filename: kumar-2023-from-words-to-music-a.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
tags: []
---
## Summary

1. **Q1:** Can subword tokenization improve musical structure and quality in generated symbolic music? 2. **Q2:** Do improvements generalize between **BPE** and **Unigram** tokenization? — §1, pp. 1–2

## Key Contributions

central contribution is an empirical token-compression study, not a new generative architecture or a semantic music representation.

### 3. Tokenization schemes and baselines

#### Pipeline

The pipeline is:

1. MIDI/GuitarPro input;
2. musical event tokenizer;
3. mapping musical events to Unicode symbols/characters;
4. BPE or Unigram tokenizer;
5. Transformer sequence modeling;
6. detokenization back to musical events.  
   — Figure 2, p. 3; §3.2, p. 4

Each song is treated as one sentence-like sequence. Figure 1 illustrates repeated character n-grams versus repeated musical-event sequences.

#### Compared representations

| Musical tokenizer | Base vocabulary | BPE | Unigram |
|---|---:|---:|---:|
| REMI | 227 | 300 | 300 |
| MIDI-Like | 331 | 1,000 | 1,000 |
| DadaGP | 2,104 | 5,000 | 5,000 |

— Table 1, p. 4

The baseline is called **“base”** in the methodology and **“Original”** in Tables 2–3; Table 4 uses “Base.” It is the same no-subword condition.

- **BPE:** repeatedly merges frequent adjacent symbol pairs.
- **Unigram:** begins with a larger vocabulary and prunes tokens probabilistically according to likelihood/loss.
- Both are applied after musical event tokenization, not directly to raw MIDI bytes.  
  — §2.1, §3.2, pp. 2, 4

### 4. Datasets, splits, models, and training

| Dataset | Subset | Musical content | Musical tokenizer | Model |
|---|---:|---|---|---|
| Folk Songs | 1,000 samples | Monophonic, single instrument, MIDI | REMI | Music Transformer |
| MAESTRO | 400 samples | Polyphonic, single instrument, MIDI | MIDI-Like | Music Transformer |
| DadaGP | 2,000

The complete evidence-grounded digest is in [`sources/kumar-2023-from-words-to-music-a.md`](../../sources/kumar-2023-from-words-to-music-a.md).

## Methodology and Architecture

Read the linked source digest for the paper's full method, equations, implementation details, and page/section anchors.

## Results

The linked source digest preserves the paper-reported results and their evidence boundaries; this page does not claim an independent reproduction.

## Related Papers

- [[overviews/2026-symbolic-music-literature-map]] — primary synthesis anchor for this batch; the overview places this paper beside related representation, generation, evaluation, and auditability work.
