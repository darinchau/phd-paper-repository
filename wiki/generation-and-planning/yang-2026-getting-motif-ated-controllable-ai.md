---
title: "Getting Motif-ated: Controllable AI Compositions from Injected Motif Prompts"
authors: "Chao Peter Yang, Cynthia Rudin, Yue Jiang, Simon Mak, and Stephen Ni-Hahn"
year: 2026
doi: 10.48550/arXiv.2609.32788
category: generation-and-planning
source: yang-2026-getting-motif-ated-controllable-ai.md
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/yang-2026-getting-motif-ated-controllable-ai.pdf"
pdf_filename: yang-2026-getting-motif-ated-controllable-ai.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
tags: []
---
## Summary

“**Getting Motif-ated: Controllable AI Compositions from Injected Motif Prompts**.” arXiv:**2609.32788v1**, `[cs.LG]`, 26 September 2026. Listed as a NeurIPS 2026 Creative AI Track paper. The PDF contains 18 pages: main paper pp. 1–6, references pp. 7–8, appendices pp. 8–11, and the NeurIPS checklist pp. 11–18.

## Key Contributions

Core contribution

**Author claim — Abstract, pp. 1–2; Conclusion, p. 6:**  
MotiGen retrofits motif control onto a pretrained symbolic music language model by combining:

1. A structured `%motif:` ABC prompt line.
2. A scalar attention bias toward motif-prompt tokens.
3. Two-phase curriculum training:
   - motif-centered crops;
   - full annotated scores.
4. A shared motif extractor/evaluator.

The reported full system contains the prompted motif in **92.3%** of generated pieces.

**Interpretation:** This is primarily a controllability and motif-grounding paper, not a source-preserving recomposition or provenance paper. The motif is abstract and transformed, rather than an exact source excerpt.

---

### 2. Pretrained base model and data

#### Base model

**Section 3.4, p. 4; Appendix A, pp. 8–9**

MotiGen fine-tunes the public **NotaGen-large** checkpoint:

- NotaGen pretraining: approximately **1.6M ABC-notation pieces**.
- NotaGen author fine-tuning: approximately **9k classical scores** with period/composer/instrumentation prompts.
- Architecture:
  - 20-layer patch-level encoder;
  - 6-layer character-level decoder;
  - hidden size 1280;
  - patch length 1024;
  - patch size 16;
  - patch-streaming regime.
- Fine-tuning:
  - AdamW;
  - learning rate `10^-5`;
  - batch size 1;
  - early stopping for up to 10 epochs on held-out loss.

#### MotiGen training data

**Section 3.4, p. 4; Appendix B, p. 9; Appendix D, p. 11**

- OpenScore Lieder: approximately **1.3k Romantic-era songs**, using the `V:1` vocal line.
- Irishman corpus: **216k+ monophonic folk tunes**.
- All piece

The complete evidence-grounded digest is in [`sources/yang-2026-getting-motif-ated-controllable-ai.md`](../../sources/yang-2026-getting-motif-ated-controllable-ai.md).

## Methodology and Architecture

Read the linked source digest for the paper's full method, equations, implementation details, and page/section anchors.

## Results

The linked source digest preserves the paper-reported results and their evidence boundaries; this page does not claim an independent reproduction.

## Related Papers

- [[overviews/2026-symbolic-music-literature-map]] — primary synthesis anchor for this batch; the overview places this paper beside related representation, generation, evaluation, and auditability work.
