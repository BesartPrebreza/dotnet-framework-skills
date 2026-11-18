---
name: framework-scaffolding
description: Use when creating a Windows-hosted .NET Framework solution or adding a project in a classic .NET Framework 4.8 solution.
---

# Framework Scaffolding

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Inspect installed Visual Studio workloads, targeting packs and supported operating systems. Pick desktop, System.Web, WCF or Windows Service hosting before generating project files. Restore, build and smoke-test the selected host.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Verify a clean checkout builds on Windows. Record the checks that ran and identify prerequisites for any outstanding checks.
