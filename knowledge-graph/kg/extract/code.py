"""Library nodes and USES edges from each lesson's ``code/`` folder.

Why this module exists
----------------------
Graphify's strongest feature is a code graph built from the AST. Lessons here
are standalone programs (no lesson imports another), so cross-file call graphs
would be empty. What *is* meaningful is which third-party libraries a lesson
leans on: "every lesson that touches torch", "the hono lessons", "pure-stdlib
lessons I can run anywhere". That is a lesson -> library relation, and it is
extracted deterministically:

* Python: the standard library ``ast`` module reads ``import x`` /
  ``from x import y``. Stdlib modules (``sys.stdlib_module_names``) and local
  modules (files in the same ``code/`` folder, ``main``, ``tests``) are skipped.
* TypeScript: a regex over ``import ... from "pkg"`` and ``require("pkg")``;
  ``node:`` builtins and relative paths are skipped.
* Rust: ``use crate_name::``; ``std``/``core``/``crate``/``self``/``super`` skipped.
* Julia: ``using``/``import`` lines; Julia's own stdlib packages skipped.

The lesson node also gains ``code_symbols`` (top-level functions and classes
in Python files) so ``kg search`` can find "where is `split_heads` defined".
"""

from __future__ import annotations

import ast
import re
import sys
from collections import defaultdict
from pathlib import Path

from kg.model import Edge, KnowledgeGraph, Node
from kg.paths import Paths

PY_STDLIB = set(getattr(sys, "stdlib_module_names", ())) | {"__future__", "typing_extensions"}
LOCAL_PY = {"main", "tests", "test_main", "conftest"}
JULIA_STDLIB = {"Base", "Core", "Random", "Statistics", "LinearAlgebra", "Printf", "Test", "Dates", "Logging",
                "SparseArrays", "Distributed", "Serialization", "Sockets", "Unicode", "InteractiveUtils", "Pkg"}
RUST_BUILTIN = {"std", "core", "alloc", "crate", "self", "super"}

_TS_IMPORT_RE = re.compile(r"""(?:from\s+|import\s+|require\()\s*['"]([^'"]+)['"]""")
_RS_USE_RE = re.compile(r"^\s*(?:pub\s+)?use\s+([A-Za-z_][A-Za-z0-9_]*)", re.MULTILINE)
_RS_EXTERN_RE = re.compile(r"^\s*extern\s+crate\s+([A-Za-z_][A-Za-z0-9_]*)", re.MULTILINE)
_JL_RE = re.compile(r"^\s*(?:using|import)\s+([A-Za-z_][A-Za-z0-9_]*(?:\s*,\s*[A-Za-z_][A-Za-z0-9_]*)*)", re.MULTILINE)

# Display names for packages whose import name differs from the project name.
_PY_DISPLAY = {"sklearn": "scikit-learn", "PIL": "Pillow", "cv2": "opencv", "yaml": "PyYAML", "bs4": "beautifulsoup4"}


def library_id(lang: str, name: str) -> str:
    return f"library:{lang}/{name}"


def python_imports(text: str) -> tuple[set[str], list[str]]:
    """Top-level imported package names and top-level function/class names."""
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return set(), []
    packages: set[str] = set()
    symbols: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                packages.add(alias.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            if node.level == 0 and node.module:  # relative imports are local by definition
                packages.add(node.module.split(".")[0])
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            symbols.append(node.name)
    return packages, symbols


def ts_imports(text: str) -> set[str]:
    out: set[str] = set()
    for m in _TS_IMPORT_RE.finditer(text):
        spec = m.group(1)
        if spec.startswith((".", "/", "node:")):
            continue
        # "@hono/node-server" -> "@hono/node-server"; "zod/v4" -> "zod"
        parts = spec.split("/")
        out.add("/".join(parts[:2]) if spec.startswith("@") else parts[0])
    return out


def rust_imports(text: str) -> set[str]:
    names = set(_RS_USE_RE.findall(text)) | set(_RS_EXTERN_RE.findall(text))
    return {n for n in names if n not in RUST_BUILTIN}


def julia_imports(text: str) -> set[str]:
    out: set[str] = set()
    for m in _JL_RE.finditer(text):
        for name in m.group(1).split(","):
            name = name.strip()
            if name and name not in JULIA_STDLIB:
                out.add(name)
    return out


def scan_code_dir(code_dir: Path) -> tuple[dict[tuple[str, str], list[str]], list[str]]:
    """``{(lang, package): [files...]}`` plus Python top-level symbols."""
    uses: dict[tuple[str, str], list[str]] = defaultdict(list)
    symbols: list[str] = []
    if not code_dir.is_dir():
        return uses, symbols
    local_py = {p.stem for p in code_dir.rglob("*.py")} | LOCAL_PY
    for path in sorted(code_dir.rglob("*")):
        if not path.is_file() or "__pycache__" in path.parts:
            continue
        rel = path.relative_to(code_dir).as_posix()
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if path.suffix == ".py":
            pkgs, syms = python_imports(text)
            if path.name == "main.py":
                symbols.extend(syms)
            for pkg in pkgs:
                if pkg in PY_STDLIB or pkg in local_py:
                    continue
                uses[("python", pkg)].append(rel)
        elif path.suffix in (".ts", ".tsx", ".js", ".mjs"):
            for pkg in ts_imports(text):
                uses[("typescript", pkg)].append(rel)
        elif path.suffix == ".rs":
            for pkg in rust_imports(text):
                uses[("rust", pkg)].append(rel)
        elif path.suffix == ".jl":
            for pkg in julia_imports(text):
                uses[("julia", pkg)].append(rel)
    return uses, symbols


def extract_code(g: KnowledgeGraph, paths: Paths) -> list[str]:
    problems: list[str] = []
    for lesson in g.nodes_of_type("lesson"):
        code_dir = paths.root / lesson.attrs["path"] / "code"
        uses, symbols = scan_code_dir(code_dir)
        lesson.attrs["code_symbols"] = symbols
        lesson.attrs["stdlib_only"] = bool(lesson.attrs.get("code_files")) and not any(
            lang == "python" for (lang, _pkg) in uses
        ) and any(f.endswith(".py") for f in lesson.attrs.get("code_files") or [])
        for (lang, pkg), files in sorted(uses.items()):
            lid = library_id(lang, pkg)
            if lid not in g:
                display = _PY_DISPLAY.get(pkg, pkg) if lang == "python" else pkg
                g.add_node(Node(id=lid, type="library", label=f"{display} ({lang})",
                                attrs={"name": display, "import_name": pkg, "language": lang},
                                source_file=paths.rel(code_dir / files[0]), line=1))
            g.add_edge(Edge(src=lesson.id, dst=lid, type="USES", attrs={"files": files, "count": len(files)},
                            source_file=paths.rel(code_dir / files[0]), line=None))
    return problems
