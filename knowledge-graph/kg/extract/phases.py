"""Phase nodes and the phase-level dependency graph.

Sources
-------
* ``phases/NN-slug/`` folder names give the phase number and a fallback title.
* ``phases/NN-slug/README.md`` H1 (``# Phase 7: Transformers Deep Dive``)
  gives the proper title.
* ``ROADMAP.md`` headings (``## Phase 7: ... (~18 hours)``) give the hour
  estimate.
* ``README.md``'s mermaid block under "The shape of the curriculum" gives the
  phase -> phase dependencies (``P5 --> P7``). Upstream's ``site/build.js``
  parses the same block with the same regex; ``site/data.js`` is generated
  from it, so we read the source of truth rather than the generated file.
"""

from __future__ import annotations

import html
import re
from pathlib import Path

from kg.markdown import parse_lesson_header
from kg.model import Edge, KnowledgeGraph, Node, phase_id
from kg.paths import Paths

PHASE_DIR_RE = re.compile(r"^(\d{2})-([a-z0-9][a-z0-9-]*)$")
# ``P5["Phase 5 — NLP"] --> P7["Phase 7 — Transformers"]`` or ``P17 --> P19``
MERMAID_EDGE_RE = re.compile(r"^\s*P(\d+)(?:\[[^\]]*\])?\s*-->\s*P(\d+)")
MERMAID_LABEL_RE = re.compile(r"P(\d+)\[\"Phase \d+\s*[—-]\s*([^\"]+)\"\]")
ROADMAP_HOURS_RE = re.compile(r"^##\s+Phase\s+(\d+):.*?\(~?\s*([\d.]+)\s*hours?\)", re.IGNORECASE)
PHASE_README_H1_RE = re.compile(r"^#\s+Phase\s+\d+\s*[:—-]\s*(.+?)\s*$")

_TITLE_FIXUPS = {
    "ai": "AI", "ml": "ML", "llm": "LLM", "llms": "LLMs", "nlp": "NLP", "rl": "RL",
    "mcp": "MCP", "rag": "RAG", "and": "and", "to": "to", "from": "from",
}


def slug_to_title(slug: str) -> str:
    """``'llms-from-scratch'`` -> ``'LLMs from Scratch'`` (fallback only)."""
    return " ".join(_TITLE_FIXUPS.get(w, w.capitalize()) for w in slug.split("-"))


def iter_phase_dirs(phases_dir: Path):
    """Yield ``(num, slug, path)`` for every ``NN-slug`` folder, sorted."""
    if not phases_dir.is_dir():
        return
    for path in sorted(phases_dir.iterdir()):
        m = PHASE_DIR_RE.match(path.name)
        if path.is_dir() and m:
            yield int(m.group(1)), m.group(2), path


def read_phase_title(phase_dir: Path) -> str | None:
    readme = phase_dir / "README.md"
    if not readme.is_file():
        return None
    for line in readme.read_text(encoding="utf-8").splitlines()[:5]:
        m = PHASE_README_H1_RE.match(line)
        if m:
            return m.group(1).strip()
    return None


def read_roadmap_hours(roadmap: Path) -> dict[int, float]:
    hours: dict[int, float] = {}
    if not roadmap.is_file():
        return hours
    for line in roadmap.read_text(encoding="utf-8").splitlines():
        m = ROADMAP_HOURS_RE.match(line)
        if m:
            hours[int(m.group(1))] = float(m.group(2))
    return hours


def parse_phase_dag(readme_text: str) -> tuple[list[tuple[int, int, int]], dict[int, str]]:
    """Return ``[(from, to, line)]`` edges and ``{num: title}`` from the mermaid block.

    Only the first mermaid block after the "shape of the curriculum" heading
    is read; the README has other mermaid diagrams that are not the DAG.
    """
    edges: list[tuple[int, int, int]] = []
    labels: dict[int, str] = {}
    in_block = False
    seen_heading = False
    for lineno, line in enumerate(readme_text.splitlines(), start=1):
        if not seen_heading:
            if "shape of the curriculum" in line.lower():
                seen_heading = True
            continue
        if line.strip().startswith("```mermaid"):
            in_block = True
            continue
        if in_block and line.strip().startswith("```"):
            break
        if not in_block:
            continue
        for m in MERMAID_LABEL_RE.finditer(line):
            labels[int(m.group(1))] = html.unescape(m.group(2)).strip()
        m = MERMAID_EDGE_RE.match(line)
        if m:
            edges.append((int(m.group(1)), int(m.group(2)), lineno))
    return edges, labels


def extract_phases(g: KnowledgeGraph, paths: Paths) -> list[str]:
    """Add phase nodes and PHASE_REQUIRES edges. Returns a list of problems."""
    problems: list[str] = []
    hours = read_roadmap_hours(paths.upstream / "ROADMAP.md")
    readme_text = paths.readme.read_text(encoding="utf-8") if paths.readme.is_file() else ""
    dag_edges, mermaid_titles = parse_phase_dag(readme_text)

    for num, slug, path in iter_phase_dirs(paths.phases_dir):
        title = read_phase_title(path) or mermaid_titles.get(num) or slug_to_title(slug)
        g.add_node(
            Node(
                id=phase_id(num),
                type="phase",
                label=f"Phase {num}: {title}",
                attrs={
                    "num": num,
                    "title": title,
                    "short_title": mermaid_titles.get(num, title),
                    "slug": path.name,
                    "hours": hours.get(num),
                    "path": paths.rel(path),
                },
                source_file=paths.rel(path / "README.md"),
                line=1,
            )
        )

    for src, dst, lineno in dag_edges:
        if phase_id(src) not in g or phase_id(dst) not in g:
            problems.append(f"README DAG references unknown phase: P{src} -> P{dst} (README.md:{lineno})")
            continue
        # Mermaid arrows point forward in time (P5 --> P7 means "7 comes after
        # 5"). Our edge type reads the other way: 7 REQUIRES 5.
        g.add_edge(
            Edge(src=phase_id(dst), dst=phase_id(src), type="PHASE_REQUIRES", attrs={"confidence": "high"},
                 source_file=paths.rel(paths.readme), line=lineno)
        )
    if not dag_edges:
        problems.append("no phase DAG found in README.md (mermaid block missing?)")
    return problems


__all__ = ["extract_phases", "iter_phase_dirs", "parse_phase_dag", "PHASE_DIR_RE", "parse_lesson_header"]
