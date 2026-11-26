"""One lesson folder -> the payload its page loads on demand.

A lesson page is the heaviest thing on the site (text, code, quiz, reusable
prompts), and there are hundreds of them, so none of it is in the start-up
payload. Each lesson gets its own small file; the page loads it the first
time the lesson is opened.

What a payload holds
--------------------
``html``       the lesson text, rendered by :mod:`kg.html.render_md`
``toc``        its headings, for the "on this page" list
``code``       the files in ``code/`` (text only, size-capped)
``quiz``       ``quiz.json`` as written upstream, after a shape check
``artifacts``  the prompts, skills and agents the lesson ships, verbatim
``figures``    which figure scripts the page must load for this lesson
``mermaid``    whether the text has diagrams (so mermaid loads only if needed)

Links between lessons
---------------------
Lesson texts link to each other with relative file paths
(``../../07-transformers/02-self-attention/``). Those are resolved against
the lesson's own folder and mapped to site routes; a link to a file the site
does not have becomes plain text rather than a dead link.
"""

from __future__ import annotations

import base64
import json
import posixpath
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urlsplit

from kg.html.render_md import render_markdown, strip_lesson_header
from kg.model import KnowledgeGraph, Node
from kg.paths import Paths

MAX_CODE_FILES = 8
MAX_CODE_BYTES = 60_000
MAX_ARTIFACT_BYTES = 40_000
MAX_IMAGE_BYTES = 400_000

# Extension -> language name used for highlighting in the page.
CODE_LANGS = {
    ".py": "python", ".ts": "typescript", ".js": "javascript", ".rs": "rust", ".jl": "julia",
    ".sh": "bash", ".json": "json", ".yml": "yaml", ".yaml": "yaml", ".toml": "toml", ".md": "markdown",
}
IMAGE_MIME = {".svg": "image/svg+xml", ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".gif": "image/gif"}

_PHASE_DIR_RE = re.compile(r"^(\d+)-")


@dataclass
class FigureIndex:
    """Which script file defines each interactive figure.

    The curriculum's site registers figures by name from ``figures*.js``
    files. A lesson only says ``figure: kv-cache``; this index answers
    "which files must be loaded for that name". A file *provides* a figure
    when it contains the quoted name (the same rule the upstream build uses).
    """

    runtime: Path | None
    sources: dict[str, str]  # file name -> source text, in load order

    @classmethod
    def scan(cls, paths: Paths) -> "FigureIndex":
        site = paths.upstream / "site"
        runtime = site / "lesson-figures.js"
        if not runtime.is_file():
            return cls(runtime=None, sources={})
        files = sorted(site.glob("figures*.js"), key=lambda p: (p.name != "figures.js", p.name))
        return cls(runtime=runtime, sources={p.name: p.read_text(encoding="utf-8") for p in files})

    def providers(self, names: list[str]) -> list[str]:
        if self.runtime is None:
            return []
        wanted = [re.compile("['\"]" + re.escape(name) + "['\"]") for name in dict.fromkeys(names)]
        return [fname for fname, src in self.sources.items() if any(rx.search(src) for rx in wanted)]


class LinkResolver:
    """Maps a relative link inside a lesson text to a site route."""

    def __init__(self, g: KnowledgeGraph, paths: Paths) -> None:
        self.paths = paths
        self.lesson_by_path = {n.attrs["path"]: n.attrs["ref"] for n in g.nodes_of_type("lesson") if n.attrs.get("path")}
        self.phase_by_path = {n.attrs["path"]: n.attrs["num"] for n in g.nodes_of_type("phase") if n.attrs.get("path")}
        self.glossary = paths.rel(paths.upstream / "glossary")

    def target(self, doc_dir: str, url: str) -> str | None:
        """``doc_dir`` and the result are POSIX paths relative to the root."""
        path = unquote(urlsplit(url).path)
        if not path:
            return None
        return posixpath.normpath(posixpath.join(doc_dir, path))

    def link(self, doc_dir: str, url: str) -> str | None:
        target = self.target(doc_dir, url)
        if target is None:
            return None
        # Longest match first: a lesson folder lives inside a phase folder.
        probe = target
        while probe and probe != ".":
            if probe in self.lesson_by_path:
                return f"#/lesson/{self.lesson_by_path[probe]}"
            if probe in self.phase_by_path:
                return f"#/phase/{self.phase_by_path[probe]}"
            probe = posixpath.dirname(probe)
        if target.startswith(self.glossary):
            return "#/concepts"
        return None

    def image(self, doc_dir: str, src: str) -> str | None:
        """Inline a local image as a ``data:`` URI so the site stays self-contained."""
        target = self.target(doc_dir, src)
        if target is None:
            return None
        file = self.paths.root / target
        mime = IMAGE_MIME.get(file.suffix.lower())
        try:
            # Never read outside the curriculum, whatever a lesson links to.
            file.resolve().relative_to(self.paths.upstream.resolve())
        except ValueError:
            return None
        if not mime or not file.is_file() or file.stat().st_size > MAX_IMAGE_BYTES:
            return None
        return f"data:{mime};base64,{base64.b64encode(file.read_bytes()).decode('ascii')}"


def _read_text(path: Path, limit: int) -> tuple[str, bool] | None:
    """File content as text, cut at ``limit`` bytes. ``None`` for binary files."""
    try:
        raw = path.read_bytes()
    except OSError:
        return None
    if b"\x00" in raw[:4096]:
        return None
    truncated = len(raw) > limit
    return raw[:limit].decode("utf-8", errors="replace"), truncated


def _code_files(lesson_dir: Path) -> list[dict[str, Any]]:
    code_dir = lesson_dir / "code"
    if not code_dir.is_dir():
        return []
    files = [
        p for p in code_dir.rglob("*")
        if p.is_file() and p.suffix.lower() in CODE_LANGS and "__pycache__" not in p.parts and "node_modules" not in p.parts
    ]
    # The entry points first, then the rest; tests and nested files last.
    files.sort(key=lambda p: (len(p.relative_to(code_dir).parts), not p.stem.startswith("main"), p.suffix != ".py", p.name))
    out = []
    for p in files[:MAX_CODE_FILES]:
        got = _read_text(p, MAX_CODE_BYTES)
        if got is None:
            continue
        text, truncated = got
        out.append({
            "name": p.relative_to(code_dir).as_posix(),
            "lang": CODE_LANGS[p.suffix.lower()],
            "text": text,
            **({"truncated": True} if truncated else {}),
        })
    if len(files) > MAX_CODE_FILES and out:
        out[-1]["more"] = len(files) - MAX_CODE_FILES
    return out


def _quiz(lesson_dir: Path) -> list[dict[str, Any]]:
    path = lesson_dir / "quiz.json"
    if not path.is_file():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return []
    items = data if isinstance(data, list) else data.get("questions", []) if isinstance(data, dict) else []
    out = []
    for q in items:
        if not isinstance(q, dict):
            continue
        options, correct = q.get("options"), q.get("correct")
        if not (isinstance(q.get("question"), str) and isinstance(options, list) and isinstance(correct, int)):
            continue
        if not 0 <= correct < len(options):
            continue
        out.append({
            "q": q["question"],
            "options": [str(o) for o in options],
            "correct": correct,
            "why": str(q.get("explanation") or ""),
            "stage": str(q.get("stage") or ""),
        })
    return out


def _artifacts(g: KnowledgeGraph, paths: Paths, lesson: Node) -> list[dict[str, Any]]:
    out = []
    for edge in g.out_edges(lesson.id, "SHIPS"):
        art = g.get(edge.dst)
        if art is None or not art.attrs.get("path"):
            continue
        file = paths.root / art.attrs["path"]
        if file.is_dir():
            file = file / "SKILL.md"
        got = _read_text(file, MAX_ARTIFACT_BYTES) if file.is_file() else None
        if got is None:
            continue
        out.append({"id": art.id, "name": art.attrs.get("name") or art.label, "kind": art.attrs.get("kind") or "", "text": got[0]})
    return out


def build_lesson(g: KnowledgeGraph, paths: Paths, lesson: Node, links: LinkResolver, figures: FigureIndex) -> dict[str, Any] | None:
    """The on-demand payload for one lesson, or ``None`` if it has no text."""
    doc_rel = lesson.attrs.get("doc_path")
    if not doc_rel:
        return None
    doc = paths.root / doc_rel
    if not doc.is_file():
        return None
    doc_dir = posixpath.dirname(doc_rel)
    rendered = render_markdown(
        strip_lesson_header(doc.read_text(encoding="utf-8")),
        resolve_link=lambda url: links.link(doc_dir, url),
        resolve_image=lambda src: links.image(doc_dir, src),
    )
    lesson_dir = paths.root / lesson.attrs["path"]
    payload: dict[str, Any] = {"html": rendered.html, "toc": [list(t) for t in rendered.toc]}
    for key, value in (
        ("code", _code_files(lesson_dir)),
        ("quiz", _quiz(lesson_dir)),
        ("artifacts", _artifacts(g, paths, lesson)),
    ):
        if value:
            payload[key] = value
    if rendered.figures and figures.runtime is not None:
        # May be an empty list: some figures are defined by the runtime itself.
        payload["figures"] = figures.providers(rendered.figures)
    if rendered.has_mermaid:
        payload["mermaid"] = True
    return payload


def lesson_file_name(lesson: Node) -> str:
    """``lesson:10/04`` -> ``10-04.js``."""
    return lesson.attrs["ref"].replace("/", "-") + ".js"
