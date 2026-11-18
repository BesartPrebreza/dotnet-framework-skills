---
name: background-execution
description: Use when adding background execution to System.Web or a Windows Service in a classic .NET Framework 4.8.1 solution.
---

# Background Execution

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Use a durable queue for work that must survive IIS recycling. Use scoped cancellation and bounded worker concurrency. Give each worker iteration its own context and explicit exception handling.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Restart the worker between claim and completion and verify recovery. Record the checks that ran and identify prerequisites for any outstanding checks.
