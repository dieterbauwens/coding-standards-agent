from pathlib import Path

import pytest

from coding_standards_mcp.standards_repository import (
    StandardsRepository,
    UnknownDomainError,
)


@pytest.fixture
def repository() -> StandardsRepository:
    standards_dir = Path(__file__).parents[1] / "standards"
    return StandardsRepository(standards_dir)


def test_lists_available_domains(repository: StandardsRepository) -> None:
    assert repository.list_domains() == [
        "ui_web_apps",
        "python_apps",
        "rest_apis",
        "mobile_apps",
    ]


@pytest.mark.parametrize("domain", ["ui_web_apps", "python_apps", "rest_apis", "mobile_apps"])
def test_loads_standards_files(repository: StandardsRepository, domain: str) -> None:
    document = repository.load_document(domain)

    assert document.startswith("# ")
    assert len(document) > 200


def test_retrieves_full_standard_document(repository: StandardsRepository) -> None:
    assert repository.get_standards("python_apps") == repository.load_document("python_apps")


def test_retrieves_topic_specific_sections(repository: StandardsRepository) -> None:
    standards = repository.get_standards("ui_web_apps", "accessibility keyboard")

    assert "## Accessibility" in standards
    assert "keyboard accessible" in standards
    assert "## Architecture" not in standards


def test_retrieves_flutter_platform_sections(repository: StandardsRepository) -> None:
    standards = repository.get_standards("mobile_apps", "platform Android iOS")

    assert "## Platform Integration" in standards
    assert "Android and iOS" in standards


def test_searches_across_domains(repository: StandardsRepository) -> None:
    results = repository.search("security secrets authentication")

    assert set(results) == {"ui_web_apps", "python_apps", "rest_apis", "mobile_apps"}
    assert all(matches for matches in results.values())
    assert any("Security" in match.section.heading for match in results["rest_apis"])


def test_rejects_unknown_domain(repository: StandardsRepository) -> None:
    with pytest.raises(UnknownDomainError, match="Unknown standards domain 'desktop_apps'"):
        repository.get_standards("desktop_apps")
