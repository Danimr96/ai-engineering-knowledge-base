"""Shared pytest fixtures.

``mini`` copies ``tests/fixtures/mini-root`` (a tiny AI-Education tree with
every format quirk we handle) into a temporary folder and returns ``Paths``
for it, so tests can build, export and even modify files freely.

``real`` returns ``Paths.default()`` if the actual upstream clone exists next
to this project, and skips the test otherwise. Only the smoke test uses it.
"""

from __future__ import annotations

import shutil
from pathlib import Path

import pytest

from kg.paths import Paths

FIXTURE_ROOT = Path(__file__).parent / "fixtures" / "mini-root"


@pytest.fixture
def mini(tmp_path: Path) -> Paths:
    root = tmp_path / "AI-Education"
    shutil.copytree(FIXTURE_ROOT, root)
    return Paths.for_root(root)


@pytest.fixture
def mini_graph(mini: Paths):
    from kg.build import build_graph

    g, stats = build_graph(mini)
    return g, stats, mini


@pytest.fixture
def real() -> Paths:
    paths = Paths.default()
    if not paths.phases_dir.is_dir():
        pytest.skip("upstream curriculum not present")
    return paths
