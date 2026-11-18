---
name: ai-observability
description: Use when monitoring model latency, usage and failures in a classic .NET Framework 4.8 solution.
---

# Ai Observability

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Capture model and provider identifiers, duration and failure class. Record tokens when the provider has reported them, and keep prompt text out of telemetry by default.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Verify that failures emit metrics without logging request content. Record the checks that ran and identify prerequisites for any outstanding checks.
