---
name: framework-testing
description: Use when adding unit, integration or database tests in a classic .NET Framework 4.8.1 solution.
---

# Framework Testing

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Use the existing test runner on Windows. Unit-test domain behavior and exercise System.Web routes and SQL Server behavior at boundaries. Keep fixture data deterministic and isolate database state.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Run tests twice and verify they do not depend on execution order. Record the checks that ran and identify prerequisites for any outstanding checks.
