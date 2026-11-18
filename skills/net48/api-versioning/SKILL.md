---
name: api-versioning
description: Use when adding or deprecating an HTTP API version in Web API 2 in a classic .NET Framework 4.8 solution.
---

# Api Versioning

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Preserve existing route matches and introduce explicit version routes. Test old clients, disambiguate controller resolution and document deprecation and migration paths.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Run both versions with the same resource and verify their contracts independently. Record the checks that ran and identify prerequisites for any outstanding checks.
