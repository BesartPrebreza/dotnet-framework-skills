---
name: framework-security-review
description: Use when reviewing authentication, authorization, cookies or request handling defensively in a classic .NET Framework 4.8.1 solution.
---

# Framework Security Review

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Trace inbound input to database, serialization and file boundaries. Review tenant and object permissions, MVC anti-forgery and IIS configuration. Record source locations and propose fixes with defensive regression checks.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Verify a protected state change rejects a request without a valid anti-forgery token. Record the checks that ran and identify prerequisites for any outstanding checks.
