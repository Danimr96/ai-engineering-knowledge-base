"""kg.markdown: the parsing rules, one quirk per test."""

from kg.markdown import (
    find_links, find_section, parse_frontmatter, parse_lesson_header, parse_minutes, parse_tables,
    slugify, split_sections, split_table_row, strip_markdown,
)

DOC = """# Multi-Head Attention

> One head learns one relation. Eight heads learn eight.

**Type:** Build
**Languages:** Python
**Prerequisites:** Phase 7 · 02 (Self-Attention from Scratch)
**Time:** ~75 minutes

## The Problem

```python
# not a heading
x = 1
```

## Key Terms

| Term | What people say | What it actually means |
|------|-----------------|------------------------|
| Head | "A circuit" | One Q/K/V projection. |
| P(a \\| b) | "Conditional" | Escaped pipe inside. |
| Short row |

## Further Reading

- [Vaswani (2017)](https://arxiv.org/abs/1706.03762) — the original spec.
- Plain line without a link.
"""


def test_header_fields_and_lines():
    h = parse_lesson_header(DOC)
    assert h.title == "Multi-Head Attention" and h.title_line == 1
    assert h.hook.startswith("One head")
    assert h.fields["Type"] == "Build"
    assert h.fields["Prerequisites"] == "Phase 7 · 02 (Self-Attention from Scratch)"
    assert h.field_lines["Prerequisites"] == 7


def test_sections_ignore_headings_inside_code_fences():
    secs = split_sections(DOC)
    assert [s.heading for s in secs if s.level == 2] == ["The Problem", "Key Terms", "Further Reading"]
    assert secs[0].heading == "Multi-Head Attention" and secs[0].level == 1
    assert find_section(secs, "key terms").start_line == 17
    assert find_section(secs, "Nope") is None


def test_table_rows_keep_escaped_pipes_and_pad_short_rows():
    sec = find_section(split_sections(DOC), "Key Terms")
    tables = parse_tables(sec.lines, first_line_no=sec.start_line + 1)
    assert len(tables) == 1
    t = tables[0]
    assert t.header == ["Term", "What people say", "What it actually means"]
    assert t.rows[1].cells == ["P(a | b)", '"Conditional"', "Escaped pipe inside."]
    assert t.rows[2].cells == ["Short row", "", ""]
    assert t.rows[0].line == 21


def test_split_table_row_edge_cases():
    assert split_table_row("| a | b |") == ["a", "b"]
    assert split_table_row("a | b") == ["a", "b"]
    assert split_table_row("| `x \\| y` | z |") == ["`x | y`", "z"]


def test_links_with_trailing_text():
    sec = find_section(split_sections(DOC), "Further Reading")
    links = find_links(sec.lines, first_line_no=sec.start_line + 1)
    assert len(links) == 1
    assert links[0].text == "Vaswani (2017)"
    assert links[0].url == "https://arxiv.org/abs/1706.03762"
    assert links[0].trailing == "the original spec."


def test_frontmatter_subset():
    meta = parse_frontmatter('---\nname: x\ndescription: "quoted: yes"\ntags: [a, b]\n---\nbody')
    assert meta == {"name": "x", "description": "quoted: yes", "tags": ["a", "b"]}
    assert parse_frontmatter("no frontmatter") == {}


def test_small_utilities():
    assert strip_markdown("**KV** `cache` [link](http://x)") == "KV cache link"
    assert slugify("Math & training") == "math-and-training"
    assert parse_minutes("~75 minutes") == 75
    assert parse_minutes("30 hours") == 1800
    assert parse_minutes("~90 min") == 90
    assert parse_minutes("soon") is None
