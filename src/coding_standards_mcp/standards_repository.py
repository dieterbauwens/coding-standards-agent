"""Load and search Markdown coding standards."""

import re
from collections.abc import Iterable
from pathlib import Path

from coding_standards_mcp.models import MarkdownSection, SectionMatch

DOMAIN_FILES: dict[str, str] = {
    "ui_web_apps": "ui_web_apps.md",
    "python_apps": "python_apps.md",
    "rest_apis": "rest_apis.md",
    "mobile_apps": "mobile_apps.md",
}

_HEADING_PATTERN = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)
_WORD_PATTERN = re.compile(r"[a-z0-9]+")


class UnknownDomainError(ValueError):
    """Raised when a requested standards domain does not exist."""


class StandardsRepository:
    """Repository for standards stored as Markdown files on disk."""

    def __init__(self, standards_dir: Path | None = None) -> None:
        self._standards_dir = standards_dir or self._default_standards_dir()

    @staticmethod
    def _default_standards_dir() -> Path:
        return Path(__file__).resolve().parents[2] / "standards"

    def list_domains(self) -> list[str]:
        """Return all supported standards domains in stable order."""
        return list(DOMAIN_FILES)

    def load_document(self, domain: str) -> str:
        """Load the complete Markdown document for a domain."""
        path = self._path_for_domain(domain)
        try:
            return path.read_text(encoding="utf-8").strip()
        except FileNotFoundError as error:
            raise FileNotFoundError(
                f"Standards file for domain '{domain}' was not found: {path}"
            ) from error

    def get_standards(self, domain: str, topic: str | None = None) -> str:
        """Return a full document or the sections most relevant to a topic."""
        document = self.load_document(domain)
        if topic is None or not topic.strip():
            return document

        matches = self._rank_sections(domain, self.split_sections(document), topic)
        if not matches:
            return f"# No matching standards\n\nNo sections matched topic `{topic}` in `{domain}`."
        return "\n\n".join(match.section.markdown for match in matches[:3])

    def search(
        self,
        query: str,
        domains: Iterable[str] | None = None,
        *,
        limit_per_domain: int = 3,
    ) -> dict[str, list[SectionMatch]]:
        """Search standards and return top matches grouped by domain."""
        if not query.strip():
            raise ValueError("Search query must not be empty.")
        selected_domains = list(domains) if domains is not None else self.list_domains()
        self._validate_domains(selected_domains)

        results: dict[str, list[SectionMatch]] = {}
        for domain in selected_domains:
            sections = self.split_sections(self.load_document(domain))
            matches = self._rank_sections(domain, sections, query)
            if matches:
                results[domain] = matches[:limit_per_domain]
        return results

    @staticmethod
    def split_sections(document: str) -> list[MarkdownSection]:
        """Split a Markdown document into heading-led sections."""
        headings = list(_HEADING_PATTERN.finditer(document))
        if not headings:
            return [MarkdownSection(heading="# Document", content=document.strip())]

        sections: list[MarkdownSection] = []
        for index, heading in enumerate(headings):
            content_start = heading.end()
            content_end = (
                headings[index + 1].start() if index + 1 < len(headings) else len(document)
            )
            sections.append(
                MarkdownSection(
                    heading=heading.group(0).strip(),
                    content=document[content_start:content_end].strip(),
                )
            )
        return sections

    def _path_for_domain(self, domain: str) -> Path:
        try:
            filename = DOMAIN_FILES[domain]
        except KeyError as error:
            available = ", ".join(self.list_domains())
            raise UnknownDomainError(
                f"Unknown standards domain '{domain}'. Available domains: {available}."
            ) from error
        return self._standards_dir / filename

    def _validate_domains(self, domains: Iterable[str]) -> None:
        for domain in domains:
            self._path_for_domain(domain)

    @staticmethod
    def _rank_sections(
        domain: str,
        sections: Iterable[MarkdownSection],
        query: str,
    ) -> list[SectionMatch]:
        query_terms = _tokenize(query)
        matches: list[SectionMatch] = []
        for section in sections:
            heading_terms = _tokenize(section.heading)
            content_terms = _tokenize(section.content)
            score = 3 * len(query_terms & heading_terms) + len(query_terms & content_terms)
            if score > 0:
                matches.append(SectionMatch(domain=domain, section=section, score=score))
        return sorted(matches, key=lambda match: (-match.score, match.section.heading.lower()))


def _tokenize(value: str) -> set[str]:
    """Normalize text into searchable terms."""
    return set(_WORD_PATTERN.findall(value.lower().replace("_", " ")))
