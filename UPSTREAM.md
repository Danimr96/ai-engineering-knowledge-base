# Upstream curriculum

`ai-engineering-from-scratch/` is an unmodified, vendored copy of:

- Repository: https://github.com/rohitg00/ai-engineering-from-scratch
- Site: https://aiengineeringfromscratch.com
- Author: Rohit Ghumare
- Licence: MIT (see `ai-engineering-from-scratch/LICENSE`)
- Commit: f6721a0167315118236ed2022ac11936831cce46

It is vendored, not a submodule, so that a plain clone or ZIP download is complete and works offline.

## Rules

- Treat the folder as read-only. Nothing in `knowledge-graph/` writes into it.
- Keep its `LICENSE` file with any copy you redistribute.
- Put your own lessons, notes and overrides outside it, or they will be lost on the next update.

## Updating

```bash
scripts/update-upstream.sh          # latest main
scripts/update-upstream.sh v1.2.0   # a tag or branch
cd knowledge-graph && ./kg.sh all && uv run pytest
```

The script replaces the folder with the requested upstream version, updates the commit line above and stages the result. Review the diff, rebuild the graph, then commit.
