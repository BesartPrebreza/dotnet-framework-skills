---
name: ef6-data-access
description: Use when writing EF6 entities, LINQ projections, paging or updates in a classic .NET Framework 4.8.1 solution.
---

# Ef6 Data Access

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Use the existing EF6 mapping approach and keep DbContext per unit of work. Project read-only queries before materialization. Handle optimistic concurrency with a configured token and explicit conflict policy.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Inspect generated SQL for server-side predicates and stable ordering. Record the checks that ran and identify prerequisites for any outstanding checks.
