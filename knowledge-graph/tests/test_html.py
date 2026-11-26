"""kg.html: the markdown renderer, the start-up payload and the site export."""

import json
import re
from html.parser import HTMLParser

import pytest

from kg.html.data import PERSONAL_EDGES, ROUTE_PATH_ID, build_payload
from kg.html.export import SINGLE_FILE_NAME, export_site, inline_safe
from kg.html.lessons import FigureIndex, LinkResolver, build_lesson
from kg.html.render_md import render_markdown, strip_lesson_header
from kg.model import KnowledgeGraph
from kg.paths import Paths


class _ScriptCounter(HTMLParser):
    """Counts <script> elements, and any element that appears after <main>
    other than the expected ones (which would mean a script leaked markup)."""

    def __init__(self) -> None:
        super().__init__()
        self.scripts = 0
        self.after_main = False
        self.other_tags_after_main = 0

    def handle_starttag(self, tag, attrs):
        if tag == "script":
            self.scripts += 1
        elif self.after_main and tag not in ("noscript", "p"):
            self.other_tags_after_main += 1

    def handle_endtag(self, tag):
        if tag == "main":
            self.after_main = True


def html(text: str, **kw) -> str:
    return render_markdown(text, **kw).html


# ---- markdown -> HTML -------------------------------------------------------


def test_lesson_text_is_escaped_not_interpreted():
    out = html("The `<s>` token and a raw <image> tag, <script>alert(1)</script>.")
    assert "<code>&lt;s&gt;</code>" in out
    assert "&lt;image&gt;" in out
    assert "<script" not in out


def test_headings_get_unique_ids_and_a_toc():
    r = render_markdown("# Title\n\n## Build It\n\ntext\n\n### Step 1\n\n## Build It\n")
    assert '<h2 id="title">' in r.html  # the page owns the only <h1>
    assert '<h2 id="build-it">' in r.html and '<h2 id="build-it-2">' in r.html
    assert r.toc == [(2, "title", "Title"), (2, "build-it", "Build It"), (3, "step-1", "Step 1"), (2, "build-it-2", "Build It")]


def test_fences_code_mermaid_and_figure():
    r = render_markdown("```python\nx = a < b\n```\n\n```mermaid\ngraph TD\n A-->B\n```\n\n```figure\nkv-cache {\"n\": 2}\n```\n")
    assert '<pre class="code" data-lang="python"><code>x = a &lt; b</code></pre>' in r.html
    assert '<pre class="mermaid-src">graph TD\n A--&gt;B</pre>' in r.html
    assert 'class="lesson-figure" data-figure="kv-cache {&quot;n&quot;: 2}"' in r.html
    assert r.has_mermaid and r.figures == ["kv-cache"]


def test_a_longer_fence_can_hold_a_shorter_one():
    out = html("````markdown\n```python\nprint(1)\n```\n````\n\nafter")
    assert out.count("<pre") == 1 and "```python" in out and "<p>after</p>" in out


def test_nested_lists_and_code_inside_an_item():
    out = html("1. first\n   - inner a\n   - inner b\n2. second\n\n   ```bash\n   ls\n   ```\n\nparagraph")
    assert out.startswith("<ol>")
    assert "<li>first\n<ul>\n<li>inner a</li>\n<li>inner b</li>\n</ul></li>" in out
    assert '<pre class="code" data-lang="bash"><code>ls</code></pre>' in out
    assert out.endswith("<p>paragraph</p>")


def test_table_with_an_escaped_pipe_and_alignment():
    out = html("| Term | Value |\n|:--|--:|\n| P(a \\| b) | `x` |\n")
    assert "<th>Term</th>" in out and '<th class="al-right">Value</th>' in out
    assert "<td>P(a | b)</td>" in out and '<td class="al-right"><code>x</code></td>' in out


def test_links_only_go_where_they_are_allowed_to():
    resolve = lambda url: "#/lesson/07/02" if "self-attention" in url else None  # noqa: E731
    out = html(
        "[paper](https://arxiv.org/abs/1706.03762) [bad](javascript:alert(1)) "
        "[lesson](../02-self-attention/) [gone](../nowhere.md) [jump](#build-it)",
        resolve_link=resolve,
    )
    assert '<a href="https://arxiv.org/abs/1706.03762" target="_blank" rel="noopener">paper</a>' in out
    assert "javascript" not in out.replace("bad", "")  # label kept, target dropped
    assert '<a href="#/lesson/07/02">lesson</a>' in out
    assert "gone" in out and "nowhere" not in out
    assert 'data-anchor="build-it"' in out


def test_code_span_inside_a_link_label():
    # Regression: the label is rendered by a nested call that must share the
    # outer call's protected pieces.
    out = html("See [`torch.nn` docs](https://pytorch.org/docs) and `other`.")
    assert '<a href="https://pytorch.org/docs" target="_blank" rel="noopener"><code>torch.nn</code> docs</a>' in out
    assert "<code>other</code>" in out and "\x00" not in out


def test_emphasis_does_not_eat_identifiers_or_maths():
    out = html("**bold**, *it*, snake_case_name, 2 * 3 * 4, and __init__.")
    assert "<strong>bold</strong>" in out and "<em>it</em>" in out
    assert "snake_case_name" in out and "2 * 3 * 4" in out


def test_metadata_lines_keep_their_line_breaks():
    assert html("**Type:** Build\n**Time:** 90 minutes") == "<p><strong>Type:</strong> Build<br><strong>Time:</strong> 90 minutes</p>"


def test_strip_lesson_header_removes_title_hook_and_metadata():
    text = "# Title\n\n> The hook.\n\n**Type:** Build\n**Time:** ~90 minutes\n\n## The Problem\n\n> a real quote\n"
    assert strip_lesson_header(text) == "## The Problem\n\n> a real quote"


def test_callout_and_block_quote():
    out = html("> [!NOTE]\n> Careful.\n\n> plain\n> quote")
    assert '<blockquote class="callout callout-note"><p class="callout-label">Note</p><p>Careful.</p></blockquote>' in out
    assert "<blockquote><p>plain\nquote</p></blockquote>" in out


# ---- start-up payload ---------------------------------------------------------


def test_payload_is_for_every_reader_not_one_learner(mini_graph):
    g, _, paths = mini_graph
    payload = build_payload(g, paths, set())
    for node in payload["nodes"]:
        assert not {"status", "evidence", "on_route", "route_order"} & set(node["a"]), node["id"]
    assert not PERSONAL_EDGES & set(payload["edge_types"])
    # ...but the route itself survives, as one more path, bridges first.
    by_id = {n["id"]: i for i, n in enumerate(payload["nodes"])}
    assert ROUTE_PATH_ID in by_id
    includes = payload["edge_types"].index("INCLUDES")
    steps = sorted((e[3]["order"], payload["nodes"][e[1]]["id"], e[3]) for e in payload["edges"] if e[0] == by_id[ROUTE_PATH_ID] and e[2] == includes)
    assert steps, "the route path has lessons"
    assert all(payload["nodes"][by_id[lid]]["type"] == "lesson" for _, lid, _ in steps)
    assert any(a.get("required") is False and a["note"].startswith("Bridge for") for _, _, a in steps)


def test_payload_edges_point_at_existing_nodes(mini_graph):
    g, _, paths = mini_graph
    payload = build_payload(g, paths, {"lesson:07/02"})
    n = len(payload["nodes"])
    assert all(0 <= e[0] < n and 0 <= e[1] < n and 0 <= e[2] < len(payload["edge_types"]) for e in payload["edges"])
    flagged = [x["id"] for x in payload["nodes"] if x["a"].get("text")]
    assert flagged == ["lesson:07/02"]
    assert {str(x["a"]["num"]) for x in payload["nodes"] if x["type"] == "phase"} <= set(payload["phase_line"])


def test_site_json_overrides_the_title(mini_graph):
    g, _, paths = mini_graph
    (paths.data_dir / "site.json").write_text(json.dumps({"title": "Our academy"}), encoding="utf-8")
    assert build_payload(g, paths, set())["title"] == "Our academy"


# ---- lesson payloads ------------------------------------------------------------


def test_lesson_payload_has_text_code_and_quiz(mini_graph):
    g, _, paths = mini_graph
    content = build_lesson(g, paths, g.get("lesson:07/02"), LinkResolver(g, paths), FigureIndex.scan(paths))
    assert content is not None
    assert "Self-Attention from Scratch" not in content["html"]  # title is shown by the page header
    assert "<table>" in content["html"] and "P(token | context)" in content["html"]
    assert content["code"][0]["name"] == "main.py" and content["code"][0]["lang"] == "python"
    assert all("__pycache__" not in f["name"] for f in content["code"])
    assert content["quiz"] and {"q", "options", "correct", "why", "stage"} <= set(content["quiz"][0])


def test_lesson_payload_ships_its_artifacts(mini_graph):
    g, _, paths = mini_graph
    content = build_lesson(g, paths, g.get("lesson:07/03"), LinkResolver(g, paths), FigureIndex.scan(paths))
    assert content is not None and content["artifacts"]
    assert all(a["text"].strip() for a in content["artifacts"])


def test_relative_links_become_routes(mini_graph):
    g, _, paths = mini_graph
    links = LinkResolver(g, paths)
    doc_dir = "ai-engineering-from-scratch/phases/07-transformers/03-multi-head/docs"
    assert links.link(doc_dir, "../../02-self-attention/docs/en.md") == "#/lesson/07/02"
    assert links.link(doc_dir, "../../../01-math-foundations/") == "#/phase/1"
    assert links.link(doc_dir, "../../../../glossary/terms.md#attention") == "#/concepts"
    assert links.link(doc_dir, "../../../../../../etc/passwd") is None
    assert links.image(doc_dir, "../../../../../MY-LEARNING-PLAN.md") is None  # outside the curriculum


# ---- export -----------------------------------------------------------------------


def test_export_writes_a_site_that_needs_nothing_else(mini_graph):
    g, _, paths = mini_graph
    stats = export_site(g, paths)
    site = paths.site_dir
    index = (site / "index.html").read_text(encoding="utf-8")
    assert stats.lessons >= 5 and stats.single_file is None
    assert "<!--KG:" not in index and "{{TITLE}}" not in index
    # Everything the page loads is a relative path that exists.
    refs = re.findall(r'(?:src|href)="([^"#]+)"', index)
    assert refs and all(not r.startswith(("http", "//")) for r in refs if not r.startswith("data:"))
    for ref in refs:
        if not ref.startswith("data:"):
            assert (site / ref).is_file(), ref
    assert (site / "data" / "lessons" / "07-02.js").read_text(encoding="utf-8").startswith('window.__kgRes("data/lessons/07-02.js",{')
    assert (site / "assets" / "fonts" / "overpass-latin.woff2").is_file()
    graph_js = (site / "data" / "graph.js").read_text(encoding="utf-8")
    payload = json.loads(graph_js[len("window.KG_DATA="):].rstrip(";\n"))
    assert payload["nodes"] and payload["edges"]


def test_export_is_idempotent_and_removes_stale_files(mini_graph):
    g, _, paths = mini_graph
    export_site(g, paths)
    lesson = paths.site_dir / "data" / "lessons" / "07-02.js"
    stale = paths.site_dir / "data" / "lessons" / "99-99.js"
    stale.write_text("old", encoding="utf-8")
    mine = paths.site_dir / "NOTES.txt"  # outside the managed folders
    mine.write_text("keep", encoding="utf-8")
    before = lesson.stat().st_mtime_ns
    export_site(g, paths)
    assert lesson.stat().st_mtime_ns == before
    assert not stale.exists() and mine.read_text(encoding="utf-8") == "keep"


def test_single_file_inlines_everything(mini_graph):
    g, _, paths = mini_graph
    stats = export_site(g, paths, single_file=True)
    out = paths.dist_dir / SINGLE_FILE_NAME
    assert stats.single_file == out and stats.single_bytes == out.stat().st_size
    page = out.read_text(encoding="utf-8")
    assert not re.search(r'<script[^>]*\ssrc=', page) and '<link rel="stylesheet"' not in page
    assert 'data-res="data/lessons/07-02.js"' in page and 'data-res="vendor/mermaid.min.js"' in page
    assert "data:font/woff2;base64," in page and 'url("fonts/' not in page
    # Parsed the way a browser does, the page holds exactly the scripts we put
    # there: no payload ended its <script> early and spilled into the document.
    parser = _ScriptCounter()
    parser.feed(page)
    blocks = re.findall(r'^<script type="text/plain" data-res="', page, re.M)
    assert parser.scripts == len(blocks) + 2  # + graph data + the app
    assert parser.other_tags_after_main == 0


def test_inline_safe_neutralises_script_terminators():
    js = 'var a = "</script><!-- x --></SCRIPT>";'
    safe = inline_safe(js)
    assert "</script" not in safe.lower() and "<!--" not in safe
    assert safe == 'var a = "<\\/script><\\!-- x --><\\/SCRIPT>";'


@pytest.mark.slow
def test_real_curriculum_exports(real, tmp_path):
    if not real.graph_json.is_file():
        pytest.skip("graph.json not built")
    g = KnowledgeGraph.read_json(real.graph_json)
    stats = export_site(g, Paths.for_root(real.root, kg_dir=tmp_path))
    assert stats.lessons > 400
    for js in (tmp_path / "site" / "data" / "lessons").glob("*.js"):
        text = js.read_text(encoding="utf-8")
        body = json.loads(text[text.index(",") + 1 : text.rindex(")")])
        # Code samples may contain anything; the rendered lesson text may not.
        assert "\x00" not in body["html"] and "<script" not in body["html"].lower(), js.name
