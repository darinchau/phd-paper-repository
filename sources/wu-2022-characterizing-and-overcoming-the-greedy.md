---
title: "Characterizing and Overcoming the Greedy Nature of Learning in Multi-modal Deep Neural Networks"
authors: Nan Wu, Stanisław Jastrzębski, Kyunghyun Cho, Krzysztof J. Geras
year: 2022
doi: 10.48550/arXiv.2202.05306
category: other
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/wu-2022-characterizing-and-overcoming-the-greedy.pdf"
pdf_filename: wu-2022-characterizing-and-overcoming-the-greedy.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-22
---

## One-line Summary

Multimodal networks often learn from one modality and under-fit the others: the paper measures this with conditional utilisation rates (for example 0.63 for depth given RGB versus 0.01 for RGB given depth), proposes a conditional-learning-speed proxy, and balances training to improve generalisation.

## 1. Document Information

- **Exact title:** *Characterizing and Overcoming the Greedy Nature of Learning in Multi-modal Deep Neural Networks*. [PDF p. 1]
- **Authors:** Nan Wu, Stanisław Jastrzębski, Kyunghyun Cho, Krzysztof J. Geras (NYU and affiliates). [PDF p. 1]
- **Source record:** arXiv `2202.05306v3` [cs.LG], 16 September 2022, 13 pages; ICML 2022. [PDF p. 1]
- **Length and denominator:** 13/13 pages checked, including the definition, Table 1, and the ablation figures.
- **Extraction method:** `pdftotext -layout`; the utilisation-rate example and Table 1 read directly.
- **Canonical integrity:** SHA-256 recorded at ingest. Downloaded from `arxiv.org/pdf/2202.05306`.
- **Category note:** filed under `other` because it is a general multimodal-optimisation result with no music-specific method.

Author-reported claims are the default; repository interpretation is marked.

## 2. Key Contributions

1. **Conditional utilisation rate** `u(m1|m0)`: the relative accuracy gain from having modality m1 in addition to m0. It measures which modality a trained model actually depends on. [§4, Def. 4.1]
2. **Evidence of imbalance** across tasks and architectures; in one hand-gesture model, `u(depth|RGB) = 0.63` while `u(RGB|depth) = 0.01`. [§1, §4]
3. **A train-time proxy** (conditional learning speed) and an algorithm that balances the modalities' learning speeds. [§5–§6]
4. **Generalisation gains** on Colored MNIST, ModelNet40, and NVIDIA Dynamic Hand Gesture. [§6, Table 1]

## 3. Methodology and Architecture

- **Diagnosis:** train the full multimodal model and unimodal variants, then compare test accuracy with and without each modality; this yields the utilisation rate. [§4]
- **Proxy:** measure how fast each modality's contribution improves during training, since the final utilisation rate cannot be computed online. [§5]
- **Intervention:** reweight or schedule modality learning so the conditional learning speeds stay balanced. [§6]
- **Models:** standard two-branch fusion networks for image, depth, and audio-like inputs. [§6]

## 4. Key Results and Benchmarks

- **Imbalance is common:** across tasks, one modality dominates; in some cases the multimodal model is worse than the best unimodal model. [§1, §4]
- **Balancing helps:** the proposed algorithm improves generalisation on all three datasets relative to standard joint training. [§6, Table 1]
- **Diagnostic value:** the utilisation rate distinguishes "the model cannot use this modality" from "the model did not learn to use it". [§4]
- **Interpretation:** a multimodal setup does not guarantee that the target modality benefits; without a utilisation check, a null result may reflect optimisation failure rather than missing information. This directly motivates instrument-only and shuffled controls in audio→symbolic distillation.

## 5. Limitations and Future Work

- **Two-modality focus** in the main analysis; extension to more modalities is limited.
- **Classification tasks** with relatively small models; generation and sequence models are not tested.
- **The proxy is indirect**; balancing may help optimisation without proving that the under-used modality contains useful information.
- **No music or symbolic data.**

## 6. Related Work

- What Makes Multi-modal Learning Better than Single (Huang et al. 2021): the generalisation-theory counterpart.
- Modality distillation and hallucination: train-time-only cross-modal transfer.
- SoundNet and Look, Listen and Learn: positive cross-modal transfer results.

## 7. Glossary

- **Conditional utilisation rate:** accuracy gain from adding a modality to an existing one.
- **Conditional learning speed:** training-time proxy for that gain.
- **NVGesture:** NVIDIA Dynamic Hand Gesture dataset.
