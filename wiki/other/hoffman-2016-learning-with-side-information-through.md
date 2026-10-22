---
title: "Learning with Side Information through Modality Hallucination"
authors: Judy Hoffman, Saurabh Gupta, Trevor Darrell
year: 2016
doi: 10.1109/CVPR.2016.96
source: hoffman-2016-learning-with-side-information-through.md
category: other
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/hoffman-2016-learning-with-side-information-through.pdf"
pdf_filename: hoffman-2016-learning-with-side-information-through.pdf
source_collection: cvf-open-access
source_format: pdf
extracted_date: 2026-10-22
tags: [modality-hallucination, side-information, rgb-d, object-detection]
---

## Summary

Hoffman et al. use depth as side information at training time and RGB alone at test time. A hallucination branch learns to reproduce mid-level depth features from RGB, and the joint RGB-plus-hallucination detector outperforms both RGB-only and RGB-ensemble baselines on NYUDv2 object detection. The paper established the "hallucinate the privileged modality" template later extended by modality distillation.

## Key Contributions

- Modality hallucination: an RGB branch trained to mimic depth pool5 activations. [§1, Fig. 1]
- Joint training with detection losses and a feature-mimicry loss. [§3]
- An RGB-only test-time detector that still benefits from depth. [§1]
- NYUDv2 gains over strong RGB baselines. [§4.1, Table 1]

## Methodology and Architecture

Fast R-CNN with RGB and depth streams; the hallucination network is initialised from the depth network, takes RGB, and is trained to match depth mid-level features. At inference, RGB passes through both the RGB and hallucination branches.

## Results

- Outperforms RGB-only and RGB-ensemble baselines on NYUDv2 detection. [§4.1, Table 1]
- 14/19 categories improve versus an AlexNet RGB ensemble; 13/19 versus an AlexNet+VGG ensemble. [§4.1]
- The gain depends on spatial correspondence between the privileged and target modalities, which audio and symbolic tokens do not share.

## Related Papers

- [[overviews/cross-modal-supervision-transfer]] — the side-information pattern and where it transfers.
- [[other/garcia-2018-modality-distillation-with-multiple-stream]] — the follow-up with multiplicative connections and soft labels.
- [[data-and-representation/aytar-2016-soundnet-learning-sound-representations-from]] — teacher–student transfer between vision and audio.
