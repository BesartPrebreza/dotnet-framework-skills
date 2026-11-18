---
name: oauth-resource-server
description: Use when protecting a Framework API with an external identity provider in a classic .NET Framework 4.8.1 solution.
---

# Oauth Resource Server

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Check the provider metadata and token type. Map accepted scopes or roles deliberately and separate authenticated identity from permission to use a resource. Match existing challenges and status codes.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Verify anonymous, insufficient-scope and unauthorized-resource requests. Record the checks that ran and identify prerequisites for any outstanding checks.
