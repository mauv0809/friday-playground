# friday-playground

Practice repository for **Friday**, a sandboxed background coding agent.

- Python package in `src/playground`, tests in `tests/`
- Toolchain pinned in `mise.toml`
- Run locally: `uv sync && uv run ruff check . && uv run pytest`
- CI (`.github/workflows/ci.yml`) must pass before anything merges to `main`

Friday works on branches and opens draft PRs. A human merges.
