"""Extractors: one module per source format.

Each extractor exposes a function ``extract_<thing>(graph, paths, ...)`` that
reads files under ``paths`` and adds nodes and edges to ``graph``. Extractors
never delete anything and never write to disk; ``kg.build`` decides the order
and persists the result.

Order matters because later extractors reference nodes created by earlier
ones (a REQUIRES edge needs both lesson nodes to exist):

    phases -> lessons -> tracks -> prereqs -> glossary -> key_terms
           -> artifacts -> resources -> learning_paths -> plan overlay
"""
