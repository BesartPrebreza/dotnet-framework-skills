---
name: msbuild-solutions
description: Use when changing solutions, project references or shared build settings in a classic .NET Framework 4.8.1 solution.
---

# Msbuild Solutions

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Inspect old-style project imports and explicit Compile items. Keep dependency direction acyclic. Review Directory.Build.props import behavior and whether each project uses packages.config or PackageReference.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Build the solution from a clean checkout and inspect the resolved references. Record the checks that ran and identify prerequisites for any outstanding checks.
