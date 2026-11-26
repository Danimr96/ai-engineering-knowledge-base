#!/bin/sh
# Thin launcher so you can type `./kg.sh build` instead of
# `uv run python -m kg.cli build`. It always runs from the project folder.
cd "$(dirname "$0")" && exec uv run python -m kg.cli "$@"
