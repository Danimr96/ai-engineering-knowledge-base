"""kg.extract.code: library detection per language."""

from kg.extract.code import julia_imports, python_imports, rust_imports, ts_imports


def test_python_imports_skip_stdlib_and_collect_symbols():
    pkgs, syms = python_imports("import math\nimport numpy as np\nfrom torch.nn import Linear\nfrom . import local\n\ndef f():\n    pass\nclass C:\n    pass\n")
    assert pkgs == {"math", "numpy", "torch"}  # stdlib filtering happens in scan_code_dir
    assert syms == ["f", "C"]
    assert python_imports("def broken(:\n") == (set(), [])


def test_ts_rust_julia_imports():
    assert ts_imports('import { Hono } from "hono";\nimport x from "zod/v4";\nimport t from "node:test";\nimport y from "./local";\nconst a = require("@hono/node-server/serve");') == {"hono", "zod", "@hono/node-server"}
    assert rust_imports("use std::io;\nuse rand::Rng;\nextern crate serde;\n") == {"rand", "serde"}
    assert julia_imports("using Random, Statistics\nusing Flux\nimport CUDA\n") == {"Flux", "CUDA"}


def test_uses_edges_on_fixture(mini_graph):
    g, _, _ = mini_graph
    uses = {(e.src, e.dst): e for e in g.edges if e.type == "USES"}
    assert ("lesson:07/02", "library:python/numpy") in uses
    assert ("lesson:07/02", "library:python/torch") in uses
    assert ("lesson:07/03", "library:typescript/hono") in uses
    assert ("lesson:07/03", "library:typescript/zod") in uses
    assert not any(dst.endswith("/node:test") or dst.endswith("/math") for _s, dst in uses)
    assert ("lesson:01/02", "library:python/numpy") in uses
    assert not any(dst == "library:python/main" for _s, dst in uses)  # local module skipped
    lesson = g.get("lesson:07/02")
    assert lesson.attrs["code_symbols"] == ["softmax", "SelfAttention"]
    assert lesson.attrs["stdlib_only"] is False
    assert g.get("library:python/numpy").attrs["name"] == "numpy"
