---
title: "See and Fix the Flaws: Enabling VLMs and Diffusion Models to Comprehend Visual Artifacts via Agentic Data Synthesis"
authors: "Jaehyun Park, Minyoung Ahn, Minkyu Kim, Jonghyun Lee, Jae-Gil Lee, Dongmin Park"
year: 2026
doi: 10.48550/arXiv.2602.20951
category: other
source: park-2026-see-and-fix-the-flaws.md
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/park-2026-see-and-fix-the-flaws.pdf"
pdf_filename: park-2026-see-and-fix-the-flaws.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-17
tags:
  - artifact-repair
  - data-synthesis
  - vision-domain
  - evaluation-gap
---

## Summary

ArtiAgent (Park et al., 2026; KAIST/SNU/KRAFTON) removes the human-labeling bottleneck from artifact-perception training data. A perception agent (GPT-4o + Grounded-SAM) grounds entities and subentities in a *real* image; a synthesis agent injects one of four structural artifact types (duplication, omission, distortion, fusion) through a training-free **inversion-injection** trick — during FLUX.1-dev inversion-restoration, target patches receive a reference patch's rotary positional embedding and cached self-attention value embedding; a curation agent filters (LPIPS band for distortion; VLM triplet-judging for the rest) and writes local plus global explanations. From 50K clean/artifact pairs (COCO, Caltech-101, 11K Hands, Celeba HQ) the paper fine-tunes Qwen2.5-VL-7B and InternVL3.5-8B, which beat GPT-5, Gemini-2.5-Pro, PAL, DiffDoctor, and LEGION across detection, localization, and explanation on ArtiBench (new 1K human-labeled benchmark over SD3.5/FLUX/Qwen-Image/Nano-Banana outputs), RichHF, LOKI, and SynthScars [§4–6, pp. 3–8].

**Why `other`:** a vision-domain paper admitted for the repair/audit side line (SLOP). Its primary methodological contribution — agentic synthesis of artifact-annotated training data via DiT embedding manipulation — fits none of the music-domain categories; its relevance here is method transfer (paired clean/corrupt data, artifact taxonomies, detect→explain→repair loops) and the explicit evaluation gap its correction pipeline leaves open.

## Key Contributions

- An annotator-free pipeline producing paired clean/artifact images with binary labels, bboxes, local explanations, and a global explanation — 100K images at 1/1K-scale supervision competitive with human labels (equal detection, slightly worse localization, better explanation; Table 4).
- Inversion-injection: PE + value injection in DiT self-attention; PE injection claimed novel, model-agnostic, training-free.
- ArtiBench: 1K images, 12 annotators, 5 modern generators, 50/50 balanced, binary + bbox + description labels — the first artifact benchmark covering FLUX/Qwen-Image/Nano-Banana-era models.
- Two downstream demos: Bradley-Terry reward-guided best-of-N generation (reward 0.06→0.23 over 6 rounds, self-metric only) and a VLM-localize → FLUX-inpaint → VLM-verify correction loop.

## Methodology and Architecture

Read the linked source digest for the full pipeline, injection hyperparameters (25-step schedule, PE off last 5 steps, value injection first 15 steps in single-stream blocks 20–38), the four tool algorithms, filtering prompts, VQA conversion, two-stage SFT, and the evaluation protocol's metric definitions.

## Results

The source digest preserves all Table 3 numbers and their evidence boundaries (best ArtiBench detection accuracy 0.630; localization mIoU stays ≤ 0.14 for every method; LEGION's SynthScars entries are train/test contaminated). Nothing on this page is an independent reproduction; the SLOP line separately verified that the released repo contains only the synthesis pipeline — the 100K set, fine-tuned checkpoints, evaluation code, and the correction pipeline are not released.

## Related Papers

- [[overviews/2026-symbolic-music-literature-map]] — primary synthesis anchor; the map places this cross-domain artifact-repair work beside the auditability and evaluation entries.
- [[concepts/auditable-creative-editing-pipelines]] — its correction loop is a stage-named detect→caption→inpaint→verify pipeline: workflow transparency in the terms of that page, but the verify stage is the same VLM that guided the repair, so it stays at workflow/decision transparency without faithful-explanation validation.
