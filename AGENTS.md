# LLM Wiki — Explainable and Transparent AI for Generative Music

A personal knowledge base of papers on explainable and transparent AI for generative music, with an emphasis on symbolic classical music, explicit music-theory knowledge, auditable generation, and human evaluation.

```
Original PDF → sources/*.md → wiki/{category}/*.md → wiki/overviews/ + wiki/concepts/
```

Language policy: all wiki content is in English. Conversation can be in any language.

Scope and evidence policy: organize papers by their primary methodological contribution, use tags and synthesis links for secondary topics, and preserve the difference between a paper's claims, independently verified evidence, and repository inference. Local possession of a PDF does not establish redistribution rights. Until repository visibility and artifact rights are decided, do not publish or push PDFs whose redistribution status is restricted or unknown.

This file is the single source of truth for how agents work in this folder. Claude Code and Codex both read it. If `CLAUDE.md` is added, keep it as a symlink to this file (`ln -s AGENTS.md CLAUDE.md`) and keep the wording agent-neutral.

---

## Startup checklist

At the start of every session in this folder, before acting on any ingest, search, or synthesis request:

1. Re-read this file.
2. Re-read `index.md`, `logs/README.md`, and any applicable operational decisions under `agenda/llm-wiki-ops/` when they are present.
3. Do not rely on memory from a previous session for anything that moves.

---

## The rules

### The four core rules

1. No web search. Never use `WebSearch` or `WebFetch` to fill a gap. Every answer must be grounded in papers actually present here. Use them only when the user explicitly asks, for that one task.
2. Answer from the wiki first. `sources/` and `wiki/` are the only sources of truth.
3. If the wiki is insufficient, re-read the original PDF in `papers/` and extract more detail. Then update the wiki so the next question does not need the PDF.
4. If no paper exists on the topic, say so: "I don't have a paper on this — please give me the PDF." Do not improvise.

These apply to every response, overview pages included: cite only papers that exist in this wiki.

### Five more rules

5. A paper is not ingested until it is connected to the synthesis layer. See "The synthesis requirement" below.
6. No tiers, no placeholder pages. Every admitted paper meets the same standard: read from the original, with concrete methods, results, limitations, and synthesis links. Never create a page from an abstract, a metadata record, a reference-list mention, or a filename. If the original cannot support a complete page, leave the paper out and record the gap in the day's log.
7. Exhaustive means exhaustive. When the user asks for all of something, process the whole set before reporting. State the denominator and the numerator. Count extraction failures, empty text, and timeouts as unchecked, not as passing. Never sample and report as if you surveyed. Never negotiate the scope down because it is large — start, checkpoint, and finish.
8. Confidential material stays out of `wiki/`. Unpublished manuscripts, drafts under review, and embargoed work must not appear in `wiki/` at all — not as a page, not as a title, not as a tag, not as a "relevance to our manuscript" section on a published paper's page. Those notes go in `agenda/`. Published work with a DOI is ordinary wiki content.
9. PDFs only. The canonical full text of a paper is an exact PDF in `papers/`. Never save publisher HTML or a browser text snapshot as a substitute. If an exact PDF cannot be obtained, keep the paper on a missing-PDF list rather than ingesting a degraded copy.

Also: correction, erratum, and retraction notices are not papers. Titles beginning `Author Correction:`, `Publisher Correction:`, `Correction:`, `Erratum`, or `Retraction` never get a page. Match the correction word only when followed by `:` or `to`, so real papers about correcting something survive.

No publisher or venue is excluded by default. Evaluate papers on relevance, methodological quality, evidence, publication status, and correction or retraction status. If an exclusion policy is later adopted, document it in `agenda/llm-wiki-ops/` and enforce it with both a DOI-prefix sweep and a body-text scan; a preprint DOI can pass a DOI check even when the paper was published in an excluded venue.

---

## Repository structure

```
phd-paper-repository/
├── AGENTS.md               # This file; CLAUDE.md, if used, is a symlink to it
├── index.md                # Generated catalog: categories, page counts, synthesis coverage
├── indexes/                # Generated per-category page listings
├── logs/                   # Daily work logs — the narrative record
│   ├── {YYYY-MM-DD}-{agent}-{host}.md
│   ├── README.md           #   generated folder guide and topic index
│   └── reports/            #   audit reports written for a person to read
├── scripts/                # Extraction, validation, index and log builders
├── papers/                 # Original PDFs, canonical storage (copy, never symlink)
├── papers-supplementary/   # Publisher supplements + manifests
├── sources/                # PDF summaries, English
├── wiki/                   # Knowledge layer, English; Obsidian vault root
│   ├── {category}/
│   ├── concepts/
│   ├── overviews/
│   └── questions/
├── agenda/                 # Project execution notes, plans, handoffs, unpublished work
└── materials/              # Non-paper reference material
```

### The three synthesis layers

- `overviews/` — encyclopedic topic pages. Declarative noun-phrase titles. Never a question title.
- `concepts/` — stable definitions, methods, mechanisms. Written once, pointed at by many paper pages.
- `questions/` — paper-anchored research questions. The title is a question; the body has `## Question`, `## Sharper follow-up`, `## What the knowledge base holds`, `## Tentative answer`.

A question-form synthesis page belongs in `questions/`, never in `overviews/`.

### `agenda/`

`agenda/{project-or-context}/` holds work-facing notes: execution plans, handoff documents, analysis backlogs, decision records, meeting follow-ups, training material, and notes on unpublished manuscripts. No schema requirements.

A handoff document includes: why the method or paper is needed and what it enables, the analyses to run, the expected results, a decision section stating when to continue or pause or stop if results are weak, and the concrete deliverables. No agent-workflow notes, no personal absolute paths, no relative-date titles.

Put durable decisions about how this wiki operates in `agenda/llm-wiki-ops/` as short ADR-style notes.

### `materials/`

Non-paper reference material, with no filename convention, no category, and no PDF frontmatter requirement: journal scope and author-guideline snapshots, writing-style profiles, lecture notes, curated meeting notes, professional-activity records.

Do not link `materials/` from `wiki/`, `sources/`, or `index.md`. It is outside the paper knowledge graph by design. Keep raw audio and raw transcripts outside this repository entirely; only curated notes come in.

---

## File naming convention

All three tiers (PDF, source, wiki) share one stem:

```
{first-author-lastname}-{year}-{first-5-title-tokens}.{ext}
```

- Tokens, not words. Lowercase the title, then take runs of alphanumerics. Every non-alphanumeric character is a separator: `self-report` is two tokens. Digits count.
- Year is 4 digits. Consortium papers use the consortium name.
- Let the ingest script generate the stem. Do not hand-build it.
- Do not bulk-rename legacy stems to match a newer rule — every wikilink and index entry would have to follow. Fix only the cases where one paper's three tiers disagree with each other.

Example: `wu-2026-an-automated-pop-song-mashup.pdf`

---

## Categories

Start with these six method- or contribution-based domain categories. Split one only when it passes roughly 500 files. For a borderline paper, use its primary methodological contribution as the category and represent cross-cutting topics with tags and synthesis links.

| Category                            | Includes                                                                                                                                                                                                                                                            |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `data-and-representation`         | Corpus construction, licensing and provenance, deduplication, symbolic or audio encodings, tokenization, and score representations; excludes papers whose main contribution is a model architecture using an established representation.                            |
| `generation-and-planning`         | Generative architectures, pretraining, long-context modeling, hierarchical planning, infilling, and diffusion; excludes papers centered on explicit theory constraints or explanations.                                                                             |
| `theory-and-constraints`          | Formal music-theory rules, computational analysis, neuro-symbolic guidance, constraint satisfaction, verification, and repair; excludes descriptive musicology without a computational method and generic generation evaluated only with theory-derived metrics.    |
| `explainability-and-auditability` | Faithful decision traces, causal or mechanistic interpretability, evidence-grounded explanations, attribution, provenance, uncertainty, and auditability; excludes controllability without an explanation or faithfulness claim.                                    |
| `retrieval-and-recombination`     | Music similarity, compatibility scoring, retrieval, alignment, mashups, source-preserving transformation, and recombination; excludes unconstrained generation from scratch.                                                                                        |
| `interaction-and-evaluation`      | Co-creative interfaces, controllable editing, MIDI question answering, human studies, perceptual or behavioral evaluation, creativity and coherence metrics, and explanation utility; excludes routine evaluation that is secondary to another paper's main method. |
| `concepts`                        | Methods, mechanisms, reusable definitions.                                                                                                                                                                                                                          |
| `overviews`                       | Encyclopedic synthesis pages.                                                                                                                                                                                                                                       |
| `questions`                       | Paper-anchored research-question pages.                                                                                                                                                                                                                             |
| `other`                           | Cross-cutting work whose primary methodological contribution does not fit a domain category; document why no specific category applies.                                                                                                                             |

Classify by method, not topic: a theory-constrained generator goes to `theory-and-constraints`, not `generation-and-planning`, when its primary contribution is the constraint method. Write and preserve exclusions — asking what to deliberately leave out is what keeps categories from blurring.

---

## Adding a paper

### Step 0 — locate the PDF

Proceed only if you are beyond a resonable doubt which single PDF you are reading. Never move, delete, or overwrite files in the user's directories.

### Step 1 — copy to `papers/` and extract text

Copy, never symlink. `pdf_path` is always an absolute path inside `papers/`; `pdf_filename` matches its basename. Never put an external path in `pdf_path`. If the LaTeX source code is available along with the PDF, store that along with the PDF as well.

Use `citra` MCP for PDF reading and extraction. If you want to read diagrams, fonts, music, and other stuff, `pymupdf` can be a great choice.

### Step 2 — write `sources/{stem}.md`

```yaml
---
title: "Paper Title"
authors: Author List
year: YYYY
doi: DOI
category: {category-slug}
pdf_path: /absolute/path/to/papers/{stem}.pdf
pdf_filename: {stem}.pdf
source_collection: publisher-or-repository-collection
source_format: pdf
extracted_date: YYYY-MM-DD
---

## One-line Summary
## 1. Document Information
## 2. Key Contributions
## 3. Methodology and Architecture
## 4. Key Results and Benchmarks
## 5. Limitations and Future Work
## 6. Related Work
## 7. Glossary
```

Replace `{category-slug}` with exactly one domain category from the table above. Use tags and synthesis links for secondary contributions.

That section list is the whole schema. Do not add a section holding the raw extraction dump — the canonical full text is the PDF, and copying it in drags publisher boilerplate into the search index.

`source_collection` names a stable source class such as a publisher or repository collection. Processing metadata is forbidden in paper frontmatter: no `tier`, no `curation_level`, no batch or run names, no agent names, no dated batch identifiers, no status tags. Batch processing is an execution strategy and must be invisible in the knowledge layer; run provenance belongs in the log.

### Step 3 — write `wiki/{category}/{stem}.md`

```yaml
---
title: "Exact English Title"
authors: Author list
year: YYYY
doi: DOI
source: {stem}.md
category: {category-slug}
pdf_path: /absolute/path/to/papers/{stem}.pdf
pdf_filename: {stem}.pdf
source_collection: publisher-or-repository-collection
source_format: pdf
extracted_date: YYYY-MM-DD
tags: []
---

## Summary
## Key Contributions
## Methodology and Architecture
## Results
## Related Papers
- [[overviews/some-page]] — relationship
```

Replace `{category-slug}` with exactly one domain category from the table above. Use tags and synthesis links for secondary contributions.

### Step 4 — connect to the synthesis layer

Mandatory. See the next section.

---

## The synthesis requirement

A source and wiki pair with no link into `overviews/` or `concepts/` is a synthesis-orphan. It behaves like a RAG cache entry, not a wiki, and defeats the purpose of the system. Every ingest, routine ones included, must end with:

1. At least one bidirectional link between the new page and the single most relevant existing overview or concept page — `Related Papers` on the paper, `Related Pages` on the synthesis page. One-way links are invisible from the side that would use them.
2. One sentence in that synthesis page's body placing the paper in context. Not just a bullet in a list. If the paper only restates what the page already says, a link is enough, but say so in the log.
3. A supersede check: does the paper strengthen, narrow, contradict, or replace an existing claim? If it contradicts or replaces one, append a `supersede` entry to the day's log.
4. If no overview or concept covers the topic, record the gap in the day's log instead of skipping silently. Create the anchor when the topic is clearly recurring.

Audit the drift with a read-only script that lists orphans. That list is the backlog.

### High-impact mode

When a paper can change an active argument, review, benchmark interpretation, or project decision:

- Process one paper, or a very small set, at a time.
- Read the relevant existing synthesis pages before writing.
- Update the overview and concept page bodies, not just the links.
- Create the concept anchor if one is missing.
- State the claim delta explicitly: strengthen, narrow, contradict, replace, or unchanged.
- If the paper's conclusion lives in a figure (heatmap direction, effect-size plot, architecture diagram), render that figure to PNG and read it as an image rather than trusting text extraction.
- If the right emphasis is unclear, ask for a short interpretation checkpoint rather than burying the decision inside a batch

---

## What the extractor gets wrong

Here are some instances where the text extraction from `citra` may be wrong. If the LaTeX source code is available, then that is the source of truth.

- Glyphs substituted rather than dropped, especially Greek letters in proper nouns.
- Minus signs lost. Undetectable from the text alone. If a sign matters, look at the PDF.
- Table columns reordered or merged, binding numbers to the wrong label.
- Figure reading order scrambled, binding values to the wrong axis label. Color is never extracted at all.
- The body silently emptied on some font runs. Corruption is per font run, not per file — a spot check on one page proves nothing about another.
- Tables that are images: invisible even to a missing-content check.
- Zero-width spaces triggering false alarms in completeness checks.
- Superscripts flattened. A layout failure, so font tools do not warn.
- Another paper appended to the end of the PDF, silently merged into one.

Two working rules: check which tool actually produced the text, because a failing extractor may fall back silently; and never run a corruption-repair substitution table in reverse, which corrupts clean text at scale and is far harder to detect than the original problem. When in doubt, read the PDF as the source of truth, or if the LaTeX code is available, that would be even better.

---

## Query-to-wiki

When a question produces a reusable comparison, analysis, decision framework, or handoff-quality synthesis, file it back instead of leaving it in chat:

- `wiki/overviews/` — research-facing literature synthesis.
- `wiki/concepts/` — stable definitions, methods, mechanisms.
- `wiki/questions/` — an open question with the evidence currently available.
- `agenda/{project-or-context}/` — execution plans, handoffs, operational notes.

Save only durable outputs a future reader would search for, not every casual answer.

---

## Housekeeping

- No scratch folders inside this repository. Temporary artifacts, text dumps, conversion output, and debug files go to the current user's temporary directory. Delete tool caches that appear.
- Supplements never go in `papers/`, which holds exactly one canonical PDF per paper. They go in `papers-supplementary/` with a manifest recording what each opaque publisher filename actually contains. Do not keep peer-review files, decision letters, or blank checklists — but do keep an author-written reporting summary, which often holds the power analysis, exclusion criteria, blinding, software versions, and demographics found nowhere else. Stop the extraction page range before it so its blank boilerplate never reaches a page.
- Never use `path` as a shell variable name. In zsh it is a special array tied to `PATH`, and assigning to it can break command lookup mid-script. The same goes for `HOME`, `IFS`, `SHELL`, `PWD`, and `RANDOM`.
- If you use git, keep the `.git` directory outside any cloud-synced folder. A sync conflict on the git index can stage hundreds of healthy files as deletions.

---

## Design principles

- Four tiers: raw PDF (immutable), `sources/`, `wiki/{category}/`, synthesis layer.
- English only in wiki content, for writing and retrieval.
- Consistent YAML in every paper record, extraction provenance included.
- No web search, no placeholders, no unconnected pages.

When in doubt, follow rule 1.
