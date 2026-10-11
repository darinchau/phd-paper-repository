---
title: "CDDFuse: Correlation-Driven Dual-Branch Feature Decomposition for Multi-Modality Image Fusion"
authors: "Zixiang Zhao, Haowen Bai, Jiangshe Zhang, Yulun Zhang, Shuang Xu, Zudi Lin, Radu Timofte, and Luc Van Gool"
year: 2023
doi: 10.48550/arXiv.2211.14461
category: other
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/zhao-2023-cddfuse-correlation-driven-dual-branch.pdf"
pdf_filename: zhao-2023-cddfuse-correlation-driven-dual-branch.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
---
## One-line Summary

Multi-modality image fusion combines complementary infrared/visible or medical images while preserving modality-shared structure and modality-specific detail. The authors identify three problems with prior CNN/autoencoder approaches: poor controllability/interpretability, limited local receptive fields, and loss of high-frequency information during forward propagation (`...txt:63–78`).

## 1. Document Information

- **Canonical source:** arXiv `2211.14461v2`; official PDF preserved as `zhao-2023-cddfuse-correlation-driven-dual-branch.pdf`.
- **Full-paper evidence:** delegate digest `del_mv415ez6_p068.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### CDDFuse digest

**Source inspected:** full `/tmp/paper-digest/2211.14461v2.pdf` and extracted text through its references (`/tmp/paper-digest/2211.14461v2.txt`, pp. 1–11). No files modified.

#### Problem

Multi-modality image fusion combines complementary infrared/visible or medical images while preserving modality-shared structure and modality-specific detail. The authors identify three problems with prior CNN/autoencoder approaches: poor controllability/interpretability, limited local receptive fields, and loss of high-frequency information during forward propagation (`...txt:63–78`).

#### Method

CDDFuse uses:

- A shared Restormer-based shallow feature encoder.
- A **dual branch**:
  - Lite Transformer (LT) branch for low-frequency, global/long-range “base” features.
  - Invertible Neural Network (INN) branch for high-frequency, local “detail” features (`...txt:178–235`).
- A correlation-driven decomposition loss: base features from the two modalities are encouraged to correlate, while detail features are encouraged to decorrelate (`...txt:277–300`).
- Separate LT/INN fusion layers followed by a Restormer decoder.
- Two-stage training: first reconstruct each source image; then fuse decomposed features (`...txt:239–276`).

The authors’ central assumption is that low-frequency information is modality-shared, whereas high-frequency information is modality-specific (`...txt:80–99`). Their “interpretability” claim is therefore architectural/constraint-based, not a demonstrated human-understandable explanation mechanism.

#### Results claimed by the authors

On infrared-visible fusion, CDDFuse reports:

- **MSRS:** EN 6.70, SD 43.38, SF 11.56, MI 3.47, SCD 1.62, VIF 1.05, Qabf 0.69, SSIM 1.00.
- **TNO:** EN 7.12, SD 46.00, SF 13.15, MI 2.19, SCD 1.76, VIF 0.77, Qabf 0.54, SSIM 1.03.
- **RoadScene:** EN 7.44, SD 54.67, SF 16.36, MI 2.30, SCD 1.81, VIF 0.69, Qabf 0.52, SSIM 0.98 (`...txt:342–377`).

They also report:

- **Semantic segmentation:** mIoU 64.3 on MSRS, versus 61.1 for the strongest listed prior method (`...txt:431–450`).
- Improved downstream infrared-visible detection and segmentation, with the paper stating best detection performance, particularly for people and trucks (`...txt:364–377`).
- Medical image fusion results across MRI–CT, MRI–PET, and MRI–SPECT, with leading scores on most listed metrics (`...txt:408–450`).
- Ablations support the decomposition loss, LT/INN specialization, and two-stage training. Removing the decomposition loss reduces MSRS EN/SD/VIF/SSIM from 6.70/43.38/1.05/1.00 to 6.19/36.49/0.96/0.97 (`...txt:310–326`, `...txt:347–353`).

These are author-reported benchmark results; the paper does not provide statistical significance testing.

#### Limitations

The paper has no dedicated limitations section. Evident limitations and caveats are:

1. **Strong domain assumption:** low-frequency = shared and high-frequency = modality-specific may fail for modalities whose shared information is encoded in edges/details or whose global structures differ (`...txt:83–99`).
2. **Interpretability is limited:** correlation constraints and feature visualizations make decomposition more inspectable, but do not establish semantic disentanglement or causal explanations.
3. **Evaluation is image-centric:** results rely mainly on eight handcrafted fusion metrics and a small number of downstream vision tasks (`...txt:257–275`).
4. **Training complexity:** the authors report “very unsatisfactory” results when abandoning two-stage training (`...txt:386–393`).
5. **Alignment sensitivity:** the experiments use paired modalities; misregistration is discussed as a known issue but is not solved by CDDFuse itself (`...txt:125–130`).
6. No experiments address symbolic music, audio generation, musical structure, or explainable composition.

#### Artifact status

**Public artifact available:** <https://github.com/Zhaozixiang1228/MMIF-CDDFuse>

The repository provides inference code, training code/configuration, pretrained IVF/MIF weights, test datasets, and preprocessing instructions. The README states that the large MSRS training dataset is not bundled and must be downloaded separately. It also reports commands intended to reproduce the paper’s tables. The README’s arXiv link appears inconsistent—it points to `2104.06977` rather than the supplied `2211.14461v2`—but identifies the same CDDFuse project.

### Relevance to explainable generative music AI

**Verdict: low direct relevance; limited methodological relevance.**

Potentially transferable ideas:

- Explicitly separating shared/global structure from modality- or source-specific detail.
- Using correlation/decorrelation objectives to make latent roles more controllable.
- Combining global dependency modeling with local-detail preservation.
- Inspecting branch-specific representations as an explanation aid.

However, this is only an analogy. The paper’s “low/high frequency” distinction means image feature scale and spatial detail, not musical frequency bands or symbolic musical abstraction. Nothing in the paper demonstrates transfer to symbolic music, composition, mashups, repair, musical explanation, or generative modeling.

## 3. Methodology and Architecture

The methodology and architecture are preserved in the embedded full-paper digest above, including its original page/section anchors.

## 4. Key Results and Benchmarks

Reported results and benchmark denominators are preserved in the embedded digest above; no unverified reproduction is implied by this record.

## 5. Limitations and Future Work

The evidence limitations, artifact status, and future-work claims are preserved in the embedded digest above. See the batch report for relevance to the explainable symbolic music AI programme.

## 6. Related Work

- [[overviews/2026-symbolic-music-literature-map]] — batch literature map and bidirectional synthesis anchor.

## 7. Glossary

- **Primary category:** `other`. Domain-specific terms are defined in the embedded digest and cross-paper synthesis.
