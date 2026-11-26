#!/bin/sh
# Replace the vendored curriculum with a given upstream version (default: main),
# record the commit in UPSTREAM.md and stage the result for review.
set -eu

REF="${1:-main}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="$ROOT/ai-engineering-from-scratch"
URL="https://github.com/rohitg00/ai-engineering-from-scratch.git"

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

git clone --quiet --depth 1 --branch "$REF" "$URL" "$TMP/upstream"
SHA="$(git -C "$TMP/upstream" rev-parse HEAD)"

# Mirror the upstream tree. Local-only folders are left alone.
rsync -a --delete \
  --exclude '.git' --exclude '.git.nested-backup' --exclude '.venv' \
  "$TMP/upstream/" "$DEST/"

sed -i.bak "s/^- Commit: .*/- Commit: $SHA/" "$ROOT/UPSTREAM.md"
rm -f "$ROOT/UPSTREAM.md.bak"

cd "$ROOT"
git add -A ai-engineering-from-scratch UPSTREAM.md
# Upstream tracks these although its own .gitignore excludes them.
git add -f ai-engineering-from-scratch/.claude/skills

echo "Vendored upstream at $SHA."
echo "Next: git diff --cached --stat, then cd knowledge-graph && ./kg.sh all && uv run pytest"
