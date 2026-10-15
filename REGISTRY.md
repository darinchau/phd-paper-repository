# Recording paper digests in the registry

When you digest a paper as part of a research step tracked in the parent repository's `registry/`, you must record the digest path correctly so the dashboard can link to it.

## Quick reference

After completing a digest (Steps 0–4 in AGENTS.md), update your registry card:

```bash
cd ../..  # back to phd-research root
python scripts/registry.py update "YOUR-CODE" \
  --paper "projects/phd-paper-repository/wiki/{category}/{stem}.md"
```

The `--paper` argument takes the **wiki digest path**, not the arXiv ID or PDF path.

Example:
```bash
python scripts/registry.py update "OPS MATCHA-Digest" \
  --paper "projects/phd-paper-repository/wiki/interaction-and-evaluation/batlle-roca-2026-on-the-human-and-computer.md"
```

## What goes in `papers:`

The `papers:` field in a registry step card holds **relative paths from the phd-research root** to wiki digest markdown files.

✅ **Correct:**
```yaml
papers:
- "projects/phd-paper-repository/wiki/generation-and-planning/wu-2023-museformer-a-transformer-with-fine.md"
- "projects/phd-paper-repository/wiki/data-and-representation/fradet-2023-miditok-a-python-package-for.md"
```

❌ **Wrong:**
```yaml
papers:
- "arXiv:2312.09703"  # this is an ID, not a path
- "papers/wu-2023-museformer-a-transformer-with-fine.pdf"  # this is the PDF, not the digest
- "wiki/generation-and-planning/wu-2023-museformer-a-transformer-with-fine.md"  # missing projects/phd-paper-repository/
```

## Why this matters

The dashboard uses these paths to:
- Link step cards to the papers they reference
- Build the citation graph showing which research depends on which literature
- Validate that digests exist and are reachable

An arXiv ID or PDF path will show as "unknown paper" in the dashboard and break the citation graph.

## Full workflow: digest + record

1. **Claim the registry step** (if not already claimed):
   ```bash
   cd /path/to/phd-research
   python scripts/registry.py claim "YOUR-CODE"
   ```

2. **Digest the paper** following AGENTS.md (Steps 0–4):
   ```bash
   cd projects/phd-paper-repository
   # ... obtain PDF, extract, write sources/{stem}.md, write wiki/{category}/{stem}.md, link synthesis ...
   ```
   
   You now have a path like:
   ```
   wiki/interaction-and-evaluation/batlle-roca-2026-on-the-human-and-computer.md
   ```

3. **Record the digest in your registry card**:
   ```bash
   cd ../..  # back to phd-research root
   python scripts/registry.py update "YOUR-CODE" \
     --paper "projects/phd-paper-repository/wiki/interaction-and-evaluation/batlle-roca-2026-on-the-human-and-computer.md"
   ```

4. **Close the step when done**:
   ```bash
   python scripts/registry.py update "YOUR-CODE" \
     --status done \
     --outcome writing \
     --synopsis "Which perceptual alignment benchmarks exist? -> Ingested Batlle-Roca 2026 MATCHA benchmark; attribute framing improves inter-rater agreement (kappa ~0.60) but metric alignment is partial"
   ```

5. **Commit both repositories**:
   ```bash
   # Commit the digest
   cd projects/phd-paper-repository
   git add papers/ sources/ wiki/ indexes/ index.md logs/
   git commit -m "digest: ingest MATCHA attribute-match perceptual alignment benchmark"
   git push
   
   # Commit the registry card
   cd ../..
   git add registry/
   git commit -m "YOUR-CODE: record digest in registry"
   git push
   ```

## Finding the category

If you're not sure which category a paper belongs to, check:
1. The paper's research domain (evaluation → `interaction-and-evaluation`, tokenization → `data-and-representation`, etc.)
2. Existing similar papers in `indexes/{category}.md`
3. The category list in AGENTS.md § Categories

The categories are:
- `data-and-representation` — tokenization, datasets, representations
- `generation-and-planning` — composition, arrangement, infilling
- `theory-and-constraints` — music theory, harmonic analysis, constraints
- `explainability-and-auditability` — interpretability, attribution, verification
- `retrieval-and-recombination` — search, recommendation, style transfer
- `interaction-and-evaluation` — user studies, perceptual evaluation, interfaces
- `concepts` — cross-cutting definitions and mechanisms
- `overviews` — literature surveys and synthesis
- `questions` — open questions
- `other` — meta-research, position papers, tools

## Troubleshooting

**"unknown paper" in dashboard:**
- Check that the `papers:` field holds a path starting with `projects/phd-paper-repository/wiki/`
- Verify the file exists: `ls projects/phd-paper-repository/wiki/{category}/{stem}.md`
- Use `registry.py update "CODE" --paper "path"` to fix it

**"No such file" when updating:**
- Make sure you're in the `phd-research` root when running `registry.py`
- The path is relative from that root, not from `projects/phd-paper-repository/`

**Multiple papers in one step:**
- Call `--paper "path1"` multiple times, or edit the card and put them in a YAML list:
  ```yaml
  papers:
  - "projects/phd-paper-repository/wiki/category/first.md"
  - "projects/phd-paper-repository/wiki/category/second.md"
  ```
