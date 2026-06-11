# REST API Standards

These standards apply to HTTP APIs that model resources and exchange structured representations.

## API Design

- Model stable resource nouns in paths and use HTTP methods to express operations.
- Use plural, lowercase resource names and consistent path, query, and field naming.
- Keep request and response schemas explicit, documented, and backward compatible.
- Use pagination, filtering, sorting, and field selection consistently across collections.
- Publish an OpenAPI description and validate examples against the implementation.

## HTTP Semantics

- Use status codes according to their standardized meaning.
- Make safe operations read-only and design idempotent operations to tolerate retries.
- Use content negotiation deliberately and return an accurate `Content-Type`.
- Support conditional requests or version checks when concurrent updates can conflict.

## Error Handling

- Return a consistent machine-readable error document, preferably RFC 9457 Problem Details.
- Include a stable error type or code, a human-readable summary, and a correlation identifier.
- Report field-level validation problems without echoing secrets or unsafe input.
- Do not expose stack traces, database details, internal hostnames, or implementation internals.
- Distinguish authentication, authorization, missing resource, conflict, and validation failures.

## Security

- Authenticate requests using an approved, current protocol and authorize every protected action.
- Enforce authorization against the requested resource, not only the route or user role.
- Validate request size, media type, schema, identifiers, and allowed values.
- Apply TLS, rate limits, abuse controls, and restrictive cross-origin policies as appropriate.
- Keep credentials out of URLs because URLs commonly appear in logs and browser history.

## Versioning and Compatibility

- Prefer additive schema evolution and tolerant readers over frequent version changes.
- Do not remove fields, narrow accepted inputs, or change field meaning without a versioned plan.
- Publish deprecation notices, migration guidance, and a retirement date before removal.
- Use contract tests to protect behavior relied on by consumers.

## Testing

- Test the API through its HTTP boundary for success, validation, authorization, and failure cases.
- Verify status codes, headers, response schemas, pagination, and idempotency behavior.
- Add consumer or schema compatibility tests for externally used APIs.
- Test rate limiting and security controls without making the suite timing-dependent.

## Observability

- Propagate correlation and trace identifiers across service boundaries.
- Log method, route template, status, duration, and outcome without logging sensitive payloads.
- Measure latency distributions, traffic, error rates, and saturation by stable route templates.
- Provide health and readiness signals that reflect actual dependency requirements.

