---
name: kg
description: Query the curriculum knowledge graph before answering questions about the AI Engineering from Scratch course. Use when the user asks what to learn before a lesson, where a concept is taught, which lessons share concepts or papers, which libraries a lesson uses, what is next on their route, or when planning or teaching a lesson. Prefer this over grepping the 523 lesson folders.
---

# The curriculum knowledge graph

`knowledge-graph/build/graph.json` holds the whole curriculum as a property graph:
phases, lessons, tracks, glossary concepts, lesson key terms, artifacts, papers,
learning paths, libraries, communities, plus the user's route, bridges and progress.
`knowledge-graph/vault/` is the same graph as an Obsidian vault (one note per node).

Run every command from `knowledge-graph/` with `./kg.sh <command>`. All of them are
instant and need no API.

| Question | Command |
|---|---|
| What must I know before lesson X? | `./kg.sh prereqs 10/04` (add `--depth 1` for direct only) |
| What builds on X? | `./kg.sh dependents 07/02` |
| Chain from X back to Y | `./kg.sh path 10/04 01/01` |
| Concepts a lesson teaches | `./kg.sh concepts 07/03` |
| Anything in plain language | `./kg.sh ask "which lessons cover the KV cache"` |
| Everything touching one node | `./kg.sh neighbors concept:kv-cache` or `neighbors 10/04` |
| Find nodes by name / alias / code symbol | `./kg.sh search "speculative"` (`--type lesson`) |
| Full dump of one node | `./kg.sh info 10/04`, `./kg.sh info concept:attention` |
| Where the user stands | `./kg.sh info 10/02` shows `status`, `route_order`, evidence |

Lesson refs are `PP/LL` (`10/04`). Node ids are `lesson:10/04`, `concept:kv-cache`,
`phase:10`, `library:python/torch`, `community:12`, `resource:arxiv:1706.03762`.

## How to use the answers

- `prereqs` output is layered by depth. Depth 1 = stated in the lesson header or a
  bridge from MY-LEARNING-PLAN.md; deeper = transitive. Mention confidence when an
  edge is `low` (track reference or override).
- Bridges (`BRIDGE` edges) are the user's own just-in-time prerequisites; treat them
  as the plan to follow before the lesson.
- `ask` returns a scoped subgraph: seeds plus neighbours grouped by edge type. Read
  it, do not paste it. Follow up with `info` on the interesting node.
- The lesson text itself lives at `ai-engineering-from-scratch/<path>/docs/en.md`
  (`info` prints `doc_path`). Read it only after the graph told you which lesson.
- Vault note for a lesson: `knowledge-graph/vault/Lessons/PP-LL Title.md`. Everything
  below the line `%% ── my notes ── %%` is the user's reflection; never overwrite it.

## After changes

If the upstream clone was pulled or MY-LEARNING-PLAN.md changed, rebuild first:
`./kg.sh all`, then read `knowledge-graph/build/report.md` (counts, unparsed
prerequisite fragments, unmatched key terms).

## Teaching a lesson with the graph

1. `./kg.sh prereqs PP/LL --depth 1` for the bridges and stated prerequisites.
2. `./kg.sh concepts PP/LL` for the terms the lesson will introduce; glossary ones
   have canonical definitions in `./kg.sh info concept:<id>`.
3. `./kg.sh info PP/LL` for `doc_path`, code files, quiz count, status.
4. Teach; when done, the user marks `status: done` in the vault note or drops work in
   `learning-artifacts/PP-LL-<slug>/`, and the next `./kg.sh all` records it.
