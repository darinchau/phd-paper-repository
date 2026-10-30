---
title: "YuE2: Unifying Symbolic and Audio Music Generation at Frontier Quality"
authors: "Ruibin Yuan et al."
year: 2026
doi: 10.48550/arXiv.2609.33757
category: generation-and-planning
source: al-2026-yue2-unifying-symbolic-and-audio.md
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/al-2026-yue2-unifying-symbolic-and-audio.pdf"
pdf_filename: al-2026-yue2-unifying-symbolic-and-audio.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
tags: []
---
## Summary

YuE2 factorizes generation into an inspectable symbolic score, semantic tokens, and acoustic realization. It demonstrates score-guided editing and source-identity retrieval, but its 3.58B-scale, partly licensed data regime is not modestly reproducible and the score is not itself a faithful explanation.

## Key Contributions

Bottom line:** YuE2 demonstrates that a readable score can improve and control full-song generation, but its scale and proprietary data regime are not modestly reproducible. For your programme, transfer the score interface, audit methodology, and provenance-aware conditioning—not the 3.58B end-to-end training ambition.

The complete evidence-grounded digest is in [`sources/al-2026-yue2-unifying-symbolic-and-audio.md`](../../sources/al-2026-yue2-unifying-symbolic-and-audio.md).

## Methodology and Architecture

Read the linked source digest for the paper's full method, equations, implementation details, and page/section anchors.

## Results

The linked source digest preserves the paper-reported results and their evidence boundaries; this page does not claim an independent reproduction.

## Implications (2026-10-30 re-check)

- **Commoditized interface, open audit.** An editable score between prompt and audio is now a released frontier feature (CC BY-NC 4.0, 24 GB). The paper makes no faithfulness claim and runs no copying audit, so those remain our claims; see the [programme note](../../../agent-notes/research-programme/2026-10-30-yue2-implications.md).
- **Reusable evaluation designs.** Plan-swap matched controls, adherence-versus-preservation as two separate axes, and work-identity retrieval (CLEWS/Discogs-VINet) are each directly transferable to our repair, faithfulness, and identity work.
- **Identity carries in harmony.** Dropping chord symbols lowers cover work-identity retrieval but raises style alignment and rated musicality — an external, quantitative version of our material-filter result, at chord-label level only (no voicing, no bass metrics).
- **Corpus ceiling stands.** The plan is a lead sheet (melody, chord symbols, key, metre, tempo, sections), so transcription-based expansion cannot supply the inner-voice texture that limits our polyphonic signature corpora.

## Related Papers

- [[overviews/2026-symbolic-music-literature-map]] — primary synthesis anchor for this batch; the overview places this paper beside related representation, generation, evaluation, and auditability work.
