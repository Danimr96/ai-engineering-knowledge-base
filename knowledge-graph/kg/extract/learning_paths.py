"""Learning-path nodes from ``learning-paths/*.json``.

Upstream ships 12 curated routes (career paths like "Applied AI Engineer",
skill routes like "Model Context Protocol"). Three JSON shapes exist, but all
of them have ``id``, ``title``, ``summary``, ``estimatedMinutes`` and a
``lessons`` array whose items carry ``order``, ``path``, ``minutes`` and
``required``. Some also carry ``optionalLessons``. We read only those keys.

The lesson is identified from the numeric prefixes in ``path``
(``phases/13-tools-and-protocols/01-the-tool-interface``), never from the
slug, matching the ID rule used everywhere else.
"""

from __future__ import annotations

import json
import re

from kg.model import Edge, KnowledgeGraph, Node, learning_path_id, lesson_id
from kg.paths import Paths

_PATH_RE = re.compile(r"phases/(\d{2})-[^/]+/(\d{2})-[^/]+")


def extract_learning_paths(g: KnowledgeGraph, paths: Paths) -> list[str]:
    problems: list[str] = []
    if not paths.learning_paths_dir.is_dir():
        return problems
    for file in sorted(paths.learning_paths_dir.glob("*.json")):
        src = paths.rel(file)
        try:
            data = json.loads(file.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            problems.append(f"learning path {src}: invalid JSON ({exc})")
            continue
        key = str(data.get("id") or file.stem)
        pid = learning_path_id(key)
        g.add_node(Node(id=pid, type="learning_path", label=str(data.get("title") or key),
                        attrs={"key": key, "title": data.get("title"), "summary": data.get("summary"),
                               "kind": data.get("kind") or data.get("workFamily"),
                               "minutes": data.get("estimatedMinutes"), "path": src},
                        source_file=src, line=1))
        items = [(item, True) for item in data.get("lessons", [])]
        items += [(item, False) for item in data.get("optionalLessons", [])]
        for item, in_main in items:
            m = _PATH_RE.search(str(item.get("path", "")))
            if not m:
                problems.append(f"learning path {key}: cannot read lesson path {item.get('path')!r}")
                continue
            lid = lesson_id(int(m.group(1)), int(m.group(2)))
            if lid not in g:
                problems.append(f"learning path {key}: missing lesson {lid}")
                continue
            required = bool(item.get("required", in_main)) and in_main
            g.add_edge(Edge(src=pid, dst=lid, type="INCLUDES",
                            attrs={"order": item.get("order"), "required": required, "minutes": item.get("minutes")},
                            source_file=src, line=None))
    return problems
