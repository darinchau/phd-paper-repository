---
title: "Co-policy: Responsive Human-Robot Co-Creation for Musical Performances"
authors: "Xuetao Li, Wenke Huang, Mang Ye, Zijian Liu, Jinhua Xie, Jifeng Xuan, and Miao Li"
year: 2026
doi: 10.48550/arXiv.2606.19914
category: interaction-and-evaluation
source: li-2026-co-policy-responsive-human-robot.md
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/li-2026-co-policy-responsive-human-robot.pdf"
pdf_filename: li-2026-co-policy-responsive-human-robot.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
tags: []
---
## Summary

The paper’s central claim is that embodied musical co-creation should be treated as a closed loop: the human supplies an incomplete musical or semantic seed, the system generates a complementary response under musical and physical constraints, and a robot realizes it through timed physical interaction.

## Key Contributions

Problem and claimed contribution

#### Problem

The authors identify two problems (§1, pp. 2–3):

1. **Semantic-to-musical grounding:** How can a robot convert an incomplete motif, style, rhythm, speech instruction, or live musical seed into a complementary response rather than copying it?
2. **Physical execution:** How can that response be executed accurately and quickly enough for interactive musical performance?

They contrast their task with:

- **Robotic playback:** The robot simply executes the user-specified notes.
- **Disembodied music generation:** A model generates symbolic or audio music without physical reachability, timing, or contact constraints.

The paper defines four dimensions of embodied co-creation (§1, p. 2):

- intent alignment,
- creative contribution/novelty,
- embodied feasibility,
- interaction responsiveness.

#### Claimed contributions

The authors claim:

1. A formal closed-loop formulation of embodied human-robot musical co-creation.
2. A modular architecture separating semantic grounding, constrained musical variation, and physical execution.
3. **GMP**, a single-pass Gaussian-mixture visuomotor policy intended to retain multiple feasible action modes without diffusion-policy denoising.
4. Real-robot chime experiments, ablations, latency measurements, ManiSkill2 checks, and blinded expert evaluation.

These are author claims; the evidence is strongest for the modular implementation and chime results, and weaker for broader claims about general musical intelligence or universal superiority over diffusion policies.

---

### 3. Architecture

### 3.1

The complete evidence-grounded digest is in [`sources/li-2026-co-policy-responsive-human-robot.md`](../../sources/li-2026-co-policy-responsive-human-robot.md).

## Methodology and Architecture

Read the linked source digest for the paper's full method, equations, implementation details, and page/section anchors.

## Results

The linked source digest preserves the paper-reported results and their evidence boundaries; this page does not claim an independent reproduction.

## Related Papers

- [[overviews/2026-symbolic-music-literature-map]] — primary synthesis anchor for this batch; the overview places this paper beside related representation, generation, evaluation, and auditability work.
