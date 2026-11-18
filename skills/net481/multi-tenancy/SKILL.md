---
name: multi-tenancy
description: Use when adding tenant routing, isolation or tenant-aware background work in a classic .NET Framework 4.8.1 solution.
---

# Multi Tenancy

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Resolve tenant identity from trusted authorization context. Apply tenant scope to EF6, raw SQL, cache keys, workers and exports. Include tenant identity in unique keys where ownership requires it.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Test two tenants with overlapping local IDs in reads, writes and exports. Record the checks that ran and identify prerequisites for any outstanding checks.
