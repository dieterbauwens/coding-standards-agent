"""Domain models used by the standards repository."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class MarkdownSection:
    """A searchable section from a Markdown document."""

    heading: str
    content: str

    @property
    def markdown(self) -> str:
        """Return the complete Markdown representation of the section."""
        return f"{self.heading}\n\n{self.content}".strip()


@dataclass(frozen=True, slots=True)
class SectionMatch:
    """A scored Markdown section search result."""

    domain: str
    section: MarkdownSection
    score: int
