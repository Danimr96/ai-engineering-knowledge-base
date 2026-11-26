"""Small, dependency-free helpers for the markdown dialect used upstream.

Why this module exists
----------------------
The curriculum is written in plain markdown with a few conventions (a bold
field header, ``## `` sections, pipe tables, link lists, and YAML-ish
frontmatter on artifact files). A full markdown parser would be overkill and
would hide the exact rules we rely on. These functions are the rules, written
out, with the quirks we found in the real files handled explicitly.

Every function takes text (or a list of lines) and returns plain Python data.
They never touch the filesystem, which makes them trivial to unit test.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any

# --------------------------------------------------------------------------
# Lesson header
# --------------------------------------------------------------------------

_H1_RE = re.compile(r"^#\s+(.+?)\s*$")
_HOOK_RE = re.compile(r"^>\s?(.*)$")
# ``**Type:** Build`` -> key "Type", value "Build". The key may contain spaces.
_FIELD_RE = re.compile(r"^\*\*([A-Za-z][A-Za-z ]*?):\*\*\s*(.*?)\s*$")


@dataclass
class LessonHeader:
    """The bold-field block at the top of every ``docs/en.md``."""

    title: str | None = None
    hook: str | None = None
    fields: dict[str, str] = field(default_factory=dict)
    # Line numbers (1-based) so edges built from a field can cite it.
    field_lines: dict[str, int] = field(default_factory=dict)
    title_line: int | None = None


def parse_lesson_header(text: str) -> LessonHeader:
    """Read the H1, the ``>`` hook and the ``**Field:** value`` lines.

    We stop at the first ``## `` heading: fields after that belong to the body.
    The hook is the first blockquote line after the H1 (the second blockquote
    line, if any, is ignored because it is prose).
    """
    header = LessonHeader()
    for lineno, raw in enumerate(text.splitlines(), start=1):
        line = raw.rstrip()
        if line.startswith("## "):
            break
        if header.title is None:
            m = _H1_RE.match(line)
            if m:
                header.title = m.group(1)
                header.title_line = lineno
            continue
        if header.hook is None:
            m = _HOOK_RE.match(line)
            if m and m.group(1).strip():
                header.hook = m.group(1).strip()
                continue
        m = _FIELD_RE.match(line)
        if m:
            key = m.group(1).strip()
            if key not in header.fields:  # first occurrence wins
                header.fields[key] = m.group(2).strip()
                header.field_lines[key] = lineno
    return header


# --------------------------------------------------------------------------
# Sections
# --------------------------------------------------------------------------


@dataclass
class Section:
    heading: str
    level: int
    start_line: int  # line of the heading (1-based)
    lines: list[str]  # body lines, without the heading


_HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
_FENCE_RE = re.compile(r"^(```+|~~~+)")


def split_sections(text: str) -> list[Section]:
    """Split a document by ATX headings, ignoring headings inside code fences.

    Fenced code blocks matter: lesson bodies contain ``# comment`` lines inside
    Python snippets that would otherwise look like H1s.
    """
    sections: list[Section] = []
    current: Section | None = None
    in_fence: str | None = None
    for lineno, line in enumerate(text.splitlines(), start=1):
        fm = _FENCE_RE.match(line)
        if fm:
            marker = fm.group(1)[0] * 3
            if in_fence is None:
                in_fence = marker
            elif line.startswith(in_fence):
                in_fence = None
        if in_fence is None:
            hm = _HEADING_RE.match(line)
            if hm:
                current = Section(heading=hm.group(2).strip(), level=len(hm.group(1)), start_line=lineno, lines=[])
                sections.append(current)
                continue
        if current is not None:
            current.lines.append(line)
    return sections


def find_section(sections: list[Section], heading: str, level: int | None = 2) -> Section | None:
    """First section whose heading matches case-insensitively."""
    target = heading.strip().casefold()
    for s in sections:
        if (level is None or s.level == level) and s.heading.casefold() == target:
            return s
    return None


# --------------------------------------------------------------------------
# Tables
# --------------------------------------------------------------------------

# A pipe that is NOT preceded by a backslash. ``\|`` is an escaped pipe inside
# a cell (52 of them upstream, e.g. ``P(token_n \| token_0)``). A naive
# ``split('|')`` would silently shift every column after it.
_CELL_SPLIT_RE = re.compile(r"(?<!\\)\|")
_SEPARATOR_ROW_RE = re.compile(r"^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$")


def split_table_row(line: str) -> list[str]:
    """``'| a | b \\| c |'`` -> ``['a', 'b | c']``."""
    stripped = line.strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|") and not stripped.endswith("\\|"):
        stripped = stripped[:-1]
    return [cell.strip().replace("\\|", "|") for cell in _CELL_SPLIT_RE.split(stripped)]


@dataclass
class TableRow:
    cells: list[str]
    line: int


@dataclass
class Table:
    header: list[str]
    rows: list[TableRow]


def parse_tables(lines: list[str], first_line_no: int = 1) -> list[Table]:
    """Find every pipe table in a block of lines.

    A table is: a header row, a separator row (``|---|---|``), then rows until
    a line that is not a table row. Rows with a different cell count than the
    header are kept (padded) rather than dropped, so a stray cell does not
    silently delete a term.
    """
    tables: list[Table] = []
    i = 0
    n = len(lines)
    while i < n - 1:
        line = lines[i]
        if "|" in line and _SEPARATOR_ROW_RE.match(lines[i + 1]):
            header = split_table_row(line)
            rows: list[TableRow] = []
            j = i + 2
            while j < n and lines[j].strip().startswith("|"):
                cells = split_table_row(lines[j])
                if len(cells) < len(header):
                    cells = cells + [""] * (len(header) - len(cells))
                rows.append(TableRow(cells=cells, line=first_line_no + j))
                j += 1
            tables.append(Table(header=header, rows=rows))
            i = j
        else:
            i += 1
    return tables


# --------------------------------------------------------------------------
# Links
# --------------------------------------------------------------------------

_LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")


@dataclass
class Link:
    text: str
    url: str
    line: int
    # Text after the link on the same line, e.g. " — the MQA paper." Kept
    # because it is the human explanation of why the resource is cited.
    trailing: str = ""


def find_links(lines: list[str], first_line_no: int = 1) -> list[Link]:
    links: list[Link] = []
    for offset, line in enumerate(lines):
        for m in _LINK_RE.finditer(line):
            trailing = line[m.end() :].strip()
            trailing = re.sub(r"^[\s—–\-:.,]+", "", trailing).strip()
            links.append(Link(text=m.group(1).strip(), url=m.group(2).strip(), line=first_line_no + offset, trailing=trailing))
    return links


def strip_markdown(text: str) -> str:
    """Remove inline markdown decoration: ``**bold**``, ``*em*``, `` `code` ``, links.

    Underscores are only emphasis at a word boundary; ``kv_cache`` keeps its
    underscore so it can be normalised like ``kv-cache`` later.
    """
    text = _LINK_RE.sub(lambda m: m.group(1), text)
    text = re.sub(r"[`*]{1,3}", "", text)
    text = re.sub(r"(?<![A-Za-z0-9])_+|_+(?![A-Za-z0-9])", "", text)
    return re.sub(r"\s+", " ", text).strip()


# --------------------------------------------------------------------------
# Frontmatter (the YAML subset used by outputs/*.md)
# --------------------------------------------------------------------------


def parse_frontmatter(text: str) -> dict[str, Any]:
    """Parse the ``---`` block at the top of a file.

    Supports exactly what upstream artifacts use: ``key: value``, quoted
    strings, and inline lists ``[a, b, c]``. Nested YAML is out of scope; a
    real YAML parser would be a dependency for four keys.
    (Modelled on ``ai-engineering-from-scratch/scripts/_lib.py``.)
    """
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    meta: dict[str, Any] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" not in line or line.startswith(" "):
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            items = [v.strip().strip("'\"") for v in value[1:-1].split(",")]
            meta[key] = [v for v in items if v]
        else:
            meta[key] = value.strip("'\"")
    return meta


# --------------------------------------------------------------------------
# Small text utilities used by several extractors
# --------------------------------------------------------------------------


def slugify(text: str) -> str:
    """``'Math & training'`` -> ``'math-and-training'``. Stable, ASCII, lowercase."""
    text = text.replace("&", " and ")
    text = re.sub(r"[^A-Za-z0-9]+", "-", text).strip("-").lower()
    return re.sub(r"-{2,}", "-", text)


def parse_minutes(value: str) -> int | None:
    """``'~75 minutes'`` -> 75, ``'30 hours'`` -> 1800, ``'~90 min'`` -> 90."""
    m = re.search(r"(\d+(?:\.\d+)?)\s*(hours?|hrs?|h|minutes?|mins?|m)?", value)
    if not m:
        return None
    qty = float(m.group(1))
    unit = (m.group(2) or "minutes").lower()
    if unit.startswith("h"):
        qty *= 60
    return int(round(qty))
