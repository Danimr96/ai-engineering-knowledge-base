"""graph.json -> Obsidian vault.

Decisions made here
-------------------
* **Which nodes get a note.** All phases, lessons, tracks, categories, paths,
  myths, artifacts and glossary concepts. Non-canonical concepts and
  resources only when at least ``min_*_lessons`` lessons point at them: a
  term used by one lesson or a paper cited once is still in ``graph.json``
  and listed inside the lesson note, but a note of its own would only add a
  leaf to the graph view. The thresholds are CLI flags.
* **Naming happens before rendering.** Every note's path is decided first,
  so a renderer can link to any other note without knowing whether it has
  been written yet.
* **Stale notes are removed.** A manifest lists what the last export wrote.
  Anything in that list that this export did not write is deleted; anything
  not in the list (your files) is never touched.
* **Unchanged files are not rewritten**, so file timestamps only move when
  content moves, and a second export is a no-op you can verify with ``diff``.
"""

from __future__ import annotations

import json
import os
from pathlib import Path

from kg.model import KnowledgeGraph, Node
from kg.obsidian.config import write_config
from kg.obsidian.preserve import read_preserved
from kg.obsidian.writer import RENDERERS, Ctx, Naming, render_home
from kg.paths import Paths

MANIFEST = ".kg-manifest.json"
MY_NOTES_README = """\
# My Notes

This folder is yours. The exporter never writes here and never deletes here.

Ideas:
- one note per lesson reflection (link it to the lesson: `[[Lessons/10-01 ...]]`)
- questions to bring back to the tutor
- your own concept notes when the glossary is missing something
"""


def _select_nodes(g: KnowledgeGraph, min_concept_lessons: int, min_resource_lessons: int) -> list[Node]:
    teaches: dict[str, set[str]] = {}
    cites: dict[str, set[str]] = {}
    for e in g.edges:
        if e.type == "TEACHES":
            teaches.setdefault(e.dst, set()).add(e.src)
        elif e.type == "CITES" and e.src.startswith("lesson:"):
            cites.setdefault(e.dst, set()).add(e.src)
    chosen: list[Node] = []
    for n in g:
        if n.type == "concept" and not n.attrs.get("canonical"):
            if len(teaches.get(n.id, ())) < min_concept_lessons:
                continue
        if n.type == "resource":
            if len(cites.get(n.id, ())) < min_resource_lessons:
                continue
        chosen.append(n)
    return chosen


def _link_upstream(vault: Path, paths: Paths) -> bool:
    """Symlink ``vault/Upstream`` -> ``ai-engineering-from-scratch/phases``.

    Lets a lesson note open the real lesson text inside Obsidian (mermaid and
    all). Skipped silently if the phases folder is missing or the link
    cannot be created.
    """
    target = paths.phases_dir
    link = vault / "Upstream"
    if not target.is_dir():
        return False
    if link.is_symlink() or link.exists():
        return link.is_symlink()
    try:
        os.symlink(os.path.relpath(target, vault), link, target_is_directory=True)
        return True
    except OSError:
        return False


def _write_if_changed(path: Path, text: str) -> bool:
    if path.is_file() and path.read_text(encoding="utf-8") == text:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return True


def export_vault(g: KnowledgeGraph, paths: Paths, *, min_concept_lessons: int = 2, min_resource_lessons: int = 2) -> int:
    """Write the vault. Returns the number of notes written (all, not only changed)."""
    vault = paths.vault_dir
    vault.mkdir(parents=True, exist_ok=True)
    manifest_path = vault / MANIFEST
    previous: set[str] = set(json.loads(manifest_path.read_text(encoding="utf-8"))) if manifest_path.is_file() else set()

    upstream_linked = _link_upstream(vault, paths)
    naming = Naming()
    nodes = _select_nodes(g, min_concept_lessons, min_resource_lessons)
    for n in sorted(nodes, key=lambda n: n.id):
        naming.assign(n)
    ctx = Ctx(g=g, paths=paths, naming=naming, upstream_linked=upstream_linked)

    written: list[str] = []
    per_folder: dict[str, int] = {}
    for n in nodes:
        rel = naming.paths[n.id] + ".md"
        path = vault / rel
        kept = read_preserved(path)
        text = RENDERERS[n.type](ctx, n, kept)
        _write_if_changed(path, text)
        written.append(rel)
        per_folder[rel.split("/", 1)[0]] = per_folder.get(rel.split("/", 1)[0], 0) + 1

    _write_if_changed(vault / "Home.md", render_home(ctx, per_folder))
    written.append("Home.md")
    for p in write_config(vault):
        written.append(p.relative_to(vault).as_posix())

    my_notes = vault / "My Notes"
    my_notes.mkdir(exist_ok=True)
    if not (my_notes / "README.md").exists():
        (my_notes / "README.md").write_text(MY_NOTES_README, encoding="utf-8")

    # Remove notes from the previous export that no longer exist in the graph.
    for stale in sorted(previous - set(written)):
        p = vault / stale
        if p.is_file() and not stale.startswith("My Notes/") and not stale.startswith(".obsidian/"):
            p.unlink()
    for folder in sorted({w.split("/", 1)[0] for w in previous}, reverse=True):
        d = vault / folder
        if d.is_dir() and folder not in ("My Notes", ".obsidian", "Bases") and not any(d.iterdir()):
            d.rmdir()

    manifest_path.write_text(json.dumps(sorted(written), indent=0) + "\n", encoding="utf-8")
    return len(nodes)
