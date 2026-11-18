---
name: browser-regression
description: Use when testing MVC or Web Forms journeys in a browser in a classic .NET Framework 4.8 solution.
---

# Browser Regression

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Use a separate compatible browser test runner when necessary. Seed a test environment and exercise actual UI navigation. Record browser details, traces and assertions with secrets removed.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Repeat the journey after a clean test-data reset. Record the checks that ran and identify prerequisites for any outstanding checks.
