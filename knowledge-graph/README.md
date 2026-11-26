# AI Engineering from Scratch — knowledge graph

Turns the curriculum in `../ai-engineering-from-scratch/` (20 phases, 523 lessons, 250 glossary terms, ~500 artifacts, ~1,700 cited resources, 35 third-party libraries, ~95 detected communities) plus your own `../MY-LEARNING-PLAN.md` into:

1. **`build/graph.json`** — a property graph (nodes, typed edges, provenance on everything). Viewer-agnostic; the seed for the Neo4j project later.
2. **`build/report.md`** — the quality report: counts, what the parsers could not place, alias candidates. Read it after every build.
3. **`vault/`** — an Obsidian vault: one note per node, wiki-links per edge, Bases tables, graph colours, and a symlink to the upstream lesson texts.

Read **[GUIDE.md](GUIDE.md)** for the walkthrough of every module and the reasoning behind each decision, and **[SCHEMA.md](SCHEMA.md)** for the data model.

## Quick start

```bash
cd knowledge-graph
./kg.sh all            # build graph.json + report.md, then export the vault
uv run pytest          # 97 tests (unit tests on a fixture repo + a smoke test on the real one)
```

Then in Obsidian: *Open folder as vault* → pick `knowledge-graph/vault`. Start at `Home.md`.
Open the graph view and use the colour groups (done = green, planned = yellow, phases = red, lessons = blue, glossary concepts = purple).

`./kg.sh` is a two-line launcher for `uv run python -m kg.cli`. Both forms work.

## Commands

| Command | What it does |
|---|---|
| `./kg.sh build` | extract everything → `build/graph.json`, `build/report.md` |
| `./kg.sh export` | `graph.json` → `vault/` (keeps your edited `status` and your notes below the marker) |
| `./kg.sh all` | build then export |
| `./kg.sh report` | print the report |
| `./kg.sh prereqs 10/04 [--depth N]` | everything to know before a lesson, by depth |
| `./kg.sh dependents 07/02` | lessons that build on one |
| `./kg.sh path 10/04 01/01` | shortest prerequisite chain between two lessons |
| `./kg.sh concepts 07/03` | concepts a lesson teaches, with match tier |
| `./kg.sh search "attention" [--type lesson]` | find nodes by label, alias or code symbol |
| `./kg.sh ask "which lessons cover the KV cache"` | plain-language question → matching nodes with their neighbourhoods (no LLM) |
| `./kg.sh neighbors concept:kv-cache` | every edge touching a node, grouped by type |
| `./kg.sh info 10/04` / `info concept:kv-cache` | dump a node with all its edges |

See [USING-THE-VAULT.md](USING-THE-VAULT.md) for the Obsidian side (graph filters, Bases, local graph, study loop) and how Claude uses the graph through the `kg` project skill in `../.claude/skills/kg/`.

`export` takes `--min-concept-lessons N` and `--min-resource-lessons N` (default 2): a lesson-only term or a cited paper gets its own note only when at least N lessons point at it. Everything is still in `graph.json` and listed inside the lesson notes.

## Layout

```text
kg/                 the pipeline (see GUIDE.md)
  extract/          one module per upstream source format
  overlay/          your plan, bridges and progress
  obsidian/         vault writer, round-trip rules, Obsidian config and Bases
data/               hand-maintained inputs, never overwritten:
  tracks.json         Phase 19 track letters → lesson ranges
  aliases.json        Key Terms spellings → glossary headings
  prereq_overrides.json  prerequisite edges the parser cannot infer
build/              generated: graph.json, report.md
vault/              generated Obsidian vault (+ your untouched My Notes/)
tests/              one test module per source module; fixtures/mini-root is a tiny curriculum
```

## What survives a rebuild

- In a lesson note, a `status` you edited by hand (it is compared with `status_auto`).
- Everything below the `%% ── my notes ── %%` line in any generated note.
- Everything in `vault/My Notes/`.
- Everything in `data/`.

Everything else in `vault/` and `build/` is regenerated from upstream on every run, which is what lets you `git pull` the curriculum and rebuild without losing your work.

## Upstream is read-only

Nothing here writes into `../ai-engineering-from-scratch/`. The vault's `Upstream/` entry is a symlink to its `phases/` folder so lesson texts open inside Obsidian; it is excluded from search and the graph view via `.obsidian/app.json`.
