"""Lesson -> concept TEACHES edges from each lesson's ``## Key Terms`` table.

Source format (474 of 523 lessons)::

    ## Key Terms

    | Term | What people say | What it actually means |
    |------|-----------------|------------------------|
    | GQA  | "The default since Llama 2" | Grouped-Query Attention with ... |

Quirks handled here (found by surveying every table upstream):
* eight different header spellings: the *first* column is always the term
  and the *last* column is always the definition, so we never assume a
  fixed column index;
* escaped pipes inside cells (``\\|``) are handled by ``kg.markdown``;
* the term cell can carry markdown (``**bold**``, `` `code` ``) and
  "Name (ACR)" pairs.

Each row goes through ``ConceptIndex.match`` (see ``resolve.py``). A hit
produces a TEACHES edge to the canonical glossary concept with the match tier
recorded. A miss produces (or reuses) a non-canonical concept node keyed by
the normalised term, so that "KV cache" mentioned in six lessons is one node
with six TEACHES edges, not six nodes.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field

from kg.extract.resolve import ConceptIndex, normalize, split_parenthetical
from kg.markdown import find_section, parse_tables, split_sections, strip_markdown
from kg.model import Edge, KnowledgeGraph, Node, concept_id
from kg.paths import Paths


@dataclass
class KeyTermStats:
    rows: int = 0
    lessons_with_table: int = 0
    by_tier: Counter = field(default_factory=Counter)  # exact / alias / normalized / new
    unmatched: Counter = field(default_factory=Counter)  # display term -> occurrences


def _clean_term(cell: str) -> str:
    term = strip_markdown(cell).strip().strip("\"'“”")
    return term


def extract_key_terms(g: KnowledgeGraph, paths: Paths, index: ConceptIndex) -> tuple[KeyTermStats, list[str]]:
    stats = KeyTermStats()
    problems: list[str] = []
    for lesson in g.nodes_of_type("lesson"):
        doc_rel = lesson.attrs.get("doc_path")
        if not doc_rel:
            continue
        doc = paths.root / doc_rel
        text = doc.read_text(encoding="utf-8")
        sections = split_sections(text)
        sec = find_section(sections, "Key Terms")
        if sec is None:
            continue
        tables = parse_tables(sec.lines, first_line_no=sec.start_line + 1)
        if not tables:
            continue
        stats.lessons_with_table += 1
        for table in tables:
            if len(table.header) < 2:
                continue
            for row in table.rows:
                term = _clean_term(row.cells[0])
                definition = strip_markdown(row.cells[-1]) if len(row.cells) > 1 else ""
                folk = strip_markdown(row.cells[1]) if len(row.cells) > 2 else ""
                if not term or term.lower() in {"term", "—", "-"}:
                    continue
                stats.rows += 1
                hit = index.match(term)
                if hit is not None:
                    cid, tier = hit
                    stats.by_tier[tier] += 1
                    match_attrs = {"via": "key_terms", "match": tier, "term_as_written": term,
                                   "confidence": "high" if tier == "exact" else "medium"}
                else:
                    # Non-canonical concept: keyed by the normalised base name so
                    # spelling variants merge. The acronym becomes an alias.
                    base, paren = split_parenthetical(term)
                    # Only treat "(…)" as a detachable acronym when the base is
                    # a real name: "P(token | context)" must stay whole.
                    if len(base) < 3 or (paren and (" " in paren.strip() or len(paren) > 8)):
                        base, paren = term, None
                    key = normalize(base) or normalize(term)
                    if not key:
                        continue
                    cid = concept_id(key)
                    label = strip_markdown(base) if base else term
                    node = Node(
                        id=cid, type="concept", label=label,
                        attrs={"name": label, "canonical": False, "aliases": [paren] if paren else [],
                               "definition": definition, "folk_definition": folk or None,
                               "first_seen_in": lesson.attrs["ref"]},
                        source_file=doc_rel, line=row.line,
                    )
                    g.add_node(node, merge=True)
                    existing = g.get(cid)
                    if existing is not None and paren and paren not in existing.attrs.get("aliases", []):
                        existing.attrs.setdefault("aliases", []).append(paren)
                    stats.by_tier["new"] += 1
                    stats.unmatched[label] += 1
                    match_attrs = {"via": "key_terms", "match": "new", "term_as_written": term, "confidence": "medium"}
                match_attrs["definition"] = definition
                if folk:
                    match_attrs["folk_definition"] = folk
                g.add_edge(Edge(src=lesson.id, dst=cid, type="TEACHES", attrs=match_attrs,
                                source_file=doc_rel, line=row.line))
    return stats, problems
