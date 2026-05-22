#!/usr/bin/env python3
"""Convert NotebookLM mind map JSON to a Mermaid mindmap diagram.

Mermaid mindmaps render natively in Notion, GitHub, and any Mermaid-compatible
viewer, so this gives a portable visual without needing the NotebookLM UI.

Usage:
    python3 scripts/mindmap_to_mermaid.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "media" / "mindmap.json"
OUT = ROOT / "media" / "mindmap.mmd"


def sanitize(s: str) -> str:
    # Mermaid mindmap labels: parentheses and brackets cause syntax issues.
    s = s.replace("(", "[").replace(")", "]")
    s = re.sub(r"\s+", " ", s).strip()
    return s


def emit(node: dict, depth: int, out: list[str]) -> None:
    indent = "  " * depth
    label = sanitize(node.get("name", ""))
    out.append(f"{indent}{label}")
    for child in node.get("children", []):
        emit(child, depth + 1, out)


def main() -> int:
    if not SRC.exists():
        print(f"Source not found: {SRC}", file=sys.stderr)
        return 1
    data = json.loads(SRC.read_text(encoding="utf-8"))

    lines = ["mindmap"]
    root_label = sanitize(data.get("name", "Mind Map"))
    lines.append(f"  root(({root_label}))")
    for child in data.get("children", []):
        emit(child, 2, lines)

    body = "\n".join(lines) + "\n"
    OUT.write_text(body, encoding="utf-8")
    node_count = sum(1 for line in lines if line.strip() and not line.startswith("mindmap"))
    print(f"Wrote {OUT} — {node_count} nodes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
