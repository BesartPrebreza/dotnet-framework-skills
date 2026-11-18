---
name: idempotency-patterns
description: Use when making retried HTTP writes safe in a classic .NET Framework 4.8 solution.
---

# Idempotency Patterns

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Scope keys by caller and operation, persist request hashes, and atomically commit business writes with the replayable response. Use a database uniqueness constraint for races.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Send two concurrent requests and assert one business effect. Record the checks that ran and identify prerequisites for any outstanding checks.
