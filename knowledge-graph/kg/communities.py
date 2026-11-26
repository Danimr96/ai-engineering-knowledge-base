"""Community detection: which lessons and concepts cluster together.

Why this module exists
----------------------
Phases are the *author's* grouping. Communities are the grouping the data
itself suggests: lessons that teach the same concepts, require each other,
or are bridged in your plan end up in the same cluster, even across phases.
Graphify does this with the Leiden algorithm; we use **label propagation**,
which is forty lines of standard library, deterministic once seeded, and good
enough to surface "the attention cluster" or "the MCP cluster".

How label propagation works
---------------------------
1. Every node starts with its own label.
2. Visit nodes in a shuffled (seeded) order; each node adopts the label most
   common among its neighbours, breaking ties deterministically.
3. Repeat until no label changes. Nodes sharing a label form a community.

Labels are LLM-free: the top concepts by degree inside the community, so a
community reads as "Attention · KV Cache · Softmax" rather than "community 7".

What goes into the graph used for clustering
--------------------------------------------
Lessons and concepts as nodes; TEACHES (only concepts taught by at least two
lessons, otherwise every one-off term is a leaf that adds noise), REQUIRES,
BRIDGE and RELATED_TO as undirected edges. Phases, resources and artifacts
are left out on purpose: CONTAINS edges would just reproduce the phases.
"""

from __future__ import annotations

import random
from collections import Counter, defaultdict

from kg.model import Edge, KnowledgeGraph, Node

CLUSTER_EDGE_TYPES = ("TEACHES", "REQUIRES", "BRIDGE", "RELATED_TO")
MIN_COMMUNITY_SIZE = 4


def build_undirected(g: KnowledgeGraph, min_concept_lessons: int = 2) -> dict[str, set[str]]:
    taught_by: Counter = Counter(e.dst for e in g.edges if e.type == "TEACHES")
    adj: dict[str, set[str]] = defaultdict(set)
    for e in g.edges:
        if e.type not in CLUSTER_EDGE_TYPES:
            continue
        if e.type == "TEACHES" and taught_by[e.dst] < min_concept_lessons:
            continue
        adj[e.src].add(e.dst)
        adj[e.dst].add(e.src)
    return adj


def label_propagation(adj: dict[str, set[str]], seed: int = 42, max_iter: int = 100) -> dict[str, int]:
    """Return ``{node: label}``. Deterministic for a given seed and graph."""
    nodes = sorted(adj)
    labels = {n: i for i, n in enumerate(nodes)}
    rng = random.Random(seed)
    order = list(nodes)
    for _ in range(max_iter):
        rng.shuffle(order)
        changed = 0
        for n in order:
            counts = Counter(labels[m] for m in adj[n])
            if not counts:
                continue
            best = max(counts.values())
            candidates = sorted(l for l, c in counts.items() if c == best)
            if labels[n] not in candidates:
                labels[n] = candidates[rng.randrange(len(candidates))]
                changed += 1
        if changed == 0:
            break
    return labels


def community_label(g: KnowledgeGraph, members: list[str], adj: dict[str, set[str]], k: int = 3) -> str:
    """Top-k concepts by degree inside the community; glossary terms first."""
    member_set = set(members)
    scored = []
    for m in members:
        n = g.get(m)
        if n is None or n.type != "concept":
            continue
        internal = len(adj.get(m, set()) & member_set)
        scored.append((n.attrs.get("canonical", False), internal, n.label))
    scored.sort(key=lambda t: (-int(t[0]), -t[1], t[2]))
    names = [name for _c, _d, name in scored[:k]]
    if not names:  # a community with no concept: use lesson titles
        names = [g.get(m).attrs.get("title", m) for m in members[:k] if g.get(m)]
    return " · ".join(names)


def detect_communities(g: KnowledgeGraph, seed: int = 42) -> list[str]:
    """Add ``community`` nodes and IN_COMMUNITY edges; set ``community`` attrs."""
    adj = build_undirected(g)
    labels = label_propagation(adj, seed=seed)
    groups: dict[int, list[str]] = defaultdict(list)
    for node, label in labels.items():
        groups[label].append(node)
    ordered = sorted((members for members in groups.values() if len(members) >= MIN_COMMUNITY_SIZE),
                     key=lambda ms: (-len(ms), ms[0]))
    src = "knowledge-graph/kg/communities.py"
    for num, members in enumerate(ordered, start=1):
        members.sort()
        lessons = [m for m in members if m.startswith("lesson:")]
        concepts = [m for m in members if m.startswith("concept:")]
        phases = Counter(g.get(m).attrs["phase"] for m in lessons if g.get(m))
        label = community_label(g, members, adj)
        cid = f"community:{num}"
        g.add_node(Node(id=cid, type="community", label=f"{num:02d} {label}",
                        attrs={"num": num, "name": label, "size": len(members), "lessons": len(lessons),
                               "concepts": len(concepts), "phases": sorted(phases),
                               "main_phase": phases.most_common(1)[0][0] if phases else None},
                        source_file=src, line=None))
        for m in members:
            n = g.get(m)
            if n is None:
                continue
            n.attrs["community"] = num
            g.add_edge(Edge(src=m, dst=cid, type="IN_COMMUNITY", source_file=src, line=None))
    return []
