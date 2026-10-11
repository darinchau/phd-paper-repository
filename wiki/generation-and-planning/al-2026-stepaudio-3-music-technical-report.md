---
title: "StepAudio 3 Music Technical Report"
authors: "Chengli Feng et al."
year: 2026
doi: 10.48550/arXiv.2609.16034
category: generation-and-planning
source: al-2026-stepaudio-3-music-technical-report.md
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/al-2026-stepaudio-3-music-technical-report.pdf"
pdf_filename: al-2026-stepaudio-3-music-technical-report.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
tags: []
---
## Summary

1. A discrete music tokenizer, 2. A Mixture-of-Experts autoregressive model, 3. An explicit ABC notation planning pass, 4. A continuous flow-matching DiT renderer.

## Key Contributions

Bottom line

**Author claim:** StepAudio 3 Music is a long-form, text- and reference-conditioned music generator combining:

1. A discrete music tokenizer,
2. A Mixture-of-Experts autoregressive model,
3. An explicit ABC notation planning pass,
4. A continuous flow-matching DiT renderer.

**Assessment:** The most research-relevant contribution is not the audio quality alone, but the **ABC-CoT intermediate arrangement plan and LLM-based plan editing**. This is a promising precedent for explainable musical control. However, the system remains primarily an audio-generation system: it does not demonstrate exact note-, chord-, bar-, source-provenance-, or repair-level guarantees. It is therefore highly relevant as an architectural inspiration for symbolic mashup/repair, but not a directly usable symbolic repair system.

---

### 1. System architecture

#### 1.1 Two-stage autoregressive generation

The paper defines lyrics, text prompts, and optional references as conditioning \(c\), an ABC arrangement plan as \(a\), and music tokens as \(m_{1:T}\).

The explicit-planning mode factorizes generation as:

\[
p(a,m_{1:T}\mid c)
=
p(a\mid c)
\prod_t p(m_t\mid m_{<t},a,c)
\]

Without explicit planning, the model directly predicts:

\[
\prod_t p(m_t\mid m_{<t},c)
\]

The ABC-CoT plan contains:

- Chords,
- Tempo,
- Time signature,
- Number of bars,
- Key,
- ABC melody notation.

The paper describes this plan as readable and editable before acoustic synthesis (Sections 2.2–2.3, pp. 2–4).

#### 1.2 Tokenizer and acoustic renderer

The final representation is:

- 50 tokens/second,
- One code

The complete evidence-grounded digest is in [`sources/al-2026-stepaudio-3-music-technical-report.md`](../../sources/al-2026-stepaudio-3-music-technical-report.md).

## Methodology and Architecture

Read the linked source digest for the paper's full method, equations, implementation details, and page/section anchors.

## Results

The linked source digest preserves the paper-reported results and their evidence boundaries; this page does not claim an independent reproduction.

## Related Papers

- [[overviews/2026-symbolic-music-literature-map]] — primary synthesis anchor for this batch; the overview places this paper beside related representation, generation, evaluation, and auditability work.
