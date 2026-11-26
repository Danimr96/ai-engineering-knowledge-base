"""Knowledge graph of the AI Engineering from Scratch curriculum.

The package is a pipeline with three stages:

1. ``kg.extract`` reads the upstream curriculum (markdown, JSON, folder names)
   and produces nodes and edges. Each extractor owns exactly one source format.
2. ``kg.build`` runs the extractors in dependency order, validates the result
   and writes ``build/graph.json`` (the canonical graph) and ``build/report.md``
   (the quality report you read after every build).
3. ``kg.obsidian`` projects ``graph.json`` into an Obsidian vault: one note per
   node, wiki-links for edges, and a few Bases tables and graph colours.

``kg.graph_ops`` holds the traversal helpers (prerequisite chains, shared
concepts) used by both the CLI and the vault writer.
"""
