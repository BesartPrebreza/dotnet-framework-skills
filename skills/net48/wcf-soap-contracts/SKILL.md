---
name: wcf-soap-contracts
description: Use when editing WCF service contracts or generated proxies in a classic .NET Framework 4.8 solution.
---

# Wcf Soap Contracts

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Preserve operation names, namespaces, binding and published data member identities. Handle typed faults deliberately, and use an Abort fallback if a client Close fails.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Compare WSDL and run a legacy client contract test. Record the checks that ran and identify prerequisites for any outstanding checks.
