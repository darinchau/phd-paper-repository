"""Validate paper-record schemas, paths, links, and crop evidence."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

from PIL import Image


SOURCE_HEADINGS = [
    "One-line Summary",
    "1. Document Information",
    "2. Key Contributions",
    "3. Methodology and Architecture",
    "4. Key Results and Benchmarks",
    "5. Limitations and Future Work",
    "6. Related Work",
    "7. Glossary",
]
WIKI_HEADINGS = [
    "Summary",
    "Key Contributions",
    "Methodology and Architecture",
    "Results",
    "Related Papers",
]
REQUIRED_SOURCE_FIELDS = {
    "title",
    "authors",
    "year",
    "doi",
    "category",
    "pdf_path",
    "pdf_filename",
    "source_collection",
    "source_format",
    "extracted_date",
}
REQUIRED_WIKI_FIELDS = REQUIRED_SOURCE_FIELDS | {"source", "tags"}
DOMAIN_CATEGORIES = {
    "data-and-representation",
    "generation-and-planning",
    "theory-and-constraints",
    "explainability-and-auditability",
    "retrieval-and-recombination",
    "interaction-and-evaluation",
    "other",
}


def frontmatter(markdown_file: Path) -> dict[str, str]:
    text = markdown_file.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"Missing YAML frontmatter: {markdown_file}")
    _, block, _ = text.split("---\n", 2)
    metadata: dict[str, str] = {}
    for line in block.splitlines():
        match = re.match(r"^([a-z_]+):(?:\s*(.*))?$", line)
        if match:
            metadata[match.group(1)] = (match.group(2) or "").strip().strip('"')
    return metadata


def sha256(file_path: Path) -> str:
    digest = hashlib.sha256()
    with file_path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def top_level_headings(markdown_file: Path) -> list[str]:
    return re.findall(
        r"^## ([^\n]+)$", markdown_file.read_text(encoding="utf-8"), flags=re.MULTILINE
    )


def validate_record(
    repo_root: Path,
    markdown_file: Path,
    expected_fields: set[str],
    expected_headings: list[str],
) -> list[str]:
    errors: list[str] = []
    try:
        metadata = frontmatter(markdown_file)
    except ValueError as error:
        return [str(error)]
    missing = expected_fields - metadata.keys()
    if missing:
        errors.append(f"{markdown_file}: missing frontmatter {sorted(missing)}")
    if metadata.get("category") not in DOMAIN_CATEGORIES:
        errors.append(f"{markdown_file}: invalid category {metadata.get('category')!r}")
    headings = top_level_headings(markdown_file)
    if headings != expected_headings:
        errors.append(
            f"{markdown_file}: top-level headings {headings!r}, expected {expected_headings!r}"
        )

    pdf_name = metadata.get("pdf_filename")
    pdf_value = metadata.get("pdf_path")
    if pdf_name and pdf_value:
        pdf_file = Path(pdf_value)
        if not pdf_file.is_absolute():
            errors.append(f"{markdown_file}: pdf_path is not absolute")
        elif not pdf_file.exists():
            errors.append(f"{markdown_file}: pdf_path does not exist: {pdf_file}")
        else:
            if pdf_file.name != pdf_name:
                errors.append(f"{markdown_file}: pdf_filename does not match pdf_path")
            if not pdf_file.resolve().is_relative_to((repo_root / "papers").resolve()):
                errors.append(f"{markdown_file}: pdf_path is outside papers/")
    if markdown_file.stem != Path(pdf_name or "").stem:
        errors.append(f"{markdown_file}: paper/source/PDF stems disagree")
    return errors


def validate_links(repo_root: Path, markdown_files: list[Path]) -> list[str]:
    errors: list[str] = []
    for markdown_file in markdown_files:
        text = markdown_file.read_text(encoding="utf-8")
        for target in re.findall(r"\[\[([^\]|#]+)", text):
            target_file = repo_root / "wiki" / f"{target}.md"
            if not target_file.exists():
                errors.append(f"{markdown_file}: missing wikilink target {target}")
        for target in re.findall(r"!\[[^\]]*\]\(([^)]+)\)", text):
            image_file = (markdown_file.parent / target).resolve()
            if not image_file.exists():
                errors.append(f"{markdown_file}: missing image {target}")
        for target in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", text):
            if re.match(r"^[a-z]+://", target) or target.startswith("#"):
                continue
            target_without_fragment = target.split("#", 1)[0]
            linked_file = (markdown_file.parent / target_without_fragment).resolve()
            if not linked_file.exists():
                errors.append(f"{markdown_file}: missing Markdown link {target}")
    return errors


def validate_crops(repo_root: Path) -> list[str]:
    errors: list[str] = []
    manifests = list(repo_root.glob("wiki/*/assets/*/crop-evidence.json"))
    for manifest_file in manifests:
        manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
        pdf_file = repo_root / manifest["source_pdf"]
        if not pdf_file.exists():
            errors.append(f"{manifest_file}: missing source PDF")
            continue
        if sha256(pdf_file) != manifest["source_sha256"].lower():
            errors.append(f"{manifest_file}: source checksum mismatch")
        ids: set[str] = set()
        outputs: set[str] = set()
        for crop in manifest["crops"]:
            if crop["id"] in ids:
                errors.append(f"{manifest_file}: duplicate crop id {crop['id']}")
            ids.add(crop["id"])
            if crop["output"] in outputs:
                errors.append(f"{manifest_file}: duplicate crop output {crop['output']}")
            outputs.add(crop["output"])
            output_file = repo_root / crop["output"]
            if not output_file.exists():
                errors.append(f"{manifest_file}: missing crop {crop['output']}")
                continue
            with Image.open(output_file) as image:
                if image.format != "PNG" or min(image.size) <= 0:
                    errors.append(f"{output_file}: invalid PNG")
    return errors


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    source_files = sorted((repo_root / "sources").glob("*.md"))
    wiki_files = sorted(
        file_path
        for category in DOMAIN_CATEGORIES
        for file_path in (repo_root / "wiki" / category).glob("*.md")
    )
    errors: list[str] = []
    for source_file in source_files:
        errors.extend(
            validate_record(repo_root, source_file, REQUIRED_SOURCE_FIELDS, SOURCE_HEADINGS)
        )
    for wiki_file in wiki_files:
        errors.extend(
            validate_record(repo_root, wiki_file, REQUIRED_WIKI_FIELDS, WIKI_HEADINGS)
        )
        metadata = frontmatter(wiki_file)
        source_name = metadata.get("source")
        if source_name and not (repo_root / "sources" / source_name).exists():
            errors.append(f"{wiki_file}: missing source record {source_name}")
    synthesis_files = sorted(
        file_path
        for folder in ("overviews", "concepts", "questions")
        for file_path in (repo_root / "wiki" / folder).glob("*.md")
    )
    catalog_files = [repo_root / "README.md", repo_root / "index.md"]
    catalog_files.extend(sorted((repo_root / "indexes").glob("*.md")))
    catalog_files.extend(sorted((repo_root / "logs").glob("*.md")))
    errors.extend(
        validate_links(
            repo_root,
            source_files + wiki_files + synthesis_files + catalog_files,
        )
    )
    errors.extend(validate_crops(repo_root))

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        raise SystemExit(1)
    print(
        f"Validated {len(source_files)} source record(s), {len(wiki_files)} paper page(s), "
        f"{len(synthesis_files)} synthesis page(s), and crop evidence."
    )


if __name__ == "__main__":
    main()
