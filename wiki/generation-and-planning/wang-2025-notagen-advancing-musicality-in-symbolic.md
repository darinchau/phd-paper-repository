---
title: "NotaGen: Advancing Musicality in Symbolic Music Generation with Large Language Model Training Paradigms"
authors: Yashan Wang, Shangda Wu, Jianhuai Hu, Xingjian Du, Yueqi Peng, Yongxin Huang, Shuai Fan, Xiaobing Li, Feng Yu, and Maosong Sun
year: 2025
doi: 10.48550/arXiv.2502.18008
source: wang-2025-notagen-advancing-musicality-in-symbolic.md
category: generation-and-planning
pdf_path: "C:/Users/User/Documents/Repository/phd-research/phd-paper-repository/papers/wang-2025-notagen-advancing-musicality-in-symbolic.pdf"
pdf_filename: wang-2025-notagen-advancing-musicality-in-symbolic.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-09-02
tags:
  - symbolic-music-generation
  - sheet-music-generation
  - classical-music
  - abc-notation
  - hierarchical-transformers
  - pretraining
  - direct-preference-optimization
  - ai-feedback
  - controllable-generation
  - human-evaluation
---

## Summary

NotaGen is a 516M-parameter classical sheet-music generator trained through an LLM-style sequence: pre-training on 1.6M internally curated ABC sheets, supervised fine-tuning on 8,948 classical sheets, and three rounds of AI-feedback preference optimization. Its interleaved ABC representation places simultaneous voices together, adds current/remaining-bar labels, and feeds fixed character patches through a patch-level decoder and then a character-level decoder. [PDF pp. 1–5]

CLaMP-DPO compares every generated piece with the mean CLaMP 2 embedding of authentic pieces sharing its `period-composer-instrumentation` prompt. The top 10% become chosen examples and the bottom 10% rejected examples for DPO-Positive. This increases CLaMP similarity, generally improves coarse prompt-label accuracy, and shifts reported A/B votes toward post-training outputs across NotaGen, MuPT, and MET. [PDF pp. 4–7]

The evidence is narrower than the abstract's wording. Human ground truth still wins all three model-reference comparisons; NotaGen receives 41.7% versus ground truth's 50.0%. No p-values, intervals, effect sizes, or complete stimulus/participant structure are reported, so “significantly outperforms” is not established in the statistical sense. CLaMP 2 is also both the training evaluator and the source of the main objective metric. [PDF pp. 6–7]

For transparent AI, NotaGen is procedurally traceable but not musically explanatory. A reviewer could reconstruct prompts, references, scalar scores, chosen/rejected quantiles, and policy iterations. The latent cosine score does not disclose chord function, voice-leading, cadence, formal role, notation rule, or the causal reason for changing a note.

## Key Contributions

1. **End-to-end LLM training recipe.** The same symbolic model receives broad pre-training, prompt-conditioned classical fine-tuning, and iterative preference optimization. [PDF pp. 1–5]
2. **Long-form sheet representation.** Interleaved ABC aligns voices within bars; full-rest-bar removal shortens sequences to 80.7% on average; `[r:]` labels provide current/countdown bar position; stream continuation extends beyond one context. [PDF pp. 2–3]
3. **Hierarchical generation.** A 20-layer patch decoder models bar-stream patches, and a six-layer character decoder realizes the next patch. The model has hidden size 1,280, context 1,024, and 516M parameters. [PDF pp. 3, 5]
4. **CLaMP-DPO.** A learned music embedding supplies prompt-conditioned chosen/rejected pairs without collecting new human preference annotations. DPO-Positive stabilizes chosen-output likelihood, and the entire loop is regenerated over three iterations. [PDF pp. 4–6]
5. **Cross-model test.** The recipe is applied to NotaGen, BPE-based ABC model MuPT, and MIDI Event Transformer; all three gain objective CLaMP score and more post-training than pre-training votes. [PDF pp. 5–7]
6. **Classical-music human evaluation.** Ninety-two music-college participants judge videos using criteria that include melody, harmony, counterpoint, orchestral balance, structure, and notation quality. The resulting single A/B choice does not separate these criteria. [PDF pp. 6–7]

![Training sequence](assets/wang-2025-notagen-advancing-musicality-in-symbolic/fig-1-training-paradigms.png)

*Figure 1, PDF p. 1. The final stage uses a reference-conditioned learned evaluator, not an explicit theory-rule reward.*

## Methodology and Architecture

### Representation and continuation

The tune header carries meter, tempo, key, score layout, instrumentation, and a `period-composer-instrumentation` prompt. In the body, `[V:]` distinguishes voices interleaved on one bar line, and `[r:current/countdown]` supplies location and remaining length. Training attaches random body segments to the header. Inference starts at bar one; when the context fills, the header and latter half of the existing body seed the next segment. [PDF pp. 2–3]

![Representation and architecture](assets/wang-2025-notagen-advancing-musicality-in-symbolic/fig-2-representation-and-architecture.png)

*Figure 2, PDF p. 3. The representation preserves simultaneous voices locally, while the architecture separates longer patch dependencies from character realization.*

### Data and supervised training

Pre-training uses 1.6M internal-use ABC sheets augmented across 15 keys. AdamW training uses learning rate `1e-4`, 1,000 warm-up steps, eight H800 GPUs, and batch size four per GPU. Epochs, total updates, duration, provenance, licensing, duplicates, and data splits are not reported. [PDF pp. 3, 5]

Fine-tuning uses 8,948 sheets: DCML 560, OpenScore String Quartet 342, OpenScore Lieder 1,334, ATEPP 55, KernScores 221, and internal sources 6,436. Internal material is therefore about 71.9% of the corpus. Works have at most 16 staves and cover three periods, 152 composers, and six instrumentation groups. [PDF pp. 3–4]

### Learned-evaluator preference optimization

For prompt `p`, CLaMP 2 embeds each generated piece `x_p` as `z_{x_p}` and averages the prompt's authentic reference embeddings as `\bar z_p`. The score is cosine similarity:

\[
c_{x_p}=\frac{z_{x_p}\cdot\bar z_p}
{\lVert z_{x_p}\rVert\lVert\bar z_p\rVert}.
\]

Eligible prompts occur more than ten times: 112 prompts covering 86.4% of the sheet data for NotaGen/MuPT and 29 covering 90.5% of MET's 3,104-piece keyboard MIDI subset. Each iteration generates about 100 pieces per prompt, selects the top/bottom 10%, and runs 10,000 DPOP steps. Settings are three iterations, `β = 0.1`, `λ = 10`, learning rate `1e-6` for NotaGen/MET and `1e-7` for MuPT. [PDF pp. 4–6]

The paper says syntax and plagiarism filters *can* be applied, but the experiment explicitly confirms only exclusion of chosen sheets whose same-instrument staves are not grouped. [PDF pp. 4, 6]

### Auditability boundary

The training loop can log source references, scores, quantile membership, preference pairs, and policy versions. However, CLaMP 2's feature dimensions are not translated into musical concepts, and the paper performs no counterfactual faithfulness test. Optimization toward a prompt's average latent reference can also trade diversity for centroid similarity; diversity and memorization are not measured.

## Results

### Objective metrics

![Objective results](assets/wang-2025-notagen-advancing-musicality-in-symbolic/table-2-objective-results.png)

*Table 2, PDF p. 6. ACS is the same learned score used to select the DPOP preference pairs.*

- **NotaGen:** ACS `0.570 → 0.730`; period accuracy `84.7% → 93.0%`; instrumentation accuracy `78.5% → 94.6%`; BAE `0.269% → 0.176%`; PPL `1.2151 → 1.2880`.
- **MuPT:** ACS `0.515 → 0.674`; period accuracy `76.3% → 82.1%`; instrumentation accuracy `78.6% → 87.6%`; BAE worsens `0.824% → 4.676%`; PPL rises `1.4159 → 1.6121`.
- **MET:** ACS `0.565 → 0.655`; period accuracy `30.0% → 38.2%`; PPL remains near-flat `1.2251 → 1.2290`.

ACS increases monotonically, but some secondary measures peak earlier: NotaGen period accuracy is 93.3% at iteration two, MuPT instrumentation is 89.2% at iteration two, and NotaGen BAE is lowest at 0.158% at iteration two. MuPT's sharply worsening BAE shows that a preference proxy can improve while symbolic validity degrades. [PDF pp. 6–7]

### Human A/B votes

![Before and after CLaMP-DPO](assets/wang-2025-notagen-advancing-musicality-in-symbolic/fig-3-before-after-clamp-dpo.png)

*Figure 3, PDF p. 6. Post-training wins descriptively for all models; the plot contains no uncertainty or significance markers.*

- NotaGen: 43.5% before, 2.2% no preference, 54.3% after.
- MuPT: 31.7% before, 14.6% no preference, 53.7% after.
- MET: 30.0% before, 20.0% no preference, 50.0% after.

Against human-authored references, NotaGen obtains 41.7% model / 8.3% no preference / 50.0% ground truth. MuPT obtains 26.8% / 4.9% / 68.3%; MET obtains 23.8% / 9.5% / 66.7%. NotaGen is the strongest model in these separate comparisons, but no model beats human ground truth. The references are drawn from the fine-tuning dataset rather than identified as an unseen work-disjoint test set. [PDF p. 7]

The study has 92 music-college participants and at least 35 valid responses per test group, but it omits unique item counts, response counts, pairing structure, randomization, blinding, inter-rater reliability, intervals, effects, power, and inferential tests. The results support observed preference shifts, not a confirmed population-level “significant” advantage. [PDF pp. 6–7]

### Main limitations

- CLaMP 2 Score assumes already reasonable, syntactically valid music and can misjudge corrupted output. [PDF p. 7]
- Large-ensemble orchestral generation still lags solo piano and string quartet. [PDF p. 7]
- The training and evaluation signals do not measure explicit harmony, voice leading, cadence, form, playability, or explanation utility.
- BAE covers duration alignment only; it is not a general score-validity measure.
- The mostly internal corpora and missing work-level splits prevent a provenance, leakage, or memorization audit.
- The human-reference comparison reuses pieces from the fine-tuning corpus, so it does not establish held-out composition generalization.
- Baselines differ in modality, architecture, tokenization, pre-training data, context, and fine-tuning subset, so the comparison cannot isolate NotaGen's representation as the cause.

## Related Papers

- [[generation-and-planning/guo-2025-moonbeam-a-midi-foundation-model]] — provides the complementary expressive-MIDI foundation-model case: Moonbeam builds relative musical structure into representation and attention, while NotaGen adds classical fine-tuning and learned-evaluator post-training to an ABC generator.
- [[overviews/symbolic-music-foundation-models]] — places NotaGen's pretrain–fine-tune–CLaMP-DPO pipeline beside Moonbeam's pretrain–adapt architecture without treating their corpora, token counts, controls, or evaluations as directly comparable.
- [[concepts/music-domain-inductive-biases]] — treats interleaved voices, bar-stream patches, countdown labels, and prompt-conditioned reference scoring as inspectable design choices while preserving the absence of component-wise causal validation.
- [[concepts/hierarchical-latent-reasoning]] — distinguishes NotaGen's patch/character representation hierarchy from HRM's iterative slow/fast latent-computation hierarchy and identifies what a genuinely theory-grounded planning interface would still require.
