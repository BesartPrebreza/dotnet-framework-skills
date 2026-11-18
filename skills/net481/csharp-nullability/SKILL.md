---
name: csharp-nullability
description: Use when handling nullability in C# Framework code in a classic .NET Framework 4.8.1 solution.
---

# Csharp Nullability

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Read LangVersion and compiler settings. For C# 7.3-compatible code use explicit guards and materialize nullable values safely. Introduce nullable reference annotations only when the project compiler and tooling support them.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Test omitted JSON fields, database nulls and empty collections. Record the checks that ran and identify prerequisites for any outstanding checks.
