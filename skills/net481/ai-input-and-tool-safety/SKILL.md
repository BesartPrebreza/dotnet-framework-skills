---
name: ai-input-and-tool-safety
description: Use when reviewing AI prompts, retrieved data or tool permissions in a classic .NET Framework 4.8.1 solution.
---

# Ai Input And Tool Safety

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Treat input and retrieved records as data. Enforce tool and resource authorization in server code, validate parameters and restrict secret access. Bound tool calls and record redacted outcomes.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Test that untrusted content cannot grant access to another tenant. Record the checks that ran and identify prerequisites for any outstanding checks.
