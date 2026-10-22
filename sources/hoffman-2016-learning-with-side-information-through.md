---
title: "Learning with Side Information through Modality Hallucination"
authors: Judy Hoffman, Saurabh Gupta, Trevor Darrell
year: 2016
doi: 10.1109/CVPR.2016.96
category: other
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/hoffman-2016-learning-with-side-information-through.pdf"
pdf_filename: hoffman-2016-learning-with-side-information-through.pdf
source_collection: cvf-open-access
source_format: pdf
extracted_date: 2026-10-22
---

## One-line Summary

Hoffman et al. train an RGB object detector with depth as side information only at training time: a hallucination branch learns to mimic mid-level depth features from RGB, and the RGB-only detector at test time outperforms both RGB-only and RGB-ensemble baselines on NYUDv2.

## 1. Document Information

- **Exact title:** *Learning with Side Information through Modality Hallucination*. [PDF p. 1]
- **Authors:** Judy Hoffman, Saurabh Gupta, Trevor Darrell (UC Berkeley). [PDF p. 1]
- **Source record:** CVPR 2016, pp. 826–834, DOI `10.1109/CVPR.2016.96`. PDF from the CVF open-access proceedings. [PDF p. 1; OpenAlex record]
- **Length and denominator:** 9/9 pages checked, including Figure 1, Table 1, and the layer/initialisation ablations.
- **Extraction method:** `pdftotext -layout`; Table 1's columns are partially reflowed, so the digest quotes the paper's category-count claim and avoids ambiguous per-class numbers.
- **Canonical integrity:** SHA-256 recorded at ingest. Downloaded from `openaccess.thecvf.com`.
- **Category note:** filed under `other` because it is a general cross-modal transfer method, not a music-domain contribution.

Author-reported claims are the default; repository interpretation is marked.

## 2. Key Contributions

1. **Modality hallucination:** a branch that takes RGB and is trained to reproduce depth-network mid-level activations, so depth information is available at test time without a depth sensor. [§1, Fig. 1]
2. **Joint training** with detection losses and a hallucination loss on pool5 features. [§3]
3. **Test-time RGB-only detector** that uses both the RGB and hallucination branches. [§1]
4. **NYUDv2 detection gains** over RGB-only and RGB-ensemble baselines. [§4.1, Table 1]

## 3. Methodology and Architecture

- **Base detector:** Fast R-CNN with a two-stream RGB and depth network. [§3]
- **Hallucination network:** initialised from the depth network, takes RGB, and is trained to mimic depth pool5 activations. [§3]
- **Losses:** standard classification and bounding-box losses plus the hallucination regression loss. [§3]
- **Inference:** RGB image passes through the RGB and hallucination branches; no depth is required. [§1]

## 4. Key Results and Benchmarks

- **NYUDv2 detection:** the method outperforms both the RGB-only baselines and the RGB-ensemble baselines. [§4.1, Table 1]
- **Category counts:** 14/19 categories improve for the AlexNet hallucination model versus an AlexNet RGB ensemble; 13/19 improve for the VGG-1024 hallucination model versus an AlexNet+VGG ensemble. [§4.1]
- **Interpretation:** the paper established the "hallucinate the privileged modality at train time, deploy single-modality" pattern. It is the direct ancestor of modality distillation (Garcia et al. 2018), and conceptually the ancestor of AGT 3's audio-teacher/symbolic-student design.

## 5. Limitations and Future Work

- **Object detection only**, RGB-D; no music or sequence data.
- **Mid-level feature mimicry** assumes the privileged and target modalities share spatial structure; audio and symbolic tokens do not, so a symbolic student cannot copy a frame-like feature map directly.
- **Depth is not available at test time** and the hallucinated features are only as good as the RGB cue allows.
- **No attribution** of which input regions produced the hallucinated evidence.

## 6. Related Work

- Modality distillation (Garcia et al. 2018): extends the idea with multiplicative connections and soft labels.
- SoundNet and Look, Listen and Learn: cross-modal transfer between vision and audio.
- Learning using privileged information: the broader theoretical framing.

## 7. Glossary

- **AP:** Average Precision.
- **Fast R-CNN:** a region-based object detector.
- **NYUDv2:** NYU Depth Dataset V2.
- **pool5:** the fifth pooling layer of the backbone network.
