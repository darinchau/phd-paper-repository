# 2026-10-17 — ArtiAgent (Park et al., CVPR 2026) ingestion

## Scope and completion

User-requested digest of **ArtiAgent** — "See and Fix the Flaws: Enabling VLMs and Diffusion Models to Comprehend Visual Artifacts via Agentic Data Synthesis", Jaehyun Park, Minyoung Ahn, Minkyu Kim, Jonghyun Lee, Jae-Gil Lee, Dongmin Park (KAIST / SNU / KRAFTON); arXiv `2602.20951v2` (v2 2026-03-26). Ingested per the digest command convention as part of registry step SLOP 3e; this is the digest the SLOP 4b handoff (ArtiAgent reproduction) was waiting on.

- PDF provenance: downloaded directly from arXiv (`pdf/2602.20951v2`), 29 pages, 38.3 MB; canonical copy in `papers/park-2026-see-and-fix-the-flaws.pdf`; SHA-256 `b7bfb4ffd218c5bc7e770cefb01b4453909a28281505be4e6a3dcfd8f75e65a0` in the source record.
- Full-paper evidence: all 29 pages read from PyMuPDF extraction (main pp. 1–8; references pp. 9–11; supplementary pp. 12–29 including all prompt templates Figures 12–17, tool algorithms 1–5, evaluation protocol B.3, VQA templates B.4, and correction-loop Algorithm 6). Figure 7's reward values are present in the extracted text; the qualitative galleries (Figures 9–11, 18–19) were not inspected pixel-wise — nothing quantitative rests on them.
- Shared `.venv` pip install was hanging on this network, so extraction used the system Python's PyMuPDF; no repository environment was modified.

## Records

- `papers/park-2026-see-and-fix-the-flaws.pdf` + `sources/park-2026-see-and-fix-the-flaws.md` + `wiki/other/park-2026-see-and-fix-the-flaws.md`.
- `wiki/overviews/2026-symbolic-music-literature-map.md` updated: one `### other` category entry, one Related Papers entry, and body sentences in "Evaluation and human interaction" (self-metric circularity caution) and "Adjacent and low-relevance methods" (ArtiAgent's elevated priority for the SLOP side line, with the repo-verified release scope).
- Reciprocal synthesis link + body paragraph added to `wiki/concepts/auditable-creative-editing-pipelines.md`: ArtiAgent's detect→caption→inpaint→verify loop as the vision-domain instance of workflow transparency whose verify stage is self-referential (the repair-guiding VLM doubles as the verifier).

Category decision: `other` — vision-domain paper admitted for the SLOP repair/audit side line; its primary contribution (agentic artifact-data synthesis via DiT positional/value-embedding manipulation) fits none of the music-domain categories, matching the precedent of the other cross-domain CV papers (LapSRN, RCAN, CDDFuse). Reason documented on the wiki page.

## Supersede check

No contradictions with existing wiki content. Deltas: (1) **strengthens** the literature-map Evaluation section's separation rule — ArtiAgent supplies a concrete, current, vision-domain instance of a repair loop closing against its own signal (VLM self-verification, reward model trained on its own synthetic pairs). (2) **narrows** the auditable-creative-editing-pipelines concept's boundary claim: a stage-decomposed loop with a fixed intermediate and a local verify query still stops at workflow transparency when the verifier is not independent. (3) The SLOP 3b novelty note's characterization ("evaluates repair qualitatively only, §6.2.2, Figure 8") is confirmed against the PDF; its "VLM self-verification loop" reading matches Appendix C.2/Algorithm 6.

## Repo-side verification carried into the record

From the SLOP 4b handoff (2026-10-17), recorded in the source record with explicit provenance: released = synthesis pipeline code (`krafton-ai/ArtiAgent`, CC-BY-NC-4.0) + ArtiBench on HF; **not** released = the 100K training set, fine-tuned VLM checkpoints, VLM fine-tuning code, perception-eval code, reward-model code, and correction-pipeline code. HF issue #11 is the open release request to watch.

## Synthesis gaps noted

- No overview or concept page yet covers **artifact-repair evaluation methodology** (how to judge a repair: human-grounded, metric-based, placebo-controlled). ArtiAgent now joins the SLOP-adjacent set as the strongest negative example (self-verified, qualitative-only repair). If the SLOP protocol's S0 stage produces a paper, that anchor should be created then; for now the literature-map Evaluation sentence carries the observation.

## Validation and status

- `validate_paper_records.py`: 73 source records, 73 paper pages, 11 synthesis pages — 0 errors, 0 warnings.
- `audit_synthesis_orphans.py`: 0/73 orphans.
- `build_indexes.py --date 2026-10-17` run after ingestion; `index.md`, `indexes/other.md`, and `logs/README.md` regenerated (the pre-existing uncommitted 2026-10-16 log-index line was preserved).
- Evidence limitations preserved: venue attribution (CVPR 2026) comes from research-line notes, not the PDF text; Table 1's artifact frequencies rest on a single-annotator 500-image audit; localization F1 is computed over positive ground-truth pixels only (a protocol choice that limits cross-paper comparability); LEGION's SynthScars entries are train/test contaminated per the paper's own dagger.
