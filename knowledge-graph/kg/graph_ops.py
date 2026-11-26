"""Graph traversals used by the CLI and the vault writer.

Pure Python on top of ``KnowledgeGraph``; no networkx on purpose so the
algorithms stay visible. Everything here is breadth-first search in some
costume:

* ``prereqs_of``      – everything you should know before a lesson, by depth
* ``dependents_of``   – everything that builds on a lesson
* ``path_between``    – one shortest prerequisite chain from A back to B
* ``shared_concepts`` – concepts two lessons both teach
* ``concept_lessons`` – lessons teaching a concept, with the match tier

Prerequisite edges point *backwards in time* (10/04 REQUIRES 07/02). So
"what comes before X" follows out-edges, and "what builds on X" follows
in-edges.
"""

from __future__ import annotations

import re
from collections import deque

from kg.model import KnowledgeGraph

PREREQ_TYPES = ("REQUIRES", "BRIDGE")


def _adjacency(g: KnowledgeGraph, types: tuple[str, ...], reverse: bool = False) -> dict[str, list[str]]:
    adj: dict[str, list[str]] = {}
    for e in g.edges:
        if e.type in types:
            a, b = (e.dst, e.src) if reverse else (e.src, e.dst)
            adj.setdefault(a, []).append(b)
    return adj


def bfs_layers(adj: dict[str, list[str]], start: str, max_depth: int | None = None) -> dict[str, int]:
    """``{node: depth}`` for every node reachable from ``start`` (excluded)."""
    depth: dict[str, int] = {start: 0}
    queue: deque[str] = deque([start])
    while queue:
        cur = queue.popleft()
        if max_depth is not None and depth[cur] >= max_depth:
            continue
        for nxt in adj.get(cur, []):
            if nxt not in depth:
                depth[nxt] = depth[cur] + 1
                queue.append(nxt)
    depth.pop(start, None)
    return depth


def prereqs_of(g: KnowledgeGraph, lesson: str, max_depth: int | None = None, types: tuple[str, ...] = PREREQ_TYPES) -> dict[str, int]:
    """Transitive prerequisites of a lesson: ``{lesson_id: depth}``.

    Depth 1 = stated directly in the lesson header (or as a bridge in your
    plan), depth 2 = prerequisites of those, and so on.
    """
    return bfs_layers(_adjacency(g, types), lesson, max_depth)


def dependents_of(g: KnowledgeGraph, lesson: str, max_depth: int | None = None) -> dict[str, int]:
    """Lessons that (transitively) require this one."""
    return bfs_layers(_adjacency(g, ("REQUIRES",), reverse=True), lesson, max_depth)


def path_between(g: KnowledgeGraph, start: str, target: str, types: tuple[str, ...] = PREREQ_TYPES) -> list[str] | None:
    """Shortest chain ``start -> ... -> target`` along prerequisite edges, or None."""
    adj = _adjacency(g, types)
    parent: dict[str, str | None] = {start: None}
    queue: deque[str] = deque([start])
    while queue:
        cur = queue.popleft()
        if cur == target:
            path = []
            node: str | None = cur
            while node is not None:
                path.append(node)
                node = parent[node]
            return list(reversed(path))
        for nxt in adj.get(cur, []):
            if nxt not in parent:
                parent[nxt] = cur
                queue.append(nxt)
    return None


def concepts_of(g: KnowledgeGraph, lesson: str) -> dict[str, str]:
    """``{concept_id: best match tier}`` taught by a lesson."""
    rank = {"exact": 0, "alias": 1, "normalized": 2, "new": 3}
    out: dict[str, str] = {}
    for e in g.out_edges(lesson, "TEACHES"):
        tier = e.attrs.get("match", "new")
        if e.dst not in out or rank.get(tier, 9) < rank.get(out[e.dst], 9):
            out[e.dst] = tier
    return out


def shared_concepts(g: KnowledgeGraph, lesson_a: str, lesson_b: str) -> list[str]:
    a, b = concepts_of(g, lesson_a), concepts_of(g, lesson_b)
    return sorted(set(a) & set(b))


def concept_lessons(g: KnowledgeGraph, concept: str) -> list[tuple[str, str]]:
    """``[(lesson_id, best tier)]`` sorted by lesson id, one entry per lesson.

    A lesson can reach a concept through several edges (a Key Terms row and a
    glossary "Learn it" link); the best match tier is kept.
    """
    rank = {"exact": 0, "alias": 1, "normalized": 2, "new": 3}
    best: dict[str, str] = {}
    for e in g.in_edges(concept, "TEACHES"):
        tier = e.attrs.get("match", "new")
        if e.src not in best or rank.get(tier, 9) < rank.get(best[e.src], 9):
            best[e.src] = tier
    return sorted(best.items())


_STOPWORDS = {
    "the", "and", "for", "with", "what", "which", "where", "how", "does", "about", "from", "into", "that", "this",
    "are", "was", "you", "your", "lesson", "lessons", "teach", "teaches", "taught", "learn", "need", "before",
    "after", "between", "connect", "connects", "connected", "explain", "show", "list", "find", "all", "any", "when",
    "cover", "covers", "covered", "use", "uses", "using", "used", "have", "has", "can", "should", "must", "know",
    "do", "is", "it", "of", "to", "in", "on", "or", "an", "as", "at", "by", "be", "we", "my", "me", "up", "so", "if",
    "no", "not", "one", "our", "its",
}


def _tokens(text: str) -> list[str]:
    return [t for t in re.findall(r"[a-z0-9][a-z0-9+#.-]*", text.casefold()) if len(t) >= 2 and t not in _STOPWORDS]


def neighbors(g: KnowledgeGraph, node_id: str) -> dict[str, list[tuple[str, str]]]:
    """``{edge type: [(direction, other id)]}`` for every edge touching a node."""
    out: dict[str, set[tuple[str, str]]] = {}
    for e in g.edges:
        if e.src == node_id:
            out.setdefault(e.type, set()).add(("->", e.dst))
        elif e.dst == node_id:
            out.setdefault(e.type, set()).add(("<-", e.src))
    # A lesson can reach a concept through two Key Terms rows (two edges);
    # for a neighbourhood listing that is one neighbour.
    return {etype: sorted(pairs) for etype, pairs in out.items()}


def ask(g: KnowledgeGraph, question: str, max_seeds: int = 5, max_per_type: int = 12) -> dict:
    """Answer a plain-language question with a *scoped subgraph*, no LLM.

    Mirrors what a graph query tool does: score every node against the
    question's words (label matches count most, aliases and definitions less),
    take the best few as seeds, and return each seed with its neighbourhood
    grouped by edge type. The caller (you, or Claude) reads the subgraph.
    """
    toks = _tokens(question)
    scored: list[tuple[float, str]] = []
    for n in g:
        if n.type in ("resource", "artifact", "myth", "category"):
            continue
        label = n.label.casefold()
        label_words = set(re.findall(r"[a-z0-9][a-z0-9+#.-]*", label))
        hay_weak = " ".join(str(a) for a in (n.attrs.get("aliases") or [])).casefold()
        hay_weak += " " + str(n.attrs.get("definition") or "").casefold()
        hay_weak += " " + " ".join(n.attrs.get("code_symbols") or []).casefold()
        score = 0.0
        for t in toks:
            if t in label_words:
                score += 4
            elif t in label:
                score += 2.5
            elif t in hay_weak:
                score += 1
        if score > 0:
            # prefer glossary concepts and lessons, then shorter labels
            bonus = 0.5 if n.type == "lesson" or n.attrs.get("canonical") else 0
            scored.append((score + bonus - len(label) / 200, n.id))
    scored.sort(reverse=True)
    seeds = [nid for _s, nid in scored[:max_seeds]]
    result = {"question": question, "tokens": toks, "seeds": []}
    for nid in seeds:
        n = g.get(nid)
        groups = {}
        for etype, items in neighbors(g, nid).items():
            groups[etype] = [(d, o, g.get(o).label if g.get(o) else o) for d, o in items[:max_per_type]]
            if len(items) > max_per_type:
                groups[etype].append(("…", "", f"{len(items) - max_per_type} more"))
        result["seeds"].append({"id": nid, "type": n.type, "label": n.label,
                                "definition": n.attrs.get("definition") or n.attrs.get("hook") or "",
                                "neighbors": groups})
    return result


def format_ask(result: dict) -> str:
    lines = [f"Question: {result['question']}", f"Matched on: {', '.join(result['tokens']) or '(nothing)'}", ""]
    if not result["seeds"]:
        lines.append("No node matched. Try other words, or `kg search`.")
    for s in result["seeds"]:
        lines.append(f"## {s['label']}  [{s['type']}]  {s['id']}")
        if s["definition"]:
            lines.append(f"  {s['definition'][:300]}")
        for etype, items in s["neighbors"].items():
            lines.append(f"  {etype}:")
            for d, oid, label in items:
                lines.append(f"    {d} {label}" + (f"  ({oid})" if oid else ""))
        lines.append("")
    return "\n".join(lines)


def search(g: KnowledgeGraph, query: str, types: tuple[str, ...] | None = None, limit: int = 25) -> list[tuple[str, str]]:
    """Case-insensitive substring search over labels and aliases."""
    q = query.casefold()
    hits: list[tuple[str, str]] = []
    for n in g:
        if types and n.type not in types:
            continue
        hay = [n.label] + [str(a) for a in n.attrs.get("aliases", []) or []]
        if any(q in h.casefold() for h in hay):
            hits.append((n.id, n.label))
            if len(hits) >= limit:
                break
    return hits
