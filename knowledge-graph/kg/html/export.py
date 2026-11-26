"""graph.json + lesson folders -> the static site.

Two outputs from the same parts
-------------------------------
* **Folder** (``site/``): ``index.html`` plus small files loaded on demand.
  Quick to open, friendly to ``git diff``, the one to publish on a web server
  or to unzip from a shared drive.
* **Single file** (``dist/*.html``): the same page with every file inlined.
  One attachment, one double click. This is the form that survives places
  that will not serve a folder of HTML (SharePoint downloads ``.html`` files
  instead of rendering them, mail strips folders, and so on).

The page does not know which one it is running from. It asks for a resource
by path (``data/lessons/10-04.js``); the loader in ``app.js`` first looks for
an inlined copy of that path and only then adds a ``<script src>`` tag. In
the single file, every on-demand script sits in the document as an inert
``<script type="text/plain">`` block that costs nothing until it is needed.

Housekeeping
------------
Files are only rewritten when their content changes, and files from a
previous export that this one did not produce are removed, so the folder
always matches the graph and a second export is a no-op.
"""

from __future__ import annotations

import base64
import json
import re
from dataclasses import dataclass
from pathlib import Path

from kg.html.data import build_payload
from kg.html.lessons import FigureIndex, LinkResolver, build_lesson, lesson_file_name
from kg.model import KnowledgeGraph
from kg.paths import Paths

PACKAGE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = PACKAGE_DIR / "assets"
VENDOR_DIR = PACKAGE_DIR / "vendor"

FONT_FILE = "overpass-latin.woff2"
SINGLE_FILE_NAME = "ai-engineering-knowledge-base.html"

# Folders inside ``site/`` that the exporter owns completely (stale files are deleted).
MANAGED = ("assets", "data", "vendor")


@dataclass
class SiteStats:
    lessons: int
    files: int
    bytes: int
    single_file: Path | None = None
    single_bytes: int = 0


def js_assign(name: str, value: object) -> str:
    """``window.<name> = <json>;`` as compact, deterministic JavaScript."""
    return f"window.{name}=" + _json(value) + ";\n"


def js_resource(path: str, value: object) -> str:
    """An on-demand file: hands its payload to the loader under its own path."""
    return f"window.__kgRes({json.dumps(path)}," + _json(value) + ");\n"


def _json(value: object) -> str:
    # U+2028/2029 are legal in JSON but were line terminators in older
    # JavaScript; escaping them keeps the output valid everywhere.
    text = json.dumps(value, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
    return text.replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")


def inline_safe(js: str) -> str:
    """Make JavaScript safe to place inside a ``<script>`` element.

    The HTML parser ends a script at the first ``</script`` and changes mode
    at ``<!--``, wherever they occur, including inside string literals. In
    JavaScript source both can only appear inside strings, regular
    expressions or comments, where ``<\\/`` and ``<\\!`` mean the same thing.
    """
    return re.sub(r"</(script)", r"<\\/\1", js, flags=re.I).replace("<!--", "<\\!--")


def _collect(g: KnowledgeGraph, paths: Paths) -> tuple[dict[str, str], dict[str, bytes], int, str]:
    """Every file of the site as ``{relative path: content}`` (text and binary)."""
    text: dict[str, str] = {}
    binary: dict[str, bytes] = {}

    links = LinkResolver(g, paths)
    figures = FigureIndex.scan(paths)
    used_figure_files: set[str] = set()
    any_figure = False
    with_text: set[str] = set()
    for lesson in g.nodes_of_type("lesson"):
        content = build_lesson(g, paths, lesson, links, figures)
        if content is None:
            continue
        with_text.add(lesson.id)
        if "figures" in content:
            any_figure = True
            used_figure_files.update(content["figures"])
        path = f"data/lessons/{lesson_file_name(lesson)}"
        text[path] = js_resource(path, content)

    payload = build_payload(g, paths, with_text)
    text["data/graph.js"] = js_assign("KG_DATA", payload)
    text["assets/app.css"] = (ASSETS_DIR / "app.css").read_text(encoding="utf-8")
    text["assets/app.js"] = (ASSETS_DIR / "app.js").read_text(encoding="utf-8")
    binary[f"assets/fonts/{FONT_FILE}"] = (VENDOR_DIR / FONT_FILE).read_bytes()
    text["vendor/mermaid.min.js"] = (VENDOR_DIR / "mermaid.min.js").read_text(encoding="utf-8")
    if figures.runtime is not None and any_figure:
        text["vendor/figures/lesson-figures.js"] = figures.runtime.read_text(encoding="utf-8")
        for name in sorted(used_figure_files):
            text[f"vendor/figures/{name}"] = figures.sources[name]
    return text, binary, len(with_text), payload["title"]


def _index_html(title: str, *, style: str, data: str, resources: str, app: str) -> str:
    template = (ASSETS_DIR / "index.html").read_text(encoding="utf-8")
    # ``str.replace`` (not ``re.sub``): the inlined scripts are full of backslashes.
    for marker, value in (
        ("{{TITLE}}", title.replace("&", "&amp;").replace("<", "&lt;")),
        ("<!--KG:STYLE-->", style),
        ("<!--KG:DATA-->", data),
        ("<!--KG:RESOURCES-->", resources),
        ("<!--KG:APP-->", app),
    ):
        template = template.replace(marker, value)
    return template


def _write_if_changed(path: Path, content: str | bytes) -> None:
    data = content.encode("utf-8") if isinstance(content, str) else content
    if path.is_file() and path.read_bytes() == data:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def _remove_stale(site: Path, keep: set[str]) -> None:
    for folder in MANAGED:
        root = site / folder
        if not root.is_dir():
            continue
        for path in sorted(root.rglob("*"), reverse=True):
            if path.is_file() and path.relative_to(site).as_posix() not in keep:
                path.unlink()
            elif path.is_dir() and not any(path.iterdir()):
                path.rmdir()


def export_site(g: KnowledgeGraph, paths: Paths, *, single_file: bool = False) -> SiteStats:
    """Write ``site/``; with ``single_file`` also write the one-file build."""
    text, binary, lessons, title = _collect(g, paths)

    # ---- folder ---------------------------------------------------------
    site = paths.site_dir
    index = _index_html(
        title,
        style='<link rel="stylesheet" href="assets/app.css">',
        data='<script src="data/graph.js"></script>',
        resources="",
        app='<script src="assets/app.js"></script>',
    )
    files: dict[str, str | bytes] = {**text, **binary, "index.html": index}
    for rel, content in files.items():
        _write_if_changed(site / rel, content)
    _remove_stale(site, set(files))
    stats = SiteStats(
        lessons=lessons,
        files=len(files),
        bytes=sum(len(c.encode("utf-8")) if isinstance(c, str) else len(c) for c in files.values()),
    )

    # ---- single file ----------------------------------------------------
    if single_file:
        font = base64.b64encode(binary[f"assets/fonts/{FONT_FILE}"]).decode("ascii")
        css = text["assets/app.css"].replace(f'url("fonts/{FONT_FILE}")', f'url("data:font/woff2;base64,{font}")')
        eager = {"data/graph.js", "assets/app.js", "assets/app.css"}
        blocks = [
            f'<script type="text/plain" data-res="{rel}">{inline_safe(src)}</script>'
            for rel, src in sorted(text.items())
            if rel not in eager
        ]
        html = _index_html(
            title,
            style=f"<style>{css}</style>",
            data=f"<script>{inline_safe(text['data/graph.js'])}</script>",
            resources="\n".join(blocks),
            app=f"<script>{inline_safe(text['assets/app.js'])}</script>",
        )
        out = paths.dist_dir / SINGLE_FILE_NAME
        _write_if_changed(out, html)
        stats.single_file = out
        stats.single_bytes = len(html.encode("utf-8"))
    return stats
