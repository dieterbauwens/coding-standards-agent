# Python Application Standards

These standards apply to Python services, command-line tools, libraries, and automation.

## Architecture

- Keep domain logic independent from frameworks, transports, and persistence details.
- Use explicit dependency injection at module boundaries instead of hidden global state.
- Prefer small cohesive modules and composition over deep inheritance hierarchies.
- Read configuration at application startup and validate it before serving work.

## Types and Interfaces

- Type all public functions, methods, and meaningful internal boundaries.
- Use dataclasses or Pydantic models for structured data instead of untyped dictionaries.
- Accept abstract collection interfaces when callers do not need a concrete container.
- Keep public interfaces narrow and document behavior, errors, and side effects.

## Error Handling

- Raise specific exceptions that describe the failed operation or invalid input.
- Catch exceptions only where they can be handled, translated, enriched, or logged once.
- Preserve exception context with `raise ... from error` when translating failures.
- Never silently discard failures; include useful context without leaking secrets.

## Security

- Validate untrusted input before using it in filesystem, subprocess, database, or template APIs.
- Pass subprocess arguments as a sequence and avoid shell execution unless strictly necessary.
- Load secrets from an approved secret store or environment, never from committed source.
- Use maintained cryptographic libraries and safe serialization formats.

## Testing

- Use pytest and follow Arrange, Act, Assert where it improves readability.
- Test observable behavior, boundary conditions, expected failures, and important integrations.
- Use temporary directories and dependency injection to isolate filesystem and external services.
- Keep unit tests fast and deterministic; mark slower integration tests clearly.
- Add a regression test whenever fixing a reproducible defect.

## Tooling and Dependencies

- Use Python 3.12 or newer and `uv` for environments, locking, and command execution.
- Use Ruff for formatting, import sorting, and linting.
- Keep runtime dependencies minimal, constrained intentionally, and represented in the lockfile.
- Run formatting, linting, type checks when configured, and tests in continuous integration.

## Observability

- Emit structured logs with operation and correlation identifiers at system boundaries.
- Record metrics for request volume, latency, failures, saturation, and domain-critical outcomes.
- Avoid sensitive data in logs, traces, exception messages, and metric labels.
- Make startup, shutdown, and background-task failures visible to operators.

