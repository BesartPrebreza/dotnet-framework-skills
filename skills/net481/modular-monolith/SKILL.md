---
name: modular-monolith
description: Use when defining module boundaries within a single application in a classic .NET Framework 4.8.1 solution.
---

# Modular Monolith

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Expose contracts at module boundaries and restrict direct access to module data. Add assembly dependency checks and document ownership of shared transactions.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Verify Order code does not depend on Inventory.Persistence. Record the checks that ran and identify prerequisites for any outstanding checks.
