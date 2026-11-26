"""Build orchestrator: run every extractor in order, validate, write outputs.

Why a single orchestrator
-------------------------
Extractors depend on each other's nodes (an edge needs both endpoints), so
*order* is part of the design. Putting the order in one function makes it
visible and testable, and lets tests run the whole pipeline on a fixture tree
in a few milliseconds.

Outputs
-------
* ``build/graph.json`` – the canonical graph (sorted, deterministic)
* ``build/report.md``  – the quality report (read it after every build)
"""

from __future__ import annotations

import subprocess
from datetime import datetime, timezone

from kg.communities import detect_communities
from kg.extract.artifacts import extract_artifacts
from kg.extract.code import extract_code
from kg.extract.glossary import extract_glossary
from kg.extract.key_terms import extract_key_terms
from kg.extract.learning_paths import extract_learning_paths
from kg.extract.lessons import extract_lessons, extract_tracks
from kg.extract.phases import extract_phases
from kg.extract.prereqs import extract_prereqs
from kg.extract.resolve import load_aliases
from kg.extract.resources import extract_resources
from kg.model import KnowledgeGraph
from kg.overlay.plan import extract_plan
from kg.paths import Paths
from kg.report import BuildStats, render_report


def upstream_commit(paths: Paths) -> str | None:
    """Short hash of the upstream clone, read-only, so the graph says which version it reflects."""
    try:
        out = subprocess.run(
            ["git", "-C", str(paths.upstream), "rev-parse", "--short", "HEAD"],
            capture_output=True, text=True, timeout=10, check=False,
        )
        return out.stdout.strip() or None
    except (OSError, subprocess.SubprocessError):
        return None


def build_graph(paths: Paths) -> tuple[KnowledgeGraph, BuildStats]:
    """Run the pipeline in memory. Does not write anything."""
    g = KnowledgeGraph()
    stats = BuildStats(upstream_commit=upstream_commit(paths), built_at=datetime.now(timezone.utc).isoformat(timespec="seconds"))

    stats.problems["phases"] = extract_phases(g, paths)
    stats.problems["lessons"] = extract_lessons(g, paths)
    stats.problems["tracks"] = extract_tracks(g, paths)
    stats.problems["prereqs"] = extract_prereqs(g, paths)

    index, probs = extract_glossary(g, paths)
    stats.problems["glossary"] = probs
    stats.problems["aliases"] = index.add_manual_aliases(load_aliases(paths.data_dir))

    kt_stats, probs = extract_key_terms(g, paths, index)
    stats.key_terms = kt_stats
    stats.problems["key_terms"] = probs

    stats.problems["artifacts"] = extract_artifacts(g, paths)
    stats.problems["resources"] = extract_resources(g, paths)
    stats.problems["learning_paths"] = extract_learning_paths(g, paths)
    stats.problems["plan"] = extract_plan(g, paths)
    stats.problems["code"] = extract_code(g, paths)
    # Last: clustering reads every edge type above.
    stats.problems["communities"] = detect_communities(g)

    stats.validation = g.validate()
    g.meta = {
        "upstream_commit": stats.upstream_commit,
        "built_at": stats.built_at,
        "root": paths.root.name,
        "node_counts": g.node_counts(),
        "edge_counts": g.edge_counts(),
    }
    return g, stats


def build_and_write(paths: Paths) -> tuple[KnowledgeGraph, BuildStats]:
    g, stats = build_graph(paths)
    g.write_json(paths.graph_json)
    paths.report_md.write_text(render_report(g, stats), encoding="utf-8")
    return g, stats
