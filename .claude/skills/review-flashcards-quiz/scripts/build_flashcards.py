#!/usr/bin/env python3
"""Build a vault flashcard deck from UTF-8 JSON data and the HTML template.

The script deliberately has no third-party dependencies.  It keeps generated
JavaScript data separate from the interaction code so card answers containing
backslashes, quotes, CJK text, or LaTeX are encoded safely.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


SKILL_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TEMPLATE = SKILL_ROOT / "assets" / "template.html"
TOKENS = {
    "topic": "{{TOPIC_NAME_JSON}}",
    "source": "{{SOURCE_NOTE_JSON}}",
    "namespace": "{{STORAGE_NAMESPACE_JSON}}",
    "chapters": "{{CHAPTERS_JSON}}",
    "cards": "{{CARDS_JSON}}",
    "quiz": "{{QUIZ_JSON}}",
}


class DeckError(ValueError):
    """A user-facing deck data or path error."""


def load_json(path: Path, label: str) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise DeckError(f"{label} not found: {path}") from exc
    except UnicodeDecodeError as exc:
        raise DeckError(f"{label} is not UTF-8: {path}") from exc
    except json.JSONDecodeError as exc:
        raise DeckError(f"{label} is invalid JSON ({path}:{exc.lineno}:{exc.colno})") from exc


def as_json_literal(value: Any) -> str:
    """Return a JSON literal safe to place inside an inline script tag."""

    text = json.dumps(value, ensure_ascii=False, separators=(",", ":"))
    # Prevent user-provided content from closing the inline script tag.
    return (
        text.replace("<", r"\u003c")
        .replace(">", r"\u003e")
        .replace("&", r"\u0026")
        .replace("\u2028", r"\u2028")
        .replace("\u2029", r"\u2029")
    )


def validate_namespace(value: str) -> str:
    if not re.fullmatch(r"[a-z0-9][a-z0-9_-]{0,63}", value):
        raise DeckError("namespace must match [a-z0-9][a-z0-9_-]{0,63}, e.g. neutral-atom-qc")
    return value


def validate_deck_data(chapters: Any, cards: Any, quiz: Any) -> None:
    if not isinstance(chapters, dict) or not chapters:
        raise DeckError("chapters.json must be a non-empty object such as {\"1\": \"Qubit algebra\"}")
    chapter_keys = set()
    for key, title in chapters.items():
        key_text = str(key)
        if not key_text.isdigit() or int(key_text) <= 0:
            raise DeckError(f"chapter key must be a positive integer string: {key!r}")
        if not isinstance(title, str) or not title.strip():
            raise DeckError(f"chapter title must be a non-empty string: {key!r}")
        chapter_keys.add(key_text)

    if not isinstance(cards, list) or not cards:
        raise DeckError("cards.json must be a non-empty array")
    card_ids: set[str] = set()
    for index, card in enumerate(cards):
        if not isinstance(card, dict):
            raise DeckError(f"card {index} must be an object")
        for field in ("id", "ch", "diff", "q", "a"):
            if field not in card:
                raise DeckError(f"card {index} is missing required field {field!r}")
        card_id = str(card["id"])
        if not card_id or card_id in card_ids:
            raise DeckError(f"card IDs must be non-empty and unique; duplicate/empty ID at {index}")
        card_ids.add(card_id)
        if str(card["ch"]) not in chapter_keys:
            raise DeckError(f"card {card_id!r} refers to missing chapter {card['ch']!r}")
        if card["diff"] not in (0, 1, False, True):
            raise DeckError(f"card {card_id!r}: diff must be 0 or 1")
        for field in ("q", "a"):
            if not isinstance(card[field], str) or not card[field].strip():
                raise DeckError(f"card {card_id!r}: {field} must be a non-empty string")
        if "source" in card and not isinstance(card["source"], str):
            raise DeckError(f"card {card_id!r}: source must be a string when present")

    if not isinstance(quiz, list):
        raise DeckError("quiz.json must be an array")
    quiz_ids: set[int] = set()
    for index, item in enumerate(quiz):
        if not isinstance(item, dict):
            raise DeckError(f"quiz item {index} must be an object")
        for field in ("id", "ch", "type", "q", "a"):
            if field not in item:
                raise DeckError(f"quiz item {index} is missing required field {field!r}")
        if isinstance(item["id"], bool) or not isinstance(item["id"], int) or item["id"] <= 0:
            raise DeckError(f"quiz item {index}: id must be a positive integer")
        if item["id"] in quiz_ids:
            raise DeckError(f"quiz IDs must be unique; duplicate ID {item['id']}")
        quiz_ids.add(item["id"])
        if str(item["ch"]) not in chapter_keys:
            raise DeckError(f"quiz item {item['id']}: missing chapter {item['ch']!r}")
        if item["type"] not in ("calc", "concept"):
            raise DeckError(f"quiz item {item['id']}: type must be calc or concept")
        for field in ("q", "a"):
            if not isinstance(item[field], str) or not item[field].strip():
                raise DeckError(f"quiz item {item['id']}: {field} must be a non-empty string")
        if "source" in item and not isinstance(item["source"], str):
            raise DeckError(f"quiz item {item['id']}: source must be a string when present")


def ensure_output_is_safe(output: Path) -> None:
    resolved = output.resolve()
    if SKILL_ROOT == resolved or SKILL_ROOT in resolved.parents:
        raise DeckError("output must be outside the skill directory; use Flashcards/<english-name>.html")


def build(args: argparse.Namespace) -> Path:
    template_path = Path(args.template).resolve() if args.template else DEFAULT_TEMPLATE
    output = Path(args.output)
    if output.is_absolute():
        raise DeckError("output must be a vault-relative path, not an absolute path")
    ensure_output_is_safe(output)
    if output.exists() and not args.force:
        raise DeckError(f"refusing to overwrite existing file: {output} (use --force only for an intentional update)")

    try:
        template = template_path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise DeckError(f"template not found: {template_path}") from exc

    chapters = load_json(Path(args.chapters), "chapters.json")
    cards = load_json(Path(args.cards), "cards.json")
    quiz = load_json(Path(args.quiz), "quiz.json")
    validate_deck_data(chapters, cards, quiz)

    namespace = validate_namespace(args.namespace or re.sub(r"[^a-z0-9]+", "-", args.topic.lower()).strip("-") or "flashcards")
    values = {
        "topic": args.topic,
        "source": args.source,
        "namespace": namespace,
        "chapters": chapters,
        "cards": cards,
        "quiz": quiz,
    }
    rendered = template
    for key, token in TOKENS.items():
        if rendered.count(token) != 1:
            raise DeckError(f"template must contain exactly one placeholder: {token}")
        rendered = rendered.replace(token, as_json_literal(values[key]))
    if "{{" in rendered or "}}" in rendered:
        raise DeckError("unresolved {{...}} placeholder remains after rendering")
    if not re.match(r"^\s*<!doctype html>", rendered, re.IGNORECASE):
        raise DeckError("rendered deck must start with <!DOCTYPE html>")

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(rendered, encoding="utf-8", newline="\n")
    return output


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--topic", required=True, help="human-readable deck title")
    parser.add_argument("--source", required=True, help="source notes/materials shown in the footer")
    parser.add_argument("--chapters", required=True, help="UTF-8 JSON object mapping chapter numbers to labels")
    parser.add_argument("--cards", required=True, help="UTF-8 JSON array of flashcards")
    parser.add_argument("--quiz", required=True, help="UTF-8 JSON array of quiz items")
    parser.add_argument("--output", required=True, help="vault-relative output HTML path")
    parser.add_argument("--namespace", help="unique lowercase storage namespace; derived from topic when omitted")
    parser.add_argument("--template", help="optional template path; defaults to this skill's assets/template.html")
    parser.add_argument("--force", action="store_true", help="intentionally overwrite an existing output")
    return parser.parse_args()


def main() -> int:
    try:
        output = build(parse_args())
    except DeckError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(f"Built {output} (UTF-8, single HTML file)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
