---
name: nuget-dependency-review
description: Use when reviewing NuGet versions, advisories or dependency changes in a classic .NET Framework 4.8.1 solution.
---

# Nuget Dependency Review

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Inventory direct and transitive dependencies using the restore method configured for each project. Verify trusted feeds and package provenance, and review binding redirects after updates.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Build from clean package caches with the approved feeds. Record the checks that ran and identify prerequisites for any outstanding checks.
