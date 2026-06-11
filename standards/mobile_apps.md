# Flutter Mobile Application Standards

These standards apply to Flutter applications that share one Dart codebase across Android and iOS.
Platform-specific behavior is allowed when required for native conventions, capabilities, security,
or a better user experience.

## Architecture

- Organize code by product feature, with presentation, application, domain, and data concerns kept
  at clear boundaries.
- Keep business rules and use cases independent from Flutter widgets, plugins, and platform APIs.
- Use explicit dependency injection and avoid service locators or mutable global state.
- Choose one state-management approach for the application and apply it consistently.
- Keep widgets small and focused; extract behavior into testable classes rather than large widget
  build methods.
- Model navigation, deep links, authentication state, and app lifecycle transitions explicitly.

## Dart and Flutter Practices

- Use the current stable Flutter and Dart releases approved by the project and pin them in CI.
- Enable sound null safety and strict static analysis; do not suppress analyzer rules without a
  documented reason.
- Prefer immutable data and `const` widgets and constructors where they are meaningful.
- Use generated, typed models for structured API data instead of passing dynamic maps through the
  application.
- Dispose controllers, subscriptions, focus nodes, and other owned resources deterministically.
- Avoid performing network, database, or expensive computation directly in widget build methods.

## User Interface and Design

- Use a shared design system for color, typography, spacing, shapes, icons, and reusable components.
- Build adaptive layouts that work across supported screen sizes, orientations, text scales, and
  safe areas.
- Respect Material conventions on Android and Apple Human Interface Guidelines on iOS where users
  expect platform-native behavior.
- Provide deliberate loading, empty, offline, partial-data, permission-denied, and error states.
- Preserve user input across rotation, temporary navigation, and recoverable failures.
- Do not rely on color, gestures, or animation alone to communicate meaning or provide an action.

## Platform Integration

- Verify behavior on both Android and iOS; a shared Flutter codebase does not guarantee identical
  platform behavior.
- Isolate platform channels, native SDK calls, and plugin wrappers behind typed Dart interfaces.
- Minimize custom Kotlin, Java, Swift, and Objective-C code and test each native integration on its
  target platform.
- Request permissions only when a feature needs them and explain their purpose before the system
  prompt when appropriate.
- Handle denied, permanently denied, restricted, and unavailable permission states without loops or
  dead ends.
- Test deep links, universal links, app links, background execution, notifications, and lifecycle
  restoration on real Android and iOS devices when those capabilities are used.
- Keep Android manifests, Gradle configuration, iOS entitlements, and privacy declarations minimal
  and aligned with actual application behavior.

## Accessibility

- Target WCAG 2.2 AA and follow Android and iOS accessibility guidance.
- Use semantic widgets and `Semantics` labels so controls, state, headings, and validation errors are
  meaningful to TalkBack and VoiceOver.
- Ensure interactive targets are large enough, keyboard and switch accessible where applicable,
  and ordered logically for assistive technology.
- Support system text scaling without clipping, overlap, hidden controls, or blocked navigation.
- Maintain sufficient color contrast and honor reduced-motion, bold-text, and other relevant system
  accessibility settings.
- Test critical journeys manually with TalkBack on Android and VoiceOver on iOS.

## Security and Privacy

- Treat all local input, deep-link data, clipboard content, files, and server responses as untrusted.
- Store tokens and sensitive values with platform-backed secure storage; do not place secrets in
  source code, assets, logs, shared preferences, or ordinary local databases.
- Enforce authorization on the server. Client-side route guards and hidden controls are not security
  boundaries.
- Use TLS for network traffic and do not bypass certificate validation in production builds.
- Redact credentials, personal data, and sensitive payloads from logs, analytics, crash reports, and
  screenshots.
- Collect only necessary data, obtain required consent, and provide platform-appropriate privacy
  disclosures and account/data deletion behavior.
- Review Flutter packages and native SDKs for maintenance, permissions, data collection, and known
  vulnerabilities before adoption.

## Networking and Data

- Access remote services through typed clients with explicit timeouts, cancellation, and consistent
  error translation.
- Retry only transient, idempotent operations, using bounded exponential backoff with jitter.
- Design offline behavior deliberately and define which source wins when local and remote data
  conflict.
- Version persisted data and test database or preference migrations before release.
- Avoid blocking application startup on non-critical network requests.
- Show stale or partial data honestly and give users a clear way to retry failed synchronization.

## Error Handling

- Translate technical failures into actionable messages without exposing implementation details.
- Distinguish validation, connectivity, timeout, authentication, authorization, server, storage, and
  unexpected failures.
- Prevent duplicate submissions while an operation is in progress and make retry behavior explicit.
- Preserve useful diagnostic context for observability while excluding secrets and personal data.
- Capture unhandled Flutter framework, Dart isolate, and platform errors through the approved crash
  reporting path.

## Testing

- Use unit tests for domain rules, state transitions, validation, serialization, and error mapping.
- Use widget tests for rendering, interaction, navigation, accessibility semantics, and key visual
  states.
- Use integration tests for critical journeys across storage, networking, plugins, and application
  lifecycle behavior.
- Run critical integration tests on both Android and iOS; include representative real-device testing
  before release.
- Keep tests deterministic by controlling time, networking, generated identifiers, and platform
  services.
- Add golden tests selectively for stable design-system components and important layouts across
  relevant screen sizes and text scales.

## Performance

- Define budgets for startup, frame rendering, memory, application size, and critical interactions.
- Profile in release or profile mode on representative lower-end physical devices.
- Avoid unnecessary widget rebuilds, synchronous work on the UI isolate, oversized images, and
  unbounded lists.
- Move CPU-intensive work off the UI isolate when profiling shows it affects responsiveness.
- Measure scrolling and animation for dropped frames and verify memory is released after navigation.
- Optimize only from measurements and retain tests or monitoring for important regressions.

## Observability

- Record structured diagnostics for application startup, API outcomes, synchronization, and critical
  user journeys.
- Include release version, build number, platform, and non-sensitive correlation identifiers in
  crash and error reports.
- Use analytics events with stable names and documented properties; avoid collecting raw sensitive
  values.
- Monitor crashes, app-not-responding events, startup time, failed requests, and release adoption by
  platform and version.

## Build and Release

- Produce Android and iOS builds from reproducible CI workflows using reviewed signing and secret
  management.
- Use distinct application identifiers, configuration, and backend environments for development,
  testing, and production.
- Keep build numbers monotonic and make the source revision traceable from each distributed build.
- Run formatting, static analysis, tests, and platform build checks before publishing artifacts.
- Validate store metadata, screenshots, privacy declarations, permissions, and release notes for
  both Google Play and the Apple App Store.
- Roll out risky releases gradually when the stores and product constraints permit, and maintain a
  tested rollback or remediation plan.

