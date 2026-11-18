---
name: framework-verification
description: Use when building, testing, or preparing a release for .NET Framework in a classic .NET Framework 4.8.1 solution.
---

# Framework Verification

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Read repository build commands and record SDK, MSBuild and targeting pack versions. Build changed configurations and run the test suite. Report commands, exit codes and gates that require another environment.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Confirm the Release build uses the expected target framework. Record the checks that ran and identify prerequisites for any outstanding checks.
