---
title: "Why Alzheimer's Speech Screening Fails to Generalize: Bridging the Deployment Gap via Cross-Corpus Evidence Anchoring"
authors: "Zijian Lu et al."
year: 2026
doi: 10.48550/arXiv.2609.31293
category: other
source: al-2026-why-alzheimer-s-speech-screening.md
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/al-2026-why-alzheimer-s-speech-screening.pdf"
pdf_filename: al-2026-why-alzheimer-s-speech-screening.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
tags: []
---
## Summary

“**Why Alzheimer’s Speech Screening Fails to Generalize: Bridging the Deploym1ent Gap via Cross-Corpus Evidence Anchoring**” [p. 1]. The embedded PDF metadata spells this as “Deployment.”

## Key Contributions

Executive summary

The paper studies whether Alzheimer’s speech-screening models generalize to unseen corpora, languages, tasks, and recording protocols. Its central finding is that:

1. Most interpretable speech markers are not directionally stable across datasets.
2. High-performing deep representations can fail catastrophically on one unseen corpus.
3. A compact, training-only-selected set of interpretable “evidence anchors” can improve worst-domain robustness when fused with an XLM-R model.
4. Mean performance and worst-domain performance require different fusion weights.

The strongest reported results are:

- XLM-R mean speaker AUC: **0.769**; worst corpus: **0.520** [§5, Table 2, p. 9].
- Balanced anchor/XLM-R fusion: **0.785 mean AUC** [§6.2, pp. 12–13].
- Anchor-heavy fusion: **0.615 worst-domain AUC**, versus **0.520** for XLM-R and **0.504** for GroupDRO [§6.2, pp. 12–13].
- However, the paired bootstrap interval for the weakest-domain improvement is **[−0.004, 0.195]**, so the improvement is not decisively significant at conventional levels [p. 13].

---

### 1. Problem and motivation

#### Author claims

The authors frame deployment as an **external-domain generalization** problem rather than an ordinary random train/test problem. A deployed system may encounter:

- new picture prompts or tasks,
- different languages,
- microphones and recording protocols,
- segmentation policies,
- ASR error profiles,
- different cohorts [§1, pp. 1–2].

They argue that:

- hand-designed markers may reverse direction across domains;
- deep representations may achieve high average

The complete evidence-grounded digest is in [`sources/al-2026-why-alzheimer-s-speech-screening.md`](../../sources/al-2026-why-alzheimer-s-speech-screening.md).

## Methodology and Architecture

Read the linked source digest for the paper's full method, equations, implementation details, and page/section anchors.

## Results

The linked source digest preserves the paper-reported results and their evidence boundaries; this page does not claim an independent reproduction.

## Related Papers

- [[overviews/2026-symbolic-music-literature-map]] — primary synthesis anchor for this batch; the overview places this paper beside related representation, generation, evaluation, and auditability work.
