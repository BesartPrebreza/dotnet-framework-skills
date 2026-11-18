---
name: problem-details-rfc9457
description: Use when standardizing System.Web API errors in a classic .NET Framework 4.8.1 solution.
---

# Problem Details Rfc9457

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Map application failures centrally through the configured Web API 2 error pipeline. Emit application/problem+json with a matching HTTP status and safe detail. Keep the established error contract where consumers rely on it.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Verify validation, authorization and unexpected server errors separately. Record the checks that ran and identify prerequisites for any outstanding checks.
