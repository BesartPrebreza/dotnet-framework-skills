---
name: http-client-adapters
description: Use when calling upstream HTTP APIs from Framework projects in a classic .NET Framework 4.8 solution.
---

# Http Client Adapters

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Preserve configured proxy and TLS behavior. Manage HttpClient lifetime using an existing compatible factory or long-lived clients with reviewed connection behavior. Pass cancellation and dispose response objects.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Simulate timeouts and transient upstream responses. Record the checks that ran and identify prerequisites for any outstanding checks.
