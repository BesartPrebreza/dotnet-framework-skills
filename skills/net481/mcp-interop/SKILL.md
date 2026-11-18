---
name: mcp-interop
description: Use when exposing approved Framework application capabilities over MCP in a classic .NET Framework 4.8.1 solution.
---

# Mcp Interop

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Verify the MCP SDK target framework. Put the server in a supported sidecar runtime when needed and keep Framework integration behind a narrow authenticated API. Define tool schemas and server-side resource checks.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Contract-test authorized reads and denied cross-tenant requests. Record the checks that ran and identify prerequisites for any outstanding checks.
