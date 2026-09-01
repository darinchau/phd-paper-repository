"""Build the root catalog, populated category indexes, and log guide."""

from __future__ import annotations

import argparse
import re
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


def frontmatter(markdown_file: Path) -> dict[str, str]:
    text = markdown_file.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    _, block, _ = text.split("---\n", 2)
    values: dict[str, str] = {}
    for line in block.splitlines():
        match = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if match:
            values[match.group(1)] = match.group(2).strip().strip('"')
    return values


def paper_pages(repo_root: Path) -> list[tuple[Path, dict[str, str]]]:
    records: list[tuple[Path, dict[str, str]]] = []
    for category in DOMAIN_CATEGORIES:
        category_dir = repo_root / "wiki" / category
        if not category_dir.exists():
            continue
        for markdown_file in sorted(category_dir.glob("*.md")):
            metadata = frontmatter(markdown_file)
            if metadata.get("category") == category:
                records.append((markdown_file, metadata))
    return records


def markdown_link(repo_root: Path, file_path: Path, label: str) -> str:
    relative = file_path.relative_to(repo_root).as_posix()
    return f"[{label}]({relative})"


def build_root_index(repo_root: Path, generated_date: str) -> None:
    records = paper_pages(repo_root)
    sources = list((repo_root / "sources").glob("*.md")) if (repo_root / "sources").exists() else []
    pdfs = list((repo_root / "papers").glob("*.pdf")) if (repo_root / "papers").exists() else []
    synth_counts = {
        name: len(list((repo_root / "wiki" / name).glob("*.md")))
        if (repo_root / "wiki" / name).exists()
        else 0
        for name in ("overviews", "concepts", "questions")
    }
    connected = 0
    for markdown_file, _ in records:
        body = markdown_file.read_text(encoding="utf-8")
        if "[[overviews/" in body or "[[concepts/" in body:
            connected += 1

    lines = [
        "# PhD Paper Repository Index",
        "",
        f"Catalog generated on {generated_date} from repository content.",
        "",
        "## Coverage",
        "",
        f"- Canonical PDFs: **{len(pdfs)}**",
        f"- Source digests: **{len(sources)}**",
        f"- Domain paper pages: **{len(records)}**",
        f"- Papers linked to an overview or concept: **{connected}/{len(records)}**",
        f"- Overviews: **{synth_counts['overviews']}**",
        f"- Concepts: **{synth_counts['concepts']}**",
        f"- Questions: **{synth_counts['questions']}**",
        "",
        "## Domain Categories",
        "",
        "| Category | Papers | Index |",
        "|---|---:|---|",
    ]
    for category in DOMAIN_CATEGORIES:
        category_records = [record for record in records if record[1].get("category") == category]
        if category_records:
            lines.append(
                f"| `{category}` | {len(category_records)} | "
                f"[open](indexes/{category}.md) |"
            )
        else:
            lines.append(f"| `{category}` | 0 | — |")

    lines.extend(["", "## Papers", ""])
    for markdown_file, metadata in records:
        title = metadata.get("title", markdown_file.stem)
        authors = metadata.get("authors", "Unknown author")
        year = metadata.get("year", "n.d.")
        lines.append(
            f"- {markdown_link(repo_root, markdown_file, title)} — {authors} ({year})"
        )

    lines.extend(["", "## Synthesis", ""])
    for folder, label in (
        ("overviews", "Overview"),
        ("concepts", "Concept"),
        ("questions", "Question"),
    ):
        for markdown_file in sorted((repo_root / "wiki" / folder).glob("*.md")):
            metadata = frontmatter(markdown_file)
            title = metadata.get("title", markdown_file.stem.replace("-", " ").title())
            lines.append(
                f"- **{label}:** {markdown_link(repo_root, markdown_file, title)}"
            )

    (repo_root / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_category_indexes(repo_root: Path) -> None:
    records = paper_pages(repo_root)
    index_dir = repo_root / "indexes"
    index_dir.mkdir(parents=True, exist_ok=True)
    for category in DOMAIN_CATEGORIES:
        category_records = [record for record in records if record[1].get("category") == category]
        output_file = index_dir / f"{category}.md"
        if not category_records:
            if output_file.exists():
                output_file.unlink()
            continue
        lines = [f"# {category.replace('-', ' ').title()}", ""]
        for markdown_file, metadata in category_records:
            title = metadata.get("title", markdown_file.stem)
            authors = metadata.get("authors", "Unknown author")
            year = metadata.get("year", "n.d.")
            relative = (Path("..") / markdown_file.relative_to(repo_root)).as_posix()
            lines.append(f"- [{title}]({relative}) — {authors} ({year})")
        output_file.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_log_guide(repo_root: Path) -> None:
    log_dir = repo_root / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    logs = sorted(
        file_path
        for file_path in log_dir.glob("????-??-??-*.md")
        if file_path.name != "README.md"
    )
    lines = [
        "# Work Logs",
        "",
        "Daily ingestion and maintenance narratives, newest first.",
        "",
    ]
    for log_file in reversed(logs):
        first_heading = next(
            (
                line.removeprefix("# ").strip()
                for line in log_file.read_text(encoding="utf-8").splitlines()
                if line.startswith("# ")
            ),
            log_file.stem,
        )
        lines.append(f"- [{first_heading}]({log_file.name})")
    (log_dir / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--date", required=True, help="Catalog date in YYYY-MM-DD form")
    args = parser.parse_args()
    repo_root = args.repo_root.resolve()
    build_root_index(repo_root, args.date)
    build_category_indexes(repo_root)
    build_log_guide(repo_root)


if __name__ == "__main__":
    main()
