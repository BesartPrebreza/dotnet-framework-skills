---
name: bounded-retries
description: Use when handling transient I/O or database failures in a classic .NET Framework 4.8.1 solution.
---

# Bounded Retries

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Follow the configured provider retry policy and classify failures. Use capped backoff and a total deadline. Require replay safety for retries crossing transaction boundaries.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Test exhausted retries and cancellation during delay. Record the checks that ran and identify prerequisites for any outstanding checks.
