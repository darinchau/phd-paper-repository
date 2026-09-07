# 2026-09-07 — Four Root Paper Ingestions

## Scope and Completion

The root held four supplied PDFs: `2608.05222v1.pdf`, `2608.06638v1.pdf`, `2608.21678v1.pdf`, and `2608.25621v1.pdf`. All four were processed independently from their originals: 9 + 13 + 10 + 19 = **51 pages**, with **4/4 source/wiki/PDF sets** connected to synthesis. The root originals were left in place. No push or publication was performed.

The knowledge base is the nested repository. Its live index and log guide were reread before ingestion; no operational-decision directory existed. Metadata-derived titles were checked against printed first pages: Diff-Symbo's author-name ordering and DS's embedded title differed from the visible document. MusPyExpress uses the explicit 2025 workshop year, corroborated by its linked code citation, while retaining the 2026 arXiv identifier. The supplied arXiv files are public preprints/workshop material, not private manuscripts.

## Extraction and Visual Evidence

Citra's Rust reader failed on Diff-Symbo with `selectable text contains an invalid horizontal advance`. Its other full-text reads succeeded, but merged spacing/layout required a second parser. Python pypdf 6.14.2 extracted all 51 pages with nonempty text. All pages, including references and appendices, were read; critical figures and result tables were also rendered and inspected with Poppler.

PyMuPDF was unavailable and an attempted temporary installation found no available package. The existing crop renderer encountered Windows temporary-directory permission errors. A temporary runner used the same Poppler/Pillow rendering and normalized crop algorithm in the already accessible system-temporary directory. Ten final crops use manifests with source SHA-256, PDF page, 144 DPI, normalized coordinates, and output path. Temporary full-text and full-page renders stay outside the repository.

The canonical filenames were generated programmatically from author, bibliographic year, and the first five alphanumeric title tokens. Exact PDF copies preserve the supplied files, including DS's appended supplement; no separate supplement or LaTeX was supplied.

## Claim Deltas and Artifact Checks

See the [review report](reports/2026-09-07-root-paper-digestion.md) for the per-paper findings and pinned artifact revisions. Diff-Symbo strengthens contextual generation while narrowing duration and control claims; MI-MIDI strengthens intervention evidence; MusPyExpress strengthens expression representation while narrowing automatic realization claims; DS strengthens a scoped relational-prior argument while narrowing perceptual and statistical interpretation.

No `supersede` action was required: none of these experiments directly contradicts or replaces an existing commensurate result. Earlier SynTheory artifact concerns remain in place. New concept anchors for expression-aware representation and DS address topics recurring across the existing music-bias and generation synthesis. Every new paper also links reciprocally to an existing overview/concept and is placed in its body.

No model scores were independently reproduced. Artifact failures and unavailable code/data remain explicitly unchecked. Static MusPy code discrepancies and the MI-MIDI showcase mismatch are retained without assuming their numerical effect on publication results. No new research paper was admitted from artifact metadata or references alone.

## Validation

- All eight new Markdown records pass the required source/wiki headings, metadata, category, canonical path, and matching-stem checks.
- All four canonical PDFs match the root originals by SHA-256 and are regular copies, not symlinks.
- All four new pages have reciprocal links to existing synthesis anchors and contextual body discussion. The read-only orphan audit reports **0/10**; the generated catalog reports **10/10** connected paper pages.
- All ten new figure/table crops were visually inspected after final cropping. Source hashes, manifests, PNG validity, and referenced image paths pass validation.
- New paper/concept/report links pass; generated indexes and the log guide were rebuilt for 2026-09-07. Parent and child `git diff --check` pass. No repository tool-cache directory was left behind.
- The full repository validator still reports **ten pre-existing PDF paths outside this checkout's papers directory**, affecting five older source/wiki pairs. Those records are unchanged. These are separate from the passing new-record checks.
