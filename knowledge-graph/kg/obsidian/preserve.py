"""What survives a rebuild of the vault.

The vault is *generated*: every export rewrites every note. That is what makes
it safe to pull upstream changes and rebuild. But two things are yours and
must not be lost:

1. **Your status.** Every lesson note has ``status`` (what the vault shows)
   and ``status_auto`` (what the build computed last time). If you edit
   ``status`` by hand, the two differ, and the next export keeps your value.
   If they are equal you never touched it, so the build may update it.
2. **Your notes.** Everything below the marker line

       %% ── my notes ── %%

   is copied verbatim into the regenerated note. Obsidian renders ``%% %%``
   as a comment, so the marker is invisible in reading view.

Anything inside ``My Notes/`` is never touched at all.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

MARKER = "%% ── my notes ── %%"
_FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
_KV_RE = re.compile(r"^([A-Za-z0-9_]+):\s*(.*)$")


@dataclass
class Preserved:
    status: str | None = None  # a hand-edited status, or None
    notes: str = ""  # text below the marker (without the marker)


def read_preserved(path: Path) -> Preserved:
    """Read an existing note and return the parts to carry over."""
    if not path.is_file():
        return Preserved()
    text = path.read_text(encoding="utf-8")
    out = Preserved()

    m = _FM_RE.match(text)
    if m:
        fm: dict[str, str] = {}
        for line in m.group(1).splitlines():
            kv = _KV_RE.match(line)
            if kv:
                fm[kv.group(1)] = kv.group(2).strip().strip('"\'')
        status, auto = fm.get("status"), fm.get("status_auto")
        if status and status != auto and status.lower() not in {"null", "none", ""}:
            out.status = status

    if MARKER in text:
        out.notes = text.split(MARKER, 1)[1].lstrip("\n").rstrip() + "\n" if text.split(MARKER, 1)[1].strip() else ""
    return out
