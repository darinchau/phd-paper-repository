# 2026-10-14 — MATCHA paper ingestion

## Scope and completion

User-requested digest of "On the Human and Computer Alignment of Attribute-Based Music Matches" (Batlle-Roca et al., arXiv:2609.00987v1, 1 September 2026, 15 pages; MTG-UPF / Sony AI / EC JRC). One paper, ingested per the digest command convention (high-impact mode: single paper, synthesis bodies updated).

- Canonical PDF downloaded from arXiv to `papers/batlle-roca-2026-on-the-human-and-computer.pdf` — SHA-256 `b5f306cc1251f0fc57cecfbd8ada14c10c51d42d61626540e91c4b5c0ad4e796`. Redistribution basis: arXiv non-exclusive license on the exact v1 PDF, consistent with the existing arXiv PDFs in `papers/`.
- All 15 pages read from the PDF extraction (main body pp. 1–7, references pp. 7–9, appendices A–C pp. 10–15, including the datasheet).
- Figures 1 and 2 (the paper's conclusions live in these panels) were rendered to PNG and visually inspected. Two independent visual reads agreed on all direction/pattern claims (AS near-zero τ, CoverID → melody/harmony, CLAP/DEfNet → rhythm/voice/timbre, KL weak on tonal dimensions) but disagreed on some cell magnitudes; the source record therefore labels all per-cell values as approximate and treats prose-stated ranges as authoritative. Rendering used a temporary `pymupdf` install in the OS temp directory; the shared repo `.venv` was not modified.

## Records

- `papers/batlle-roca-2026-on-the-human-and-computer.pdf` (canonical copy)
- `sources/batlle-roca-2026-on-the-human-and-computer.md`
- `wiki/interaction-and-evaluation/batlle-roca-2026-on-the-human-and-computer.md`
- `wiki/overviews/2026-symbolic-music-literature-map.md` updated as the bidirectional synthesis anchor: new entry in the interaction-and-evaluation list, new Related Papers entry, and a body sentence in the "Evaluation and human interaction" synthesis section.
- Paper-to-paper cross-links added bidirectionally with `wiki/explainability-and-auditability/al-2026-towards-ai-generated-music-plagiarism.md` (and one-way from the new page to TrueMuse).

Category decision: `interaction-and-evaluation` — the primary methodological contribution is a perceptual human study and evaluation benchmark, not a new similarity metric or explanation method; replication assessment is the motivation, covered by tags and synthesis links.

## Supersede check

Strengthens, does not contradict: the attribute-specific alignment results empirically support the existing claim (literature map; plagiarism-VI paper) that no single scalar similarity score captures musical similarity. No claims replaced. Delta recorded here per the synthesis requirement.

## Synthesis gap noted

No concept page exists for perceptually grounded, attribute-level similarity/replication evaluation. The topic is now touched by at least five papers (MATCHA, plagiarism-VI, TrueMuse, tracing-inputs-verifying-outputs, repetition-and-copying), so it qualifies as a recurring anchor candidate. Creation deferred to a future session rather than decided inside this ingest; the literature map carries the interim synthesis sentence.

## Validation and status

- `validate_paper_records.py`: 69 source records, 69 paper pages, 10 synthesis pages, crop evidence — 0 errors, 0 warnings.
- `build_indexes.py --date 2026-10-14` run after ingestion and again after this log; `index.md`, `indexes/interaction-and-evaluation.md`, and `logs/README.md` regenerated.
- Evidence limitations preserved in the source record: heatmap cell values approximate; AS-subset alignment evidence is a generation artifact per the authors; AI-generated alignment rests on the 30 uncontrolled AM cases; no symbolic metric evaluated.
