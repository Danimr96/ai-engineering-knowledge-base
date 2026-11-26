"""Project ``graph.json`` into an Obsidian vault.

Obsidian's data model is simple: a folder of markdown files, where every file
is a node and every ``[[wiki-link]]`` is an edge. The graph view draws exactly
that. So exporting a property graph means:

* one note per node, in a folder per node type (``Lessons/``, ``Concepts/``);
* node attributes in the YAML frontmatter (Obsidian calls them properties,
  and Bases tables can sort and filter on them);
* every edge as a wiki-link inside a section named after the edge type, with
  the edge attributes (confidence, note) written next to the link, because a
  wiki-link itself cannot carry attributes.

Modules
-------
writer.py    note text for each node type
preserve.py  what survives a rebuild (your status, your notes below the marker)
config.py    ``.obsidian/`` settings (graph colours) and ``.base`` tables
export.py    the orchestrator: which nodes get a note, cleanup of stale notes
"""
