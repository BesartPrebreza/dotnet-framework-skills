---
name: redis-cache-aside
description: Use when adding Redis caching to a Framework application in a classic .NET Framework 4.8.1 solution.
---

# Redis Cache Aside

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Confirm package and TFM compatibility. Reuse the connection multiplexer, scope keys by environment and tenant, and add TTL with jitter. Invalidate after database commit.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Verify stale cache behavior when invalidation or Redis connectivity fails. Record the checks that ran and identify prerequisites for any outstanding checks.
