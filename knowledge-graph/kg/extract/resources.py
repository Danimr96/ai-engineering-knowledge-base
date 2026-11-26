"""Resource nodes (papers, docs, blog posts) and CITES edges.

Sources
-------
* every lesson's ``## Further Reading`` list of ``[Title](url) — why``
* the glossary's ``Sources`` bullets (called from ``glossary.py``)

The interesting query is "which lessons cite the same paper?". It only works
if the same paper always maps to the same node, so the core of this module is
``canonical_key``: it strips scheme, ``www.``, trailing slashes, fragments and
tracking parameters, and folds every arXiv URL form (``/abs/1706.03762``,
``/pdf/1706.03762v7``) into ``arxiv:1706.03762``. Without that step the ~2,300
links upstream become ~2,000 singleton nodes and the query never fires.
"""

from __future__ import annotations

import re
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

from kg.markdown import Link, find_links, find_section, split_sections
from kg.model import Edge, KnowledgeGraph, Node, resource_id
from kg.paths import Paths

_ARXIV_RE = re.compile(r"arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5}|[a-z\-]+/\d{7})(?:v\d+)?", re.IGNORECASE)
_DOI_RE = re.compile(r"doi\.org/(10\.\S+)", re.IGNORECASE)
_TRACKING_PARAMS = {"utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content", "ref", "fbclid", "gclid"}


def canonical_key(url: str) -> tuple[str, str]:
    """Return ``(key, kind)`` where kind is 'arxiv' | 'doi' | 'web'.

    ``https://arxiv.org/pdf/1706.03762v7`` -> ``('arxiv:1706.03762', 'arxiv')``
    ``https://www.Example.com/a/b/?utm_source=x#top`` -> ``('example.com/a/b', 'web')``
    """
    m = _ARXIV_RE.search(url)
    if m:
        return f"arxiv:{m.group(1).lower()}", "arxiv"
    m = _DOI_RE.search(url)
    if m:
        return f"doi:{m.group(1).rstrip('/').lower()}", "doi"
    parts = urlsplit(url.strip())
    host = parts.netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    path = re.sub(r"/+$", "", parts.path) or ""
    query = [(k, v) for k, v in parse_qsl(parts.query, keep_blank_values=True) if k not in _TRACKING_PARAMS]
    key = host + path
    if query:
        key += "?" + urlencode(sorted(query))
    return key, "web"


def _clean_title(text: str) -> str:
    # "Vaswani et al. (2017). Attention Is All You Need §3.2.2" -> keep as is,
    # but drop surrounding quotes and whitespace. The full text stays in attrs.
    return text.strip().strip('"“”').strip()


def add_resource(g: KnowledgeGraph, link: Link, *, source_file: str | None) -> str | None:
    """Create (or reuse) the resource node for a link. Returns its id, or None for non-http links."""
    url = link.url.strip()
    if not url.lower().startswith(("http://", "https://")):
        return None  # relative links to other lessons are handled elsewhere
    key, kind = canonical_key(url)
    rid = resource_id(key)
    if rid not in g:
        title = _clean_title(link.text) or key
        g.add_node(Node(id=rid, type="resource", label=title,
                        attrs={"title": title, "url": url, "kind": kind, "key": key, "host": urlsplit(url).netloc.lower()},
                        source_file=source_file, line=link.line))
    return rid


def extract_resources(g: KnowledgeGraph, paths: Paths) -> list[str]:
    """Further Reading of every lesson -> resource nodes + CITES edges."""
    problems: list[str] = []
    for lesson in g.nodes_of_type("lesson"):
        doc_rel = lesson.attrs.get("doc_path")
        if not doc_rel:
            continue
        text = (paths.root / doc_rel).read_text(encoding="utf-8")
        sec = find_section(split_sections(text), "Further Reading")
        if sec is None:
            continue
        for link in find_links(sec.lines, first_line_no=sec.start_line + 1):
            rid = add_resource(g, link, source_file=doc_rel)
            if rid is None:
                continue
            g.add_edge(Edge(src=lesson.id, dst=rid, type="CITES",
                            attrs={"note": link.trailing, "via": "further_reading"},
                            source_file=doc_rel, line=link.line))
    return problems
