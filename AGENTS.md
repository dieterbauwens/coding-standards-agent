# Repository Guidelines

- Use Python 3.12 or newer and manage dependencies with `uv`.
- Run `uv run ruff format .` and `uv run ruff check .` before completing changes.
- Run tests with `uv run pytest` and add focused tests for behavior changes.
- Add type hints to all functions, methods, and meaningful variables.
- Keep MCP tool functions thin. Input validation, document loading, ranking, and search logic belong
  in repository or model classes.
- Keep functions small, deterministic, and independently testable.
- Store coding standards as Markdown under `standards/`; do not embed standards in Python code.
- Do not introduce absolute filesystem paths. Resolve bundled standards relative to the package.

