# UI and Web Application Standards

These standards apply to browser-based user interfaces and web applications.

## Architecture

- Organize code by product feature when features have distinct behavior and ownership.
- Keep rendering, state transitions, data access, and domain rules in clearly separated modules.
- Prefer platform capabilities and the existing design system before adding dependencies.
- Keep shared components focused on stable, reusable behavior rather than speculative reuse.

## Accessibility

- Meet WCAG 2.2 AA for user-facing experiences.
- Use semantic HTML and native controls before adding ARIA roles.
- Ensure every interaction is keyboard accessible and has a visible focus indicator.
- Associate form controls with labels and announce validation errors to assistive technology.
- Do not use color alone to communicate state, and respect reduced-motion preferences.

## Security

- Treat all browser input and remote content as untrusted.
- Prevent cross-site scripting through contextual escaping; avoid unsafe HTML injection APIs.
- Keep credentials, private keys, and privileged authorization decisions out of client code.
- Use secure, HTTP-only, same-site cookies for session identifiers where applicable.
- Pin dependencies with the project lockfile and review security updates promptly.

## Testing

- Test user-visible behavior instead of component implementation details.
- Cover critical journeys with integration or end-to-end tests, including failure states.
- Add accessibility checks, while retaining manual keyboard and screen-reader verification.
- Keep tests deterministic by controlling time, network responses, and generated identifiers.

## Performance

- Define measurable performance budgets for initial load and important interactions.
- Avoid unnecessary JavaScript, render work, network waterfalls, and layout shifts.
- Load non-critical code and media lazily without delaying primary content.
- Measure production behavior with appropriate real-user and synthetic monitoring.

## Error Handling

- Present actionable messages that explain what failed and what the user can do next.
- Preserve user input when submission fails and prevent duplicate operations during retries.
- Log diagnostic context without exposing secrets or sensitive personal information.
- Provide deliberate loading, empty, offline, partial-data, and permission-denied states.

