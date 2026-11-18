---
name: sql-server-query-review
description: Use when optimizing SQL Server reporting queries, views or procedures in a classic .NET Framework 4.8.1 solution.
---

# Sql Server Query Review

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Define row grain and join cardinality before optimizing. Parameterize filters, compare result shape and totals, then measure the actual plan and logical reads on representative data.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Check warehouse coverage and totals before and after the change. Record the checks that ran and identify prerequisites for any outstanding checks.
