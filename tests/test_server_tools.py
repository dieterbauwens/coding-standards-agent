import pytest

from coding_standards_mcp.server import (
    get_coding_standards,
    list_standard_domains,
    search_coding_standards,
)
from coding_standards_mcp.standards_repository import UnknownDomainError


def test_list_standard_domains_tool() -> None:
    assert list_standard_domains() == [
        "ui_web_apps",
        "python_apps",
        "rest_apis",
        "mobile_apps",
    ]


def test_get_coding_standards_tool() -> None:
    result = get_coding_standards("rest_apis", "error handling")

    assert "## Error Handling" in result
    assert "Problem Details" in result


def test_search_coding_standards_tool_groups_by_domain() -> None:
    result = search_coding_standards("testing deterministic", ["python_apps", "ui_web_apps"])

    assert "## Domain: `python_apps`" in result
    assert "## Domain: `ui_web_apps`" in result
    assert "## Testing" in result


def test_get_mobile_coding_standards_tool() -> None:
    result = get_coding_standards("mobile_apps", "accessibility semantics")

    assert "## Accessibility" in result
    assert "Semantics" in result


def test_get_coding_standards_tool_rejects_unknown_domain() -> None:
    with pytest.raises(UnknownDomainError, match="Available domains"):
        get_coding_standards("desktop_apps")
