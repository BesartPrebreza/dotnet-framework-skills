---
name: domain-driven-design
description: Use when modeling aggregates, value objects or domain events in a classic .NET Framework 4.8 solution.
---

# Domain Driven Design

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Make invariants explicit inside aggregate operations. Store persistence mapping in EF6 configuration, and write external messages through a durable outbox inside the same database transaction.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Test allocation above remaining stock and confirm state is preserved. Record the checks that ran and identify prerequisites for any outstanding checks.
