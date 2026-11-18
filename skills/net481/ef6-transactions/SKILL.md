---
name: ef6-transactions
description: Use when coordinating writes, outbox records or multiple SaveChanges calls in a classic .NET Framework 4.8.1 solution.
---

# Ef6 Transactions

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Use a short DbContextTransaction when one context owns multiple writes. Enable async flow explicitly with TransactionScope where required. Review retry and distributed transaction behavior against the configured provider.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Force the second write to fail and verify atomic rollback. Record the checks that ran and identify prerequisites for any outstanding checks.
