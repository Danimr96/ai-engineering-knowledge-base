# Using the vault

How to get answers out of `vault/` in Obsidian, and how Claude uses the same graph from the terminal.

## Open it

Obsidian → *Open folder as vault* → `AI-Education/knowledge-graph/vault`. Start at `Home.md`. Everything you see is generated except: the text below the `%% ── my notes ── %%` line of any note, `My Notes/`, and any settings you change in Obsidian (graph colours, appearance).

## Five ways to read the graph

**1. The graph view** (`Ctrl/Cmd+G`). Colours are preset: green = done, yellow = planned, red = phases, blue = lessons, purple = glossary concepts, grey = lesson-only terms, pink = communities, cyan = libraries. Useful filters in the search box at the top of the graph pane:

| Filter | Shows |
|---|---|
| `path:Lessons` | the prerequisite skeleton (lessons linked by REQUIRES / BRIDGE / ROUTE_NEXT) |
| `tag:#route` | your route only |
| `path:Lessons tag:#phase/10` | one phase |
| `path:Concepts tag:#concept/glossary` | the curated concept map with RELATED_TO edges |
| `tag:#community/12` | one cluster, lessons and concepts together |
| `path:Lessons OR path:Libraries` | which lessons need torch / numpy / hono |
| `-path:Resources -path:Artifacts` | hide the leaf-heavy folders |

**2. The local graph** of the note you are reading (`Open local graph`, depth 1 to 3). On a lesson note at depth 2 you see its prerequisites, their prerequisites, the concepts and the papers. This is the single most useful view while studying.

**3. Bases** (`Bases/*.base`): tables over frontmatter. `Lessons.base` has views *All lessons*, *By community*, *Done*, *Build lessons*; `My Route.base` has *Not done yet*; `Concepts.base` splits glossary vs lesson-only and groups by category; `Resources.base` sorts papers by how many lessons cite them; `Libraries.base` and `Communities.base` do the same for those. Add your own view with the *+* button; it is saved in the `.base` file, which the exporter overwrites, so copy a base to `My Notes/` if you customise it heavily.

**4. Backlinks and search.** Every concept note lists *Taught in* with each lesson's own definition. Obsidian search understands the frontmatter: `[status:done]`, `[lesson_type:build]`, `[community:12]`, `tag:#stdlib-only`, `path:Lessons "flash attention"`.

**5. Properties.** Click any lesson's `status` in the properties panel and change it; the exporter keeps your value (it compares against `status_auto`). Set `status: skipped` for bridges you already know.

## What each note gives you

- **Lesson**: stated prerequisites with confidence, your bridges, the transitive chain, what builds on it, concepts (glossary vs lesson term, with the lesson's wording), artifacts, further reading with "also cited by N other lessons", learning paths, route position, libraries, community, and links to the lesson text (`Upstream/…`, rendered inside Obsidian), GitHub, the folder, your visual lesson and your artifacts.
- **Concept**: glossary definition, confusion, related concepts, every lesson that teaches it.
- **Community**: the lessons and concepts that cluster together, across phases, with a label made of its most connected concepts.
- **Phase / Track / Path**: ordered lesson tables with status.
- **Resource**: which lessons cite the paper, with each lesson's reason.
- **Library**: which lessons import it.

## Study loop with the vault

1. Open `Bases/My Route.base` → *Not done yet* → the next lesson.
2. In the lesson note, check *Bridges* and *Prerequisites*; open bridge notes and mark the ones you already know `status: skipped`.
3. Open the lesson text (`Upstream/…` link) and the *Concepts taught* list side by side.
4. Write the reflection below the marker. Link concepts with `[[Concepts/…]]` so your own notes join the graph.
5. Set `status: done` (or drop your work in `learning-artifacts/PP-LL-*/`) and run `./kg.sh all`.

## How Claude uses it

Claude does not open Obsidian; it reads the same graph. A project skill (`AI-Education/.claude/skills/kg/SKILL.md`) tells it to run the CLI before answering curriculum questions:

```bash
./kg.sh ask "what do I need before pre-training a mini GPT"   # scoped subgraph, no LLM
./kg.sh prereqs 10/04 --depth 1                                # bridges + stated prerequisites
./kg.sh concepts 10/04                                          # terms the lesson introduces
./kg.sh neighbors concept:kv-cache                              # every edge on a node
./kg.sh info 10/02                                              # status, route, doc path
```

`ask` is the equivalent of Graphify's `query`: it scores nodes against the words of the question, takes the best matches as seeds, and prints each seed with its neighbourhood grouped by edge type. Claude reads that instead of grepping 523 folders, then opens the one `docs/en.md` it needs. The vault notes are plain markdown too, so Claude can read a lesson note (and your reflection below the marker) directly when it helps.

## Keeping it current

```bash
cd ai-engineering-from-scratch && git pull && cd ../knowledge-graph && ./kg.sh all
```

Then skim `build/report.md`: counts, unparsed prerequisite fragments, unmatched key terms, communities. Your statuses and notes survive.
