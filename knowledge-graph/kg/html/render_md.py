"""Markdown -> HTML, for the subset of markdown the lessons use.

Why not a library
-----------------
The whole project is standard library only, and the lessons use a small,
regular dialect: ATX headings, paragraphs, nested lists, block quotes, pipe
tables, fenced code, links, images and emphasis. Two fence languages are
special: ``mermaid`` (a diagram the browser renders) and ``figure`` (the name
of an interactive widget from the curriculum's own site).

Safety rule
-----------
Every character of lesson text is HTML-escaped. The only tags in the output
are the ones this module writes. Lessons talk about tokens such as ``<s>`` or
``<image>``; they must show up as text, never as markup. Link targets are
limited to http, https and mailto, or to whatever ``resolve_link`` returns.

How it works
------------
Two passes, like most markdown renderers:

1. **Blocks** (:meth:`Renderer.blocks`): walk the lines, decide which block
   starts at the current line, consume it, recurse for containers (lists and
   block quotes hold blocks themselves).
2. **Inline** (:meth:`Renderer.inline`): inside a paragraph, heading or cell,
   pull out code spans, images and links first (their content must not be
   touched by the emphasis rules), escape what is left, apply emphasis, then
   put the protected pieces back.
"""

from __future__ import annotations

import html
import re
from dataclasses import dataclass, field
from typing import Callable

from kg.markdown import split_table_row

# ---- block-level patterns ---------------------------------------------------

_FENCE_RE = re.compile(r"^(\s*)(`{3,}|~{3,})\s*([^\s`]*)")
_HEADING_RE = re.compile(r"^\s{0,3}(#{1,6})\s+(.*?)\s*#*\s*$")
_HR_RE = re.compile(r"^\s{0,3}([-*_])(\s*\1){2,}\s*$")
_LIST_RE = re.compile(r"^(\s*)([-*+]|\d{1,9}[.)])(\s+)(.*)$")
_QUOTE_RE = re.compile(r"^\s{0,3}>\s?(.*)$")
_TABLE_SEP_RE = re.compile(r"^\s*\|?\s*:?-{1,}:?\s*(\|\s*:?-{1,}:?\s*)*\|?\s*$")
_CALLOUT_RE = re.compile(r"^\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*$", re.I)
_META_RE = re.compile(r"^\*\*[A-Za-z][A-Za-z /-]*:\*\*")

# ---- inline patterns --------------------------------------------------------

_CODE_SPAN_RE = re.compile(r"(`+)(.+?)\1(?!`)", re.S)
_BACKSLASH_RE = re.compile(r"\\([\\`*_{}\[\]()#+\-.!|<>~$])")
_LINK_TARGET = r"\(\s*(<[^>]*>|[^\s()]*(?:\([^\s()]*\)[^\s()]*)*)(?:\s+\"([^\"]*)\")?\s*\)"
_IMAGE_RE = re.compile(r"!\[([^\]]*)\]" + _LINK_TARGET)
_LINK_RE = re.compile(r"\[((?:[^\[\]]|\[[^\[\]]*\])*)\]" + _LINK_TARGET)
_AUTOLINK_RE = re.compile(r"<(https?://[^\s<>]+)>")
_BARE_URL_RE = re.compile(r"(?<![\w\"'=/>])(https?://[^\s<]+[^\s<.,;:!?)\]'\"])")
_SAFE_URL_RE = re.compile(r"^(https?://|mailto:)", re.I)

_EMPHASIS = [
    (re.compile(r"\*\*\*(?=\S)(.+?)(?<=\S)\*\*\*", re.S), r"<strong><em>\1</em></strong>"),
    (re.compile(r"\*\*(?=\S)(.+?)(?<=\S)\*\*", re.S), r"<strong>\1</strong>"),
    (re.compile(r"(?<!\w)__(?=\S)(.+?)(?<=\S)__(?!\w)", re.S), r"<strong>\1</strong>"),
    (re.compile(r"(?<![\w*])\*(?=[^\s*])(.+?)(?<=[^\s*])\*(?![\w*])", re.S), r"<em>\1</em>"),
    (re.compile(r"(?<!\w)_(?=[^\s_])(.+?)(?<=[^\s_])_(?!\w)", re.S), r"<em>\1</em>"),
    (re.compile(r"~~(?=\S)(.+?)(?<=\S)~~", re.S), r"<del>\1</del>"),
]

# Placeholders for protected inline pieces. ``\x00`` cannot occur in a lesson.
_STASH_RE = re.compile("\x00(\\d+)\x00")


def esc(text: str) -> str:
    """HTML-escape text, including quotes (safe inside attributes too)."""
    return html.escape(text, quote=True)


def slugify_heading(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug or "section"


def strip_lesson_header(text: str) -> str:
    """Drop the title, the hook quote and the ``**Type:**`` metadata lines.

    The page shows those as structured header elements built from the graph,
    so repeating them at the top of the text would be noise.
    """
    lines = text.splitlines()
    i, seen_title, seen_other = 0, False, False
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
        elif not seen_title and re.match(r"^#\s+", line):
            seen_title = True
            i += 1
        elif not seen_other and line.lstrip().startswith(">"):
            i += 1
        elif _META_RE.match(line.strip()):
            seen_other = True
            i += 1
        else:
            break
    return "\n".join(lines[i:])


@dataclass
class Rendered:
    """Result of rendering one document."""

    html: str
    toc: list[tuple[int, str, str]] = field(default_factory=list)  # (level, id, text)
    figures: list[str] = field(default_factory=list)  # names in ``figure`` fences
    has_mermaid: bool = False


class Renderer:
    """Renders one document. Create a new instance per document.

    ``resolve_link(url)`` maps a relative link to a site URL, or returns
    ``None`` to render the link text without a link. ``resolve_image(src)``
    does the same for images (typically returning a ``data:`` URI).
    """

    def __init__(
        self,
        *,
        resolve_link: Callable[[str], str | None] | None = None,
        resolve_image: Callable[[str], str | None] | None = None,
    ) -> None:
        self.resolve_link = resolve_link or (lambda url: None)
        self.resolve_image = resolve_image or (lambda src: None)
        self.toc: list[tuple[int, str, str]] = []
        self.figures: list[str] = []
        self.has_mermaid = False
        self._ids: dict[str, int] = {}

    # ---- public -------------------------------------------------------
    def render(self, text: str) -> Rendered:
        body = self.blocks(text.replace("\r\n", "\n").expandtabs(4).split("\n"))
        return Rendered(html=body, toc=self.toc, figures=self.figures, has_mermaid=self.has_mermaid)

    # ---- blocks -------------------------------------------------------
    def blocks(self, lines: list[str]) -> str:
        out: list[str] = []
        i, n = 0, len(lines)
        while i < n:
            line = lines[i]
            if not line.strip():
                i += 1
                continue
            fence = _FENCE_RE.match(line)
            if fence:
                i = self._fence(lines, i, fence, out)
                continue
            heading = _HEADING_RE.match(line)
            if heading:
                out.append(self._heading(len(heading.group(1)), heading.group(2)))
                i += 1
                continue
            if _HR_RE.match(line):
                out.append("<hr>")
                i += 1
                continue
            if _QUOTE_RE.match(line):
                i = self._quote(lines, i, out)
                continue
            if _LIST_RE.match(line):
                i = self._list(lines, i, out)
                continue
            if "|" in line and i + 1 < n and "-" in lines[i + 1] and _TABLE_SEP_RE.match(lines[i + 1]):
                i = self._table(lines, i, out)
                continue
            i = self._paragraph(lines, i, out)
        return "\n".join(out)

    def _starts_block(self, lines: list[str], i: int) -> bool:
        """Does a new block start at line ``i`` (which ends a paragraph)?"""
        line = lines[i]
        if _FENCE_RE.match(line) or _HEADING_RE.match(line) or _HR_RE.match(line):
            return True
        if _QUOTE_RE.match(line) or _LIST_RE.match(line):
            return True
        return "|" in line and i + 1 < len(lines) and "-" in lines[i + 1] and bool(_TABLE_SEP_RE.match(lines[i + 1]))

    def _fence(self, lines: list[str], i: int, m: re.Match[str], out: list[str]) -> int:
        indent, marker, lang = len(m.group(1)), m.group(2), m.group(3).lower()
        body: list[str] = []
        i += 1
        while i < len(lines):
            stripped = lines[i].strip()
            # A closing fence uses the same character, is at least as long as
            # the opening one, and has nothing after it.
            if stripped.startswith(marker) and set(stripped) == {marker[0]}:
                i += 1
                break
            body.append(lines[i][indent:] if lines[i][:indent].strip() == "" else lines[i])
            i += 1
        code = "\n".join(body)
        if lang == "mermaid":
            self.has_mermaid = True
            out.append(f'<div class="diagram"><pre class="mermaid-src">{esc(code)}</pre></div>')
        elif lang == "figure":
            spec = code.strip()
            if spec:
                self.figures.append(spec.split()[0])
                out.append(f'<div class="lesson-figure" data-figure="{esc(spec)}"></div>')
        else:
            attr = f' data-lang="{esc(lang)}"' if lang else ""
            out.append(f'<pre class="code"{attr}><code>{esc(code)}</code></pre>')
        return i

    def _heading(self, level: int, text: str) -> str:
        plain = re.sub(r"[`*_]", "", text)
        base = slugify_heading(plain)
        count = self._ids.get(base, 0)
        self._ids[base] = count + 1
        anchor = base if count == 0 else f"{base}-{count + 1}"
        level = max(2, level)  # the page title is the only <h1>
        if level <= 3:
            self.toc.append((level, anchor, plain))
        return f'<h{level} id="{anchor}">{self.inline(text)}</h{level}>'

    def _quote(self, lines: list[str], i: int, out: list[str]) -> int:
        inner: list[str] = []
        while i < len(lines):
            m = _QUOTE_RE.match(lines[i])
            if m:
                inner.append(m.group(1))
            elif lines[i].strip() and inner and inner[-1].strip() and not self._starts_block(lines, i):
                inner.append(lines[i])  # lazy continuation of the quoted paragraph
            else:
                break
            i += 1
        callout = _CALLOUT_RE.match(inner[0].strip()) if inner else None
        if callout:
            kind = callout.group(1).lower()
            out.append(
                f'<blockquote class="callout callout-{kind}"><p class="callout-label">{kind.capitalize()}</p>'
                f"{self.blocks(inner[1:])}</blockquote>"
            )
        else:
            out.append(f"<blockquote>{self.blocks(inner)}</blockquote>")
        return i

    def _list(self, lines: list[str], i: int, out: list[str]) -> int:
        first = _LIST_RE.match(lines[i])
        assert first
        base_indent = len(first.group(1))
        ordered = first.group(2)[0].isdigit()
        start = int(first.group(2)[:-1]) if ordered else 1
        items: list[list[str]] = []
        loose = False
        n = len(lines)
        while i < n:
            m = _LIST_RE.match(lines[i])
            if not (m and len(m.group(1)) == base_indent and m.group(2)[0].isdigit() == ordered):
                break
            content_indent = base_indent + len(m.group(2)) + len(m.group(3))
            item = [m.group(4)]
            i += 1
            while i < n:
                line = lines[i]
                if not line.strip():
                    # A blank line stays in the item only if indented content follows.
                    j = i
                    while j < n and not lines[j].strip():
                        j += 1
                    if j < n and _indent(lines[j]) > base_indent and not _is_sibling(lines[j], base_indent):
                        item.extend([""] * (j - i))
                        i = j
                        continue
                    if j < n and _is_sibling(lines[j], base_indent, ordered):
                        loose = True
                        i = j
                    break
                if _is_sibling(line, base_indent):
                    break
                if _indent(line) > base_indent:
                    item.append(line[min(content_indent, _indent(line)):])
                elif self._starts_block(lines, i):
                    break
                else:
                    item.append(line.strip())  # lazy continuation
                i += 1
            items.append(item)
        tag = "ol" if ordered else "ul"
        attr = f' start="{start}"' if ordered and start != 1 else ""
        out.append(f"<{tag}{attr}>")
        for item in items:
            body = self.blocks(item)
            if not loose and body.startswith("<p>") and body.count("<p>") == 1:
                body = body.replace("<p>", "", 1).replace("</p>", "", 1)
            body = re.sub(r"^(<p>)?\[ \] ", r"\1&#9744; ", body)
            body = re.sub(r"^(<p>)?\[[xX]\] ", r"\1&#9745; ", body)
            out.append(f"<li>{body}</li>")
        out.append(f"</{tag}>")
        return i

    def _table(self, lines: list[str], i: int, out: list[str]) -> int:
        header = split_table_row(lines[i])
        aligns = []
        for cell in split_table_row(lines[i + 1]):
            left, right = cell.startswith(":"), cell.endswith(":")
            aligns.append("center" if left and right else "right" if right else "")
        i += 2
        rows: list[list[str]] = []
        while i < len(lines) and "|" in lines[i] and lines[i].strip():
            rows.append(split_table_row(lines[i]))
            i += 1

        def cell(tag: str, text: str, col: int) -> str:
            align = aligns[col] if col < len(aligns) else ""
            attr = f' class="al-{align}"' if align else ""
            return f"<{tag}{attr}>{self.inline(text)}</{tag}>"

        head = "".join(cell("th", text, c) for c, text in enumerate(header))
        body = "".join(
            "<tr>" + "".join(cell("td", text, c) for c, text in enumerate(row)) + "</tr>" for row in rows
        )
        out.append(f'<div class="table-wrap"><table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>')
        return i

    def _paragraph(self, lines: list[str], i: int, out: list[str]) -> int:
        para = [lines[i].strip()]
        raw = [lines[i]]
        i += 1
        while i < len(lines) and lines[i].strip() and not self._starts_block(lines, i):
            para.append(lines[i].strip())
            raw.append(lines[i])
            i += 1
        # A line break is kept when the author asked for one (two trailing
        # spaces or a backslash) or when consecutive lines are ``**Key:** value``.
        joined = para[0]
        for k in range(1, len(para)):
            hard = raw[k - 1].endswith("  ") or raw[k - 1].endswith("\\")
            meta = bool(_META_RE.match(para[k - 1]) and _META_RE.match(para[k]))
            joined = joined.rstrip("\\") + ("\x01" if hard or meta else "\n") + para[k]
        out.append("<p>" + self.inline(joined).replace("\x01", "<br>") + "</p>")
        return i

    # ---- inline -------------------------------------------------------
    def inline(self, text: str, _stash: list[str] | None = None) -> str:
        # A link label is rendered by a nested call. It may contain placeholders
        # made by the outer call (a code span inside a link), so both calls
        # share one stash and only the outermost puts the pieces back.
        nested = _stash is not None
        stash: list[str] = _stash if _stash is not None else []

        def keep(fragment: str) -> str:
            stash.append(fragment)
            return f"\x00{len(stash) - 1}\x00"

        def code_span(m: re.Match[str]) -> str:
            return keep(f"<code>{esc(m.group(2).strip() or m.group(2))}</code>")

        def image(m: re.Match[str]) -> str:
            alt, src = m.group(1), m.group(2).strip("<>")
            resolved = src if _SAFE_URL_RE.match(src) else self.resolve_image(src)
            if not resolved:
                return keep(f'<span class="missing-image">[image: {esc(alt or src)}]</span>')
            return keep(f'<img src="{esc(resolved)}" alt="{esc(alt)}" loading="lazy">')

        def link(m: re.Match[str]) -> str:
            label = self.inline(m.group(1), stash)
            url = m.group(2).strip("<>")
            if _SAFE_URL_RE.match(url):
                return keep(f'<a href="{esc(url)}" target="_blank" rel="noopener">{label}</a>')
            if url.startswith("#") and len(url) > 1:
                return keep(f'<a class="anchor-link" data-anchor="{esc(url[1:])}" tabindex="0">{label}</a>')
            resolved = self.resolve_link(url)
            return keep(f'<a href="{esc(resolved)}">{label}</a>' if resolved else label)

        def autolink(m: re.Match[str]) -> str:
            url = m.group(1)
            return keep(f'<a href="{esc(url)}" target="_blank" rel="noopener">{esc(url)}</a>')

        text = _CODE_SPAN_RE.sub(code_span, text)
        text = _BACKSLASH_RE.sub(lambda m: keep(esc(m.group(1))), text)
        text = _IMAGE_RE.sub(image, text)
        text = _LINK_RE.sub(link, text)
        text = _AUTOLINK_RE.sub(autolink, text)
        text = esc(text)
        text = re.sub(r"&lt;br\s*/?&gt;", "<br>", text)
        text = _BARE_URL_RE.sub(
            lambda m: keep(f'<a href="{m.group(1)}" target="_blank" rel="noopener">{m.group(1)}</a>'), text
        )
        for pattern, replacement in _EMPHASIS:
            text = pattern.sub(replacement, text)
        if nested:
            return text
        # Put protected pieces back. A stashed link holds the placeholders of
        # its label, so repeat until none are left.
        while _STASH_RE.search(text):
            text = _STASH_RE.sub(lambda m: stash[int(m.group(1))], text)
        return text


def _indent(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def _is_sibling(line: str, base_indent: int, ordered: bool | None = None) -> bool:
    """Is ``line`` a list item at the same level as the list being read?"""
    m = _LIST_RE.match(line)
    if not m or len(m.group(1)) != base_indent:
        return False
    return ordered is None or m.group(2)[0].isdigit() == ordered


def render_markdown(
    text: str,
    *,
    resolve_link: Callable[[str], str | None] | None = None,
    resolve_image: Callable[[str], str | None] | None = None,
) -> Rendered:
    """Render one markdown document. See :class:`Renderer`."""
    return Renderer(resolve_link=resolve_link, resolve_image=resolve_image).render(text)
