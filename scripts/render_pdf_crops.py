"""Render reproducible figure-only crops declared in a JSON manifest.

The manifest uses normalized top-left coordinates so crop definitions remain
stable across rendering resolutions. Poppler's ``pdftoppm`` performs the PDF
render; Pillow performs only the deterministic crop and PNG save.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import tempfile
from pathlib import Path

from PIL import Image


def sha256(file_path: Path) -> str:
    digest = hashlib.sha256()
    with file_path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path.cwd(),
        help="Root used to resolve source_pdf and crop output paths.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    repo_root = args.repo_root.resolve()
    manifest_path = args.manifest.resolve()
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    pdf_file = (repo_root / manifest["source_pdf"]).resolve()
    expected_hash = manifest["source_sha256"].lower()
    actual_hash = sha256(pdf_file)
    if actual_hash != expected_hash:
        raise SystemExit(
            f"Source checksum mismatch: expected {expected_hash}, got {actual_hash}"
        )

    renderer = shutil.which("pdftoppm")
    if renderer is None:
        raise SystemExit("pdftoppm is required but was not found on PATH")

    dpi = int(manifest["dpi"])
    with tempfile.TemporaryDirectory(prefix="pdf-crops-") as temp_name:
        temp_dir = Path(temp_name)
        for crop in manifest["crops"]:
            pdf_page = int(crop["pdf_page"])
            preview_prefix = temp_dir / f"page-{pdf_page}"
            subprocess.run(
                [
                    renderer,
                    "-f",
                    str(pdf_page),
                    "-l",
                    str(pdf_page),
                    "-r",
                    str(dpi),
                    "-png",
                    "-singlefile",
                    str(pdf_file),
                    str(preview_prefix),
                ],
                check=True,
            )

            with Image.open(preview_prefix.with_suffix(".png")) as page_image:
                width, height = page_image.size
                left, top, right, bottom = crop["bbox_normalized"]
                if not (0 <= left < right <= 1 and 0 <= top < bottom <= 1):
                    raise SystemExit(
                        f"Invalid normalized bounding box for {crop['id']}: "
                        f"{crop['bbox_normalized']}"
                    )
                pixel_box = (
                    round(left * width),
                    round(top * height),
                    round(right * width),
                    round(bottom * height),
                )
                output_file = (repo_root / crop["output"]).resolve()
                output_file.parent.mkdir(parents=True, exist_ok=True)
                page_image.crop(pixel_box).save(output_file, format="PNG", optimize=True)
                print(
                    f"{crop['id']}: PDF p. {pdf_page} -> "
                    f"{output_file.relative_to(repo_root)}"
                )


if __name__ == "__main__":
    main()
