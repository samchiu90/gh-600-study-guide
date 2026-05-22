#!/usr/bin/env python3
"""Convert NotebookLM-generated flashcards JSON to an Anki .apkg deck.

Output is a separate deck named 'GH-600 — NotebookLM Cards' so the user can
tell at a glance which are hand-authored (gh-600.apkg) vs. LLM-generated.

Usage:
    python3 scripts/nlm_flashcards_to_anki.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import genanki

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "media" / "notebooklm-flashcards.json"
OUT = ROOT / "media" / "nlm-flashcards.apkg"

DECK_ID = 2005190001
MODEL_ID = 2005190002


def main() -> int:
    if not SRC.exists():
        print(f"Source not found: {SRC}", file=sys.stderr)
        return 1

    data = json.loads(SRC.read_text(encoding="utf-8"))
    cards = data.get("cards", [])
    if not cards:
        print("No cards in source JSON.", file=sys.stderr)
        return 1

    model = genanki.Model(
        MODEL_ID,
        "GH-600 NotebookLM Card",
        fields=[{"name": "Front"}, {"name": "Back"}],
        templates=[
            {
                "name": "Card 1",
                "qfmt": '<div class="q">{{Front}}</div>',
                "afmt": '{{FrontSide}}<hr id="answer"><div class="a">{{Back}}</div>',
            }
        ],
        css=(
            ".card { font-family: -apple-system, BlinkMacSystemFont, sans-serif; "
            "font-size: 18px; text-align: left; color: #1a1a1a; background: #fffef6; "
            "padding: 18px; line-height: 1.55; } "
            ".q { font-weight: 600; margin-bottom: 14px; } "
            ".a { color: #1a1a1a; } "
            "hr#answer { border: none; border-top: 1px solid #ddd; margin: 14px 0; }"
        ),
    )

    deck = genanki.Deck(DECK_ID, "GH-600 — NotebookLM Cards")
    for c in cards:
        note = genanki.Note(
            model=model,
            fields=[c.get("front", ""), c.get("back", "")],
            tags=["GH-600", "NotebookLM-generated"],
        )
        deck.add_note(note)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    genanki.Package(deck).write_to_file(str(OUT))
    print(f"Wrote {OUT} ({len(cards)} cards)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
