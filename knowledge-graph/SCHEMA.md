# Schema

The graph is a **property graph**: nodes and edges both have a type, a label, a free-form `attrs` dictionary, and provenance (`source_file`, `line`). This is the same model Neo4j uses, so `graph.json` can be loaded there without reshaping.

## Identity

IDs are built from the **numeric folder prefixes**, never from slugs or titles, because upstream may rename a folder but will not renumber it.

| Node type | ID pattern | Example |
|---|---|---|
| phase | `phase:<num>` | `phase:10` |
| lesson | `lesson:<PP>/<LL>` | `lesson:10/04` |
| track | `track:<PP>/<letter>` | `track:19/B` |
| concept | `concept:<normalized name>` | `concept:kv-cache` |
| category | `category:<slug>` | `category:models-and-inference` |
| artifact | `artifact:<PP>/<LL>/<slug>` | `artifact:07/03/mha-configurator` |
| resource | `resource:<canonical key>` | `resource:arxiv:1706.03762` |
| learning_path | `path:<id>` | `path:applied-ai-engineer` |
| myth | `myth:<n>` | `myth:3` |
| library | `library:<language>/<import name>` | `library:python/torch` |
| community | `community:<n>` (sorted by size) | `community:12` |

Concept normalisation (`kg/extract/resolve.py`): lowercase, `&` → `and`, every run of non-alphanumerics → `-`. So `KV cache`, `KV-Cache` and `kv_cache` are one node.

Resource canonicalisation (`kg/extract/resources.py`): any arXiv URL form → `arxiv:<id>` (version suffix dropped), `doi.org/...` → `doi:...`, otherwise host + path without scheme, `www.`, trailing slash, fragment or tracking parameters.

## Nodes

| Type | Key attributes |
|---|---|
| phase | `num`, `title`, `hours` (from ROADMAP.md), `path` |
| lesson | `phase`, `num`, `ref` (`10/04`), `title`, `hook`, `lesson_type` (build / learn / learn+build / capstone / reference), `type_raw`, `languages[]`, `time_min`, `prereq_raw`, `prereq_unparsed[]`, `code_files[]`, `quiz_count`, `path`, `doc_path`, plus overlay: `status` (done / planned / null), `evidence[]`, `on_route`, `route_order`, `route_section` |
| track | `phase`, `letter`, `title`, `start`, `end` (from `data/tracks.json`) |
| concept | `name`, `canonical` (true = glossary term), `category`, `aliases[]`, `definition`, `folk_definition`, `why_it_matters`, `in_practice`, `confusion`; non-canonical also `first_seen_in` |
| category | `name` (one of the 12 glossary categories) |
| artifact | `name`, `kind` (skill / prompt / agent), `description`, `version`, `tags[]`, `bundle`, `path`, `lesson` |
| resource | `title`, `url`, `kind` (arxiv / doi / web), `key`, `host` |
| learning_path | `key`, `title`, `summary`, `kind`, `minutes`, `path` |
| myth | `claim`, `reality`, `why_it_matters` |
| library | `name`, `import_name`, `language` (python / typescript / rust / julia); third-party only, stdlib and local modules excluded |
| community | `num`, `name` (top three concepts by internal degree), `size`, `lessons`, `concepts`, `phases`, `main_phase`; from label propagation, see `kg/communities.py` |

Lessons also carry `code_symbols` (top-level functions and classes in `main.py`) and `stdlib_only`.

Quiz questions and code files are attributes of the lesson, not nodes: they connect to exactly one lesson and would only add leaves. Tags on artifacts are attributes too; in the vault they become Obsidian tags.

## Edges

Prerequisite edges point **backwards in time**: `10/04 REQUIRES 07/02` means "learn 07/02 first".

| Type | From → To | Attributes |
|---|---|---|
| CONTAINS | phase → lesson, track → lesson | `order` |
| PHASE_REQUIRES | phase → phase | from the mermaid DAG in README.md |
| REQUIRES | lesson → lesson | `raw` (the whole field), `span` (the fragment), `confidence`, `group` (shared by the lessons of one range or track), `note`, `via` (header / track / override) |
| REQUIRES_PHASE | lesson → phase | same, plus `whole_phase` when a range covered every lesson on disk |
| TEACHES | lesson → concept | `via` (key_terms / glossary_learn_it), `match` (exact / alias / normalized / new), `term_as_written`, `definition` (the lesson's own wording), `confidence` |
| RELATED_TO | concept → concept | from the glossary's *Related terms* |
| IN_CATEGORY | concept → category | |
| SHIPS | lesson → artifact | |
| CITES | lesson → resource, concept → resource | `note` (the text after the link), `via` (further_reading / glossary) |
| INCLUDES | learning_path → lesson | `order`, `required`, `minutes` |
| BRIDGE | lesson → lesson | `note`; from the *Bridges* column of MY-LEARNING-PLAN.md |
| ROUTE_NEXT | lesson → lesson | reading order of MY-LEARNING-PLAN.md route tables |
| USES | lesson → library | `files[]`, `count`; from imports parsed with `ast` (Python) or regexes (TS, Rust, Julia) |
| IN_COMMUNITY | lesson / concept → community | assigned by label propagation over TEACHES, REQUIRES, BRIDGE, RELATED_TO |

Edge identity for de-duplication is `(src, dst, type, via, term_as_written)`: two Key Terms rows that map to the same glossary concept are two pieces of evidence and stay two edges.

### Confidence

| Level | Meaning |
|---|---|
| high | an explicit lesson number in the source text, or a glossary exact match |
| medium | a whole phase, a range that turned out to be a whole phase, "all of this phase", an alias or normalised concept match |
| low | a Phase 19 *track* reference (the source text is inconsistent about track ranges) or an entry from `data/prereq_overrides.json` |

## Provenance

Every node and edge carries `source_file` (relative to `AI-Education/`) and `line`. For a REQUIRES edge that is the line of the `**Prerequisites:**` field; for a TEACHES edge from Key Terms it is the table row. `build/graph.json` also records `meta.upstream_commit`, the short hash of the upstream clone the graph reflects.

## Validation

`KnowledgeGraph.validate()` (in `kg/model.py`) returns a list of problems and the build refuses to exit 0 while it is non-empty:

- every edge endpoint exists (no dangling references);
- endpoint types match the table above;
- no self-loops on REQUIRES / BRIDGE / ROUTE_NEXT;
- `confidence`, when present, is high / medium / low.

## Vault projection

| Graph | Vault |
|---|---|
| node | one note in `<Folder>/` (Phases, Lessons, Tracks, Concepts, Categories, Artifacts, Resources, Paths, Myths) |
| node attrs | YAML frontmatter (properties), prose attributes in the body |
| edge | a wiki-link inside a section named after the edge type, with confidence / note / tier written next to it |
| lesson `ref` | note aliases `10/04` and `10-04`, so `[[10-04]]` resolves |
| status, phase, type | Obsidian tags `status/done`, `phase/10`, `type/build`, `route` (drive the graph colours) |

Notes always link with the full path form `[[Lessons/10-04 Title|10/04 Title]]`; a bare `[[Title]]` would be ambiguous across folders.

Which nodes get a note: every phase, lesson, track, category, path, myth, artifact and glossary concept. A **non-canonical concept** (a Key Terms row that matched no glossary heading) and a **resource** only get a note when at least two lessons point at them (`--min-concept-lessons`, `--min-resource-lessons`). The rest stay in `graph.json` and appear as plain text inside the lesson notes.

### Round-trip rules

1. `status` in a lesson note is yours once it differs from `status_auto`.
2. Text below `%% ── my notes ── %%` is copied verbatim into the regenerated note.
3. `My Notes/` is never written or deleted by the exporter.
4. `.obsidian/graph.json` and `app.json` are written only if missing, so settings you change in Obsidian stick. `Bases/*.base` are regenerated.
5. A manifest (`vault/.kg-manifest.json`) lists what the last export wrote; only files in it can be deleted as stale.
