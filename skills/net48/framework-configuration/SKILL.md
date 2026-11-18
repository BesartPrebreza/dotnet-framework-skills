---
name: framework-configuration
description: Use when editing app.config, web.config, transforms, or typed settings in a classic .NET Framework 4.8 solution.
---

# Framework Configuration

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Read settings once at startup and parse with invariant culture. Validate required keys before initializing dependent services. Use host-provided secret storage and explicit transform checks.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Reject zero, negative and malformed timeout values. Record the checks that ran and identify prerequisites for any outstanding checks.
