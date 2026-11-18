---
name: restartable-batch-imports
description: Use when building CSV, Excel or database batch imports in a classic .NET Framework 4.8.1 solution.
---

# Restartable Batch Imports

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Stage rows with a stable source key. Validate before promotion and commit one bounded chunk with its checkpoint. Render row-level error reports and treat retries as a normal path.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Stop after a committed chunk and restart without duplicating records. Record the checks that ran and identify prerequisites for any outstanding checks.
