# AI Engineering knowledge base and knowledge graph

A self-contained AI engineering knowledge base: a full open-source curriculum, a knowledge graph built on top of it, and two ways to explore it, a website that runs from a folder and an Obsidian vault. Clone it (or download the ZIP) and everything works offline, with no API keys and no Python dependencies beyond the standard library.

## What is inside

| Folder | What it is |
|---|---|
| [ai-engineering-from-scratch/](ai-engineering-from-scratch/) | The curriculum: 20 phases, 523 lessons, glossary, learning paths, certifications. A vendored copy of the MIT-licensed [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch). See [UPSTREAM.md](UPSTREAM.md). |
| [knowledge-graph/](knowledge-graph/) | The pipeline that turns the curriculum into a property graph, plus its outputs. Pure standard-library Python. |
| [knowledge-graph/build/graph.json](knowledge-graph/build/graph.json) | The graph itself: phases, lessons, concepts, artifacts, papers, libraries, communities, and typed edges (prerequisites, teaches, uses, cites) with provenance. Viewer-agnostic, ready to load into Neo4j or any other graph store. |
| [knowledge-graph/site/](knowledge-graph/site/) | The knowledge base as a website: curriculum map, every lesson with text, code, quiz, diagrams and interactive figures, glossary, syllabus planner, graph explorer. Plain files, no server. |
| [knowledge-graph/vault/](knowledge-graph/vault/) | The same graph as an Obsidian vault: one note per node, a wiki-link per edge, Bases tables and graph colour groups. |
| [MY-LEARNING-PLAN.md](MY-LEARNING-PLAN.md) | One learner's route through the curriculum (starts at Phase 10, with just-in-time bridge lessons). The graph overlays it as route, bridges and progress. Replace it with your own. |
| [lessons/](lessons/), [learning-artifacts/](learning-artifacts/) | Worked lessons: a visual explainer page per lesson plus complete, commented, tested code. |
| [.claude/skills/kg/](.claude/skills/kg/) | A Claude Code skill that makes Claude query the graph before answering curriculum questions. |

## Quick start

Read it, with nothing to install: open `knowledge-graph/site/index.html` in a browser. That is the whole knowledge base; it loads nothing from the network and keeps your progress in your own browser.

Prefer Obsidian? Install [Obsidian](https://obsidian.md), choose *Open folder as vault*, pick `knowledge-graph/vault` and start at `Home.md`.

Query the graph from a terminal (needs [uv](https://docs.astral.sh/uv/) and Python 3.12+):

```bash
cd knowledge-graph
./kg.sh prereqs 10/04                         # everything to know before a lesson
./kg.sh ask "which lessons cover the KV cache" # plain-language lookup, no LLM
./kg.sh search "attention" --type lesson
./kg.sh all                                    # rebuild graph.json, the vault and the site
./kg.sh html --single-file                     # the site as one self-contained HTML file
uv run pytest                                  # run the test suite
```

The full command list is in [knowledge-graph/README.md](knowledge-graph/README.md). The data model is in [SCHEMA.md](knowledge-graph/SCHEMA.md), the module-by-module walkthrough in [GUIDE.md](knowledge-graph/GUIDE.md), and the Obsidian recipes in [USING-THE-VAULT.md](knowledge-graph/USING-THE-VAULT.md).

## Sharing the site

- **A shared drive or a synced folder**: copy `knowledge-graph/site/` and open `index.html`.
- **One file**: the latest [release](../../releases) has `ai-engineering-knowledge-base.html`, about 25 MB with everything inside. Use this for SharePoint, which downloads `.html` files from a document library instead of displaying them: upload the file, readers download it and open it.
- **A web server**, if you have one: serve `knowledge-graph/site/` as static files.

## Using it as the base for an internal academy

- **Your own name on it.** Create `knowledge-graph/data/site.json` with a `title` and a `tagline`, then run `./kg.sh html`.
- **Syllabi.** *Plan a syllabus* on the site gives the ordered prerequisites for any target lessons and exports them as Markdown or CSV.
- **Tracking.** Each reader marks lessons as done and can save their progress to a file to send to whoever runs the course.

- **Cohorts and tracks.** `learning-paths/` in the curriculum and `knowledge-graph/data/tracks.json` define routes. `./kg.sh prereqs` and `./kg.sh path` give the prerequisite chain for any target lesson, which is what you need to design a syllabus that does not skip foundations.
- **Per-learner plans.** Each learner keeps their own `MY-LEARNING-PLAN.md`; `./kg.sh all` regenerates the vault with their route and progress. Notes in `vault/My Notes/` and anything below the `my notes` marker in a generated note survive rebuilds.
- **Your own content.** Add internal lessons under a new phase folder following `ai-engineering-from-scratch/LESSON_TEMPLATE.md` and rebuild; they join the graph like any other lesson. Hand-maintained inputs live in `knowledge-graph/data/` and are never overwritten.
- **A graph database.** `graph.json` is a plain list of nodes and typed edges, so a Neo4j loader is a short script.

## Platform notes

- `knowledge-graph/vault/Upstream` is a symbolic link to the curriculum's `phases/` folder so lesson texts open inside Obsidian. On Windows, clone with `git clone -c core.symlinks=true` (needs Developer Mode or an elevated shell); without it the vault still works, only that shortcut is missing. A ZIP download does not preserve the link either.
- Rebuilding the vault with `./kg.sh all` recreates the link.

## Licence and attribution

The curriculum in `ai-engineering-from-scratch/` is © 2026 Rohit Ghumare, MIT licence; its `LICENSE` file is kept in place and must stay with any copy. See [UPSTREAM.md](UPSTREAM.md) for the pinned version and how to update it.
