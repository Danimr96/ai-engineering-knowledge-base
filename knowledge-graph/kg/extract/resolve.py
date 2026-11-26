"""Entity resolution for concepts: is "MHA" the same thing as "Multi-Head Attention"?

Why this module exists
----------------------
Concepts arrive from two places: the glossary (250 curated, canonical terms)
and the Key Terms table of each lesson (thousands of rows written by many
authors: "KV cache", "KV-Cache", "kv_cache", "Grouped-Query Attention (GQA)").
The graph is only useful if those rows land on the *same* concept node, and
on the glossary node when one exists. That is entity resolution, done here
with three deliberately simple tiers:

1. **exact**: the normalised term equals a normalised glossary heading.
2. **alias**: it equals a glossary alias, an acronym taken from the heading
   ("Automatic Speech Recognition (ASR)" -> "asr"), or an entry in the
   hand-maintained ``data/aliases.json``.
3. **normalized**: a looser variant matches (parenthetical stripped, or a
   conservative singular form).

Anything else becomes a *non-canonical* concept keyed by its normalised form,
so the same unmatched term used by several lessons still merges into one node.
There is no fuzzy or embedding matching on purpose: silent wrong merges are
worse than visible misses, and the report lists misses by frequency so you
can fill ``aliases.json`` top-down.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

from kg.markdown import strip_markdown

_PAREN_RE = re.compile(r"\s*\(([^)]*)\)\s*")
_NON_ALNUM_RE = re.compile(r"[^a-z0-9]+")


def normalize(term: str) -> str:
    """Canonical key for a term: lowercase, ASCII-ish, hyphen-separated.

    ``'Grouped-Query Attention (GQA)'`` -> ``'grouped-query-attention-gqa'``
    ``'KV cache'`` / ``'KV-Cache'`` / ``'kv_cache'`` -> ``'kv-cache'``
    """
    text = strip_markdown(term)
    text = text.replace("&", " and ").replace("+", " plus ")
    text = text.casefold()
    text = _NON_ALNUM_RE.sub("-", text).strip("-")
    return text


def split_parenthetical(term: str) -> tuple[str, str | None]:
    """``'Multi-Head Attention (MHA)'`` -> ``('Multi-Head Attention', 'MHA')``."""
    clean = strip_markdown(term)
    m = _PAREN_RE.search(clean)
    if not m:
        return clean, None
    base = (clean[: m.start()] + " " + clean[m.end() :]).strip()
    return base or clean, m.group(1).strip() or None


def singular(key: str) -> str | None:
    """Very conservative singularisation of a normalised key. None if unchanged.

    Only the last word is touched and only for the two most common English
    endings, so "series" or "bias" are never mangled.
    """
    if key.endswith("ies") and len(key) > 4:
        return key[:-3] + "y"
    if key.endswith("es") and key[:-2].endswith(("sh", "ch", "x", "ss")):
        return key[:-2]
    if key.endswith("s") and not key.endswith(("ss", "us", "is", "as", "os")) and len(key) > 3:
        return key[:-1]
    return None


def variants(term: str) -> list[tuple[str, str]]:
    """Ordered ``(key, tier)`` candidates to try for a Key Terms cell.

    The order encodes confidence: the first hit wins.
    """
    out: list[tuple[str, str]] = []
    full = normalize(term)
    if full:
        out.append((full, "exact"))
    base, paren = split_parenthetical(term)
    base_key = normalize(base)
    if base_key and base_key != full:
        out.append((base_key, "normalized"))
    if paren and len(paren) <= 8 and " " not in paren.strip():
        out.append((normalize(paren), "alias"))  # acronym in parentheses
    for key, _tier in list(out):
        s = singular(key)
        if s and (s, "normalized") not in out:
            out.append((s, "normalized"))
    return out


@dataclass
class ConceptIndex:
    """Lookup table from normalised keys to canonical concept IDs."""

    exact: dict[str, str] = field(default_factory=dict)  # key -> concept id
    alias: dict[str, str] = field(default_factory=dict)  # key -> concept id
    labels: dict[str, str] = field(default_factory=dict)  # concept id -> display name

    def add_canonical(self, concept_id: str, name: str, aliases: list[str] | None = None) -> None:
        self.labels[concept_id] = name
        self.exact[normalize(name)] = concept_id
        base, paren = split_parenthetical(name)
        base_key = normalize(base)
        if base_key and base_key not in self.exact:
            self.alias[base_key] = concept_id
        if paren and len(paren) <= 8 and " " not in paren.strip():
            self.alias.setdefault(normalize(paren), concept_id)
        for a in aliases or []:
            k = normalize(a)
            if k:
                self.alias.setdefault(k, concept_id)
        s = singular(normalize(name))
        if s:
            self.alias.setdefault(s, concept_id)

    def add_manual_aliases(self, table: dict[str, str]) -> list[str]:
        """``data/aliases.json``: ``{"raw term or key": "Glossary Heading"}``.

        Returns problems for aliases pointing at unknown glossary terms.
        """
        problems: list[str] = []
        by_name = {normalize(name): cid for cid, name in self.labels.items()}
        for raw, target in table.items():
            if raw.startswith("_"):
                continue
            cid = by_name.get(normalize(target))
            if cid is None:
                problems.append(f"aliases.json: {raw!r} -> unknown glossary term {target!r}")
                continue
            self.alias[normalize(raw)] = cid
        return problems

    def match(self, term: str) -> tuple[str, str] | None:
        """Return ``(concept_id, tier)`` or None. Tier is exact | alias | normalized."""
        for key, tier in variants(term):
            if key in self.exact:
                return self.exact[key], "exact" if tier == "exact" else tier
            if key in self.alias:
                return self.alias[key], "alias" if tier == "exact" else tier
        return None


def load_aliases(data_dir: Path) -> dict[str, str]:
    path = data_dir / "aliases.json"
    if not path.is_file():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))
