"""List domain paper pages with no link to an overview or concept."""

from __future__ import annotations

from pathlib import Path


DOMAIN_CATEGORIES = (
    "data-and-representation",
    "generation-and-planning",
    "theory-and-constraints",
    "explainability-and-auditability",
    "retrieval-and-recombination",
    "interaction-and-evaluation",
    "other",
)


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    orphans: list[Path] = []
    checked = 0
    for category in DOMAIN_CATEGORIES:
        category_dir = repo_root / "wiki" / category
        if not category_dir.exists():
            continue
        for paper_page in sorted(category_dir.glob("*.md")):
            checked += 1
            body = paper_page.read_text(encoding="utf-8")
            if "[[overviews/" not in body and "[[concepts/" not in body:
                orphans.append(paper_page.relative_to(repo_root))

    if orphans:
        print(f"Synthesis orphans: {len(orphans)}/{checked}")
        for orphan in orphans:
            print(orphan.as_posix())
        raise SystemExit(1)
    print(f"Synthesis orphans: 0/{checked}")


if __name__ == "__main__":
    main()
