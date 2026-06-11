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
