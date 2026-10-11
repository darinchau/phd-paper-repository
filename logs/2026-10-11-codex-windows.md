# 2026-10-11 — Root paper digestion and cleanup

## Scope and completion

The root repository contained two papers not previously represented in `projects/phd-paper-repository`: `harmony_dmrn_2020.pdf` and `Interpretable_Music_Harmonic_Analysis_Through_Multilinear_Mixture_of_Experts.pdf`. Existing repository searches found no source digest, wiki page, or canonical PDF for either title.

Both papers were read from their PDFs with layout-preserving text extraction. Canonical copies were committed before creating the digest records:

- `papers/mcleod-2020-a-modular-system-for.pdf` — SHA-256 `6ad358a29510512f96c91fdd1334dde9d32945d5d1ef1b7867957d70815e2565`; child commit `91b66c0`.
- `papers/triantafyllou-2026-interpretable-music-harmonic.pdf` — SHA-256 `e576e194b8f10a9a32fbdb5ab5d4fcc914dcdd9cdb65a2597b0c02ea204e8796`; child commit `a39784a`.

## Records

- `sources/mcleod-2020-a-modular-system-for.md`
- `wiki/theory-and-constraints/mcleod-2020-a-modular-system-for.md`
- `sources/triantafyllou-2026-interpretable-music-harmonic.md`
- `wiki/explainability-and-auditability/triantafyllou-2026-interpretable-music-harmonic.md`
- `wiki/concepts/music-domain-inductive-biases.md` updated as the bidirectional synthesis anchor.

McLeod and Rohrmeier's two-page DMRN+15 paper is categorized under theory and constraints: its six-module chord/local-key pipeline makes analysis stages inspectable, but the modules remain learned black boxes and the private-score evaluation reports only compact partial/full accuracies. Triantafyllou et al.'s ICASSP 2026 paper is categorized under explainability and auditability: MoE-RNBERT retains near-baseline RNA accuracy and shows correlational expert activation patterns around dominant-to-tonic and circle-of-fifths contexts, without causal expert interventions or human explanation-utility evidence.

## Validation and cleanup status

Indexes and log indexes were rebuilt after ingestion. The canonical PDFs will remain in the child repository; the two original PDFs at the root are temporary duplicates and are to be deleted from the root in separate deletion commits after validation. Root deletion and the parent submodule pointer update are intentionally separate from the digest commits.

The repository-wide validator may still report pre-existing absolute `pdf_path` values from older records that point to prior checkout locations; this is unrelated to the two new records. New records use the current `projects/phd-paper-repository/papers/` paths.
