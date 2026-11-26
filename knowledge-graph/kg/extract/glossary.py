"""Canonical concepts from ``glossary/terms.md`` and myths from ``glossary/myths.md``.

Source format (terms.md)::

    ### Adam (Optimizer)
    - **Category:** Math & training
    - **What people say:** The optimizer you use without thinking about it.
    - **What it actually means:** Adaptive Moment Estimation. ...
    - **Common confusion:** ...
    - **Sources:** [Adam paper](https://arxiv.org/abs/1412.6980)
    - **Related terms:** AdamW, Optimizer, Learning Rate
    - **Learn it:** [Activation Functions](../phases/03-deep-learning-core/04-activation-functions/)
    - **Aliases:** ...

What we produce
---------------
* one ``concept`` node per ``### Term`` (``canonical: true``)
* one ``category`` node per distinct Category, with IN_CATEGORY edges
* RELATED_TO edges from "Related terms" (every one of the 935 references
  resolves by case-insensitive match, verified during exploration)
* TEACHES edges (lesson -> concept, ``via: glossary_learn_it``) from "Learn it"
* CITES edges (concept -> resource) from "Sources"
* one ``myth`` node per ``## "..."`` section in myths.md
"""

from __future__ import annotations

import re

from kg.extract.resolve import ConceptIndex, normalize
from kg.extract.resources import add_resource
from kg.markdown import Link, find_links, slugify, split_sections, strip_markdown
from kg.model import Edge, KnowledgeGraph, Node, category_id, concept_id, lesson_id, myth_id
from kg.paths import Paths

_BULLET_RE = re.compile(r"^-\s+\*\*([^*]+?):\*\*\s*(.*)$")
_LEARN_IT_RE = re.compile(r"\.\./phases/(\d{2})-[^/]+/(\d{2})-[^/)]+/?")

# Bullet label -> attribute name on the concept node
_FIELD_MAP = {
    "What it actually means": "definition",
    "What people say": "folk_definition",
    "Why it matters": "why_it_matters",
    "In practice": "in_practice",
    "Common confusion": "confusion",
    "Why it's called that": "etymology",
}


def _split_terms(value: str) -> list[str]:
    """``'AdamW, Optimizer, Learning Rate'`` -> list. Commas inside () are kept."""
    out: list[str] = []
    depth = 0
    cur: list[str] = []
    for ch in value:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth = max(0, depth - 1)
        if ch == "," and depth == 0:
            out.append("".join(cur).strip())
            cur = []
        else:
            cur.append(ch)
    if cur:
        out.append("".join(cur).strip())
    return [strip_markdown(t) for t in out if t.strip()]


def extract_glossary(g: KnowledgeGraph, paths: Paths) -> tuple[ConceptIndex, list[str]]:
    """Add concept, category and myth nodes. Returns the index for Key Terms matching."""
    problems: list[str] = []
    index = ConceptIndex()
    if not paths.glossary_terms.is_file():
        problems.append(f"glossary not found: {paths.glossary_terms}")
        return index, problems

    src = paths.rel(paths.glossary_terms)
    text = paths.glossary_terms.read_text(encoding="utf-8")
    entries = [s for s in split_sections(text) if s.level == 3]

    # Pass 1: nodes (so RELATED_TO in pass 2 can resolve forward references)
    parsed: list[tuple[Node, dict[str, str], dict[str, int]]] = []
    for sec in entries:
        name = strip_markdown(sec.heading)
        fields: dict[str, str] = {}
        field_lines: dict[str, int] = {}
        for offset, line in enumerate(sec.lines):
            m = _BULLET_RE.match(line.strip())
            if m:
                fields[m.group(1).strip()] = m.group(2).strip()
                field_lines[m.group(1).strip()] = sec.start_line + 1 + offset
        aliases = _split_terms(fields.get("Aliases", "")) if fields.get("Aliases") else []
        cid = concept_id(normalize(name))
        attrs = {
            "name": name,
            "canonical": True,
            "category": fields.get("Category"),
            "aliases": aliases,
        }
        for label, attr in _FIELD_MAP.items():
            if fields.get(label):
                attrs[attr] = strip_markdown(fields[label]) if attr != "definition" else fields[label]
        node = Node(id=cid, type="concept", label=name, attrs=attrs, source_file=src, line=sec.start_line)
        if cid in g:
            problems.append(f"glossary: duplicate normalised term {name!r} ({src}:{sec.start_line})")
            continue
        g.add_node(node)
        index.add_canonical(cid, name, aliases)
        parsed.append((node, fields, field_lines))

    # Pass 2: edges
    for node, fields, field_lines in parsed:
        cat = fields.get("Category")
        if cat:
            catid = category_id(slugify(cat))
            if catid not in g:
                g.add_node(Node(id=catid, type="category", label=cat, attrs={"name": cat}, source_file=src, line=node.line))
            g.add_edge(Edge(src=node.id, dst=catid, type="IN_CATEGORY", source_file=src, line=field_lines.get("Category")))

        for rel in _split_terms(fields.get("Related terms", "")):
            hit = index.match(rel)
            if hit is None:
                problems.append(f"glossary: related term {rel!r} of {node.label!r} not found")
                continue
            if hit[0] != node.id:
                g.add_edge(Edge(src=node.id, dst=hit[0], type="RELATED_TO", attrs={"via": "glossary"},
                                source_file=src, line=field_lines.get("Related terms")))

        learn = fields.get("Learn it")
        if learn:
            for m in _LEARN_IT_RE.finditer(learn):
                lid = lesson_id(int(m.group(1)), int(m.group(2)))
                if lid not in g:
                    problems.append(f"glossary: Learn it for {node.label!r} points at missing lesson {lid}")
                    continue
                g.add_edge(Edge(src=lid, dst=node.id, type="TEACHES",
                                attrs={"via": "glossary_learn_it", "match": "exact", "confidence": "high"},
                                source_file=src, line=field_lines.get("Learn it")))

        sources = fields.get("Sources")
        if sources:
            for link in find_links([sources], field_lines.get("Sources") or node.line or 1):
                rid = add_resource(g, link, source_file=src)
                if rid:
                    g.add_edge(Edge(src=node.id, dst=rid, type="CITES", attrs={"note": link.trailing, "via": "glossary"},
                                    source_file=src, line=link.line))

    problems.extend(_extract_myths(g, paths))
    return index, problems


def _extract_myths(g: KnowledgeGraph, paths: Paths) -> list[str]:
    if not paths.glossary_myths.is_file():
        return []
    src = paths.rel(paths.glossary_myths)
    text = paths.glossary_myths.read_text(encoding="utf-8")
    n = 0
    for sec in split_sections(text):
        if sec.level != 2:
            continue
        n += 1
        claim = sec.heading.strip().strip('"“”')
        reality = why = ""
        for line in sec.lines:
            s = line.strip()
            if s.startswith("**Reality:**"):
                reality = s[len("**Reality:**"):].strip()
            elif s.startswith("**Why it matters:**"):
                why = s[len("**Why it matters:**"):].strip()
        g.add_node(Node(id=myth_id(n), type="myth", label=f"Myth: {claim}",
                        attrs={"claim": claim, "reality": reality, "why_it_matters": why},
                        source_file=src, line=sec.start_line))
    return []
