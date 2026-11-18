---
name: layered-architecture
description: Use when changing controllers, UI forms, data access or business services in a classic .NET Framework 4.8 solution.
---

# Layered Architecture

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Inspect existing project references. Keep transport and UI adapters thin and preserve application transaction ownership. Return DTOs from boundaries and keep data access queryable inside the persistence layer.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Confirm UI and API adapters share the application use case. Record the checks that ran and identify prerequisites for any outstanding checks.
