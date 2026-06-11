"""MCP tool definitions for coding standards."""

from mcp.server.fastmcp import FastMCP

from coding_standards_mcp.standards_repository import StandardsRepository

mcp = FastMCP("coding-standards-mcp-server")
repository = StandardsRepository()


@mcp.tool()
def list_standard_domains() -> list[str]:
    """List the available coding standards domains."""
    return repository.list_domains()


@mcp.tool()
def get_coding_standards(domain: str, topic: str | None = None) -> str:
    """Get all standards for a domain or the sections most relevant to a topic."""
    return repository.get_standards(domain, topic)


@mcp.tool()
def search_coding_standards(query: str, domains: list[str] | None = None) -> str:
    """Search coding standards and return matching excerpts grouped by domain."""
    results = repository.search(query, domains)
    if not results:
        return f"# Coding standards search\n\nNo standards matched `{query}`."

    groups: list[str] = [f"# Coding standards search: {query}"]
    for domain, matches in results.items():
        excerpts = "\n\n".join(match.section.markdown for match in matches)
        groups.append(f"## Domain: `{domain}`\n\n{excerpts}")
    return "\n\n".join(groups)


def main() -> None:
    """Run the MCP server over standard input/output."""
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
