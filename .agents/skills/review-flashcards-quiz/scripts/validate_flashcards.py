#!/usr/bin/env python3
"""Validate generated flashcard HTML without opening or mutating a browser."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


# Do not flag JavaScript's intentional nullish-coalescing operator (??).
BAD_RENDER_PATTERNS = ("? pulse", "?1", "2?", "reverse ?")


def extract_inline_scripts(html: str) -> list[str]:
    return re.findall(r"<script(?:\s[^>]*)?>([\s\S]*?)</script>", html, re.IGNORECASE)


def validate(path: Path, allow_placeholders: bool) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    try:
        html = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return [f"file not found: {path}"], []
    except UnicodeDecodeError:
        return [f"file is not valid UTF-8: {path}"], []

    if not re.match(r"^\s*<!doctype html>", html, re.IGNORECASE):
        errors.append("missing <!DOCTYPE html> at the beginning")
    if not re.search(r'<meta\s+charset=["\']?UTF-8', html, re.IGNORECASE):
        errors.append("missing UTF-8 meta charset")
    if len(re.findall(r"^const DECK = /\* DECK_DATA \*/$", html, re.MULTILINE)) != 1:
        errors.append("expected exactly one DECK data marker")
    if len(re.findall(r"^/\* /DECK_DATA \*/;$", html, re.MULTILINE)) != 1:
        errors.append("expected exactly one DECK closing marker")
    for required in ("Flashcards", "renderMathInElement", "localStorage", "exportReview"):
        if required not in html:
            errors.append(f"missing required feature marker: {required}")

    placeholders = sorted(set(re.findall(r"\{\{[^}]+\}\}", html)))
    if placeholders and not allow_placeholders:
        errors.append("unresolved placeholders: " + ", ".join(placeholders))
    if "\ufffd" in html:
        errors.append("contains Unicode replacement characters (possible encoding corruption)")
    lowered = html.lower()
    for pattern in BAD_RENDER_PATTERNS:
        if pattern in lowered:
            errors.append(f"contains suspicious rendering-corruption pattern: {pattern!r}")

    scripts = extract_inline_scripts(html)
    if not scripts:
        errors.append("no inline application script found")
    elif not placeholders and shutil.which("node"):
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".js", delete=False) as handle:
            handle.write(scripts[-1])
            script_path = Path(handle.name)
        try:
            result = subprocess.run(
                ["node", "--check", str(script_path)],
                capture_output=True,
                text=True,
                encoding="utf-8",
            )
            if result.returncode:
                errors.append("inline JavaScript syntax check failed: " + (result.stderr or result.stdout).strip())
        finally:
            script_path.unlink(missing_ok=True)
    elif not placeholders:
        warnings.append("node is unavailable; JavaScript syntax was not checked")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path, help="generated HTML files or the template")
    parser.add_argument(
        "--allow-placeholders",
        action="store_true",
        help="allow the six JSON placeholders when validating assets/template.html",
    )
    args = parser.parse_args()

    failed = False
    for path in args.paths:
        errors, warnings = validate(path, args.allow_placeholders)
        if errors:
            failed = True
            print(f"FAIL {path}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"PASS {path}")
        for warning in warnings:
            print(f"  warning: {warning}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
