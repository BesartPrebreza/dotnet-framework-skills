---
name: owin-jwt-validation
description: Use when configuring bearer tokens in OWIN or Web API 2 in a classic .NET Framework 4.8.1 solution.
---

# Owin Jwt Validation

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Inspect existing authentication middleware and pipeline order. Validate issuer, audience, expiry and trusted signature keys. Keep resource authorization in the application boundary.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Verify wrong issuer, audience and expired tokens are rejected. Record the checks that ran and identify prerequisites for any outstanding checks.
