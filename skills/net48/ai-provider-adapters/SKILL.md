---
name: ai-provider-adapters
description: Use when adding AI features to a Framework application in a classic .NET Framework 4.8 solution.
---

# Ai Provider Adapters

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Place the provider behind an application interface. Use an approved HTTP API or a separate supported runtime when SDK targets are incompatible. Set deadlines and validate structured responses before use.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Test malformed output, provider outage and cancellation. Record the checks that ran and identify prerequisites for any outstanding checks.
