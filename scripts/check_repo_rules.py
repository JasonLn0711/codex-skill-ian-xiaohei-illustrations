#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(".")
README = ROOT / "README.md"
IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".webp"}

FORBIDDEN_CODE_TERMS = [
    "ImageDraw",
    "PIL.ImageDraw",
    "matplotlib.pyplot",
    "svgwrite",
    "cairo",
]

SIMPLIFIED_FLAGS = [
    "这里",
    "这个",
    "说明",
    "图像",
    "路径",
]

PROTECTED_IMAGE_KEYWORDS = ["qr", "qrcode", "wechat"]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def warn(message: str) -> None:
    print(f"WARN: {message}")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def check_readme_images() -> None:
    if not README.exists():
        fail("README.md not found")

    text = read_text(README)
    image_paths = re.findall(r"!\[[^\]]*\]\(([^)]+)\)", text)

    for raw in image_paths:
        if raw.startswith(("http://", "https://")):
            continue
        path = ROOT / raw
        if not path.exists():
            fail(f"README references missing image: {raw}")


def check_programmatic_generation_code() -> None:
    current_script = Path(__file__).resolve()
    for path in ROOT.rglob("*.py"):
        if path.resolve() == current_script:
            continue
        text = read_text(path)
        for term in FORBIDDEN_CODE_TERMS:
            if term in text:
                warn(f"Potential programmatic drawing term '{term}' in {path}")


def check_image_provenance_mentions() -> None:
    protocol = ROOT / "docs" / "GENERATION_PROTOCOL.md"
    if not protocol.exists():
        fail("docs/GENERATION_PROTOCOL.md not found")

    protocol_text = read_text(protocol)
    provenance_files = [protocol_text]

    for path in ROOT.rglob("README.md"):
        if "generated" in str(path) or "images" in str(path):
            provenance_files.append(read_text(path))

    provenance_text = "\n".join(provenance_files)

    for img in sorted(ROOT.rglob("*")):
        if not img.is_file() or img.suffix.lower() not in IMAGE_EXTS:
            continue

        rel = str(img.relative_to(ROOT))
        rel_lower = rel.lower()
        if any(keyword in rel_lower for keyword in PROTECTED_IMAGE_KEYWORDS):
            continue

        parent_recorded = any(str(parent).strip(".") in provenance_text for parent in img.parents)
        if rel not in provenance_text and not parent_recorded:
            warn(f"Image has no provenance mention: {rel}")


def check_traditional_chinese_bias() -> None:
    for path in ROOT.rglob("*.md"):
        text = read_text(path)
        for flag in SIMPLIFIED_FLAGS:
            if flag in text:
                warn(f"Possible Simplified Chinese term '{flag}' in {path}")


def main() -> None:
    check_readme_images()
    check_programmatic_generation_code()
    check_image_provenance_mentions()
    check_traditional_chinese_bias()
    print("repo rule checks completed")


if __name__ == "__main__":
    main()
