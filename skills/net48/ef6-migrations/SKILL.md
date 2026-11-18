---
name: ef6-migrations
description: Use when changing an EF6 Code First database schema in a classic .NET Framework 4.8 solution.
---

# Ef6 Migrations

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Confirm EF6 migration ownership and baseline. Stage changes that affect existing rows, backfill in bounded batches and review generated scripts in deployment order.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Apply the script to a restored database and verify persisted data. Record the checks that ran and identify prerequisites for any outstanding checks.
