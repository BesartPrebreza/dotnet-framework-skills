---
name: audit-logging
description: Use when recording security-sensitive operations or business approvals in a classic .NET Framework 4.8.1 solution.
---

# Audit Logging

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Capture actor, action, resource, outcome and correlation ID. Exclude secrets and personal payloads. Use durable records when required by the operation and define failure behavior.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Verify failed and successful actions emit appropriately redacted events. Record the checks that ran and identify prerequisites for any outstanding checks.
