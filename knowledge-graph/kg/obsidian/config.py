"""Obsidian configuration files and Bases tables written into the vault.

``.obsidian/graph.json``
    The graph view's settings. The only part that matters to us is
    ``colorGroups``: an ordered list of (search query, colour). The first query
    a note matches decides its colour, so status groups come before folder
    groups (a done lesson is green even though it sits in ``Lessons/``).

``.obsidian/app.json``
    ``userIgnoreFilters`` hides the ``Upstream/`` symlink from search and the
    graph (3,000 upstream files would swamp it) while keeping its notes
    openable through links.

``Bases/*.base``
    Bases is Obsidian's built-in table view (core plugin, 1.9+). A ``.base``
    file is YAML: which notes (``filters``) and which columns (``order``).
    They read the frontmatter properties the writer emits, so a lesson's
    ``status`` or a concept's ``taught_in`` becomes a sortable column.
"""

from __future__ import annotations

import json
from pathlib import Path


def _rgb(hex_color: str) -> dict:
    return {"a": 1, "rgb": int(hex_color.lstrip("#"), 16)}


GRAPH_COLOR_GROUPS = [
    ("tag:#status/done", "#3FB950"),
    ("tag:#status/planned", "#E3B341"),
    ("path:Phases", "#F85149"),
    ("path:Tracks", "#DB6D28"),
    ("path:Lessons", "#58A6FF"),
    ("path:Concepts tag:#concept/glossary", "#BC8CFF"),
    ("path:Concepts", "#8B949E"),
    ("path:Categories", "#D2A8FF"),
    ("path:Artifacts", "#39D353"),
    ("path:Resources", "#79C0FF"),
    ("path:Paths", "#FFA657"),
    ("path:Myths", "#FF7B72"),
    ("path:Libraries", "#56D4DD"),
    ("path:Communities", "#F778BA"),
    ("path:\"My Notes\"", "#F0F6FC"),
]


def graph_settings() -> dict:
    return {
        "collapse-filter": True,
        "search": "-path:Upstream",
        "showTags": False,
        "showAttachments": False,
        "hideUnresolved": True,
        "showOrphans": True,
        "collapse-color": False,
        "colorGroups": [{"query": q, "color": _rgb(c)} for q, c in GRAPH_COLOR_GROUPS],
        "collapse-display": True,
        "showArrow": True,
        "textFadeThreshold": -0.5,
        "nodeSizeMultiplier": 1.2,
        "lineSizeMultiplier": 0.8,
        "collapse-forces": True,
        "centerStrength": 0.45,
        "repelStrength": 12,
        "linkStrength": 0.9,
        "linkDistance": 220,
        "scale": 0.6,
        "close": False,
    }


def app_settings() -> dict:
    return {
        "userIgnoreFilters": ["Upstream/"],
        "showUnsupportedFiles": False,
        "newFileLocation": "folder",
        "newFileFolderPath": "My Notes",
        "attachmentFolderPath": "My Notes/attachments",
        "useMarkdownLinks": False,
        "alwaysUpdateLinks": True,
    }


# --------------------------------------------------------------------------
# Bases
# --------------------------------------------------------------------------

LESSONS_BASE = """\
filters:
  and:
    - file.inFolder("Lessons")
views:
  - type: table
    name: All lessons
    order:
      - file.name
      - phase
      - lesson_type
      - time_min
      - status
      - prereqs
      - concepts
      - community
      - libraries
    sort:
      - property: phase
        direction: ASC
      - property: num
        direction: ASC
  - type: table
    name: By community
    order:
      - file.name
      - community
      - phase
      - status
    sort:
      - property: community
        direction: ASC
      - property: phase
        direction: ASC
  - type: table
    name: Done
    filters:
      and:
        - status == "done"
    order:
      - file.name
      - phase
      - time_min
      - status
  - type: table
    name: Build lessons
    filters:
      and:
        - lesson_type == "build"
    order:
      - file.name
      - phase
      - time_min
      - status
    sort:
      - property: phase
        direction: ASC
      - property: num
        direction: ASC
"""

ROUTE_BASE = """\
filters:
  and:
    - file.inFolder("Lessons")
    - on_route == true
views:
  - type: table
    name: My route
    order:
      - route_order
      - file.name
      - time_min
      - status
      - prereqs
    sort:
      - property: route_order
        direction: ASC
  - type: table
    name: Not done yet
    filters:
      and:
        - status != "done"
    order:
      - route_order
      - file.name
      - time_min
      - status
    sort:
      - property: route_order
        direction: ASC
"""

CONCEPTS_BASE = """\
filters:
  and:
    - file.inFolder("Concepts")
views:
  - type: table
    name: Glossary concepts
    filters:
      and:
        - canonical == true
    order:
      - file.name
      - category
      - taught_in
    sort:
      - property: taught_in
        direction: DESC
  - type: table
    name: Lesson-only terms
    filters:
      and:
        - canonical == false
    order:
      - file.name
      - taught_in
    sort:
      - property: taught_in
        direction: DESC
  - type: table
    name: By category
    order:
      - file.name
      - category
      - taught_in
    sort:
      - property: category
        direction: ASC
      - property: file.name
        direction: ASC
"""

RESOURCES_BASE = """\
filters:
  and:
    - file.inFolder("Resources")
views:
  - type: table
    name: Most cited
    order:
      - file.name
      - kind
      - host
      - cited_by
    sort:
      - property: cited_by
        direction: DESC
"""

ARTIFACTS_BASE = """\
filters:
  and:
    - file.inFolder("Artifacts")
views:
  - type: table
    name: All artifacts
    order:
      - file.name
      - kind
      - lesson
      - version
    sort:
      - property: lesson
        direction: ASC
"""

LIBRARIES_BASE = """\
filters:
  and:
    - file.inFolder("Libraries")
views:
  - type: table
    name: Most used
    order:
      - file.name
      - language
      - used_by
    sort:
      - property: used_by
        direction: DESC
"""

COMMUNITIES_BASE = """\
filters:
  and:
    - file.inFolder("Communities")
views:
  - type: table
    name: Clusters
    order:
      - file.name
      - lessons
      - concepts
      - phases
    sort:
      - property: num
        direction: ASC
"""

BASES = {
    "Bases/Libraries.base": LIBRARIES_BASE,
    "Bases/Communities.base": COMMUNITIES_BASE,
    "Bases/Lessons.base": LESSONS_BASE,
    "Bases/My Route.base": ROUTE_BASE,
    "Bases/Concepts.base": CONCEPTS_BASE,
    "Bases/Resources.base": RESOURCES_BASE,
    "Bases/Artifacts.base": ARTIFACTS_BASE,
}


def write_config(vault: Path) -> list[Path]:
    """Write ``.obsidian/*.json`` and ``Bases/*.base``. Returns written paths."""
    written: list[Path] = []
    obsidian = vault / ".obsidian"
    obsidian.mkdir(parents=True, exist_ok=True)
    for name, data in (("graph.json", graph_settings()), ("app.json", app_settings())):
        p = obsidian / name
        # Do not clobber settings Obsidian has since changed, except on first run.
        if not p.exists():
            p.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
            written.append(p)
    for rel, text in BASES.items():
        p = vault / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        if not p.exists() or p.read_text(encoding="utf-8") != text:
            p.write_text(text, encoding="utf-8")
        written.append(p)
    return written
