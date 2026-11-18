---
name: openapi-contracts
description: Use when maintaining OpenAPI specifications or generating C# clients in a classic .NET Framework 4.8.1 solution.
---

# Openapi Contracts

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Treat the contract as a versioned artifact. Confirm generator compatibility with the consumer TFM and serializer. Diff operation IDs, required fields and nullable behavior before regeneration.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Regenerate twice and check for a clean second diff. Record the checks that ran and identify prerequisites for any outstanding checks.
