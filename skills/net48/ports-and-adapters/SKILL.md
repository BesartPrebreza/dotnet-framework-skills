---
name: ports-and-adapters
description: Use when extracting business logic from System.Web, WinForms or WCF in a classic .NET Framework 4.8 solution.
---

# Ports And Adapters

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Define ports in the application assembly for external dependencies. Implement adapters at the edge. Compose concrete dependencies in the host and keep infrastructure references outward.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Build the application project independently of host assemblies. Record the checks that ran and identify prerequisites for any outstanding checks.
