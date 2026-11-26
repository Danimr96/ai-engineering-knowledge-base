"""kg.obsidian: the vault projection and what survives a rebuild."""

import re

from kg.obsidian.export import MANIFEST, export_vault
from kg.obsidian.preserve import MARKER
from kg.obsidian.writer import safe_name

LINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")


def _all_links(vault):
    links = set()
    for md in vault.rglob("*.md"):
        if "My Notes" in md.parts:
            continue
        for m in LINK_RE.finditer(md.read_text(encoding="utf-8")):
            links.add(m.group(1))
    return links


def test_safe_name():
    assert safe_name('10/04 Pre-Training: "a/b" [x] #1?') == "10-04 Pre-Training- -a-b- -x- -1"
    assert len(safe_name("x" * 300)) <= 110


def test_export_writes_notes_and_every_link_resolves(mini_graph):
    g, _, paths = mini_graph
    n = export_vault(g, paths, min_concept_lessons=2, min_resource_lessons=2)
    vault = paths.vault_dir
    assert (vault / "Home.md").is_file()
    assert (vault / "Lessons" / "07-03 Multi-Head Attention.md").is_file()
    assert (vault / "Phases" / "07 Transformers Deep Dive.md").is_file()
    assert (vault / "Concepts" / "Attention.md").is_file()  # glossary concept
    assert (vault / "Concepts" / "Softmax.md").is_file()
    assert not (vault / "Concepts" / "Dot product.md").exists()  # lesson-only, 1 lesson: no note
    assert (vault / "Resources").is_dir()
    assert (vault / "Libraries" / "numpy (python).md").is_file()
    assert list((vault / "Communities").glob("*.md"))
    assert (vault / "Bases" / "Lessons.base").is_file()
    assert (vault / "Bases" / "Communities.base").is_file()
    assert (vault / ".obsidian" / "graph.json").is_file()
    assert (vault / "My Notes" / "README.md").is_file()
    assert (vault / MANIFEST).is_file()
    assert n > 20

    existing = {p.relative_to(vault).with_suffix("").as_posix() for p in vault.rglob("*.md")}
    existing |= {p.relative_to(vault).as_posix() for p in vault.rglob("*.base")}
    for target in _all_links(vault):
        if target.startswith("Upstream/"):
            continue
        assert target in existing, f"dangling link {target}"


def test_lesson_note_content(mini_graph):
    g, _, paths = mini_graph
    export_vault(g, paths)
    text = (paths.vault_dir / "Lessons" / "07-02 Self-Attention from Scratch.md").read_text(encoding="utf-8")
    assert text.startswith('---\nid: "lesson:07/02"\n')
    assert "status: done" in text and "status_auto: done" in text
    assert "  - 07/02\n" in text  # alias
    assert "[[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]]" in text
    assert "from override" in text  # the Calculus override is labelled
    assert "### Bridges to check first (my plan)" in text
    assert "Not understood by the parser: `Calculus`" in text
    assert "## Concepts taught" in text and "`glossary`" in text and "`lesson term`" in text
    assert "## Further reading" in text and "also cited by 1 other lesson" in text
    assert "## My route" in text and "Next: [[Lessons/07-03 Multi-Head Attention" in text
    assert "**Libraries:** [[Libraries/numpy (python)|numpy]]" in text and "[[Communities/" in text
    assert text.rstrip().endswith(MARKER)


def test_manual_status_and_notes_survive_rebuild(mini_graph):
    g, _, paths = mini_graph
    export_vault(g, paths)
    note = paths.vault_dir / "Lessons" / "19-30 BPE Tokenizer.md"
    text = note.read_text(encoding="utf-8")
    assert "status: planned" in text
    text = text.replace("status: planned", "status: in_progress", 1) + "\nMy reflection about tokenizers.\n"
    note.write_text(text, encoding="utf-8")

    export_vault(g, paths)
    text2 = note.read_text(encoding="utf-8")
    assert "status: in_progress" in text2 and "status_auto: planned" in text2
    assert text2.rstrip().endswith("My reflection about tokenizers.")
    assert "tags:\n" in text2 and "status/in_progress" in text2


def test_untouched_status_follows_the_build(mini_graph):
    g, _, paths = mini_graph
    export_vault(g, paths)
    note = paths.vault_dir / "Lessons" / "19-30 BPE Tokenizer.md"
    g.get("lesson:19/30").attrs["status"] = "done"  # as if evidence appeared
    export_vault(g, paths)
    assert "status: done" in note.read_text(encoding="utf-8")


def test_second_export_is_a_noop_and_stale_notes_are_removed(mini_graph):
    g, _, paths = mini_graph
    export_vault(g, paths)
    vault = paths.vault_dir
    snapshot = {p: p.read_text(encoding="utf-8") for p in vault.rglob("*.md")}
    mtimes = {p: p.stat().st_mtime_ns for p in snapshot}
    export_vault(g, paths)
    assert {p: p.read_text(encoding="utf-8") for p in vault.rglob("*.md")} == snapshot
    assert all(p.stat().st_mtime_ns == mtimes[p] for p in snapshot)

    mine = vault / "My Notes" / "keep me.md"
    mine.write_text("mine\n", encoding="utf-8")
    del g.nodes["myth:1"]
    export_vault(g, paths)
    assert not list((vault / "Myths").glob("*.md")) if (vault / "Myths").exists() else True
    assert mine.is_file()
