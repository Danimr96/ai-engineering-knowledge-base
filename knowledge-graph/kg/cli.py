"""Command-line entry point: ``uv run kg <command>``.

Commands
--------
build              extract everything -> build/graph.json + build/report.md
export             graph.json -> Obsidian vault (vault/)
all                build then export
report             print build/report.md
prereqs REF        transitive prerequisites of a lesson (REF like 10/04)
dependents REF     lessons that build on a lesson
path A B           shortest prerequisite chain from A back to B
concepts REF       concepts a lesson teaches
search TEXT        find nodes by label
ask "QUESTION"     plain-language question -> the matching nodes and their neighbourhoods
neighbors ID|REF   every edge touching a node, grouped by type
info ID|REF        dump one node and its edges

``--root`` points the pipeline at another AI-Education folder (used by tests).
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from kg import graph_ops
from kg.model import KnowledgeGraph, lesson_id
from kg.paths import Paths


def _paths(args: argparse.Namespace) -> Paths:
    return Paths.for_root(Path(args.root)) if args.root else Paths.default()


def _ref(text: str) -> str:
    """Accept ``10/04``, ``10-04`` or a full node id."""
    if ":" in text:
        return text
    p, l = text.replace("-", "/").split("/")
    return lesson_id(int(p), int(l))


def _load(paths: Paths) -> KnowledgeGraph:
    if not paths.graph_json.is_file():
        sys.exit(f"{paths.graph_json} not found. Run `uv run kg build` first.")
    return KnowledgeGraph.read_json(paths.graph_json)


def _label(g: KnowledgeGraph, node_id: str) -> str:
    n = g.get(node_id)
    return n.label if n else node_id


# ---- commands --------------------------------------------------------------


def cmd_build(args: argparse.Namespace) -> int:
    from kg.build import build_and_write

    paths = _paths(args)
    g, stats = build_and_write(paths)
    print(f"graph:  {paths.graph_json}")
    print(f"report: {paths.report_md}")
    print("nodes:", g.node_counts())
    print("edges:", g.edge_counts())
    total_problems = sum(len(v) for v in stats.problems.values())
    print(f"validation problems: {len(stats.validation)}   extractor problems: {total_problems}")
    return 1 if stats.validation else 0


def cmd_export(args: argparse.Namespace) -> int:
    from kg.obsidian.export import export_vault

    paths = _paths(args)
    g = _load(paths)
    written = export_vault(g, paths, min_concept_lessons=args.min_concept_lessons, min_resource_lessons=args.min_resource_lessons)
    print(f"vault: {paths.vault_dir}  ({written} notes written)")
    return 0


def cmd_all(args: argparse.Namespace) -> int:
    rc = cmd_build(args)
    return rc or cmd_export(args)


def cmd_report(args: argparse.Namespace) -> int:
    paths = _paths(args)
    if not paths.report_md.is_file():
        sys.exit("no report yet; run `uv run kg build`")
    print(paths.report_md.read_text(encoding="utf-8"))
    return 0


def cmd_prereqs(args: argparse.Namespace) -> int:
    g = _load(_paths(args))
    lid = _ref(args.lesson)
    if lid not in g:
        sys.exit(f"unknown lesson {lid}")
    print(f"Before {_label(g, lid)}:")
    layers = graph_ops.prereqs_of(g, lid, args.depth)
    by_depth: dict[int, list[str]] = {}
    for node, d in layers.items():
        by_depth.setdefault(d, []).append(node)
    for d in sorted(by_depth):
        print(f"  depth {d}:")
        for node in sorted(by_depth[d]):
            print(f"    {_label(g, node)}")
    phases = [e for e in g.out_edges(lid, "REQUIRES_PHASE")]
    if phases:
        print("  whole phases:")
        for e in phases:
            print(f"    {_label(g, e.dst)}  ({e.attrs.get('span', '')})")
    if not layers and not phases:
        print("  (none recorded)")
    return 0


def cmd_dependents(args: argparse.Namespace) -> int:
    g = _load(_paths(args))
    lid = _ref(args.lesson)
    print(f"Builds on {_label(g, lid)}:")
    for node, d in sorted(graph_ops.dependents_of(g, lid, args.depth).items(), key=lambda kv: (kv[1], kv[0])):
        print(f"  depth {d}: {_label(g, node)}")
    return 0


def cmd_path(args: argparse.Namespace) -> int:
    g = _load(_paths(args))
    a, b = _ref(args.start), _ref(args.target)
    path = graph_ops.path_between(g, a, b)
    if path is None:
        print(f"no prerequisite chain from {_label(g, a)} back to {_label(g, b)}")
        return 1
    print(" -> ".join(_label(g, n) for n in path))
    return 0


def cmd_concepts(args: argparse.Namespace) -> int:
    g = _load(_paths(args))
    lid = _ref(args.lesson)
    for cid, tier in sorted(graph_ops.concepts_of(g, lid).items(), key=lambda kv: kv[0]):
        n = g.get(cid)
        flag = "glossary" if n and n.attrs.get("canonical") else "lesson-only"
        print(f"  {n.label if n else cid}  [{tier}, {flag}]")
    return 0


def cmd_ask(args: argparse.Namespace) -> int:
    g = _load(_paths(args))
    print(graph_ops.format_ask(graph_ops.ask(g, args.question, max_seeds=args.seeds)))
    return 0


def cmd_neighbors(args: argparse.Namespace) -> int:
    g = _load(_paths(args))
    nid = _ref(args.node) if "/" in args.node and ":" not in args.node else args.node
    if nid not in g:
        sys.exit(f"unknown node {nid}")
    print(f"{_label(g, nid)}  ({nid})")
    for etype, items in graph_ops.neighbors(g, nid).items():
        print(f"  {etype} ({len(items)}):")
        for d, other in items[: args.limit]:
            print(f"    {d} {_label(g, other)}")
        if len(items) > args.limit:
            print(f"    … {len(items) - args.limit} more")
    return 0


def cmd_search(args: argparse.Namespace) -> int:
    g = _load(_paths(args))
    types = tuple(args.type) if args.type else None
    for nid, label in graph_ops.search(g, args.text, types):
        print(f"  {nid:40s} {label}")
    return 0


def cmd_info(args: argparse.Namespace) -> int:
    g = _load(_paths(args))
    nid = _ref(args.node) if "/" in args.node and ":" not in args.node else args.node
    n = g.get(nid)
    if n is None:
        sys.exit(f"unknown node {nid}")
    print(f"{n.id}  [{n.type}]  {n.label}")
    print(f"  source: {n.source_file}:{n.line}")
    for k, v in n.attrs.items():
        if v not in (None, "", [], {}):
            print(f"  {k}: {v}")
    print("  out:")
    for e in g.out_edges(nid):
        print(f"    -{e.type}-> {_label(g, e.dst)}  {e.attrs.get('confidence', '')} {e.attrs.get('span', '')}")
    print("  in:")
    for e in g.in_edges(nid):
        print(f"    <-{e.type}- {_label(g, e.src)}  {e.attrs.get('confidence', '')}")
    return 0


# ---- parser ----------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="kg", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--root", help="AI-Education folder (default: derived from this package's location)")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("build").set_defaults(fn=cmd_build)
    e = sub.add_parser("export")
    e.add_argument("--min-concept-lessons", type=int, default=2,
                   help="non-canonical concepts need this many lessons to get their own note (default 2)")
    e.add_argument("--min-resource-lessons", type=int, default=2,
                   help="resources need this many citing lessons to get their own note (default 2)")
    e.set_defaults(fn=cmd_export)
    a = sub.add_parser("all")
    a.add_argument("--min-concept-lessons", type=int, default=2)
    a.add_argument("--min-resource-lessons", type=int, default=2)
    a.set_defaults(fn=cmd_all)
    sub.add_parser("report").set_defaults(fn=cmd_report)

    s = sub.add_parser("prereqs"); s.add_argument("lesson"); s.add_argument("--depth", type=int, default=None); s.set_defaults(fn=cmd_prereqs)
    s = sub.add_parser("dependents"); s.add_argument("lesson"); s.add_argument("--depth", type=int, default=None); s.set_defaults(fn=cmd_dependents)
    s = sub.add_parser("path"); s.add_argument("start"); s.add_argument("target"); s.set_defaults(fn=cmd_path)
    s = sub.add_parser("concepts"); s.add_argument("lesson"); s.set_defaults(fn=cmd_concepts)
    s = sub.add_parser("search"); s.add_argument("text"); s.add_argument("--type", action="append"); s.set_defaults(fn=cmd_search)
    s = sub.add_parser("ask", help="plain-language question -> scoped subgraph (no LLM)"); s.add_argument("question"); s.add_argument("--seeds", type=int, default=5); s.set_defaults(fn=cmd_ask)
    s = sub.add_parser("neighbors"); s.add_argument("node"); s.add_argument("--limit", type=int, default=25); s.set_defaults(fn=cmd_neighbors)
    s = sub.add_parser("info"); s.add_argument("node"); s.set_defaults(fn=cmd_info)

    args = p.parse_args(argv)
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
