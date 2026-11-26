# Guide: how the knowledge graph is built, and why each piece exists

This is the walkthrough. Read it once top to bottom with the code open next to it; afterwards, `build/report.md` and the module docstrings are enough.

The short version: **three stages, one direction of data flow.**

```text
upstream markdown/JSON  ──extract──▶  graph.json  ──export──▶  Obsidian vault
MY-LEARNING-PLAN.md     ──overlay──▶      ▲
data/*.json (yours)     ───────────────────┘
```

Nothing flows backwards. Upstream is never written. `graph.json` is never edited by hand. The vault is regenerated, except for the parts the round-trip rules protect (your `status`, your notes below the marker, `My Notes/`).

---

## 1. Why a graph at all

A curriculum is already a graph, it is just hidden in prose: "Prerequisites: Phase 7 · 02", "Related terms: KV Cache, Softmax", "Further Reading: Vaswani 2017". Reading it linearly you only ever see one edge at a time. Extracting the edges lets you ask questions the folder tree cannot answer:

- What do I actually need before 10/04, transitively? (`./kg.sh prereqs 10/04`)
- Which lessons cite the same paper as this one? (`Resources/` notes)
- Which concept appears in the most lessons? (report, "Concepts taught by the most lessons")
- Where is "KV cache" taught, and does every lesson mean the same thing by it? (`Concepts/KV Cache`)
- What is next on *my* route, and which bridges are still pending? (`Bases/My Route.base`)

You do this kind of modelling at work. The difference here is that you own every step, so when an edge looks wrong you can trace it to the line of markdown that produced it.

## 2. The model (`kg/model.py`)

Two dataclasses and a container. It is the contract every other module obeys.

**Property graph.** `Node(id, type, label, attrs, source_file, line)` and `Edge(src, dst, type, attrs, source_file, line)`. Free-form `attrs` on both. This is exactly Neo4j's model, which is the point: your next project can load `graph.json` with one `UNWIND` per type.

**Closed vocabularies.** `NODE_TYPES` and `EDGE_TYPES` are frozen sets, and `EDGE_TYPES` also records which node types an edge may connect. Adding a type means adding it there first. The benefit shows up immediately: an extractor with a typo (`"Lesson"` vs `"lesson"`) fails at `add_node`, not three modules later.

**IDs before anything else.** `lesson:10/04` comes from the numeric folder prefixes. Slugs and titles are labels, not identity, because upstream can rename `04-pre-training-mini-gpt` but will not renumber it. The ID helpers live in this module so no two extractors can spell the same thing differently. This is the single most important decision in any KG: if identity is unstable, every later merge is wrong.

**Provenance everywhere.** Every node and edge records the file and line that produced it. It costs nothing at build time and is what makes the vault debuggable: a strange prerequisite edge points you to `docs/en.md:7`.

**Validation returns a list, it does not raise.** `validate()` collects every dangling endpoint, type mismatch, self-loop and bad confidence value. The report shows them all at once; the build exits non-zero if the list is not empty.

**Determinism.** `write_json` sorts nodes, edges and keys. If upstream did not change, a rebuild is byte-identical, so `diff build/graph.json` after a `git pull` shows exactly what the pull changed.

## 3. Markdown helpers (`kg/markdown.py`)

No markdown library. The curriculum uses a handful of conventions, and writing them out as small functions makes the rules visible and testable. The quirks were found by surveying every file upstream, not guessed:

- **Header block**: `# Title`, `> hook`, then `**Field:** value` lines. There is no YAML frontmatter in lessons; `parse_lesson_header` records the line number of each field so edges can cite it.
- **Sections** split on `## ` headings but *ignore headings inside code fences*: lesson bodies contain Python with `# comment` lines.
- **Tables**: cells are split on a pipe that is *not* preceded by a backslash. Upstream has 52 cells like `P(token_n \| token_0)`; a naive `split("|")` silently shifts every column after them. Short rows are padded, not dropped.
- **Links** keep the trailing text ("— the MQA paper"), which is the human explanation of the citation.
- **Frontmatter** parser handles exactly what artifact files use (`key: value`, quoted strings, inline lists). Modelled on upstream's `scripts/_lib.py`, re-implemented so it is ours.

## 4. Extractors (`kg/extract/`)

One module per source format. Each exposes `extract_<thing>(graph, paths)`, reads files, adds nodes and edges, returns a list of problems. They never write to disk and never delete. `kg/build.py` fixes their order, because later ones reference nodes created by earlier ones.

### 4.1 Phases (`phases.py`)

Phase nodes from the `NN-slug` folders. Title from the phase README's H1 (better than the slug), hours from `ROADMAP.md`. The phase-level DAG comes from the mermaid block in the upstream `README.md` (`P5 --> P7`); the same regex upstream's `site/build.js` uses. We read the source, not the generated `site/data.js`, because parsing generated JavaScript is brittle.

Note the direction flip: mermaid arrows point forward in time, our `PHASE_REQUIRES` points backward (7 requires 5). Prerequisite edges always point at what to learn *first*; keeping one convention across the whole graph is what makes the BFS in `graph_ops.py` trivial.

### 4.2 Lessons (`lessons.py`)

Lesson nodes from `NN-slug/MM-slug` folders plus the header block. Two normalisations worth seeing:

- `**Type:**` has eleven spellings upstream ("Build", "Learn + Build", "Build (Capstone)", "Learn + lab"). We keep the raw string and add a five-value `lesson_type` for filtering.
- `**Languages:** Python (stdlib)` drops the qualifier; "none", "--" and "—" all mean no code.

The `Prerequisites` field is stored raw here and parsed in the next module. Splitting "read the field" from "interpret the field" keeps each part testable.

Tracks (Phase 19 only) come from `data/tracks.json`, hand-made, because the source text refers to "Track B foundations" but no file upstream defines what that is. The ranges were read off the folder names; the text is inconsistent about them, which is why edges built from a bare track reference get confidence `low`.

### 4.3 Prerequisites (`prereqs.py`), the hard one

The field is free text in at least a dozen shapes (see the module docstring for the list). The comma alone means four different things. So this is a **scanner with state**, not a regex:

1. Walk the string left to right. At each position try the most specific pattern first: `Phases 14 · 32 to 14 · 40`, then `Phase N`, then `Lesson(s) N`, then `Track X`, then a parenthetical, then a separator, then a word.
2. Remember the last phase mentioned ("sticky phase") so a bare `Lesson 09` after `Phase 11 Lesson 01` knows it is 11/09.
3. Parse a lesson list as a whole before attaching it, because a trailing "of this phase" ("Lessons 30 and 31 of this phase") changes the phase of *every* item.
4. A phase mention followed by explicit lessons is a container, not a requirement on the whole phase: "Phase 1, Lessons 01-04" produces four lesson edges, not a phase edge. "Phase 10 (LLMs from Scratch)" alone produces a phase edge.
5. A parenthetical is parsed as a list only if it looks like one ("(Lessons 09 Information Theory, 06 Probability)", "(04, 06, 07)"); otherwise it becomes the `note` of the previous reference.
6. "Track C lessons 42-49": the explicit numbers win and the track is ignored. "Track B foundations, lessons 70 and 71": both count. The rule is whether a comma separates them.
7. Whatever remains is residue. Filler words ("safety lessons", "foundations") are dropped; the rest is reported as *unparsed* and attached to the lesson. On the real repo that is five fragments in 523 lessons: `Calculus`, `Don't skip`, `basic NumPy`, `basic PyTorch familiarity`, `using MCP revision`.

`parse_prereq_text` is a pure function (text in, refs out), which is why `tests/test_prereqs_parse.py` can be a table of forty real strings. `resolve` then checks the refs against the lessons that exist: ranges expand to one edge per existing lesson sharing a `group`; a range that covers the whole phase collapses to `REQUIRES_PHASE`; missing lessons become problems, never invented nodes; "All of Phase 14" written inside Phase 14 means "the earlier lessons of this phase".

`data/prereq_overrides.json` is the escape hatch for the fragments the parser cannot resolve ("Phase 1 · Calculus" → 01/04). Edges from it carry `via: override` and confidence `low` so they are visibly different in the vault.

**Ratchet tests.** `tests/test_build_smoke.py` asserts *at most 6* unparsed fragments on the real repo, not exactly 5. Lower bounds that only move in one direction survive `git pull`; exact counts do not.

### 4.4 Glossary (`glossary.py`)

The 250 `### Term` entries are the canonical concepts. Each bullet (`- **Category:** …`) becomes an attribute; `Related terms` become RELATED_TO edges (all 935 references resolve, checked); `Learn it` links become TEACHES edges with `via: glossary_learn_it`; `Sources` become resource nodes. The 12 categories are nodes so the vault can colour and group by them. `myths.md` gives 21 myth nodes, unconnected for now: they are worth reading, not worth guessing edges for.

### 4.5 Entity resolution (`resolve.py`, `key_terms.py`)

This is the part you will recognise from work. Each of 473 lessons has a Key Terms table (3,801 rows) written by many authors: "KV cache", "KV-Cache", "kv_cache", "Grouped-Query Attention (GQA)". Two questions per row: *is this a glossary term?* and *if not, is it the same as a row in another lesson?*

Three tiers, in confidence order, first hit wins:

1. **exact** – the normalised term equals a normalised glossary heading.
2. **alias** – it equals a glossary alias, the acronym in a heading's parentheses ("ASR"), the heading without its parentheses, or an entry in your `data/aliases.json`.
3. **normalized** – a looser form matches: parenthetical stripped, or a conservative singular.

A miss creates a *non-canonical* concept keyed by the normalised name, so the same unmatched term used by six lessons is one node with six edges, not six nodes. Its acronym is kept as an alias.

What is deliberately *not* here: fuzzy string distance and embedding similarity. A silent wrong merge (two ideas glued into one node) is worse than a visible miss, and misses are visible: the report lists unmatched terms by frequency. That list is your to-do for `aliases.json`, top-down. The first build matched 9% of rows; that is the honest number, because the glossary has 250 terms and the lessons use 2,961 distinct ones. The 91% are real concepts too, just not curated ones.

`Edge.key()` includes the term as written, so a table that lists both "MHA" and "Attention" and maps both to the glossary's *Attention* keeps two edges: two rows, two pieces of evidence.

### 4.6 Artifacts, resources, learning paths

- **Artifacts** (`artifacts.py`): every `outputs/skill-*.md`, `prompt-*.md`, `agent-*.md` and skill bundle. Their `tags` stay attributes and become Obsidian tags; a tag node with 40 neighbours would only clutter the graph.
- **Resources** (`resources.py`): Further Reading links. The interesting query ("which lessons cite the same paper") only works if the same paper is always the same node, so `canonical_key` folds `arxiv.org/abs/1706.03762`, `/pdf/1706.03762v7` and friends into `arxiv:1706.03762`, strips `www.`, trailing slashes, fragments and tracking parameters. Result: 359 resources cited by two or more lessons; without canonicalisation most of them would be singletons.
- **Learning paths** (`learning_paths.py`): the 12 upstream routes. Three JSON shapes exist; we read only the five keys they share.

### 4.7 Your overlay (`overlay/plan.py`)

Everything above describes the curriculum. This module describes *you*, and lives in its own package so the separation is visible in the tree:

- route tables in `MY-LEARNING-PLAN.md` (any `## Route…` section) → `ROUTE_NEXT` chain in reading order;
- every `NN/MM` token in the bridges column → a `BRIDGE` edge with the words after it as note;
- progress evidence: `lessons/NN-MM-*.html` and `learning-artifacts/NN-MM-*/` mark a lesson `done`; on the route without evidence → `planned`.

### 4.8 Code and libraries (`extract/code.py`)

Borrowed from Graphify's strongest idea, adapted to our data. Lessons are standalone programs, so a call graph across lessons would be empty; what carries meaning is which third-party libraries a lesson leans on. Python imports are read with the standard `ast` module (deterministic, no regex fragility), filtered against `sys.stdlib_module_names` and the lesson's own modules; TypeScript, Rust and Julia use small regexes with their builtins excluded. Result: `library` nodes, `USES` edges, a `stdlib_only` flag (389 of the Python lessons need nothing installed) and `code_symbols` on each lesson so `search` and `ask` can find where a function is defined.

### 4.9 Communities (`communities.py`)

Phases are the author's grouping; communities are the grouping the data suggests. Label propagation (forty lines, seeded, deterministic) runs over an undirected graph of lessons and concepts joined by TEACHES (concepts taught by at least two lessons), REQUIRES, BRIDGE and RELATED_TO. Clusters of four or more members become `community` nodes with `IN_COMMUNITY` edges, tags `community/NN` in the vault, and a label made of the three most connected concepts inside them, so a cluster reads "Attention · Cross-Attention · Self-Attention" without any LLM. The interesting ones are those spanning several phases: they are the real themes of the curriculum, as opposed to its table of contents.

## 5. Assembly, report, traversal

**`build.py`** runs the extractors in dependency order, validates, stamps the upstream commit hash, writes `graph.json` and `report.md`. It is short on purpose: the order *is* the design and should fit on one screen.

**`report.py`** is the habit that keeps the graph honest. After every build, read it in this order: counts (are there still 20 phases and 523 lessons?), validation (must be empty), extractor problems, unparsed fragments (candidates for overrides), key-term statistics (candidates for aliases), shared resources (proof canonicalisation works), concept hubs.

**`graph_ops.py`** is breadth-first search in several costumes: transitive prerequisites by depth, dependents, shortest chain between two lessons, shared concepts. Pure Python, no networkx, so the algorithms stay readable. When you load `graph.json` into Neo4j, `prereqs_of` becomes `MATCH (l)-[:REQUIRES*1..3]->(p)`.

`ask` is the query surface, the counterpart of Graphify's `query`: it scores every node against the words of a question (label words count 4, substrings 2.5, aliases, definitions and code symbols 1), takes the best five as seeds and prints each with its neighbourhood grouped by edge type. No LLM is involved; the reader (you or Claude) does the reasoning over a subgraph small enough to read. The project skill in `AI-Education/.claude/skills/kg/SKILL.md` tells Claude to run it before answering curriculum questions, which is how the graph gets used rather than merely browsed.

## 6. The vault (`kg/obsidian/`)

Obsidian's data model is simple: a folder of markdown files, where every file is a node and every `[[wiki-link]]` is an edge. So exporting a property graph means:

- **one note per node**, in a folder per type; note names start with the numeric ref so they sort in curriculum order;
- **properties in frontmatter** (`status`, `phase`, `time_min`, `taught_in`…), which is what Bases tables sort and filter on;
- **edges as wiki-links** inside a section named after the edge type. A wiki-link cannot carry attributes, so confidence, note and match tier are written next to the link;
- **full-path links** (`[[Lessons/10-04 Title|10/04 Title]]`). A bare `[[Title]]` is ambiguous when two folders hold the same name, and ambiguity is exactly what a KG must not have. The export test checks that every one of the 17,864 links resolves.

**What gets a note.** All phases, lessons, tracks, categories, paths, myths, artifacts and glossary concepts. Non-canonical concepts and resources only when at least two lessons point at them (CLI flags). The rest stays in `graph.json` and appears as plain text inside lesson notes. The vault is a *projection* of the graph, tuned for reading; the graph is the complete record.

**Naming before rendering.** Every note's path is decided first (`Naming`), then notes are rendered, so any renderer can link to any node without caring whether its note is written yet.

**Round-trip** (`preserve.py`). Every export rewrites every note, which is what makes `git pull` safe. Two things survive: a `status` you edited (detected because it differs from `status_auto`, the value the build computed last time) and everything below `%% ── my notes ── %%`, an Obsidian comment so the marker is invisible in reading view. `My Notes/` is never touched. A manifest lists what the exporter wrote, so only those files can be deleted as stale. Unchanged files are not rewritten, so a second export is a no-op you can verify with `diff`.

**Config** (`config.py`). `.obsidian/graph.json` colour groups are an ordered list of search queries; the first match wins, so `tag:#status/done` comes before `path:Lessons`. `.obsidian/app.json` hides `Upstream/` (a symlink to the upstream `phases/` folder) from search and the graph while keeping its notes openable, so the lesson text renders inside Obsidian with its mermaid diagrams. Bases files are YAML: a global `filters` block, then `views` with `order` (columns) and `sort`.

## 7. Using it

1. `./kg.sh all`, open `vault/` in Obsidian, start at `Home.md`.
2. Graph view: filter `path:Lessons` to see the prerequisite skeleton; `tag:#route` for your route; `path:Concepts tag:#concept/glossary` for the curated concept map.
3. In a lesson note: *Prerequisites* (stated), *Bridges* (yours), *Before this lesson* (transitive), *Builds on this*, *Concepts taught* with the lesson's own wording, *Further reading* with "also cited by N other lessons".
4. When you finish a lesson: either create `learning-artifacts/NN-MM-*/` (auto-detected) or edit `status:` in the note. Write your reflection below the marker.
5. After `git pull` upstream: `./kg.sh all`, read `report.md`, `diff` the vault if curious.
6. To improve matching: take the top unmatched terms from the report and add the ones that really are glossary terms to `data/aliases.json`. To fix a prerequisite the parser cannot read: `data/prereq_overrides.json`.

## 8. What to take from this project

- **Identity first.** Stable IDs from the numeric prefixes made every later merge trivial. Pick the wrong key and no amount of parsing fixes it.
- **Provenance is cheap and priceless.** Two fields per record; every surprising edge became a five-second check.
- **Parsers need a report, not just tests.** Tests prove the cases you thought of; the unparsed list shows the ones you did not.
- **Visible misses beat silent merges.** Three matching tiers and an alias file you curate, instead of fuzzy matching you cannot audit.
- **Derived data is disposable; human data is not.** The build regenerates everything, and three explicit rules protect what is yours.
- **Ratchets, not exact counts**, for tests against a moving source.

## 9. Next

- Load `graph.json` into Neo4j: one constraint per label on `id`, one `UNWIND … MERGE` per node type, one per edge type. The model needs no reshaping. That is the seed of the next project.
- Embedding similarity between lessons or concepts as a separate, clearly labelled edge type (`SIMILAR_TO`, with the score as an attribute), never merged into the curated ones.
- Certification lessons (`certifications/claude/`) with their own explicit prerequisite JSON.
