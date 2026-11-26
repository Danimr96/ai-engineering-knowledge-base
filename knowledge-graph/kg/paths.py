"""Where everything lives on disk.

Why this module exists
----------------------
Every extractor needs to know where the upstream curriculum is, where your own
files are (learning plan, visual lessons, artifacts) and where to write output.
Centralising those paths in one small object means:

* tests can point the whole pipeline at a tiny fixture tree by passing a
  different ``root`` (see ``tests/conftest.py``);
* no module hard-codes ``../ai-engineering-from-scratch`` and silently breaks
  when a folder moves.

The layout this object encodes::

    AI-Education/                      <- root
      MY-LEARNING-PLAN.md              <- your route and bridges
      lessons/                         <- your visual lesson pages (html)
      learning-artifacts/              <- your own code per lesson
      ai-engineering-from-scratch/     <- upstream clone, read-only
        README.md                      <- phase dependency graph (mermaid)
        phases/NN-slug/MM-slug/...     <- lessons
        glossary/terms.md, myths.md
        learning-paths/*.json
      knowledge-graph/                 <- this project
        data/                          <- hand-maintained inputs
        build/                         <- generated graph.json + report.md
        vault/                         <- generated Obsidian vault
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

# ``kg/paths.py`` -> ``knowledge-graph/`` -> ``AI-Education/``
_PACKAGE_DIR = Path(__file__).resolve().parent
_DEFAULT_KG_DIR = _PACKAGE_DIR.parent
_DEFAULT_ROOT = _DEFAULT_KG_DIR.parent


@dataclass(frozen=True)
class Paths:
    """All input and output locations, derived from a single ``root``.

    ``frozen=True`` makes the object immutable: once built for a run, nobody
    can accidentally redirect the output folder halfway through.
    """

    root: Path
    kg_dir: Path

    # ---- convenience constructors -------------------------------------
    @classmethod
    def default(cls) -> "Paths":
        """Paths for the real project, derived from this file's location."""
        return cls(root=_DEFAULT_ROOT, kg_dir=_DEFAULT_KG_DIR)

    @classmethod
    def for_root(cls, root: Path, kg_dir: Path | None = None) -> "Paths":
        """Paths for an arbitrary root (used by tests with a fixture tree).

        ``kg_dir`` defaults to ``<root>/knowledge-graph`` so a temporary root
        gets its own ``data/``, ``build/`` and ``vault/`` folders.
        """
        root = Path(root).resolve()
        return cls(root=root, kg_dir=(kg_dir or root / "knowledge-graph").resolve())

    # ---- upstream curriculum (read-only) ------------------------------
    @property
    def upstream(self) -> Path:
        return self.root / "ai-engineering-from-scratch"

    @property
    def phases_dir(self) -> Path:
        return self.upstream / "phases"

    @property
    def readme(self) -> Path:
        return self.upstream / "README.md"

    @property
    def glossary_terms(self) -> Path:
        return self.upstream / "glossary" / "terms.md"

    @property
    def glossary_myths(self) -> Path:
        return self.upstream / "glossary" / "myths.md"

    @property
    def learning_paths_dir(self) -> Path:
        return self.upstream / "learning-paths"

    # ---- your own files -----------------------------------------------
    @property
    def learning_plan(self) -> Path:
        return self.root / "MY-LEARNING-PLAN.md"

    @property
    def visual_lessons_dir(self) -> Path:
        return self.root / "lessons"

    @property
    def learning_artifacts_dir(self) -> Path:
        return self.root / "learning-artifacts"

    # ---- this project -------------------------------------------------
    @property
    def data_dir(self) -> Path:
        """Hand-maintained inputs. The build never writes here."""
        return self.kg_dir / "data"

    @property
    def build_dir(self) -> Path:
        return self.kg_dir / "build"

    @property
    def graph_json(self) -> Path:
        return self.build_dir / "graph.json"

    @property
    def report_md(self) -> Path:
        return self.build_dir / "report.md"

    @property
    def vault_dir(self) -> Path:
        return self.kg_dir / "vault"

    # ---- helpers ------------------------------------------------------
    def rel(self, path: Path) -> str:
        """Path relative to ``root`` as a POSIX string, for provenance fields.

        Provenance must be stable across machines, so we never store absolute
        paths in ``graph.json``.
        """
        try:
            return Path(path).resolve().relative_to(self.root).as_posix()
        except ValueError:
            return Path(path).as_posix()
