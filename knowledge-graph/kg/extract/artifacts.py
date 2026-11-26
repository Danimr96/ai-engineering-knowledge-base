"""Artifact nodes from each lesson's ``outputs/`` folder.

Every lesson "ships" something reusable: a skill (``outputs/skill-*.md``), a
prompt (``prompt-*.md``), an agent (``agent-*.md``) or a skill bundle (a
folder with a ``SKILL.md``). They carry real YAML frontmatter::

    ---
    name: mha-configurator
    description: Recommend head count, KV-head count, ...
    version: 1.0.0
    phase: 7
    lesson: 3
    tags: [transformers, attention, mha, gqa]
    ---

Tags are kept as a list attribute and become Obsidian tags in the vault, not
graph nodes: a tag node with 40 neighbours adds clutter, while an Obsidian tag
gives the same "show me everything tagged attention" for free.
"""

from __future__ import annotations

import re
from pathlib import Path

from kg.markdown import parse_frontmatter, slugify
from kg.model import Edge, KnowledgeGraph, Node, artifact_id
from kg.paths import Paths

ARTIFACT_KINDS = ("skill", "prompt", "agent")
_KIND_RE = re.compile(r"^(skill|prompt|agent)-(.+)$")


def _artifact_from_file(path: Path, kind: str, lesson_attrs: dict, paths: Paths, bundle: bool = False) -> Node:
    meta = parse_frontmatter(path.read_text(encoding="utf-8", errors="replace"))
    name = str(meta.get("name") or (path.parent.name if bundle else path.stem)).strip()
    tags = meta.get("tags") if isinstance(meta.get("tags"), list) else []
    return Node(
        id=artifact_id(lesson_attrs["phase"], lesson_attrs["num"], slugify(name) or slugify(path.stem)),
        type="artifact",
        label=name,
        attrs={
            "name": name,
            "kind": kind,
            "description": str(meta.get("description") or "").strip(),
            "version": str(meta.get("version") or "").strip(),
            "tags": [slugify(t) for t in tags if t],
            "bundle": bundle,
            "path": paths.rel(path),
            "lesson": lesson_attrs["ref"],
        },
        source_file=paths.rel(path),
        line=1,
    )


def extract_artifacts(g: KnowledgeGraph, paths: Paths) -> list[str]:
    problems: list[str] = []
    for lesson in g.nodes_of_type("lesson"):
        outputs = paths.root / lesson.attrs["path"] / "outputs"
        if not outputs.is_dir():
            continue
        for path in sorted(outputs.iterdir()):
            node: Node | None = None
            if path.is_file() and path.suffix == ".md":
                m = _KIND_RE.match(path.stem)
                if m:
                    node = _artifact_from_file(path, m.group(1), lesson.attrs, paths)
            elif path.is_dir() and (path / "SKILL.md").is_file():
                node = _artifact_from_file(path / "SKILL.md", "skill", lesson.attrs, paths, bundle=True)
            if node is None:
                continue
            if node.id in g:
                problems.append(f"artifacts: duplicate id {node.id} from {paths.rel(path)}")
                continue
            g.add_node(node)
            g.add_edge(Edge(src=lesson.id, dst=node.id, type="SHIPS", source_file=paths.rel(path), line=1))
    return problems
