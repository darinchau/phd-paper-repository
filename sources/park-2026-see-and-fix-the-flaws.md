---
title: "See and Fix the Flaws: Enabling VLMs and Diffusion Models to Comprehend Visual Artifacts via Agentic Data Synthesis"
authors: "Jaehyun Park, Minyoung Ahn, Minkyu Kim, Jonghyun Lee, Jae-Gil Lee, Dongmin Park"
year: 2026
doi: 10.48550/arXiv.2602.20951
category: other
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/park-2026-see-and-fix-the-flaws.pdf"
pdf_filename: park-2026-see-and-fix-the-flaws.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-17
---

## One-line Summary

ArtiAgent is a three-agent (perception, synthesis, curation) pipeline that synthesizes structural-artifact training data without human labels — injecting artifacts into real images by manipulating positional and value embeddings of a diffusion transformer during inversion-restoration — and uses 50K such clean/artifact pairs (100K images) to fine-tune VLMs that beat proprietary baselines at artifact detection, localization, and explanation on a new 1K human-labeled benchmark (ArtiBench), with two downstream demos: reward-guided artifact-free generation and VLM-guided inpainting correction [pp. 1–8].

## 1. Document Information

- **Canonical source:** arXiv `2602.20951v2` (v2 updated 2026-03-26), KAIST / Seoul National University / KRAFTON. CVPR-format paper; identified as CVPR 2026 in the research line's novelty-check notes (SLOP 3b), though the PDF itself does not state the venue.
- **Canonical integrity:** SHA-256 `b7bfb4ffd218c5bc7e770cefb01b4453909a28281505be4e6a3dcfd8f75e65a0`. Downloaded directly from arXiv (pdf/2602.20951v2); 29 PDF pages, 38.3 MB.
- **Full-paper evidence:** all 29 pages read from a PyMuPDF full-text extraction (main paper pp. 1–8; references pp. 9–11; supplementary pp. 12–29 including all prompt templates, tool algorithms, evaluation protocol, and the correction-loop pseudocode). Figures 6–8 carry quantitative or claim-bearing content read from their text/extraction context only (Figure 7's reward values are in the extracted text; Figures 9–11, 18–19 are qualitative galleries not inspected pixel-wise).
- **Artifacts:** ArtiBench released on Hugging Face (`KRAFTON/ArtiBench`, footnote 1, p. 2). The abstract's "Code is available at link" resolves to the official GitHub repo `krafton-ai/ArtiAgent` (synthesis pipeline only; license CC-BY-NC-4.0) — repo-release scope was verified independently in the SLOP 4b handoff note (2026-10-17), not by the paper text itself.
- **Evidence policy:** author claims, reported measurements, repo-verified release facts, and repository inferences are kept distinct below.

## 2. Key Contributions

1. **ArtiAgent framework** — a fully automated agentic pipeline (no human labeling) that turns a real image into an artifact-injected twin with binary label, bounding boxes, local explanations, and a global explanation [§4, pp. 3–6].
2. **Inversion-injection tools** — a training-free artifact-injection mechanism for any DiT image generator: during inversion-restoration (FireFlow on FLUX.1-dev), target-region patches are given the positional embeddings (RoPE positions) and cached self-attention value embeddings of reference patches, so denoising "believes" the reference patch's location and content. PE injection is claimed as novel; value injection is prior art from image editing [§4.2.2, p. 4–5; App A.1, p. 12].
3. **Datasets** — a 100K-image synthesized training set (50K clean/artifact pairs from COCO, Caltech-101, 11K Hands, Celeba HQ) [§4.4, p. 6; abstract], plus **ArtiBench**, a 1K-image human-labeled benchmark (12 annotators; binary label + bboxes + descriptions; 50/50 artifact/artifact-free) built from five modern generators: SD3.5, FLUX-schnell, FLUX-dev, Qwen-Image, Nano-Banana, with prompts from MS-COCO, PartiPrompts, FuseCap [§5, p. 6; App B.2, p. 26].
4. **Experiments** — fine-tuned open VLMs (Qwen2.5-VL-7B, InternVL3.5-8B) beat GPT-4o/Gemini-2.5-Pro/GPT-5 and artifact baselines (PAL, DiffDoctor, LEGION) across detection, localization, and explanation on ArtiBench, RichHF, LOKI, SynthScars; plus two downstream applications [§6, pp. 6–8].

**Problem scoping:** the paper targets *structural* visual artifacts (physical-structure violations like two noses, six fingers, fused bodies) of *modern* DiT diffusion models, explicitly excluding text-to-image misalignment and the naive Gaussian-noise/blur artifacts of early GAN/U-Net models [§3.1, p. 3]. A 100-caption × 5-model human audit reports artifact frequencies: SD3.5-Large 36%, FLUX-schnell 28%, Qwen-Image 17%, FLUX-dev 12%, Nano-Banana 5%; type distribution roughly duplication 37% / distortion 34% / fusion 20% / omission 9% [Table 1, Figure 2, p. 3].

## 3. Methodology and Architecture

### Perception agent [§4.1, p. 3; App A.2.1, pp. 12, 16–17]

- GPT-4o decomposes the image into a two-layer entity/subentity vocabulary: **peripheral** subentities (hands, fingers, wheels — fixed/bounded count) and **intermediate** subentities (face, arm, door). Hard rules exclude variable-cardinality micro-parts (leaves, hairs), occluded parts, and torso-fused parts, to keep candidates segmentable and injectable.
- Grounded-SAM grounds entities and subentities to segmentation masks; containment analysis (mask-overlap ratio) attaches each subentity to its parent entity.

### Synthesis agent [§4.2, pp. 3–5; App A.3, pp. 12–14]

Four tools consume the grounding and emit **target–reference patch mappings** M = {(p_t, p_r)}:

- **Add (duplication):** places a copy of a peripheral subentity on a scored perimeter band around the subentity centroid; score prefers proximity, no overlap with the original instance, no collision with same-subentity instances of other objects [Alg. 1, p. 18].
- **Remove (omission):** maps every subentity patch to its nearest (L1) background-patch neighbor within a radius-R neighborhood, preferring true-background pools when they cover ≥ half the neighborhood [Alg. 2, p. 19].
- **Distort (intermediate subentities):** three kernels — shuffle (random permutation of subentity patches), Gaussian jitter (bounded resampling within same-entity foreground), strip (partition into strips along the dominant axis and circularly shift each strip with alternating signs) [Alg. 3, pp. 13, 19–20].
- **Fuse (two overlapping entities):** builds a dilated fusion band around the entity-overlap region, splits it into K farthest-point-seeded regions, and pairs each band patch with an offset-shifted patch from the opposite entity's non-overlap side [Alg. 4–5, pp. 14, 21–22].

**Inversion-injection** [§4.2.2, pp. 4–5; Figure 5, p. 5]: the image is inverted (FireFlow rectified-flow inversion) and re-denoised through FLUX.1-dev; per-layer self-attention value embeddings V(ℓ) are cached during inversion.

- *Target region:* p_t's RoPE positions for Q/K are replaced by the reference patch's position p_r, and V(p_t) ← cached V(p_r) — position decides *where*, value decides *what*.
- *Background:* original positions, original cached values.
- PE injection is off for the last 5 of 25 denoising steps (last step only for omission, which needs stronger positional perturbation); value injection runs only the first 15 steps and only in the deeper single-stream blocks 20–38 of FLUX.1-dev. The stated purpose is to avoid shortcut features (edge discontinuities) and keep background consistency. An attention-map visualization argues the fine-tuned VLM attends to genuine artifact regions rather than shortcuts [App A.1, p. 12; App A.4, p. 14, Figure 9].
- Injection-step ablation (Qwen2.5-VL-7B on ArtiBench detection, 1K samples): 5/25 → 0.513 acc, 10/25 → 0.583, **15/25 → 0.586/0.570 F1 (best)**, 20/25 → 0.540 [Table 5, p. 14].

### Curation agent [§4.3, pp. 5–6; App A.2.2–A.2.3, pp. 12, 23–24]

- **Filtering:** distortion pairs are kept iff τ1 ≤ 1 − d_LPIPS(original, artifact) ≤ τ2 with τ1=0.5, τ2=0.9 (heuristically set; high LPIPS = implausible damage, low LPIPS = unidentifiable change). Duplication/omission/fusion are filtered by GPT-4o judging an image **triplet**: masked-context original, cropped original region, cropped injected region, with per-type strict detection criteria (e.g., omission requires stump/hollow/inpainting-trace evidence and rejects "could be merely occluded"; fusion requires boundary loss, not mere blur) [Figure 14, p. 23; Figure 15, p. 23].
- **Explanations:** per-region *local* explanation from the same triplet ("what looks wrong", without naming the injection type) and a *global* 2–3-sentence image-level explanation synthesized from all bbox + local-explanation pairs [Figures 16–17, p. 24]. BLIP2 generates the clean-image caption.

### Training data [§4.4, p. 6; App B.4, p. 28]

50K pairs from COCO, Caltech-101, 11K Hands, Celeba HQ (real images; the clean side is the inversion-restoration reconstruction of the real image, to remove residual diffusion traits from the *pair* difference). VQA conversion yields two conversations per pair (clean: "no artifacts" + grounding + caption; artifact: "yes" + bbox list + region explanation + global explanation) [Tables 7–8, p. 28]. VLM fine-tuning: two-stage SFT — stage 1 LM + projector only (vision encoder frozen), lr 1e-5, batch 64, cosine decay, 1 epoch; stage 2 unfreezes the vision encoder, lr 1e-6, 200 steps [App B.4.2, p. 28].

## 4. Key Results and Benchmarks

### Artifact perception (Table 3, p. 7)

| Method | ArtiBench det. Acc/F1 | ArtiBench loc. mIoU/F1 | ArtiBench expl. ROUGE/CSS |
| --- | --- | --- | --- |
| PAL | – | 0.079 / 0.028 | – |
| DiffDoctor | – | 0.077 / 0.139 | – |
| LEGION | – | 0.067 / 0.112 | 0.133 / 0.314 |
| GPT-4o | 0.619 / 0.601 | 0.086 / 0.040 | 0.107 / 0.266 |
| Gemini-2.5-Pro | 0.582 / 0.575 | 0.061 / 0.091 | 0.097 / 0.358 |
| GPT-5 | 0.599 / 0.577 | 0.126 / 0.146 | 0.121 / 0.382 |
| Qwen2.5-VL-7B | 0.501 / 0.336 | 0.075 / 0.028 | 0.106 / 0.267 |
| Qwen2.5-VL-7B + ArtiAgent | **0.627 / 0.627** | 0.119 / 0.198 | 0.169 / 0.454 |
| InternVL3.5-8B | 0.498 / 0.357 | 0.013 / 0.022 | 0.081 / 0.189 |
| InternVL3.5-8B + ArtiAgent | **0.630 / 0.620** | 0.100 / 0.170 | 0.137 / 0.401 |

- Gains hold across the other three benchmarks (e.g., SynthScars localization F1 0.185 → 0.214 for GPT-5 vs Qwen+ArtiAgent; SynthScars explanation CSS 0.434 GPT-5 vs 0.643 Qwen+ArtiAgent). LEGION's SynthScars entries are train/test contaminated (trained on the SynthScars train split; dagger-marked).
- Stated claim: InternVL detection accuracy +26.5% (relative, 0.498→0.630) [§6.1.2, p. 7].
- **Scaling (Figure 6, p. 7):** averaged across benchmarks, localization and explanation surpass GPT-5 with as few as 1K synthesized samples; binary detection keeps improving up to 100K.
- **Human vs synthetic labels (Table 4, p. 7):** 500 SynthScars (human labels) + 500 clean ArtiAgent vs 1,000 ArtiAgent-only, on ArtiBench — detection equal (0.555/0.555 acc), localization favors human labels (mIoU 0.094 vs 0.074; attributed to ArtiAgent's patch-level granularity), explanation favors ArtiAgent (ROUGE 0.222 vs 0.156; CSS 0.606 vs 0.521).

### Evaluation protocol [App B.3, p. 27]

- Detection: accuracy + macro F1. Localization: all region formats (bbox/polygon/heatmap) are mapped to pixel-wise binary maps; IoU plus an **F1 over positive ground-truth pixels only** (explicitly to soften bbox over-prediction penalties; this protocol choice materially affects cross-paper comparability). Explanation: ROUGE-L + CSS (cosine of sentence-transformer embeddings). Evaluation prompts share a fixed "artifact prior" describing the four types [Figure 20, p. 27].

### Downstream application 1: reward-guided artifact-free generation [§6.2.1, p. 8; App C.1, p. 28]

- Bradley-Terry reward model: frozen CLIP ViT-B/16 + MLP head trained on clean-vs-artifact pairs (AdamW, lr 1e-3, batch 32, 5 epochs, two cross-scene negative pairs per batch to encourage content-agnostic ranking).
- Test-time best-of-N scaling on FLUX-schnell: round r samples 2^r latents, keeps the verifier-best image; 6 rounds × 100 MS-COCO prompts. Reported mean reward rises 0 → 0.06±0.11 → … → 0.23±0.08 across rounds [Figure 7, p. 8]. Evidence is the reward curve plus qualitative examples; no human or external-metric evaluation of the selected images.

### Downstream application 2: VLM-guided artifact correction [§6.2.2, p. 8; App C.2, pp. 28–29]

- Loop (Algorithm 6): fine-tuned Qwen2.5-VL-7B localizes the artifact bbox once; generates a "clean scene" caption; FLUX.1-dev ControlNet inpainting (AlimamaCreative beta) fills the region; the same VLM re-verifies *that region only* (Yes/No); repeat until the VLM says No.
- **Evaluation is qualitative only** (Figure 8, six before/after pairs); no quantitative repair metric, no human study of repaired outputs, and the verifier is the same model family that guided the repair — a self-verification loop. (This is the claim gap the SLOP line's S0 meta-evaluation stage targets.)

## 5. Limitations and Future Work

**Paper-stated:**

- Overall detection accuracy stays low (best 0.63 on ArtiBench) — artifact comprehension in modern images is unsolved [§6.1.2, p. 7].
- Localization gap vs human annotation is attributed to ArtiAgent's patch-level label granularity [§6.1.4, p. 7].
- LPIPS thresholds τ1/τ2 are heuristic, not derived [App A.1, p. 12].

**Evidence-boundary observations (this digest):**

- Correction (§6.2.2) has no quantitative or human evaluation; the verification signal is the repair-guiding VLM itself (circularity risk).
- The reward-guided generation result is a reward-model curve on its own 100 prompts; the reward model is trained on ArtiAgent's own synthetic pairs, so "fewer artifacts" means "higher self-trained reward", not externally judged quality.
- The §3.2 artifact-frequency audit is one human annotator over 100 captions × 5 models (500 images) — small base for the Table 1 percentages.
- Benchmarks mix label formats; the paper's own F1-over-positive-pixels choice is a comparability caveat when porting numbers.

**Repo-verified release status (SLOP 4b handoff, 2026-10-17; not paper text):** released = synthesis pipeline code (CC-BY-NC-4.0) + ArtiBench HF dataset; **not** released = the 100K training set, fine-tuned VLM checkpoints, VLM fine-tuning code, perception-eval code, reward-model code, and correction-pipeline code. Open HF issue #11 requests the checkpoints/dataset.

## 6. Related Work

- **PAL** (ICCV 2023) — 10K pixel-annotated perceptual-defect images; segmentation + inpainting correction.
- **RichHF-18K** (CVPR 2024) — human-feedback heatmaps over Pick-a-Pic images; preference-refined diffusion.
- **SynthScars / LEGION** (2025) — 12K masked-and-explained synthetic images; GLaMM-based ground-and-explain model; earlier-generator artifact distribution (Midjourney/DALL·E3/SD1.x-era).
- **DiffDoctor** (2025) — semi-supervised expansion of a 25K seed set; segmentation + diffusion fine-tuning.
- **LOKI** (2024) — multimodal synthetic-data detection benchmark (image artifact subset: 229 images).
- Inversion/editing lineage reused by the synthesis agent: SDEdit, Null-text Inversion, FireFlow, RF-Edit [§4.2.2 refs].

## 7. Glossary

- **VLM / MLLM** — vision-language model; Qwen2.5-VL-7B and InternVL3.5-8B are the fine-tuned backbones; GPT-4o, Gemini-2.5-Pro, GPT-5 the proprietary baselines.
- **DiT** — diffusion transformer (e.g., FLUX.1-dev); artifacts are injected in its self-attention during denoising.
- **PE / value injection** — replacing a target patch's rotary positional embedding (where) and cached self-attention value embedding (what) with a reference patch's.
- **RoPE** — rotary position embedding, the positional encoding manipulated by PE injection.
- **FireFlow** — fast rectified-flow inversion method used for the inversion-restoration loop.
- **Grounded-SAM** — GroundingDINO open-vocabulary detector + SAM segmentation, used by the perception agent.
- **LPIPS, τ1/τ2** — learned perceptual image distance; the 0.5/0.9 retention band for distortion filtering.
- **ArtiBench** — the paper's 1K human-labeled artifact benchmark (12 annotators, 5 modern generators, 50/50 balanced).
- **mIoU / F1 / ROUGE-L / CSS** — localization and explanation metrics; the localization F1 is computed over positive ground-truth pixels only (App B.3.2).
- **VQA / SFT** — visual question answering; supervised fine-tuning (two-stage, projector-then-vision-encoder unfreezing).
- **Bradley-Terry (BT) reward model** — pairwise preference scorer (CLIP ViT-B/16 + MLP) used for best-of-N test-time scaling.
- **Structural visual artifacts** — the paper's scope: duplication, omission, distortion, fusion; excludes prompt-misalignment defects.
