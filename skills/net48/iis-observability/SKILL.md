---
name: iis-observability
description: Use when adding logging, health checks, or operational telemetry in a classic .NET Framework 4.8 solution.
---

# Iis Observability

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Correlate structured application logs with IIS request data. Keep readiness responses bounded and omit sensitive diagnostics. Verify telemetry library compatibility and worker lifecycle behavior.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Simulate database unavailability and verify the application reports readiness correctly. Record the checks that ran and identify prerequisites for any outstanding checks.
