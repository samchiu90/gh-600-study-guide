#!/usr/bin/env python3
"""Convert flashcards.md to an importable Anki .apkg deck.

Parses the **Qn.** / **A.** pattern, tracks `## Domain N` headings to tag
each card by exam domain, and writes the deck to media/gh-600.apkg.

Usage:
    python3 scripts/convert_flashcards.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import genanki

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "flashcards.md"
OUT = ROOT / "media" / "gh-600.apkg"

# Stable IDs so re-running produces an updateable deck rather than a duplicate.
DECK_ID = 2005180001
MODEL_ID = 2005180002

DOMAIN_RE = re.compile(r"^##\s+Domain\s+(\d+)\s+—\s+(.+?)\s+\(", re.MULTILINE)
QA_RE = re.compile(
    r"\*\*Q(\d+)\.\*\*\s*(.+?)\n\*\*A\.\*\*\s*(.+?)(?=\n\*\*Q\d+\.\*\*|\n## |\n### |\Z)",
    re.DOTALL,
)

# Light markdown→HTML transforms suited to Anki's renderer.
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
CODE_RE = re.compile(r"`([^`]+)`")
BOLD_RE = re.compile(r"\*\*([^*]+)\*\*")
ITALIC_RE = re.compile(r"(?<!\*)\*([^*\n]+)\*(?!\*)")


def md_to_html(text: str) -> str:
    text = LINK_RE.sub(r'<a href="\2">\1</a>', text)
    text = CODE_RE.sub(r"<code>\1</code>", text)
    text = BOLD_RE.sub(r"<b>\1</b>", text)
    text = ITALIC_RE.sub(r"<i>\1</i>", text)
    text = text.replace("\n", "<br>")
    return text


def parse_cards(text: str):
    domain_at = [(m.start(), m.group(1), m.group(2).strip()) for m in DOMAIN_RE.finditer(text)]

    def domain_for(pos: int):
        cur = ("0", "Cross-cutting")
        for start, num, name in domain_at:
            if start < pos:
                cur = (num, name)
            else:
                break
        return cur

    cards = []
    for m in QA_RE.finditer(text):
        qid = m.group(1)
        q = m.group(2).strip()
        a = m.group(3).strip()
        domain_num, _ = domain_for(m.start())
        tags = ["GH-600", f"Domain-{domain_num}"]
        cards.append((qid, q, a, tags))
    return cards


def build_deck(cards):
    model = genanki.Model(
        MODEL_ID,
        "GH-600 Q&A",
        fields=[
            {"name": "QId"},
            {"name": "Question"},
            {"name": "Answer"},
        ],
        templates=[
            {
                "name": "Card 1",
                "qfmt": '<div class="qid">{{QId}}</div><div class="q">{{Question}}</div>',
                "afmt": '{{FrontSide}}<hr id="answer"><div class="a">{{Answer}}</div>',
            }
        ],
        css=(
            ".card { font-family: -apple-system, BlinkMacSystemFont, sans-serif; "
            "font-size: 18px; text-align: left; color: #1a1a1a; background: #fafafa; "
            "padding: 18px; line-height: 1.55; } "
            ".qid { color: #888; font-size: 12px; margin-bottom: 8px; letter-spacing: 0.5px; } "
            ".q { font-weight: 600; margin-bottom: 14px; } "
            ".a { color: #1a1a1a; } "
            "code { background: #eef; padding: 1px 5px; border-radius: 3px; "
            "font-family: 'SF Mono', Menlo, monospace; font-size: 0.92em; } "
            "b { color: #0b3a82; } "
            "hr#answer { border: none; border-top: 1px solid #ccc; margin: 14px 0; }"
        ),
    )

    deck = genanki.Deck(DECK_ID, "GH-600 — Agentic AI Developer")
    for qid, q, a, tags in cards:
        note = genanki.Note(
            model=model,
            fields=[f"Q{qid}", md_to_html(q), md_to_html(a)],
            tags=tags,
        )
        deck.add_note(note)
    return deck


def main():
    if not SRC.exists():
        print(f"Source not found: {SRC}", file=sys.stderr)
        return 1

    text = SRC.read_text(encoding="utf-8")
    cards = parse_cards(text)
    if not cards:
        print("No cards parsed — check the Qn./A. pattern.", file=sys.stderr)
        return 1

    print(f"Parsed {len(cards)} cards.")
    by_domain = {}
    for _qid, _q, _a, tags in cards:
        for t in tags:
            if t.startswith("Domain-"):
                by_domain[t] = by_domain.get(t, 0) + 1
    for d in sorted(by_domain):
        print(f"  {d}: {by_domain[d]} cards")

    deck = build_deck(cards)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    genanki.Package(deck).write_to_file(str(OUT))
    print(f"Wrote {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
