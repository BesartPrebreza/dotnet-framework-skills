---
name: async-request-pipelines
description: Use when adding async Web API, MVC or streamed response handling in a classic .NET Framework 4.8 solution.
---

# Async Request Pipelines

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Propagate cancellation to I/O, return Task from async request actions and bound buffering. Keep System.Web request context requirements explicit at the controller boundary.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Test disconnected requests and bounded execution under load. Record the checks that ran and identify prerequisites for any outstanding checks.
