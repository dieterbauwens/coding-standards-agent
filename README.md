# Dieter's Coding Standards MCP Server

`coding-standards-mcp-server` exposes centralized engineering standards to coding agents
through Model Context Protocol (MCP) tools. It includes standards for UI/web applications,
Python applications, REST APIs, and Flutter mobile applications targeting Android and iOS.

## Setup

Install [uv](https://docs.astral.sh/uv/), then create the environment and install dependencies:

```shell
uv sync
```

Run formatting, linting, and tests:

```shell
uv run ruff format .
uv run ruff check .
uv run pytest
```

## Running the server

The server uses MCP's standard input/output transport:

```shell
uv run coding-standards-mcp-server
```

Example client configuration (run the client from this project directory):

```json
{
  "mcpServers": {
    "coding-standards": {
      "command": "uv",
      "args": ["run", "coding-standards-mcp-server"]
    }
  }
}
```

When the client cannot set a working directory, add `--directory` before `run` and provide the
absolute path to this project.

## Tools

- `list_standard_domains()` lists `ui_web_apps`, `python_apps`, `rest_apis`, and `mobile_apps`.
- `get_coding_standards(domain, topic?)` returns a full document or its most relevant sections.
- `search_coding_standards(query, domains?)` searches selected or all domains and groups matching
  excerpts by domain.

Example calls:

```text
get_coding_standards(domain="python_apps", topic="testing")
get_coding_standards(domain="rest_apis", topic="error_handling")
get_coding_standards(domain="mobile_apps", topic="platform integration")
search_coding_standards(query="authentication secrets", domains=["ui_web_apps", "rest_apis"])
```

## Adding standards

1. Add or edit Markdown in `standards/`.
2. Structure guidance with descriptive `#`, `##`, and `###` headings; headings define searchable
   sections.
3. To add a domain, add its key and filename to `DOMAIN_FILES` in
   `src/coding_standards_mcp/standards_repository.py`.
4. Add repository and tool tests for the new domain.

Search is intentionally local and deterministic. It tokenizes the query, scores overlap in section
headings and bodies, and returns the highest-scoring sections.

## Hands on 🚀

When creating a new project, a local AGENTS.md-file is still required. This file should include instructions to use the Coding Standards Agent (the standard provider for general rules) in conjunction with repository-specific instructions.

Example `AGENTS.md` file for a random Python REST API application:

```markdown
# AGENTS.md

## Project Overview

This repository contains a Python REST API.

Before making changes, inspect the repository structure, configuration, and existing conventions. Prefer established project patterns over introducing new ones.

## Coding Standards

Personal coding standards are provided dynamically by the coding standards agent and are the source of truth for general engineering practices.

For every implementation or review:

1. Retrieve standards for the `python_apps` domain.
2. Retrieve standards for the `rest_apis` domain.
3. Request standards relevant to the specific task or topic.
4. Apply both sets of standards alongside this file.

Do not copy the retrieved standards into this repository. Query the standards agent again for each new task so that the latest version is used.

If standards conflict:

1. Explicit instructions from the user take precedence.
2. Repository-specific instructions in this file take precedence over general standards.
3. More specific coding standards take precedence over broader standards.
4. Ask for clarification when a material conflict remains.

## Repository Structure

- `src/`: application source code
- `tests/`: unit and integration tests
- `pyproject.toml`: dependencies and tool configuration
- `README.md`: setup and usage documentation

Keep domain logic independent from the HTTP framework and persistence layer. Follow the existing dependency-injection and module-boundary patterns.

## Development Workflow

Install dependencies and run the application using the commands documented in `README.md` and `pyproject.toml`.

Before completing a change, run:

```shell
pytest
ruff check .
ruff format --check .
mypy src
```