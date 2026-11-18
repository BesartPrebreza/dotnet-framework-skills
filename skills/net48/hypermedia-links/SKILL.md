---
name: hypermedia-links
description: Use when adding discoverable HTTP resource links in a classic .NET Framework 4.8 solution.
---

# Hypermedia Links

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Use named Web API routes and build links using the configured route helper. Respect reverse-proxy host rules and caller access before exposing action links.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Verify links resolve behind the deployed virtual directory. Record the checks that ran and identify prerequisites for any outstanding checks.
